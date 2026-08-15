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


# ---------- _extract_word_limit ----------
#
# A word limit is a HARD constraint: a wrong number eliminates the journal
# outright, and the user never sees it in order to overrule. So every case
# below that can't be read confidently must come back None, not a guess.


def test_word_limit_plain_number():
    assert fit_score._extract_word_limit("| **Word limit** | 8,000 |") == 8000


def test_word_limit_takes_the_ceiling_of_a_range():
    """This test previously asserted the LOWER bound, and that was wrong.
    An eval run caught it: Theory & Psychology says "5,000-8,000 standard;
    up to 10,000 permitted" and was eliminating 9,000-word papers it
    explicitly accepts. The row feeds a hard constraint, so it has to read
    as the journal's ceiling — an over-permissive limit lets the user judge
    for themselves, while an over-strict one removes the venue before they
    ever see it."""
    assert fit_score._extract_word_limit("| **Word limit** | ~8,500-10,000 |") == 10000
    assert fit_score._extract_word_limit(
        "| **Word limit** | 5,000–8,000 standard; up to 10,000 permitted |") == 10000
    assert fit_score._extract_word_limit(
        "| **Word limit** | 5,000–10,000 (extensible to 15,000 depending on topic) |") == 15000


def test_character_count_does_not_outrank_a_word_count():
    """Taking the largest number alone would read Cell's limit as 50,000
    words. When any figure is labelled as words, only those are eligible."""
    assert fit_score._extract_word_limit(
        "| **Word limit** | Articles ~50,000 characters with spaces (~7,500 words) |") == 7500


def test_page_limit_is_not_a_word_limit():
    """Regression: 11 entries stated page limits, which were read as word
    counts — ACM TACCESS eliminated anything over "30 words"."""
    for cell in ("4 pages (including figures and references)",
                 "8 pages (full paper) + 2 pages references",
                 "6 pages (text, figures, tables combined)"):
        assert fit_score._extract_word_limit(f"| **Word limit** | {cell} |") is None, cell


def test_no_strict_limit_beats_a_trailing_number():
    for cell in ("No strict limit; recommended ≤30 pages",
                 "No strict word count; typically 8-15 pages in IEEE 2-column format",
                 "Submission: no formal page limit; recommended ≤25 pages excluding references"):
        assert fit_score._extract_word_limit(f"| **Word limit** | {cell} |") is None, cell


def test_year_range_is_not_a_word_limit():
    cell = ("No explicit hard limit in current official PDF; empirical sampling of "
            "2023–2025 publications shows median ~22 pages")
    assert fit_score._extract_word_limit(f"| **Word limit** | {cell} |") is None


def test_two_thousand_words_is_still_a_valid_limit():
    """Guard the year check from over-firing: 2,000 words is a real limit."""
    assert fit_score._extract_word_limit("| **Word limit** | 2,000 words |") == 2000


def test_word_limit_ignores_the_phrase_elsewhere_in_the_file():
    """Regression: one entry's Desk Rejection Rate cell mentions 'exceeding
    ~8,000-word limit', and a loose search matched that row, returning the
    date from its next column."""
    content = (
        "| **Desk Rejection Rate** | triggers include exceeding ~8,000-word limit | 2026-07-13 |\n"
        "| **Word limit** | 9,500 |\n"
    )
    assert fit_score._extract_word_limit(content) == 9500


def test_word_limit_negotiability_row_is_not_the_limit():
    content = "| **Word limit negotiability** | Soft (extensions possible) |\n"
    assert fit_score._extract_word_limit(content) is None


def test_no_word_limit_row_at_all():
    assert fit_score._extract_word_limit("| **Abstract limit** | 150 words |") is None


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


# ---------- detect_disputes (docs/GOVERNANCE.md §4) ----------


def test_no_dispute_marker_returns_empty():
    content = "## Soft Metadata\n\n> [!WARNING]\n> **Tier 2 (community estimate)**\n"
    assert fit_score.detect_disputes(content) == []


