# Use Case Template

Copy this file and rename it to `<descriptive-slug>.md` (e.g. `embodied-cognition-cross-disciplinary-submission.md`). Fill in the sections below.

---

# {Case Title}

> **Submitted by**: @your-github-handle
> **Date**: YYYY-MM-DD
> **Field**: psychology / hci / qualitative-methods / [other]
> **Anonymization status**: [Real paper, attributes anonymized | Fictional but realistic | Composite of multiple real sessions]

## Paper attributes

The paper that drives this session. Use bullet form so AI agents can extract attributes cleanly.

- **Topic / keywords**:
- **Methodology**:
- **Word count**:
- **APC budget**:
- **OA required**: Yes / No
- **AI usage**: Yes / No (and whether disclosed)
- **IRB status**:
- **Sensitive content**:
- **Other constraints**: (timeline, preprint intent, OPSEC, etc.)

## What this case demonstrates

A short bullet list of skill behaviors this case exercises. Match these to the six E2E scenarios when possible:

- [ ] **Discovery** — does the skill activate without prompting?
- [ ] **Soft Metadata recommendation** — top-N with evidence citations
- [ ] **Constraint change cascade** — what shifts when (e.g.) OA requirement is added
- [ ] **Rejection-fallback walk** — what happens after a desk reject
- [ ] **Out-of-coverage honesty** — does the AI refuse to hallucinate
- [ ] **Comparison verdict** — head-to-head selection between specific journals

## Session transcript

Multi-turn conversation in the order it happened. Use Q/A format with brief context labels.

### Q1 — Initial query

> **Author**: {what the user said}

> **AI**: {the AI's full response — preserve formatting, ranked lists, eliminations, evidence citations}

### Q2 — Follow-up / constraint change

> **Author**: {next message}

> **AI**: {response}

*(continue for all turns)*

## Key takeaways

Three to five bullets summarizing the strategic insights this session produced. These are what readers will quote.

- {insight 1}
- {insight 2}
- {insight 3}

## Skill behavior notes

Optional. Anything notable about how the skill performed:

- Where it surprised you (positively or negatively)
- Where you had to nudge it
- Where it gave reasoning that wasn't explicitly in `SKILL.md` (good — shows emergent strategic synthesis)
- Where it deviated from `SKILL.md` (concerning — file an issue)

## Anonymization notes

If you anonymized a real paper, briefly describe what was changed:

- {original attribute} → {anonymized equivalent} (rationale)

This helps reviewers verify that the strategic logic still holds even with the substitution. Do not reveal anything that would reverse the anonymization.

## License

By submitting this use case you agree to license it under CC BY-NC-SA 4.0 (the same license as the rest of Journal Atlas content). See [LICENSE](../LICENSE).
