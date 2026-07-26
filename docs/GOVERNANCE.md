# Governance: Disputing a Subjective Claim

**Status: Adopted (2026-07-27) — policy decided.** The `Disputed`-banner
code mechanism (§4) is a pending follow-up implementation, not yet built.
This closes the gap `ATLAS_V2_DESIGN.md` §9 flags as blocking for public
release: Journal Atlas's Soft Metadata sections make subjective claims
(political leanings, reviewer culture, framing expectations) about real,
named journals and publishers; this document is the formal path for
someone who believes a claim about their journal is wrong to get it
corrected.

## 1. What this covers

**In scope — subjective claims**, the parts of an entry that describe a
journal's culture or disposition rather than a verifiable fact:
`Soft Metadata > Epistemological & Political Leanings`, `Framing
Requirements`, `Reviewer Pool Characteristics`, `Voice & Style`,
`Sensitive Topics` receptiveness ratings, and all of `Strategic Notes`
(Hard Blockers, Best/Not-Recommended-For, Rejection Fallback Chain).

**Out of scope — use [Update Journal Info](../.github/ISSUE_TEMPLATE/update-journal.md) instead.**
Factual/structural fields (Identity, Metrics, Subject Density, Policies —
AI/Preprint/Open Access/Peer Review type) are either sourced from OpenAlex
or a publisher's own published policy page. A claim there is either right
or wrong, not disputed in the reputational sense this document addresses;
"it's outdated" or "it's factually wrong" is a correction, not a dispute.

## 2. The writing-time rule this is paired with

**No unsourced subjective claim.** Every Soft Metadata assertion about a
real journal must be traceable to *something* — even a low-confidence
something:

- Tier 1: a specific citation (article count, source URL, submission
  experience).
- Tier 2: explicitly labeled as family/community-level convention, not
  claimed as journal-specific.
- AI-Researched: a cited source and a `signal_quality` score.

This is already [CONSUMPTION_CONTRACT.md](../skills/journal-atlas/CONSUMPTION_CONTRACT.md)'s
rule #1-#3 applied at write time, not just read time: if a claim can't be
labeled with one of the above, it shouldn't be written at all — flagged as
`*(pending)*` instead.

## 3. Filing a dispute

Open a [Dispute a Claim](../.github/ISSUE_TEMPLATE/dispute-claim.md) issue.
Anyone can file one — a journal editor, an author who submitted there, or
a maintainer who spots something off during review. The issue asks for:
the specific claim (quoted, not paraphrased), why it's believed inaccurate,
any supporting context, and the disputant's relationship to the journal
(for the maintainer's context when weighing it — not a gate on who may
file).

## 4. While a dispute is open

The disputed entry gets a **`Disputed`** marker — orthogonal to the
existing Tier 1 / Tier 2 / AI-Researched / Skeleton labels (a dispute is
about one claim's accuracy, not about which evidence-gathering method
produced it, so it can sit on top of any tier). The marker:

- Names the specific disputed field(s), not the whole entry — the rest of
  the entry's claims stand.
- Links to the open issue.
- Is visible wherever the tier banner is (the entry file itself, and
  anywhere the skill/demo surfaces tier information, e.g. the demo's
  evidence cards) — a disputed claim should never look more confident than
  an undisputed one.

*(This section describes the intended behavior; the actual banner-parsing
code change — extending `fit_score.detect_tier()` and the demo's evidence
card — is a follow-up implementation step once this policy's shape is
confirmed, not bundled into this draft.)*

## 5. Resolution

The maintainer (repo owner) makes the final call — this is not a voting or
consensus process. Three outcomes:

1. **Corrected** — the claim is edited or removed; a Changelog row records
   what changed and why, and the `Disputed` marker is removed.
2. **Confirmed as-is** — the maintainer finds the existing claim
   sufficiently supported; the marker is removed and the issue closed with
   the reasoning stated (so the same dispute isn't silently reopened later
   without new information).
3. **Marked genuinely uncertain** — both sides have a reasonable point and
   there's no way to fully resolve it from available evidence (mirrors how
   `EXISTING_ENTRY_CONFLICTS.md` already handles a few existing cases); the
   claim is softened to say so explicitly rather than asserting either
   side.

**Response-time commitment**: acknowledged within 2 weeks, resolved on a
best-effort basis (solo-maintained — this is a deliberately modest,
sustainable promise, not an SLA).

**Affiliation weight**: judged purely on the evidence offered, regardless
of who files it. A verified editor and an anonymous reader get the same
consideration — the point of a citation-based system is that the citation
carries the weight, not the citer.

**Repeat disputes**: a claim already resolved (confirmed or marked
uncertain) is not reopened absent genuinely new evidence — prevents the
mechanism being used to simply wear down an unwelcome but accurate claim
through repetition.
