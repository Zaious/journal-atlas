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
instead of a blank spinner. Rate-limit / abuse protection is deliberately
NOT implemented here (this is the local-dev / architecture scaffold) — see
demo/README.md for what a deployed version still needs.
"""
from __future__ import annotations

import json
import os
import sys
from dataclasses import asdict
from pathlib import Path
from typing import AsyncIterator

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

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
    allow_methods=["POST"],
    allow_headers=["*"],
)


class RecommendRequest(BaseModel):
    paper_description: str


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


async def extract_paper(provider, freeform_text: str) -> fit_score.Paper:
    data = await provider.extract(_build_extraction_prompt(freeform_text), PAPER_SCHEMA)
    return fit_score.Paper.from_dict(data)


def unstated_constraints(paper: fit_score.Paper) -> list[str]:
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
    return unstated


# ---------- Stage 2: screening (fit_score.py, unmodified) ----------

MIN_CANDIDATES_BEFORE_WIDENING = 3


def _score_against(paper: fit_score.Paper) -> list[fit_score.JournalScore]:
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
        if elim:
            js.eliminated, js.elimination_reason = True, elim
        else:
            js.score, js.dimension_scores = fit_score.compute_score(
                paper, journal_data, fit_score.DEFAULT_WEIGHTS)
        results.append(js)
    return sorted((r for r in results if not r.eliminated), key=lambda r: -r.score)


def screen_candidates(paper: fit_score.Paper) -> list[fit_score.JournalScore]:
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
    passing = _score_against(paper)
    if paper.fields and len(passing) < MIN_CANDIDATES_BEFORE_WIDENING:
        from dataclasses import replace
        passing = _score_against(replace(paper, fields=[]))
    return passing[:TOP_N_SCREEN]


# ---------- Stage 3: synthesis (Sonnet, streamed) ----------

def build_evidence_card(path: Path) -> dict:
    """Tier + top-cited topic rows for the screening SSE event — real,
    checkable evidence behind a fit_score number, not just the number."""
    content = path.read_text(encoding="utf-8")
    try:
        journal_data = fit_score.parse_journal_file(path)
    except Exception:
        journal_data = {}
    top_topics = sorted(journal_data.get("topics") or [], key=lambda t: -t[1])[:3]
    return {
        "tier": fit_score.detect_tier(content),
        "disputes": fit_score.detect_disputes(content),
        "top_topics": [{"name": name, "count": count} for name, count in top_topics],
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


def build_synthesis_prompt(freeform_text: str, paper: fit_score.Paper, candidates: list[fit_score.JournalScore]) -> str:
    sections = []
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
        header = f"=== {c.name} (fit_score {c.score:.1f}/100 | evidence tier: {tier}"
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
        "and why they rank below the top pick, (3) tier/uncertainty flags per the "
        "rules above for any candidate that isn't Tier 1, (4) one rejection-fallback "
        "suggestion if the top pick doesn't work out. Keep it under 400 words."
    )


async def sse_recommend(freeform_text: str) -> AsyncIterator[str]:
    def event(name: str, data: dict) -> str:
        return f"event: {name}\ndata: {json.dumps(data)}\n\n"

    if PROVIDER is None:
        yield event("error", {"message": PROVIDER_ERROR})
        return

    # Both stages are awaited/streamed natively rather than blocking the event
    # loop for their full duration.

    yield event("stage", {"stage": "parsing", "status": "start"})
    try:
        paper = await extract_paper(PROVIDER, freeform_text)
    except Exception as exc:
        yield event("error", {"message": f"extraction failed: {exc}"})
        return
    yield event("stage", {"stage": "parsing", "status": "done", "paper": asdict(paper),
                          "unstated": unstated_constraints(paper)})

    yield event("stage", {"stage": "screening", "status": "start"})
    try:
        candidates = screen_candidates(paper)
    except Exception as exc:
        yield event("error", {"message": f"screening failed: {exc}"})
        return
    yield event("stage", {"stage": "screening", "status": "done", "candidates": [
        {"name": c.name, "score": round(c.score, 1), **build_evidence_card(c.path)}
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
        yield event("error", {"message": f"synthesis failed: {exc}"})
        return
    yield event("stage", {"stage": "synthesis", "status": "done"})


@app.post("/api/recommend")
async def recommend(req: RecommendRequest):
    return StreamingResponse(sse_recommend(req.paper_description), media_type="text/event-stream")


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
    }
