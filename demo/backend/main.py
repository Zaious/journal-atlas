#!/usr/bin/env python3
"""
Journal Atlas web demo backend — FastAPI, SSE streaming, no database.

Three-stage pipeline per request, all stateless (nothing persisted between
requests):
  1. EXTRACT (Haiku, forced tool-use) — freeform paper description -> the
     same `Paper` dataclass fit_score.py already scores against.
  2. SCREEN (fit_score.py, no LLM) — deterministic pre-ranking across the
     curated 399 entries, reused as-is, not reimplemented. Each candidate's
     tier and top cited topic counts ride along in this stage's SSE event
     for the frontend's evidence cards.
  3. SYNTHESIZE (Sonnet, streamed) — inlines CONSUMPTION_CONTRACT.md's
     tier/evidence rules, then reads a trimmed Soft Metadata / Strategic
     Notes excerpt of the top candidates and writes the kind of reasoned
     recommendation SKILL.md's own workflow produces (not just a score
     table): a pick with reasoning, runners-up, eliminations, honest
     tier/uncertainty flags, a rejection fallback suggestion.

Every stage emits an SSE event so the frontend can show real progress
instead of a blank spinner.

Abuse and cost controls live in ratelimit.py and are wired into both
LLM-calling endpoints: input size caps bound a single request, per-client
rate limits are friction, and a global daily cap is what actually bounds the
bill. See demo/README.md for what each one does and does not protect against.
"""
from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import asdict
from pathlib import Path
from typing import AsyncIterator

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import BaseModel, Field

# Point at the .env beside this file rather than letting load_dotenv() search
# upward from the working directory. uvicorn is often started from the repo
# root with --app-dir, and the bare call then silently finds nothing: the
# server comes up reporting "API key not set" while the same code works when
# run from this directory.
load_dotenv(Path(__file__).resolve().parent / ".env")

# Reuse fit_score.py directly — no reimplementation of the scoring logic.
SKILL_SCRIPTS = Path(__file__).resolve().parents[2] / "skills" / "journal-atlas" / "scripts"
sys.path.insert(0, str(SKILL_SCRIPTS))
import fit_score  # noqa: E402

import providers  # noqa: E402 - local module, imported after sys.path is set
import ratelimit  # noqa: E402 - local module, imported after sys.path is set

JOURNALS_ROOT = SKILL_SCRIPTS.parent / "references" / "journals"
TOP_N_SCREEN = 10  # matches SKILL.md's own ">50 entries: read only top 10-15"

# fit_score.score_topic_density() matches Paper.topics against each journal's Top
# Topics table via bidirectional substring containment, not fuzzy overlap — so
# extraction has to phrase topics near-verbatim to real OpenAlex topic names to
# score anything but a neutral 50.0. Built by build_topic_vocabulary.py; re-run
# that script whenever references/journals/**/*.md changes.
TOPIC_VOCABULARY_PATH = Path(__file__).resolve().parent / "topic_vocabulary.json"
try:
    TOPIC_VOCABULARY: list[str] = json.loads(TOPIC_VOCABULARY_PATH.read_text(encoding="utf-8"))
except FileNotFoundError:
    TOPIC_VOCABULARY = []
    print(f"warning: {TOPIC_VOCABULARY_PATH} missing — run build_topic_vocabulary.py; "
          "topic extraction will fall back to unconstrained free text", file=sys.stderr)

# The canonical tier/evidence rules SKILL.md's checklist points to. A real skill
# session can just read that file; this synthesis call has no file-read tool, so
# the rules have to be inlined into its prompt directly rather than referenced.
CONSUMPTION_CONTRACT_PATH = SKILL_SCRIPTS.parent / "CONSUMPTION_CONTRACT.md"
try:
    CONSUMPTION_CONTRACT = CONSUMPTION_CONTRACT_PATH.read_text(encoding="utf-8")
except FileNotFoundError:
    CONSUMPTION_CONTRACT = ""
    print(f"warning: {CONSUMPTION_CONTRACT_PATH} missing — synthesis will run "
          "without the tier/evidence consumption rules", file=sys.stderr)

REQUEST_TIMEOUT_SECONDS = 60.0
MAX_RETRIES = 2

# Which LLM backend runs the extract and synthesize stages. See providers.py;
# selected by LLM_PROVIDER, defaults to gemini. Built once at import so a
# missing key or SDK surfaces in /api/health rather than on first request.
PROVIDER, PROVIDER_ERROR = providers.build_provider(REQUEST_TIMEOUT_SECONDS, MAX_RETRIES)

app = FastAPI(title="Journal Atlas demo backend")
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.environ.get("CORS_ORIGINS", "http://localhost:5173,http://localhost:5174,http://localhost:5175").split(","),
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# One limiter for the whole process, shared by both LLM-calling endpoints so a
# client cannot spend its recommendation budget and then keep going on
# follow-ups. /api/coverage and /api/health are not counted: they cost nothing
# and blocking them would hide the very message explaining the block.
LIMITER = ratelimit.RateLimiter()


