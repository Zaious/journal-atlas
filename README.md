# Journal Atlas

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/Content-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE-CODE)
[![Schema](https://img.shields.io/badge/Schema-v1.2-green.svg)](skills/journal-atlas/TEMPLATE.md)
[![Status](https://img.shields.io/badge/Status-Pre--release%20(seeding)-orange.svg)](#status)

**A community-maintained, AI-native knowledge base of academic journal fit metadata.**

> **Status (2026-05): Pre-release.** Schema is stable at v1.2; we are currently
> seeding the initial journal entries. Expect limited coverage until first
> contributors land. Contributions, feedback, and journal nominations all welcome.
>
> 22 seed entries across psychology, HCI, and qualitative methods are split into
> Tier 1 (14 evidence-backed) and Tier 2 (11 community-estimate) — see
> [SEED_DATA_QUALITY.md](SEED_DATA_QUALITY.md) for the methodology and how to
> help upgrade Tier 2 entries to Tier 1.

Journal Atlas fills a gap that Impact Factor and Scimago don't cover: **soft metadata** — the unwritten rules about reviewer culture, framing expectations, sensitive topic tolerance, AI policy nuances, and methodological preferences that researchers currently learn only through experience or word of mouth.

## What's Inside

Each journal entry is a structured Markdown file covering 7 dimensions:

| Dimension | What it tells you |
|-----------|-------------------|
| **Identity** | Name, publisher, ISSN, editorial board location |
| **Metrics** | IF, h-index, CiteScore, acceptance rate, review timeline |
| **Policies** | AI policy, preprint rules, OA/APC, embargo periods |
| **Format** | Word limits, article types, reference limits |
| **Subject Density** | What topics this journal actually publishes (OpenAlex data) |
| **Soft Metadata** | Reviewer culture, framing requirements, sensitive topic tolerance, epistemological leanings |
| **Strategic Notes** | Hard blockers, adaptation effort, best/worst fit |

**Soft Metadata is the core differentiator.** Everything else you can find on Scimago. The information in Soft Metadata is what saves you a rejection and 6 months.

## Coverage

**Any academic discipline is welcome.** The template and workflow are field-agnostic.

Initial seed coverage includes psychology (including cross-disciplinary phenomenology / cognitive-science venues), HCI, and qualitative methodology — but we actively welcome contributions from all fields. If your discipline isn't represented yet, you can be the one to start it.

---

## How to Use

### Option 1: Claude Code via plugin marketplace (recommended)

In a Claude Code session (main session, not a worktree sub-session, which doesn't expose `/plugin`):

```
/plugin marketplace add Zaious/journal-atlas
/plugin install journal-atlas@journal-atlas
```

Then restart Claude Code. The skill is auto-discovered when relevant.

Ask naturally:

> "I have a 12,000-word theoretical paper on embodied cognition.
> No IRB, no APC budget, I used AI for writing assistance, no immediate
> OA needed. Which journals fit?"

### Option 1b: Claude Code via manual `git clone` (fallback if `/plugin` unavailable)

If you're in a worktree session or otherwise don't have `/plugin` available, install the skill directly:

```bash
# Windows PowerShell
git clone https://github.com/Zaious/journal-atlas.git $HOME\.claude\skills\journal-atlas

# macOS / Linux
git clone https://github.com/Zaious/journal-atlas.git ~/.claude/skills/journal-atlas
```

Then restart Claude Code (or start a new session). The skill becomes available the same way as Option 1.

### Option 2: Claude Desktop

1. Clone this repo: `git clone https://github.com/Zaious/journal-atlas.git`
2. Create a new Project in Claude Desktop
3. Upload the `.md` files from `skills/journal-atlas/references/journals/` as Project Knowledge
4. Copy the contents of `skills/journal-atlas/SKILL.md` into Project Instructions

### Option 3: ChatGPT (GPT Builder)

1. Clone this repo
2. From the repo root, run `cd skills/journal-atlas && python scripts/bundle_for_upload.py` to merge journal files into uploadable chunks
3. Upload the output files to your GPT's Knowledge section
4. Copy the contents of `skills/journal-atlas/SKILL.md` into your GPT's Instructions

### Option 4: Just read it

Browse [`skills/journal-atlas/references/journals/`](skills/journal-atlas/references/journals/) on GitHub. Every journal is a readable Markdown page. No AI required.

### Want to see Journal Atlas in action first?

[**`use-cases/`**](use-cases/) contains full multi-turn session transcripts showing what the skill produces with real(istic) papers — including how constraint changes cascade, how the rejection-fallback chain gets walked, and how the skill admits when it can't help. The [Self-state Dynamics use case](use-cases/self-state-altered-states-autoethnography.md) covers all six end-to-end scenarios.

---

## Automation (skills/journal-atlas/scripts/)

| Script | Purpose | Status |
|--------|---------|--------|
| `import_openalex.py` | Auto-populate a new journal entry from OpenAlex API (Identity / Metrics / Subject Density / OA fields). Uses pyalex (MIT). | ✅ Available |
| `validate_structure.py` | Check that journal `.md` files match the template schema. Runs on every PR. | ✅ Available |
| `fit_score.py` | Compute a numerical fit score given your paper's attributes vs. each journal. | ⚠️ v0.1 — needs backtest validation |
| `bundle_for_upload.py` | Merge journal files into larger chunks for platforms with file count limits (e.g. ChatGPT). | ✅ Available |
| `update_metrics.py` | Fetch latest IF / h-index / CiteScore from OpenAlex API. Proposes a PR draft — never auto-writes. | ✅ Available |
| `topic_trend_scan.py` | Scan a journal's recent publications to detect topic trend shifts. | ✅ Available |

Run scripts from the skill root: `cd skills/journal-atlas && python scripts/<name>.py`.
See [skills/journal-atlas/scripts/README.md](skills/journal-atlas/scripts/README.md) for setup and usage examples.

---

## Contributing

We need your journal expertise. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

**Quick version:**
1. Copy [`skills/journal-atlas/TEMPLATE.md`](skills/journal-atlas/TEMPLATE.md)
2. Fill in what you know (partial entries welcome — others can fill gaps)
3. Open a PR

The most valuable contributions are **Soft Metadata** — the stuff that isn't in any database. If you've published in a journal and know its unwritten rules, that knowledge helps every researcher who comes after you.

---

## What This Is NOT

- **Not a journal ranking.** We provide metadata; you decide what matters.
- **Not a predatory journal blacklist.** Use [Cabells](https://www2.cabells.com/) for that.
- **Not a replacement for Scimago/JCR.** We aggregate their quantitative metrics as a convenience. Our value is the soft metadata they don't have.

---

## Lineage

Journal Atlas stands on a 20-year tradition of journal recommenders. We acknowledge the work that came before, and we situate ourselves within it rather than against it.

| Year | System | Approach | Status |
|------|--------|----------|--------|
| 2007 | [JANE](https://jane.biosemantics.org/) (Schuemie & Kors, *Bioinformatics*) | PubMed text similarity | Operational, biomedical-only |
| 2007 | [eTBLAST](https://pubmed.ncbi.nlm.nih.gov/17452348/) (Errami et al., *Nucleic Acids Research*) | Three-in-one: reviewer + journal + duplicate detection | Server offline |
| 2015 | [Elsevier Journal Finder](https://journalfinder.elsevier.com/) (Kang et al., *RecSys*) | NLP + Okapi BM25 over Elsevier's catalog | Operational, vendor-locked |
| 2018 | [Maglet](https://ieeexplore.ieee.org/document/8660987/) (Mohtaj & Tavakkoli, *IST*) | Persian-language regional recommender | Academic publication, no public deployment |
| 2022 | [Open Journal Matcher](https://github.com/MarkEEaton/open-journal-matcher) (Eaton, CUNY) | spaCy word vectors over DOAJ; pioneered "[pervious technology](https://academicworks.cuny.edu/kb_pubs/261)" framing | Service offline 2022/07 (single-maintainer + grant ended) |
| 2021– | [B!SON](https://service.tib.eu/bison/) (TIB + SLUB Dresden, BMBF-funded) | Elasticsearch + BM25 + OpenCitations bibliographic coupling + ML semantic | **Currently the state of the art** for OA recommendation |

### Honoring Open Journal Matcher (OJM)

This project owes particular intellectual debt to **Mark E. Eaton's Open Journal Matcher** *(2020-2022)*. In July 2022, Eaton took OJM offline, writing:

> *"My hope is that someone will pick up where I left off, and build something similar, or perhaps adapt the code for the OJM. There's a place for a tool like the OJM; and we shouldn't leave this space entirely to the big journal publishing companies."*
> — Eaton (2022), [The last days of the Open Journal Matcher](https://kingsboroughlibtech.commons.gc.cuny.edu/2022/07/29/the-last-days-of-the-open-journal-matcher/)

**Journal Atlas is one response to that invitation.**

Eaton's companion paper [*On the ethics of working with library technology*](https://academicworks.cuny.edu/kb_pubs/261) introduced the concept of **"pervious technology"** — tools that users can reach into, tinker with, and adapt, in contrast to impervious black-box systems. Eaton argued that pervious tools, combined with diverse perspectives, are how ethical problems in technology become apparent.

Journal Atlas extends this idea further: where OJM was pervious *at the code layer* (Flask + spaCy, open source on GitHub), Journal Atlas is pervious *at the data layer* — every journal entry is a plain-text Markdown file that any researcher can read, edit, and discuss. The knowledge itself is the product, not a service that can be turned off when one maintainer burns out.

### What Journal Atlas Adds to the Lineage

Every system above answers the same question — *given an abstract, which journals match?* — using metric similarity over publication data. None of them capture the knowledge a senior colleague would share over coffee:

- *"That journal's reviewer pool expects Heidegger literacy."*
- *"This one desk-rejects anything without IRB, even theoretical work."*
- *"They say single-blind, but the editor leaks identity to friendly reviewers."*
- *"First-person voice gets you flagged here, but it's expected next door."*

Three design choices distinguish Journal Atlas from the lineage:

1. **Per-journal knowledge base, not per-query app.** Predecessors compute fresh similarity scores at query time; Journal Atlas maintains persistent, citable journal profiles — soft metadata that algorithms cannot extract from publication data and that improves monotonically as the community contributes. This information requires human community knowledge, and it requires durability beyond any single maintainer's commitment.

2. **Markdown + Git, not service infrastructure.** Predecessors that depended on cloud services (OJM) or grant funding cycles (B!SON's BMBF period ended 2023/01) face structural maintenance risks. Journal Atlas has zero hosting cost and zero single point of failure. Anyone can fork. We learned this lesson from OJM's offline notice — *single maintainers do not survive without community*. Journal Atlas is community-first by design.

3. **Designed for the agent era, not the search-bar era.** Previous systems are web applications: users open a browser, submit a query, read results. Journal Atlas is structured as a [Claude Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) — the machine-readable skill convention now adopted across Claude Desktop, Claude Code, and increasingly ChatGPT GPTs and other AI agent platforms. When an autonomous research agent plans a submission strategy, it doesn't visit a website; it loads `SKILL.md`, consults the relevant journal files, and reasons over them. By packaging journal knowledge in the lingua franca of contemporary AI agents, Journal Atlas joins the research-pipeline ecosystem natively — installable in one command, consumable by any tool that speaks the skill convention, and durable across whatever interface comes next.

We are complementary to B!SON, not competing — use B!SON to discover candidate OA journals, then read their Journal Atlas pages to understand what submission to each *actually involves*.

---

## License

Journal Atlas uses a **dual-license** model:

- **Content** (Markdown files, journal entries, documentation, templates) — [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/) (CC BY-NC-SA 4.0)
- **Code** (everything under `skills/journal-atlas/scripts/`) — [MIT License](LICENSE-CODE)

**Attribution is required for all uses, commercial or non-commercial.** See [CITATION.cff](CITATION.cff) for the preferred citation format and [AUTHORS.md](AUTHORS.md) for the full credits.

**Commercial use** — non-commercial use is free under CC BY-NC-SA 4.0. For commercial licensing (integration into paid products, redistribution within commercial services, fee-based research-as-a-service offerings, or similar), please contact **Meng-Han Lee at zaious.design@gmail.com** to discuss terms. We welcome conversations about partnerships and sustainable ecosystem integration.

Full license details: [LICENSE](LICENSE) | [LICENSE-CODE](LICENSE-CODE)

---

## Acknowledgments

**Founding author**: Meng-Han Lee ([Zaious](https://zaious.dev/)), Independent HCI Researcher and AI Agent Architect. Originator of the [Agentic Social Affordance Framework (ASAF)](https://doi.org/10.5281/zenodo.19652278).

**AI Agent Team**: ChronicleCore — a multi-agent system collaborating under Zaious's direction. Architect: Cardinal (樞機師 / Yui). Other agents will be credited as they contribute. See [AUTHORS.md](AUTHORS.md) for the full team and contributor roster.

Built by researchers, for researchers. Maintained by the community.

Initial seed data drawn from journal evaluations conducted during active manuscript submission processes in psychology, HCI, and qualitative methodology (2025-2026).

See [INSPIRATION.md](INSPIRATION.md) for a full list of tools, papers, and concepts that influenced this project's design.
