// Journal Atlas — soft-metadata gathering workflow (implements WO2).
// The ARCHITECTURE is fixed by this script; the executing session only supplies targets.
//
// Invoke (in a Claude Code session with the Workflow tool):
//   Workflow({ scriptPath: "<this file>", args: { batch_name: "psych-b2",
//              journals: [ {name, issn}, ... ], effort: "medium" } })
//
// Returns { batch, built_on, entries: [ <ENTRY_SCHEMA> ] }. The invoking session
// saves that JSON to references/_soft_metadata_drafts/<batch_name>.json.
// Resume-friendly: re-invoke with resumeFromRunId to replay completed journals.

export const meta = {
  name: 'soft-metadata-gather',
  description: 'WO2: AI-bootstrap facts-only soft metadata for a batch of journals (honest-blank, cross-language)',
  phases: [{ title: 'Research', detail: 'one agent per journal — policy + positioning + experiential, facts only' }],
}

const ENTRY_SCHEMA = {
  type: 'object',
  properties: {
    issn: { type: 'string' }, name: { type: 'string' },
    ai_policy: { type: 'object', properties: {
      leniency_1_5: { type: ['integer', 'null'] }, gate: { type: ['string', 'null'] },
      summary: { type: ['string', 'null'] }, source_url: { type: ['string', 'null'] },
      signal_quality: { type: 'integer' } }, required: ['signal_quality'] },
    peer_review: { type: 'object', properties: {
      type: { type: ['string', 'null'] }, source_url: { type: ['string', 'null'] } } },
    preprint: { type: 'object', properties: {
      allowed: { type: ['string', 'null'] }, source_url: { type: ['string', 'null'] } } },
    positioning: { type: 'object', properties: {
      accepts_now: { type: ['string', 'null'] },
      methods_welcome: { type: 'array', items: { type: 'string' } },
      framing_required: { type: ['string', 'null'] },
      sources: { type: 'array', items: { type: 'string' } },
      signal_quality: { type: 'integer' } }, required: ['signal_quality'] },
    experiential: { type: 'object', properties: {
      review_time_months: { type: ['string', 'null'] }, desk_reject_pct: { type: ['string', 'null'] },
      acceptance_note: { type: ['string', 'null'] }, reviewer_culture: { type: ['string', 'null'] },
      sources: { type: 'array', items: { type: 'string' } },
      signal_quality: { type: 'integer' } }, required: ['signal_quality'] },
    sensitive_topics_note: { type: ['string', 'null'] },
    blanks: { type: 'array', items: { type: 'object', properties: {
      field: { type: 'string' }, why: { type: 'string' } }, required: ['field', 'why'] } },
    cross_language_checked: { type: 'array', items: { type: 'string' } },
    overall_signal_quality: { type: 'integer' },
  },
  required: ['issn', 'name', 'ai_policy', 'positioning', 'experiential', 'blanks', 'overall_signal_quality'],
}

const RULES = `You are producing a FACTS-ONLY soft-metadata draft for one academic journal, per Journal Atlas work order WO2. Today is 2026-07-13. Load WebSearch/WebFetch via ToolSearch.

Research THREE layers and return the structured schema:
1. POLICY: AI-use policy (leniency 1-5 where 1=ban, 5=fully open; + permission gate yes/no/conditional), peer-review type, preprint policy. Prefer the publisher's public policy page; note if journal-specific. Store the FACT + source URL, never the verbatim policy text.
2. POSITIONING: what the journal actually accepts NOW — infer from recent (2024-2026) article titles/topics + aims&scope + any current special-issue CFP. methods_welcome = list. framing_required if any.
3. EXPERIENTIAL: review time, desk-reject %, acceptance note, reviewer culture. Sources are query-time, FACTS ONLY: SciRev (extract the numbers, do not copy prose), and CROSS-LANGUAGE IS MANDATORY — check Chinese sources 小木虫 muchong.com, fabiaoji, 知乎 zhihu, and English Reddit r/AskAcademia.

HARD RULES:
- Facts, not verbatim. Tag every claim with source type + URL.
- HONEST BLANK beats filler: if a field has no first-hand public source, leave it null, set that layer's signal_quality low, and add a blanks[] entry saying why (e.g. "review_time: SciRev 0 reviews, no forum discussion"). NEVER invent generic numbers or generic reviewer-culture narrative.
- No subjective claim (political leaning, reviewer culture) without a concrete source.
- signal_quality per layer 0-5: 5=first-hand abundant, 3-4=multiple public discussions incl cross-language, 1-2=publisher-policy/scope-only, 0=nothing (blank).
- List cross_language_checked with what each source yielded (incl "0 results" honestly).

Prose fields may be in Traditional Chinese. A truthful sparse entry beats a rich fabricated one.`

phase('Research')

const journals = (args && args.journals) || []
if (!journals.length) throw new Error('args.journals is required: [{name, issn}, ...]')
const effort = (args && args.effort) || 'medium'
const batchName = (args && args.batch_name) || 'batch'
log(`WO2 ${batchName}: ${journals.length} journals @ effort=${effort}`)

const entries = await parallel(journals.map(j => () =>
  agent(`${RULES}\n\nJOURNAL: ${j.name} (ISSN ${j.issn}).`,
    { label: `soft:${j.issn}`, phase: 'Research', schema: ENTRY_SCHEMA, effort })
    .then(e => e ? { ...e, issn: e.issn || j.issn, name: e.name || j.name } : null)
))

return { batch: batchName, built_on: '2026-07-13', entries: entries.filter(Boolean) }
