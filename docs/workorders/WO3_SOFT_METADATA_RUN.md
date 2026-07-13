# WO3 — Soft-Metadata Gathering Run (dispatch to a separate session)

> **Architecture authority: the origin session (this repo's design).** You (the
> executing session) run this work order **as written** — do not redesign the
> schema, the rules, or the target list. If something seems wrong, record it and
> report back; do not "improve" the architecture. Your job is to gather data.
> **This is the token-heavy job — it is where surplus usage should go.**

## What you're doing
Run the fixed WO2 soft-metadata pipeline over the prepared target list, producing
facts-only drafts (per-field `signal_quality`, provenance, honest blanks).

## Inputs (already prepared, do not regenerate)
- **Workflow (the architecture — fixed):**
  `skills/journal-atlas/scripts/soft_metadata_workflow.js`
- **Target lists (real ISSNs, demand-ranked + curated/verified supplement, deduped):**
  - `skills/journal-atlas/references/_soft_metadata_drafts/targets_psychology.json` — 185 journals
  - `skills/journal-atlas/references/_soft_metadata_drafts/targets_philosophy.json` — 107 journals
  - `skills/journal-atlas/references/_soft_metadata_drafts/targets_hci.json` — 64 journals
  - Each is an array of `{name, issn, works_in_field, source}` where `source` is
    `"ranked"` (OpenAlex demand-ranked), `"repo-curated"` (from existing
    `references/journals/**.md`), or `"manual-supplement-verified"` (individually
    ISSN-verified against OpenAlex, added to round out coverage where automatic
    ranking under- or mis-classified — see caveat below).
- **Rules reference:** `docs/workorders/WO2_SOFT_METADATA_BATCH.md` (the hard rules
  are already baked into the workflow's prompt; read WO2 to understand them).

## Procedure (batched — recommended)
Run the three domains as separate batch series (don't mix journals from
different domains into the same chunk — keep provenance clean per domain).
Process each domain's list in chunks of ~15–20 so each batch checkpoints to its
own file.

1. Load a target list. Split into chunks of ~18.
2. For each chunk `i` of domain `<d>` (`psych` / `phil` / `hci`), run:
   ```
   Workflow({
     scriptPath: "<abs path>/skills/journal-atlas/scripts/soft_metadata_workflow.js",
     args: { batch_name: "<d>-b<i>", journals: <chunk>, effort: "medium" }
   })
   ```
3. When it completes, save the returned JSON to
   `skills/journal-atlas/references/_soft_metadata_drafts/<d>-b<i>.json`.
4. Repeat for all chunks, all three domains. If a run dies mid-way, relaunch
   with `resumeFromRunId` — completed journals replay from cache.

One-shot alternative: pass a whole domain's list as `args.journals` in a single
call (concurrency is capped internally, resume-friendly). Simpler to launch,
but no per-batch checkpoints and a very long single run.

## Effort / cost
- `effort: "medium"` is the default for scale (185+107+64 = 356 journals total).
  Bump to `"high"` for a smaller, higher-value sub-batch. Batch 1 (12 psychology
  journals, high) cost ~615k tokens; expect the full run to be several million
  tokens — that is the point.

## Known data-quality caveat on the target lists
OpenAlex's automatic topic classification gets noisy at low article-volume:
during list-building, real Indonesian business/vocational-education journals
were found auto-tagged as "Human-Computer Interaction," and real French
linguistics/rhetoric journals as "Philosophy." These were caught and removed
before finalizing the lists above (already fixed — no action needed), but if a
journal in a batch turns out to be obviously off-domain when you research it
(e.g., a business journal in the HCI list), treat that as a signal the source
list itself has a residual error: note it in your batch report rather than
silently researching a wrong-domain journal.

## Rules you must NOT relax (already in the workflow prompt)
- **Facts, not verbatim.** Store facts + source URLs only. No forum/policy/abstract
  prose copied in.
- **Honest blank beats filler.** No source → null + `signal_quality` + a `blanks[]`
  reason. Never invent review times, acceptance rates, or reviewer-culture claims.
- **Cross-language mandatory** — always check 小木虫 / fabiaoji / 知乎, not just English.
- **No unsourced subjective claims** (political leaning / reviewer culture).

## Deliverable back to the origin session
- `references/_soft_metadata_drafts/psych-b*.json` files (one per batch).
- A one-line coverage note per batch: how many journals reached experiential
  `signal_quality ≥ 3` vs how many are honest-blank (this measures where the
  cross-language moat paid off).
- **Do not** merge into `references/journals/**.md` or commit — the origin
  session reviews the drafts and decides what merges. Leave the JSON for review.

## Reference: what a good entry looks like
See `references/_soft_metadata_drafts/batch1_psychology-core.json` (12 entries
already produced by the origin session) for the exact expected output shape and
quality bar.
