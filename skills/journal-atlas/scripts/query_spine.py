#!/usr/bin/env python3
"""
query_spine.py — Breadth queries over the full ISSN-keyed journal spine.

Unlike query_journals.py / fit_score.py (which read the ~399 curated
references/journals/**/*.md entries — Layer-E/P depth), this script reads
journal_spine.db — the ~167k-row deterministic fact table (OpenAlex + DOAJ +
JUFO + CAS 中科院分区 + Norwegian Register + Retraction Watch, ISSN-L joined).
No LLM, no soft metadata — Layer-S/P structural facts only.

Use this for "breadth" questions the curated 399 can't answer:
  - "What CAS Zone 1 journals exist near this topic that we haven't curated yet?"
  - "All JUFO level 2-3 journals in a country/publisher"
  - "Any journal with a retraction history above N"
  - "Is <journal> even in our data at all?"

Each result is flagged `in_curated_kb` — when true, go read the matching
references/journals/**/*.md file for the soft-metadata depth this script
does not have. See docs/ATLAS_V2_DESIGN.md §5 ("the skill reads the spine
for breadth ... and the markdown entries for depth").

Usage:
    # Prominent, uncurated CAS Zone 1/2 journals matching a topic keyword
    python scripts/query_spine.py --topic-contains "embodied cognition" --cas-zone 1,2 --uncurated-only

    # JUFO level 2-3, sorted by works count
    python scripts/query_spine.py --jufo-level 2,3 --sort-by works_count --limit 20

    # Is this ISSN in the spine at all, and do we have a curated entry for it?
    python scripts/query_spine.py --issn 0022-3514

    # JSON output for tooling
    python scripts/query_spine.py --publisher Sage --min-h-index 50 --format json

Requires scripts/spine/journal_spine.db, which is git-ignored (256MB+) and
must be built locally — see scripts/spine/README.md. Fails with a clear
message (not a crash) if the DB is missing.

Author: Cardinal (架構師), Journal Atlas project
License: MIT
"""

from __future__ import annotations

import argparse
import csv
import glob
import io
import json
import re
import sqlite3
import sys
from pathlib import Path
from typing import Any, Optional

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass

DEFAULT_DB_PATH = Path(__file__).parent / "spine" / "journal_spine.db"
DEFAULT_JOURNALS_ROOT = Path(__file__).parent.parent / "references" / "journals"

DEFAULT_COLUMNS = [
    "name", "publisher", "country", "works_count", "h_index",
    "cas_zone", "jufo_level", "in_curated_kb",
]


# ---------- ISSN handling ----------


def normissn(s: Optional[str]) -> Optional[str]:
    if not s:
        return None
    s = re.sub(r"[^0-9Xx]", "", str(s)).upper()
    return s if len(s) == 8 else None


def build_curated_issn_index(journals_root: Path) -> dict[str, Path]:
    """Map normalized ISSN -> curated .md path, for every ISSN mentioned in
    any curated entry's Identity table (Print or Online)."""
    index: dict[str, Path] = {}
    if not journals_root.exists():
        return index
    for fp in journals_root.rglob("*.md"):
        if fp.name in {"README.md", "TEMPLATE.md", ".gitkeep"}:
            continue
        try:
            text = fp.read_text(encoding="utf-8")
        except OSError:
            continue
        for issn in re.findall(
            r"\*\*ISSN \((?:Print|Online)\)\*\*\s*\|\s*([0-9]{4}-[0-9]{3}[0-9Xx])", text
        ):
            n = normissn(issn)
            if n:
                index[n] = fp
    return index


# ---------- DB access ----------


def open_db(db_path: Path) -> sqlite3.Connection:
    if not db_path.exists():
        print(
            f"Spine DB not found at {db_path}.\n"
            "It's git-ignored (256MB+) and must be built locally. See "
            "scripts/spine/README.md — quick start:\n"
            "  cd scripts/spine && python build_spine.py --full --fetch-bulk ./bulk "
            "&& python build_spine.py --full --out journal_spine.db\n"
            "Or point --db at an existing copy.",
            file=sys.stderr,
        )
        sys.exit(1)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    return conn


def resolve_issn_l(conn: sqlite3.Connection, issn: str) -> Optional[str]:
    n = normissn(issn)
    if not n:
        return None
    row = conn.execute("SELECT issn_l FROM issn_index WHERE issn = ?", (n,)).fetchone()
    return row["issn_l"] if row else None


# ---------- Filtering ----------


