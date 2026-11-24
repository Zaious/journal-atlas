#!/usr/bin/env python3
"""
tier1_gate.py — does an entry meet the written promotion rule for Sourced?

(The file keeps its name and CLI; "Tier 1" was renamed "Sourced" on 2026-11-24.)

SEED_DATA_QUALITY.md says an entry moves to Sourced (formerly "Tier 1") when:
  - at least 5 of the 7 Soft Metadata subsections carry evidence-backed claims,
  - Reviewer Pool Characteristics cites OpenAlex publication patterns or personal
    experience (or any source URL),
  - the warning banner is gone, and a maintainer has approved.

Until now that was prose. This turns the first three into an exit code, so a
promotion is a measurement rather than a feeling. It does NOT check the fourth:
a person still has to say yes. It also does not make an entry "human verified":
passing means the claims cite counts or sources, nothing more.

"Evidence-backed subsection" here = filled (no *(pending)* / *(fill manually)*),
and at least two of its lines cite a source URL, a stated count (articles, n=,
%) or an OpenAlex-derived figure. A line that records a gap ("unreadable",
"0 reviews", "not found") does not count even if it carries a URL, and a
subsection whose only support is "(community estimate)" does not count.

Usage:
    python tier1_gate.py [--json] [--quiet] paths...
Exit code 0 if every path passes, 1 otherwise.
"""
from __future__ import annotations

import argparse
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
import fit_score  # noqa: E402
import lint_content  # noqa: E402

SUBSECTIONS = [
    "Epistemological & Political Leanings",
    "Framing Requirements",
    "Methodological Preferences",
    "Voice & Style",
    "Reviewer Pool Characteristics",
    "Sensitive Topics",
    "Practical Concerns",
]
MIN_BACKED = 5
PLACEHOLDER = re.compile(r"\*\(pending[^)]*\)\*|\*\(fill manually\)\*|\(pending\)", re.I)
COUNT = re.compile(r"\b\d[\d,]*\s*(?:articles?|article\(s\)|publications?|papers?|works|reviews?|threads?)\b|\bn\s*=\s*\d+|\d+\s*%", re.I)


# A line that records a gap (blocked page, zero results, "not found") is a
# recorded blank, not evidence, even though it often carries a URL or a number.
GAP_LINE = re.compile(
    r"unreadable|not read\b|could not|couldn.t|"
    # an HTTP status, not a number that happens to look like one ("denominator 405" is a count)
    r"(?:\bHTTP\s*|\bstatus\s*|\berror\s*|\breturn(?:s|ed)\s*)(?:40[0-9]|429|50[0-9])\b|\b(?:40[0-9]|429)\s*(?:error|forbidden|not found)|"
    r"\b0 (?:reviews|results|hits|articles)\b|"
    r"\bno (?:public |first-hand |relevant )?(?:evidence|source|data|reviews|results)\b|not found|none found|"
    r"returned (?:nothing|zero|no)\b|not available|unverified|\bblank\b|\bpending\b",
    re.I,
)
MIN_EVIDENCE_LINES = 2


def evidence_lines(body: str) -> list[str]:
    out = []
    for line in (body or "").splitlines():
        low = line.lower()
        cited = "http" in low or COUNT.search(line) or "openalex" in low
        if cited and not GAP_LINE.search(line):
            out.append(line)
    return out


def subsection_state(body: str) -> str:
    """'empty' | 'estimate' | 'backed'. Backed = at least two lines that cite
    a URL, a count or an OpenAlex figure and do not themselves record a gap."""
    text = (body or "").strip()
    if len(text) < 40 or PLACEHOLDER.search(text):
        return "empty"
    if len(evidence_lines(text)) >= MIN_EVIDENCE_LINES:
        return "backed"
    return "estimate"


def strip_banner(content: str) -> str:
    """Treat the entry as if its tier banner were already removed."""
    sm = fit_score.extract_h2_block(content, "Soft Metadata")
    banner = re.match(r"(\s*(?:>[^\n]*\n)+)", sm)
    return content.replace(banner.group(1), "", 1) if banner else content


def check(path: str) -> dict:
    content = open(path, encoding="utf-8").read()
    as_t1 = strip_banner(content)
    states = {n: subsection_state(fit_score._extract_subsection(as_t1, n)) for n in SUBSECTIONS}
    backed = sum(1 for s in states.values() if s == "backed")
    reviewer = fit_score._extract_subsection(as_t1, "Reviewer Pool Characteristics") or ""
    reviewer_ok = bool(re.search(r"openalex|personal experience|https?://", reviewer, re.I))
    strategic = fit_score.extract_h2_block(as_t1, "Strategic Notes")
    strategic_pending = len(PLACEHOLDER.findall(strategic))
    lint = [v for v in (lint_content.check_uncited_high_scores(as_t1) + lint_content.check_tier1_placeholders(
        as_t1.replace("> [!NOTE]", "").replace("> [!WARNING]", "")))]
    reasons = []
    if backed < MIN_BACKED:
        reasons.append(f"only {backed}/7 subsections evidence-backed (need {MIN_BACKED}): " +
                       ", ".join(f"{n.split(' ')[0]}={s}" for n, s in states.items() if s != "backed"))
    if not reviewer_ok:
        reasons.append("Reviewer Pool Characteristics cites no OpenAlex pattern, personal experience or URL")
    if strategic_pending:
        reasons.append(f"Strategic Notes has {strategic_pending} unfilled placeholder(s)")
    reasons += [f"lint: {v}" for v in lint]
    return {"path": path, "tier_now": fit_score.detect_tier(content), "backed": backed, "states": states,
            "pass": not reasons, "reasons": reasons}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--quiet", action="store_true", help="print failures only")
    args = ap.parse_args()
    results = [check(p) for p in args.paths]
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=1))
    else:
        for r in results:
            if r["pass"] and args.quiet:
                continue
            print(("PASS " if r["pass"] else "FAIL ") + f"{r['backed']}/7  {os.path.basename(r['path'])}  [{r['tier_now']}]")
            for why in r["reasons"]:
                print("       - " + why)
        print(f"\n{sum(r['pass'] for r in results)}/{len(results)} pass")
    return 0 if all(r["pass"] for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
