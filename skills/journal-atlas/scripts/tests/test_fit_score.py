#!/usr/bin/env python3
"""
test_fit_score.py — Regression tests for fit_score.py's parsing/scoring logic.

Written after two severe, previously-undetected bugs surfaced in the same
session (2026-07-26): _detect_ai_permission_gate() matched the TEMPLATE's own
row label regardless of the actual Yes/No answer (399/399 curated files
false-positived, silently zeroing out screening results for any AI-disclosing
paper), and _extract_sensitive_topics() mis-parsed a table separator row as a
fake topic. Neither had a test catching it — this suite exists so the next
regression of this shape fails loudly instead of shipping silently.

Fixtures are small inline markdown snippets, not the real 399-file corpus —
fast, deterministic, and each one isolates a single parsing edge case.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import fit_score  # noqa: E402


# ---------- _detect_ai_permission_gate ----------


def test_ai_permission_gate_answer_no_is_not_a_gate():
    """The regression itself: the row LABEL is literally "Explicit permission
    gate?" — a naive whole-section search for that phrase matches every
    journal regardless of the answer. Must read the answer cell."""
    content = """
## Policies

### AI Policy

| Aspect | Detail |
|--------|--------|
| **Has journal-specific AI policy?** | Yes |
| **Explicit permission gate?** | No — disclosure-based (routine grammar/spell-check tools exempt) |
| **Leniency (1-5)** | 3-4 |
"""
    assert fit_score._detect_ai_permission_gate(content) is False


def test_ai_permission_gate_answer_yes_is_a_gate():
    content = """
## Policies

### AI Policy

| Aspect | Detail |
|--------|--------|
| **Explicit permission gate?** | Yes — Guilford Press publisher policy prohibits using AI to create article content |
"""
    assert fit_score._detect_ai_permission_gate(content) is True


def test_ai_permission_gate_no_ai_policy_section_is_unknown():
    content = "## Policies\n\n### Peer Review\n\n| Aspect | Detail |\n|---|---|\n"
    assert fit_score._detect_ai_permission_gate(content) is None


def test_ai_permission_gate_row_missing_is_unknown_not_false_positive():
    """If the AI Policy section exists but doesn't have the expected row in
    the expected bold-label format, don't fall back to a whole-section
    phrase search — that's exactly how the original bug happened."""
    content = """
### AI Policy

Generative AI use must be disclosed in the Acknowledgements section.
"""
    assert fit_score._detect_ai_permission_gate(content) is None


# ---------- _extract_top_topics ----------


def test_extract_top_topics_real_table():
    content = """
### Top Topics (last 5 years)

| Topic | Article Count |
|-------|--------------|
| Bioinformatics and Genomic Networks | 4763 |
| Genomics and Phylogenetic Studies | 4345 |
"""
    topics = fit_score._extract_top_topics(content)
    assert topics == [
        ("Bioinformatics and Genomic Networks", 4763),
        ("Genomics and Phylogenetic Studies", 4345),
    ]


def test_extract_top_topics_prose_only_returns_empty():
    """Hand-written qualitative framing with no numeric table — the parser
    must not hallucinate rows out of prose."""
    content = """
### Top Topics

*(Top topics ranking — see OpenAlex API for full distribution. Cultural
psychology focus; theoretical home of dialogical self theory.)*
"""
    assert fit_score._extract_top_topics(content) == []


def test_extract_top_topics_placeholder_table_returns_empty():
    content = """
### Top Topics (last 5 years)

| Topic | Article Count (2020-2025) |
|-------|--------------------------|
| Computational biology methods | *(community estimate)* |
| Bioinformatics algorithms | *(community estimate)* |
"""
    assert fit_score._extract_top_topics(content) == []


def test_extract_top_topics_heading_suffix_still_parses():
    """TEMPLATE.md's convention appends suffixes like "(last 5 years)" to
    several headings — the section-boundary regex must tolerate that."""
    content = """
### Top Topics (last 5 years)

| Topic | Article Count |
|-------|--------------|
| Neuroscience and Neuropharmacology Research | 1137 |

### Orientation
"""
    topics = fit_score._extract_top_topics(content)
    assert topics == [("Neuroscience and Neuropharmacology Research", 1137)]


# ---------- detect_tier ----------


def test_detect_tier_no_banner_is_tier_1():
    content = "## Soft Metadata\n\n### Epistemological & Political Leanings\n"
    assert fit_score.detect_tier(content) == "Tier 1 (evidence-backed)"


def test_detect_tier_warning_banner_is_tier_2():
    content = "## Soft Metadata\n\n> [!WARNING]\n> **Tier 2 (community estimate)** — adapted from family norms.\n\n### Epistemological & Political Leanings\n"
    assert fit_score.detect_tier(content) == "Tier 2 (community estimate)"


def test_detect_tier_note_with_ai_researched_text():
    content = "## Soft Metadata\n\n> [!NOTE]\n> **AI-Researched (2026-07-13)** — per-journal sourced facts.\n\n### Epistemological & Political Leanings\n"
    assert fit_score.detect_tier(content) == "AI-Researched"


def test_detect_tier_note_without_ai_researched_text_is_skeleton():
    content = "## Soft Metadata\n\n> [!NOTE]\n> Auto-generated scaffold, not yet filled.\n\n### Epistemological & Political Leanings\n"
    assert fit_score.detect_tier(content) == "Skeleton"


# ---------- _extract_sensitive_topics ----------


