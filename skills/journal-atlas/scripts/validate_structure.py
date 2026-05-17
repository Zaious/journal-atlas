#!/usr/bin/env python3
"""
validate_structure.py — Check journal entries against the TEMPLATE schema.

Verifies that each journal .md file under references/journals/ conforms to
the current TEMPLATE.md structure (sections present, frontmatter valid,
required fields populated, freshness date reasonable).

Usage:
    # Validate all journal entries
    python scripts/validate_structure.py

    # Validate a specific file
    python scripts/validate_structure.py references/journals/psychology/theory-and-psychology.md

    # Validate a glob pattern
    python scripts/validate_structure.py "references/journals/psychology/*.md"

    # JSON output (for CI machine-readable output)
    python scripts/validate_structure.py --json

Exit codes:
    0 — all files passed (warnings allowed)
    1 — one or more files had errors (CI failure)

Design notes:
    - Errors fail CI. Warnings do not.
    - Schema version is read from TEMPLATE.md (first line: `<!-- schema: vX.Y -->`).
    - Each journal file must declare its own schema version in the same format.
    - This script is intentionally narrow: it validates structure, not content.
      Soft Metadata accuracy is a human review responsibility.

Author: Cardinal (架構師), Journal Atlas project
License: MIT (this script) / see LICENSE for content
"""

from __future__ import annotations

import argparse
import glob
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Optional


# ---------- Required structure (must match TEMPLATE.md v1.3) ----------

REQUIRED_H2_SECTIONS: list[str] = [
    "Identity",
    "Metrics",
    "Policies",
    "Format",
    "Subject Density",
    "Soft Metadata",
    "Strategic Notes",
    "Changelog",
]

# v1.3: Conference entries (under conferences/ subtree) also require this H2
CONFERENCE_REQUIRED_H2: list[str] = [
    "Conference Specifics",
]

CONFERENCE_REQUIRED_H3_UNDER_CONFSPECS: list[str] = [
    "Submission Cycle",
    "Program Committee",
    "Submission Format",
    "Review Format",
]

REQUIRED_H3_UNDER_POLICIES: list[str] = [
    "Peer Review",
    "AI Policy",
    "Preprint Policy",
    "Open Access",
]

REQUIRED_H3_UNDER_METRICS: list[str] = [
    "Review Cycle Time",
    "Publication Frequency",
]

REQUIRED_H3_UNDER_STRATEGIC_NOTES: list[str] = [
    "Hard Blockers",
    "Soft Tax",
    "Best Suited For",
    "Not Recommended For",
    "Rejection Fallback Chain",
]

REQUIRED_H3_UNDER_SOFT_METADATA: list[str] = [
    "Epistemological & Political Leanings",
    "Framing Requirements",
    "Methodological Preferences",
    "Voice & Style",
    "Reviewer Pool Characteristics",
    "Sensitive Topics",
    "Practical Concerns",
]

FRESHNESS_WARN_DAYS: int = 365 + 180  # 18 months — match SKILL.md threshold
FRESHNESS_HARD_LIMIT_DAYS: int = 365 * 3  # 3 years — beyond this is an error


# ---------- Validation results ----------


@dataclass
class FileResult:
    path: Path
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.errors

    def as_dict(self) -> dict:
        return {
            "path": str(self.path),
            "passed": self.passed,
            "errors": self.errors,
            "warnings": self.warnings,
        }


# ---------- Validation logic ----------


def get_template_schema_version(repo_root: Path) -> Optional[str]:
    """Read the current schema version from TEMPLATE.md."""
    template = repo_root / "TEMPLATE.md"
    if not template.exists():
        return None
    first_line = template.read_text(encoding="utf-8").splitlines()[0]
    match = re.match(r"<!--\s*schema:\s*(v\d+\.\d+)\s*-->", first_line)
    return match.group(1) if match else None


