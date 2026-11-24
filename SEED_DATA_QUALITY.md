# Seed Data Quality & Confidence Tiers

> 🌐 **Languages**: English | *(Traditional Chinese version welcome via PR)*

This document explains how the seed journal entries were authored, the differences in evidentiary backing between them, and how the community can help upgrade lower-confidence entries.

We believe a community-maintained knowledge base only earns trust if it is honest about what it doesn't yet know. This page is that honesty.

## What the tier names do and do not mean

Until 2026-11-24 these were called Tier 1 and Tier 2; the JCDL 2026 paper (tag `jcdl2026`) uses the old names. The names do not mean a person verified anything.

Measured 2026-11-22, because the names suggest more than the entries contain:

- **First-hand human reports: 0 of 399 entries** (Sourced: 0 of 11, Estimated: 0 of 152, AI-Researched: 0 of 236), counted by the exact markers the contribution skill writes: `personal experience YYYY`, `contributed by @handle`, `confirmed by personal experience`. A first-hand account typed into free text without a marker would not be found by this count.
- **Who wrote the entries.** The maintainer, working with an AI model, for all three tiers. There are no outside contributors yet. "Sourced" is not "a human checked it"; it is "the claims cite specific counts and sources". The promotion rule below asks for cited evidence, and accepts OpenAlex publication patterns in place of personal experience.
- **"Estimated" (called "Community estimate" until 2026-11-24).** Family-level Soft Metadata adapted from norms shared by similar journals. The word *community* names where the knowledge comes from, not people who reviewed this entry.
- **Second-hand human data does exist in places**, mainly SciRev review-time statistics with a stated sample size (about 74 entries, found by text match, so possibly more). Review culture, desk-reject behaviour and attitude to methods have no first-hand source in any entry.
- **Scoring does not read the tier.** It reads evidence coverage: the share of the six scoring dimensions that have a value. An Estimated entry has a value in nearly every dimension and so scores as fully covered; an AI-Researched entry leaves unsupported dimensions blank and is scored on about 40%. Across three in-domain profiles, journals only, Estimated held 49 of the 60 top-20 slots and AI-Researched held 1, although AI-Researched is 59% of the corpus. `fit_score.py` does not downweight Estimated; the recommendation workflow must say the tier aloud.
- **Table 1 of the JCDL 2026 paper** uses the same coverage measure; its Estimated row is "100%" for that reason. The paper's numbers belong to tag `jcdl2026`.