def test_sensitive_topics_separator_row_is_not_a_fake_topic():
    """Regression: a 16-dash separator row was previously parsed as a topic
    named "----------------" because the exclusion check only matched a
    literal 4-dash string."""
    content = """
### Sensitive Topics

| Topic Category | Receptiveness | Evidence |
|----------------|---------------|----------|
| BDSM / Kink | Low | 0 articles found |
| Suicide / Self-harm | Medium | 3 articles 2021-2026 |
"""
    topics = fit_score._extract_sensitive_topics(content)
    assert "----------------" not in topics
    assert "topic category" not in topics
    assert topics["bdsm / kink"] == "low"
    assert topics["suicide / self-harm"] == "medium"


def test_sensitive_topics_pipe_style_separator_also_excluded():
    content = """
### Sensitive Topics

| Topic Category | Receptiveness | Evidence |
|----------------|---------------|----------|
| Drug use | High | Family norm |
"""
    topics = fit_score._extract_sensitive_topics(content)
    assert "----------------" not in topics
    assert topics["drug use"] == "high"


# ---------- score_topic_density ----------


def test_topic_density_no_paper_topics_is_neutral():
    paper = fit_score.Paper(topics=[])
    journal = {"topics": [("Embodied Cognition", 50)]}
    assert fit_score.score_topic_density(paper, journal) == 50.0


def test_topic_density_no_journal_topics_is_neutral():
    paper = fit_score.Paper(topics=["embodied cognition"])
    assert fit_score.score_topic_density(paper, {}) == 50.0


def test_topic_density_substring_match_scores_above_neutral():
    paper = fit_score.Paper(topics=["Embodied Cognition and Movement"])
    journal = {"topics": [("Embodied Cognition and Movement", 30)]}
    score = fit_score.score_topic_density(paper, journal)
    assert score == 60.0  # min(100, 30 * 2)


def test_topic_density_no_overlap_scores_zero_not_neutral():
    """A paper topic that matches nothing in this journal's table should
    score 0 for THIS journal, not the neutral 50 — otherwise a real absence
    of evidence is indistinguishable from no data at all."""
    paper = fit_score.Paper(topics=["Embodied Cognition and Movement"])
    journal = {"topics": [("Unrelated Topic Entirely", 999)]}
    assert fit_score.score_topic_density(paper, journal) == 0.0


# ---------- check_hard_constraints ----------


def test_ai_usage_paper_eliminated_when_journal_has_gate():
    paper = fit_score.Paper(ai_usage=True)
    journal = {"has_ai_permission_gate": True}
    reason = fit_score.check_hard_constraints(paper, journal)
    assert reason is not None
    assert "permission" in reason.lower()


def test_ai_usage_paper_not_eliminated_when_journal_has_no_gate():
    """The exact end-to-end scenario the corpus-wide bug broke: before the
    fix, has_ai_permission_gate was True for 399/399 files, so every
    AI-disclosing paper eliminated every candidate."""
    paper = fit_score.Paper(ai_usage=True)
    journal = {"has_ai_permission_gate": False}
    assert fit_score.check_hard_constraints(paper, journal) is None


def test_ai_usage_paper_not_eliminated_when_gate_unknown():
    """None (couldn't determine) must be treated as "don't eliminate" — the
    safe default when parsing is uncertain, not a silent False-equivalent
    that could later be conflated with a confirmed no-gate."""
    paper = fit_score.Paper(ai_usage=True)
    journal = {"has_ai_permission_gate": None}
    assert fit_score.check_hard_constraints(paper, journal) is None


def test_word_limit_exceeded_eliminates():
    paper = fit_score.Paper(word_count=12000)
    journal = {"word_limit": 8000}
    reason = fit_score.check_hard_constraints(paper, journal)
    assert reason is not None
    assert "word_limit" in reason


def test_irb_hard_requirement_eliminates_paper_without_irb():
    paper = fit_score.Paper(irb=False)
    journal = {"irb_strictness": "hard"}
    reason = fit_score.check_hard_constraints(paper, journal)
    assert reason is not None
    assert "IRB" in reason


# ---------- effective_apc (the 4-case OA logic) ----------


def test_effective_apc_subscription_is_free():
    assert fit_score.effective_apc({"oa_model": "subscription"}, oa_required=False) == 0
    assert fit_score.effective_apc({"oa_model": "subscription"}, oa_required=True) == 0


def test_effective_apc_hybrid_free_unless_oa_required():
    journal = {"oa_model": "hybrid", "apc_usd_oa": 3000}
    assert fit_score.effective_apc(journal, oa_required=False) == 0
    assert fit_score.effective_apc(journal, oa_required=True) == 3000


def test_effective_apc_full_oa_always_charges():
    journal = {"oa_model": "full_oa", "apc_usd_oa": 1450}
    assert fit_score.effective_apc(journal, oa_required=False) == 1450
    assert fit_score.effective_apc(journal, oa_required=True) == 1450


# ---------- parse_journal_file (integration: wiring, not just unit logic) ----------


FULL_FIXTURE = """<!-- schema: v1.3 -->

# Test Journal

## Policies

### AI Policy

| Aspect | Detail |
|--------|--------|
| **Explicit permission gate?** | No — disclosure-based |

## Format

| Aspect | Detail |
|--------|--------|
| **Word limit** | 8,000 |

## Subject Density

### Top Topics (last 5 years)

| Topic | Article Count |
|-------|--------------|
| Embodied Cognition | 40 |
"""


def test_parse_journal_file_wires_extractors_together(tmp_path):
    p = tmp_path / "test-journal.md"
    p.write_text(FULL_FIXTURE, encoding="utf-8")
    data = fit_score.parse_journal_file(p)
    assert data["name"] == "Test Journal"
    assert data["word_limit"] == 8000
    assert data["has_ai_permission_gate"] is False
    assert data["topics"] == [("Embodied Cognition", 40)]