def validate_file(path: Path, expected_schema: Optional[str]) -> FileResult:
    """Validate a single journal entry file."""
    result = FileResult(path=path)

    if not path.exists():
        result.errors.append(f"File not found: {path}")
        return result

    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        result.errors.append(f"File is not valid UTF-8: {exc}")
        return result

    if not content.strip():
        result.errors.append("File is empty")
        return result

    # 1. Schema version check
    first_line = content.splitlines()[0] if content else ""
    schema_match = re.match(r"<!--\s*schema:\s*(v\d+\.\d+)\s*-->", first_line)
    if not schema_match:
        result.errors.append(
            "First line must be a schema marker like '<!-- schema: v1.2 -->'"
        )
    elif expected_schema and schema_match.group(1) != expected_schema:
        result.warnings.append(
            f"Schema version is {schema_match.group(1)}; "
            f"current TEMPLATE is {expected_schema}. Consider updating."
        )

    # 2. Required H2 sections (all entries)
    h2_sections = set(re.findall(r"^## +(.+?)\s*$", content, re.MULTILINE))
    for required in REQUIRED_H2_SECTIONS:
        if required not in h2_sections:
            result.errors.append(f"Missing required H2 section: '{required}'")

    # 2b. Conference-specific H2 (only for conferences/ subtree entries)
    is_conference_entry = "conferences" in path.parts
    if is_conference_entry:
        for required in CONFERENCE_REQUIRED_H2:
            if required not in h2_sections:
                result.errors.append(
                    f"Missing required H2 section: '{required}' "
                    "(required for entries under conferences/)"
                )
        # Also check H3 under Conference Specifics
        _check_h3_under_h2(
            content,
            "Conference Specifics",
            CONFERENCE_REQUIRED_H3_UNDER_CONFSPECS,
            result,
            severity="error",
        )

    # 3. Required H3 subsections under specific H2s
    _check_h3_under_h2(
        content, "Metrics", REQUIRED_H3_UNDER_METRICS, result, severity="error"
    )
    _check_h3_under_h2(
        content,
        "Policies",
        REQUIRED_H3_UNDER_POLICIES,
        result,
        severity="error",
    )
    _check_h3_under_h2(
        content,
        "Soft Metadata",
        REQUIRED_H3_UNDER_SOFT_METADATA,
        result,
        severity="error",
    )
    _check_h3_under_h2(
        content,
        "Strategic Notes",
        REQUIRED_H3_UNDER_STRATEGIC_NOTES,
        result,
        severity="error",
    )

    # 4. Last verified date present and parseable
    last_verified = _extract_last_verified(content)
    if not last_verified:
        result.errors.append(
            "Missing or unparseable 'Last verified' date in the header "
            "(expected format: 'Last verified: YYYY-MM-DD')"
        )
    else:
        age_days = (date.today() - last_verified).days
        if age_days < 0:
            result.warnings.append(
                f"'Last verified' date is in the future: {last_verified}"
            )
        elif age_days > FRESHNESS_HARD_LIMIT_DAYS:
            result.errors.append(
                f"'Last verified' date is {age_days} days old "
                f"(> {FRESHNESS_HARD_LIMIT_DAYS} day hard limit). "
                "Re-verify before merging."
            )
        elif age_days > FRESHNESS_WARN_DAYS:
            result.warnings.append(
                f"'Last verified' date is {age_days} days old "
                f"(> {FRESHNESS_WARN_DAYS} day warn threshold). "
                "Consider re-verifying."
            )

    # 5. Changelog has at least one entry row
    changelog_section = _extract_section(content, "Changelog")
    if changelog_section:
        # Look for a row that isn't the header/separator
        rows = [
            line for line in changelog_section.splitlines()
            if line.strip().startswith("|") and "---" not in line
        ]
        # Subtract the header row
        if len(rows) < 2:
            result.errors.append(
                "Changelog must contain at least one entry row (beyond the header)"
            )

    # 6. Filename naming convention (lowercase kebab-case)
    filename = path.stem
    if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", filename):
        result.warnings.append(
            f"Filename '{filename}' is not lowercase kebab-case "
            "(see CONTRIBUTING.md naming convention)"
        )

    return result


def _check_h3_under_h2(
    content: str,
    h2_name: str,
    required_h3: list[str],
    result: FileResult,
    severity: str = "error",
) -> None:
    """Verify that specified H3 subsections exist under a given H2 section."""
    section_content = _extract_section(content, h2_name)
    if not section_content:
        # The H2 itself missing is caught elsewhere; don't double-report
        return
    h3_sections = set(re.findall(r"^### +(.+?)\s*$", section_content, re.MULTILINE))
    for required in required_h3:
        if required not in h3_sections:
            message = f"Missing required H3 '{required}' under '{h2_name}'"
            if severity == "error":
                result.errors.append(message)
            else:
                result.warnings.append(message)