**Update 2026-11-23.** 94 entries were added (23 in `education/`, 11 in `ai-society/`, 13 in `philosophy/`, 6 each in `economics/`, `management/` and the new `game-studies/`, 3 in `hci/`, 5 each in `library-science/` and `political-science/`, and 4 each in `communication/`, `sociology/`, `anthropology/` and `linguistics/`) and 103 entries moved to Sourced, giving 493 entries: **114 Sourced · 149 Estimated · 230 AI-Researched**. First-hand human reports: still **0 of 493**. A move to Sourced required, per entry: `scripts/tier1_gate.py` passing with at least 6 of 7 Soft Metadata subsections carrying two or more cited lines (a line that records a gap, such as an unreadable page or "0 reviews", does not count); and an independent spot-check of 8 to 12 claim–source pairs in which the verifier fetched each source and found no pair contradicted. Verifiers did find defects (a template comment read as policy, an inflated keyword share, board counts that did not add up, claims attributed to the wrong page); each was corrected before promotion and is named in the entry's changelog. Entries whose key facts rested only on search-engine summaries of unreadable pages, or that passed the gate by only 5 of 7, stayed where they were until their pages were read in a real browser (Educational Philosophy and Theory, Educational Theory, Learning, Media and Technology, Information, Communication & Society and Technology in Society were then re-checked there and promoted on 2026-11-23). A second batch of 16 entries (8 education, 8 philosophy) went through the same gate and one independent spot-check before promotion. A third batch of 12 (comparative philosophy, economics, organisation and management, AI) followed the same path, with one more check of what the corrections added for the three entries that were rewritten from newly readable live pages. A fourth batch of 27 entries (library and information science, communication, sociology, anthropology, political science, linguistics, and more education, economics and management) was written from regional and national journal registers and recent field lists, independently spot-checked (6 pairs per entry, sources re-fetched and Crossref counts re-run), corrected, and promoted when the gate and the check both passed; Applied Linguistics was promoted after its pages were re-read in a real browser. Where a live page answered only in a real browser, the maintainer's own browser was used to read public pages; nothing was logged into or downloaded. Figures that depend on OpenAlex are marked "not independently re-run" where the daily request budget ran out. A fifth batch of 10 (information science, communication, sociology, anthropology, international relations, science and technology studies, philosophy of science, linguistics) and a sixth of 6 video-game and game-studies journals went through the same pipeline. Pages that curl could not read were re-read in the maintainer's own browser for about 30 existing entries; those recovered rows were read directly from the pages and have not had a separate independent spot-check. Held back as AI-Researched: Quantitative Science Studies, Game Studies, Simulation & Gaming and IEEE Transactions on Games, whose key pages are readable only from archived copies or only in a real browser without a second check. The 11 entries that were already Sourced were re-researched the same way; none passed the gate before (8 reached 4 of 7, 2 reached 3, 1 reached 1) and all now do. Median evidence coverage across the three Table 1 profiles is now Sourced 75% (range 50–100), Estimated 100%, AI-Researched 40%: Sourced sits below Estimated because it leaves blank the dimensions it could not source, while Estimated holds an estimate in every field and is scored as covered.

A tier is therefore a statement about how an entry's claims are sourced, never about who has verified them. The way to change that is a first-hand report: `/ja-validate`.

## Two orthogonal dimensions

To avoid confusion, we track entry quality across **two independent axes**:

1. **Evidence Quality** (`Sourced` vs `Estimated` vs `AI-Researched`) — how trustworthy are the Soft Metadata claims that have been written?
2. **Completeness** (`Skeleton` vs filled) — has Soft Metadata been written at all, or is the entry still a structural scaffold?

A Skeleton entry has **no Tier assignment yet** because there's nothing to evaluate. Sourced / Estimated / AI-Researched only apply once Soft Metadata has been authored.

### A third evidence basis: AI-Researched (2026-07)

Starting with the v2 "coverage-first" pivot (see [docs/ATLAS_V2_DESIGN.md](docs/ATLAS_V2_DESIGN.md)), a new batch of entries was added via a different process than either Sourced or Estimated: **per-journal AI research** against live public sources (publisher policy pages, recent publications, SciRev, and mandatory cross-language checks against 小木虫/fabiaoji/知乎), with a per-field `signal_quality` (0–5) score and honest blanks where no public evidence existed — never generic family-level filler.

This is neither Sourced (deeper per-journal research, directed by the maintainer and carried out with an AI) nor Estimated (family-level estimate adapted across many journals at once): it sits in between, with real per-journal citations but often thinner coverage than Sourced, especially on the long tail where no public discussion exists. Rather than force these into the existing two-tier vocabulary, they carry their own banner:

> [!NOTE]
> **AI-Researched (YYYY-MM-DD)** — per-journal sourced facts with an explicit `signal_quality` score; see the entry's "AI-Research Notes" subsection for exactly what was checked and why any field is blank.

**What AI-Researched entries have**: Identity/Metrics/Subject Density from the spine (OpenAlex + JUFO + CAS 中科院分区 + Norwegian Register + DOAJ — all deterministic, sourced facts, no LLM involved); Policies (AI policy, peer review type, preprint) and Positioning (current acceptance focus) from cited per-journal research; Experiential facts (review time, desk-reject notes, reviewer culture) where a public source existed.

