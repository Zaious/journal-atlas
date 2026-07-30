# JCDL Demo Readiness

What Journal Atlas needs in order to be a credible JCDL Posters & Demos
submission. Scoped to that one goal — not to the project being finished (see
[PROJECT_COMPLETION.md](PROJECT_COMPLETION.md) for that, which is a much
larger and different target).

Status of this document: assessment written 2026-07-27 against the state of
`main` at that date. Track-requirement facts were read from the official
JCDL 2026 CFP; everything else is measured from the repo.

---

## 1. What the track actually requires

From the JCDL 2026 Call for Posters and Demos:

| Requirement | Detail |
|---|---|
| Length | 2–4 pages excluding references (1 page for non-archival fast abstracts) |
| Format | ACM two-column, PDF |
| Review | **Single-blind** — author names and affiliations included |
| Demo-specific | **A working link is mandatory**: either a video of up to 5 minutes, or a live online interface |
| Deadline | 2026-08-14 AoE (notification 08-31, camera-ready 09-10) |
| Sessions | Hybrid; poster/demo sessions run in Gather.Town, with a 1-minute "Minute Madness" pitch |
| Awards | Best Poster / Best Demo |

The CFP explicitly invites emerging AI/LLM topics and work from academic,
industry, and cultural-heritage sectors.

Note the main research track (10-page full / 4-page short) closed 2026-07-15.
Posters & Demos is the remaining route for this cycle.

## 2. What a demo reviewer is actually judging

A demo track is not a paper track with fewer pages. The question is not "is
this validated" but roughly:

1. **Does the artifact exist and work?** — this is the whole point of the
   mandatory link.
2. **Is it relevant to digital libraries?** — scholarly metadata
   infrastructure is squarely in scope.
3. **Is there something here I haven't seen?** — novelty of approach, not
   size of evaluation.
4. **Would conference attendees want to stand at this booth?**

That framing is favourable to this project's current state. The absence of a
formal evaluation is survivable in a demo; the absence of a working artifact
is not.

## 3. The argument to make

Two claims, in this order. The first gets attention, the second is what a
JCDL audience will actually find interesting.

**Claim 1 — the metadata gap.** Existing journal-matching tools (JANE,
publisher-side finders, and the open-source Open Journal Matcher this project
credits in its README) match on **topic similarity**. None of them model
reviewer culture, framing requirements, sensitive-topic tolerance, AI-use
policy, first-person voice acceptance, or rejection-fallback paths. Those are
the things that actually decide whether a non-mainstream manuscript survives
review, and they are exactly what an author cannot recover from an abstract
similarity score.

**Claim 2 — contestable, confidence-labelled subjective metadata.** This is
the more novel contribution for this venue. The knowledge base makes
subjective claims about real, named journals, and it carries machinery for
being honest and answerable about them:

- a tier system separating evidence-backed from community-estimate from
  AI-researched, surfaced in the data and to every consumer
- per-field `signal_quality` and deliberate blanks instead of plausible
  filler
- a written consumption contract that every consumer (skill, chat package,
  demo backend) points at rather than restating
- an adopted dispute mechanism with a `Disputed` marker that is orthogonal
  to tier, so a contested claim never renders as confidently as a settled one

Provenance, trust, and contestability in curated metadata is a digital
libraries problem. Most demo submissions overclaim; this one has a documented
discipline about *not* overclaiming, and that is worth foregrounding rather
than hiding.

## 4. Hard blockers

Ordered. Nothing else matters until these are done.

### 4.1 The demo must actually run end to end

**Status: DONE (2026-07-30).** The three-stage pipeline now completes real
requests on Gemini (`LLM_PROVIDER` selects Gemini or Anthropic; see
`demo/providers.py`). Verified in the browser: staged progress, tier-badged
evidence cards, and a streamed recommendation that cites per-row evidence and
flags tiers correctly.

The first real run paid for itself by exposing four defects that only surface
under real traffic — blank env vars overriding model defaults, page counts and
years parsed as word limits across 13 entries, field narrowing that starved
the candidate set, and tier being left to inference which produced a
self-contradiction. All fixed.

### 4.2 The repository must be public

**Status: not done** — still private. A demo paper pointing at a private
repository fails on contact. The branch merge that made this safe is already
done (`main` now carries the full 399-entry corpus rather than the old
166-entry state), so this is a switch, not a project.

### 4.3 A recorded demo video

