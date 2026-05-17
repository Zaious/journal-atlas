# Seed Data Quality & Confidence Tiers

> 🌐 **Languages**: English | *(Traditional Chinese version welcome via PR)*

This document explains how the seed journal entries were authored, the differences in evidentiary backing between them, and how the community can help upgrade lower-confidence entries.

We believe a community-maintained knowledge base only earns trust if it is honest about what it doesn't yet know. This page is that honesty.

## Two orthogonal dimensions

To avoid confusion, we track entry quality across **two independent axes**:

1. **Evidence Quality** (`Tier 1` vs `Tier 2`) — how trustworthy are the Soft Metadata claims that have been written?
2. **Completeness** (`Skeleton` vs filled) — has Soft Metadata been written at all, or is the entry still a structural scaffold?

A Skeleton entry has **no Tier assignment yet** because there's nothing to evaluate. Tier 1 / Tier 2 only apply once Soft Metadata has been authored.

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

## Current distribution (2026-05)

| State | Count | Banner | Where |
|-------|-------|--------|-------|
| **Skeleton** | 0 | `> [!NOTE]` | All Skeleton entries from earlier phases have been promoted to Tier 2 in Phase 4. |
| **Tier 2** | 121 | `> [!WARNING]` | 103 journals (originally HCI + ScienceClaw-adapted + Phase 4 promotions) + 18 conferences (HCI / ML / NLP / Data Mining family-adapted). Family-level claims; per-journal/per-conference evidence not yet collected. |
| **Tier 1** | 11 | none | The 8 psychology + 3 qualitative-methods entries with deep evidence harvesting from manuscript submission research |
| **Total** | **132** | | |

### Field-directory breakdown

| Field | Count | Notes |
|-------|-------|-------|
| `psychology/` | 53 | Includes cross-disciplinary phenomenology / cognitive-science venues |
| `hci/` | 23 | Added Nature Machine Intelligence + IEEE Access from ScienceClaw |
| `qualitative-methods/` | 4 | |
| `cognitive-science/` | 12 | |
| `multidisciplinary/` | 7 | Nature / Nature Comms / NHB / Science / Science Adv / PNAS / PLOS ONE |
| `biology/` | 9 | Cell Press family + PLOS Bio/Comp Bio + Nature Methods/Biotech |
| `medical/` | 5 | NEJM / Lancet / JAMA / BMJ / Annals of Internal Medicine |
| `physics/` | 1 | Physical Review Letters |
| `conferences/hci/` (new) | 8 | ACM CHI, CSCW, UIST, DIS, IUI, IDC, CHI PLAY, IEEE HRI |
| `conferences/ml/` (new) | 5 | NeurIPS, ICML, ICLR, CVPR, AAAI |
| `conferences/nlp/` (new) | 3 | ACL, EMNLP, NAACL |
| `conferences/data-mining/` (new) | 2 | KDD, WWW |
| **Total** | **132** | |

### Schema version

All 132 entries conform to **schema v1.3**, which introduces:
- **`Venue type`** required field in Identity (`Journal` / `Conference` / `Proceedings-Journal`)
- **`Conference Specifics`** required H2 section for `conferences/` subtree (4 sub-tables: Submission Cycle, Program Committee, Submission Format, Review Format) + Conference Calendar
- Path-aware validation: `validate_structure.py` enforces Conference Specifics only on `conferences/` entries.

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

### Tier 2 — Community estimate (121 entries)

**Backing**: Identity / Metrics / Policies / Format / Subject Density populated from OpenAlex API and publisher author guidelines (high reliability). Soft Metadata authored from community / family-level knowledge rather than per-entry evidence harvesting.

**Composition** (121 entries):
- **Journals (103)**: 11 original HCI journals + 17 ScienceClaw-adapted entries (multidisciplinary / biology / medical) + 75 Phase 4 promotions (across all field directories)
- **Conferences (18)**: 8 HCI (ACM SIGCHI family) + 5 ML (NeurIPS-style) + 3 NLP (ACL family + ARR rolling review) + 2 Data Mining (KDD / WWW)

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