**What they intentionally leave `(pending)`**: the deeply subjective Sourced/Estimated subsections — Epistemological & Political Leanings, scored (0–5) Methodological Preferences, Voice & Style, the Sensitive Topics table, and all of Strategic Notes (Hard Blockers / Soft Tax / Best-vs-Not-Recommended-For / Rejection Fallback Chain). These require either lived submission/review experience or a maintainer's deliberate judgment call — AI-research's pipeline was designed to never estimate them without a source, so they're honest gaps, not oversights. Community contributions via `/ja-validate` are exactly how these get filled.

## Lifecycle

```
            ┌─────────────┐
            │  Skeleton   │  Auto-generated from OpenAlex.
            │  (no Tier)  │  Soft Metadata = placeholders.
            └──────┬──────┘  Banner: > [!NOTE]
                   │
       /ja-validate │ /ja-contribute / direct PR
                   │
                   ▼
            ┌─────────────┐
            │  Estimated  │  Soft Metadata adapted from family-level
            │ (not per-   │  norms; no per-claim evidence cited.
            │  journal)   │  Banner: > [!WARNING]
            └──────┬──────┘
                   │
       evidence    │ accumulates (article counts, source URLs,
                   │ first-hand submission/review experience)
                   ▼
            ┌─────────────┐
            │   Sourced   │  Soft Metadata claims have specific
            │ (cites      │  cited evidence (article counts,
            │  sources)   │  source URLs, publication patterns).
            └─────────────┘  No banner (default state).
```

## Current distribution (2026-07)

| State | Count | Banner | Where |
|-------|-------|--------|-------|
| **Skeleton** | 0 | `> [!NOTE]` | All Skeleton entries from earlier phases have been promoted to Estimated in Phase 4. |
| **Estimated** | 152 | `> [!WARNING]` | 132 journals + 20 conferences. Family-level claims; per-journal/per-conference evidence not yet collected. |
| **Sourced** | 11 | none | The 8 psychology + 3 qualitative-methods entries with deep evidence harvesting from manuscript submission research |
| **AI-Researched** | 236 | `> [!NOTE]` | 100 psychology + 106 philosophy (new field) + 30 hci. Per-journal AI research with cited `signal_quality` (0–5); see below. |
| **Total** | **399** | | |

The 236 AI-Researched entries came from the v2 coverage-first pivot (2026-07-13): three demand-ranked target lists (psychology 185, philosophy 107, hci 64 — 100% covered, zero gaps) minus 114 journals that already had an existing entry (those are candidates for a future patch pass, not yet merged in). `overall_signal_quality` distribution across all 350 researched journals: 0 (4), 1 (50), 2 (219), 3 (71), 4 (6) — the bulk sitting at 2/5 (policy + positioning facts, thin-to-no experiential signal) is the expected shape of the long-tail cliff documented in `docs/ATLAS_V2_DESIGN.md` §2. See `references/_soft_metadata_drafts/GAPS_AND_NOTES.md` for the full merge/dedup log, including 4 defunct-ISSN entries flagged for cleanup.

### Field-directory breakdown

| Field | Count | Notes |
|-------|-------|-------|
| `psychology/` | 160 | 60 original (cross-disciplinary phenomenology venues + P3-4) + 100 AI-Researched (2026-07) |
| `hci/` | 60 | 30 original (ScienceClaw + P3-2/P3-4 additions) + 30 AI-Researched (2026-07) |
| `philosophy/` | 106 | **New field directory (2026-07)** — 100% AI-Researched; no Sourced/Estimated entries yet |
| `qualitative-methods/` | 5 | Includes P3-4 College Composition and Communication |
| `cognitive-science/` | 17 | Includes P3-2 TACL + P3-4 (Cerebral Cortex / NeuroImage / Neurosci of Consciousness / Clinical Neuropsych) |
| `multidisciplinary/` | 8 | Nature / Nature Comms / NHB / Science / Science Adv / PNAS / PLOS ONE + P3-4 Scientific Reports |
| `biology/` | 15 | Cell Press family + PLOS + Nature Methods/Biotech + P3-2 (Bioinformatics, NAR, Cell Reports) + P3-4 (Briefings in Bioinformatics / eLife / Genome Research) |
| `medical/` | 5 | NEJM / Lancet / JAMA / BMJ / Annals of Internal Medicine |
| `physics/` | 3 | Physical Review Letters + P3-2 (Nature Physics, Physical Review Research) |
| `conferences/hci/` | 10 | CHI / CSCW / UIST / DIS / IUI / IDC / CHI PLAY / IEEE HRI + P3-4 (ACM ASSETS / ACII) |
| `conferences/ml/` | 5 | NeurIPS, ICML, ICLR, CVPR, AAAI |
| `conferences/nlp/` | 3 | ACL, EMNLP, NAACL |
| `conferences/data-mining/` | 2 | KDD, WWW |
| **Total** | **399** | 399/399 pass `scripts/validate_structure.py` |

