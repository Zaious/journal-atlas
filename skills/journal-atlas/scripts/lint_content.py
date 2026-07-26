#!/usr/bin/env python3
"""
lint_content.py — Content-semantics checks beyond validate_structure.py's
schema checks: does the DATA make sense, not just the file's SHAPE.

validate_structure.py confirms every required section/field exists; it
can't tell an honestly-blank cell from a confidently-wrong one, or a
disclosed-thin-evidence AI-Researched entry from one that quietly dropped
its confidence score. This is a stdlib-only, offline check (no pyalex) so
it can run in CI on every push.

Checks:
  1. **Uncited high score.** A Methodological Preferences row scored 4-5, or
     a Sensitive Topics row rated "High", with no digit or URL in its
     Evidence column — an unsupported high-confidence claim, exactly what
     enrich_methodology_evidence.py's asymmetric-capping discipline (never
     auto-assign 4-5/High from a count alone) is designed to prevent from
     being introduced in the first place. Mirrors that script's own
     is_uncited() heuristic.
  2. **Unfilled placeholder inside a Tier 1 entry.** Tier 1 means deep
     evidence harvesting — a literal "*(pending)*" / "*(fill manually)*"
     surviving in one means the entry is presented as complete but isn't.
  3. **AI-Researched entry with no signal_quality score.** The entire point
     of that lineage label is a stated, checkable confidence number; a file
     carrying the banner without one is indistinguishable from a banner
     that was copy-pasted without the substance behind it.

Usage:
    python lint_content.py [--json] [paths...]
Exit code 1 if any violation found (CI-friendly); 0 otherwise.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

sys.path.insert(0, os.path.dirname(__file__))
import fit_score  # noqa: E402 - reuse its section/tier parsing, don't reimplement

JOURNALS_ROOT = os.path.join(os.path.dirname(__file__), "..", "references", "journals")


CONTENTLESS_WORD_LIMIT = 3


def is_uncited(evidence_cell: str) -> bool:
    """True if the evidence cell has no checkable citation (no digit, no
    URL). Mirrors enrich_methodology_evidence.py's helper of the same name —
    duplicated here (not imported) so this linter stays pyalex-free and can
    run in CI without network access."""
    if not evidence_cell or evidence_cell in ("", "*(pending)*", "(pending)"):
        return True
    return not re.search(r"\d", evidence_cell) and "http" not in evidence_cell.lower()


def is_contentless(evidence_cell: str) -> bool:
    """True if the justification is a template default rather than a reason.

    Stricter than is_uncited() on purpose. enrich_methodology_evidence.py
    already learned (and documented) that a bare no-digit/no-URL test can't
    tell a hand-authored, checkable prose claim — "Methodology and Research
    Practice section explicitly welcomes critical work", which names a
    specific journal section anyone can go read — from a contentless
    template default like "Family norm". Flagging the former produces noise
    that trains people to ignore the linter.

    So: uncited AND under a handful of content words. Measured against this
    corpus (2026-07-27), that splits 536 raw uncited-high-score hits into
    377 genuinely contentless ("Family norm", "Welcomed", "Core") and 159
    that say something specific enough to check or argue with.
    """
    if not is_uncited(evidence_cell):
        return False
    return len(re.findall(r"[A-Za-z0-9'-]+", evidence_cell)) <= CONTENTLESS_WORD_LIMIT


def check_uncited_high_scores(content: str) -> list[str]:
    """High-confidence scores (4-5 / "High") justified by a template default
    rather than a reason. See is_contentless() for why the bar is
    "contentless", not merely "no digit"."""
    violations = []
    methodology = fit_score._extract_subsection(content, "Methodological Preferences") or ""
    for line in methodology.splitlines():
        m = re.match(r"\|\s*([^|]+?)\s*\|\s*([0-5])\s*\|([^|]*)\|", line)
        if m and int(m.group(2)) >= 4 and is_contentless(m.group(3).strip()):
            violations.append(f"Methodological Preferences > {m.group(1).strip()}: "
                               f"scored {m.group(2)}, justified only by {m.group(3).strip()!r}")

    sensitive = fit_score._extract_subsection(content, "Sensitive Topics") or ""
    for line in sensitive.splitlines():
        m = re.match(r"\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|([^|]*)\|", line)
        if not m:
            continue
        topic, receptiveness = m.group(1).strip(), m.group(2).strip()
        if topic.lower() in ("topic category",) or re.fullmatch(r"-+", topic):
            continue
        if receptiveness.lower() == "high" and is_contentless(m.group(3).strip()):
            violations.append(f"Sensitive Topics > {topic}: rated High, "
                               f"justified only by {m.group(3).strip()!r}")
    return violations


def check_tier1_placeholders(content: str) -> list[str]:
    if fit_score.detect_tier(content) != "Tier 1 (evidence-backed)":
        return []
    soft_metadata = fit_score.extract_h2_block(content, "Soft Metadata")
    hits = re.findall(r"\*\(pending\)\*|\*\(fill manually\)\*", soft_metadata)
    if hits:
        return [f"Tier 1 entry but Soft Metadata still has {len(hits)} unfilled placeholder(s)"]
    return []


def check_ai_researched_has_signal_quality(content: str) -> list[str]:
    if fit_score.detect_tier(content) != "AI-Researched":
        return []
    if not re.search(r"signal_quality", content, re.IGNORECASE):
        return ["AI-Researched banner present but no signal_quality score found anywhere in the file"]
    return []


CHECKS = [check_uncited_high_scores, check_tier1_placeholders, check_ai_researched_has_signal_quality]


def lint_file(path: str) -> list[str]:
    content = open(path, encoding="utf-8").read()
    violations = []
    for check in CHECKS:
        violations.extend(check(content))
    return violations


def collect_files(paths: list[str]) -> list[str]:
    if not paths:
        paths = [os.path.join(JOURNALS_ROOT, "**", "*.md")]
    files = []
    for p in paths:
        if os.path.isdir(p):
            files.extend(glob.glob(os.path.join(p, "**", "*.md"), recursive=True))
        elif any(ch in p for ch in "*?["):
            files.extend(glob.glob(p, recursive=True))
        else:
            files.append(p)
    return sorted(f for f in files if not f.endswith("TEMPLATE.md"))


def relkey(path: str) -> str:
    """Path relative to references/journals/, forward-slashed — stable across
    machines and OSes so the baseline file is portable (not tied to a
    particular absolute path or Windows-vs-POSIX separator)."""
    return os.path.relpath(path, JOURNALS_ROOT).replace(os.sep, "/")


DEFAULT_BASELINE_PATH = os.path.join(os.path.dirname(__file__), "lint_baseline.json")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*", help="Files, directories, or globs (default: all of references/journals/)")
    ap.add_argument("--json", action="store_true", help="Emit JSON output for CI tooling")
    ap.add_argument("--baseline", default=DEFAULT_BASELINE_PATH,
                    help=f"Baseline JSON path (default: {DEFAULT_BASELINE_PATH}). "
                         "Fail only on violations beyond it — see --update-baseline.")
    ap.add_argument("--no-baseline", action="store_true", help="Ignore the baseline; fail on ANY violation")
    ap.add_argument("--update-baseline", action="store_true",
                    help="Write current per-file violation counts as the new baseline, then exit 0")
    args = ap.parse_args()

    files = collect_files(args.paths)
    results: dict[str, list[str]] = {}
    for path in files:
        violations = lint_file(path)
        if violations:
            results[relkey(path)] = violations

    if args.update_baseline:
        baseline = {key: len(v) for key, v in results.items()}
        with open(args.baseline, "w", encoding="utf-8") as f:
            json.dump(baseline, f, indent=2, sort_keys=True)
        total = sum(baseline.values())
        print(f"Baseline written to {args.baseline}: {len(baseline)} files, {total} known violations "
              "(pre-existing debt, not newly introduced — see docs/ATLAS_V2_DESIGN.md §9 on evidence quality)",
              file=sys.stderr)
        return 0

    baseline = {} if args.no_baseline else _load_baseline(args.baseline)
    newly_bad = {
        key: violations for key, violations in results.items()
        if len(violations) > baseline.get(key, 0)
    }

    if args.json:
        print(json.dumps({"all": results, "newly_bad": newly_bad}, indent=2, ensure_ascii=False))
    else:
        for key, violations in results.items():
            marker = " [NEW/WORSE]" if key in newly_bad else ""
            print(f"\n{key}{marker}")
            for v in violations:
                print(f"  - {v}")
        total = sum(len(v) for v in results.values())
        new_total = sum(len(v) for v in newly_bad.values())
        print(f"\n=== {len(files)} files checked | {len(results)} files with violations ({total} total) | "
              f"{len(newly_bad)} files newly bad vs baseline ({new_total} new/worse violations) ===",
              file=sys.stderr)

    return 1 if newly_bad else 0


def _load_baseline(path: str) -> dict[str, int]:
    if not os.path.exists(path):
        return {}
    return json.loads(open(path, encoding="utf-8").read())


if __name__ == "__main__":
    sys.exit(main())