def test_dispute_marker_detected_with_field_names():
    content = """
## Soft Metadata

> [!CAUTION]
> **Disputed** — Reviewer Pool Characteristics. See #42.

> [!WARNING]
> **Tier 2 (community estimate)**
"""
    disputes = fit_score.detect_disputes(content)
    assert len(disputes) == 1
    assert "Reviewer Pool Characteristics" in disputes[0]


def test_dispute_is_orthogonal_to_tier():
    """A dispute must not change or mask the tier — they answer different
    questions (is this claim accurate vs. how was the evidence gathered)."""
    content = """
## Soft Metadata

> [!CAUTION]
> **Disputed** — Epistemological & Political Leanings. See #7.

> [!WARNING]
> **Tier 2 (community estimate)** — family-level adaptation.
"""
    assert fit_score.detect_tier(content) == "Tier 2 (community estimate)"
    assert len(fit_score.detect_disputes(content)) == 1


def test_multiple_disputes_all_detected():
    content = """
> [!CAUTION]
> **Disputed** — Framing Requirements. See #10.

> [!CAUTION]
> **Disputed**: Voice & Style. See #11.
"""
    assert len(fit_score.detect_disputes(content)) == 2


def test_no_entry_in_corpus_is_currently_disputed():
    """Sanity check on the real corpus: the mechanism exists but nothing is
    disputed yet, so a stray marker (or a false-positive pattern) shows up
    here rather than silently mislabeling a live entry."""
    root = Path(__file__).resolve().parents[2] / "references" / "journals"
    disputed = [
        p.name for p in root.rglob("*.md")
        if p.name != "TEMPLATE.md" and fit_score.detect_disputes(p.read_text(encoding="utf-8"))
    ]
    assert disputed == []


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


def test_topic_density_no_paper_topics_is_unknown():
    """Previously asserted a neutral 50. That was the bug: it made an entry
    with no topic data outscore one whose real counts were a weak match."""
    paper = fit_score.Paper(topics=[])
    journal = {"topics": [("Embodied Cognition", 50)]}
    assert fit_score.score_topic_density(paper, journal) is None


def test_topic_density_no_journal_topics_is_unknown():
    paper = fit_score.Paper(topics=["embodied cognition"])
    assert fit_score.score_topic_density(paper, {}) is None


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


def test_unstated_irb_does_not_eliminate():
    """Regression: running a purely theoretical paper through the pipeline
    eliminated 33 journals — TOCHI, IJHCS and Human-Computer Interaction
    among them — because extraction defaulted an unmentioned IRB to False
    and the check tested falsiness. The paper never raised the question.
    None means unknown, and unknown must not eliminate a venue the user
    will never see."""
    assert fit_score.check_hard_constraints(
        fit_score.Paper(irb=None), {"irb_strictness": "hard"}) is None
    assert fit_score.Paper().irb is None
    assert fit_score.Paper.from_dict({}).irb is None


def test_unstated_apc_budget_does_not_eliminate():
    """Same shape for cost: an unmentioned budget is not a $0 budget."""
    journal = {"oa_model": "full_oa", "apc_usd_oa": 3000}
    assert fit_score.check_hard_constraints(fit_score.Paper(apc_budget=None), journal) is None
    assert fit_score.check_hard_constraints(fit_score.Paper(apc_budget=0), journal) is not None


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


# ---------- unknown dimensions must not be invented ----------
#
# Measured on this corpus (2026-07-30): reviewer_pool returned a constant 50
# for all 399 entries while carrying 0.15 of the weight; first-person
# acceptance is unrecorded for 59.6%, review time for 56.6%, methodology
# scores for 33.6%. Most of a typical score was therefore the same fabricated
# numbers, and candidates clustered within a point or two of each other.


def test_missing_topic_table_returns_none_not_neutral():
    """A neutral 50 made an entry with no topic table beat one whose real
    counts were a weak match (33.3) — rewarding absent data."""
    paper = fit_score.Paper(topics=["Embodied Cognition"])
    assert fit_score.score_topic_density(paper, {"topics": []}) is None
    assert fit_score.score_topic_density(fit_score.Paper(topics=[]), {"topics": [("x", 5)]}) is None


def test_unimplemented_reviewer_pool_contributes_nothing():
    assert fit_score.score_reviewer_pool(fit_score.Paper(), {}) is None


