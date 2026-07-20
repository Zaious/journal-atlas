#!/usr/bin/env python3
"""
fit_score.py — Compute fit scores for a paper against journal entries.

Reads paper attributes (JSON or CLI args), parses journal markdown files,
applies hard-constraint filters, and ranks remaining journals by weighted
soft-fit score.

Status: v0.1 — functional skeleton. The scoring weights and hard-constraint
detection rules are reasonable defaults, but they have NOT been validated
against ground-truth submission outcomes. Once we have seed data and real
backtest cases (e.g. SSS/ASAF reconstruction by 賢者), tune the weights and
extraction rules accordingly. See TODO markers below.

Usage:
    # From a JSON file describing the paper
    python scripts/fit_score.py --paper-json my-paper.json

    # From CLI args (subset of attributes)
    python scripts/fit_score.py \\
        --topics "embodied cognition,collaborative learning" \\
        --methodology theoretical \\
        --word-count 12000 \\
        --apc-budget 0

    # JSON output
    python scripts/fit_score.py --paper-json my-paper.json --json

Paper JSON schema:
    {
      "topics": ["embodied cognition", "collaborative learning"],
      "methodology": "theoretical" | "autoethnography" | "mixed" | ...,
      "word_count": 12000,
      "apc_budget": 0,
      "ai_usage": true,
      "ai_disclosed": true,
      "sensitive_content": ["BDSM", "drug use"],
      "irb": false,
      "opsec_concerns": false,
      "preprint_intent": true,
      "timeline_priority": "fast" | "normal" | "flexible",
      "fields": ["psychology", "hci"]
    }

Author: Cardinal (架構師), Journal Atlas project
License: MIT
"""

from __future__ import annotations

import argparse
import glob
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional


# ---------- Default scoring weights ----------
# TODO: Validate these against backtest cases (賢者 Task C). Current values are
# educated guesses informed by the SSS/ASAF submission experience.

DEFAULT_WEIGHTS: dict[str, float] = {
    "topic_density": 0.25,
    "methodology_fit": 0.20,
    "reviewer_pool": 0.15,
    "sensitive_topic_tolerance": 0.15,
    "voice_compatibility": 0.10,
    "strategic_factors": 0.15,
}

# Score range per dimension: 0-100. Total weighted score also 0-100.


# ---------- Data structures ----------


@dataclass
class Paper:
    """A paper described by its attributes — input to scoring."""
    topics: list[str] = field(default_factory=list)
    methodology: Optional[str] = None
    word_count: Optional[int] = None
    apc_budget: Optional[int] = None
    oa_required: bool = False  # True = author needs immediate OA (no paywall acceptable)
    ai_usage: bool = False
    ai_disclosed: bool = True
    sensitive_content: list[str] = field(default_factory=list)
    irb: bool = True  # Default True = paper has IRB if applicable
    opsec_concerns: bool = False
    preprint_intent: bool = False
    timeline_priority: str = "normal"  # fast / normal / flexible
    fields: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict) -> "Paper":
        return cls(
            topics=data.get("topics", []),
            methodology=data.get("methodology"),
            word_count=data.get("word_count"),
            apc_budget=data.get("apc_budget"),
            oa_required=data.get("oa_required", False),
            ai_usage=data.get("ai_usage", False),
            ai_disclosed=data.get("ai_disclosed", True),
            sensitive_content=data.get("sensitive_content", []),
            irb=data.get("irb", True),
            opsec_concerns=data.get("opsec_concerns", False),
            preprint_intent=data.get("preprint_intent", False),
            timeline_priority=data.get("timeline_priority", "normal"),
            fields=data.get("fields", []),
        )


