"""Screening backtest (docs/status/SCORING_2026-11.md): six neutral queries across fields, top 10 each.

Prints, per query, the top 10 with tier, score, coverage and the topic_density
value (None = topical relevance unknown, 0 = the venue's listed topics do not
include the paper's). Summary: how many of each top 5 have unknown or zero
topical relevance. Run before and after a scoring change and diff.

    python demo/backend/backtest_screening.py <label>   # also writes backtest-<label>.json
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import main  # noqa: E402
import fit_score  # noqa: E402

QUERIES = {
    # Topics are real names from demo/backend/topic_vocabulary.json, as the
    # extraction stage aligns a description to them in production.
    "hci-older-adults": {"topics": ["Technology Use by Older Adults", "Aging and Gerontology Research", "Voice and Speech Disorders"], "methodology": "mixed-methods", "word_count": 8000, "apc_budget": 0},
    "edu-teacher-feedback": {"topics": ["Student Assessment and Feedback", "Teacher Professional Development and Motivation", "Educational Assessment and Improvement"], "methodology": "qualitative", "word_count": 7000, "apc_budget": 0},
    "phil-testimony": {"topics": ["Epistemology, Ethics, and Metaphysics", "Feminist Epistemology and Gender Studies"], "methodology": "theoretical", "word_count": 9000, "apc_budget": 0},
    "psych-sleep-memory": {"topics": ["Sleep and Wakefulness Research", "Cognitive Functions and Memory"], "methodology": "experimental", "word_count": 6000, "apc_budget": 0},
    "econ-labor": {"topics": ["Employment, Labor, and Gender Studies", "Economic Growth and Productivity"], "methodology": "quantitative", "word_count": 9000, "apc_budget": 0},
    "games-toxicity": {"topics": ["online games", "player communities", "toxic behavior"], "methodology": "qualitative", "word_count": 8000, "apc_budget": 0},
}

out = {}
for q, attrs in QUERIES.items():
    paper = fit_score.Paper.from_dict(attrs)
    ranked = main._score_against(paper)[:10]
    rows = []
    for c in ranked:
        tier = fit_score.detect_tier(c.path.read_text(encoding="utf-8")).split(" ")[0]
        td = c.dimension_scores.get("topic_density")
        rows.append({
            "name": c.name, "tier": tier, "score": round(c.score, 1),
            "coverage": round(fit_score.score_coverage(c.dimension_scores, fit_score.DEFAULT_WEIGHTS), 2),
            "topic": None if td is None else round(td),
        })
    out[q] = rows

label = sys.argv[1] if len(sys.argv) > 1 else "run"
for q, rows in out.items():
    top5 = rows[:5]
    unknown = sum(r["topic"] is None for r in top5)
    zero = sum(r["topic"] == 0 for r in top5)
    pos = sum((r["topic"] or 0) > 0 for r in top5)
    print(f"== {q}: top 5 -> relevant {pos}, unknown {unknown}, zero {zero}")
    for i, r in enumerate(rows, 1):
        print(f"  {i:2d} {r['score']:5.1f} cov {r['coverage']:.2f} topic {str(r['topic']):>4s} {r['tier'][:9]:9s} {r['name'][:55]}")
Path(f"backtest-{label}.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
