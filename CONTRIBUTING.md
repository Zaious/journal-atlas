# Contributing to Journal Atlas

Thank you for helping build a knowledge base that saves researchers from blind submissions and wasted months.

## What We Need Most

**Soft Metadata.** The unwritten rules. The stuff you only know if you've published there or reviewed there.

Examples of high-value contributions:
- "This journal desk-rejects anything without a cultural framing"
- "Reviewers here are mostly phenomenologists — expect Husserl references"
- "They say they accept autoethnography but the last 5 years show only 2 articles"
- "AI policy says 'follow publisher guidelines' but the editor told me they want explicit disclosure emails"

### Frameworks That Help You Write Soft Metadata

You don't need to invent assessments from scratch. Several existing frameworks can help you describe a journal's culture systematically:

- **Reviewer culture** — Trubble et al. (2020), *"What feedback do reviewers give when reviewing qualitative manuscripts?"* ([Birmingham meta-review](https://link.springer.com/article/10.1186/s12874-020-01005-y)) identified 30 recurring themes in reviewer reports on qualitative work. If you've reviewed for or been reviewed by a journal, these themes can structure what you observed.
- **Discourse community framing** — Pat Thomson's [Patter blog](https://patthomson.net/2023/12/04/publishing-in-top-ranked-journals/) frames journal choice as "choosing a community of researchers, writers and readers." Useful for filling in *Editorial Board Discourse Community Signals*.
- **Editor decision-making** — Achilleas Kostoulas's [How to avoid desk rejections](https://achilleaskostoulas.com/2014/02/13/how-to-avoid-desk-rejections/) gives editor-side perspective on what triggers desk rejection. Useful for filling in *Hard Blockers* and *Desk Rejection Rate*.
- **Submission ladder** — Terence Tao's [Submit to an appropriate journal](https://terrytao.wordpress.com/advice-on-writing-papers/submit-to-an-appropriate-journal/) frames journal choice as a tiered strategy. Useful for filling in *Best Suited For* / *Not Recommended For*.

Cite these in your `Evidence` columns when relevant. They give your contribution academic grounding.

## How to Contribute

### Adding a New Journal

1. Copy [`TEMPLATE.md`](TEMPLATE.md) to `references/journals/<field>/<journal-name>.md`
2. Fill in what you know. **Partial entries are welcome** — leave unknown fields blank rather than guessing
3. Open a PR

**Naming convention:**
- Lowercase kebab-case: `theory-and-psychology.md`
- Use full name, not abbreviation: `phenomenology-and-the-cognitive-sciences.md` not `pcs.md`
- Drop leading articles: `journal-of-personality.md` not `the-journal-of-personality.md`
- Ampersand → "and": `culture-and-psychology.md`

**Field directories:**
- `psychology/` — clinical, cognitive, theoretical, social
- `hci/` — human-computer interaction
- `qualitative-methods/` — methodology-focused journals
- `cognitive-science/` — cognitive science, philosophy of mind

If none fits, open an issue to discuss adding a new field directory.

### Updating an Existing Journal

1. Edit the relevant `.md` file
2. Add a row to the **Changelog** at the bottom
3. Update `Last verified` date in the header if you re-checked official sources
4. Open a PR

### Reporting Outdated Information

If you notice something wrong but don't have time to fix it, [open an issue](../../issues/new?template=update-journal.md).

## Quality Standards

### Required for All Contributions

- [ ] `Last verified` date is present and accurate
- [ ] Changelog has an entry for your change
- [ ] Factual claims cite a source (URL, official document, or "personal communication YYYY-MM")
- [ ] Soft Metadata assessments are marked as `(community estimate)` when subjective

### Sources We Trust

| Source Type | Trust Level | Example |
|-------------|-------------|---------|
| Journal's official author guidelines page | High | "Word limit: 8,000" |
| Publisher policy page (Sage, Springer, etc.) | High | "Sage AI policy tier 2" |
| OpenAlex / Scimago data | High (for metrics) | "h-index: 90" |
| Published articles in the journal | Medium-High | "3 BDSM articles 2015-2025" |
| Personal publishing experience | Medium | "Reviewer asked for cultural framing" |
| Second-hand reports | Low — mark as (unverified) | "A colleague said..." |

### What We Don't Accept

- Guesses presented as facts
- Metrics without retrieval dates
- Soft Metadata without any evidence (even "personal experience" counts as evidence — just label it)
- AI-generated entries that haven't been verified by a human with domain knowledge

## Review Process

1. **Automated check**: CI runs `scripts/validate-structure.py` to ensure template compliance
2. **Maintainer review**: A field maintainer checks factual accuracy
3. **Merge**: Once approved, your contribution is live

We aim to review PRs within 7 days. If yours is stale, ping in the PR comments.

## Maintainer Roles

| Role | Responsibility |
|------|---------------|
| **Field Maintainer** | Reviews PRs for journals in their field. Must have published in or reviewed for journals in that field. |
| **Core Maintainer** | Reviews cross-cutting changes (template, scripts, infrastructure). |

Interested in becoming a Field Maintainer? Open an issue or reach out.

## Code of Conduct

This is an academic knowledge base. We expect:
- Factual accuracy over opinion
- Respectful disagreement (if you think a Soft Metadata assessment is wrong, provide counter-evidence)
- No promotional content for or against any journal
- Sensitivity when discussing editorial biases — describe, don't judge

## License Discussion

We're evaluating license options. The goal is:
- Free for anyone to use (researchers, AI tools, institutions)
- Attribution required (credit the community)
- Contributions remain open

Current candidates: CC-BY-4.0, MIT, Apache-2.0. Input welcome via issues.