def test_unknown_dimensions_are_dropped_not_averaged_in():
    """Two entries alike on the one known dimension should score alike,
    whatever else is missing — the missing parts must not silently pull them
    apart."""
    paper = fit_score.Paper(topics=["Embodied Cognition"], methodology=None)
    journal = {"topics": [("Embodied Cognition", 50)]}
    total, dims = fit_score.compute_score(paper, journal, fit_score.DEFAULT_WEIGHTS)
    assert dims["topic_density"] == 100.0
    assert dims["methodology_fit"] is None
    assert dims["reviewer_pool"] is None
    # Shrunk toward the prior because coverage is partial, but still above it.
    assert fit_score.SHRINKAGE_PRIOR < total < 100.0


def test_full_coverage_is_not_shrunk():
    """Shrinkage must leave a fully-evidenced score exactly as computed,
    otherwise it is just the old fudge in a new place."""
    paper = fit_score.Paper(topics=["X"], methodology="autoethnography",
                            sensitive_content=[], timeline_priority="fast")
    journal = {
        "topics": [("X", 50)],
        "methodology_scores": {"autoethnography": 5},
        "first_person_acceptance": 5,
        "review_time_months": 3,
    }
    total, dims = fit_score.compute_score(paper, journal, fit_score.DEFAULT_WEIGHTS)
    coverage = fit_score.score_coverage(dims, fit_score.DEFAULT_WEIGHTS)
    # reviewer_pool is unimplemented, so full coverage is unreachable today;
    # what matters is that the shrinkage is exactly proportional to coverage.
    known = {k: v for k, v in dims.items() if v is not None}
    w = fit_score.DEFAULT_WEIGHTS
    observed = sum(known[k] * w[k] for k in known) / sum(w[k] for k in known)
    expected = coverage * observed + (1 - coverage) * fit_score.SHRINKAGE_PRIOR
    assert abs(total - expected) < 1e-9


def test_thin_evidence_cannot_outrank_solid_evidence_on_equal_merit():
    """The failure introduced by renormalisation alone: an entry known only
    on one strong dimension outscored one that is strong across five."""
    paper = fit_score.Paper(topics=["X"], methodology="autoethnography",
                            timeline_priority="fast")
    thin = {"topics": [("X", 50)]}
    solid = {"topics": [("X", 50)], "methodology_scores": {"autoethnography": 5},
             "first_person_acceptance": 5, "review_time_months": 3}
    thin_total, _ = fit_score.compute_score(paper, thin, fit_score.DEFAULT_WEIGHTS)
    solid_total, _ = fit_score.compute_score(paper, solid, fit_score.DEFAULT_WEIGHTS)
    assert solid_total > thin_total


def test_score_coverage_reports_the_evidenced_fraction():
    paper = fit_score.Paper(topics=["X"])
    _, dims = fit_score.compute_score(paper, {"topics": [("X", 50)]},
                                      fit_score.DEFAULT_WEIGHTS)
    coverage = fit_score.score_coverage(dims, fit_score.DEFAULT_WEIGHTS)
    assert 0.0 < coverage < 1.0


# ---------- reviewer_pool and strategic_factors (implemented 2026-07-30) ----------
#
# Both previously contributed nothing while carrying 0.30 of the weight
# between them, which capped every entry in the corpus at 70% coverage no
# matter how complete it was.


def _bias_cell(value: str) -> str:
    return ("### Reviewer Pool Characteristics@@"
            "| **Quantitative mindset bias on qualitative work?** | " + value + " | |@@"
            ).replace("@@", "\n")


def test_quant_bias_severity_is_read_from_the_leading_term():
    assert fit_score._extract_quant_bias(_bias_cell("Very High")) == 1.0
    assert fit_score._extract_quant_bias(_bias_cell("Yes (strong)")) == 1.0
    assert fit_score._extract_quant_bias(_bias_cell("Mixed")) == 0.5
    assert fit_score._extract_quant_bias(_bias_cell("No")) == 0.0
    # "Very High" must beat "High", and "Low-Medium" must beat "Low".
    assert fit_score._extract_quant_bias(_bias_cell("Very high - RCTs expected")) == 1.0
    assert fit_score._extract_quant_bias(_bias_cell("Low-Medium - qualitative routine")) == 0.3