def _extract_section(content: str, h2_name: str) -> Optional[str]:
    """Extract the content of an H2 section (up to the next H2 or EOF)."""
    pattern = re.compile(
        rf"^## +{re.escape(h2_name)}\s*$(.*?)(?=^## +|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(content)
    return match.group(1) if match else None


def _extract_last_verified(content: str) -> Optional[date]:
    """Find the 'Last verified: YYYY-MM-DD' line near the top of the file."""
    match = re.search(
        r"\*\*Last verified\*\*:?\s*(\d{4}-\d{2}-\d{2})",
        content,
    )
    if not match:
        return None
    try:
        return datetime.strptime(match.group(1), "%Y-%m-%d").date()
    except ValueError:
        return None


# ---------- File discovery ----------


def collect_files(paths: list[str], repo_root: Path) -> list[Path]:
    """Expand globs and validate each path exists."""
    files: list[Path] = []
    if not paths:
        # Default: all journal entries
        default_glob = str(repo_root / "references" / "journals" / "**" / "*.md")
        files = [Path(p) for p in glob.glob(default_glob, recursive=True)]
    else:
        for pattern in paths:
            matched = glob.glob(pattern, recursive=True)
            if matched:
                files.extend(Path(p) for p in matched)
            elif Path(pattern).exists():
                files.append(Path(pattern))
    # Filter out non-.md files just in case
    return sorted(p for p in files if p.suffix == ".md" and p.name != "TEMPLATE.md")


# ---------- Output rendering ----------


def render_human(results: list[FileResult]) -> str:
    """Render results in human-readable form."""
    lines: list[str] = []
    error_count = 0
    warn_count = 0
    pass_count = 0

    for result in results:
        rel = result.path
        if result.passed and not result.warnings:
            lines.append(f"  PASS  {rel}")
            pass_count += 1
        elif result.passed and result.warnings:
            lines.append(f"  WARN  {rel} ({len(result.warnings)} warnings)")
            for w in result.warnings:
                lines.append(f"        - {w}")
            warn_count += len(result.warnings)
            pass_count += 1
        else:
            lines.append(
                f"  FAIL  {rel} "
                f"({len(result.errors)} errors, {len(result.warnings)} warnings)"
            )
            for e in result.errors:
                lines.append(f"        ERROR: {e}")
            for w in result.warnings:
                lines.append(f"        WARN:  {w}")
            error_count += len(result.errors)
            warn_count += len(result.warnings)

    lines.append("")
    lines.append("=" * 60)
    failing = sum(1 for r in results if not r.passed)
    lines.append(
        f"Summary: {pass_count} passed, {failing} failed | "
        f"{error_count} errors, {warn_count} warnings | "
        f"{len(results)} files checked"
    )
    return "\n".join(lines)


def render_json(results: list[FileResult]) -> str:
    """Render results as JSON."""
    return json.dumps(
        {
            "summary": {
                "total": len(results),
                "passed": sum(1 for r in results if r.passed),
                "failed": sum(1 for r in results if not r.passed),
                "total_errors": sum(len(r.errors) for r in results),
                "total_warnings": sum(len(r.warnings) for r in results),
            },
            "files": [r.as_dict() for r in results],
        },
        indent=2,
    )


# ---------- CLI ----------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate journal entries against TEMPLATE schema.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Files or globs to validate (default: all under references/journals/)",
    )
    parser.add_argument(
        "--json", action="store_true", help="Emit JSON output for CI tooling"
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Repository root (default: current directory)",
    )

    args = parser.parse_args()

    expected_schema = get_template_schema_version(args.repo_root)
    if expected_schema is None and not args.json:
        print(
            "Note: could not read schema version from TEMPLATE.md. "
            "Skipping schema-version checks.",
            file=sys.stderr,
        )

    files = collect_files(args.paths, args.repo_root)
    if not files:
        if args.json:
            print(json.dumps({"summary": {"total": 0}, "files": []}))
        else:
            print("No journal files found to validate.")
        return 0

    results = [validate_file(p, expected_schema) for p in files]

    if args.json:
        print(render_json(results))
    else:
        print(render_human(results))

    # Non-zero exit if any file failed
    return 1 if any(not r.passed for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