@dataclass
class JournalScore:
    path: Path
    name: str
    score: float = 0.0
    dimension_scores: dict[str, float] = field(default_factory=dict)
    eliminated: bool = False
    elimination_reason: Optional[str] = None
    warnings: list[str] = field(default_factory=list)
    # Cost annotation for hybrid journals — surfaced in output so user sees both paths
    oa_model: Optional[str] = None
    apc_subscription_usd: Optional[int] = None
    apc_oa_usd: Optional[int] = None

    def cost_note(self) -> str:
        """Short human-readable cost annotation."""
        if self.oa_model == "hybrid":
            oa = f"${self.apc_oa_usd:,}" if self.apc_oa_usd else "?"
            return f"$0 via subscription / {oa} via OA"
        if self.oa_model == "subscription":
            return "$0 (subscription only — paywalled)"
        if self.oa_model == "full_oa":
            oa = f"${self.apc_oa_usd:,}" if self.apc_oa_usd else "?"
            return f"{oa} (full OA)"
        return "unknown"

    def as_dict(self) -> dict:
        return {
            "path": str(self.path),
            "name": self.name,
            "score": round(self.score, 2),
            "dimensions": {k: round(v, 2) for k, v in self.dimension_scores.items()},
            "eliminated": self.eliminated,
            "elimination_reason": self.elimination_reason,
            "warnings": self.warnings,
            "oa_model": self.oa_model,
            "apc_subscription_usd": self.apc_subscription_usd,
            "apc_oa_usd": self.apc_oa_usd,
            "cost_note": self.cost_note(),
        }


# ---------- Markdown parsing helpers ----------


def parse_journal_file(path: Path) -> dict[str, Any]:
    """Extract structured data from a journal markdown file.

    Returns a dict with keys like 'name', 'word_limit', 'apc_usd',
    'topics' (list), 'sensitive_topics' (dict), etc. Best-effort parsing —
    falls back to None for fields it can't find.

    TODO: This parser is regex-based and brittle. Once seed data lands,
    replace with a proper structured markdown parser.
    """
    content = path.read_text(encoding="utf-8")

    name = _extract_h1(content) or path.stem

    listed_apc = _extract_listed_apc(content)
    has_subscription_path = _detect_subscription_path(content)
    oa_model = _detect_oa_model(content, has_subscription_path)

    return {
        "name": name,
        "word_limit": _extract_word_limit(content),
        "apc_usd_oa": listed_apc,  # Cost if OA path is chosen
        "apc_usd_subscription": 0 if has_subscription_path else None,  # $0 if available
        "oa_model": oa_model,  # "subscription" / "hybrid" / "full_oa" / "unknown"
        "has_subscription_path": has_subscription_path,
        "has_ai_permission_gate": _detect_ai_permission_gate(content),
        "irb_strictness": _extract_irb_strictness(content),
        "topics": _extract_top_topics(content),
        "methodology_scores": _extract_methodology_scores(content),
        "sensitive_topics": _extract_sensitive_topics(content),
        "first_person_acceptance": _extract_first_person_score(content),
        "review_time_months": _extract_review_time(content),
    }


def _extract_h1(content: str) -> Optional[str]:
    match = re.search(r"^# +(.+?)\s*$", content, re.MULTILINE)
    return match.group(1).strip() if match else None


def _extract_word_limit(content: str) -> Optional[int]:
    """Find a word limit number near 'Word limit' label."""
    # Look for patterns like "Word limit | 12,000" or "Word limit | 8000"
    pattern = re.search(
        r"Word limit.*?\|\s*[^0-9|]*([\d,]+)", content, re.IGNORECASE
    )
    if not pattern:
        return None
    try:
        return int(pattern.group(1).replace(",", ""))
    except ValueError:
        return None


def _extract_listed_apc(content: str) -> Optional[int]:
    """Find the listed OA APC (the price an author pays if they choose OA).

    For hybrid journals this is the OA-path cost; for full-OA journals this
    is the only price. Subscription-only journals have no listed APC.
    """
    oa_section = _extract_subsection(content, "Open Access")
    text = oa_section or content
    pattern = re.search(r"APC.*?\$\s*([\d,]+)", text, re.IGNORECASE)
    if not pattern:
        return None
    try:
        return int(pattern.group(1).replace(",", ""))
    except ValueError:
        return None


