# Inspiration & Acknowledgments

Journal Atlas stands on a 20-year tradition of journal recommender tools and a wider scholarship on academic publishing ethics. This document lists every project, paper, and concept that influenced our design — with explicit notes on what we use, what we only reference, and what licenses apply.

---

## Direct Tool Dependencies (used in code)

| Tool | Purpose | License | How we use it |
|------|---------|---------|---------------|
| [**OpenAlex API**](https://openalex.org/) | Bibliometric data source | **CC0** (public domain) | Auto-populate Identity / Metrics / Subject Density / OA via `skills/journal-atlas/scripts/import_openalex.py`. No attribution required, but we cite it. |
| [**pyalex**](https://github.com/J535D165/pyalex) | Python client for OpenAlex | MIT | Imported in `skills/journal-atlas/scripts/import_openalex.py`. |
| [**DOAJ**](https://doaj.org/) | Open Access journal directory | CC0 (data dumps) | Used for cross-validating OA model and APC data. |
| [**SCImago Journal & Country Rank**](https://www.scimagojr.com/) | Bibliometric quartile data | Freely downloadable CSV | Used for cross-validating Quartile field. We do not redistribute SCImago data; users fetch their own. |

We may add `habanero` (Crossref Python client, BSD) in a future release for DOI-level metadata.

---

## Predecessor Systems (referenced, not adapted)

Journal Atlas is the latest in a 20-year lineage of journal recommender tools. We reference these systems in our [Lineage](README.md#lineage) section but do **not** incorporate their code.

### Open Journal Matcher (OJM) — Mark E. Eaton, 2020–2022

The most direct predecessor in spirit. OJM was an open-source DOAJ journal recommender built by a single librarian at CUNY Kingsborough. It went offline in July 2022, with its maintainer writing:

> *"My hope is that someone will pick up where I left off… we shouldn't leave this space entirely to the big journal publishing companies."*
> — Eaton (2022), [*The last days of the Open Journal Matcher*](https://kingsboroughlibtech.commons.gc.cuny.edu/2022/07/29/the-last-days-of-the-open-journal-matcher/)

**Journal Atlas is one response to that invitation.** We do not adapt OJM's code (Flask + spaCy on Google Cloud Functions); we adapt its *mission*. Where OJM was pervious at the code layer, Journal Atlas is pervious at the data layer (Markdown + Git).

**Citation**:
- Eaton, M. E. (2022). *On the ethics of working with library technology: the case of the Open Journal Matcher*. CUNY Academic Works. https://academicworks.cuny.edu/kb_pubs/261
- Eaton, M. E. (2022, July 29). *The last days of the Open Journal Matcher* [Blog post]. CUNY Kingsborough Library Technology Blog.

We owe Eaton's "pervious technology" concept particular intellectual debt — it is one of the clearest articulations of why open, modifiable tools matter for ethical algorithmic systems in academia.

### Other Predecessor Systems

| System | Year | Reference | What we learned |
|--------|------|-----------|----------------|
| **JANE** (Journal/Author Name Estimator) | 2007 | Schuemie & Kors, *Bioinformatics* (2008) | First widely-adopted PubMed-based recommender. Showed algorithmic matching is feasible. Biomedical-limited. |
| **ETBLAST** | 2007 | Errami et al., *Bioinformatics* (2007) | Pioneered three-in-one recommendation (reviewer + journal + similar paper). Now offline. |
| **Elsevier Journal Finder** | 2015 | Kang et al., *RecSys* (2015) | Established NLP + Okapi BM25 as baseline algorithm. Limited to one publisher. |
| **Maglet** | 2018 | Mohtaj & Tavakkoli, *IST* (2018) | Proved regional/language-specific recommenders have value (Persian). |
| **B!SON** | 2021– | Eppelin et al. (TIB + SLUB Dresden) | Current state of the art for OA recommendation. Transparent algorithms, multi-institutional governance. **Complementary to us**, not competitor. |

---

## Methodological Inspiration (referenced in CONTRIBUTING.md guidance)

These works inform how contributors should think about and write Soft Metadata. None are incorporated into the repo as code; they are cited as guidance.

| Work | Author(s) | What it informs |
|------|-----------|----------------|
| *"What feedback do reviewers give when reviewing qualitative manuscripts?"* [(BMC Medical Research Methodology, 2020)](https://link.springer.com/article/10.1186/s12874-020-01005-y) | Trubble et al. (Birmingham meta-review) | Reviewer Pool Characteristics; the Quantitative Mindset Bias detection field |
| [*Publishing in top-ranked journals*](https://patthomson.net/2023/12/04/publishing-in-top-ranked-journals/) (blog post, 2023) | Pat Thomson | Discourse Community framing in Soft Metadata |
| [*How to avoid desk rejections*](https://achilleaskostoulas.com/2014/02/13/how-to-avoid-desk-rejections/) (blog post, 2014) | Achilleas Kostoulas | Hard Blockers / Desk Rejection Rate fields |
| [*Submit to an appropriate journal*](https://terrytao.wordpress.com/advice-on-writing-papers/submit-to-an-appropriate-journal/) (blog post) | Terence Tao | Submission Ladder framing for Strategic Notes |
| [*Better Practices in Journal Metadata*](https://www.erudit.org/public/documents/Better_Practices_Metadata_CP.pdf) (PDF, 2023) | Coalition Publica / Érudit | General journal metadata best practices |
| [*Open Journal Systems schema*](https://github.com/pkp/ojs) (GPL) | Public Knowledge Project | Inspired what fields a "journal record" should contain. We do **not** incorporate OJS code (GPL); we only studied its data model. |

---

## Workflow Concepts Borrowed (not code)

### Rejection Fallback Chain — adapted from AutoResearchClaw

The **Rejection Fallback Chain** section in our journal template and the **Rejection Recovery Mode** in our SKILL.md are conceptually adapted from the multi-stage gate/pivot mechanism in [AutoResearchClaw](https://github.com/) — an autonomous research pipeline that explicitly handles failure modes with `PROCEED / PIVOT / ITERATE` decisions at critical stages.

We don't use any AutoResearchClaw code or infrastructure. We borrowed one idea: **realistic submission workflows are tiered**. A recommender that only outputs "best match" misses the actual practitioner question, which is "and if this doesn't work?" Journal Atlas treats every journal entry as a node in a directed graph of fallback links, letting the AI traverse the graph as a rejection-recovery strategy.

This idea also independently echoes Terence Tao's submission ladder advice (cited in CONTRIBUTING.md): aim high, fall down the ladder. We make that ladder explicit and per-journal.

---

## Related but Independent Projects

Tools that share part of our problem space but operate differently. We may eventually propose integration with some of these, but currently they are independent:

- [**ScienceClaw**](https://github.com/beita6969/ScienceClaw) (MIT, Peter Steinberger 2025) — A self-evolving AI research colleague built on the OpenClaw engine. 285+ skills covering 28 academic disciplines, runtime skill evolution, persistent research memory, zero-hallucination protocol. **Different product class**: ScienceClaw is an autonomous research agent (handles literature search, database queries, statistical analysis, paper writing); Journal Atlas is a per-journal soft-metadata knowledge base. Their `venue-templates` skill (formatting requirements + reviewer expectations + writing styles for 50+ venues, ~5,600 lines of structured Markdown) is a particularly useful **data source** for upgrading our entries. See "Data Sources" section below for how we use it.
- [**Journal-Recommendation-Agent**](https://github.com/jinjinbenjin/Journal-Recommendation-Agent) — query-time AI recommender (Streamlit + Ollama). Different from us: per-query app vs per-journal knowledge base.
- [**findpapers**](https://github.com/jonatasgrosman/findpapers) — multi-source academic paper finder. Adjacent: useful for contributors finding example papers from a journal.
- [**Wispar**](https://github.com/Scriptbash/Wispar) — academic journal update tracker. Adjacent: could inform our "Last verified" maintenance workflow.
- [**metaknowledge**](https://github.com/UWNETLAB/metaknowledge) — Python bibliometric analysis. Adjacent: useful if Journal Atlas adds inter-journal relationship dimensions later.

---

## Data Sources (used as evidence base, adapted into our schema)

These are external knowledge bases whose factual content we have referenced when populating or validating journal entries. Per MIT license terms, content is adapted into our TEMPLATE v1.3 schema (not copy-pasted), and source attribution is recorded in each affected entry's Changelog.

- [**ScienceClaw `venue-templates`**](https://github.com/beita6969/ScienceClaw/tree/main/skills/venue-templates) — MIT-licensed structured Markdown covering Nature / Science / Cell Press / PLOS / IEEE / ACM / Frontiers and ~50 other major venues. Files used:
  - `references/journals_formatting.md` (486 lines) — word counts, abstract limits, citation styles, structural requirements → adapted into our `## Format` section
  - `references/reviewer_expectations.md` (417 lines) — what reviewers prioritize per venue family, common desk-reject patterns → adapted into `Soft Metadata > Reviewer Pool Characteristics` + `Strategic Notes > Hard Blockers`
  - `references/venue_writing_styles.md` (321 lines) — style spectrum across venue types → adapted into `Soft Metadata > Voice & Style` + `Framing Requirements`
  - `references/nature_science_style.md`, `cell_press_style.md`, `medical_journal_styles.md`, `cs_conference_style.md`, `ml_conference_style.md` — venue-family deep dives, used selectively when an entry covers one of these venues

**Attribution convention in our entries**: Changelog rows reference adapted content as `data adapted from ScienceClaw venue-templates (MIT)` with the specific date and contributor.

**Entries currently incorporating ScienceClaw data**:

**A. Journal entries (Format fields — Word limit / Abstract limit / Article types):**

| Field directory | Journals |
|-----------------|----------|
| `multidisciplinary/` | Nature, Nature Communications, Nature Human Behaviour, Science, Science Advances, PNAS, PLOS ONE |
| `biology/` | Cell, Neuron, Immunity, Molecular Cell, Developmental Cell, PLOS Biology, PLOS Computational Biology, Nature Methods, Nature Biotechnology |
| `medical/` | NEJM, The Lancet, JAMA, BMJ, Annals of Internal Medicine |
| `physics/` | Physical Review Letters |
| `hci/` | Nature Machine Intelligence, IEEE Access (added via ScienceClaw scope expansion) |

**B. Conference entries (Soft Metadata family-level adaptation, P3-1 2026-05-17):**

All 18 conference entries under `conferences/` use family-level Soft Metadata templates adapted from:
- `references/cs_conference_style.md` — ACM HCI conference conventions (CHI / CSCW / UIST / DIS / IUI / IDC / CHI PLAY / IEEE HRI)
- `references/ml_conference_style.md` — ML conference conventions (NeurIPS / ICML / ICLR / CVPR / AAAI)
- `references/reviewer_expectations.md` — Cross-venue reviewer expectations (used for NLP family: ACL / EMNLP / NAACL; Data Mining family: KDD / WWW)

Reviewer Pool Characteristics, Framing Requirements, Methodological Preferences, Voice & Style, and Hard Blockers / Soft Tax / Best-suited-for / Not-recommended-for narratives for the 18 conference entries are family-level adaptations of the above ScienceClaw files. Per-conference Identity / Submission Cycle / Program Committee / Submission Format / Review Format details were authored from public CFP and community knowledge.

**C. P3-2 Pass 2 high-leverage journal additions (2026-05-17):**

10 additional journal entries were built to plug fallback-chain gaps identified by the P3-2 audit:

| Entry | Field | Soft Metadata family source |
|-------|-------|-----------------------------|
| Bioinformatics | biology | New `biology-oa` family template (Cardinal-authored, informed by OUP / PLOS / Cell Press OA norms) |
| Nucleic Acids Research | biology | Same `biology-oa` family |
| Cell Reports | biology | Same `biology-oa` family |
| Nature Physics | physics | New `physics-flagship` family (Cardinal-authored, modeled on Nature Portfolio editorial culture) |
| Physical Review Research | physics | New `physics-apos-oa` family (Cardinal-authored, APS conventions) |
| ACM PACM CSCW | hci (Proceedings-Journal) | ScienceClaw `cs_conference_style.md` (ACM SIGCHI family) adapted to proceedings-journal format |
| ACM PACM IMWUT | hci (Proceedings-Journal) | Same — adapted to UbiComp/ISWC proceedings-journal context |
| ACM TOHRI | hci | New `acm-hci-journal` family (Cardinal-authored, ACM Transactions editorial conventions) |
| ACM TACCESS | hci | Same `acm-hci-journal` family |
| TACL (Transactions of ACL) | cognitive-science | ScienceClaw `reviewer_expectations.md` (ACL community) adapted to journal-format |

ScienceClaw attribution is captured in each entry's Changelog where applicable.

**D. P3-4 niche-venue additions (2026-05-17):**

21 additional entries built to plug remaining fallback-chain markers identified by the post-P3-2 audit (38→25 markers, 50→29 venue mentions):

| Subset | Entries | Family template |
|--------|---------|-----------------|
| Biology OA (3) | Briefings in Bioinformatics, eLife, Genome Research | `biology-oa` (reused from P3-2) + new `biology-elife` for eLife's Reviewed Preprints model |
| Multidisciplinary OA (1) | Scientific Reports | New `multidisciplinary-oa-generalist` family (soundness-over-significance review culture) |
| Neuroscience (4) | Cerebral Cortex, NeuroImage, Neuroscience of Consciousness, Clinical Neuropsychologist | New `neuroscience-flagship` family |
| Psychology society-flagship (7) | Memory & Cognition, Alzheimer's & Dementia, Counselling Psych Quarterly, J Vocational Behavior, Environment & Behavior, Assessment, J Gerontology B Psych Sci | New `psychology-society` family |
| HCI magazine-design (3) | IEEE Pervasive Computing, J Design History, IJ Design | New `hci-magazine-design` family |
| Writing studies (1) | College Composition and Communication | New `qualitative-writing` family (NCTE/4Cs norms) |
| Accessibility/affective conferences (2) | ACM ASSETS, ACII | New `accessibility-conference` family (participatory + affective-validity norms) |

Each affected entry's Changelog references the specific family source. Tier 2 (community estimate) banner is applied to all 152 family-adapted entries.

**Conformance with our license model**: ScienceClaw's MIT license permits derivative content. Our adapted Markdown becomes part of the CC BY-SA 4.0 content layer; the underlying schema and tooling remain MIT-compatible. Original ScienceClaw `.md` files are not redistributed in this repo; users wanting their full text should clone the upstream repo directly.

---

## Anti-Patterns We Avoid

We owe these systems gratitude too — for showing what to avoid.

| Pattern | Source | What we do instead |
|---------|--------|-------------------|
| **Publisher lock-in recommenders** | Elsevier / Springer / T&F Journal Finders | Cross-publisher, vendor-neutral |
| **Black-box AI scoring** | Trinka, Researcher.Life | Transparent, human-readable Markdown |
| **Single-maintainer production system** | OJM (died of burnout, not technology) | Community-first, zero-cost infra |
| **Grant-dependent cloud services** | Multiple academic recommenders | Pure Git + Markdown, no runtime cost |
| **Closed source ranking algorithms** | ABS AJG | Open scoring logic in `skills/journal-atlas/scripts/fit_score.py` |

---

## How to Reference Journal Atlas

If you use Journal Atlas in your research workflow or build on it, please cite:

```
Journal Atlas: A community-maintained knowledge base of academic journal fit metadata.
https://github.com/Zaious/journal-atlas (Year accessed: 2026).
```

We will issue a versioned release with a formal citation (CITATION.cff) once v1.0 stabilizes.

---

## License Compatibility Notes

Journal Atlas uses a dual libre/open-license model:
- **Content** — CC BY-SA 4.0
- **Code** (`skills/journal-atlas/scripts/`) — MIT

Compatibility audit for our dependencies and references:

- **OpenAlex data** (CC0) places no restrictions on our use. ✅
- **pyalex** (MIT) is compatible with both our content and code licenses. ✅
- **DOAJ data** (CC0) is freely usable. ✅
- **SCImago CSV** is freely downloadable; we do not redistribute it. ✅
- We do **not** incorporate code from any GPL-licensed predecessor (notably OJS), so our license choice is not constrained by copyleft propagation. ✅

If you find a license incompatibility we missed, please [open an issue](../../issues/new).
