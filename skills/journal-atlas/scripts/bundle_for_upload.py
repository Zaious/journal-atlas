#!/usr/bin/env python3
"""
bundle_for_upload.py — Merge journal entries for platforms with file-count limits.

ChatGPT GPT Builder allows up to 20 knowledge files. Claude Desktop projects
have similar limits. This script merges journal markdown files into a small
number of bundle files (one per field, by default) suitable for upload.

Each bundle preserves the source filenames as headers, so the AI can still
distinguish entries within a bundle.

Usage:
    # Default: one bundle per field, output to dist/
    python scripts/bundle_for_upload.py

    # Custom output directory
    python scripts/bundle_for_upload.py --out-dir /tmp/journal-bundles

    # Single bundle of everything (for very small knowledge bases)
    python scripts/bundle_for_upload.py --single-file

    # Specify max entries per bundle (forces splitting)
    python scripts/bundle_for_upload.py --max-per-bundle 50

Output:
    Files like dist/psychology.md, dist/hci.md, etc.
    Each bundle starts with a manifest of contained journals.

Design notes:
    - We do NOT include SKILL.md or TEMPLATE.md in bundles. Those are
      copied separately or pasted into the platform's "instructions" field.
    - Output is deterministic — same input always produces same bundles.

Author: Cardinal (架構師), Journal Atlas project
License: MIT
"""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

# Maximum size suggestion before splitting (in characters; ChatGPT has 2MB/file).
# Practically, AI models slow down on huge files, so we soft-cap at 500K chars.
SOFT_BUNDLE_LIMIT_CHARS: int = 500_000


def collect_journals_by_field(journals_root: Path) -> dict[str, list[Path]]:
    """Walk references/journals/ and group .md files by field directory."""
    if not journals_root.exists():
        return {}

    by_field: dict[str, list[Path]] = {}
    for entry in sorted(journals_root.iterdir()):
        if not entry.is_dir():
            continue
        field_name = entry.name
        md_files = sorted(
            p for p in entry.glob("*.md") if p.name not in {".gitkeep", "README.md"}
        )
        if md_files:
            by_field[field_name] = md_files
    return by_field


def make_bundle(
    field_name: str, files: list[Path], bundle_index: int = 1, total_bundles: int = 1
) -> str:
    """Create a single bundle markdown file from a list of journal entries."""
    today = date.today().isoformat()
    suffix = f" (part {bundle_index} of {total_bundles})" if total_bundles > 1 else ""

    lines: list[str] = [
        f"# Journal Atlas Bundle: {field_name}{suffix}",
        "",
        f"> **Bundled on**: {today}",
        f"> **Contains**: {len(files)} journal entries",
        f"> **Source**: https://github.com/Zaious/journal-atlas",
        "",
        "## Manifest",
        "",
    ]
    for f in files:
        lines.append(f"- `{f.name}` — {_extract_title(f)}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Append each journal file with a marker so AI can locate entries
    for f in files:
        lines.append(f"<!-- BEGIN JOURNAL: {f.stem} -->")
        lines.append("")
        lines.append(f.read_text(encoding="utf-8").rstrip())
        lines.append("")
        lines.append(f"<!-- END JOURNAL: {f.stem} -->")
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def _extract_title(path: Path) -> str:
    """Get the first H1 from a journal file as its display title."""
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    except (OSError, UnicodeDecodeError):
        pass
    return path.stem


def split_into_size_limited_bundles(
    files: list[Path], limit_chars: int
) -> list[list[Path]]:
    """Split a list of files into bundles, each below the character limit."""
    bundles: list[list[Path]] = []
    current: list[Path] = []
    current_size = 0
    for f in files:
        size = f.stat().st_size
        if current_size + size > limit_chars and current:
            bundles.append(current)
            current = [f]
            current_size = size
        else:
            current.append(f)
            current_size += size
    if current:
        bundles.append(current)
    return bundles


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Bundle journal entries for upload to platforms with file count limits."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--journals-root",
        type=Path,
        default=Path("references/journals"),
        help="Root directory of journal entries (default: references/journals)",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("dist"),
        help="Output directory (default: dist/)",
    )
    parser.add_argument(
        "--single-file",
        action="store_true",
        help="Merge all journals into one file regardless of field",
    )
    parser.add_argument(
        "--max-per-bundle",
        type=int,
        default=None,
        help="Force splitting if a field has more than N entries",
    )
    parser.add_argument(
        "--size-limit-chars",
        type=int,
        default=SOFT_BUNDLE_LIMIT_CHARS,
        help=(
            f"Soft size limit per bundle in characters "
            f"(default: {SOFT_BUNDLE_LIMIT_CHARS:,})"
        ),
    )

    args = parser.parse_args()

    by_field = collect_journals_by_field(args.journals_root)
    if not by_field:
        print(
            f"No journal entries found under {args.journals_root}. Nothing to bundle.",
            file=sys.stderr,
        )
        return 1

    args.out_dir.mkdir(parents=True, exist_ok=True)

    if args.single_file:
        all_files = [f for files in by_field.values() for f in files]
        bundle = make_bundle("all-journals", all_files)
        out_path = args.out_dir / "journal-atlas-bundle.md"
        out_path.write_text(bundle, encoding="utf-8")
        print(
            f"Wrote single bundle: {out_path} "
            f"({len(all_files)} journals, {len(bundle):,} chars)"
        )
        return 0

    total_written = 0
    for field_name, files in by_field.items():
        # Decide whether to split
        if args.max_per_bundle:
            chunks = [
                files[i : i + args.max_per_bundle]
                for i in range(0, len(files), args.max_per_bundle)
            ]
        else:
            chunks = split_into_size_limited_bundles(files, args.size_limit_chars)

        for i, chunk in enumerate(chunks, start=1):
            bundle = make_bundle(field_name, chunk, i, len(chunks))
            suffix = f"-part{i}" if len(chunks) > 1 else ""
            out_path = args.out_dir / f"{field_name}{suffix}.md"
            out_path.write_text(bundle, encoding="utf-8")
            print(
                f"Wrote: {out_path} "
                f"({len(chunk)} journals, {len(bundle):,} chars)"
            )
            total_written += 1

    print()
    print(f"Done. {total_written} bundle(s) in {args.out_dir}/")
    print()
    print("Next steps:")
    print(f"  - Upload files from {args.out_dir}/ to your ChatGPT GPT or")
    print("    Claude Desktop Project's knowledge area")
    print("  - Copy SKILL.md content into the platform's instructions field")

    return 0


if __name__ == "__main__":
    sys.exit(main())