# Input size caps. These bound the cost of a *single* request, which rate
# limiting cannot: without them one call can carry an arbitrary payload into a
# prompt the demo pays for. They also keep the demo honest about what it is for
# — an abstract or a description, not a whole manuscript.
MAX_DESCRIPTION_CHARS = 12_000
MAX_ANSWER_CHARS = 2_000
MAX_RECOMMENDATION_CHARS = 20_000


class RecommendRequest(BaseModel):
    paper_description: str = Field(max_length=MAX_DESCRIPTION_CHARS)
    # The user's reply to the one clarifying question, appended to the
    # description before re-extraction. None on the first pass.
    clarifications: str | None = Field(default=None, max_length=MAX_ANSWER_CHARS)
    # Set when the user chose to proceed without answering.
    skip_clarify: bool = False


MAX_FOLLOWUPS = 2


class FollowupRequest(BaseModel):
    """A follow-up question about a recommendation already given.

    The prior turn's context comes back from the browser rather than from
    server-side session state, so the demo keeps its no-database property and
    the conversation lives where the user can see and discard it.
    """
    paper_description: str = Field(max_length=MAX_DESCRIPTION_CHARS)
    recommendation: str = Field(max_length=MAX_RECOMMENDATION_CHARS)
    question: str = Field(max_length=MAX_ANSWER_CHARS)
    candidate_names: list[str] = Field(default=[], max_length=TOP_N_SCREEN)
    # Client-supplied, so it caps an honest client and nothing else. A client
    # that always sends 0 gets unlimited follow-ups from this check alone —
    # what actually bounds that case is the rate limiter in ratelimit.py.
    asked_so_far: int = 0


# ---------- Stage 1: extraction ----------

PAPER_SCHEMA = {
    "type": "object",
    "properties": {
        "topics": {"type": "array", "items": {"type": "string"}, "description": "3-6 topic strings; prefer exact matches from the provided vocabulary, verbatim"},
        "methodology": {"type": ["string", "null"], "description": "e.g. quantitative experimental, autoethnography, theoretical"},
        "word_count": {"type": ["integer", "null"]},
        "apc_budget": {"type": ["integer", "null"], "description": "USD the author can pay in publication fees. Use null when the text does not say — null means 'not stated' and leaves the constraint unapplied, whereas 0 means 'explicitly cannot pay anything' and eliminates every journal with a fee."},
        "oa_required": {"type": "boolean", "description": "true only if the author explicitly needs immediate open access"},
        "ai_usage": {"type": "boolean", "description": "true if the text mentions AI-assisted writing"},
        "sensitive_content": {"type": "array", "items": {"type": "string"}, "description": "any sensitive topics the paper covers, empty if none"},
        "irb": {"type": ["boolean", "null"], "description": "true if ethics approval was obtained, false ONLY if the text explicitly says there is none, null when the text is silent or the question does not arise (e.g. a purely theoretical paper). false eliminates every journal with a hard IRB requirement, so do not infer it from silence."},
        "preprint_intent": {"type": "boolean"},
        "timeline_priority": {"type": "string", "enum": ["fast", "normal", "flexible"]},
        "venue_type": {"type": ["string", "null"], "description": "Which venue types the author will submit to, but ONLY when the text says so: \"journals\" if it rules conferences out (e.g. \"journals only\"), \"conferences\" if it rules journals out, \"either\" if it says both are fine. null when the text is silent. null leaves the constraint unapplied and the interface asks once; do not infer a preference from the subject matter."},
        "fields": {"type": "array", "items": {"type": "string"}, "description": "Which curated directories to search. Journals: psychology, hci, philosophy, cognitive-science, biology, medical, physics, multidisciplinary, qualitative-methods. Conferences (include these whenever conference proceedings are a plausible venue, which for HCI/ML/NLP work they usually are): conferences/hci, conferences/ml, conferences/nlp, conferences/data-mining. Prefer listing several over guessing one, and leave empty to search everything — a directory you omit is never seen by the user."},
    },
    "required": ["topics", "methodology", "sensitive_content", "fields", "timeline_priority", "oa_required", "ai_usage", "preprint_intent"],
    "additionalProperties": False,
}

# How each provider is coaxed into schema-conforming JSON differs (forced
# tool-use vs a response schema) and lives in providers.py; this module only
# supplies the schema.


def _build_extraction_prompt(freeform_text: str) -> str:
    vocab_block = "\n".join(TOPIC_VOCABULARY)
    topics_guidance = (
        "For `topics`: our journal database indexes topic density using specific "
        "OpenAlex category names, matched by substring — so a topic only scores as "
        "a match when it is copied near-verbatim from the list below. When the "
        "paper's subject matches or closely overlaps with one of these names, copy "
        "that EXACT string into the topics array (do not paraphrase or shorten "
        "it). Only add your own free-text phrase if nothing below is a reasonable "
        f"match.\n\nKnown topic names:\n{vocab_block}\n\n"
        if TOPIC_VOCABULARY else ""
    )
    return (
        "Extract structured attributes from this paper description for an "
        "academic-journal-matching tool. Do not invent facts not implied by "
        "the text — leave arrays empty / booleans at their conservative "
        f"default rather than guessing.\n\n{topics_guidance}---\n\n{freeform_text}"
    )


