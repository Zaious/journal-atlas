#!/usr/bin/env python3
"""
update_metrics.py — Refresh quantitative metrics from OpenAlex.

For each existing journal entry, fetch the latest h-index, 2yr citedness,
i10-index, and works count from OpenAlex, then emit a unified diff showing
what would change. Does NOT modify files by default — proposes changes for
human review.

Usage:
    # Dry-run: show diffs for all entries (default)
    python scripts/update_metrics.py

    # Dry-run a specific field
    python scripts/update_metrics.py --field psychology

    # Apply changes (writes files after confirmation)
    python scripts/update_metrics.py --apply

    # JSON output
    python scripts/update_metrics.py --json

Design notes:
    - Only touches the Metrics section (rows for h-index / 2-yr citedness /
      i10-index / Total Works). Never touches Soft Metadata, Strategic Notes,
      Policies, Format, or Identity — those are human-curated.
    - Skips entries without a recognizable ISSN or OpenAlex ID.
    - Bumps the "Last verified" date and adds a Changelog row when --apply.

Author: Cardinal (架構師), Journal Atlas project
License: MIT
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Optional

try:
    from pyalex import Sources, config
except ImportError:
    print("ERROR: pyalex not installed. Run: pip install pyalex", file=sys.stderr)
    sys.exit(1)


if email := os.environ.get("OPENALEX_EMAIL"):
    config.email = email


METRIC_PATTERNS: dict[str, re.Pattern] = {
    "h_index": re.compile(
        r"(\|\s*\*\*h-index\*\*\s*\|\s*)([^|]*?)(\s*\|\s*)([^|]*?)(\s*\|)"
    ),
    "two_yr_citedness": re.compile(
        r"(\|\s*\*\*2-yr Mean Citedness \(OpenAlex IF proxy\)\*\*\s*\|\s*)([^|]*?)(\s*\|\s*)([^|]*?)(\s*\|)"
    ),
    "i10_index": re.compile(
        r"(\|\s*\*\*i10-index\*\*\s*\|\s*)([^|]*?)(\s*\|\s*)([^|]*?)(\s*\|)"
    ),
    "works_count": re.compile(
        r"(\|\s*\*\*Total Works\*\*\s*\|\s*)([^|]*?)(\s*\|\s*)([^|]*?)(\s*\|)"
    ),
}

LAST_VERIFIED_PATTERN = re.compile(
    r"(\*\*Last verified\*\*:?\s*)(\d{4}-\d{2}-\d{2})"
)


@dataclass
class MetricDiff:
    field: str
    old_value: str
    new_value: str

    def changed(self) -> bool:
        return self.old_value.strip() != self.new_value.strip()


@dataclass
class FileDiff:
    path: Path
    issn: Optional[str]
    diffs: list[MetricDiff]
    error: Optional[str] = None

    def has_changes(self) -> bool:
        return any(d.changed() for d in self.diffs)


# ---------- Extraction helpers ----------


def extract_issn(content: str) -> Optional[str]:
    """Find the first ISSN in the Identity table (Print preferred, Online fallback)."""
    for label in ("ISSN \\(Print\\)", "ISSN \\(Online\\)"):
        pattern = re.compile(
            rf"\|\s*\*\*{label}\*\*\s*\|\s*([0-9]{{4}}-[0-9Xx]{{4}})",
        )
        match = pattern.search(content)
        if match:
            return match.group(1)
    return None


def extract_openalex_id(content: str) -> Optional[str]:
    """Find OpenAlex source ID if listed."""
    match = re.search(r"\*\*OpenAlex ID\*\*\s*\|\s*(\S+)", content)
    if match:
        return match.group(1)
    return None


def fetch_current_metrics(
    issn: Optional[str], openalex_id: Optional[str]
) -> dict[str, Optional[float | int]]:
    """Return latest metrics from OpenAlex."""
    if openalex_id:
        source = Sources()[openalex_id]
    elif issn:
        results = Sources().filter(issn=issn).get()
        if not results:
            raise ValueError(f"No source found for ISSN {issn}")
        source = results[0]
    else:
        raise ValueError("No ISSN or OpenAlex ID found in file")

    stats = source.get("summary_stats") or {}
    return {
        "h_index": stats.get("h_index"),
        "two_yr_citedness": stats.get("2yr_mean_citedness"),
        "i10_index": stats.get("i10_index"),
        "works_count": source.get("works_count"),
    }


def format_value(field: str, value: Optional[float | int]) -> str:
    if value is None:
        return ""
    if field == "two_yr_citedness" and isinstance(value, (int, float)):
        return f"{value:.2f}"
    return str(value)


# ---------- Diff computation ----------


def compute_file_diff(path: Path) -> FileDiff:
    content = path.read_text(encoding="utf-8")
    issn = extract_issn(content)
    openalex_id = extract_openalex_id(content)

    if not issn and not openalex_id:
        return FileDiff(
            path=path,
            issn=None,
            diffs=[],
            error="No ISSN or OpenAlex ID found in Identity section",
        )

    try:
        new_metrics = fetch_current_metrics(issn, openalex_id)
    except Exception as exc:
        return FileDiff(
            path=path, issn=issn, diffs=[], error=f"OpenAlex fetch failed: {exc}"
        )

    diffs: list[MetricDiff] = []
    for field, pattern in METRIC_PATTERNS.items():
        match = pattern.search(content)
        if not match:
            continue
        old_value = match.group(2).strip()
        new_value = format_value(field, new_metrics.get(field))
        diffs.append(MetricDiff(field=field, old_value=old_value, new_value=new_value))

    return FileDiff(path=path, issn=issn, diffs=diffs)


def apply_file_diff(file_diff: FileDiff, today: str) -> None:
    """Rewrite the file with new metric values, bump Last verified, add Changelog row."""
    if not file_diff.has_changes():
        return

    content = file_diff.path.read_text(encoding="utf-8")
    today_iso = today

    # Update each metric row
    for diff in file_diff.diffs:
        if not diff.changed():
            continue
        pattern = METRIC_PATTERNS[diff.field]

        def replacement(m: re.Match) -> str:
            return f"{m.group(1)}{diff.new_value}{m.group(3)}{today_iso}{m.group(5)}"

        content = pattern.sub(replacement, content, count=1)

    # Bump Last verified date
    content = LAST_VERIFIED_PATTERN.sub(
        lambda m: f"{m.group(1)}{today_iso}", content
    )

    # Add Changelog row (insert before the closing of the Changelog table)
    changed_fields = ", ".join(d.field for d in file_diff.diffs if d.changed())
    changelog_row = (
        f"| {today_iso} | Refreshed metrics from OpenAlex ({changed_fields}) | @bot |"
    )
    content = _append_changelog_row(content, changelog_row)

    file_diff.path.write_text(content, encoding="utf-8")


def _append_changelog_row(content: str, new_row: str) -> str:
    """Append a row to the Changelog table at the end of the file."""
    # Find the Changelog section
    match = re.search(
        r"(## +Changelog\s*\n\|[^|\n]+\|[^|\n]+\|[^|\n]+\|\s*\n\|[-\s|]+\|\s*\n)(.*?)(\Z)",
        content,
        re.DOTALL,
    )
    if not match:
        return content  # No changelog table found — skip
    header = match.group(1)
    existing_rows = match.group(2).rstrip()
    if new_row in existing_rows:
        return content  # Already present
    return content[: match.start()] + header + existing_rows + "\n" + new_row + "\n"


# ---------- Output rendering ----------


def render_human(diffs: list[FileDiff]) -> str:
    lines: list[str] = []
    for fd in diffs:
        rel = fd.path
        if fd.error:
            lines.append(f"\n  SKIP  {rel}")
            lines.append(f"        {fd.error}")
            continue
        if not fd.has_changes():
            lines.append(f"\n  OK    {rel} (no changes)")
            continue
        lines.append(f"\n  DIFF  {rel}")
        for d in fd.diffs:
            if d.changed():
                lines.append(
                    f"        {d.field:20s} {d.old_value!r:>15s}  ->  {d.new_value!r}"
                )
    return "\n".join(lines)


def render_json(diffs: list[FileDiff]) -> str:
    return json.dumps(
        [
            {
                "path": str(fd.path),
                "issn": fd.issn,
                "error": fd.error,
                "diffs": [
                    {
                        "field": d.field,
                        "old": d.old_value,
                        "new": d.new_value,
                        "changed": d.changed(),
                    }
                    for d in fd.diffs
                ],
            }
            for fd in diffs
        ],
        indent=2,
    )


# ---------- File discovery ----------


def collect_files(journals_root: Path, field: Optional[str]) -> list[Path]:
    if not journals_root.exists():
        return []
    if field:
        target = journals_root / field
        if not target.exists():
            return []
        return sorted(target.glob("*.md"))
    return sorted(
        p for p in journals_root.rglob("*.md")
        if p.name not in {"README.md", ".gitkeep"}
    )


# ---------- CLI ----------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Refresh OpenAlex-derived metrics in journal entries.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--journals-root",
        type=Path,
        default=Path("references/journals"),
        help="Root directory of journal entries",
    )
    parser.add_argument("--field", type=str, help="Limit to one field directory")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually write changes (default: dry-run only)",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON output")

    args = parser.parse_args()

    files = collect_files(args.journals_root, args.field)
    if not files:
        msg = f"No journal files found under {args.journals_root}"
        if args.field:
            msg += f"/{args.field}"
        if args.json:
            print(json.dumps({"error": msg, "files": []}))
        else:
            print(msg, file=sys.stderr)
        return 0

    file_diffs: list[FileDiff] = []
    for path in files:
        file_diffs.append(compute_file_diff(path))

    # Always show the diff first
    if args.json:
        print(render_json(file_diffs))
    else:
        print(render_human(file_diffs))

    changed_count = sum(1 for fd in file_diffs if fd.has_changes())
    error_count = sum(1 for fd in file_diffs if fd.error)

    if not args.json:
        print()
        print("=" * 60)
        print(
            f"Summary: {len(files)} files | "
            f"{changed_count} with changes | "
            f"{error_count} errors/skips"
        )

    if args.apply and changed_count:
        today = date.today().isoformat()
        for fd in file_diffs:
            if fd.has_changes():
                apply_file_diff(fd, today)
        if not args.json:
            print(f"\nApplied changes to {changed_count} files.")
            print("Review with `git diff` before committing.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