### Fallback-chain coverage (P3-2 + P3-4 ledger)

P3-2 + P3-4 systematically swept the entries containing `community contribution welcome` markers across three passes:

- **P3-2 Pass 1 (linker)**: replaced 17 venue mentions with relative-path links to existing Atlas entries
- **P3-2 Pass 2 (build + relink)**: added 10 high-leverage new entries + 6 more venues linked
- **P3-4 (build + relink)**: added 21 niche entries (19 journals + 2 conferences) + 21 more venues linked

After all three passes, 44 venue mentions have been resolved across 51 originally-marked entries.

**Remaining**: 25 markers / 29 venue mentions across 22 entries — these are deeper-niche venues (Briefings in Functional Genomics, Genome Biology, Journal of Neuroscience, Heliyon, Imaging Neuroscience, Career Development Quarterly, Sustainability Science, Educational Researcher, etc.) or generic-tag references ("other educational-research journals" / "Specialty IEEE Transactions in relevant subfield" / "Specialty Physical Review journal" / "other topics") that cannot be resolved to a single entry. These intentionally stay as community-contribution markers and represent the entry points for future contributors.

### Schema version

All 163 entries conform to **schema v1.3**, which introduces:
- **`Venue type`** required field in Identity (`Journal` / `Conference` / `Proceedings-Journal`)
- **`Conference Specifics`** required H2 section for `conferences/` subtree (4 sub-tables: Submission Cycle, Program Committee, Submission Format, Review Format) + Conference Calendar
- Path-aware validation: `validate_structure.py` enforces Conference Specifics only on `conferences/` entries.

### Society Registry (P3-3, schema `society-v1`)

A separate Society Registry under `references/societies/` provides reverse-index metadata: for each major society / publisher in the Atlas, the registry lists all owned venues, society-wide policies (AI / Authorship / OA / Ethics), editorial culture norms, and cross-venue submission strategy (rejection cascade paths).

| Society | Type | Atlas venues | Path |
|---------|------|-------------|------|
| ACM SIGCHI | Society | 8 conferences + 5 journals | [→](skills/journal-atlas/references/societies/acm-sigchi.md) |
| ACM SIGACCESS | Society | 1 conference + 1 journal | [→](skills/journal-atlas/references/societies/acm-sigaccess.md) |
| ACL | Society | 3 conferences + 2 journals | [→](skills/journal-atlas/references/societies/acl.md) |
| APS | Society | 2 journals | [→](skills/journal-atlas/references/societies/aps.md) |
| APA | Society | 12 journals | [→](skills/journal-atlas/references/societies/apa.md) |
| Cell Press | Publisher | 6 journals | [→](skills/journal-atlas/references/societies/cell-press.md) |
| Nature Portfolio | Publisher | 8 journals | [→](skills/journal-atlas/references/societies/nature-portfolio.md) |
| PLOS | Publisher | 3 journals | [→](skills/journal-atlas/references/societies/plos.md) |

The registry has its own lightweight validator (`scripts/validate_societies.py`) checking schema marker + required H2 sections. Society entries are not subject to the journal/conference Venue type or Conference Specifics validation.

## Confidence tiers