# Values the model may return for venue_type, and the synonyms it reaches for
# anyway. Anything unrecognised becomes None -- an unreadable answer is an
# unstated constraint, not a licence to guess which way the author meant it.
VENUE_TYPE_SYNONYMS = {
    "journals": "journals", "journal": "journals", "journals only": "journals",
    "conferences": "conferences", "conference": "conferences",
    "proceedings": "conferences", "conferences only": "conferences",
    "either": "either", "both": "either", "any": "either", "no preference": "either",
}


def normalise_venue_type(raw) -> str | None:
    if not isinstance(raw, str):
        return None
    return VENUE_TYPE_SYNONYMS.get(raw.strip().lower())


async def extract_paper(provider, freeform_text: str) -> tuple[fit_score.Paper, str | None]:
    """The Paper the scorer takes, plus the one stated constraint it has no
    field for. venue_type decides which venues may be recommended at all, so
    it eliminates like a hard constraint, but fit_score.Paper is the skill's
    schema and the demo does not get to widen it."""
    data = await provider.extract(_build_extraction_prompt(freeform_text), PAPER_SCHEMA)
    return fit_score.Paper.from_dict(data), normalise_venue_type(data.get("venue_type"))


def unstated_constraints(paper: fit_score.Paper, venue_type: str | None = None) -> list[str]:
    """Hard constraints the description never mentioned, so none was applied.

    A single-shot request cannot stop and ask, but it can say what it assumed.
    These are the constraints that ELIMINATE, and an eliminated venue never
    reaches the user to be overruled — so when one is unknown the honest move
    is to leave it unapplied and name it, rather than pick a default and
    silently narrow the field.
    """
    unstated = []
    if paper.apc_budget is None:
        unstated.append("No publication-fee budget given, so no journal was ruled out on cost. "
                        "If you cannot pay an APC, say so — it changes the list substantially.")
    if paper.irb is None:
        unstated.append("No ethics/IRB status given, so no journal was ruled out on it. "
                        "Say if your study involves human participants without approval.")
    if paper.word_count is None:
        unstated.append("No word count given, so no journal was ruled out on length.")
    if venue_type is None:
        unstated.append("No venue type given, so both journals and conferences were "
                        "searched. Say \"journals only\" if proceedings are no use to you.")
    return unstated


def clarifying_question(paper: fit_score.Paper, venue_type: str | None = None) -> str | None:
    """One question, asked once, covering whatever would actually change the
    answer. None when nothing material is missing.

    Deliberately deterministic rather than model-generated: it costs nothing,
    it is testable, and it can only ask about gaps the scorer genuinely acts
    on. Everything is bundled into a single turn because a demo that
    interrogates the user three times before showing anything is worse than
    one that guesses.
    """
    asks = []
    if paper.apc_budget is None:
        asks.append("**Publication fees** \u2014 can you pay an APC, and roughly up to how much? "
                    "(Many journals have a free subscription route, so \u201cno budget\u201d "
                    "rarely means no options.)")
    if paper.word_count is None:
        asks.append("**Length** \u2014 roughly how many words?")
    # Only worth asking when the work could plausibly involve human subjects.
    # A theoretical paper has no IRB question, and asking anyway makes the
    # tool look like it did not read the description.
    theoretical = (paper.methodology or "").lower() in {
        "theoretical", "conceptual", "theoretical / conceptual", "philosophical"}
    if paper.irb is None and not theoretical:
        asks.append("**Ethics approval** \u2014 does the work involve human participants, and if "
                    "so do you have IRB/ethics approval?")
    # Asked only when the description did not say. It used to be asked every
    # time, on the grounds that extraction reliably omitted venue type -- but
    # extraction omitted it because nothing asked for it, and asking a user to
    # repeat what they already wrote invites them to skip, which threw the
    # constraint away. Section 5 promises a question only where the
    # description leaves a constraint unstated; this is what makes that true.
    if venue_type is None:
        asks.append("**Venue type** \u2014 journals only, or should conference proceedings "
                    "(CHI, CSCW, NeurIPS, ACL and similar) be considered too?")

    if not asks:
        return None
    if len(asks) == 1 and venue_type is None and asks[0].startswith("**Venue type**"):
        # Venue type alone is not worth a round trip: unlike a fee budget it
        # cannot silently eliminate everything, and the answer is visible in
        # the results either way.
        return None
    return ("Before I search, a few things that would change the answer:\n\n"
            + "\n".join("- " + a for a in asks)
            + "\n\nAnswer what you can \u2014 anything you skip stays unconstrained, "
              "and I will say so.")


