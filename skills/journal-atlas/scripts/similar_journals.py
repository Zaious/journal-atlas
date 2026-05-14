#!/usr/bin/env python3
"""
similar_journals.py — Find journals most similar to a given target.

Useful when:
  - "PCS rejected me — what's most like PCS?" (broader than the curated
    Rejection Fallback Chain)
  - "I'm considering PCS but want to see comparable venues" (lateral discovery)
  - "Show me journals topically and structurally close to Theory & Psychology"

Similarity is computed across three signals:
  1. Topic Jaccard — overlap of OpenAlex top-topics sets (Subject Density)
  2. Methodology — cosine similarity over methodology receptiveness vectors
  3. Structural — same publisher, same OA model, h-index proximity, word-limit
                  proximity, AI policy alignment

The output is a ranked list with score breakdown so users can see WHY a
journal is similar — not just that the model thinks so.

Usage:
    # Find journals like PCS
    python scripts/similar_journals.py --target phenomenology-and-the-cognitive-sciences

    # Limit search to one field
    python scripts/similar_journals.py --target theory-and-psychology --field psychology

    # Show top 10 with full score breakdown
    python scripts/similar_journals.py --target qualitative-inquiry --top-n 10

    # JSON for tooling
    python scripts/similar_journals.py --target review-of-general-psychology --format json

Filename matching:
    --target can be a partial filename (slug) or a substring of the journal
    title. The script picks the unambiguous match; if multiple match,
    the candidates are listed and the script exits with code 2.

Author: Cardinal (架構師), Journal Atlas project
License: MIT
"""

from __future__ import annotations

import argparse
import io
import json
import math
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

# UTF-8 stdout on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass


PENDING_MARKERS = {"*(pending)*", "(pending)"}


# ---------- Data structures ----------


@dataclass
class JournalProfile:
    path: Path
    slug: str  # filename stem
    name: str
    field: str
    publisher: Optional[str] = None
    oa_model: Optional[str] = None
    h_index: Optional[int] = None
    word_limit: Optional[int] = None
    has_ai_permission_gate: Optional[bool] = None
    has_zero_embargo: Optional[bool] = None
    topics: set[str] = field(default_factory=set)
    methodology_scores: dict[str, int] = field(default_factory=dict)