Each journal entry under `skills/journal-atlas/references/journals/` was authored through a structured process. The depth of evidentiary backing varies by source:

### Skeleton — Auto-generated scaffold (0 entries — historical reference)

> Phase 4 (2026-05) promoted all earlier Skeleton entries to Estimated via family-level Soft Metadata adaptation. This section is retained as documentation for future contributions that introduce new Skeleton entries (e.g., via `scripts/import_openalex.py --field <new-field>`).

**Backing**: Identity / Metrics / Subject Density / Open Access fields populated automatically via `scripts/import_openalex.py` from the OpenAlex API. Soft Metadata sections (Reviewer Pool Characteristics, Framing Requirements, Methodological Preferences, Voice & Style, Sensitive Topics, Practical Concerns) and Strategic Notes are placeholder text awaiting contributor input.

**What Skeleton means in practice**:
- Structural data is reliable (Identity, h-index, OA model, etc.)
- Soft Metadata sections display `*(community estimate)*` or `*(fill manually)*` placeholders — these are **not** estimates, they are markers that no human has written anything yet
- The recommendation workflow's `Step 4.5: Pre-Conclusion Self-Check` requires AI agents to flag Skeleton entries to the user
- These entries should not be ranked or recommended as if their Soft Metadata existed
- Estimated subjective-judgment uncertainty: **N/A — no judgment yet recorded**

**How to upgrade a Skeleton entry to Estimated**: write at least 5 of the 7 Soft Metadata subsections with community-knowledge-level information (no per-claim evidence required yet). This can be done conversationally via `/ja-validate <journal>` or `/ja-contribute`.

### Sourced (11 entries)

**Backing**: Deep evidence harvesting via author submission research + targeted OpenAlex topic queries + reading of recent publications + publisher policy primary sources.

**Entries**:

| Field | Journals |
|-------|----------|
| psychology (8) | Collabra: Psychology, Culture & Psychology, Frontiers in Psychology, New Ideas in Psychology, Phenomenology and the Cognitive Sciences, Review of General Psychology, Self and Identity, Theory & Psychology |
| qualitative-methods (3) | Cultural Studies ↔ Critical Methodologies, Qualitative Inquiry, Qualitative Research in Psychology |

**What Sourced means in practice**:
- Soft Metadata claims often include specific article counts ("48 articles on self-state ecosystem 2020–2025") with source attribution
- AI Policy, Word Limit, Embargo, OA APC pricing all sourced from publisher author guidelines (with retrieval dates)
- Reviewer pool characteristics and framing requirements informed by recent publication patterns and (where available) published reviewer reports
- Estimated subjective-judgment uncertainty: ~15%

### Estimated (152 entries)

**Backing**: Identity / Metrics / Policies / Format / Subject Density populated from OpenAlex API and publisher author guidelines (high reliability). Soft Metadata authored from community / family-level knowledge rather than per-entry evidence harvesting.

**Composition** (152 entries):
- **Journals (132)**: 11 original HCI journals + 17 ScienceClaw-adapted entries (multidisciplinary / biology / medical) + 75 Phase 4 promotions (across all field directories) + 10 P3-2 high-leverage additions (Bioinformatics / NAR / Cell Reports / Nature Physics / PRR / 4 ACM HCI journals / TACL) + 19 P3-4 niche additions (3 biology / 1 multidisciplinary / 4 neuroscience / 7 psychology / 3 hci / 1 qual-methods)
- **Conferences (20)**: 8 HCI (ACM SIGCHI family) + 5 ML (NeurIPS-style) + 3 NLP (ACL family + ARR rolling review) + 2 Data Mining (KDD / WWW) + 2 P3-4 (ACM ASSETS / ACII)