def merge_clarifications(description: str, clarifications: str | None) -> str:
    if not clarifications or not clarifications.strip():
        return description
    return (description
            + "\n\n--- The author was asked for missing details and replied ---\n"
            + clarifications.strip())


# ---------- Stage 2: screening (fit_score.py, unmodified) ----------

MIN_CANDIDATES_BEFORE_WIDENING = 3


# "Proceedings-Journal" is ACM's PACM titles: a journal that publishes a
# conference's papers. An author who said "journals only" wants these, and an
# author who said "conferences" is submitting to the conference, so both
# answers keep them.
VENUE_TYPE_EXCLUDES = {"journals": {"conference"}, "conferences": {"journal"}}


def _venue_type_of(path: Path) -> str | None:
    return (identity_fields(path.read_text(encoding="utf-8")).get("Venue type") or "").lower() or None


def _score_against(paper: fit_score.Paper,
                   venue_type: str | None = None) -> list[fit_score.JournalScore]:
    excluded = VENUE_TYPE_EXCLUDES.get(venue_type or "", set())
    results = []
    for path in fit_score.collect_journals(paper, JOURNALS_ROOT):
        try:
            journal_data = fit_score.parse_journal_file(path)
        except Exception:
            continue
        js = fit_score.JournalScore(
            path=path, name=journal_data["name"],
            oa_model=journal_data.get("oa_model"),
            apc_subscription_usd=journal_data.get("apc_usd_subscription"),
            apc_oa_usd=journal_data.get("apc_usd_oa"),
        )
        elim = fit_score.check_hard_constraints(paper, journal_data)
        if not elim and excluded and (_venue_type_of(path) or "") in excluded:
            elim = "venue type: you asked for %s" % venue_type
        if elim:
            js.eliminated, js.elimination_reason = True, elim
        else:
            js.score, js.dimension_scores = fit_score.compute_score(
                paper, journal_data, fit_score.DEFAULT_WEIGHTS)
            js.warnings = [f"evidence_coverage={fit_score.score_coverage(js.dimension_scores, fit_score.DEFAULT_WEIGHTS):.2f}"]
        results.append(js)
    return sorted((r for r in results if not r.eliminated), key=lambda r: -r.score)


def screen_candidates(paper: fit_score.Paper,
                      venue_type: str | None = None) -> list[fit_score.JournalScore]:
    """Rank the corpus, widening past the extracted field guess if that guess
    starved the result set.

    The extraction stage picks which field directories to search, and it
    picks too narrowly on interdisciplinary papers. Measured on an
    autoethnographic paper about conference accessibility: the guess
    ("qualitative-methods") yielded 1 candidate, while searching everything
    yielded 10 — and the top all-fields result outranked the narrowed
    winner. The good matches lived in hci and design, which the guess never
    looked at.

    A field the extractor omits is invisible: the user never sees the venue
    and so cannot overrule the omission, which is the same reason
    _extract_word_limit() refuses to guess. Full-corpus screening is local
    file parsing that measures at well under a second for all 399 entries,
    so widening costs nothing worth protecting.
    """
    # Always score the whole corpus. `fields` is kept as extracted metadata
    # and shown to the user, but it no longer filters.
    #
    # It was a cost optimisation that measured as negative: full-corpus
    # screening is local file parsing at 0.41s for all 399 entries, while the
    # narrowing repeatedly cost real candidates. It gave 1 result where the
    # full corpus gave 10 with a better top pick, and it kept the conference
    # directories out of an HCI theory paper's search even after the author
    # explicitly asked for conferences — extraction simply never listed them.
    # The scorer already ranks irrelevant fields down; an omitted directory is
    # invisible and cannot be ranked at all.
    from dataclasses import replace
    return _score_against(replace(paper, fields=[]), venue_type)[:TOP_N_SCREEN]


# ---------- Stage 3: synthesis (Sonnet, streamed) ----------

def _find_entry(name: str) -> Path | None:
    """Locate a curated entry by its H1 title. Follow-ups arrive carrying
    names rather than paths, because the browser holds the state and a name is
    the only part of it a user could sensibly inspect."""
    for path in JOURNALS_ROOT.rglob("*.md"):
        if path.name == "TEMPLATE.md":
            continue
        if fit_score._extract_h1(path.read_text(encoding="utf-8")) == name:
            return path
    return None


# The corpus records a missing value as an italicised parenthetical --
# *(pending)*, *(N/A -- conference proceedings)*, *(varies by year)*. Those
# are recorded blanks, not values, and a card that printed them would be
# doing the one thing the corpus rule exists to prevent.
_RECORDED_BLANK = re.compile(r"^\*+\(.*\)\*+$|^\(.*\)$|^(?:n/?a|-{1,2}|\u2014)$",
                             re.I | re.S)
_IDENTITY_ROW = re.compile(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.*?)\s*\|\s*$", re.M)


