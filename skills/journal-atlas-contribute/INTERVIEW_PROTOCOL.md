# Interview Protocol — Question Bank for Soft Metadata Extraction

> This document maps each TEMPLATE.md Soft Metadata subsection to the
> conversational questions that extract actionable data from a contributor.
>
> **Don't read all questions at once.** Pick 1-2 per turn based on what
> the user already said. Skip questions the user's previous statements
> already answered. The goal is a natural conversation, not a survey.

---

## 1. Epistemological & Political Leanings

**Opening prompt** (if user hasn't hinted at this yet):

> "When you were preparing your manuscript for [journal], did you get the
> sense it was more friendly to certain theoretical traditions or worldviews?"

**Follow-up probes**:

| If user says... | Extract into... | Follow-up |
|-----------------|-----------------|-----------|
| "very Western-centric" | Cross-cultural friendliness: Low | "Any examples? Did reviewers flag non-Western references?" |
| "they published my decolonial analysis" | Non-Western epistemology openness: High | "Did reviewers engage with it substantively, or just tolerate it?" |
| "very open-minded editorially" | Diversity topic receptiveness: High | "Open to what specifically? Race/gender/disability/sexuality...?" |
| "conservative, sticks to [tradition]" | Dominant theoretical tradition: [capture] | "Which tradition? Cognitive? Phenomenological? Critical?" |

---

## 2. Framing Requirements

> "Did you have to frame your work in a specific way to get past the editor
> or reviewers? Like, was there an expected lens?"

| If user says... | Extract into... | Follow-up |
|-----------------|-----------------|-----------|
| "had to add a cultural angle" | Mandatory framing: Yes, cultural | "Was it a desk-reject risk without the framing, or just reviewer preference?" |
| "no, very flexible" | Mandatory framing: No | "So a cognitive paper and a critical-theory paper would both be fine?" |
| "reviewers really wanted phenomenological grounding" | Mandatory framing: Yes, phenomenological | "Would a paper without phenomenological vocabulary be desk-rejected or just pushed to revise?" |

---

## 3. Methodological Preferences

> "What research methods does [journal] seem to welcome? And which ones
> would be a hard sell?"

For each method the user mentions, try to pin a 0-5 receptiveness score:

| If user says... | Score | Method field |
|-----------------|-------|-------------|
| "they love experiments" | 5 | Quantitative experimental |
| "they publish some interviews but it's not their bread and butter" | 3 | Qualitative interviews |
| "autoethnography would be a stretch" | 1-2 | Autoethnography |
| "theory papers are their core" | 5 | Theoretical / Conceptual |
| "meta-analyses are welcome" | 4 | Meta-analysis |

**Calibration question** (optional):

> "If you had to rate how receptive [journal] is to [method] on a 0-5 scale
> — 0 being 'never publishes it' and 5 being 'it's their bread and butter'
> — what would you say?"

---

## 4. Voice & Style

> "What's the writing register like? Is first-person voice okay, or is it
> strictly third-person academic?"

| If user says... | Extract into... |
|-----------------|-----------------|
| "first person is totally fine, even expected" | First-person voice acceptance: 4-5 |
| "I used 'I' occasionally and nobody flagged it" | First-person voice acceptance: 3 |
| "strictly impersonal, passive voice" | First-person voice acceptance: 0-1 |
| "formal but accessible, not too jargon-heavy" | Writing style notes: capture |
| "dense philosophical language expected" | Writing style notes: capture |

---

## Reference: venue-family reviewer patterns

For high-coverage venue families, the following adapted patterns may help calibrate questions before talking with the contributor. These are family-level defaults; per-journal experience overrides them.

| Venue family | Reviewer expectation pattern | Common desk-reject signal |
|--------------|----------------------------|--------------------------|
| **High-impact multidisciplinary** (Nature, Science, Cell, PNAS) | Broad significance over technical depth; ≥1 non-specialist reviewer; cross-disciplinary accessibility | Findings too specialized; incremental advance; inaccessible writing |
| **Cell Press family** | Mechanism focus; multiple complementary approaches; in vivo validation; figure-by-figure scrutiny | Single-method mechanism claims; descriptive without mechanism |
| **Medical** (NEJM/Lancet/JAMA/BMJ/Annals) | Clinical relevance / practice change; CONSORT/STROBE; dedicated statistical reviewer; effect-size + CI reporting | Underpowered; selective outcomes; claims exceed evidence |
| **ML conferences** (NeurIPS/ICML/ICLR) | Technical novelty; reproducibility; ablations mandatory; benchmark comparisons | Missing ablations; unclear novelty; no released code |
| **HCI conferences** (CHI/CSCW) | User impact; design implications; qualitative methods accepted; participant reporting standards | Generic "we built a tool" without user study; small-N quant claims |

*Reference adapted from ScienceClaw venue-templates `reviewer_expectations.md` (MIT). Use these only as priors — always verify against the contributor's first-hand experience.*

---

## 5. Reviewer Pool Characteristics

> "What was your impression of the reviewers? What tradition did they seem
> to come from?"

This is the richest question — let the user talk, then extract:

| Signal | Extract into... |
|--------|-----------------|
| "reviewers were clearly from [tradition]" | Dominant tradition: [capture] |
| "one reviewer didn't understand my qualitative methods" | Reviewer competence variance: Medium-High |
| "reviewer asked why I didn't have a control group" | Quantitative mindset bias: Yes |
| "all three reviewers got exactly what I was doing" | Reviewer competence variance: Low (uniform) |
| "I could tell from the feedback they were [university/country]-based" | Discourse community signals |

**Birmingham 2020 calibration** (optional, for advanced contributors):

> "Did you notice any of these patterns in the reviewer feedback?
> — Requesting larger/representative samples on qualitative work
> — Asking for statistical power analysis on a theoretical paper
> — Suggesting you reframe your work through a different paradigm"

These map to the Quantitative Mindset Bias field (from Birmingham 2020
meta-review of qualitative manuscript reviewer feedback).

---

## 6. Sensitive Topics

> "Were there any topic sensitivities you noticed? Like, would a paper on
> [BDSM / drug use / suicide / political extremism / etc.] fly here?"

For each topic:

| If user says... | Extract into... |
|-----------------|-----------------|
| "they've published on [topic] before, it's fine" | Receptiveness: Medium-High + evidence |
| "I wouldn't touch that with this journal" | Receptiveness: Low |
| "never tested, no idea" | Receptiveness: Untested |
| "reviewers would push back but editor would allow it" | Receptiveness: Medium |

**Evidence probe**: "Do you know of any specific papers on [topic] published
there? Even roughly — like 'a few in the last 5 years' helps."

---

## 7. Practical Concerns

> "A few quick logistics about [journal] — any of these come up for you?"

| Question | Field |
|----------|-------|
| "Did they require IRB approval for your paper?" | IRB requirement strictness |
| "Is single-authored work common there, or is it unusual?" | Single-author acceptance |
| "Were you affiliated with a university, or independent? Any friction?" | Independent scholar friendliness |
| "Did they ask you to share your raw data?" | Data transparency requirement |

---

## 8. Strategic Notes (post-Soft-Metadata)

After the seven Soft Metadata dimensions, shift to strategy:

> "Now some bigger-picture questions about submitting to [journal]."

| Question | Field |
|----------|-------|
| "Is there anything that would get you desk-rejected outright?" | Hard Blockers |
| "How much effort would it take to adapt a paper that doesn't perfectly fit?" | Soft Tax |
| "What kind of paper really thrives at this journal?" | Best Suited For |
| "What kind of paper should absolutely not be sent here?" | Not Recommended For |
| "If [journal] rejected you, where would you try next — and why?" | Rejection Fallback Chain |

---

## When to stop

The interview is complete when:
- All 7 Soft Metadata subsections have at least a partial value
- Strategic Notes has at least Hard Blockers + Best/Not Recommended For
- The user shows signs of fatigue ("I think that's all I know")

At that point, generate the patch and guide the user to PR submission.
Don't push for perfection — partial evidence is better than no evidence.
Future contributors can fill gaps.
