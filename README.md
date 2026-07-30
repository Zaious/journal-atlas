# Journal Atlas

> 🌐 **Languages**: English | [繁體中文](README.zh-Hant.md)

[![License: CC BY-SA 4.0](https://img.shields.io/badge/Content-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE-CODE)
[![Schema](https://img.shields.io/badge/Schema-v1.3-green.svg)](skills/journal-atlas/TEMPLATE.md)
[![Status](https://img.shields.io/badge/Status-Pre--release%20(seeding)-orange.svg)](#tier-system)

**A community-maintained, AI-native knowledge base of academic journal fit metadata.**

Journal Atlas captures what bibliometric tools like Impact Factor and Scimago don't: the **soft metadata** of academic journals — reviewer culture, framing expectations, sensitive-topic tolerance, AI policy nuances, methodological preferences, and rejection-fallback strategies — encoded as a Claude Agent Skill installable across Claude Code, Claude Desktop, and ChatGPT.

> **Status (2026-07): Pre-release.** 399 seed entries — 379 journals across 9 field
> directories (including new `philosophy/`) + 20 conferences across 4 sub-domains
> (HCI / ML / NLP / Data Mining). Quality breakdown: **11 Tier 1** (evidence-backed) ·
> **152 Tier 2** (community estimate) · **236 AI-Researched** (per-journal AI research
> with cited `signal_quality`, v2 coverage-first pivot) · **0 Skeleton**.
> Schema **v1.3** — adds `Venue type` field + `Conference Specifics` section.
> Plus 8 Society Registry entries (`references/societies/`, schema `society-v1`)
> covering ACM SIGCHI / SIGACCESS / ACL / APS / APA / Cell Press / Nature Portfolio / PLOS.
> See [Tier System](#tier-system) and [SEED_DATA_QUALITY.md](SEED_DATA_QUALITY.md).

---

## Table of Contents

- [Quick Start](#quick-start)
- [Installation](#installation)
- [Skills Overview](#skills-overview)
- [Slash Commands](#slash-commands)
- [Workflows (with examples)](#workflows)
- [Tier System](#tier-system)
- [Automation Scripts](#automation-scripts)
- [Try It Without Installing](#try-it-without-installing)
- [Contributing](#contributing)
- [Use Cases](#use-cases)
- [What This Is NOT](#what-this-is-not)
- [Adjacent Tools](#adjacent-tools)
- [Lineage](#lineage)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Quick Start

```bash
# 1. Install (Claude Code main session)
/plugin marketplace add Zaious/journal-atlas
/plugin install journal-atlas@journal-atlas
# Restart Claude Code

# 2. Ask anything
/ja-recommend
> "I have a 12,000-word theoretical paper on embodied cognition.
>  No IRB, no APC budget. Which journals fit?"
```

You'll get a ranked recommendation with evidence citations from the knowledge base, hard-constraint elimination, rejection-fallback chains, and strategic notes.

---

## Installation

### Option 1: Claude Code via plugin marketplace (recommended)

In a Claude Code **main session** (not a worktree sub-session — those don't expose `/plugin`):

```
/plugin marketplace add Zaious/journal-atlas
/plugin install journal-atlas@journal-atlas
```

Restart Claude Code. Both skills (`journal-atlas` + `journal-atlas-contribute`) and all 8 slash commands become available.

### Option 1b: Claude Code via manual `git clone` (fallback)

If you're in a worktree session or otherwise don't have `/plugin`:

```bash
# Windows PowerShell
git clone https://github.com/Zaious/journal-atlas.git $HOME\.claude\plugins\journal-atlas

# macOS / Linux
git clone https://github.com/Zaious/journal-atlas.git ~/.claude/plugins/journal-atlas
```

Restart Claude Code. The plugin (skills + commands) becomes available.

### Option 2: Claude Desktop

1. Clone this repo: `git clone https://github.com/Zaious/journal-atlas.git`
2. Create a new Project in Claude Desktop
3. Upload the `.md` files from `skills/journal-atlas/references/journals/` as Project Knowledge
4. Copy the contents of `skills/journal-atlas/SKILL.md` into Project Instructions
5. (Optional) Repeat with `skills/journal-atlas-contribute/SKILL.md` if you want the contribution workflow

### Option 3: ChatGPT (GPT Builder)

1. Clone this repo
2. From the repo root, run `cd skills/journal-atlas && python scripts/bundle_for_upload.py` — merges journal files into bundles within ChatGPT's 20-file limit
3. Upload the bundles from `dist/` to your GPT's Knowledge section
4. Copy the contents of `skills/journal-atlas/SKILL.md` into your GPT's Instructions

### Option 4: Just browse the knowledge base

Browse [`skills/journal-atlas/references/journals/`](skills/journal-atlas/references/journals/) on GitHub. Every journal is a readable Markdown page. No AI required.

---

## Skills Overview

The plugin contains **two skills**, each addressing a different workflow:

### `journal-atlas` — The Advisor

Use when you have a paper and need decisions: recommendations, comparisons, rejection recovery, structured queries, lateral discovery.

**Capabilities**:
- Read the journal knowledge base
- Apply hard constraints (word limit, APC budget, AI policy, IRB, OA requirement)
- Rank candidates by soft fit across 6 dimensions
- Walk Rejection Fallback Chains
- Present recommendations with cited evidence and Tier-aware confidence flags

**Entry-count-aware design** scales from current 399 entries and beyond:
- ≤20 entries: direct read
- 21–50: `scripts/fit_score.py` pre-ranking
- 50+: mandatory pre-ranking; AI reads top 10–15
- 200+: `scripts/query_journals.py` field-filter first (now the default path at 399)

### `journal-atlas-contribute` — The Contributor

Use when you have experience to share: validating an existing entry, contributing a new journal, generating a PR-ready patch.

**Two modes**:

| Mode | When | What happens |
|------|------|--------------|
| **Mode B — Validate & Augment** *(preferred)* | Entry exists for the journal you mention | AI reads the existing entry, quotes claims back to you one at a time, captures your confirmations / corrections / additions, generates a Markdown patch with evidence-source upgrades (e.g. `(community estimate)` → `(personal experience 2024)`). Highest leverage for Tier 2 → Tier 1 promotion. |
| **Mode A — Cold Contribute** | No entry exists | AI offers OpenAlex-based scaffold, then walks through a 7-section structured interview filling Soft Metadata + Strategic Notes. |

**Output persistence is mandatory** — patches are written to `dist/contributed_<slug>.md` or `dist/patch_<slug>_<date>.md` for portable PR submission.

---

## Slash Commands

All commands prefixed `ja-` to avoid namespace conflicts. `$ARGUMENTS` passthrough lets you invoke directly with details.

### Advisor commands (route to `journal-atlas`)

#### `/ja-recommend`

Full 6-step recommendation workflow. Asks for your paper attributes if not provided.

**Example**:
```
/ja-recommend
> "12,000-word theoretical paper on embodied cognition. No IRB. $0 APC budget.
>  AI-assisted writing (will disclose). No immediate OA needed."
```

**You get back**: top 3 ranked recommendations with `Why it fits` evidence quotes, `Watch out for` risks, `Key stats`, `Cost` (subscription/OA paths), `If rejected, try next` fallback chain, and a `Journals Considered but Eliminated` transparency table.

#### `/ja-compare`

Head-to-head comparison of 2+ named journals.

**Example**:
```
/ja-compare
> "PCS vs RGP vs T&P — for a 12K theoretical paper, AI-disclosed,
>  immediate OA required, $0 budget"
```

**You get back**: a per-dimension table (Topic / Methodology / AI policy / Word limit / APC / Embargo / Reviewer culture / Sensitive topics) with explicit verdict per journal.

#### `/ja-fallback`

Rejection recovery — walks the Rejection Fallback Chain for a journal that rejected you.

**Example**:
```
/ja-fallback
> "PCS rejected me — reviewer said framing wasn't phenomenological enough.
>  Where should I try next?"
```

**You get back**: the journal's official Fallback Chain, filtered by your rejection reason if provided, plus a "pivot strategy" for adapting your paper to the next target.

#### `/ja-query`

Structured boolean filter — runs `scripts/query_journals.py` and presents the table.

**Example queries**:
```
/ja-query → "Show all Q1 psychology journals without AI permission gates"
/ja-query → "List Sage journals with zero embargo"
/ja-query → "Find journals accepting autoethnography at 3/5 or higher"
/ja-query → "Show me HCI journals sorted by h-index, top 10"
```

**You get back**: a filtered table with the specific data points that match. No AI reasoning over individual journals — pure deterministic filtering, scales to thousands of entries.

#### `/ja-similar`

Find journals algorithmically similar to a target — broader than the curated Rejection Fallback Chain.

**Example**:
```
/ja-similar → "What journals are most like PCS?"
/ja-similar → "Show me 10 closest to Qualitative Inquiry"
```

**You get back**: ranked similar journals with per-dimension contribution breakdown (topic Jaccard, methodology cosine, publisher match, OA model, h-index proximity, word-limit proximity, AI policy, embargo). Often surfaces lateral candidates the human-curated chain misses.

#### `/ja-related`

Find papers within a target journal matching your keywords — for cover-letter prep ("we engage with their recent X, Y, Z").

**Example**:
```
/ja-related → "Recent embodied-cognition papers in PCS, last 5 years"
/ja-related → "Self-state autoethnography papers in QRP, top 3"
```

**You get back**: ranked papers (title, authors, year, citation count, DOI) scored by keyword match + recency + citations. Markdown format ready to paste into a cover letter.

### Contributor commands (route to `journal-atlas-contribute`)

#### `/ja-contribute`

Cold Contribute mode — propose a new journal entry from scratch.

**Example**:
```
/ja-contribute
> "I want to add an entry for Behavioral and Brain Sciences. I've published there."
```

**Flow**: AI offers OpenAlex scaffold → structured interview across 7 Soft Metadata sub-sections (Epistemological Leanings / Framing / Methodological Preferences / Voice & Style / Reviewer Pool / Sensitive Topics / Practical Concerns) + Strategic Notes → generates full TEMPLATE-conformant entry → writes to `dist/contributed_<slug>.md` → guides you through PR submission.

#### `/ja-validate`

Validate & Augment mode — improve an existing entry from your experience.

**Example**:
```
/ja-validate
> "I submitted to PCS last year. Our entry's Reviewer Pool description —
>  is it accurate?"
```

**Flow**: AI reads PCS entry → quotes the Reviewer Pool claim → asks you to confirm/correct/expand → continues through other Soft Metadata sections relevant to your experience → generates a Markdown patch → writes to `dist/patch_pcs_2026-05-16.md` → guides you through PR submission.

**This is the recommended contribution path** — most efficient way to upgrade Tier 2 entries to Tier 1.

---

## Workflows

End-to-end examples. Each shows the conversation, what the skill does internally, and the typical output.

### Workflow 1: Find a journal for your paper

**Scenario**: You have a paper, you need a target journal.

```
> /ja-recommend
< What's your paper about? Share: topic, methodology, word count, APC budget,
< AI usage, IRB status, sensitive content, OA requirement, timeline.

> 12,000-word theoretical paper on embodied cognition.
> No IRB (theoretical only). $0 APC budget. AI-assisted writing (will disclose).
> No immediate OA needed. Sensitive content: ritualized altered states.

< [AI reads psychology/, cognitive-science/, hci/ entries; filters by hard
<  constraints; ranks remaining by 6-dimension soft fit; walks fallback chain]

< 🥇 Phenomenology and the Cognitive Sciences
<   Why it fits: 205 articles on embodied/self-state cognition 2020-2025...
<   Cost: $0 via subscription / $3,190 via OA
<   If rejected, try next: Theory & Psychology → Review of General Psychology
<                         → New Ideas in Psychology
< 🥈 ...
```

### Workflow 2: Compare specific journals

**Scenario**: You're choosing between 2–3 journals.

```
> /ja-compare PCS vs RGP vs T&P for a 12K theoretical paper with AI use disclosed,
> $0 APC, immediate OA required

< [Per-dimension table generated; each cell quotes specific TEMPLATE data]
< Verdict: RGP — sole survivor of all hard constraints (Sage zero embargo
< grants immediate OA at $0; word limit 15K accommodates 12K; AI policy
< disclosure-based; T&P blocked by AI permission gate + 10K word limit;
< PCS blocked by 12-month Springer embargo destroying the immediate-OA need)
```

### Workflow 3: Rejection recovery

**Scenario**: A reviewer rejected you. What's next?

```
> /ja-fallback PCS rejected — reviewer 2 said not phenomenological enough

< [AI reads PCS's Rejection Fallback Chain section; filters by rejection reason]
< Hard-blocked official fallbacks:
<   Theory & Psychology: blocked by AI gate + 10K word limit
<   New Ideas in Psychology: blocked by 7.5K word ceiling + 24-month embargo
<
< 🏆 Sole survivor: Review of General Psychology
<   Why it works: Sage zero-embargo grants immediate OA at $0; 15K word room;
<   doesn't require phenomenology. Pivot strategy: drop continental philosophy
<   vocabulary, repackage altered-state autoethnography as "extreme theoretical
<   case study illuminating self-state mechanisms in general psychology".
```

### Workflow 4: Structured query (filter by criteria)

**Scenario**: You want a filtered list, not a recommendation.

```
> /ja-query Show all Q1 psychology journals with zero embargo and no AI gate

< [Runs scripts/query_journals.py with --field psychology --quartile Q1
<  --zero-embargo --no-ai-permission-gate]
<
< 6 of 163 entries match:
< | Journal | h-index | OA model | Word limit |
< |---------|---------|----------|------------|
< | Review of General Psychology | 158 | hybrid | 15,000 |
< | Culture & Psychology | 75 | hybrid | 12,000 |
< | ...
```

### Workflow 5: Find similar journals (lateral discovery)

**Scenario**: You're exploring; the curated fallback chain doesn't help.

```
> /ja-similar What's most like PCS?

< Most similar (algorithmic, 8-dimension weighted):
< 1. AI & Society (0.508) — Springer + cognitive science cross-disciplinary
<    overlap; 90% h-index proximity. NOT in PCS's curated fallback chain,
<    surfaces as a lateral candidate.
< 2. Culture & Psychology (0.441) — methodology cosine 0.97...
< ...
```

### Workflow 6: Cover-letter preparation

**Scenario**: You've chosen a journal; you want to find papers to engage with.

```
> /ja-related PCS embodied cognition self-state 4E, last 5 years

< [Queries OpenAlex Works API filtered by PCS, scored by keyword + recency
<  + citations]
< Top 3:
< 1. "The exceptionality of enactivism within 4E cognition" (2026)
<    DOI: 10.1007/s11097-025-10131-1
< 2. "What is 4E cognitive science?" (2025) - 6 citations
< 3. ...

# Paste markdown into your cover letter draft.
```

### Workflow 7: Contribute your submission experience

**Scenario**: You've published in (or been rejected by) a journal. Your experience is evidence.

```
> /ja-validate I submitted to PCS last year. Want to share what I learned.

< Reading the PCS entry... Our entry says "reviewer pool drawn primarily from
< phenomenology and 4E-cognition communities; expect deep literacy in Husserl,
< Merleau-Ponty, Gallagher, Zahavi". Does that match what you saw?

> Reviewer 2 was clearly Husserl-focused; reviewer 1 was more from predictive
> processing tradition. Reviewer 3 was a methodologist who wanted clearer
> phenomenological-method justification.

< Capturing as: "Reviewer mix observed 2024: phenomenological-tradition focus
< (Husserl + predictive processing + phenomenological method)". This is
< first-hand experience evidence — upgrades the entry from community-estimate
< to personal-experience. Move to next claim?

[... continues through other Soft Metadata claims ...]

< Patch written to dist/patch_phenomenology-and-the-cognitive-sciences_2026-05-16.md
< Open this file, copy the content, and paste into a new PR at
< https://github.com/Zaious/journal-atlas. Need help with the PR mechanics?
```

---

## Tier System

Each entry has two orthogonal axes:

**Evidence Quality** (`Tier 1` ↔ `Tier 2`) — how trustworthy are the Soft Metadata claims?

**Completeness** (`Skeleton` ↔ filled) — has Soft Metadata been written at all?

Lifecycle:

```
Skeleton ──[Soft Metadata written from community knowledge]──► Tier 2
   (no Tier yet, > [!NOTE] banner)                            (> [!WARNING] banner)
                                                                     │
                                              [evidence accumulates: article counts,
                                               source URLs, first-hand experience]
                                                                     ▼
                                                                  Tier 1
                                                              (no banner)
```

Current distribution: **11 Tier 1 · 152 Tier 2 · 236 AI-Researched · 0 Skeleton = 399 total** (379 journals + 20 conferences).

Separately from tier, 14 entries carry a **publication-status banner**: 12 verified as ceased or renamed (each naming its successor, so a rejected manuscript has somewhere to go) and 2 flagged dormant where no issue could be confirmed for over a decade but no closure notice exists either. Recommending a venue that cannot accept submissions wastes the one thing an author cannot get back, so these are marked rather than silently ranked. AI-Researched is a third evidence basis introduced by the v2 coverage-first pivot — see [SEED_DATA_QUALITY.md](SEED_DATA_QUALITY.md#a-third-evidence-basis-ai-researched-2026-07) for what it means.

Full methodology + upgrade workflow in [SEED_DATA_QUALITY.md](SEED_DATA_QUALITY.md).

### Think a claim about your journal is wrong?

Soft Metadata makes subjective claims — reviewer culture, framing
expectations, political leanings — about real, named journals. If one is
inaccurate, there is a formal way to get it corrected: open a
[Dispute a Claim](.github/ISSUE_TEMPLATE/dispute-claim.md) issue. Anyone can
file one, editors and readers alike, and disputes are judged on the evidence
offered rather than on who files them. While a dispute is open the entry
carries a `Disputed` marker naming the contested field, so the claim is never
presented as confidently as an undisputed one.

Full policy — scope, resolution outcomes, response-time commitment — in
[docs/GOVERNANCE.md](docs/GOVERNANCE.md).

---

## Automation Scripts

13 scripts in `skills/journal-atlas/scripts/` plus 10 pipeline scripts in `scripts/spine/` — all Python 3.10+, MIT-licensed. Run from the skill root: `cd skills/journal-atlas && python scripts/<name>.py`.

Everything in the main table is standard-library only. The `spine/` pipeline scripts need `pyalex` and network access, and are for corpus maintenance rather than day-to-day use.

| Script | Purpose | Typical use |
|--------|---------|-------------|
| `query_journals.py` | Structured boolean filter (publisher, OA model, h-index, quartile, AI policy, embargo, methodology) | `--field psychology --quartile Q1 --no-ai-permission-gate` |
| `fit_score.py` | Weighted soft-fit scoring + hard constraint elimination | `--topics "embodied cognition" --methodology theoretical --word-count 12000` |
| `similar_journals.py` | 8-dimension weighted similarity to a target | `--target phenomenology-and-the-cognitive-sciences --top-n 5` |
| `related_papers.py` | OpenAlex Works API search within a target journal | `--journal pcs --keywords "embodied cognition,self-state"` |
| `import_openalex.py` | Generate a v1.3-conformant entry from OpenAlex | `--issn 1568-7759 --field psychology --dry-run` |
| `validate_structure.py` | Schema validation; runs in CI on every PR | (run without arguments to validate everything) |
| `bundle_for_upload.py` | Merge journal files for ChatGPT GPT (20-file limit) | `--out-dir dist/` |
| `update_metrics.py` | Refresh OpenAlex metrics in existing entries; propose diffs | `--field psychology --apply` |
| `topic_trend_scan.py` | Scan a journal's recent publication topics; keyword presence check | `--issn 0959-3543 --keywords "BDSM,autoethnography"` |
| `query_spine.py` | Breadth query across all 166,821 spine journals, cross-referenced against the curated set | `--issn 0959-3543` / `--cas-zone 1,2 --uncurated-only` |
| `lint_content.py` | Content-semantics checks beyond schema: uncited high scores, Tier 1 placeholders, missing `signal_quality`. Runs in CI against a frozen baseline | (run without arguments) |
| `package_for_claude_ai.py` | Build the claude.ai chat-mode upload zip | `--out-dir dist/` |

Corpus-maintenance pipelines under `scripts/spine/` (require `pyalex`): building the ISSN spine, enriching methodology evidence from OpenAlex counts, and `detect_defunct.py`, which screens for journals that have stopped publishing. That last one **reports rather than applies** — its first full run called 20 entries ceased and at least 6 turned out to be actively publishing, because OpenAlex indexes small, humanities and non-English venues poorly. Marking a live journal "ceased" is a false claim about a real organisation, so writing a banner requires a human-verified list.

Full setup and example workflows in [scripts/README.md](skills/journal-atlas/scripts/README.md).

---

## Try It Without Installing

[`demo/`](demo/) is a small web app that runs the same pipeline the skill uses:
freeform description → `fit_score.py` screening across all 399 entries → a
streamed recommendation. Three stages, no database, nothing persisted between
requests.

It reuses `fit_score.py` unmodified rather than reimplementing the scoring, and
runs on either Gemini or Claude (`LLM_PROVIDER` in `.env`). Each candidate is
shown as an expandable card carrying its evidence tier and real cited article
counts — the visible proof that a recommendation is assembled from checkable
records rather than model recall.

Setup and launch instructions in [demo/README.md](demo/README.md).

---

## Contributing

The lowest-friction contribution path is **`/ja-validate <journal>`** — share your submission experience conversationally, the skill generates a PR-ready Markdown patch in `dist/`.

Other paths:

- **`/ja-contribute`** — Cold-contribute a new journal entry from scratch
- **[Submission Experience report](.github/ISSUE_TEMPLATE/submission-experience.md)** — Structured GitHub Issue for post-submission retrospectives (acts as a community pattern library)
- **Traditional PR** — Copy [`skills/journal-atlas/TEMPLATE.md`](skills/journal-atlas/TEMPLATE.md), fill what you know, open a PR

See [CONTRIBUTING.md](CONTRIBUTING.md) for quality standards, naming conventions, and reviewer guidelines.

**What we need most**: Soft Metadata. The unwritten rules — reviewer culture, framing requirements, sensitive-topic tolerance. If you've published in or reviewed for a journal, that knowledge is evidence no algorithm can extract.

---

## Use Cases

Full multi-turn session transcripts demonstrating the skill end-to-end:

- **[Self-State Dynamics in Altered-State Autoethnography](use-cases/self-state-altered-states-autoethnography.md)** *(EN)* / **[繁體中文](use-cases/zh-Hant/self-state-altered-states-autoethnography.md)** — 8-turn session covering recommendation, constraint changes, rejection recovery, comparison verdict, and out-of-coverage honesty

See [`use-cases/`](use-cases/) for the contribution template and how to submit your own case study.

---

## What This Is NOT

- **Not a journal ranking.** We provide metadata; you decide what matters.
- **Not a predatory journal blacklist.** Use [Cabells](https://www2.cabells.com/) for that.
- **Not a replacement for Scimago/JCR.** We aggregate their quantitative metrics as a convenience. Our value is the soft metadata they don't have.
- **Not a paper-discovery tool.** For finding papers across the web related to your research, use [Connected Papers](https://www.connectedpapers.com/), [Research Rabbit](https://www.researchrabbit.ai/), [Litmaps](https://www.litmaps.com/), or [Semantic Scholar](https://www.semanticscholar.org/). Journal Atlas does help you find papers **within a specific journal** via `/ja-related` — useful for cover-letter prep.

---

## Adjacent Tools

Journal Atlas plays well with these tools — each answers a different question:

| Tool | Question it answers |
|------|---------------------|
| **Journal Atlas** (this) | "Which journal fits my paper, and what should I expect submitting there?" |
| [B!SON](https://service.tib.eu/bison/) | "Given my abstract, which OA journals algorithmically match?" |
| [Cabells](https://www2.cabells.com/) | "Is this journal predatory?" |
| [Scimago](https://www.scimagojr.com/) / [JCR](https://jcr.clarivate.com/) | "What's the bibliometric ranking of this journal?" |
| [Connected Papers](https://www.connectedpapers.com/) | "What papers cluster around my key paper?" |
| [Research Rabbit](https://www.researchrabbit.ai/) | "Show me my paper's intellectual neighborhood." |
| [Semantic Scholar](https://www.semanticscholar.org/) | "Find papers across the literature on this topic." |

A typical workflow combines several:

1. Discover candidate venues with B!SON
2. Read Journal Atlas entries for those candidates to understand soft metadata
3. Cross-check predatory status with Cabells
4. Use `/ja-related` to find papers to cite within the chosen venue

---

## Lineage

Journal Atlas stands on a 20-year tradition of journal recommenders. We acknowledge the work that came before, and situate ourselves within it rather than against it.

| Year | System | Approach | Status |
|------|--------|----------|--------|
| 2007 | [JANE](https://jane.biosemantics.org/) (Schuemie & Kors, *Bioinformatics*) | PubMed text similarity | Operational, biomedical-only |
| 2007 | [eTBLAST](https://pubmed.ncbi.nlm.nih.gov/17452348/) (Errami et al., *Nucleic Acids Research*) | Three-in-one: reviewer + journal + duplicate detection | Server offline |
| 2015 | [Elsevier Journal Finder](https://journalfinder.elsevier.com/) (Kang et al., *RecSys*) | NLP + Okapi BM25 over Elsevier's catalog | Operational, vendor-locked |
| 2018 | [Maglet](https://ieeexplore.ieee.org/document/8660987/) (Mohtaj & Tavakkoli, *IST*) | Persian-language regional recommender | Academic publication |
| 2022 | [Open Journal Matcher](https://github.com/MarkEEaton/open-journal-matcher) (Eaton, CUNY) | spaCy word vectors over DOAJ; "[pervious technology](https://academicworks.cuny.edu/kb_pubs/261)" framing | Service offline 2022/07 |
| 2021– | [B!SON](https://service.tib.eu/bison/) (TIB + SLUB Dresden, BMBF-funded) | Elasticsearch + BM25 + OpenCitations + ML semantic | **Currently state of the art** for OA recommendation |

### Honoring Open Journal Matcher (OJM)

This project owes particular intellectual debt to **Mark E. Eaton's Open Journal Matcher** *(2020-2022)*. In July 2022, Eaton took OJM offline, writing:

> *"My hope is that someone will pick up where I left off, and build something similar, or perhaps adapt the code for the OJM. There's a place for a tool like the OJM; and we shouldn't leave this space entirely to the big journal publishing companies."*
> — Eaton (2022), [The last days of the Open Journal Matcher](https://kingsboroughlibtech.commons.gc.cuny.edu/2022/07/29/the-last-days-of-the-open-journal-matcher/)

**Journal Atlas is one response to that invitation.**

Eaton's companion paper [*On the ethics of working with library technology*](https://academicworks.cuny.edu/kb_pubs/261) introduced the concept of **"pervious technology"** — tools that users can reach into, tinker with, and adapt. Journal Atlas extends this idea: where OJM was pervious at the code layer, Journal Atlas is pervious at the data layer. The knowledge itself is the product, not a service that can be turned off when one maintainer burns out.

### What Journal Atlas Adds

Three design choices distinguish Journal Atlas from the lineage:

1. **Per-journal knowledge base, not per-query app.** Persistent, citable profiles that improve monotonically with community contribution. Soft metadata algorithms cannot extract from publication data.
2. **Markdown + Git, not service infrastructure.** Zero hosting cost. Zero single point of failure. Anyone can fork.
3. **Designed for the agent era.** Structured as a Claude Agent Skill — installable in one command, consumable by any tool that speaks the skill convention, durable across whatever interface comes next.

We are complementary to B!SON, not competing. Use B!SON to discover candidate OA journals, then read their Journal Atlas pages to understand what submission *actually* involves. See [INSPIRATION.md](INSPIRATION.md) for the full data sources and reference materials.

---

## License

Journal Atlas uses a **dual libre/open-license** model:

- **Content** (Markdown files, journal entries, documentation, templates) — [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0) — the same copyleft license used by Wikipedia.
- **Code** (everything under `skills/journal-atlas/scripts/`) — [MIT License](LICENSE-CODE)

**Attribution is required for all uses.** See [CITATION.cff](CITATION.cff) for the preferred citation format and [AUTHORS.md](AUTHORS.md) for the full credits.

**ShareAlike (copyleft) protects the commons.** You may share and adapt Journal Atlas content for any purpose, including commercial use, but derivative works must be released under the same CC BY-SA 4.0 license. This prevents proprietary absorption while keeping the knowledge base genuinely free.

This dual model aligns with the Free Software Foundation's Four Freedoms, the Open Source Initiative's Open Source Definition, and Creative Commons' Definition of Free Cultural Works.

**Partnerships & integrations** — for deeper collaboration beyond what the license requires (custom datasets, sustained integrations, etc.), contact **Meng-Han Lee at zaious.design@gmail.com**.

Full license details: [LICENSE](LICENSE) | [LICENSE-CODE](LICENSE-CODE)

---

## Acknowledgments

**Founding author**: Meng-Han Lee ([Zaious](https://zaious.dev/)), Independent HCI Researcher and AI Agent Architect. Originator of the [Agentic Social Affordance Framework (ASAF)](https://doi.org/10.5281/zenodo.19652278).

**AI Agent Team**: ChronicleCore — a multi-agent system collaborating under Zaious's direction. Architect: Cardinal (樞機師 / Yui). Other agents will be credited as they contribute. See [AUTHORS.md](AUTHORS.md) for the full team and contributor roster.

Built by researchers, for researchers. Maintained by the community.

See [INSPIRATION.md](INSPIRATION.md) for a full list of tools, papers, and concepts that influenced this project's design — including the ScienceClaw venue-templates corpus that contributed Format and family-level Soft Metadata to several entries.