def identity_fields(content: str) -> dict:
    """The Identity table, minus its recorded blanks.

    Not in fit_score.parse_journal_file() because none of it scores: the
    scorer reads only fields a dimension acts on. It is here because a reader
    who is shown a venue name and a number cannot check either without a
    publisher, an ISSN or a link.
    """
    block = re.search(r"^## Identity\s*$(.*?)^## ", content, re.S | re.M)
    if not block:
        return {}
    out = {}
    for key, value in _IDENTITY_ROW.findall(block.group(1)):
        value = value.strip()
        if value and not _RECORDED_BLANK.match(value):
            out[key.strip()] = value
    return out


def build_evidence_card(path: Path) -> dict:
    """Tier + top-cited topic rows for the screening SSE event — real,
    checkable evidence behind a fit_score number, not just the number."""
    content = path.read_text(encoding="utf-8")
    try:
        journal_data = fit_score.parse_journal_file(path)
    except Exception:
        journal_data = {}
    top_topics = sorted(journal_data.get("topics") or [], key=lambda t: -t[1])[:3]
    ident = identity_fields(content)
    # Print ISSN first when both exist: it is the one a reader is most likely
    # to have seen on a call for papers. Absent for conferences, correctly.
    issn = ident.get("ISSN (Print)") or ident.get("ISSN (Online)")
    return {
        "tier": fit_score.detect_tier(content),
        "disputes": fit_score.detect_disputes(content),
        "top_topics": [{"name": name, "count": count} for name, count in top_topics],
        "venue_type": ident.get("Venue type"),
        "publisher": ident.get("Publisher"),
        "issn": issn,
        "url": ident.get("URL"),
    }


def _format_policy_digest(journal_data: dict) -> str:
    """Condensed structured facts, in place of Identity/Metrics/Policies/Format's
    full raw tables (mostly *(community estimate)* / *(see JCR)* placeholder
    noise) — built from fields fit_score.parse_journal_file() already extracts
    for scoring, not reparsed by hand."""
    parts = []
    oa_model = journal_data.get("oa_model")
    if oa_model:
        apc_bits = []
        if journal_data.get("apc_usd_subscription") == 0:
            apc_bits.append("$0 subscription path")
        if journal_data.get("apc_usd_oa") is not None:
            apc_bits.append(f"${journal_data['apc_usd_oa']} OA path")
        parts.append(f"OA model: {oa_model}" + (f" ({', '.join(apc_bits)})" if apc_bits else ""))
    if journal_data.get("word_limit"):
        parts.append(f"Word limit: {journal_data['word_limit']}")
    if journal_data.get("review_time_months") is not None:
        parts.append(f"Review time: ~{journal_data['review_time_months']} months")
    if journal_data.get("has_ai_permission_gate") is not None:
        gate = journal_data["has_ai_permission_gate"]
        parts.append(f"AI policy: {'explicit permission gate' if gate else 'disclosure-based, no gate'}")
    if journal_data.get("irb_strictness"):
        parts.append(f"IRB: {journal_data['irb_strictness']}")
    return " | ".join(parts) if parts else "(no structured policy data parsed)"


def build_candidate_excerpt(path: Path) -> str:
    """Soft Metadata + Strategic Notes + a policy digest — not the full file.

    Drops Identity/Metrics/Policies/Format's raw tables, Conference Specifics,
    and Changelog: provenance and placeholder-heavy noise the synthesis model
    doesn't need to write a grounded recommendation.
    """
    content = path.read_text(encoding="utf-8")
    try:
        journal_data = fit_score.parse_journal_file(path)
    except Exception:
        journal_data = {}
    parts = [_format_policy_digest(journal_data)]
    for section_name in ("Subject Density", "Soft Metadata", "Strategic Notes"):
        text = fit_score.extract_h2_block(content, section_name)
        if text:
            parts.append(f"#### {section_name}\n{text}")
    return "\n\n".join(parts)


def tie_sizes(candidates: list[fit_score.JournalScore]) -> dict[str, int]:
    """How many candidates share each candidate's exact evidence profile.

    Measured 2026-09-03 on an HCI query restricted to the conference
    directories: three groups of 8, 7 and 3 venues, each group agreeing to the
    digit on all six dimensions. It is not a scoring defect. Those entries were
    built from one family template and none of the 20 conference entries
    carries topic data at all, so topic_density -- the heaviest dimension at
    0.25 -- is unknown for every one of them and the remaining five are
    family-level facts. They are the same record wearing different names.

    Ordering them anyway would manufacture a ranking out of nothing, and the
    reader has no way to see that the order is arbitrary. Reporting the tie is
    the same move the scorer already makes for a missing dimension: say that
    nothing is known rather than supply a number.
    """
    groups: dict[tuple, list[str]] = {}
    for c in candidates:
        key = (round(c.score, 1),
               tuple(sorted((k, v) for k, v in c.dimension_scores.items())))
        groups.setdefault(key, []).append(c.name)
    return {name: len(names) for names in groups.values() for name in names}


