#!/usr/bin/env python3
"""
topic_trend_scan.py — Detect topic-distribution shifts in a journal.

Queries OpenAlex for all works published by a journal in a given time window,
aggregates topic counts, and (if a baseline cache exists) compares against
the previous window to flag trending and declining topics.

Usage:
    # Scan a journal by ISSN, last 3 years (default)
    python scripts/topic_trend_scan.py --issn 0959-3543

    # Custom time window (years from today)
    python scripts/topic_trend_scan.py --issn 0959-3543 --years 5

    # Check for specific keywords (useful for "is this journal still publishing X?")
    python scripts/topic_trend_scan.py --issn 0959-3543 \\
        --keywords "BDSM,autoethnography,self-state"

    # JSON output for tooling
    python scripts/topic_trend_scan.py --issn 0959-3543 --json

Cache:
    Results are cached to .cache/topic-scans/{issn}-{years}y.json with a
    30-day TTL. Use --refresh to force a re-fetch.

Author: Cardinal (架構師), Journal Atlas project
License: MIT
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Optional

try:
    from pyalex import Sources, Works, config
except ImportError:
    print("ERROR: pyalex not installed. Run: pip install pyalex", file=sys.stderr)
    sys.exit(1)


if email := os.environ.get("OPENALEX_EMAIL"):
    config.email = email


CACHE_DIR = Path(".cache/topic-scans")
CACHE_TTL_DAYS = 30
DEFAULT_YEARS = 3
DEFAULT_TOP_N = 15


# ---------- Data structures ----------


@dataclass
class TopicScanResult:
    journal_name: str
    openalex_id: str
    issn: Optional[str]
    window_years: int
    window_start: str  # YYYY-MM-DD
    window_end: str
    total_works: int
    topic_counts: dict[str, int] = field(default_factory=dict)
    keyword_hits: dict[str, int] = field(default_factory=dict)
    fetched_at: str = ""

    def as_dict(self) -> dict:
        return {
            "journal_name": self.journal_name,
            "openalex_id": self.openalex_id,
            "issn": self.issn,
            "window_years": self.window_years,
            "window_start": self.window_start,
            "window_end": self.window_end,
            "total_works": self.total_works,
            "topic_counts": self.topic_counts,
            "keyword_hits": self.keyword_hits,
            "fetched_at": self.fetched_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "TopicScanResult":
        return cls(**data)


# ---------- Cache helpers ----------


def cache_path(issn_or_id: str, years: int) -> Path:
    safe = issn_or_id.replace("/", "_").replace(":", "_")
    return CACHE_DIR / f"{safe}-{years}y.json"


def load_cache(path: Path) -> Optional[TopicScanResult]:
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        fetched = datetime.fromisoformat(data["fetched_at"])
        if (datetime.now() - fetched).days > CACHE_TTL_DAYS:
            return None
        return TopicScanResult.from_dict(data)
    except (OSError, json.JSONDecodeError, KeyError, ValueError):
        return None


def save_cache(result: TopicScanResult, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result.as_dict(), indent=2), encoding="utf-8")


# ---------- OpenAlex queries ----------


def resolve_source(issn: Optional[str], openalex_id: Optional[str]) -> dict:
    if openalex_id:
        return Sources()[openalex_id]
    if issn:
        results = Sources().filter(issn=issn).get()
        if not results:
            raise ValueError(f"No source found for ISSN {issn}")
        return results[0]
    raise ValueError("Need --issn or --openalex-id")


def fetch_works_in_window(
    source_id: str, start_date: str, end_date: str
) -> list[dict]:
    """Page through Works for a source within a date window."""
    works: list[dict] = []
    query = (
        Works()
        .filter(
            primary_location={"source": {"id": source_id}},
            from_publication_date=start_date,
            to_publication_date=end_date,
        )
        .select(["id", "title", "topics", "keywords", "publication_year"])
    )
    # Paginate
    for page in query.paginate(per_page=200, n_max=10_000):
        works.extend(page)
    return works


def aggregate_topics(works: list[dict]) -> dict[str, int]:
    counter: Counter[str] = Counter()
    for work in works:
        for t in work.get("topics") or []:
            name = t.get("display_name")
            if name:
                counter[name] += 1
    return dict(counter.most_common())


def check_keywords(works: list[dict], keywords: list[str]) -> dict[str, int]:
    hits: dict[str, int] = {kw: 0 for kw in keywords}
    if not keywords:
        return hits
    lowered_keywords = [(kw, kw.lower()) for kw in keywords]
    for work in works:
        # Search in title + keywords + topic names
        text_blob = (work.get("title") or "").lower()
        for kw in work.get("keywords") or []:
            text_blob += " " + (kw.get("display_name") or "").lower()
        for t in work.get("topics") or []:
            text_blob += " " + (t.get("display_name") or "").lower()
        for kw_orig, kw_lower in lowered_keywords:
            if kw_lower in text_blob:
                hits[kw_orig] += 1
    return hits


# ---------- Main scan ----------


def scan(
    issn: Optional[str],
    openalex_id: Optional[str],
    years: int,
    keywords: list[str],
    refresh: bool = False,
) -> TopicScanResult:
    cache_key = issn or openalex_id
    cpath = cache_path(cache_key, years)

    if not refresh and not keywords:
        cached = load_cache(cpath)
        if cached:
            return cached

    source = resolve_source(issn, openalex_id)
    source_id = source["id"]
    journal_name = source.get("display_name", "Unknown Journal")
    issn_list = source.get("issn") or []

    today = date.today()
    start_date = (today - timedelta(days=365 * years)).isoformat()
    end_date = today.isoformat()

    works = fetch_works_in_window(source_id, start_date, end_date)
    topics = aggregate_topics(works)
    keyword_hits = check_keywords(works, keywords)

    result = TopicScanResult(
        journal_name=journal_name,
        openalex_id=source_id,
        issn=issn_list[0] if issn_list else issn,
        window_years=years,
        window_start=start_date,
        window_end=end_date,
        total_works=len(works),
        topic_counts=topics,
        keyword_hits=keyword_hits,
        fetched_at=datetime.now().isoformat(timespec="seconds"),
    )

    save_cache(result, cpath)
    return result


# ---------- Output ----------


def render_human(result: TopicScanResult, top_n: int) -> str:
    lines: list[str] = [
        f"\nTopic Trend Scan: {result.journal_name}",
        f"  ISSN: {result.issn or '(none)'}",
        f"  Window: {result.window_start} -> {result.window_end} ({result.window_years} years)",
        f"  Total works in window: {result.total_works}",
        f"  Fetched: {result.fetched_at}",
        "",
        f"  Top {top_n} topics:",
    ]
    items = list(result.topic_counts.items())[:top_n]
    if not items:
        lines.append("    (no topics found)")
    else:
        max_topic_len = max(len(t) for t, _ in items)
        max_count = max(c for _, c in items)
        bar_width = 30
        for topic, count in items:
            bar = "#" * int(bar_width * count / max_count)
            lines.append(f"    {topic:<{max_topic_len}}  {count:>5}  {bar}")

    if result.keyword_hits:
        lines.append("")
        lines.append("  Keyword hits:")
        for kw, count in result.keyword_hits.items():
            status = "found" if count > 0 else "NOT FOUND"
            lines.append(f"    {kw:<30s}  {count:>5}  ({status})")

    return "\n".join(lines)


def render_json(result: TopicScanResult, top_n: int) -> str:
    data = result.as_dict()
    data["topic_counts"] = dict(list(data["topic_counts"].items())[:top_n])
    return json.dumps(data, indent=2)


# ---------- CLI ----------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan a journal's recent publication topics for trend shifts.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--issn", help="Journal ISSN (e.g. 0959-3543)")
    group.add_argument("--openalex-id", help="OpenAlex source ID (e.g. S12345678)")

    parser.add_argument("--years", type=int, default=DEFAULT_YEARS)
    parser.add_argument(
        "--top-n",
        type=int,
        default=DEFAULT_TOP_N,
        help=f"Number of top topics to show (default {DEFAULT_TOP_N})",
    )
    parser.add_argument(
        "--keywords",
        type=str,
        help="Comma-separated keywords to specifically check for presence",
    )
    parser.add_argument(
        "--refresh", action="store_true", help="Ignore cache, re-fetch from OpenAlex"
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON output")

    args = parser.parse_args()
    keywords = [k.strip() for k in (args.keywords or "").split(",") if k.strip()]

    try:
        result = scan(
            issn=args.issn,
            openalex_id=args.openalex_id,
            years=args.years,
            keywords=keywords,
            refresh=args.refresh,
        )
    except Exception as exc:
        msg = f"Scan failed: {exc}"
        if args.json:
            print(json.dumps({"error": msg}))
        else:
            print(msg, file=sys.stderr)
        return 1

    if args.json:
        print(render_json(result, args.top_n))
    else:
        print(render_human(result, args.top_n))

    return 0


if __name__ == "__main__":
    sys.exit(main())