def test_quant_bias_placeholder_is_unknown():
    for value in ("*(pending)*", "*(fill manually)*", "N/A", ""):
        assert fit_score._extract_quant_bias(_bias_cell(value)) is None, value


def test_reviewer_pool_friction_is_symmetric():
    """A quantitatively-minded pool is friction for qualitative work and
    alignment for quantitative work - the same field read from both sides."""
    journal = {"quant_bias": 1.0}
    assert fit_score.score_reviewer_pool(
        fit_score.Paper(methodology="autoethnography"), journal) == 0.0
    assert fit_score.score_reviewer_pool(
        fit_score.Paper(methodology="quantitative experimental"), journal) == 100.0


def test_theoretical_papers_get_a_reviewer_pool_score():
    """Theory work meets the same "where is your data?" objection, and
    excluding it cost every theoretical submission this dimension."""
    assert fit_score.score_reviewer_pool(
        fit_score.Paper(methodology="theoretical"), {"quant_bias": 0.0}) == 100.0


def test_reviewer_pool_unknown_without_bias_or_methodology():
    assert fit_score.score_reviewer_pool(
        fit_score.Paper(methodology="autoethnography"), {}) is None
    assert fit_score.score_reviewer_pool(fit_score.Paper(), {"quant_bias": 1.0}) is None


def test_strategic_uses_hard_blockers_not_just_review_speed():
    """Previously this read only review time, and only when the author was in
    a hurry, so it said nothing on most queries while the hand-written
    Strategic Notes went unused by every dimension."""
    paper = fit_score.Paper(methodology="autoethnography", timeline_priority="normal")
    blocked = {"hard_blockers": "Autoethnography is not accepted under any framing."}
    clear = {"hard_blockers": "Requires pre-registration for confirmatory work."}
    assert fit_score.score_strategic(paper, blocked) < fit_score.score_strategic(paper, clear)


def test_strategic_is_unknown_when_nothing_speaks():
    paper = fit_score.Paper(methodology="autoethnography", timeline_priority="normal")
    assert fit_score.score_strategic(paper, {}) is None


def test_strategic_placeholder_sections_are_not_treated_as_content():
    content = "### Hard Blockers\n\n*(pending)*\n"
    assert fit_score._extract_strategic_text(content, "Hard Blockers") is None


# ---------- shrinkage is one-sided (2026-08-14) ----------


def test_uncertainty_never_promotes_a_candidate():
    """Symmetric shrinkage toward 50 had a mirror failure nobody had named:
    a venue scoring 0 on 20% coverage landed at 40, above a venue known
    across every dimension to score 35. "Almost certainly wrong, but nobody
    checked" outranked "checked, and mediocre". Acting on a recommendation
    costs a submission cycle; missing one costs a candidate still visible
    further down the list. So the prior may lower a score and never raise
    one."""
    def scored(observed, coverage):
        shrunk = coverage * observed + (1 - coverage) * fit_score.SHRINKAGE_PRIOR
        return min(observed, shrunk)

    bad_and_unknown = scored(0.0, 0.2)
    mediocre_and_known = scored(35.0, 1.0)
    assert bad_and_unknown == 0.0
    assert bad_and_unknown < mediocre_and_known


def test_the_original_over_optimism_is_still_corrected():
    """The one-sidedness must not undo what shrinkage was added for: a
    strong-looking score resting on a third of the evidence still gets pulled
    down toward the prior."""
    def scored(observed, coverage):
        shrunk = coverage * observed + (1 - coverage) * fit_score.SHRINKAGE_PRIOR
        return min(observed, shrunk)

    assert scored(90.0, 0.3) == 62.0
    assert scored(75.0, 1.0) == 75.0


def test_shrinkage_leaves_a_fully_evidenced_entry_untouched():
    paper = fit_score.Paper(topics=["embodied cognition"], methodology="autoethnography")
    dims = {k: 60.0 for k in fit_score.DEFAULT_WEIGHTS}
    assert fit_score.score_coverage(dims, fit_score.DEFAULT_WEIGHTS) == 1.0