def build_synthesis_prompt(freeform_text: str, paper: fit_score.Paper, candidates: list[fit_score.JournalScore]) -> str:
    sections = []
    tied = tie_sizes(candidates)
    for c in candidates:
        try:
            content = c.path.read_text(encoding="utf-8")
            excerpt = build_candidate_excerpt(c.path)
        except OSError:
            continue
        # State the tier outright instead of leaving it to be inferred from
        # the banner inside the excerpt. Observed with gemini-3.5-flash-lite:
        # asked to infer, it cited "Tier 1 evidence" for a journal in one
        # paragraph and then summarised all candidates as "AI-Researched or
        # Tier 2" in the next — self-contradicting on the single field the
        # tier system exists to communicate. Removing the inference step
        # removes that failure.
        tier = fit_score.detect_tier(content)
        disputes = fit_score.detect_disputes(content)
        cov = fit_score.score_coverage(c.dimension_scores, fit_score.DEFAULT_WEIGHTS)
        header = (f"=== {c.name} (fit_score {c.score:.1f}/100 from {cov:.0%} of the scoring "
                  f"dimensions — the rest had no data | evidence tier: {tier}")
        if tied.get(c.name, 1) > 1:
            header += (f" | TIED with {tied[c.name] - 1} other candidate(s) on an "
                       f"identical evidence profile — their order here is arbitrary")
        if disputes:
            header += f" | DISPUTED: {'; '.join(disputes)}"
        sections.append(header + f") ===\n{excerpt}")
    contract_block = f"{CONSUMPTION_CONTRACT}\n\n---\n\n" if CONSUMPTION_CONTRACT else ""
    return (
        "You are the Journal Atlas skill. Follow the rules below when citing "
        f"anything from the candidate excerpts.\n\n{contract_block}"
        "A researcher described their paper; it has already been parsed and "
        "pre-ranked by a deterministic scorer against a curated knowledge base. "
        f"Here is their original description:\n\n{freeform_text}\n\n"
        f"Parsed attributes: {json.dumps(asdict(paper))}\n\n"
        "Below are excerpts from the top pre-ranked candidates' curated entries "
        "(policy digest + Subject Density + Soft Metadata + Strategic Notes), in "
        "score order. Read them and write a real recommendation — not a "
        "restatement of the scores:\n\n"
        + "\n\n".join(sections) + "\n\n---\n\n"
        "Write: (1) your top pick with specific reasoning drawn from that journal's "
        "actual reviewer-culture/framing/sensitive-topics content, (2) 1-2 runners-up "
        "and why they rank below the top pick — but where a candidate is marked TIED, "
        "say it is tied and on what rather than inventing a reason to separate "
        "them, (3) tier/uncertainty flags per the "
        "rules above for any candidate that isn't Tier 1, (4) one rejection-fallback "
        "suggestion if the top pick doesn't work out. Keep it under 400 words."
    )


async def sse_recommend(req: RecommendRequest) -> AsyncIterator[str]:
    def event(name: str, data: dict) -> str:
        return f"event: {name}\ndata: {json.dumps(data)}\n\n"

    if PROVIDER is None:
        yield event("error", {"message": PROVIDER_ERROR})
        return

    freeform_text = merge_clarifications(req.paper_description, req.clarifications)

    # Both stages are awaited/streamed natively rather than blocking the event
    # loop for their full duration.

    yield event("stage", {"stage": "parsing", "status": "start"})
    try:
        paper, venue_type = await extract_paper(PROVIDER, freeform_text)
    except Exception as exc:
        yield event("error", {"message": describe_provider_failure(exc, "reading your paper")})
        return
    yield event("stage", {"stage": "parsing", "status": "done", "paper": asdict(paper),
                          "unstated": unstated_constraints(paper, venue_type),
                          "venue_type": venue_type})

    # Ask once, before spending screening and synthesis on assumptions the
    # user could have corrected in one sentence. Skipped when they already
    # answered or explicitly chose to proceed.
    if req.clarifications is None and not req.skip_clarify:
        question = clarifying_question(paper, venue_type)
        if question:
            yield event("clarify", {"question": question})
            return

    yield event("stage", {"stage": "screening", "status": "start"})
    try:
        candidates = screen_candidates(paper, venue_type)
    except Exception as exc:
        yield event("error", {"message": f"screening failed: {exc}"})
        return
    _screen_ties = tie_sizes(candidates)
    yield event("stage", {"stage": "screening", "status": "done", "candidates": [
        {"name": c.name, "score": round(c.score, 1),
         "coverage": fit_score.score_coverage(c.dimension_scores, fit_score.DEFAULT_WEIGHTS),
         "tied_with": _screen_ties.get(c.name, 1) - 1,
         **build_evidence_card(c.path)}
        for c in candidates
    ]})

    if not candidates:
        yield event("error", {"message": "No candidates passed hard constraints — try relaxing budget/word-count assumptions."})
        return

    yield event("stage", {"stage": "synthesis", "status": "start"})
    prompt = build_synthesis_prompt(freeform_text, paper, candidates)
    try:
        async for text in PROVIDER.stream(prompt):
            yield event("text", {"delta": text})
    except Exception as exc:
        yield event("error", {"message": describe_provider_failure(exc, "writing the recommendation")})
        return
    yield event("stage", {"stage": "synthesis", "status": "done"})


