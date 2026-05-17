#!/usr/bin/env python3
"""
Lightweight validator for Society Registry entries under references/societies/.

Each society entry must have:
  - Schema marker: <!-- schema: society-v1 -->
  - H1 (# title)
  - Required H2 sections: Identity, Mission, Venues in Journal Atlas,
    Society-wide Policies, Editorial Culture, Cross-venue Submission Strategy,
    Changelog

Run from project root:
  python scripts/validate_societies.py
"""
from pathlib import Path
import re
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
SOCIETIES_DIR = REPO_ROOT / "references" / "societies"

SCHEMA_MARKER = "<!-- schema: society-v1 -->"
REQUIRED_H2 = [
    "Identity",
    "Mission",
    "Venues in Journal Atlas",
    "Society-wide Policies",
    "Editorial Culture",
    "Cross-venue Submission Strategy",
    "Changelog",
]

H1 = re.compile(r"^# (.+?)$", re.M)
H2 = re.compile(r"^## (.+?)$", re.M)


def validate_file(path: Path) -> tuple[int, int]:
    """Return (errors, warnings) for one file."""
    txt = path.read_text(encoding="utf-8")
    errors = 0
    warnings = 0
    msgs: list[str] = []

    if SCHEMA_MARKER not in txt:
        msgs.append(f"  ERROR: missing schema marker '{SCHEMA_MARKER}'")
        errors += 1

    if not H1.search(txt):
        msgs.append("  ERROR: missing H1 (# title)")
        errors += 1

    found_h2 = set(m.group(1).strip() for m in H2.finditer(txt))
    for required in REQUIRED_H2:
        if required not in found_h2:
            msgs.append(f"  ERROR: missing required H2 section '{required}'")
            errors += 1

    if errors > 0 or warnings > 0:
        print(f"{'FAIL' if errors else 'WARN'}  {path.relative_to(REPO_ROOT)} ({errors} errors, {warnings} warnings)")
        for m in msgs:
            print(m)
    else:
        print(f"PASS  {path.relative_to(REPO_ROOT)}")

    return errors, warnings


def main() -> int:
    if not SOCIETIES_DIR.exists():
        print(f"No societies directory at {SOCIETIES_DIR}", file=sys.stderr)
        return 0

    total = 0
    failed = 0
    total_errors = 0
    total_warnings = 0
    for md in sorted(SOCIETIES_DIR.rglob("*.md")):
        if md.name.upper() == "TEMPLATE.MD":
            continue
        total += 1
        errors, warnings = validate_file(md)
        if errors > 0:
            failed += 1
        total_errors += errors
        total_warnings += warnings

    print("=" * 60)
    print(
        f"Summary: {total - failed} passed, {failed} failed | "
        f"{total_errors} errors, {total_warnings} warnings | {total} files checked"
    )
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
