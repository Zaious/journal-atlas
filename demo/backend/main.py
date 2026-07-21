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
import re
import sys
from dataclasses import asdict
from pathlib import Path
from typing import AsyncIterator

import anthropic
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

load_dotenv()

# Reuse fit_score.py directly — no reimplementation of the scoring logic.
SKILL_SCRIPTS = Path(__file__).resolve().parents[2] / "skills" / "journal-atlas" / "scripts"
sys.path.insert(0, str(SKILL_SCRIPTS))
import fit_score  # noqa: E402

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

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
EXTRACTION_MODEL = "claude-haiku-4-5"
SYNTHESIS_MODEL = "claude-sonnet-5"
REQUEST_TIMEOUT_SECONDS = 60.0
MAX_RETRIES = 2

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
        "apc_budget": {"type": ["integer", "null"], "description": "USD the author can pay in publication fees; 0 if none mentioned or implied"},
        "oa_required": {"type": "boolean", "description": "true only if the author explicitly needs immediate open access"},
        "ai_usage": {"type": "boolean", "description": "true if the text mentions AI-assisted writing"},
        "sensitive_content": {"type": "array", "items": {"type": "string"}, "description": "any sensitive topics the paper covers, empty if none"},
        "irb": {"type": "boolean", "description": "true unless the text says there is no IRB/ethics approval"},
        "preprint_intent": {"type": "boolean"},
        "timeline_priority": {"type": "string", "enum": ["fast", "normal", "flexible"]},
        "fields": {"type": "array", "items": {"type": "string"}, "description": "which curated field directories to search: psychology, hci, philosophy, cognitive-science, biology, medical, physics, multidisciplinary, qualitative-methods (empty = search all)"},
    },
    "required": ["topics", "methodology", "sensitive_content", "fields", "timeline_priority", "oa_required", "ai_usage", "irb", "preprint_intent"],
    "additionalProperties": False,
}

# Forced single-tool call, not an `output_config`/json_schema response format —
# anthropic==0.69.0's Messages API has no such top-level parameter (verified
# against the installed SDK's actual signature; passing it raises TypeError on
# every request). Tool-forcing is the long-supported, SDK-verified way to get
# schema-conforming JSON out of Messages.create().
EXTRACT_TOOL = {
    "name": "extract_paper_attributes",
    "description": "Extract structured attributes from a paper description for academic-journal matching.",
    "input_schema": PAPER_SCHEMA,
}


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


async def extract_paper(client: "anthropic.AsyncAnthropic", freeform_text: str) -> fit_score.Paper:
    response = await client.messages.create(
        model=EXTRACTION_MODEL,
        max_tokens=1024,
        tools=[EXTRACT_TOOL],
        tool_choice={"type": "tool", "name": "extract_paper_attributes"},
        messages=[{
            "role": "user",
            "content": _build_extraction_prompt(freeform_text),
        }],
    )
    tool_use = next(b for b in response.content if b.type == "tool_use")
    return fit_score.Paper.from_dict(tool_use.input)


# ---------- Stage 2: screening (fit_score.py, unmodified) ----------

def screen_candidates(paper: fit_score.Paper) -> list[fit_score.JournalScore]:
    candidate_paths = fit_score.collect_journals(paper, JOURNALS_ROOT)
    results = []
    for path in candidate_paths:
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
            js.score, js.dimension_scores = fit_score.compute_score(paper, journal_data, fit_score.DEFAULT_WEIGHTS)
        results.append(js)
    passing = sorted((r for r in results if not r.eliminated), key=lambda r: -r.score)
    return passing[:TOP_N_SCREEN]


# ---------- Stage 3: synthesis (Sonnet, streamed) ----------

def _extract_h2_section(content: str, name: str) -> str:
    """Whole ## section incl. its ### children, stopping at the next ## heading.

    Unlike fit_score._extract_subsection() (which stops at the next ## OR ###
    and is meant for pulling one named subsection for scoring), this is for
    pulling an entire top-level block — e.g. all of Soft Metadata's children
    — intact for the synthesis prompt.
    """
    match = re.search(
        rf"^## +{re.escape(name)}\b[^\n]*\n(.*?)(?=^## +|\Z)",
        content, re.MULTILINE | re.DOTALL,
    )
    return match.group(1).strip() if match else ""


def detect_tier(content: str) -> str:
    """Tier label from Soft Metadata's banner, per CONSUMPTION_CONTRACT.md's
    table: Tier 2 -> [!WARNING], AI-Researched -> [!NOTE] + "AI-Researched",
    Skeleton -> [!NOTE] alone (0 entries in the corpus today, kept for
    completeness), no banner -> Tier 1."""
    banner = _extract_h2_section(content, "Soft Metadata")[:400]
    if "[!WARNING]" in banner:
        return "Tier 2 (community estimate)"
    if "AI-Researched" in banner:
        return "AI-Researched"
    if "[!NOTE]" in banner:
        return "Skeleton"
    return "Tier 1 (evidence-backed)"


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
        "tier": detect_tier(content),
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
        text = _extract_h2_section(content, section_name)
        if text:
            parts.append(f"#### {section_name}\n{text}")
    return "\n\n".join(parts)


def build_synthesis_prompt(freeform_text: str, paper: fit_score.Paper, candidates: list[fit_score.JournalScore]) -> str:
    sections = []
    for c in candidates:
        try:
            excerpt = build_candidate_excerpt(c.path)
        except OSError:
            continue
        sections.append(f"=== {c.name} (fit_score {c.score:.1f}/100) ===\n{excerpt}")
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

    if not ANTHROPIC_API_KEY:
        yield event("error", {"message": "ANTHROPIC_API_KEY not set on the server — see demo/backend/.env.example"})
        return

    # Async client — both calls below are awaited/streamed natively rather than
    # blocking the event loop for their full duration (the sync client's
    # `.stream()` would otherwise stall every other concurrent request for as
    # long as Sonnet takes to finish generating).
    client = anthropic.AsyncAnthropic(
        api_key=ANTHROPIC_API_KEY,
        timeout=REQUEST_TIMEOUT_SECONDS,
        max_retries=MAX_RETRIES,
    )

    yield event("stage", {"stage": "parsing", "status": "start"})
    try:
        paper = await extract_paper(client, freeform_text)
    except Exception as exc:
        yield event("error", {"message": f"extraction failed: {exc}"})
        return
    yield event("stage", {"stage": "parsing", "status": "done", "paper": asdict(paper)})

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
        async with client.messages.stream(
            model=SYNTHESIS_MODEL,
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            async for text in stream.text_stream:
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
    return {"status": "ok", "journals_root_exists": JOURNALS_ROOT.exists(), "api_key_configured": bool(ANTHROPIC_API_KEY)}
