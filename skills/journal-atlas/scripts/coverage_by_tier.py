# -*- coding: utf-8 -*-
"""Reproduce Table 1: evidence coverage by tier.

The paper's central empirical claim is that coverage splits on the tier
boundary -- Tier 1 and Tier 2 entries are evidenced across most of the weighted
schema, AI-Researched entries across roughly 40% of it. That claim was
measurable but not reproducible: the numbers lived in a one-off run, and
Availability claimed the repository holds the script behind Table 1 when it did
not. This is that script.

Coverage is not a property of an entry alone. Four of the six dimensions score
the entry *against a manuscript*, so an empty query drives them all to unknown
and understates coverage badly -- an unconstrained Paper reports AI-Researched
at 15%, which measures the absent query, not the absent evidence. Coverage is
therefore measured against several representative profiles and reported as the
range across them, which is what Table 1's ranges mean.

    python scripts/coverage_by_tier.py
"""
import io
import os
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fit_score as F  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent / "references" / "journals"

# Spread across the fields the corpus actually covers, so no single discipline's
# vocabulary decides the result.
PROFILES = [
    ("qualitative", dict(topics=["phenomenology", "lived experience", "embodiment"],
                         methodology="qualitative")),
    ("experimental", dict(topics=["memory", "attention", "cognition"],
                          methodology="experimental")),
    ("theoretical", dict(topics=["ethics", "epistemology", "philosophy of mind"],
                         methodology="theoretical")),
    ("systems", dict(topics=["human-computer interaction", "interaction design"],
                     methodology="system building")),
]

TIER_ORDER = ["Tier 1 (evidence-backed)", "Tier 2 (community estimate)",
              "AI-Researched", "Skeleton"]
BASIS = {
    "Tier 1 (evidence-backed)": "Evidence-backed, sourced",
    "Tier 2 (community estimate)": "Community estimate, banner-marked",
    "AI-Researched": "Per-field signal quality, banner",
    "Skeleton": "Structure only",
}


def main() -> int:
    if not ROOT.is_dir():
        print("no corpus at %s" % ROOT, file=sys.stderr)
        return 1

    paths = sorted(ROOT.rglob("*.md"))
    tiers = {}
    journals = {}
    for path in paths:
        tiers[path] = F.detect_tier(io.open(path, encoding="utf-8").read())
        journals[path] = F.parse_journal_file(path)

    # tier -> profile -> mean coverage
    means = defaultdict(dict)
    counts = defaultdict(int)
    for path in paths:
        counts[tiers[path]] += 1
    for label, kwargs in PROFILES:
        paper = F.Paper(**kwargs)
        acc = defaultdict(list)
        for path in paths:
            _, dims = F.compute_score(paper, journals[path], F.DEFAULT_WEIGHTS)
            acc[tiers[path]].append(F.score_coverage(dims, F.DEFAULT_WEIGHTS))
        for tier, vals in acc.items():
            means[tier][label] = sum(vals) / len(vals)

    print("Evidence coverage by tier (n = %d), %d profiles\n"
          % (len(paths), len(PROFILES)))
    print("%-30s %5s  %-34s %s" % ("Tier", "n", "Basis", "Coverage"))
    print("-" * 96)
    for tier in TIER_ORDER:
        if tier not in counts:
            continue
        vals = [means[tier][label] for label, _ in PROFILES]
        lo, hi = min(vals) * 100, max(vals) * 100
        span = "%.0f%%" % lo if hi - lo < 1 else "%.0f-%.0f%%" % (lo, hi)
        print("%-30s %5d  %-34s %s" % (tier, counts[tier], BASIS.get(tier, ""), span))

    print("\nby profile:")
    print("%-30s %s" % ("", "  ".join("%12s" % l for l, _ in PROFILES)))
    for tier in TIER_ORDER:
        if tier not in counts:
            continue
        print("%-30s %s" % (tier, "  ".join("%11.0f%%" % (means[tier][l] * 100)
                                            for l, _ in PROFILES)))
    print("\nRead the columns, not just the range. 'systems' probes HCI topics")
    print("against a corpus that is mostly psychology and philosophy, so")
    print("topic_density comes back unknown for a query reason rather than an")
    print("evidence reason, and every tier drops together. The paper's 85-100%")
    print("and ~40% correspond to the in-domain columns, which is how the")
    print("system is actually used; the out-of-domain column is kept here")
    print("because dropping it would be choosing the flattering measurement.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