def _detect_subscription_path(content: str) -> bool:
    """True if the journal offers a $0 subscription submission path.

    Recognized phrasings:
      "Subscription submission cost | $0"
      "subscription publishing model, no APC charges apply"
      "Model | Subscription" / "Model | Hybrid"
    """
    oa_section = _extract_subsection(content, "Open Access")
    text = oa_section or content
    return bool(
        re.search(
            r"(subscription[^|]*\|\s*\$?\s*0\b"
            r"|subscription[^.]*no APC"
            r"|\bModel\b[^|]*\|\s*Subscription\b"
            r"|\bModel\b[^|]*\|\s*Hybrid\b)",
            text,
            re.IGNORECASE,
        )
    )


def _detect_oa_model(content: str, has_subscription_path: bool) -> str:
    """Classify the journal's OA model.

    Returns: "subscription" / "hybrid" / "full_oa" / "unknown"
    """
    oa_section = _extract_subsection(content, "Open Access") or content
    if re.search(r"\bModel\b[^|]*\|\s*Full OA", oa_section, re.IGNORECASE):
        return "full_oa"
    if re.search(r"\bModel\b[^|]*\|\s*Hybrid", oa_section, re.IGNORECASE):
        return "hybrid"
    if re.search(r"\bModel\b[^|]*\|\s*Subscription", oa_section, re.IGNORECASE):
        return "subscription"
    # Heuristic fallback when explicit Model row is missing
    if has_subscription_path:
        return "hybrid"
    return "unknown"


def effective_apc(journal: dict, oa_required: bool) -> Optional[int]:
    """Compute the price the user would actually pay given their OA preference.

    - subscription journals: $0 (regardless of oa_required, but flagged elsewhere)
    - hybrid + oa_required=False: $0 via subscription path
    - hybrid + oa_required=True: listed OA APC (must pay)
    - full_oa: listed APC regardless
    """
    model = journal.get("oa_model", "unknown")
    listed = journal.get("apc_usd_oa")
    sub = journal.get("apc_usd_subscription")

    if model == "subscription":
        return 0
    if model == "hybrid":
        return 0 if not oa_required else listed
    if model == "full_oa":
        return listed
    # Unknown model: be conservative — if subscription path exists, use it
    if sub is not None and not oa_required:
        return sub
    return listed


def _detect_ai_permission_gate(content: str) -> bool:
    """Heuristic: does the AI Policy require explicit permission?"""
    ai_section = _extract_subsection(content, "AI Policy")
    if not ai_section:
        return False
    return bool(
        re.search(r"explicit permission|permission gate|prior approval",
                  ai_section, re.IGNORECASE)
    )


def _extract_irb_strictness(content: str) -> Optional[str]:
    """Returns 'hard', 'soft', 'flexible', or None."""
    section = _extract_subsection(content, "Practical Concerns")
    if not section:
        return None
    if re.search(r"IRB.*hard", section, re.IGNORECASE):
        return "hard"
    if re.search(r"IRB.*soft", section, re.IGNORECASE):
        return "soft"
    if re.search(r"IRB.*flexible", section, re.IGNORECASE):
        return "flexible"
    return None


def _extract_top_topics(content: str) -> list[tuple[str, int]]:
    """Extract (topic, count) tuples from Subject Density > Top Topics."""
    section = _extract_subsection(content, "Top Topics")
    if not section:
        return []
    topics: list[tuple[str, int]] = []
    for line in section.splitlines():
        match = re.match(r"\|\s*([^|]+?)\s*\|\s*([\d,]+)\s*\|", line)
        if match:
            topic = match.group(1).strip()
            try:
                count = int(match.group(2).replace(",", ""))
                if topic and not topic.startswith("-") and topic.lower() != "topic":
                    topics.append((topic, count))
            except ValueError:
                continue
    return topics


