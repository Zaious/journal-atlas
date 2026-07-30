"""Abuse and cost controls for the public demo.

The demo runs on a key the maintainer pays for, and every request to
`/api/recommend` is two LLM calls carrying attacker-controllable text. Without
limits it is a free LLM proxy with an unbounded bill attached.

Three controls, deliberately layered, because each one fails differently:

1. **Input size caps** (in `main.py`, on the Pydantic models). The first line of
   defence and the only one that bounds the cost of a *single* request. Rate
   limits are useless if one request can carry 500 KB into the prompt.

2. **Per-client rate limits.** Stops casual repeated use. Weak by construction:
   IPs are shared behind NAT and cheap behind a VPN, so this is friction, not
   a wall.

3. **A global daily cap.** The only control that actually bounds the bill,
   because it holds no matter how the requests are distributed across clients.
   When it trips the demo stops calling the provider and says so — the
   knowledge base is public and the skill runs locally, so a user who hits it
   has somewhere to go.

Deliberately in-memory: the demo's design property is that it persists nothing
between requests, and adding a datastore purely to count requests would trade
that away. The cost is real and is documented in `demo/README.md` — counters
reset when the process restarts, and each worker holds its own, so the true
ceiling is `GLOBAL_DAILY_LIMIT x workers`. Run one worker, or move the counter
to Redis, if that matters.
"""

from __future__ import annotations

import os
import threading
import time
from collections import deque

HOUR = 3600
DAY = 86400


def _int_env(name: str, default: int) -> int:
    raw = os.environ.get(name)
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError:
        return default


class RateLimiter:
    """Sliding-window request counting, per client and globally.

    Sliding rather than fixed-window because a fixed window lets a client spend
    its whole daily allowance twice across a boundary a second apart, which is
    exactly the shape an abusive script produces.
    """

    def __init__(
        self,
        per_hour: int | None = None,
        per_day: int | None = None,
        global_per_day: int | None = None,
    ) -> None:
        self.per_hour = per_hour if per_hour is not None else _int_env("RATE_LIMIT_PER_HOUR", 10)
        self.per_day = per_day if per_day is not None else _int_env("RATE_LIMIT_PER_DAY", 30)
        self.global_per_day = (
            global_per_day if global_per_day is not None
            else _int_env("GLOBAL_DAILY_LIMIT", 250)
        )
        self._clients: dict[str, deque[float]] = {}
        self._global: deque[float] = deque()
        self._lock = threading.Lock()

    def _prune(self, stamps: deque[float], now: float, window: int) -> None:
        while stamps and stamps[0] <= now - window:
            stamps.popleft()

    def check(self, client_key: str, now: float | None = None) -> str | None:
        """Record a request and return None, or a message explaining the refusal.

        Nothing is recorded when the request is refused: a client that keeps
        hammering a closed door should not push its own reopening further away,
        and neither should it burn the global budget it was just denied.
        """
        now = time.time() if now is None else now
        with self._lock:
            self._prune(self._global, now, DAY)
            if self.global_per_day and len(self._global) >= self.global_per_day:
                return (
                    "This demo has used up its daily budget of "
                    f"{self.global_per_day} requests. It runs on one person's API key. "
                    "The knowledge base and the skill are open source and run locally "
                    "with no such limit — see the repository README."
                )

            stamps = self._clients.setdefault(client_key, deque())
            self._prune(stamps, now, DAY)

            if self.per_day and len(stamps) >= self.per_day:
                return (
                    f"Daily limit reached ({self.per_day} requests). "
                    "Install the skill to run this locally without limits."
                )

            recent = sum(1 for s in stamps if s > now - HOUR)
            if self.per_hour and recent >= self.per_hour:
                oldest_in_hour = next(s for s in stamps if s > now - HOUR)
                wait_min = max(1, int((oldest_in_hour + HOUR - now) / 60) + 1)
                return (
                    f"Hourly limit reached ({self.per_hour} requests). "
                    f"Try again in about {wait_min} minutes, or install the skill "
                    "to run this locally without limits."
                )

            stamps.append(now)
            self._global.append(now)
            # Bound memory: without this, one request per unique IP is a slow
            # leak for as long as the process lives.
            if len(self._clients) > 10_000:
                for key in [k for k, v in self._clients.items() if not v]:
                    del self._clients[key]
            return None

    def snapshot(self, now: float | None = None) -> dict:
        """Current usage, for /api/health. No client keys — those are IPs.

        Takes the same injectable clock as `check`; a method that reads the
        wall clock while its sibling accepts one cannot be reasoned about at
        any instant that is not now.
        """
        now = time.time() if now is None else now
        with self._lock:
            self._prune(self._global, now, DAY)
            return {
                "global_used_today": len(self._global),
                "global_daily_limit": self.global_per_day,
                "per_client_hourly_limit": self.per_hour,
                "per_client_daily_limit": self.per_day,
                "tracked_clients": len(self._clients),
            }


def client_key(request) -> str:
    """Identify the caller for rate-limiting purposes.

    `X-Forwarded-For` is trusted only when `TRUST_PROXY=1`, because any client
    can send that header and a limiter that believes it is a limiter that can
    be bypassed by setting a string. Leaving it unset when deployed behind a
    proxy fails in the safe direction: every caller shares the proxy's IP and
    therefore one bucket, which is stricter than intended rather than looser.
    """
    if os.environ.get("TRUST_PROXY") == "1":
        forwarded = request.headers.get("x-forwarded-for", "")
        if forwarded:
            return forwarded.split(",")[0].strip()
    return getattr(getattr(request, "client", None), "host", None) or "unknown"
