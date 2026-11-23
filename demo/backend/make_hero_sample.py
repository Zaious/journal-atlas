#!/usr/bin/env python3
"""Write the screening result shown in the home page's product shot.

The home page shows what the tool returns, the way the sibling product pages
show a real replay rather than a mock-up. This runs the real screening stage
(fit_score over the corpus on disk, no language model involved) for one fixed,
neutral example paper and writes the top candidates to
demo/frontend/src/sample/screening-sample.json, with the corpus version and the
date, so the page can caption exactly what the picture is.

The paper's attributes are written here by hand, in the shape the extraction
model produces; the ranking, scores, tiers, coverage and topic counts are the
script's real output. Re-run it whenever the corpus changes:

    python demo/backend/make_hero_sample.py
"""

from __future__ import annotations

import datetime as _dt
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import main  # noqa: E402
import fit_score  # noqa: E402

OUT = Path(__file__).resolve().parents[1] / "frontend" / "src" / "sample" / "screening-sample.json"
SHOWN = 3

# A neutral example, unrelated to any manuscript of the maintainer.
EXAMPLE = {
    "description": (
        "A mixed-methods study of how older adults use voice assistants at home: "
        "diaries and interviews with 24 households. About 8,000 words, no budget "
        "for open-access fees."
    ),
    # Shown on the Chinese page; the same example, translated.
    "description_zh": "一項關於高齡者如何在家使用語音助理的混合方法研究：24 個家戶的日記與訪談。約 8,000 字，沒有開放近用費用的預算。",
    "paper": {
        "topics": ["older adults", "voice assistants", "smart home", "technology adoption"],
        "methodology": "mixed-methods",
        "word_count": 8000,
        "apc_budget": 0,
    },
}


def main_() -> None:
    paper = fit_score.Paper.from_dict(EXAMPLE["paper"])
    ranked = main.screen_candidates(paper)
    ties = main.tie_sizes(ranked)
    cards = []
    for c in ranked[:SHOWN]:
        card = main.build_evidence_card(c.path)
        cards.append({
            "name": c.name,
            "score": round(c.score, 1),
            "coverage": fit_score.score_coverage(c.dimension_scores, fit_score.DEFAULT_WEIGHTS),
            "tied_with": ties.get(c.name, 1) - 1,
            **card,
        })
    version = main.VERSION or {}
    out = {
        "generated": _dt.date.today().isoformat(),
        "corpus": version.get("corpus_describe") or version.get("corpus_commit"),
        "returned": len(ranked),  # the screening returns its top N; this is N, not the corpus size
        "example": EXAMPLE,
        "candidates": cards,
        # What the tool lists back as "not stated, so not applied" for this example,
        # in the backend's own words (it does not translate them).
        "unstated": main.unstated_constraints(paper),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({len(cards)} of {len(ranked)} candidates)")
    for c in cards:
        print(f"  {c['score']:5.1f}  {round(c['coverage'] * 100):3d}%  {c['tier'][:22]:22s}  {c['name']}")


if __name__ == "__main__":
    main_()