def _extract_methodology_scores(content: str) -> dict[str, int]:
    """Extract methodology receptiveness scores (0-5)."""
    section = _extract_subsection(content, "Methodological Preferences")
    if not section:
        return {}
    scores: dict[str, int] = {}
    for line in section.splitlines():
        match = re.match(r"\|\s*([^|]+?)\s*\|\s*([0-5])\s*\|", line)
        if match:
            method = match.group(1).strip().lower()
            try:
                scores[method] = int(match.group(2))
            except ValueError:
                continue
    return scores


def _extract_sensitive_topics(content: str) -> dict[str, str]:
    """Extract sensitive topic receptiveness labels."""
    section = _extract_subsection(content, "Sensitive Topics")
    if not section:
        return {}
    topics: dict[str, str] = {}
    for line in section.splitlines():
        # Format: | Topic | Receptiveness | Evidence |
        match = re.match(r"\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", line)
        if match:
            topic = match.group(1).strip().lower()
            receptiveness = match.group(2).strip().lower()
            if topic and receptiveness and topic not in {"topic category", "----"}:
                topics[topic] = receptiveness
    return topics


def _extract_first_person_score(content: str) -> Optional[int]:
    """Extract first-person voice acceptance score (0-5)."""
    section = _extract_subsection(content, "Voice & Style")
    if not section:
        return None
    match = re.search(r"First-person.*?\|\s*([0-5])", section, re.IGNORECASE)
    if match:
        try:
            return int(match.group(1))
        except ValueError:
            pass
    return None


def _extract_review_time(content: str) -> Optional[float]:
    """Extract typical time-to-acceptance in months."""
    section = _extract_subsection(content, "Review Cycle Time")
    if not section:
        return None
    # Look for "Time to acceptance" row
    match = re.search(
        r"Time to acceptance.*?\|\s*([^|]+)\|",
        section, re.IGNORECASE
    )
    if not match:
        return None
    text = match.group(1).strip().lower()
    # Try to parse a number with month/week unit
    num_match = re.search(r"(\d+(?:\.\d+)?)", text)
    if not num_match:
        return None
    try:
        n = float(num_match.group(1))
        if "week" in text:
            n = n / 4.0  # weeks → months
        return n
    except ValueError:
        return None


