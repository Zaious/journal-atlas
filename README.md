# Journal Atlas

> 🌐 **Languages**: English | [繁體中文](README.zh-Hant.md)

[![License: CC BY-SA 4.0](https://img.shields.io/badge/Content-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE-CODE)
[![Schema](https://img.shields.io/badge/Schema-v1.3-green.svg)](skills/journal-atlas/TEMPLATE.md)
[![Status](https://img.shields.io/badge/Status-Pre--release%20(seeding)-orange.svg)](#tier-system)

### ▶ [Try it now — journal-atlas.chroniclecore.com](https://journal-atlas.chroniclecore.com)

Paste an abstract, get a cited recommendation. No account, no install. Runs the
same knowledge base and the same scoring code as the skill below.

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
- [Coverage and Inclusion Status](#coverage-and-inclusion-status)
- [Tier System](#tier-system)
- [How This Got Here](#how-this-got-here)
- [Automation Scripts](#automation-scripts)
- [Try It Without Installing](#try-it-without-installing)
- [**Contributing — the two things that actually move this**](#contributing--the-two-things-that-actually-move-this)
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

## Coverage and Inclusion Status

**Journal Atlas is not a general journal database.** It is a deep, uneven atlas of
one region of the literature: the qualitative and interpretive human sciences,
plus the parts of computing that publish about people. Read the table before you
read a recommendation.

### What is actually in the corpus

399 curated entries, as of 2026-07-30:

| Field | Entries | Tier 1 | Tier 2 | AI-Researched |
|---|---:|---:|---:|---:|
| Psychology | 160 | 8 | 52 | 100 |
| Philosophy | 106 | 0 | 0 | **106** |
| HCI (journals) | 60 | 0 | 30 | 30 |
| Cognitive science | 17 | 0 | 17 | 0 |
| Biology | 15 | 0 | 15 | 0 |
| HCI (conferences) | 10 | 0 | 10 | 0 |
| Multidisciplinary (*Nature*, *Science*, PNAS, PLOS ONE…) | 8 | 0 | 8 | 0 |
| ML conferences (NeurIPS, ICML, ICLR, AAAI, CVPR) | 5 | 0 | 5 | 0 |
| Medical (*NEJM*, *Lancet*, *JAMA*, *BMJ*, *Annals*) | 5 | 0 | 5 | 0 |
| Qualitative methods | 5 | 3 | 2 | 0 |
| NLP conferences (ACL, EMNLP, NAACL) | 3 | 0 | 3 | 0 |
| Physics | 3 | 0 | 3 | 0 |
| Data-mining conferences (KDD, WWW) | 2 | 0 | 2 | 0 |

Four adjacent fields — psychology, philosophy, HCI, cognitive science — are
**88% of the corpus (353 of 399)**. Everything else is a thin, deliberately
chosen sample of the venues an author in those fields might reach toward: the
five general-science megajournals, the five general-medicine journals, the major
ML/NLP conferences. They are landmarks, not coverage.

### What is verifiably absent

These returned **zero** entries when the corpus was probed on 2026-07-30:

- **Library and information science** — including digital libraries. (Yes: this
  tool cannot evaluate a paper submitted to the venue this project itself
  targets. Stated here rather than discovered by a user.)
- **Sociology** · **Anthropology** · **Chemistry, mathematics, and the earth sciences**

Near-zero, and misleadingly so: economics/business (2), law (1), political
science (1) — every one of those is a *philosophy* journal about the subject
(*Business Ethics Quarterly*, *Erasmus Journal for Philosophy and Economics*),
not a journal of the discipline. Education (9) and linguistics (3) exist only as
their psychology-facing edges. There is no marketing, no consumer research, no
nursing science, no engineering outside three robotics venues.

**If your field is on that list, this tool has nothing to offer you yet, and it
will say so.** It is built to answer "I don't have data on this" rather than to
produce a plausible-looking ranking of the nearest journals it happens to hold —
a wrong recommendation costs an author months. Point `/ja-contribute` at a
journal you know and it becomes the first entry in a new field.

### Why the distribution looks like this

It is not a principled sampling frame. It reflects where the project started —
one researcher's own submission problem in qualitative psychology and philosophy
of mind — and then grew outward along the paths that mattered to its
contributors. The corpus is honest about being a convenience sample. The fields
above are the highest-value places to grow it — see
[Contributing](#contributing--the-two-things-that-actually-move-this) for the
two paths that do that.

### How complete is an individual entry

Separately from *which* journals exist, entries differ in how much of each one
is filled in. Every scoring dimension returns "unknown" rather than a midpoint
when the evidence is missing, so a recommendation carries an **evidence
coverage** percentage alongside its score:

- **163 entries (Tier 1 + Tier 2): 85–100% coverage.** Scored on nearly every dimension.
- **236 entries (AI-Researched): ~40% coverage.** These are missing the same four
  things — methodology fit, reviewer-pool character, voice compatibility, and
  strategic notes — because the AI-research pipeline was built never to estimate
  them without a source. They need lived submission or review experience. See
  [SEED_DATA_QUALITY.md](SEED_DATA_QUALITY.md).

So `62.5/100 · 45% evidence` and `73.0/100 · 75% evidence` are different claims,
and the interface shows you which one you got. A high score on thin evidence is
a shrunken score by construction — scores are pulled toward the neutral 50 in
proportion to how little is known — but it is still worth less than the same
number backed by more.

**Philosophy is the sharpest case: 106 entries, none human-verified.** It is the
second-largest field in the corpus and the least substantiated. Treat those
recommendations as leads to check, not as findings.

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

---

## How This Got Here

Every date below is a commit date, recoverable with `git log --reverse`. The
shape of the history is the argument, so it is given rather than summarized.

### The problem nobody was solving

Ask any capable model where to send your paper and you get a list of the most
prestigious venues in the general area. That answer is not wrong so much as
useless: it is the answer you would have guessed yourself, it ignores every
constraint that actually decides the outcome — fee budget, word ceiling, ethics
approval, whether your method will survive the reviewer pool — and it is
delivered with the same confidence whether the model knows the journal or is
reconstructing it from the shape of its name.

Plenty of tools answer neighbouring questions well: B!SON matches abstracts to
OA journals, Cabells flags predatory venues, Scimago ranks. What none of them
hold is the part authors actually ask each other about in private — how a
reviewer pool treats qualitative work, whether a "no strict word limit" is real,
what a desk rejection there means. That knowledge exists, distributed across
people who have submitted and reviewed, and nowhere machine-readable.

So the question this project started from was narrow: **can that soft knowledge
be written down in a form an AI agent can read, without inventing the parts
nobody knows?**

### 2026-05-12 → 05-18: dogfooding, 22 → 163 entries

Built to solve one researcher's own submission problem, in their own fields.
The first day's second commit already widened the scope from those fields to all
disciplines — the narrowness was visible immediately.

The decision that shaped everything came on **05-14, at 22 entries**: Tier 2
warning banners and [SEED_DATA_QUALITY.md](SEED_DATA_QUALITY.md), written
before there was any corpus worth defending. Marking your own data as
low-confidence while you have almost none of it is cheap; it is expensive later,
once the number is something you would rather quote. Doing it at 22 entries is
why the tier system is load-bearing rather than decorative.

By **05-17** the corpus reached 163 through absorbing an adjacent venue-template
project and writing conference entries. On **05-18** the content licence moved
from CC BY-NC-SA to **CC BY-SA** — dropping NonCommercial, because a knowledge
base that a commercial tool may not read is a knowledge base arguing with its
own purpose.

Then **eight weeks of nothing.** 05-18 to 07-13, no commits.

### 2026-07-13: the pivot — breadth, because depth alone cannot be evaluated

163 hand-written entries is a demo. The problem is that nobody can tell whether
a demo is right. Ask it about a journal it holds and it looks impressive; ask it
about the journal you actually care about and it has nothing, and you cannot
distinguish "this project is a careful instrument with a narrow corpus" from
"this project is thin."

So v2 went coverage-first, in one day:

- A **166,821-row ISSN spine** joining OpenAlex, DOAJ, JUFO, CAS, the Norwegian
  Register and Retraction Watch — enough to answer *does this journal exist,
  is it indexed, is it alive* for essentially any ISSN, without pretending to
  soft metadata.
- An **AI research pipeline** ([WO2](docs/workorders/WO2_SOFT_METADATA_BATCH.md))
  that took the corpus from 163 to **399** the same day.

The pipeline's rule is the whole point, and it is why the coverage table above
reads the way it does: **facts with a source URL, or a blank with a recorded
reason.** Not a plausible sentence. `review_time: SciRev returned 0 reviews` is
a correct output. Chinese-language sources (小木虫, 知乎) were mandatory rather
than optional, because for many journals they carry the only first-hand signal
that exists.

That rule is exactly why 236 AI-researched entries sit at ~40% evidence
coverage instead of 100%. The four dimensions they are missing — methodology
fit, reviewer pool, voice, strategic notes — are the ones that need someone who
has actually submitted. A pipeline that filled them would have produced a
better-looking corpus and a worse one.

### 2026-07-20 → 07-30: finding out what was wrong with it

**Ten days of commits. Zero entries added.** The last third of the project was
spent breaking its own work:

| What was found | Why it mattered |
|---|---|
| AI-permission-gate matched the template's own row label | **399 of 399** journals falsely gated — any paper disclosing AI use was eliminated corpus-wide, silently |
| Page counts and years parsed as word limits | One venue rejected anything over "30 words" |
| Unstated IRB and fee budget read as *no* IRB and *zero* budget | 33 journals eliminated for a theoretical paper, invisibly |
| Word-limit ranges read as the floor | "Up to 10,000 permitted" scored as 5,000 — caught by evals, after a test had asserted the wrong behaviour |
| Two of six scoring dimensions were never implemented | Capped every entry in the corpus at 70% evidence coverage |
| 61 high scores with no citation behind them | Given real OpenAlex counts; one was contradicted and downgraded |
| Defunct-journal screening | ~30% false-positive rate measured, so `--write` was gated behind human verification rather than shipped |

The pattern in every one of those: a hard constraint that eliminates a candidate
is **invisible to the user**. A wrong recommendation can be argued with. A
journal that silently never appears cannot. So ambiguity now resolves
permissively, and unknown propagates as unknown rather than as a midpoint.

Also in this window: a [dispute mechanism](docs/GOVERNANCE.md) with a stated
response time, a `Disputed` marker, a content linter, CI, 12 verified-ceased
journals flagged with their successors named, and the first real end-to-end run
on a live model — which immediately exposed four more defects.

### 2026-07-31: public

Not because it is finished. Because the honest statement of what it holds, what
it does not, and how wrong it has been is now written down and checkable — and
that statement is more useful to a stranger than another two hundred entries
would be.

What it can do: rank real venues against real constraints, cite article counts
per topic, tell you the evidence behind each score, and say "I don't have data
on this." What it cannot do: cover most of the academy, tell you anything
trustworthy about reviewer culture at 236 of its 399 entries, or replace one
colleague who has published there. See
[Coverage and Inclusion Status](#coverage-and-inclusion-status) for the numbers,
and [PROJECT_COMPLETION.md](docs/PROJECT_COMPLETION.md) for what finished would
look like.

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

### **[journal-atlas.chroniclecore.com](https://journal-atlas.chroniclecore.com)** — live, no account, no install

[`demo/`](demo/) is the web app behind it, running the same pipeline the skill uses:
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

## Contributing — the two things that actually move this

The coverage table above states the two holes precisely, and they need two
different kinds of help. Everything else is secondary.

> **Hole 1 — most of the academy is missing.** Nine field directories, 88% of
> them four adjacent fields. Zero entries in library science, sociology,
> anthropology, the physical sciences.
>
> **Hole 2 — 236 of 399 entries have no human behind them.** They carry policy
> and topic facts with sources, and nothing about how it actually goes.

### Path 1 — Bring your whole field in, the way we did

**This is the highest-leverage contribution and it is not a per-journal chore.**
The 236-entry expansion on 2026-07-13 was one AI research run over a target
list, and the procedure is published so you can point it at your own field:
[**WO2_SOFT_METADATA_BATCH.md**](docs/workorders/WO2_SOFT_METADATA_BATCH.md).

Roughly:

1. **Build a target list.** Pick your field, rank by OpenAlex citation count or
   by what people in your field actually submit to. 20 journals is a real
   contribution; 100 makes your field first-class.
2. **Run the three-layer pass per journal** — policy (AI use, peer review,
   preprint, OA/APC) from publisher pages; positioning from OpenAlex topics;
   experiential (review time, desk-reject rate, reviewer culture) from SciRev,
   Reddit, and **the Chinese-language forums 小木虫 / 知乎, which are mandatory,
   not optional** — for a great many journals they carry the only first-hand
   account that exists anywhere.
3. **Open a PR with the drafts.** They land as AI-Researched tier, banner and
   all, and become the scaffolding your field's practitioners fill in.

Two rules make the difference between help and damage:

- **Facts with a source URL, or a blank with a recorded reason.** `review_time:
  SciRev returned 0 reviews` is a correct, valuable output. A plausible sentence
  with no source is worse than an empty field, because the empty field is
  honest and someone will fill it.
- **Never store verbatim text** from forums, policy pages, or abstracts —
  normalize to a fact plus a link. It keeps the corpus CC BY-SA-compatible.

If your field has zero entries today, the first PR is the one that matters most.
Say so in the issue and the target list can be built with you.

### Path 2 — Backfill what only you know

**If you have submitted to or reviewed for a journal, you hold data this project
cannot obtain any other way.** No amount of AI research reaches it. It is
precisely the four dimensions the 236 AI-researched entries are missing:

- Does the reviewer pool judge qualitative work by quantitative standards?
- Is the stated word limit real, or is it negotiable in practice?
- What framing does a paper need to survive there?
- Which topics get a rougher ride than the scope statement admits?
- What does a desk rejection there actually mean, and where should it go next?

```bash
/ja-validate <journal name>
```

It interviews you conversationally and writes a PR-ready patch into `dist/`.
Ten minutes about one journal you know well is worth more than a hundred entries
of policy scraping — and if it contradicts what an entry currently claims, say
so: contradictions are handled by the [dispute
mechanism](docs/GOVERNANCE.md), not quietly dropped.

**One journal is a real contribution.** Most of Path 2's value arrives one entry
at a time.

### Everything else

- **`/ja-contribute`** — cold-write a new entry from scratch
- **[Submission Experience report](.github/ISSUE_TEMPLATE/submission-experience.md)** — structured issue for a post-submission retrospective
- **Traditional PR** — copy [`TEMPLATE.md`](skills/journal-atlas/TEMPLATE.md), fill what you know, leave the rest blank
- **Tell us an entry is wrong** — see [Think a claim about your journal is wrong?](#think-a-claim-about-your-journal-is-wrong)

Quality standards, naming conventions and reviewer guidelines are in
[CONTRIBUTING.md](CONTRIBUTING.md). The one standard that is not negotiable:
**a blank field beats a guess.**

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

The corpus is the visible part, but it is not the contribution. Two of these
three are **methods**, and a method transfers to fields this project will never
cover.

**1. A method for judging fit** — [`fit_score.py`](skills/journal-atlas/scripts/fit_score.py)
plus [CONSUMPTION_CONTRACT.md](skills/journal-atlas/CONSUMPTION_CONTRACT.md).
Hard constraints eliminate; six weighted dimensions rank what survives. The
discipline that makes it usable is what it does with ignorance: an unevidenced
dimension returns *unknown* rather than a midpoint, the remaining weights
renormalise, and the result shrinks toward neutral in proportion to how little
is known. So a score arrives with an evidence-coverage figure attached, and
`62.5/100 · 45% evidence` is legible as a weaker claim than `73.0/100 · 75%
evidence`. None of that is specific to journals.

**2. A method for building the corpus with AI without inventing it** —
[WO2_SOFT_METADATA_BATCH.md](docs/workorders/WO2_SOFT_METADATA_BATCH.md). Three
layers per venue (policy, positioning, experiential), cross-language sources
mandatory rather than optional, and one rule that decides everything: **a fact
with a source URL, or a blank with a recorded reason.** `review_time: SciRev
returned 0 reviews` is a correct output. This is what took the corpus from 163
to 399 entries in a day, and it is what a contributor points at their own field.

**3. Standards you can fork instead of argue about.** Two kinds of disagreement
get two mechanisms. If a *claim* is wrong, the [dispute
process](docs/GOVERNANCE.md) corrects it in place. If you think the *standard*
is wrong — that Tier 2 is too generous, that AI-Researched entries should not
ship at all, that the weights are miscalibrated — you fork, change the rules,
and run your own. That is cheap here specifically because there is no service to
duplicate: clone the repository, edit Markdown, done. Two corpora with different
bars can both be right for different readers, which is not true of a tool with
one hosted answer.

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
