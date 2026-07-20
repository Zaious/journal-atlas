# Seed Data Quality & Confidence Tiers

> 🌐 **Languages**: English | *(Traditional Chinese version welcome via PR)*

This document explains how the seed journal entries were authored, the differences in evidentiary backing between them, and how the community can help upgrade lower-confidence entries.

We believe a community-maintained knowledge base only earns trust if it is honest about what it doesn't yet know. This page is that honesty.

## Two orthogonal dimensions

To avoid confusion, we track entry quality across **two independent axes**:

1. **Evidence Quality** (`Tier 1` vs `Tier 2` vs `AI-Researched`) — how trustworthy are the Soft Metadata claims that have been written?
2. **Completeness** (`Skeleton` vs filled) — has Soft Metadata been written at all, or is the entry still a structural scaffold?

A Skeleton entry has **no Tier assignment yet** because there's nothing to evaluate. Tier 1 / Tier 2 / AI-Researched only apply once Soft Metadata has been authored.

### A third evidence basis: AI-Researched (2026-07)

Starting with the v2 "coverage-first" pivot (see [docs/ATLAS_V2_DESIGN.md](docs/ATLAS_V2_DESIGN.md)), a new batch of entries was added via a different process than either Tier 1 or Tier 2: **per-journal AI research** against live public sources (publisher policy pages, recent publications, SciRev, and mandatory cross-language checks against 小木虫/fabiaoji/知乎), with a per-field `signal_quality` (0–5) score and honest blanks where no public evidence existed — never generic family-level filler.

This is neither Tier 1 (deep manual evidence-harvesting by the maintainer) nor Tier 2 (family-level community estimate adapted across many journals at once): it sits in between, with real per-journal citations but often thinner coverage than Tier 1, especially on the long tail where no public discussion exists. Rather than force these into the existing two-tier vocabulary, they carry their own banner:

> [!NOTE]
> **AI-Researched (YYYY-MM-DD)** — per-journal sourced facts with an explicit `signal_quality` score; see the entry's "AI-Research Notes" subsection for exactly what was checked and why any field is blank.

**What AI-Researched entries have**: Identity/Metrics/Subject Density from the spine (OpenAlex + JUFO + CAS 中科院分区 + Norwegian Register + DOAJ — all deterministic, sourced facts, no LLM involved); Policies (AI policy, peer review type, preprint) and Positioning (current acceptance focus) from cited per-journal research; Experiential facts (review time, desk-reject notes, reviewer culture) where a public source existed.

**What they intentionally leave `(pending)`**: the deeply subjective Tier 1/Tier 2 subsections — Epistemological & Political Leanings, scored (0–5) Methodological Preferences, Voice & Style, the Sensitive Topics table, and all of Strategic Notes (Hard Blockers / Soft Tax / Best-vs-Not-Recommended-For / Rejection Fallback Chain). These require either lived submission/review experience or a maintainer's deliberate judgment call — AI-research's pipeline was designed to never estimate them without a source, so they're honest gaps, not oversights. Community contributions via `/ja-validate` are exactly how these get filled.

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
            │   Tier 2    │  Soft Metadata written from community
            │ (community  │  knowledge; no per-claim evidence cited.
            │  estimate)  │  Banner: > [!WARNING]
            └──────┬──────┘
                   │
       evidence    │ accumulates (article counts, source URLs,
                   │ first-hand submission/review experience)
                   ▼
            ┌─────────────┐
            │   Tier 1    │  Soft Metadata claims have specific
            │ (evidence-  │  cited evidence (article counts,
            │  backed)    │  source URLs, publication patterns).
            └─────────────┘  No banner (default state).
