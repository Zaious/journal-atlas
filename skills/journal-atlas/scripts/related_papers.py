#!/usr/bin/env python3
"""
related_papers.py — Find papers within a target journal that are most relevant
                    to a topic / set of keywords.

Useful when:
  - Writing a cover letter: "We engage with [PCS's recent X, Y, Z papers]"
  - Pre-submission: "Has this journal published similar work in the last 5 years?"
  - Validating a journal fit before submission: "Are my themes actually being
    published here recently, or am I drawn by historical reputation?"

Output: ranked list of papers from the target journal, sorted by recency
+ citation count + topic relevance to the user's keywords.

Usage:
    # Recent embodied-cognition papers in PCS
    python scripts/related_papers.py \\
        --journal phenomenology-and-the-cognitive-sciences \\
        --keywords "embodied cognition,self-state,4E"

    # Limit to last 3 years, top 5
    python scripts/related_papers.py \\
        --journal review-of-general-psychology \\
        --keywords "autoethnography,integrative theory" \\
        --years 3 --top-n 5

    # By ISSN if you don't know the slug
    python scripts/related_papers.py \\
        --issn 1568-7759 \\
        --keywords "phenomenology,embodiment"

    # Markdown for embedding in a cover letter draft
    python scripts/related_papers.py \\
        --journal qualitative-inquiry \\
        --keywords "autoethnography,sensitive topics" \\
        --format markdown

Author: Cardinal (架構師), Journal Atlas project
License: MIT
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Optional

try:
    from pyalex import Sources, Works, config
except ImportError:
    print("ERROR: pyalex not installed. Run: pip install pyalex", file=sys.stderr)
    sys.exit(1)

# UTF-8 stdout on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass


if email := os.environ.get("OPENALEX_EMAIL"):
    config.email = email


@dataclass
class PaperHit:
    title: str
    year: Optional[int]
    citations: int
    doi: Optional[str]
    url: Optional[str]
    abstract: Optional[str]
    authors: list[str]
    matched_keywords: list[str]
    relevance_score: float

    def as_dict(self) -> dict:
        return {
            "title": self.title,
            "year": self.year,
            "citations": self.citations,
            "doi": self.doi,
            "url": self.url,
            "authors": self.authors,
            "matched_keywords": self.matched_keywords,
            "relevance_score": round(self.relevance_score, 3),
            "abstract": self.abstract,
        }


# ---------- ISSN / slug resolution ----------


def resolve_issn_from_slug(journals_root: Path, slug: str) -> Optional[str]:
    """Find the ISSN for a given journal slug or name substring."""
    if not journals_root.exists():
        return None
    q = slug.lower().replace("_", "-")
    candidates = []
    for f in journals_root.rglob("*.md"):
        if f.name in {"README.md", ".gitkeep"}:
            continue
        if q in f.stem.lower():
            candidates.append(f)
    if not candidates:
        # Try name substring
        for f in journals_root.rglob("*.md"):
            if f.name in {"README.md", ".gitkeep"}:
                continue
            content = f.read_text(encoding="utf-8")
            m = re.search(r"^# +(.+?)\s*$", content, re.MULTILINE)
            if m and q in m.group(1).lower():
                candidates.append(f)
    if len(candidates) == 0:
        return None
    if len(candidates) > 1:
        print(
            f"Ambiguous --journal '{slug}'. Candidates: "
            + ", ".join(c.stem for c in candidates),
            file=sys.stderr,
        )
        return None

    content = candidates[0].read_text(encoding="utf-8")
    # Try ISSN (Print) then (Online)
    for label in [r"ISSN \(Print\)", r"ISSN \(Online\)"]:
        m = re.search(
            rf"\|\s*\*\*{label}\*\*\s*\|\s*([0-9]{{4}}-[0-9Xx]{{4}})",
            content,
        )
        if m:
            return m.group(1)
    return None


# ---------- OpenAlex query ----------


def resolve_source_id(issn: str) -> str:
    sources = Sources().filter(issn=issn).get()
    if not sources:
        raise ValueError(f"No OpenAlex source for ISSN {issn}")
    return sources[0]["id"]


def fetch_papers_in_window(source_id: str, start_date: str, end_date: str) -> list[dict]:
    """Page through Works for a source within a date window."""
    works: list[dict] = []
    query = (
        Works()
        .filter(
            primary_location={"source": {"id": source_id}},
            from_publication_date=start_date,
            to_publication_date=end_date,
        )
        .select(
            [
                "id",
                "title",
                "doi",
                "publication_year",
                "cited_by_count",
                "abstract_inverted_index",
                "authorships",
            ]
        )
    )
    for page in query.paginate(per_page=200, n_max=5_000):
        works.extend(page)
    return works


def reconstruct_abstract(inverted_index: Optional[dict]) -> Optional[str]:
    """OpenAlex stores abstracts as inverted index; reconstruct flat text."""
    if not inverted_index:
        return None
    positions: dict[int, str] = {}
    for word, pos_list in inverted_index.items():
        for pos in pos_list:
            positions[pos] = word
    if not positions:
        return None
    max_pos = max(positions)
    return " ".join(positions.get(i, "") for i in range(max_pos + 1)).strip()


# ---------- Scoring ----------


def score_paper(
    work: dict, keywords: list[str], year_cutoff: int
) -> tuple[float, list[str]]:
    """Compute relevance score and return list of matched keywords.

    Score components:
      - Keyword match count (title + abstract): up to 0.6
      - Recency (linear decay over 5 years): up to 0.25
      - Citation count (log-scaled): up to 0.15

    All weighted to keep score in [0, 1] roughly.
    """
    title = (work.get("title") or "").lower()
    abstract = reconstruct_abstract(work.get("abstract_inverted_index")) or ""
    text_blob = (title + " " + abstract.lower()).strip()

    matched = []
    for kw in keywords:
        if kw.lower() in text_blob:
            matched.append(kw)

    keyword_score = 0.0
    if keywords:
        keyword_score = min(1.0, len(matched) / max(1, len(keywords) * 0.5)) * 0.60
        # Bonus for title hits
        title_hits = sum(1 for kw in keywords if kw.lower() in title)
        if title_hits:
            keyword_score = min(0.60, keyword_score + 0.10 * title_hits)

    # Recency
    year = work.get("publication_year")
    recency_score = 0.0
    if year:
        years_ago = max(0, date.today().year - year)
        if years_ago <= 5:
            recency_score = (1.0 - years_ago / 5.0) * 0.25

    # Citation (log scale)
    citations = work.get("cited_by_count") or 0
    import math
    citation_score = min(0.15, math.log1p(citations) / 10.0 * 0.15)

    total = keyword_score + recency_score + citation_score
    return total, matched


# ---------- Main ----------


def find_related(
    issn: str, keywords: list[str], years: int, top_n: int
) -> list[PaperHit]:
    today = date.today()
    start = (today - timedelta(days=365 * years)).isoformat()
    end = today.isoformat()

    source_id = resolve_source_id(issn)
    works = fetch_papers_in_window(source_id, start, end)

    hits: list[PaperHit] = []
    for w in works:
        score, matched = score_paper(w, keywords, today.year)
        if score < 0.05 or not matched:
            continue
        authors = []
        for au in (w.get("authorships") or [])[:4]:
            name = (au.get("author") or {}).get("display_name")
            if name:
                authors.append(name)
        hits.append(
            PaperHit(
                title=w.get("title") or "(no title)",
                year=w.get("publication_year"),
                citations=w.get("cited_by_count") or 0,
                doi=w.get("doi"),
                url=(w.get("doi") and w["doi"]) or w.get("id"),
                abstract=reconstruct_abstract(w.get("abstract_inverted_index")),
                authors=authors,
                matched_keywords=matched,
                relevance_score=score,
            )
        )

    hits.sort(key=lambda h: -h.relevance_score)
    return hits[:top_n]


# ---------- Output ----------


def render_human(hits: list[PaperHit], journal_label: str, keywords: list[str]) -> str:
    if not hits:
        return f"\nNo papers in '{journal_label}' matched the keywords {keywords}."
    lines = [
        f"\nMost related papers in {journal_label}",
        f"  Keywords: {', '.join(keywords)}",
        f"  Showing top {len(hits)}",
        "",
    ]
    for i, h in enumerate(hits, 1):
        authors_str = ", ".join(h.authors[:3])
        if len(h.authors) > 3:
            authors_str += " et al."
        lines.append(f"{i}. [{h.year}] {h.title}")
        if authors_str:
            lines.append(f"   {authors_str}")
        lines.append(
            f"   Score: {h.relevance_score:.2f}  "
            f"Citations: {h.citations}  "
            f"Matched: {', '.join(h.matched_keywords)}"
        )
        if h.doi:
            lines.append(f"   DOI: {h.doi}")
        lines.append("")
    return "\n".join(lines)


def render_markdown(hits: list[PaperHit], journal_label: str, keywords: list[str]) -> str:
    if not hits:
        return f"*No papers in {journal_label} matched.*"
    lines = [
        f"## Related papers in {journal_label}",
        f"**Keywords**: {', '.join(keywords)}",
        "",
    ]
    for i, h in enumerate(hits, 1):
        authors_str = ", ".join(h.authors[:3])
        if len(h.authors) > 3:
            authors_str += " et al."
        link = f"[DOI]({h.doi})" if h.doi else ""
        lines.append(f"{i}. **{h.title}** ({h.year}) — {authors_str}. Citations: {h.citations}. {link}")
        lines.append(f"   - Matched: {', '.join(h.matched_keywords)}")
        lines.append("")
    return "\n".join(lines)


def render_json(hits: list[PaperHit], journal_label: str, keywords: list[str]) -> str:
    return json.dumps(
        {
            "journal": journal_label,
            "keywords": keywords,
            "results": [h.as_dict() for h in hits],
        },
        indent=2,
    )


# ---------- CLI ----------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Find papers in a target journal most relevant to keywords.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--journal", type=str, help="Slug or name substring of the journal entry")
    group.add_argument("--issn", type=str, help="ISSN (skips slug resolution)")

    parser.add_argument("--keywords", required=True, type=str, help="Comma-separated keywords")
    parser.add_argument("--years", type=int, default=5, help="Years to look back (default 5)")
    parser.add_argument("--top-n", type=int, default=8)
    parser.add_argument(
        "--journals-root",
        type=Path,
        default=Path("references/journals"),
    )
    parser.add_argument("--format", choices=["text", "markdown", "json"], default="text")

    args = parser.parse_args()
    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
    if not keywords:
        print("ERROR: --keywords cannot be empty", file=sys.stderr)
        return 2

    if args.issn:
        issn = args.issn
        label = f"ISSN {issn}"
    else:
        issn = resolve_issn_from_slug(args.journals_root, args.journal)
        if not issn:
            print(
                f"Could not resolve ISSN for journal '{args.journal}'. "
                "Try --issn directly.",
                file=sys.stderr,
            )
            return 2
        label = args.journal

    try:
        hits = find_related(issn, keywords, args.years, args.top_n)
    except Exception as exc:
        print(f"Query failed: {exc}", file=sys.stderr)
        return 1

    if args.format == "json":
        print(render_json(hits, label, keywords))
    elif args.format == "markdown":
        print(render_markdown(hits, label, keywords))
    else:
        print(render_human(hits, label, keywords))

    return 0


if __name__ == "__main__":
    sys.exit(main())