# Sent on every SSE response. Without these the demo streams correctly on
# localhost and appears to hang behind a CDN, which is the worst possible place
# to find out.
#
#   X-Accel-Buffering  nginx and Cloudflare both buffer text/event-stream by
#                      default — Cloudflare has been observed holding output
#                      until roughly 100 KB accumulates, which for this payload
#                      means the entire recommendation lands at once, or never.
#                      This is the header both honour to turn that off.
#   no-transform       stops a proxy applying compression or minification,
#                      which reintroduces buffering by another route.
#   keep-alive         the connection must survive the whole generation.
#
# The 100-second origin timeout (Cloudflare 524) is not a risk here for a
# different reason: it measures silence, and the first `stage` event is emitted
# before any model call, so bytes are always flowing within milliseconds.
def describe_provider_failure(exc: Exception, stage: str) -> str:
    """Turn a provider exception into something a visitor can act on.

    The raw string is an SDK dump — `429 RESOURCE_EXHAUSTED {'error': {...}}` —
    which tells a researcher nothing and leaks internals to everyone else. The
    quota case matters most: the provider enforces its own per-day ceiling,
    separately from and possibly *below* GLOBAL_DAILY_LIMIT, so exhausting it
    while this page still believes it has budget left is a normal Tuesday
    rather than an edge case. It should read as "come back later" and point at
    the version with no cap, not as a crash.

    The real exception still goes to the server log; only the visitor gets the
    short version.
    """
    print(f"provider failure during {stage}: {exc!r}", file=sys.stderr)
    text = str(exc)
    lowered = text.lower()

    if any(k in lowered for k in ("429", "resource_exhausted", "quota", "rate limit",
                                  "too many requests")):
        return ("The demo has used up its model quota for now. It runs on one person's "
                "API key, and the provider caps that separately from the limits shown "
                "on this page. Try again later, or install the skill to run the same "
                "thing on your own key with no cap.")
    if any(k in lowered for k in ("401", "403", "api key", "permission denied",
                                  "unauthenticated", "invalid argument")):
        return ("The demo's model access is misconfigured — that is the maintainer's "
                "problem, not anything you did. The skill runs locally against the "
                "same knowledge base in the meantime.")
    if any(k in lowered for k in ("timeout", "timed out", "deadline")):
        return (f"The model took too long during {stage}. This usually clears on a "
                "retry.")
    return (f"Something failed during {stage}. If it keeps happening, an issue on the "
            "repository with what you pasted would help.")


SSE_HEADERS = {
    "Cache-Control": "no-cache, no-transform",
    "X-Accel-Buffering": "no",
    "Connection": "keep-alive",
}


def _rate_limited(request: Request) -> JSONResponse | None:
    """429 with a plain explanation, or None to proceed.

    Returned as JSON rather than as an SSE `error` event because the refusal
    happens before the stream starts, and a 429 the browser can see is more
    useful to anyone deploying this than a 200 carrying bad news.
    """
    refusal = LIMITER.check(ratelimit.client_key(request))
    if refusal is None:
        return None
    return JSONResponse(status_code=429, content={"message": refusal})


@app.post("/api/recommend")
async def recommend(req: RecommendRequest, request: Request):
    limited = _rate_limited(request)
    if limited is not None:
        return limited
    return StreamingResponse(sse_recommend(req), media_type="text/event-stream",
                             headers=SSE_HEADERS)


async def sse_followup(req: FollowupRequest) -> AsyncIterator[str]:
    def event(name: str, data: dict) -> str:
        return "event: " + name + "\ndata: " + json.dumps(data) + "\n\n"

    if PROVIDER is None:
        yield event("error", {"message": PROVIDER_ERROR})
        return
    # Enforced here as well as in the UI: the client is not trusted to cap its
    # own use of a key the server pays for.
    if req.asked_so_far >= MAX_FOLLOWUPS:
        yield event("error", {"message": "Follow-up limit reached (" + str(MAX_FOLLOWUPS)
                                         + "). Start a new search to explore further."})
        return

    contract = CONSUMPTION_CONTRACT + "\n\n---\n\n" if CONSUMPTION_CONTRACT else ""
    entries = []
    for name in req.candidate_names[:TOP_N_SCREEN]:
        path = _find_entry(name)
        if path:
            tier = fit_score.detect_tier(path.read_text(encoding="utf-8"))
            entries.append("=== " + name + " (evidence tier: " + tier + ") ===\n"
                           + build_candidate_excerpt(path))

    prompt = (
        "You are the Journal Atlas skill, answering a follow-up about a recommendation "
        "you already gave. Follow these rules when citing anything.\n\n" + contract
        + "The author's paper:\n\n" + req.paper_description + "\n\n"
        + "The recommendation you gave:\n\n" + req.recommendation + "\n\n"
        + (("Curated entries for the candidates, to answer from:\n\n"
            + "\n\n".join(entries) + "\n\n") if entries else "")
        + "---\n\nTheir follow-up question:\n\n" + req.question + "\n\n"
        + "Answer it directly and briefly. Stay inside what the entries actually say \u2014 if "
          "the answer is not in them, say so rather than filling the gap from general "
          "knowledge, and name what would be needed to answer it properly."
    )
    try:
        async for text in PROVIDER.stream(prompt):
            yield event("text", {"delta": text})
    except Exception as exc:
        yield event("error", {"message": describe_provider_failure(exc, "answering the follow-up")})
        return
    yield event("done", {"remaining": MAX_FOLLOWUPS - req.asked_so_far - 1})


