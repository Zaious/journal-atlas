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


def trusted_hops() -> int:
    """How many proxies sit in front of this app, from `TRUST_PROXY`.

    A count rather than a boolean, because which entry of `X-Forwarded-For`
    identifies the caller depends on how many trusted proxies appended to it:

        TRUST_PROXY=1   client → Caddy                    (direct origin)
        TRUST_PROXY=2   client → Cloudflare → Caddy       (proxied / orange cloud)

    Anything unparseable reads as 0, which ignores the header entirely. That
    fails in the safe direction — every caller shares one bucket, stricter than
    intended rather than bypassable.
    """
    raw = (os.environ.get("TRUST_PROXY") or "").strip().lower()
    if raw in ("true", "yes", "on"):
        return 1
    try:
        return max(0, int(raw))
    except ValueError:
        return 0


def client_key(request) -> str:
    """Identify the caller for rate-limiting purposes.

    `X-Forwarded-For` is a list that each proxy **appends** to, so the entries
    a client controls are on the *left* and the ones added by infrastructure
    are on the *right*. Reading the leftmost entry — the obvious thing, and
    what this function did until it was tested against a real deployment —
    means anyone can send `X-Forwarded-For: <anything>` and get a fresh
    rate-limit bucket per request.

    So the caller is counted in from the right: with N trusted proxies in
    front, each of which appended exactly one entry, `chain[-N]` is the address
    the outermost trusted proxy observed, and nothing to the left of it can
    change that.

    Caddy hides this bug by default — with no `trusted_proxies` configured it
    discards a client-supplied `X-Forwarded-For` rather than appending to it,
    so leftmost and rightmost are the same entry. The moment Cloudflare goes in
    front and Caddy is told to trust it, they stop being the same entry:
    Cloudflare appends the client IP to whatever the client sent rather than
    replacing it. A limiter that reads leftmost is correct right up until that
    switch, and silently worthless afterwards.

    Falls back to the peer address when the chain is shorter than the
    configured hop count, which means the deployment is misconfigured; one
    shared bucket is the right way to be wrong.
    """
    hops = trusted_hops()
    if hops:
        chain = [p.strip() for p in request.headers.get("x-forwarded-for", "").split(",") if p.strip()]
        if len(chain) >= hops:
            return chain[-hops]
    return getattr(getattr(request, "client", None), "host", None) or "unknown"