def build_query(args: argparse.Namespace) -> tuple[str, list[Any]]:
    clauses: list[str] = []
    params: list[Any] = []

    if args.issn:
        clauses.append("issn_l = ?")
        params.append(args.issn)  # already resolved by caller
    if args.name_contains:
        clauses.append("display_name LIKE ? COLLATE NOCASE")
        params.append(f"%{args.name_contains}%")
    if args.publisher:
        clauses.append("publisher LIKE ? COLLATE NOCASE")
        params.append(f"%{args.publisher}%")
    if args.country:
        clauses.append("country = ?")
        params.append(args.country.upper())
    if args.min_works_count is not None:
        clauses.append("works_count >= ?")
        params.append(args.min_works_count)
    if args.min_h_index is not None:
        clauses.append("h_index >= ?")
        params.append(args.min_h_index)
    if args.max_h_index is not None:
        clauses.append("h_index <= ?")
        params.append(args.max_h_index)
    if args.min_cited_by_count is not None:
        clauses.append("cited_by_count >= ?")
        params.append(args.min_cited_by_count)
    if args.min_two_yr_citedness is not None:
        clauses.append("two_yr_citedness >= ?")
        params.append(args.min_two_yr_citedness)
    if args.is_oa:
        clauses.append("is_oa = 1")
    if args.in_doaj:
        clauses.append("is_in_doaj = 1")
    if args.max_apc is not None:
        clauses.append("(apc_usd IS NOT NULL AND apc_usd <= ?)")
        params.append(args.max_apc)
    if args.jufo_level:
        wanted = [v.strip() for v in args.jufo_level.split(",") if v.strip()]
        clauses.append(f"jufo_level IN ({','.join('?' for _ in wanted)})")
        params.extend(wanted)
    if args.norway_level:
        wanted = [v.strip() for v in args.norway_level.split(",") if v.strip()]
        clauses.append(f"norway_level IN ({','.join('?' for _ in wanted)})")
        params.extend(wanted)
    if args.cas_zone:
        wanted = [v.strip() for v in args.cas_zone.split(",") if v.strip()]
        # cas_zone is stored as "<digit> [rank/total]" — match on the leading digit
        or_clauses = " OR ".join(["cas_zone LIKE ?" for _ in wanted])
        clauses.append(f"({or_clauses})")
        params.extend(f"{v}%" for v in wanted)
    if args.cas_top:
        clauses.append("cas_top = 1")
    if args.max_retractions is not None:
        clauses.append("(retraction_count IS NULL OR retraction_count <= ?)")
        params.append(args.max_retractions)
    if args.peer_review_type:
        clauses.append("peer_review_type LIKE ? COLLATE NOCASE")
        params.append(f"%{args.peer_review_type}%")
    if args.topic_contains:
        clauses.append("topics_json LIKE ? COLLATE NOCASE")
        params.append(f"%{args.topic_contains}%")

    where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
    sql = f"SELECT * FROM journals {where}"
    return sql, params


SORTABLE = {
    "name": "display_name", "works_count": "works_count", "h_index": "h_index",
    "cited_by_count": "cited_by_count", "two_yr_citedness": "two_yr_citedness",
    "retraction_count": "retraction_count",
}


# ---------- Output ----------


def row_to_record(row: sqlite3.Row, curated_index: dict[str, Path]) -> dict[str, Any]:
    d = dict(row)
    curated_path = curated_index.get(normissn(row["issn_l"]) or "")
    d["name"] = d.pop("display_name")
    d["in_curated_kb"] = curated_path is not None
    d["curated_path"] = str(curated_path) if curated_path else None
    try:
        topics = json.loads(d.get("topics_json") or "[]")
        d["top_topics"] = ", ".join(t["name"] for t in topics[:3])
    except (json.JSONDecodeError, TypeError, KeyError):
        d["top_topics"] = None
    return d


def _fmt_cell(v: Any) -> str:
    if v is None:
        return "-"
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, float):
        return f"{v:.2f}"
    return str(v)


def render_table(records: list[dict], columns: list[str]) -> str:
    if not records:
        return "(no matches)"
    rows = [[_fmt_cell(r.get(c)) for c in columns] for r in records]
    widths = [max(len(columns[i]), *(len(row[i]) for row in rows)) for i in range(len(columns))]
    lines = ["  ".join(h.ljust(w) for h, w in zip(columns, widths))]
    lines.append("  ".join("-" * w for w in widths))
    for row in rows:
        lines.append("  ".join(cell.ljust(w) for cell, w in zip(row, widths)))
    return "\n".join(lines)


def render_csv(records: list[dict], columns: list[str]) -> str:
    out = io.StringIO()
    writer = csv.writer(out)
    writer.writerow(columns)
    for r in records:
        writer.writerow([_fmt_cell(r.get(c)) for c in columns])
    return out.getvalue()


def render_markdown(records: list[dict], columns: list[str]) -> str:
    if not records:
        return "*(no matches)*"
    header = "| " + " | ".join(columns) + " |"
    sep = "|" + "|".join("---" for _ in columns) + "|"
    rows = ["| " + " | ".join(_fmt_cell(r.get(c)) for c in columns) + " |" for r in records]
    return "\n".join([header, sep] + rows)