@app.post("/api/followup")
async def followup(req: FollowupRequest, request: Request):
    limited = _rate_limited(request)
    if limited is not None:
        return limited
    return StreamingResponse(sse_followup(req), media_type="text/event-stream",
                             headers=SSE_HEADERS)


# ---------- Coverage disclosure ----------
#
# Computed from the corpus rather than written down, so the "what do you
# actually cover" panel cannot drift away from what is on disk. The prose
# framing lives in the frontend; the counts have to come from here.

FIELD_LABELS = {
    "psychology": "Psychology",
    "philosophy": "Philosophy",
    "hci": "HCI (journals)",
    "cognitive-science": "Cognitive science",
    "biology": "Biology",
    "conferences/hci": "HCI conferences",
    "multidisciplinary": "Multidisciplinary",
    "conferences/ml": "ML conferences",
    "medical": "Medical",
    "qualitative-methods": "Qualitative methods",
    "conferences/nlp": "NLP conferences",
    "physics": "Physics",
    "conferences/data-mining": "Data-mining conferences",
}

_COVERAGE_CACHE: dict | None = None


def compute_coverage() -> dict:
    """Per-field entry counts split by evidence tier, plus totals."""
    global _COVERAGE_CACHE
    if _COVERAGE_CACHE is not None:
        return _COVERAGE_CACHE

    fields: dict[str, dict[str, int]] = {}
    for path in sorted(JOURNALS_ROOT.rglob("*.md")):
        if "TEMPLATE" in path.name:
            continue
        key = "/".join(path.relative_to(JOURNALS_ROOT).parts[:-1])
        tier = fit_score.detect_tier(path.read_text(encoding="utf-8"))
        bucket = fields.setdefault(key, {"tier1": 0, "tier2": 0, "ai": 0, "total": 0})
        if tier.startswith("Tier 1"):
            bucket["tier1"] += 1
        elif tier.startswith("Tier 2"):
            bucket["tier2"] += 1
        else:
            bucket["ai"] += 1
        bucket["total"] += 1

    rows = [
        {"field": key, "label": FIELD_LABELS.get(key, key), **counts}
        for key, counts in sorted(fields.items(), key=lambda kv: -kv[1]["total"])
    ]
    _COVERAGE_CACHE = {
        "total": sum(r["total"] for r in rows),
        "fields": rows,
        # The four adjacent fields the corpus actually grew out of. Reported as
        # a share so the concentration is visible without the reader adding up
        # the table themselves. HCI's conference directory counts toward HCI —
        # splitting a field by venue type here would understate the
        # concentration, which is the one thing this disclosure must not do.
        "core_fields": ["psychology", "philosophy", "hci", "conferences/hci",
                        "cognitive-science"],
        # Written out rather than joined from the labels above, which would
        # read "HCI (journals), HCI conferences" and count HCI twice.
        "core_label": "psychology, philosophy, HCI and cognitive science",
        # Probed 2026-07-30. Not derivable from the corpus — absence of a
        # directory is not proof nobody looked — so it is recorded by hand and
        # dated.
        "absent": [
            "Library and information science (including digital libraries)",
            "Sociology",
            "Anthropology",
            "Chemistry, mathematics, and the earth sciences",
        ],
        "absent_checked": "2026-07-30",
    }
    return _COVERAGE_CACHE


@app.get("/api/coverage")
async def coverage():
    return compute_coverage()


@app.get("/healthz")
async def healthz():
    """Liveness probe.

    Separate from /api/health because deployment tooling probes this path by
    convention and wants a cheap, stable 200 — not the provider configuration
    and usage counters /api/health reports for a human debugging a deploy.
    """
    return {"status": "ok"}


@app.get("/api/health")
async def health():
    return {
        "status": "ok",
        "journals_root_exists": JOURNALS_ROOT.exists(),
        "provider": PROVIDER.name if PROVIDER else None,
        "extraction_model": PROVIDER.extraction_model if PROVIDER else None,
        "synthesis_model": PROVIDER.synthesis_model if PROVIDER else None,
        "provider_ready": PROVIDER is not None,
        "provider_error": PROVIDER_ERROR,
        "limits": LIMITER.snapshot(),
    }
