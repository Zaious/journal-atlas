#!/usr/bin/env python3
"""
query_journals.py — Deterministic filter queries over the journal knowledge base.

Unlike fit_score.py (which computes weighted soft-fit scores for paper-vs-journal
matching), this script handles structured boolean queries:

  - "All Q1 psychology journals"
  - "Open Access journals with h-index >= 100"
  - "Journals without AI permission gates"
  - "Sage journals with zero-embargo Green OA"

This is the right tool when the user asks deterministic questions that don't
require AI semantic reasoning. It scales to 1000+ entries; fit_score's 6-dim
soft scoring saturates context above ~50 entries.

Usage:
    # All OA-only journals in psychology
    python scripts/query_journals.py --oa-model full_oa --field psychology

    # h-index >= 100 (uses OpenAlex h-index, more reliable than JCR IF for our seed)
    python scripts/query_journals.py --min-h-index 100

    # Q1 or Q2 journals in HCI (when Quartile is populated)
    python scripts/query_journals.py --quartile Q1,Q2 --field hci

    # No AI permission gate
    python scripts/query_journals.py --no-ai-permission-gate

    # Sage journals (publisher substring match)
    python scripts/query_journals.py --publisher Sage

    # Combine filters: psychology hybrid journals with no AI gate
    python scripts/query_journals.py --field psychology --oa-model hybrid --no-ai-permission-gate

    # JSON output for tooling
    python scripts/query_journals.py --field psychology --min-h-index 50 --format json

Pending fields:
    Many entries have fields marked *(pending)*. Pending fields are treated as
    UNKNOWN and excluded from matches — a "Q1 query" only returns journals
    that explicitly state Q1. This is the honest behavior; we never assume.

Author: Cardinal (架構師), Journal Atlas project
License: MIT
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

# Ensure UTF-8 stdout on Windows (default cp950 chokes on em-dashes, arrows, etc.)
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass


PENDING_MARKERS = {"*(pending)*", "(pending)", "*(not disclosed by publisher)*"}


@dataclass
class JournalRecord:
    """Structured record parsed from a journal .md file."""

    path: Path
    name: str
    field: str  # subdirectory name
    publisher: Optional[str] = None
    issn_print: Optional[str] = None
    impact_factor: Optional[float] = None
    h_index: Optional[int] = None
    two_yr_citedness: Optional[float] = None
    quartile: Optional[str] = None
    oa_model: Optional[str] = None  # subscription / hybrid / full_oa / unknown
    apc_usd: Optional[int] = None
    has_subscription_path: bool = False
    has_ai_permission_gate: Optional[bool] = None  # None = unknown
    word_limit: Optional[int] = None
    review_time_months: Optional[float] = None
    has_zero_embargo: Optional[bool] = None
    methodology_scores: dict[str, int] = field(default_factory=dict)
    last_verified: Optional[str] = None
    extra: dict[str, Any] = field(default_factory=dict)

    def as_dict(self) -> dict:
        return {
            "name": self.name,
            "field": self.field,
            "path": str(self.path),
            "publisher": self.publisher,
            "impact_factor": self.impact_factor,
            "h_index": self.h_index,
            "two_yr_citedness": self.two_yr_citedness,
            "quartile": self.quartile,
            "oa_model": self.oa_model,
            "apc_usd": self.apc_usd,
            "has_subscription_path": self.has_subscription_path,
            "has_ai_permission_gate": self.has_ai_permission_gate,
            "word_limit": self.word_limit,
            "review_time_months": self.review_time_months,
            "has_zero_embargo": self.has_zero_embargo,
            "last_verified": self.last_verified,
        }


# ---------- Parsing ----------


def parse_journal_file(path: Path) -> JournalRecord:
    """Extract structured fields from a journal .md file (regex-based parser)."""
    content = path.read_text(encoding="utf-8")
    field_name = path.parent.name

    rec = JournalRecord(
        path=path,
        name=_extract_h1(content) or path.stem,
        field=field_name,
    )

    # Identity
    rec.publisher = _extract_table_value(content, "Publisher")
    rec.issn_print = _extract_table_value(content, r"ISSN \(Print\)")

    # Metrics — try several field labels
    if_str = _extract_table_value(content, "Impact Factor")
    rec.impact_factor = _to_float(if_str)
    rec.h_index = _to_int(_extract_table_value(content, "h-index"))
    rec.two_yr_citedness = _to_float(
        _extract_table_value(content, "2-Year Mean Citedness")
        or _extract_table_value(content, "2yr Mean Citedness")
        or _extract_table_value(content, "2-yr Mean Citedness")
    )
    quart = _extract_table_value(content, "Quartile.*?")
    rec.quartile = _normalize_quartile(quart) if quart else None

    # Format
    word_limit = _extract_table_value(content, "Word limit")
    rec.word_limit = _to_int(word_limit)

    # Open Access / APC
    oa_section = _extract_subsection(content, "Open Access") or content
    rec.has_subscription_path = _detect_subscription_path(content)
    rec.oa_model = _detect_oa_model(oa_section, rec.has_subscription_path)
    apc_str = _extract_table_value(oa_section, "APC")
    rec.apc_usd = _parse_apc(apc_str)

    # AI policy — read the explicit "Explicit permission gate?" row's Yes/No
    ai_section = _extract_subsection(content, "AI Policy")
    if ai_section:
        m = re.search(
            r"\|\s*\*\*Explicit permission gate\??\*\*\s*\|\s*([^|]+)",
            ai_section, re.IGNORECASE
        )
        if m:
            value = m.group(1).strip().lower()
            if value.startswith("yes"):
                rec.has_ai_permission_gate = True
            elif value.startswith("no"):
                rec.has_ai_permission_gate = False
            # "conditional" or pending → leave as None (unknown)

    # Embargo
    preprint_section = _extract_subsection(content, "Preprint Policy") or content
    rec.has_zero_embargo = bool(
        re.search(r"zero[- ]embargo|no embargo|0\s*months?\s*embargo", preprint_section, re.IGNORECASE)
    )

    # Methodology preferences (for query like "where is autoethnography >=3")
    method_section = _extract_subsection(content, "Methodological Preferences")
    if method_section:
        for line in method_section.splitlines():
            m = re.match(r"\|\s*([^|]+?)\s*\|\s*([0-5])\s*\|", line)
            if m:
                method = m.group(1).strip().lower()
                rec.methodology_scores[method] = int(m.group(2))

    # Review cycle time
    review_section = _extract_subsection(content, "Review Cycle Time")
    if review_section:
        m = re.search(
            r"Time to acceptance.*?\|\s*([^|]+)\|",
            review_section, re.IGNORECASE
        )
        if m:
            text = m.group(1).strip().lower()
            num = re.search(r"(\d+(?:\.\d+)?)", text)
            if num:
                try:
                    n = float(num.group(1))
                    if "week" in text:
                        n = n / 4.0
                    rec.review_time_months = n
                except ValueError:
                    pass

    # Last verified
    m = re.search(r"\*\*Last verified\*\*:?\s*(\d{4}-\d{2}-\d{2})", content)
    if m:
        rec.last_verified = m.group(1)

    return rec


def _extract_h1(content: str) -> Optional[str]:
    match = re.search(r"^# +(.+?)\s*$", content, re.MULTILINE)
    return match.group(1).strip() if match else None


def _extract_table_value(content: str, label_pattern: str) -> Optional[str]:
    """Find a table row like `| **<label>** | <value> |` and return <value>."""
    pattern = re.compile(
        rf"\|\s*\*?\*?{label_pattern}\*?\*?\s*\|\s*([^|]+?)\s*\|",
        re.IGNORECASE,
    )
    match = pattern.search(content)
    if not match:
        return None
    value = match.group(1).strip()
    if value in PENDING_MARKERS or not value or value.lower() == "tbd":
        return None
    return value


def _extract_subsection(content: str, name: str) -> Optional[str]:
    pattern = re.compile(
        rf"^#{{2,3}} +{re.escape(name)}\s*$(.*?)(?=^#{{2,3}} +|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(content)
    return match.group(1) if match else None


def _detect_subscription_path(content: str) -> bool:
    oa_section = _extract_subsection(content, "Open Access") or content
    return bool(
        re.search(
            r"(subscription[^|]*\|\s*\$?\s*0\b"
            r"|subscription[^.]*no APC"
            r"|\bModel\b[^|]*\|\s*Subscription\b"
            r"|\bModel\b[^|]*\|\s*Hybrid\b)",
            oa_section,
            re.IGNORECASE,
        )
    )


def _detect_oa_model(oa_section: str, has_subscription_path: bool) -> str:
    if re.search(r"\bModel\b[^|]*\|\s*Full OA", oa_section, re.IGNORECASE):
        return "full_oa"
    if re.search(r"\bModel\b[^|]*\|\s*Hybrid", oa_section, re.IGNORECASE):
        return "hybrid"
    if re.search(r"\bModel\b[^|]*\|\s*Subscription\b(?!\s*\+)", oa_section, re.IGNORECASE):
        return "subscription"
    if has_subscription_path:
        return "hybrid"
    return "unknown"


def _parse_apc(s: Optional[str]) -> Optional[int]:
    if not s:
        return None
    m = re.search(r"\$\s*([\d,]+)", s)
    if not m:
        return None
    try:
        return int(m.group(1).replace(",", ""))
    except ValueError:
        return None


def _normalize_quartile(s: str) -> Optional[str]:
    m = re.search(r"\bQ([1-4])\b", s)
    return f"Q{m.group(1)}" if m else None


def _to_float(s: Optional[str]) -> Optional[float]:
    if not s:
        return None
    m = re.search(r"(\d+(?:\.\d+)?)", s)
    return float(m.group(1)) if m else None


def _to_int(s: Optional[str]) -> Optional[int]:
    if not s:
        return None
    m = re.search(r"(\d[\d,]*)", s)
    if not m:
        return None
    try:
        return int(m.group(1).replace(",", ""))
    except ValueError:
        return None


# ---------- Filtering ----------


def matches(rec: JournalRecord, args: argparse.Namespace) -> bool:
    """Return True if record passes all active filters."""

    if args.field and rec.field != args.field:
        return False

    if args.publisher:
        if not rec.publisher or args.publisher.lower() not in rec.publisher.lower():
            return False

    if args.oa_model and rec.oa_model != args.oa_model:
        return False

    if args.has_ai_permission_gate is not None:
        if rec.has_ai_permission_gate is None:  # unknown — exclude
            return False
        if rec.has_ai_permission_gate != args.has_ai_permission_gate:
            return False

    # Impact Factor (fallback to 2yr citedness when JCR IF missing)
    if_value = rec.impact_factor if rec.impact_factor is not None else rec.two_yr_citedness
    if args.min_if is not None:
        if if_value is None or if_value < args.min_if:
            return False
    if args.max_if is not None:
        if if_value is None or if_value > args.max_if:
            return False

    if args.min_h_index is not None:
        if rec.h_index is None or rec.h_index < args.min_h_index:
            return False
    if args.max_h_index is not None:
        if rec.h_index is None or rec.h_index > args.max_h_index:
            return False

    if args.quartile:
        wanted = {q.strip().upper() for q in args.quartile.split(",")}
        if not rec.quartile or rec.quartile.upper() not in wanted:
            return False

    if args.min_word_limit is not None:
        if rec.word_limit is None or rec.word_limit < args.min_word_limit:
            return False

    if args.max_apc is not None:
        if rec.apc_usd is None or rec.apc_usd > args.max_apc:
            return False
    if args.min_apc is not None:
        if rec.apc_usd is None or rec.apc_usd < args.min_apc:
            return False

    if args.zero_embargo:
        if not rec.has_zero_embargo:
            return False

    if args.max_review_months is not None:
        if rec.review_time_months is None or rec.review_time_months > args.max_review_months:
            return False

    if args.methodology:
        method = args.methodology.lower()
        score = None
        for k, v in rec.methodology_scores.items():
            if method in k:
                score = v
                break
        threshold = args.min_methodology_score or 3
        if score is None or score < threshold:
            return False

    return True


# ---------- Output ----------


DEFAULT_COLUMNS = ["name", "field", "publisher", "h_index", "oa_model", "apc_usd", "word_limit"]


def render_table(records: list[JournalRecord], columns: list[str]) -> str:
    """Pretty-print as aligned columns."""
    if not records:
        return "(no matches)"

    # Compute column widths
    headers = columns
    rows = [[_fmt_cell(getattr(r, c, None)) for c in columns] for r in records]
    widths = [max(len(headers[i]), *(len(row[i]) for row in rows)) for i in range(len(headers))]

    lines = []
    sep = "  ".join("-" * w for w in widths)
    lines.append("  ".join(h.ljust(w) for h, w in zip(headers, widths)))
    lines.append(sep)
    for row in rows:
        lines.append("  ".join(cell.ljust(w) for cell, w in zip(row, widths)))
    return "\n".join(lines)


def _fmt_cell(v: Any) -> str:
    if v is None:
        return "-"
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, float):
        return f"{v:.2f}"
    return str(v)


def render_csv(records: list[JournalRecord], columns: list[str]) -> str:
    out = io.StringIO()
    writer = csv.writer(out)
    writer.writerow(columns)
    for r in records:
        writer.writerow([_fmt_cell(getattr(r, c, None)) for c in columns])
    return out.getvalue()


def render_json(records: list[JournalRecord]) -> str:
    return json.dumps([r.as_dict() for r in records], indent=2)


def render_markdown(records: list[JournalRecord], columns: list[str]) -> str:
    if not records:
        return "*(no matches)*"
    header = "| " + " | ".join(columns) + " |"
    sep = "|" + "|".join("---" for _ in columns) + "|"
    rows = ["| " + " | ".join(_fmt_cell(getattr(r, c, None)) for c in columns) + " |" for r in records]
    return "\n".join([header, sep] + rows)


# ---------- File discovery ----------


def collect_files(journals_root: Path) -> list[Path]:
    if not journals_root.exists():
        return []
    return sorted(
        p for p in journals_root.rglob("*.md")
        if p.name not in {"README.md", ".gitkeep"}
    )


# ---------- CLI ----------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Deterministic filter queries over the journal knowledge base.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    # Field / publisher / OA model
    parser.add_argument("--field", type=str, help="Filter by field directory")
    parser.add_argument("--publisher", type=str, help="Substring match on publisher")
    parser.add_argument(
        "--oa-model",
        type=str,
        choices=["subscription", "hybrid", "full_oa", "unknown"],
        help="Open Access model",
    )

    # AI policy
    ai_group = parser.add_mutually_exclusive_group()
    ai_group.add_argument("--has-ai-permission-gate", action="store_const",
                          dest="has_ai_permission_gate", const=True,
                          help="Only journals requiring AI permission")
    ai_group.add_argument("--no-ai-permission-gate", action="store_const",
                          dest="has_ai_permission_gate", const=False,
                          help="Exclude journals requiring AI permission")
    parser.set_defaults(has_ai_permission_gate=None)

    # Metrics
    parser.add_argument("--min-if", type=float, help="Min Impact Factor (falls back to 2yr citedness)")
    parser.add_argument("--max-if", type=float, help="Max Impact Factor")
    parser.add_argument("--min-h-index", type=int)
    parser.add_argument("--max-h-index", type=int)
    parser.add_argument(
        "--quartile",
        type=str,
        help="Quartile(s) — single (Q1) or CSV (Q1,Q2)",
    )

    # Format
    parser.add_argument("--min-word-limit", type=int, help="Min word ceiling")

    # OA / APC
    parser.add_argument("--max-apc", type=int, help="Max OA APC (USD)")
    parser.add_argument("--min-apc", type=int)
    parser.add_argument("--zero-embargo", action="store_true",
                        help="Only journals with zero-embargo Green OA")

    # Review speed
    parser.add_argument("--max-review-months", type=float,
                        help="Max time to acceptance (months)")

    # Methodology
    parser.add_argument("--methodology", type=str,
                        help="Methodology label (e.g. 'autoethnography') — match if receptiveness >= threshold")
    parser.add_argument("--min-methodology-score", type=int, default=3,
                        help="Min methodology receptiveness (default 3)")

    # I/O
    parser.add_argument(
        "--journals-root",
        type=Path,
        default=Path("references/journals"),
        help="Root directory of journal entries",
    )
    parser.add_argument(
        "--format",
        choices=["table", "csv", "json", "markdown"],
        default="table",
    )
    parser.add_argument(
        "--columns",
        type=str,
        default=",".join(DEFAULT_COLUMNS),
        help=f"Output columns CSV (default: {','.join(DEFAULT_COLUMNS)})",
    )
    parser.add_argument(
        "--sort-by",
        type=str,
        default="name",
        help="Sort by field (default: name)",
    )

    return parser.parse_args()


def main() -> int:
    args = parse_args()

    files = collect_files(args.journals_root)
    if not files:
        print(f"No journal files under {args.journals_root}", file=sys.stderr)
        return 1

    records: list[JournalRecord] = []
    for path in files:
        try:
            records.append(parse_journal_file(path))
        except Exception as exc:
            print(f"Skipping {path}: {exc}", file=sys.stderr)

    filtered = [r for r in records if matches(r, args)]

    # Sort
    if args.sort_by:
        def sort_key(r: JournalRecord) -> Any:
            v = getattr(r, args.sort_by, None)
            return (v is None, v if v is not None else "")
        filtered.sort(key=sort_key, reverse=args.sort_by in {"h_index", "impact_factor", "two_yr_citedness"})

    columns = [c.strip() for c in args.columns.split(",") if c.strip()]

    if args.format == "json":
        print(render_json(filtered))
    elif args.format == "csv":
        print(render_csv(filtered, columns))
    elif args.format == "markdown":
        print(render_markdown(filtered, columns))
    else:
        print(f"=== {len(filtered)} of {len(records)} journals match ===")
        print()
        print(render_table(filtered, columns))

    return 0


if __name__ == "__main__":
    sys.exit(main())