def render_json(records: list[dict], columns: list[str]) -> str:
    return json.dumps([{c: r.get(c) for c in columns} for r in records], indent=2)


# ---------- CLI ----------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Breadth queries over the full ~167k-row journal spine (structural facts only).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--issn", type=str, help="Look up a single ISSN (any variant, resolved via issn_index)")
    parser.add_argument("--name-contains", type=str, help="Substring match on journal name")
    parser.add_argument("--publisher", type=str, help="Substring match on publisher")
    parser.add_argument("--country", type=str, help="Exact 2-letter country code")
    parser.add_argument("--min-works-count", type=int, help="Min OpenAlex works_count (a proxy for how active/prominent the journal is)")
    parser.add_argument("--min-h-index", type=int)
    parser.add_argument("--max-h-index", type=int)
    parser.add_argument("--min-cited-by-count", type=int)
    parser.add_argument("--min-two-yr-citedness", type=float)
    parser.add_argument("--is-oa", action="store_true", help="OpenAlex-flagged fully open access")
    parser.add_argument("--in-doaj", action="store_true", help="Listed in DOAJ")
    parser.add_argument("--max-apc", type=int, help="Max APC (USD)")
    parser.add_argument("--jufo-level", type=str, help="CSV of JUFO levels, e.g. '2,3'")
    parser.add_argument("--norway-level", type=str, help="CSV of Norwegian Register levels, e.g. '1,2'")
    parser.add_argument("--cas-zone", type=str, help="CSV of CAS 中科院分区 zone digits, e.g. '1,2'")
    parser.add_argument("--cas-top", action="store_true", help="CAS Top-journal flag only")
    parser.add_argument("--max-retractions", type=int, help="Max Retraction Watch count (integrity filter)")
    parser.add_argument("--peer-review-type", type=str, help="Substring match, e.g. 'double blind'")
    parser.add_argument("--topic-contains", type=str, help="Substring match against OpenAlex topic names")
    parser.add_argument("--uncurated-only", action="store_true", help="Exclude journals that already have a curated references/journals entry")
    parser.add_argument("--curated-only", action="store_true", help="Only journals that already have a curated references/journals entry")

    parser.add_argument("--db", type=Path, default=DEFAULT_DB_PATH, help=f"Path to journal_spine.db (default: {DEFAULT_DB_PATH})")
    parser.add_argument("--journals-root", type=Path, default=DEFAULT_JOURNALS_ROOT, help="Curated markdown root, for the in_curated_kb cross-reference")
    parser.add_argument("--format", choices=["table", "csv", "json", "markdown"], default="table")
    parser.add_argument("--columns", type=str, default=",".join(DEFAULT_COLUMNS))
    parser.add_argument("--sort-by", type=str, default="works_count", choices=list(SORTABLE))
    parser.add_argument("--limit", type=int, default=50, help="Max rows to return (default 50 — the spine is ~167k rows; narrow with filters or raise this explicitly)")

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    conn = open_db(args.db)

    if args.issn:
        resolved = resolve_issn_l(conn, args.issn)
        if not resolved:
            print(f"ISSN {args.issn} not found in spine (issn_index has 247k+ known ISSNs; "
                  "an unlisted ISSN may be a typo, a defunct journal, or simply outside OpenAlex's coverage).",
                  file=sys.stderr)
            return 1
        args.issn = resolved

    sql, params = build_query(args)
    order_col = SORTABLE[args.sort_by]
    sql += f" ORDER BY {order_col} IS NULL, {order_col} DESC"
    total_matching = conn.execute(f"SELECT COUNT(*) FROM ({sql})", params).fetchone()[0]
    sql += " LIMIT ?"
    params_with_limit = [*params, args.limit]
    rows = conn.execute(sql, params_with_limit).fetchall()

    curated_index = build_curated_issn_index(args.journals_root)
    records = [row_to_record(r, curated_index) for r in rows]

    if args.uncurated_only:
        records = [r for r in records if not r["in_curated_kb"]]
    if args.curated_only:
        records = [r for r in records if r["in_curated_kb"]]

    columns = [c.strip() for c in args.columns.split(",") if c.strip()]

    if args.format == "json":
        print(render_json(records, columns))
    elif args.format == "csv":
        print(render_csv(records, columns))
    elif args.format == "markdown":
        print(render_markdown(records, columns))
    else:
        shown_note = f" (showing {len(records)}, limit={args.limit})" if total_matching > len(records) else ""
        print(f"=== {total_matching} of 166,821 spine journals match{shown_note} ===")
        print()
        print(render_table(records, columns))

    return 0


if __name__ == "__main__":
    sys.exit(main())