def _extract_subsection(content: str, name: str) -> Optional[str]:
    """Extract content under an H2 or H3 section by name.

    Matches headings with a trailing suffix too, e.g. "### Top Topics
    (last 5 years)" for a lookup of "Top Topics" — TEMPLATE.md's actual
    convention includes such suffixes on several headings.
    """
    pattern = re.compile(
        rf"^#{{2,3}} +{re.escape(name)}\b[^\n]*\n(.*?)(?=^#{{2,3}} +|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(content)
    return match.group(1) if match else None


# ---------- Hard constraint checks ----------


def check_hard_constraints(paper: Paper, journal: dict[str, Any]) -> Optional[str]:
    """Return elimination reason if hard constraint fails, else None."""
    if paper.word_count and journal.get("word_limit"):
        if paper.word_count > journal["word_limit"]:
            return (
                f"word_limit too low ({journal['word_limit']:,} < "
                f"paper {paper.word_count:,})"
            )

    if paper.apc_budget is not None:
        eff_apc = effective_apc(journal, paper.oa_required)
        if eff_apc is not None and eff_apc > paper.apc_budget:
            reason = f"APC ${eff_apc:,} exceeds budget ${paper.apc_budget:,}"
            if paper.oa_required and journal.get("oa_model") == "hybrid":
                reason += " (hybrid OA path required — subscription path unavailable per user preference)"
            return reason

    if paper.ai_usage and journal.get("has_ai_permission_gate"):
        return "AI policy requires explicit permission (user did not indicate willingness to email ahead)"

    if not paper.irb and journal.get("irb_strictness") == "hard":
        return "IRB hard requirement; paper has no IRB"

    return None


# ---------- Scoring ----------


def score_topic_density(paper: Paper, journal: dict[str, Any]) -> float:
    """0-100 score based on topic keyword overlap."""
    if not paper.topics or not journal.get("topics"):
        return 50.0  # No data → neutral
    total = 0.0
    for paper_topic in paper.topics:
        best_match = 0
        for journal_topic, count in journal["topics"]:
            if paper_topic.lower() in journal_topic.lower() or \
               journal_topic.lower() in paper_topic.lower():
                best_match = max(best_match, count)
        total += min(100, best_match * 2)  # 50 articles → 100 score
    return total / len(paper.topics) if paper.topics else 50.0


def score_methodology(paper: Paper, journal: dict[str, Any]) -> float:
    """0-100 based on methodology receptiveness score (0-5 in TEMPLATE)."""
    if not paper.methodology or not journal.get("methodology_scores"):
        return 50.0
    methodology_scores = journal["methodology_scores"]
    for method_key, score in methodology_scores.items():
        if paper.methodology.lower() in method_key:
            return (score / 5.0) * 100
    return 50.0


def score_sensitive_topics(paper: Paper, journal: dict[str, Any]) -> float:
    """0-100 based on whether journal accepts the sensitive topics in paper."""
    if not paper.sensitive_content:
        return 100.0  # No sensitive content → no constraint
    if not journal.get("sensitive_topics"):
        return 30.0  # Has sensitive content but no journal data → penalize
    total = 0.0
    for topic in paper.sensitive_content:
        receptiveness = "untested"
        for journal_topic, level in journal["sensitive_topics"].items():
            if topic.lower() in journal_topic or journal_topic in topic.lower():
                receptiveness = level
                break
        score_map = {
            "high": 100, "medium": 60, "low": 20, "untested": 30, "": 30,
        }
        total += score_map.get(receptiveness, 30)
    return total / len(paper.sensitive_content)


def score_voice(paper: Paper, journal: dict[str, Any]) -> float:
    """0-100 based on first-person acceptance (TODO: refine when paper voice is known)."""
    fp_score = journal.get("first_person_acceptance")
    if fp_score is None:
        return 50.0
    return (fp_score / 5.0) * 100


def score_strategic(paper: Paper, journal: dict[str, Any]) -> float:
    """0-100 based on review speed if user prioritizes fast turnaround."""
    if paper.timeline_priority != "fast":
        return 70.0  # Neutral default
    review_time = journal.get("review_time_months")
    if review_time is None:
        return 50.0
    # 3 months or less → 100; 12 months → 0
    return max(0.0, min(100.0, 100 - (review_time - 3) * (100.0 / 9.0)))


def score_reviewer_pool(paper: Paper, journal: dict[str, Any]) -> float:
    """TODO: Implement once we have a way to match paper's theoretical framework
    against journal's Reviewer Pool Characteristics narrative.

    For now: 50 (neutral) — let other dimensions discriminate.
    """
    return 50.0


def compute_score(
    paper: Paper, journal: dict[str, Any], weights: dict[str, float]
) -> tuple[float, dict[str, float]]:
    """Compute weighted total score and per-dimension breakdown."""
    dims = {
        "topic_density": score_topic_density(paper, journal),
        "methodology_fit": score_methodology(paper, journal),
        "reviewer_pool": score_reviewer_pool(paper, journal),
        "sensitive_topic_tolerance": score_sensitive_topics(paper, journal),
        "voice_compatibility": score_voice(paper, journal),
        "strategic_factors": score_strategic(paper, journal),
    }
    total = sum(dims[k] * weights[k] for k in dims)
    return total, dims


# ---------- File discovery ----------


def collect_journals(paper: Paper, journals_root: Path) -> list[Path]:
    """Find candidate journals based on the paper's field preference."""
    if not journals_root.exists():
        return []
    if paper.fields:
        files: list[Path] = []
        for f in paper.fields:
            field_dir = journals_root / f
            if field_dir.exists():
                files.extend(field_dir.glob("*.md"))
        return sorted(p for p in files if p.name not in {"README.md"})
    # All fields
    return sorted(
        p for p in journals_root.rglob("*.md")
        if p.name not in {"README.md", ".gitkeep"}
    )


# ---------- CLI ----------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compute fit scores for a paper against journal entries.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--paper-json", type=Path, help="Path to JSON describing the paper")
    group.add_argument("--topics", type=str, help="Comma-separated topic keywords")

    parser.add_argument("--methodology", type=str, help="e.g. theoretical, autoethnography")
    parser.add_argument("--word-count", type=int)
    parser.add_argument("--apc-budget", type=int)
    parser.add_argument(
        "--require-oa",
        action="store_true",
        help=(
            "Require immediate Open Access (no paywall acceptable). Without this flag, "
            "hybrid journals are treated as $0-cost via their subscription path."
        ),
    )
    parser.add_argument("--fields", type=str, help="Comma-separated field directories to search")
    parser.add_argument(
        "--journals-root", type=Path, default=Path("references/journals")
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    parser.add_argument(
        "--top-n", type=int, default=5, help="Show top N recommendations (default 5)"
    )

    return parser.parse_args()


def build_paper(args: argparse.Namespace) -> Paper:
    if args.paper_json:
        data = json.loads(args.paper_json.read_text(encoding="utf-8"))
        return Paper.from_dict(data)
    return Paper(
        topics=[t.strip() for t in (args.topics or "").split(",") if t.strip()],
        methodology=args.methodology,
        word_count=args.word_count,
        apc_budget=args.apc_budget,
        oa_required=args.require_oa,
        fields=[f.strip() for f in (args.fields or "").split(",") if f.strip()],
    )


def main() -> int:
    args = parse_args()
    paper = build_paper(args)

    candidate_paths = collect_journals(paper, args.journals_root)
    if not candidate_paths:
        msg = (
            f"No journal files found under {args.journals_root}. "
            "Has the knowledge base been seeded yet?"
        )
        if args.json:
            print(json.dumps({"error": msg, "results": []}))
        else:
            print(msg, file=sys.stderr)
        return 1

    results: list[JournalScore] = []
    for path in candidate_paths:
        try:
            journal_data = parse_journal_file(path)
        except Exception as exc:
            print(f"Skipping {path}: parse error: {exc}", file=sys.stderr)
            continue

        js = JournalScore(
            path=path,
            name=journal_data["name"],
            oa_model=journal_data.get("oa_model"),
            apc_subscription_usd=journal_data.get("apc_usd_subscription"),
            apc_oa_usd=journal_data.get("apc_usd_oa"),
        )

        elim = check_hard_constraints(paper, journal_data)
        if elim:
            js.eliminated = True
            js.elimination_reason = elim
            results.append(js)
            continue

        total, dims = compute_score(paper, journal_data, DEFAULT_WEIGHTS)
        js.score = total
        js.dimension_scores = dims
        results.append(js)

    # Sort: passing first by score desc, then eliminated
    passing = sorted(
        (r for r in results if not r.eliminated), key=lambda r: -r.score
    )
    eliminated = [r for r in results if r.eliminated]

    if args.json:
        print(json.dumps({
            "paper": paper.__dict__,
            "weights": DEFAULT_WEIGHTS,
            "passing": [r.as_dict() for r in passing[:args.top_n]],
            "eliminated": [r.as_dict() for r in eliminated],
            "all_passing_count": len(passing),
        }, indent=2))
    else:
        oa_note = " [OA REQUIRED]" if paper.oa_required else ""
        print(
            f"=== Top {min(args.top_n, len(passing))} of {len(passing)} "
            f"candidates{oa_note} ==="
        )
        for i, r in enumerate(passing[:args.top_n], 1):
            print(f"\n{i}. {r.name}  ({r.score:.1f}/100)")
            print(f"     Cost: {r.cost_note()}")
            for dim, score in r.dimension_scores.items():
                print(f"     {dim:30s} {score:.1f}")
        if eliminated:
            print(f"\n=== Eliminated ({len(eliminated)}) ===")
            for r in eliminated:
                print(f"  - {r.name}: {r.elimination_reason}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
