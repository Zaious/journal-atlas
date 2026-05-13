# Journal Atlas

**A community-maintained, AI-native knowledge base of academic journal fit metadata.**

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

Initial seed coverage includes psychology, HCI, qualitative methodology, and cognitive science — but we actively welcome contributions from all fields. If your discipline isn't represented yet, you can be the one to start it.

---

## How to Use

### Option 1: Claude Code (recommended)

Install as a skill plugin:

```bash
claude /plugin marketplace add Zaious/journal-atlas
claude /plugin install journal-atlas
```

Then ask naturally:

> "I have a 12,000-word theoretical paper on self-state switching in BDSM contexts.
> No IRB, no APC budget, I used AI for writing assistance. Which journals fit?"

The skill reads the knowledge base, filters by your constraints, and ranks by soft fit.

### Option 2: Claude Desktop

1. Clone this repo: `git clone https://github.com/Zaious/journal-atlas.git`
2. Create a new Project in Claude Desktop
3. Upload the `.md` files from `references/journals/` as Project Knowledge
4. Copy the contents of `SKILL.md` into Project Instructions

### Option 3: ChatGPT (GPT Builder)

1. Clone this repo
2. Run `python scripts/bundle-for-upload.py` to merge journal files into uploadable chunks
3. Upload the output files to your GPT's Knowledge section
4. Copy the contents of `SKILL.md` into your GPT's Instructions

### Option 4: Just read it

Browse [`references/journals/`](references/journals/) on GitHub. Every journal is a readable Markdown page. No AI required.

---

## Automation (scripts/)

| Script | Purpose |
|--------|---------|
| `validate-structure.py` | Check that journal `.md` files match the template schema. Runs on every PR. |
| `update-metrics.py` | Fetch latest IF / h-index / CiteScore from OpenAlex API. Proposes a PR draft — never auto-writes. |
| `topic-trend-scan.py` | Scan a journal's recent publications to detect topic trend shifts. |
| `fit-score.py` | Compute a numerical fit score given your paper's attributes vs. each journal. |
| `bundle-for-upload.py` | Merge journal files into larger chunks for platforms with file count limits (e.g. ChatGPT). |

---

## Contributing

We need your journal expertise. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

**Quick version:**
1. Copy [TEMPLATE.md](TEMPLATE.md)
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

### Where Journal Atlas Fits

Every system above answers the same question — *given an abstract, which journals match?* — using metric similarity over publication data. None of them capture the knowledge a senior colleague would share over coffee:

- *"That journal's reviewer pool expects Heidegger literacy."*
- *"This one desk-rejects anything without IRB, even theoretical work."*
- *"They say single-blind, but the editor leaks identity to friendly reviewers."*
- *"First-person voice gets you flagged here, but it's expected next door."*

Journal Atlas is the first system to make this knowledge **structured, contributable, and machine-readable**. We are complementary to B!SON, not competing — use B!SON to discover candidate OA journals, then read their Journal Atlas pages to understand what submission to each *actually involves*.

Two design choices distinguish us from the lineage:

1. **Per-journal knowledge base, not per-query app** — predecessors compute fresh similarity scores at query time; we maintain persistent, citable journal profiles that humans and AI agents both consume.
2. **Markdown + Git, not service infrastructure** — predecessors that depended on cloud services (OJM) or grant funding cycles (B!SON's BMBF period ended 2023/01) face structural risks; we have zero hosting cost and zero single point of failure. Anyone can fork.

We learned the maintenance lesson from OJM's offline notice: *single maintainers do not survive*. Journal Atlas is community-first by design.

---

## License

[TBD — see CONTRIBUTING.md for discussion]

---

## Lineage

Journal Atlas builds on a 20-year tradition of journal recommender tools. Each previous attempt taught us something:

- **JANE** *(Schuemie & Kors, 2008)* — the first widely-used PubMed-based recommender. Showed that journal matching could be algorithmically assisted. Limited to biomedical fields.
- **ETBLAST** *(Errami et al., 2007)* — pioneered three-in-one recommendation (reviewer + journal + similar papers). Now offline.
- **Elsevier Journal Finder** *(Kang et al., 2015)* — established NLP + BM25 as a baseline. Limited to one publisher's catalog.
- **Maglet** *(Mohtaj & Tavakkoli, 2018)* — proved that regional / language-specific recommenders have real value (Persian-language journals).
- **B!SON** *(TIB + SLUB Dresden, 2021–)* — the current state of the art for OA journal recommendation. Transparent algorithms, multi-institutional governance. Strongly recommended as a complementary tool to Journal Atlas: B!SON gives you query-time recommendations; Journal Atlas gives you per-journal context.

### Honoring Open Journal Matcher (OJM)

This project owes particular intellectual debt to **Mark E. Eaton's Open Journal Matcher** *(2020-2022)*, an open-source DOAJ journal recommender built at CUNY Kingsborough.

In 2022, Eaton took OJM offline, writing:

> *"My hope is that someone will pick up where I left off, and build something similar, or perhaps adapt the code for the OJM. There's a place for a tool like the OJM; and we shouldn't leave this space entirely to the big journal publishing companies."*
> — Eaton (2022), [The last days of the Open Journal Matcher](https://kingsboroughlibtech.commons.gc.cuny.edu/2022/07/29/the-last-days-of-the-open-journal-matcher/)

**Journal Atlas is one response to that invitation.**

Eaton's 2022 paper [*On the ethics of working with library technology: the case of the Open Journal Matcher*](https://academicworks.cuny.edu/kb_pubs/261) introduced the concept of **"pervious technology"** — tools that users can reach into, tinker with, and adapt, in contrast to impervious black-box systems. Eaton argued that pervious tools, combined with diverse perspectives, are how ethical problems in technology become apparent.

Journal Atlas extends this idea further: where OJM was pervious *at the code layer* (Flask + spaCy, open source on GitHub), Journal Atlas is pervious *at the data layer* — every journal entry is a plain-text Markdown file that any researcher can read, edit, and discuss. The knowledge itself is the product, not a service that can be turned off when one maintainer burns out.

### What Journal Atlas Adds to the Lineage

Across all previous systems, two patterns held:
1. **All recommenders computed metric similarity from abstracts.** None captured reviewer culture, framing requirements, methodological preferences, or sensitive topic receptiveness.
2. **All were query-time applications** — running services that needed someone to maintain them. None were durable, community-maintained per-journal knowledge bases.

Journal Atlas addresses both gaps. The soft metadata captured here is information that algorithms cannot extract from publication metadata — it requires human community knowledge, and it requires durability beyond any single maintainer's commitment.

---

## Acknowledgments

Built by researchers, for researchers. Maintained by the community.

Initial seed data drawn from journal evaluations conducted during active manuscript submission processes in psychology, HCI, and qualitative methodology (2025-2026).

See [INSPIRATION.md](INSPIRATION.md) for a full list of tools, papers, and concepts that influenced this project's design.