**What Estimated means in practice**:
- Identity / Metrics / Policies are reliable (OpenAlex + publisher / conference CFP)
- Subject Density top topics are reliable (OpenAlex output for journals; CFP topic areas for conferences)
- **Reviewer Pool Characteristics, Framing Requirements, sensitive-topic receptiveness without article counts, and methodology receptiveness scores without numbered evidence are family-level estimates**
- Each Estimated entry includes a visible warning banner in its Soft Metadata section
- Conference entries additionally use family-level (HCI / ML / NLP / Data Mining) Soft Metadata templates adapted from ScienceClaw `cs_conference_style.md`, `ml_conference_style.md`, `reviewer_expectations.md` (MIT)
- Estimated subjective-judgment uncertainty: ~40-50%

A representative example of Estimated calibration limits: a `topic_trend_scan.py` audit of TOCHI's last 5 years (374 publications) found 0 articles tagged `autoethnography`, even though the Estimated entry rated autoethnography receptiveness at 3/5 based on third-wave HCI generalizations. This is exactly the kind of gap Estimated banner contributors are invited to close.

## Why the distinction matters

Sourced entries cite a source for each claim, so a recommendation built on them can be traced and checked; none has been verified by a person who has submitted there. Estimated entries are useful for filtering and discovery (the structural data is reliable), but their Soft Metadata is a family-level estimate. Cross-check either kind before committing to a submission decision.

The `fit_score.py` and recommendation workflow do not currently downweight Estimated entries automatically. AI agents using the skill should consider Estimated banners as a hedge when presenting recommendations.

## Upgrading an Estimated entry

Contributors are invited to help upgrade Estimated entries. Useful contributions:

1. **Run `scripts/topic_trend_scan.py`** against the journal with field-specific keywords; commit the resulting evidence into Subject Density / Sensitive Topics / Methodological Preferences with cited article counts.
2. **Replace community-estimate phrases** with evidence-backed statements once data is added (banner can be removed when most Soft Metadata fields carry specific cited evidence).
3. **Read recent reviewer reports** if you've published in or reviewed for the journal; add observations to Reviewer Pool Characteristics with personal-experience source notes.

Workflow:

```bash
# 1. Pick an Estimated entry to upgrade (any HCI journal)
# 2. Run a topic scan with field-relevant keywords
python scripts/topic_trend_scan.py --issn <issn> --years 5 \
    --keywords "autoethnography,critical HCI,AI ethics,embodied interaction"

# 3. Open the journal .md, replace pending or community-estimate values
#    with evidence-backed values (cite article counts)

# 4. Once Subject Density + Sensitive Topics + Methodological Preferences
#    all carry numbered evidence, remove the Estimated banner from the
#    Soft Metadata section

# 5. Validate
python scripts/validate_structure.py references/journals/hci/<your-entry>.md

# 6. Open a PR with the rationale for tier promotion in the description
```

An Estimated entry transitions to Sourced when:

- At least 5 of the 7 Soft Metadata subsections carry evidence-backed claims
- Reviewer Pool Characteristics references either OpenAlex publication patterns or personal experience as source
- The banner has been removed
- A maintainer review has approved the promotion

## What's not in this document (yet)

- Per-entry confidence breakdown beyond Sourced / Estimated
- Automated tier-promotion detection (planned for a future `scripts/audit_tiers.py`)
- Cross-entry consistency checks (e.g. journals from the same publisher should share embargo policy unless one of them explicitly overrides)

## Metrics freshness

All quantitative metrics in the original 22 seed entries were sourced from OpenAlex on 2026-05-13 / 2026-05-14. Subsequent batches (Q1 expansion, ScienceClaw absorption, Phase 4 family-promotion, P3-1 conferences) were captured 2026-05-15 through 2026-05-17. Conference acceptance rates / submission cycle details for the 18 P3-1 entries are drawn from public CFP / conference websites (last verified 2026-05-17), not OpenAlex. `scripts/update_metrics.py` runs monthly via [.github/workflows/refresh-metrics.yml](.github/workflows/refresh-metrics.yml), which opens a PR with the proposed metric changes rather than committing them directly.

## Acknowledgments

This honest-disclosure framing was developed in dialogue with the founding author and the ChronicleCore expert system during pre-release quality review. See [AUTHORS.md](AUTHORS.md) for the full team.