@dataclass
class SimilarityScore:
    target: str
    candidate: str
    candidate_path: Path
    total: float = 0.0
    breakdown: dict[str, float] = field(default_factory=dict)
    shared_topics: list[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        return {
            "candidate": self.candidate,
            "candidate_path": str(self.candidate_path),
            "total_score": round(self.total, 3),
            "breakdown": {k: round(v, 3) for k, v in self.breakdown.items()},
            "shared_topics": self.shared_topics,
        }


# ---------- Parsing ----------


def parse_profile(path: Path) -> JournalProfile:
    content = path.read_text(encoding="utf-8")
    profile = JournalProfile(path=path, slug=path.stem, name=_h1(content) or path.stem, field=path.parent.name)

    profile.publisher = _table_value(content, "Publisher")
    profile.h_index = _to_int(_table_value(content, "h-index"))
    profile.word_limit = _to_int(_table_value(content, "Word limit"))

    # OA model
    oa_section = _subsection(content, "Open Access") or content
    if re.search(r"\bModel\b[^|]*\|\s*Full OA", oa_section, re.IGNORECASE):
        profile.oa_model = "full_oa"
    elif re.search(r"\bModel\b[^|]*\|\s*Hybrid", oa_section, re.IGNORECASE):
        profile.oa_model = "hybrid"
    elif re.search(r"\bModel\b[^|]*\|\s*Subscription\b", oa_section, re.IGNORECASE):
        profile.oa_model = "subscription"
    elif re.search(r"subscription[^|]*\|\s*\$?\s*0", oa_section, re.IGNORECASE):
        profile.oa_model = "hybrid"
    else:
        profile.oa_model = "unknown"

    # AI gate
    ai_section = _subsection(content, "AI Policy")
    if ai_section:
        m = re.search(r"\|\s*\*\*Explicit permission gate\??\*\*\s*\|\s*([^|]+)", ai_section, re.IGNORECASE)
        if m:
            v = m.group(1).strip().lower()
            if v.startswith("yes"):
                profile.has_ai_permission_gate = True
            elif v.startswith("no"):
                profile.has_ai_permission_gate = False

    # Zero embargo
    pp = _subsection(content, "Preprint Policy") or content
    profile.has_zero_embargo = bool(
        re.search(r"zero[- ]embargo|no embargo|0\s*months?\s*embargo", pp, re.IGNORECASE)
    )

    # Topics
    topics_section = _subsection(content, "Top Topics")
    if topics_section:
        for line in topics_section.splitlines():
            m = re.match(r"\|\s*([^|]+?)\s*\|\s*[\d,]+", line)
            if m:
                topic = m.group(1).strip()
                if topic and not topic.lower().startswith(("topic", "----")):
                    profile.topics.add(topic.lower())

    # Methodology
    method_section = _subsection(content, "Methodological Preferences")
    if method_section:
        for line in method_section.splitlines():
            m = re.match(r"\|\s*([^|]+?)\s*\|\s*([0-5])\s*\|", line)
            if m:
                method = m.group(1).strip().lower()
                profile.methodology_scores[method] = int(m.group(2))

    return profile


def _h1(content: str) -> Optional[str]:
    m = re.search(r"^# +(.+?)\s*$", content, re.MULTILINE)
    return m.group(1).strip() if m else None


def _table_value(content: str, label: str) -> Optional[str]:
    pattern = re.compile(rf"\|\s*\*?\*?{label}\*?\*?\s*\|\s*([^|]+?)\s*\|", re.IGNORECASE)
    m = pattern.search(content)
    if not m:
        return None
    v = m.group(1).strip()
    return None if v in PENDING_MARKERS or not v else v


def _subsection(content: str, name: str) -> Optional[str]:
    pattern = re.compile(
        rf"^#{{2,3}} +{re.escape(name)}\s*$(.*?)(?=^#{{2,3}} +|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    m = pattern.search(content)
    return m.group(1) if m else None


def _to_int(s: Optional[str]) -> Optional[int]:
    if not s:
        return None
    m = re.search(r"(\d[\d,]*)", s)
    return int(m.group(1).replace(",", "")) if m else None


# ---------- Similarity scoring ----------

# Tunable weights. Sum should be ~= 1.0 (raw outputs in [0,1]).
WEIGHTS = {
    "topic_jaccard": 0.40,
    "methodology_cosine": 0.20,
    "publisher_match": 0.10,
    "oa_model_match": 0.10,
    "h_index_proximity": 0.10,
    "word_limit_proximity": 0.05,
    "ai_policy_match": 0.03,
    "embargo_match": 0.02,
}


def topic_jaccard(a: set[str], b: set[str]) -> float:
    if not a and not b:
        return 0.0
    inter = a & b
    union = a | b
    if not union:
        return 0.0
    return len(inter) / len(union)


def methodology_cosine(a: dict[str, int], b: dict[str, int]) -> float:
    keys = set(a) | set(b)
    if not keys:
        return 0.0
    va = [a.get(k, 0) for k in keys]
    vb = [b.get(k, 0) for k in keys]
    dot = sum(x * y for x, y in zip(va, vb))
    na = math.sqrt(sum(x * x for x in va))
    nb = math.sqrt(sum(y * y for y in vb))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def numeric_proximity(a: Optional[float], b: Optional[float], max_diff: float) -> float:
    """Returns 1.0 when equal, 0.0 when >= max_diff apart."""
    if a is None or b is None:
        return 0.0
    diff = abs(a - b)
    if diff >= max_diff:
        return 0.0
    return 1.0 - (diff / max_diff)


def publisher_match(a: Optional[str], b: Optional[str]) -> float:
    if not a or not b:
        return 0.0
    # Normalize a bit — first token
    norm = lambda s: s.split()[0].lower() if s else ""
    return 1.0 if norm(a) == norm(b) else 0.0


def equal_or_zero(a: Any, b: Any) -> float:
    if a is None or b is None:
        return 0.0
    return 1.0 if a == b else 0.0


def compute_similarity(target: JournalProfile, candidate: JournalProfile) -> SimilarityScore:
    score = SimilarityScore(
        target=target.slug,
        candidate=candidate.slug,
        candidate_path=candidate.path,
        shared_topics=sorted(target.topics & candidate.topics),
    )

    score.breakdown["topic_jaccard"] = topic_jaccard(target.topics, candidate.topics)
    score.breakdown["methodology_cosine"] = methodology_cosine(
        target.methodology_scores, candidate.methodology_scores
    )
    score.breakdown["publisher_match"] = publisher_match(target.publisher, candidate.publisher)
    score.breakdown["oa_model_match"] = equal_or_zero(target.oa_model, candidate.oa_model)
    score.breakdown["h_index_proximity"] = numeric_proximity(
        target.h_index, candidate.h_index, max_diff=150
    )
    score.breakdown["word_limit_proximity"] = numeric_proximity(
        target.word_limit, candidate.word_limit, max_diff=10000
    )
    score.breakdown["ai_policy_match"] = equal_or_zero(
        target.has_ai_permission_gate, candidate.has_ai_permission_gate
    )
    score.breakdown["embargo_match"] = equal_or_zero(
        target.has_zero_embargo, candidate.has_zero_embargo
    )

    score.total = sum(score.breakdown[k] * WEIGHTS[k] for k in score.breakdown)
    return score


# ---------- File discovery ----------


def collect_profiles(journals_root: Path, field: Optional[str] = None) -> list[JournalProfile]:
    if not journals_root.exists():
        return []
    if field:
        target_dir = journals_root / field
        files = sorted(target_dir.glob("*.md")) if target_dir.exists() else []
    else:
        files = sorted(p for p in journals_root.rglob("*.md") if p.name not in {"README.md", ".gitkeep"})
    profiles = []
    for f in files:
        try:
            profiles.append(parse_profile(f))
        except Exception as exc:
            print(f"Skipping {f}: {exc}", file=sys.stderr)
    return profiles


def find_target(profiles: list[JournalProfile], query: str) -> JournalProfile:
    """Find a single profile matching the query string (slug or name substring)."""
    q = query.lower().replace("_", "-")
    # Exact slug
    for p in profiles:
        if p.slug.lower() == q:
            return p
    # Slug substring
    slug_matches = [p for p in profiles if q in p.slug.lower()]
    if len(slug_matches) == 1:
        return slug_matches[0]
    # Name substring
    name_matches = [p for p in profiles if q in p.name.lower()]
    if len(name_matches) == 1:
        return name_matches[0]
    # Combined ambiguity
    candidates = list({p.slug for p in slug_matches + name_matches})
    if not candidates:
        raise ValueError(f"No journal matches '{query}'")
    raise ValueError(
        f"Ambiguous query '{query}'. Candidates:\n  " + "\n  ".join(sorted(candidates))
    )


# ---------- Output ----------


def render_human(target: JournalProfile, scores: list[SimilarityScore], top_n: int) -> str:
    lines: list[str] = [f"\nMost similar to: {target.name}  ({target.slug})", ""]
    top = scores[:top_n]
    if not top:
        return f"No comparable journals found for {target.slug}."

    for i, s in enumerate(top, 1):
        # Find the candidate name from path
        cname = _h1(s.candidate_path.read_text(encoding="utf-8")) or s.candidate
        lines.append(f"{i}. {cname}  ({s.candidate})")
        lines.append(f"   Total similarity: {s.total:.3f}")
        # Show top 3 contributing breakdown items
        breakdown_sorted = sorted(s.breakdown.items(), key=lambda kv: -kv[1] * WEIGHTS[kv[0]])
        for k, v in breakdown_sorted[:4]:
            contribution = v * WEIGHTS[k]
            lines.append(f"     {k:25s} raw={v:.2f}  weighted={contribution:.3f}")
        if s.shared_topics:
            shared_preview = ", ".join(s.shared_topics[:3])
            more = f" (+{len(s.shared_topics) - 3} more)" if len(s.shared_topics) > 3 else ""
            lines.append(f"     shared topics: {shared_preview}{more}")
        lines.append("")
    return "\n".join(lines)


def render_json(target: JournalProfile, scores: list[SimilarityScore], top_n: int) -> str:
    return json.dumps(
        {
            "target": {"slug": target.slug, "name": target.name, "field": target.field},
            "weights": WEIGHTS,
            "results": [s.as_dict() for s in scores[:top_n]],
        },
        indent=2,
    )


# ---------- CLI ----------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Find journals most similar to a given target.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--target", required=True, help="Slug or name substring of the target journal")
    parser.add_argument(
        "--field",
        type=str,
        help="Restrict comparison set to one field (psychology / hci / qualitative-methods)",
    )
    parser.add_argument("--top-n", type=int, default=5)
    parser.add_argument(
        "--journals-root",
        type=Path,
        default=Path("references/journals"),
    )
    parser.add_argument("--format", choices=["text", "json"], default="text")

    args = parser.parse_args()

    profiles = collect_profiles(args.journals_root, field=None)  # parse all
    if not profiles:
        print(f"No journals under {args.journals_root}", file=sys.stderr)
        return 1

    try:
        target = find_target(profiles, args.target)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    candidates = [p for p in profiles if p.slug != target.slug]
    if args.field:
        candidates = [p for p in candidates if p.field == args.field]
    if not candidates:
        print(f"No comparison candidates available.", file=sys.stderr)
        return 1

    scores = sorted(
        (compute_similarity(target, c) for c in candidates),
        key=lambda s: -s.total,
    )

    if args.format == "json":
        print(render_json(target, scores, args.top_n))
    else:
        print(render_human(target, scores, args.top_n))

    return 0


if __name__ == "__main__":
    sys.exit(main())