**Status: not started**, and now unblocked (4.1 is done). Up to 5 minutes. The natural
structure follows the pipeline: paste a paper description → watch the stages
resolve → open an evidence card to show the tier badge and the actual cited
article counts → show a `Disputed` marker → show an honest blank.

The evidence cards matter here disproportionately: they are the visible proof
that the recommendation is built from checkable records rather than model
recall. That is the single most demo-able property of the whole system.

## 5. Strongly recommended, not strictly blocking

### 5.1 A small retrospective evaluation

**Status: partly done (2026-07-30).** A 4-case skill eval now exists at
`skills/journal-atlas/evals/`, run against a no-skill baseline: 18/18 vs
11/18. Its most quotable result is the JCR case — asked about a journal
absent from the corpus, the baseline produced a section headed "Who your
reviewers will actually be", while the skill declined and said so.

What it is not is an accuracy measurement. The assertions were written by
the skill's own author, one passes vacuously for the baseline, and n=4.
`fit_score.py`'s weights remain unvalidated against real submission
outcomes, which is still the larger gap.

A demo does not require an evaluation, but n=10–20 retrospective cases —
manuscripts with known submission outcomes, checking whether the ranking is
sane and whether hard-constraint eliminations were correct — would change the
paper from "here is a thing" to "here is a thing with some evidence it
behaves." The gap between a tiny evaluation and no evaluation is much larger
in a reviewer's mind than the gap between a tiny one and a medium one.

Cheapest credible version: take entries whose Rejection Fallback Chains were
hand-authored by a human with real experience, and check whether the
similarity/scoring machinery independently surfaces the same venues.

### 5.2 Decide how to present the evidence-thinness honestly

312 high-confidence scores rest on contentless justifications, and 236 of 399
entries are AI-Researched with `signal_quality` mostly at 2/5. This is
documented, baselined, and CI-guarded — but a reviewer who digs will find it.

Two ways to handle it, and the choice should be deliberate:

- **Foreground it** as part of Claim 2 — the tier system exists precisely
  because coverage was bought at the cost of depth, and the honesty machinery
  is the response to that trade-off. This is the stronger move for this venue.
- **Bury it** and risk a reviewer surfacing it as a gotcha.

The first is both more defensible and more interesting. The project's own
`SEED_DATA_QUALITY.md` already makes this argument well and can be drawn on
directly.

### 5.3 OPSEC re-check under new exposure

The worked example recurring across README and SKILL.md (12,000-word
theoretical embodied-cognition paper, $0 APC, targeting a named venue)
identifies the maintainer's own in-progress submission. This was reviewed and
accepted when the exposure was "GitHub visitors."

Single-blind review names the author regardless, so the paper itself is not
the issue. What changes is that the repository becomes linked from an
ACM-published artifact and indexed accordingly. Worth one deliberate decision
rather than inheriting the earlier one by default.

## 6. Explicitly not required for this submission

Recorded so effort does not leak into them:

- Clearing the 312 baselined lint violations
- Filling the remaining conference entries' Top Topics
- Resolving the 8 human-judgment items in `EXISTING_ENTRY_CONFLICTS.md`
- Any community-contribution volume
- The full breadth-vs-depth roadmap in `PROJECT_COMPLETION.md`

## 7. Current state, measured

For reference when writing the paper. Measured 2026-07-27 on `main`.

| Dimension | State |
|---|---|
| Corpus | 399 entries (379 journals + 20 conferences) |
| Tier distribution | 11 Tier 1 · 152 Tier 2 · 236 AI-Researched · 0 Skeleton |
| Schema conformance | 399/399 pass `validate_structure.py` |
| Spine | 166,821 ISSN-keyed journals joining OpenAlex + DOAJ + JUFO + CAS + Norwegian Register + Retraction Watch |
| Automated tests | 46, covering parsing/scoring regressions and API call shapes |
| CI | schema validation + tests + content lint + frontend typecheck on every push/PR |
| Content lint | 312 known violations, baselined; CI blocks new ones |
| Governance | Adopted; `Disputed` marker implemented and surfaced in the demo |
| Data hygiene | 12 ceased journals flagged with named successors; 2 entries corrected off wrong OpenAlex sources. Evals showed the banners matter for the deterministic scorer, not the model — a strong model already knows these cessations |
| Skill evaluation | 4 cases, with-skill vs baseline. 18/18 vs 11/18. The discriminating cases are soft-metadata ones; bibliographic facts do not discriminate |
| Demo | Built, browser-verified up to the API boundary, never run with a real key |
| Repository | Private; `main` merged and current |
