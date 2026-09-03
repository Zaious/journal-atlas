# -*- coding: utf-8 -*-
"""Reproduce Table 1: evidence coverage by tier.

The paper's central empirical claim is that coverage splits on the tier
boundary -- curated entries are evidenced across most of the weighted schema,
AI-Researched entries across roughly 40% of it. That claim was measurable but
not reproducible: the numbers lived in a one-off run, and Availability claimed
the repository holds what is behind Table 1 when it did not.

Table 1 is a claim about *entries*: "163 entries at ...". An earlier version of
this script reported the mean coverage of each tier, which answers a different
question -- a tier whose entries are half at 100% and half at 40% has the same
mean as one whose entries all sit at 70%, and only the second is what a range
in a table normally means. This version reports the distribution over entries,
which is what the table claims.

Coverage is not a property of an entry alone. Four of the six dimensions score
the entry *against a manuscript*, so the query decides how much of the schema
is even consulted. Two things follow:

  - The reported figure pools every (entry, profile) pair in a tier across
    three in-domain profiles, and gives its median and range.
  - A fourth profile probes HCI topics against a corpus that is mostly
    psychology and philosophy. There topic_density comes back unknown for a
    *query* reason rather than an *evidence* reason, so folding it into the
    headline figure would mislabel a coverage gap in the corpus's reach as one
    in its evidence. It is reported separately rather than dropped, because
    dropping it silently would be choosing the flattering measurement -- and
    Section 6 discloses the same narrowness in prose.

    python scripts/coverage_by_tier.py
"""
import io
import os
import statistics
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fit_score as F  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent / "references" / "journals"

# Spread across the fields the corpus actually covers, so no single discipline's
# vocabulary decides the result. in_domain=False means the profile asks about a
# field the corpus does not hold; see the module docstring.
PROFILES = [
    ("qualitative", True, dict(topics=["phenomenology", "lived experience", "embodiment"],
                               methodology="qualitative")),
    ("experimental", True, dict(topics=["memory", "attention", "cognition"],
                                methodology="experimental")),
    ("theoretical", True, dict(topics=["ethics", "epistemology", "philosophy of mind"],
                               methodology="theoretical")),
    ("systems", False, dict(topics=["human-computer interaction", "interaction design"],
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


def _cell(values: list[float]) -> str:
    """Median, and the range after it when the entries actually spread."""
    med = statistics.median(values) * 100
    lo, hi = min(values) * 100, max(values) * 100
    if hi - lo < 1:
        return "%.0f%%" % med
    return "%.0f%% (%.0f-%.0f)" % (med, lo, hi)


def main() -> int:
    if not ROOT.is_dir():
        print("no corpus at %s" % ROOT, file=sys.stderr)
        return 1

    paths = sorted(ROOT.rglob("*.md"))
    tiers, journals = {}, {}
    for path in paths:
        tiers[path] = F.detect_tier(io.open(path, encoding="utf-8").read())
        journals[path] = F.parse_journal_file(path)

    counts = defaultdict(int)
    for path in paths:
        counts[tiers[path]] += 1

    # tier -> profile -> [per-entry coverage]
    per_entry = defaultdict(lambda: defaultdict(list))
    for label, _in_domain, kwargs in PROFILES:
        paper = F.Paper(**kwargs)
        for path in paths:
            _, dims = F.compute_score(paper, journals[path], F.DEFAULT_WEIGHTS)
            per_entry[tiers[path]][label].append(
                F.score_coverage(dims, F.DEFAULT_WEIGHTS))

    in_domain = [p[0] for p in PROFILES if p[1]]
    out_domain = [p[0] for p in PROFILES if not p[1]]

    print("Evidence coverage by tier (n = %d)" % len(paths))
    print("median and range over entries, pooled across %d in-domain profiles: %s\n"
          % (len(in_domain), ", ".join(in_domain)))
    print("%-30s %5s  %-34s %s" % ("Tier", "n", "Basis", "Coverage"))
    print("-" * 96)
    for tier in TIER_ORDER:
        if tier not in counts:
            continue
        pooled = [v for label in in_domain for v in per_entry[tier][label]]
        print("%-30s %5d  %-34s %s"
              % (tier, counts[tier], BASIS.get(tier, ""), _cell(pooled)))

    print("\nper profile (median over entries):")
    print("%-30s %s" % ("", "  ".join("%12s" % l for l, _, _ in PROFILES)))
    for tier in TIER_ORDER:
        if tier not in counts:
            continue
        print("%-30s %s" % (tier, "  ".join(
            "%11.0f%%" % (statistics.median(per_entry[tier][l]) * 100)
            for l, _, _ in PROFILES)))

    for label in out_domain:
        print("\n'%s' is out of domain and is NOT in the headline figure: it probes" % label)
        print("HCI topics against a corpus that is mostly psychology and philosophy, so")
        print("topic_density returns unknown for a query reason rather than an evidence")
        print("reason and every tier drops together. Section 6 discloses that narrowness")
        print("in prose; folding it in here would relabel it as missing evidence.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
