# WO2 — Soft-Metadata Batch (AI-bootstrapped, facts-only)

> **Type**: model-intensive AI research — **this is where surplus usage should go.**
> Parallelizable per journal. Follows [ATLAS_V2_DESIGN.md](../ATLAS_V2_DESIGN.md)
> §2 (layers) + §3 (facts-not-verbatim rule).
> **Input**: a batch of journals (name + ISSN). Start with the psychology +
> adjacent core; scale outward by OpenAlex citation rank (demand-tiered).

## Goal
For each journal, produce a **facts-only** soft-metadata draft with per-field
`signal_quality` (0–5) and provenance, leaving fields **blank** where no
first-hand public signal exists. Output merges into the curated
`references/journals/**.md` entries (TEMPLATE.md Soft Metadata + Strategic Notes
sections) or a structured JSON for review.

## Per-journal procedure (three layers)

1. **Policy** (Layer P): AI-use policy (leniency 1–5 + permission gate),
   peer-review type, preprint policy, OA/APC. Prefer **publisher-level** public
   pages (model ~20 publishers once, inherit); fetch journal-specific only when
   it differs. Hardened HTTP client (browser UA + cookie jar + follow redirects)
   — headless only as a T&F-Cloudflare fallback. Store the **fact + source URL**,
   not the verbatim policy text.
2. **Positioning** (Layer P): what it accepts *now*. Default = OpenAlex
   `topics`/`topic_share` (free, no LLM). Deep = synthesize recent article
   title+abstract sample. Add **current signals**: special-issue CFPs
   (Frontiers Research Topics / T&F / WikiCFP), new-editor editorials (PMC OA).
3. **Experiential** (Layer E): review time, desk-reject %, acceptance note,
   reviewer culture. Sources, **facts only, query-time**: SciRev (extract
   individual numbers, never copy the DB), **Chinese forums 小木虫 / fabiaoji /
   知乎 (mandatory — often the richest signal)**, Reddit (OAuth, non-commercial).
   **If no first-hand source exists → leave blank, set signal_quality, record
   that LetPub/SciRev returned 0.** Never fill with generic narrative.

## Hard rules
- **Facts, not verbatim.** Store normalized facts + source URLs. No forum posts,
  policy prose, or full abstracts baked in (copyright / CC BY-SA incompatible).
- **Honest blank beats filler.** The long-tail cliff is expected; a blank field
  with `signal_quality: 0` is a correct output, not a failure.
- **Tag every claim** with its source type + URL + date.
- **Cross-language is mandatory** — always check Chinese sources, not just English.
- **Red-license sources (SciRev / Reddit / Sherpa / PubPeer / SJR)** are
  query-time only: extract the fact, keep the link, do not persist verbatim.
- **No subjective claim without a source** (defamation/reputation guard for
  political-leaning / reviewer-culture fields).

## Output schema (per journal)
```
{ issn, name,
  ai_policy: {leniency_1_5, gate, summary, source_url, signal_quality},
  peer_review: {type, source_url},
  preprint: {allowed, source_url},
  positioning: {accepts_now, methods_welcome, framing_required, sources[], signal_quality},
  experiential: {review_time_months, desk_reject_pct, acceptance_note,
                 reviewer_culture, sources[], signal_quality},
  sensitive_topics: {...},
  blanks: [ {field, why} ],           # explicit, e.g. "review_time: SciRev 0 reviews"
  cross_language_checked: [...],
  overall_signal_quality }
```

## Acceptance
- N journals with per-field `signal_quality` + provenance.
- Explicit blanks where no signal (with the "why").
- Zero unsourced subjective claims. Zero verbatim third-party prose.

## Batch 1 (psychology + adjacent core, launched 2026-07-13)
JPSP · Current Psychology · Theory & Psychology · Qualitative Research in
Psychology · Frontiers in Psychology · Personality and Individual Differences ·
Journal of Happiness Studies · New Ideas in Psychology · Review of General
Psychology · Psychological Science · Collabra: Psychology · Journal of Research
in Personality. Scale subsequent batches by OpenAlex citation rank.