```

## Current distribution (2026-07)

| State | Count | Banner | Where |
|-------|-------|--------|-------|
| **Skeleton** | 0 | `> [!NOTE]` | All Skeleton entries from earlier phases have been promoted to Tier 2 in Phase 4. |
| **Tier 2** | 152 | `> [!WARNING]` | 132 journals + 20 conferences. Family-level claims; per-journal/per-conference evidence not yet collected. |
| **Tier 1** | 11 | none | The 8 psychology + 3 qualitative-methods entries with deep evidence harvesting from manuscript submission research |
| **AI-Researched** | 236 | `> [!NOTE]` | 100 psychology + 106 philosophy (new field) + 30 hci. Per-journal AI research with cited `signal_quality` (0–5); see below. |
| **Total** | **399** | | |

The 236 AI-Researched entries came from the v2 coverage-first pivot (2026-07-13): three demand-ranked target lists (psychology 185, philosophy 107, hci 64 — 100% covered, zero gaps) minus 114 journals that already had an existing entry (those are candidates for a future patch pass, not yet merged in). `overall_signal_quality` distribution across all 350 researched journals: 0 (4), 1 (50), 2 (219), 3 (71), 4 (6) — the bulk sitting at 2/5 (policy + positioning facts, thin-to-no experiential signal) is the expected shape of the long-tail cliff documented in `docs/ATLAS_V2_DESIGN.md` §2. See `references/_soft_metadata_drafts/GAPS_AND_NOTES.md` for the full merge/dedup log, including 4 defunct-ISSN entries flagged for cleanup.

### Field-directory breakdown

| Field | Count | Notes |
|-------|-------|-------|
| `psychology/` | 160 | 60 original (cross-disciplinary phenomenology venues + P3-4) + 100 AI-Researched (2026-07) |
| `hci/` | 60 | 30 original (ScienceClaw + P3-2/P3-4 additions) + 30 AI-Researched (2026-07) |
| `philosophy/` | 106 | **New field directory (2026-07)** — 100% AI-Researched; no Tier 1/Tier 2 entries yet |
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

> Phase 4 (2026-05) promoted all earlier Skeleton entries to Tier 2 via family-level Soft Metadata adaptation. This section is retained as documentation for future contributions that introduce new Skeleton entries (e.g., via `scripts/import_openalex.py --field <new-field>`).

**Backing**: Identity / Metrics / Subject Density / Open Access fields populated automatically via `scripts/import_openalex.py` from the OpenAlex API. Soft Metadata sections (Reviewer Pool Characteristics, Framing Requirements, Methodological Preferences, Voice & Style, Sensitive Topics, Practical Concerns) and Strategic Notes are placeholder text awaiting contributor input.

**What Skeleton means in practice**:
- Structural data is reliable (Identity, h-index, OA model, etc.)
- Soft Metadata sections display `*(community estimate)*` or `*(fill manually)*` placeholders — these are **not** estimates, they are markers that no human has written anything yet
- The recommendation workflow's `Step 4.5: Pre-Conclusion Self-Check` requires AI agents to flag Skeleton entries to the user
- These entries should not be ranked or recommended as if their Soft Metadata existed
- Estimated subjective-judgment uncertainty: **N/A — no judgment yet recorded**

**How to upgrade a Skeleton entry to Tier 2**: write at least 5 of the 7 Soft Metadata subsections with community-knowledge-level information (no per-claim evidence required yet). This can be done conversationally via `/ja-validate <journal>` or `/ja-contribute`.

### Tier 1 — Evidence-backed (11 entries)

**Backing**: Deep evidence harvesting via author submission research + targeted OpenAlex topic queries + reading of recent publications + publisher policy primary sources.

**Entries**:

| Field | Journals |
|-------|----------|
| psychology (8) | Collabra: Psychology, Culture & Psychology, Frontiers in Psychology, New Ideas in Psychology, Phenomenology and the Cognitive Sciences, Review of General Psychology, Self and Identity, Theory & Psychology |
| qualitative-methods (3) | Cultural Studies ↔ Critical Methodologies, Qualitative Inquiry, Qualitative Research in Psychology |

**What Tier 1 means in practice**:
- Soft Metadata claims often include specific article counts ("48 articles on self-state ecosystem 2020–2025") with source attribution
- AI Policy, Word Limit, Embargo, OA APC pricing all sourced from publisher author guidelines (with retrieval dates)
- Reviewer pool characteristics and framing requirements informed by recent publication patterns and (where available) published reviewer reports
- Estimated subjective-judgment uncertainty: ~15%

### Tier 2 — Community estimate (152 entries)

**Backing**: Identity / Metrics / Policies / Format / Subject Density populated from OpenAlex API and publisher author guidelines (high reliability). Soft Metadata authored from community / family-level knowledge rather than per-entry evidence harvesting.

**Composition** (152 entries):
- **Journals (132)**: 11 original HCI journals + 17 ScienceClaw-adapted entries (multidisciplinary / biology / medical) + 75 Phase 4 promotions (across all field directories) + 10 P3-2 high-leverage additions (Bioinformatics / NAR / Cell Reports / Nature Physics / PRR / 4 ACM HCI journals / TACL) + 19 P3-4 niche additions (3 biology / 1 multidisciplinary / 4 neuroscience / 7 psychology / 3 hci / 1 qual-methods)
- **Conferences (20)**: 8 HCI (ACM SIGCHI family) + 5 ML (NeurIPS-style) + 3 NLP (ACL family + ARR rolling review) + 2 Data Mining (KDD / WWW) + 2 P3-4 (ACM ASSETS / ACII)

**What Tier 2 means in practice**:
- Identity / Metrics / Policies are reliable (OpenAlex + publisher / conference CFP)
- Subject Density top topics are reliable (OpenAlex output for journals; CFP topic areas for conferences)
- **Reviewer Pool Characteristics, Framing Requirements, sensitive-topic receptiveness without article counts, and methodology receptiveness scores without numbered evidence are family-level community estimates**
- Each Tier 2 entry includes a visible warning banner in its Soft Metadata section
- Conference entries additionally use family-level (HCI / ML / NLP / Data Mining) Soft Metadata templates adapted from ScienceClaw `cs_conference_style.md`, `ml_conference_style.md`, `reviewer_expectations.md` (MIT)
- Estimated subjective-judgment uncertainty: ~40-50%

A representative example of Tier 2 calibration limits: a `topic_trend_scan.py` audit of TOCHI's last 5 years (374 publications) found 0 articles tagged `autoethnography`, even though the Tier 2 entry rated autoethnography receptiveness at 3/5 based on third-wave HCI generalizations. This is exactly the kind of gap Tier 2 banner contributors are invited to close.

## Why the distinction matters

Tier 1 entries can be used confidently in AI recommendation workflows. Tier 2 entries are useful for filtering and discovery (the structural data is reliable), but Soft Metadata reasoning should be cross-checked before committing to a submission decision.

The `fit_score.py` and recommendation workflow do not currently downweight Tier 2 entries automatically. AI agents using the skill should consider Tier 2 banners as a hedge when presenting recommendations.

## Upgrading a Tier 2 entry

Contributors are invited to help upgrade Tier 2 entries. Useful contributions:

1. **Run `scripts/topic_trend_scan.py`** against the journal with field-specific keywords; commit the resulting evidence into Subject Density / Sensitive Topics / Methodological Preferences with cited article counts.
2. **Replace community-estimate phrases** with evidence-backed statements once data is added (banner can be removed when most Soft Metadata fields carry specific cited evidence).
3. **Read recent reviewer reports** if you've published in or reviewed for the journal; add observations to Reviewer Pool Characteristics with personal-experience source notes.

Workflow:

```bash
# 1. Pick a Tier 2 entry to upgrade (any HCI journal)
# 2. Run a topic scan with field-relevant keywords
python scripts/topic_trend_scan.py --issn <issn> --years 5 \
    --keywords "autoethnography,critical HCI,AI ethics,embodied interaction"

