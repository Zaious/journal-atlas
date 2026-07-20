# Existing-Entry Merge — Flagged Conflicts (RESOLVED 2026-07-20)

> Generated 2026-07-13 from the 112-file careful comparison merge (see GAPS_AND_NOTES.md).
> Resolved 2026-07-20 via an autonomous deep-reasoning + live-verification pass, followed by
> an adversarial re-verification pass (3 independent skeptical fact-checkers) on every finding
> whose only evidence was a WebSearch snippet rather than a direct primary-source fetch.

**Total: 193 conflicts across 98 journals.**

| Outcome | Count |
|---|---|
| Adopted the new (AI-research) finding, verified live | 76 |
| Harmonized wording (both sides described the same underlying fact) | 37 |
| Kept existing content (new finding out of scope, unconvincing, or a scoring-calibration disagreement) | 72 |
| Escalated to human — genuinely out of scope or a subjective judgment call | 9 |

Every resolution that changed a curated entry is recorded in that entry's own
Changelog section, dated 2026-07-20. The full per-journal reasoning trail
(including every agent's rationale and evidence citations) is preserved in
`_merge_patch_proposals.json` and the workflow transcripts for this pass.

## Adversarial-verification catch

Of the resolutions whose only evidence was a WebSearch snippet (direct fetch
blocked by 403/Cloudflare/paywall), 20 were independently re-checked by 3
skeptical fact-checkers each before being trusted:

- **19/20 confirmed** on independent re-verification (several upgraded from
  snippet-only to a genuine live primary-source fetch in the process).
- **1/20 refuted** and reverted: *Qualitative Inquiry*'s Peer Review Type was
  briefly changed to "Open peer review" based on marketing-page language; all
  3 re-verifiers independently fetched the journal's actual peer-review-policy
  page and found it explicitly classified as Double-anonymized. The entry has
  been corrected back, with the stronger, now-verified citation.
- 2 more were refined (not reverted) after re-verification surfaced additional
  nuance beyond the original finding: *Counselling Psychology Quarterly*'s
  Peer Review Type turned out to be a genuine self-contradiction on the
  publisher's own site (flagged as unclear rather than asserted either way),
  and *The Clinical Neuropsychologist*'s "journal-specific AI policy" claim
  was corrected to note a real disclosure-checklist item exists even though
  there's no dedicated AI-policy page.

## Escalated to human (9)

These were correctly left untouched — either because the finding falls in a
Soft Metadata / Strategic Notes subjective subsection outside this pass's
editing scope (Framing Requirements, Best Suited For, Epistemological &
Political Leanings, Reviewer Pool Characteristics, etc.), or because the
disagreement is a rating-scale calibration judgment call with no fact to
verify. Each entry's own file retains the original finding in its
"AI-Research Notes" supplement for reference.

1. ~~**ACM Transactions on Accessible Computing (TACCESS)** — Open Access
   Model/APC~~ — **done 2026-07-20**: Open Access table updated to Full OA
   / ~$1,450 standard APC (2026 transitional rate $250-$350), per ACM's
   2026-01-01 full-OA conversion.
2. **Alzheimer's & Dementia** — Soft Metadata > Framing Requirements / Best
   Suited For: positioning judgment (bench-to-bedside framing, AI/digital
   health scope), out of scope.
3. **Cognitive Therapy and Research** — Soft Metadata > Methodological
   Preferences / Framing Requirements: editorial-direction judgment, out of
   scope.
4. **Counselling Psychology Quarterly** — Soft Metadata > Framing
   Requirements / Epistemological & Political Leanings: qualitative
   editorial-direction judgment, out of scope.
5. **IEEE Transactions on Affective Computing** — Soft Metadata (Framing
   Requirements / Best Suited For / Reviewer Pool Characteristics): editorial
   judgment on thin/anecdotal evidence, out of scope.
6. **Journal of Applied Social Psychology** — Soft Metadata > Reviewer Pool
   Characteristics / Practical Concerns: whether an n=1 anecdote should be
   promoted into the main narrative — an editorial weighting call.
7. **Journal of Personality Assessment** — AI Policy Leniency (1-5): both
   sides agree on the underlying policy; the only disagreement is whether it
   scores 3 or 4 — a rubric-calibration judgment, not a fact dispute.
8. **Social and Personality Psychology Compass** — Strategic Notes > Hard
   Blockers / Framing Requirements: out of scope; independently corroborated
   via Wiley's own author guidelines that the journal now also accepts
   concise empirical reports (3000-5000 words), not just reviews — worth a
   maintainer follow-up.
9. **Transactions of the Association for Computational Linguistics** —
   Soft Metadata > Reviewer Pool Characteristics / Practical Concerns:
   whether community-forum commentary should be folded into the main
   narrative — an editorial weighting call.
