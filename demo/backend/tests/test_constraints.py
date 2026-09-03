"""Tests for the two reviewer items fixed on 2026-09-03, and the tie they exposed.

These read the real corpus rather than fixtures. The functions under test exist
to answer "what does this entry actually say", so a fixture that says what the
test wants would test nothing: the failure mode being guarded against is a
parser that quietly turns a recorded blank into a value, and only real entries
carry the shapes the corpus actually uses.

Anchors are chosen for what they are rather than for their contents:
  - a Tier 1 journal with a full Identity table,
  - a conference, whose ISSN is a recorded blank because conferences have none,
  - an ACM PACM title, whose venue type is neither Journal nor Conference.
Assertions are about properties, not about a publisher's name, so re-verifying
an entry does not break the suite.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import main  # noqa: E402
import fit_score  # noqa: E402

JOURNAL = main.JOURNALS_ROOT / "qualitative-methods" / "qualitative-inquiry.md"
CONFERENCE = main.JOURNALS_ROOT / "conferences" / "hci" / "acm-chi.md"
HYBRID = main.JOURNALS_ROOT / "hci" / "acm-pacm-cscw.md"


# ---------------------------------------------------------------- R2.6

def test_identity_fields_reads_the_table():
    ident = main.identity_fields(JOURNAL.read_text(encoding="utf-8"))
    assert ident["Venue type"] == "Journal"
    assert ident["Publisher"]
    assert ident["URL"].startswith("http")


@pytest.mark.parametrize("value", [
    "*(pending)*",
    "*(pending verification)*",
    "*(N/A - conference proceedings)*",
    "*(varies by year; international rotating chairs)*",
    "(pending)",
    "N/A",
    "-",
])
def test_recorded_blanks_are_not_values(value):
    """The corpus writes a missing value as an italicised parenthetical. A card
    that printed one would be asserting exactly what the blank exists to avoid."""
    content = "## Identity\n\n| Field | Value |\n|---|---|\n| **Publisher** | %s |\n\n## Metrics\n" % value
    assert "Publisher" not in main.identity_fields(content)


def test_a_conference_reports_no_issn_rather_than_its_placeholder():
    card = main.build_evidence_card(CONFERENCE)
    assert card["venue_type"] == "Conference"
    assert card["issn"] is None
    assert card["url"]


def test_issn_falls_through_to_online_when_there_is_no_print_issn():
    card = main.build_evidence_card(HYBRID)
    ident = main.identity_fields(HYBRID.read_text(encoding="utf-8"))
    assert "ISSN (Print)" not in ident
    assert card["issn"] == ident["ISSN (Online)"]


def test_every_entry_yields_a_card_without_raising():
    """A malformed Identity table must degrade to absent fields, not a 500."""
    for path in main.JOURNALS_ROOT.rglob("*.md"):
        if path.name == "TEMPLATE.md":
            continue
        card = main.build_evidence_card(path)
        assert set(card) >= {"tier", "venue_type", "publisher", "issn", "url"}


# ---------------------------------------------------------------- R2.4

@pytest.mark.parametrize("raw,expected", [
    ("journals", "journals"),
    ("Journals only", "journals"),
    ("JOURNAL", "journals"),
    ("conferences", "conferences"),
    ("proceedings", "conferences"),
    ("both", "either"),
    ("", None),
    (None, None),
    (42, None),
    ("maybe later", None),          # unreadable answer is an unstated one
])
def test_venue_type_normalisation(raw, expected):
    assert main.normalise_venue_type(raw) == expected


def _fully_specified() -> fit_score.Paper:
    return fit_score.Paper(topics=["Cognitive Abilities and Testing"],
                           methodology="qualitative", word_count=8000,
                           apc_budget=0, irb=True)


def test_venue_type_is_not_asked_when_the_description_stated_it():
    """The bug this fixes: the question was asked unconditionally, so a user who
    wrote "journals only" was asked again, and skipping discarded their words."""
    paper = fit_score.Paper(topics=["x"], methodology="experimental")  # much unstated
    asked = main.clarifying_question(paper, "journals")
    assert asked is not None                      # fees/length/ethics still unknown
    assert "Venue type" not in asked


def test_venue_type_is_asked_when_the_description_did_not_state_it():
    paper = fit_score.Paper(topics=["x"], methodology="experimental")
    assert "Venue type" in main.clarifying_question(paper, None)


def test_no_question_at_all_when_nothing_material_is_missing():
    assert main.clarifying_question(_fully_specified(), "journals") is None


def test_venue_type_alone_is_not_worth_a_round_trip():
    """Everything else is known and only venue type is not. Unlike a fee budget
    it cannot silently eliminate the whole list, so it is reported as an
    unstated assumption instead of costing the user a turn."""
    assert main.clarifying_question(_fully_specified(), None) is None
    assert any("venue type" in u.lower()
               for u in main.unstated_constraints(_fully_specified(), None))


def test_stated_venue_type_is_not_reported_as_unstated():
    assert not any("venue type" in u.lower()
                   for u in main.unstated_constraints(_fully_specified(), "journals"))


def _venue_types(candidates) -> set:
    return {main._venue_type_of(c.path) for c in candidates}


def test_journals_only_removes_conferences():
    paper = fit_score.Paper(topics=["Human-Computer Interaction"], methodology="qualitative",
                            irb=True)
    assert "conference" not in _venue_types(main.screen_candidates(paper, "journals"))


def test_conferences_only_removes_journals():
    paper = fit_score.Paper(topics=["Human-Computer Interaction"], methodology="qualitative",
                            irb=True)
    assert "journal" not in _venue_types(main.screen_candidates(paper, "conferences"))


def test_an_unstated_venue_type_eliminates_nothing():
    paper = fit_score.Paper(topics=["Human-Computer Interaction"], methodology="qualitative",
                            irb=True)
    unconstrained = main._score_against(paper, None)
    assert len(unconstrained) >= len(main._score_against(paper, "journals"))


def test_proceedings_journals_survive_both_answers():
    """ACM's PACM titles are journals that publish a conference's papers. An
    author who said "journals only" wants them, and one submitting to the
    conference reaches them through it, so neither answer may drop them."""
    paper = fit_score.Paper(topics=["Human-Computer Interaction"], methodology="qualitative",
                            irb=True)
    for answer in ("journals", "conferences"):
        kept = {c.path for c in main._score_against(paper, answer)}
        assert HYBRID in kept, answer


def test_the_venue_type_elimination_says_why():
    paper = fit_score.Paper(topics=["Human-Computer Interaction"], methodology="qualitative",
                            irb=True)
    excluded = main.VENUE_TYPE_EXCLUDES["journals"]
    assert "conference" in excluded


# ---------------------------------------------------------------- the tie

def test_identical_evidence_profiles_are_reported_as_tied():
    """Eight ACM conferences share one family template and none of the twenty
    conference entries carries topic data, so topic_density is unknown for all
    of them and the remaining five dimensions are family-level facts. They score
    identically because they are the same record under different names."""
    paper = fit_score.Paper(topics=["Human-Computer Interaction"], methodology="qualitative",
                            irb=True)
    candidates = main.screen_candidates(paper, "conferences")
    ties = main.tie_sizes(candidates)
    assert max(ties.values()) >= 3
    assert all(ties[c.name] >= 1 for c in candidates)


def test_a_unique_profile_is_not_marked_tied():
    a = fit_score.JournalScore(path=JOURNAL, name="A", score=70.0,
                               dimension_scores={"topic_density": 50.0})
    b = fit_score.JournalScore(path=JOURNAL, name="B", score=70.0,
                               dimension_scores={"topic_density": 10.0})
    assert main.tie_sizes([a, b]) == {"A": 1, "B": 1}


def test_the_same_score_from_different_dimensions_is_not_a_tie():
    """Two entries can reach 70.0 by different routes. That is a coincidence of
    arithmetic, not indistinguishable evidence, and marking it would cry wolf."""
    a = fit_score.JournalScore(path=JOURNAL, name="A", score=70.0,
                               dimension_scores={"topic_density": 80.0, "voice_compatibility": 60.0})
    b = fit_score.JournalScore(path=JOURNAL, name="B", score=70.0,
                               dimension_scores={"topic_density": 60.0, "voice_compatibility": 80.0})
    assert main.tie_sizes([a, b]) == {"A": 1, "B": 1}


def test_unknown_dimensions_count_as_part_of_the_profile():
    a = fit_score.JournalScore(path=JOURNAL, name="A", score=70.0,
                               dimension_scores={"topic_density": None})
    b = fit_score.JournalScore(path=JOURNAL, name="B", score=70.0,
                               dimension_scores={"topic_density": None})
    assert main.tie_sizes([a, b]) == {"A": 2, "B": 2}


def test_the_synthesis_prompt_declares_a_tie_and_forbids_inventing_a_reason():
    paper = fit_score.Paper(topics=["Human-Computer Interaction"], methodology="qualitative",
                            irb=True)
    prompt = main.build_synthesis_prompt("an HCI paper", paper,
                                         main.screen_candidates(paper, "conferences"))
    assert "TIED with" in prompt
    assert "inventing a reason to separate" in prompt


# ---------------------------------------------------------------- version

def test_the_version_block_reaches_the_disclosure_payload():
    """The coverage panel is where a reader learns what the corpus does and does
    not hold; which corpus it is belongs in the same place."""
    assert "version" in main.compute_coverage()


def test_a_missing_version_file_degrades_to_absent_rather_than_wrong():
    """Absent is a legitimate state — a dev checkout has no version.json. What
    is not legitimate is claiming a commit that did not ship, so the loader
    yields an empty mapping and the UI renders nothing at all."""
    assert isinstance(main.VERSION, dict)
    if main.VERSION:
        assert main.VERSION.get("corpus_commit")


def test_the_paper_doi_is_never_invented():
    """Null until a release is actually archived. A placeholder that looked like
    a DOI would be the one kind of error this whole file exists to prevent."""
    paper = main.VERSION.get("paper", {})
    if paper.get("doi") is not None:
        assert paper["doi"].startswith("10."), paper["doi"]