# 3. Open the journal .md, replace pending or community-estimate values
#    with evidence-backed values (cite article counts)

# 4. Once Subject Density + Sensitive Topics + Methodological Preferences
#    all carry numbered evidence, remove the Tier 2 banner from the
#    Soft Metadata section

# 5. Validate
python scripts/validate_structure.py references/journals/hci/<your-entry>.md

# 6. Open a PR with the rationale for tier promotion in the description
```

A Tier 2 entry transitions to Tier 1 when:

- At least 5 of the 7 Soft Metadata subsections carry evidence-backed claims
- Reviewer Pool Characteristics references either OpenAlex publication patterns or personal experience as source
- The banner has been removed
- A maintainer review has approved the promotion

## What's not in this document (yet)

- Per-entry confidence breakdown beyond Tier 1 / Tier 2
- Automated tier-promotion detection (planned for a future `scripts/audit_tiers.py`)
- Cross-entry consistency checks (e.g. journals from the same publisher should share embargo policy unless one of them explicitly overrides)

## Metrics freshness

All quantitative metrics in the original 22 seed entries were sourced from OpenAlex on 2026-05-13 / 2026-05-14. Subsequent batches (Q1 expansion, ScienceClaw absorption, Phase 4 family-promotion, P3-1 conferences) were captured 2026-05-15 through 2026-05-17. Conference acceptance rates / submission cycle details for the 18 P3-1 entries are drawn from public CFP / conference websites (last verified 2026-05-17), not OpenAlex. `scripts/update_metrics.py` should be re-run monthly; we will schedule a GitHub Action after launch.

## Acknowledgments

This honest-disclosure framing was developed in dialogue with the founding author and the ChronicleCore expert system during pre-release quality review. See [AUTHORS.md](AUTHORS.md) for the full team.
