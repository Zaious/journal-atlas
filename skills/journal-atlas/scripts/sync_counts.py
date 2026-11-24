#!/usr/bin/env python3
"""Keep the corpus counts that the documentation states as current in step
with the corpus.

The documents say "493 entries", "114 Sourced" and so on in prose, and every
batch of new entries left some of those sentences behind: on 2026-11-25 the
README still said "current 399 entries" and "163 entries (Sourced +
Estimated)" a month after both had changed, after several manual "update the
numbers" passes. A count that is stated as *current* is therefore wrapped in an
invisible marker and written by this script, never by hand:

    scales from current <!--n:total-->493<!--/n--> entries

Dated, historical figures ("deployed 2026-07-30 with 399 entries", the paper's
Table 1) are deliberately NOT marked: they describe a past state and must not
move.

    python skills/journal-atlas/scripts/sync_counts.py           # rewrite the marked counts
    python skills/journal-atlas/scripts/sync_counts.py --check   # exit 1 if any is stale (CI)

tests/test_sync_counts.py runs the check, so a stale or unknown marker fails CI.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import fit_score  # noqa: E402

SKILL = SCRIPTS.parent
REPO = SKILL.parents[1]
JOURNALS = SKILL / "references" / "journals"

# Every document that states current counts. A marker in any other file is not
# checked, so add the file here when you add a marker to it.
DOCUMENTS = [
    "README.md",
    "README.zh-Hant.md",
    "SEED_DATA_QUALITY.md",
    "docs/status/PROJECT_COMPLETION.md",
]

MARKER = re.compile(r"<!--n:([a-z_]+)-->(.*?)<!--/n-->")


def compute() -> dict[str, int]:
    """Counts read off the corpus on disk, by the same tier detector the scorer uses."""
    tiers: Counter[str] = Counter()
    kind: Counter[str] = Counter()
    by_tier_kind: Counter[tuple[str, str]] = Counter()
    fields: set[str] = set()
    philosophy: Counter[str] = Counter()
    first_hand = 0
    for path in JOURNALS.rglob("*.md"):
        if path.name == "TEMPLATE.md":
            continue
        text = path.read_text(encoding="utf-8")
        tier = fit_score.detect_tier(text).split(" ")[0]
        rel = path.relative_to(JOURNALS).parent.as_posix()
        k = "conference" if rel.startswith("conferences") else "journal"
        tiers[tier] += 1
        kind[k] += 1
        by_tier_kind[(tier, k)] += 1
        if k == "journal":
            fields.add(rel.split("/")[0])
        if rel == "philosophy":
            philosophy[tier] += 1
        first_hand += bool(fit_score.has_first_hand_report(text))
    return {
        "total": sum(tiers.values()),
        "journals": kind["journal"],
        "conferences": kind["conference"],
        "journal_fields": len(fields),
        "sourced": tiers["Sourced"],
        "estimated": tiers["Estimated"],
        "ai": tiers["AI-Researched"],
        "skeleton": tiers["Skeleton"],
        "curated": tiers["Sourced"] + tiers["Estimated"],
        "estimated_journals": by_tier_kind[("Estimated", "journal")],
        "estimated_conferences": by_tier_kind[("Estimated", "conference")],
        "first_hand": first_hand,
        "philosophy": sum(philosophy.values()),
        "philosophy_ai": philosophy["AI-Researched"],
        "philosophy_sourced": philosophy["Sourced"],
    }


def sync(check: bool) -> list[str]:
    counts = compute()
    problems: list[str] = []
    for rel in DOCUMENTS:
        path = REPO / rel
        text = path.read_text(encoding="utf-8")

        def replace(m: re.Match) -> str:
            key, shown = m.group(1), m.group(2)
            if key not in counts:
                problems.append(f"{rel}: unknown count <!--n:{key}--> (known: {', '.join(sorted(counts))})")
                return m.group(0)
            want = f"{counts[key]:,}" if "," in shown else str(counts[key])
            if shown != want:
                problems.append(f"{rel}: {key} says {shown}, the corpus has {want}")
            return f"<!--n:{key}-->{want}<!--/n-->"

        new = MARKER.sub(replace, text)
        if not check and new != text:
            path.write_text(new, encoding="utf-8")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--check", action="store_true", help="report stale counts and exit 1; change nothing")
    args = ap.parse_args()
    problems = sync(check=args.check)
    unknown = [p for p in problems if "unknown count" in p]
    if args.check and problems:
        print("sync_counts: stale counts (run: python skills/journal-atlas/scripts/sync_counts.py)")
        print("\n".join(f"  - {p}" for p in problems))
        return 1
    if unknown:
        print("\n".join(unknown))
        return 1
    print("sync_counts: " + ("all marked counts current" if args.check else f"{len(problems)} count(s) updated"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
