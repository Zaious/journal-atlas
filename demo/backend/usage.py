"""Anonymous daily totals of how the demo is used.

Decided by the maintainer on 2026-11-23 (docs/status/SITE_SPEC.md, decision 4):
the site collects no visitor data and loads no third-party script, but the
maintainer may learn *whether the demo is used and where it comes up empty*.
That is all this module records, and it is deliberately narrow:

* A UTC date, how many searches started, and how each ended (a fixed set of
  words, see OUTCOMES).
* For searches that reached a ranking: the field directory of the best match
  (``psychology``, ``philosophy`` ...), which is one of about a dozen values the
  corpus itself defines, never free text.
* How many follow-up questions were asked.

It never sees an address, a header, a user agent, or any part of what was
pasted. Like ``ratelimit.py`` it lives in memory only: the demo persists nothing
between requests, and a counter file would trade that away. The cost is that the
numbers restart from zero whenever the process restarts, and the public
``/api/usage`` says so.

The one signal that matters for the maintainer is ``no_candidates`` plus a top
field that is thin: that is where people ask and the corpus has nothing to say.
"""

from __future__ import annotations

import threading
import time
from collections import Counter

# A closed set, so an unexpected string can never be used to smuggle text in.
OUTCOMES = (
    "completed",      # parsed, ranked, recommendation written
    "clarified",      # stopped to ask one clarifying question
    "no_candidates",  # no entry passed the hard constraints
    "error",          # a provider or screening failure
    "refused",        # turned away by the rate or daily limit
    "abandoned",      # the visitor left before the stream ended
)

KEEP_DAYS = 30
_FIELD_MAX_LEN = 40


def _day(now: float) -> str:
    return time.strftime("%Y-%m-%d", time.gmtime(now))


class UsageCounter:
    def __init__(self) -> None:
        self._days: dict[str, dict] = {}
        self._lock = threading.Lock()
        self._since = time.time()

    def _bucket(self, now: float) -> dict:
        day = _day(now)
        bucket = self._days.get(day)
        if bucket is None:
            bucket = {"outcomes": Counter(), "top_field": Counter(), "followups": 0}
            self._days[day] = bucket
            for old in sorted(self._days)[:-KEEP_DAYS]:
                del self._days[old]
        return bucket

    def record(self, outcome: str, top_field: str | None = None, now: float | None = None) -> None:
        if outcome not in OUTCOMES:
            raise ValueError(f"unknown outcome {outcome!r}")
        now = time.time() if now is None else now
        with self._lock:
            bucket = self._bucket(now)
            bucket["outcomes"][outcome] += 1
            if top_field and len(top_field) <= _FIELD_MAX_LEN:
                bucket["top_field"][top_field] += 1

    def record_followup(self, now: float | None = None) -> None:
        now = time.time() if now is None else now
        with self._lock:
            self._bucket(now)["followups"] += 1

    def snapshot(self, days: int = 14) -> dict:
        with self._lock:
            keys = sorted(self._days)[-days:]
            rows = []
            for key in keys:
                b = self._days[key]
                rows.append({
                    "date": key,
                    "searches": sum(b["outcomes"].values()),
                    "outcomes": {o: b["outcomes"].get(o, 0) for o in OUTCOMES},
                    "top_field": dict(b["top_field"].most_common()),
                    "followups": b["followups"],
                })
            return {
                "days": rows,
                "since": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(self._since)),
                "note": ("Anonymous totals kept in memory: no address, no text, no "
                         "identifier. They restart from zero when the server restarts, "
                         "so a day can be partial."),
            }
