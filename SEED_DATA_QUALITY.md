# Seed Data Quality & Confidence Tiers

> 🌐 **Languages**: English | *(Traditional Chinese version welcome via PR)*

This document explains how the initial 22 seed journal entries were authored, the differences in evidentiary backing between them, and how the community can help upgrade lower-confidence entries.

We believe a community-maintained knowledge base only earns trust if it is honest about what it doesn't yet know. This page is that honesty.

## Confidence tiers

Each journal entry under `skills/journal-atlas/references/journals/` was authored through a structured process. The depth of evidentiary backing varies by source:

### Tier 1 — Evidence-backed (14 entries)

**Backing**: Deep evidence harvesting via author submission research + targeted OpenAlex topic queries + reading of recent publications + publisher policy primary sources.

**Entries**:

| Field | Journals |
|-------|----------|
| psychology (8) | Collabra: Psychology, Culture & Psychology, Frontiers in Psychology, New Ideas in Psychology, Phenomenology and the Cognitive Sciences, Review of General Psychology, Self and Identity, Theory & Psychology |
| qualitative-methods (3) | Cultural Studies ↔ Critical Methodologies, Qualitative Inquiry, Qualitative Research in Psychology |
| *implicit*: 3 of the 11 HCI entries received partial Tier 1 evidence from HCI Venue Map work, but all 11 are tagged Tier 2 below pending broader validation. |

**What Tier 1 means in practice**:
- Soft Metadata claims often include specific article counts ("48 articles on self-state ecosystem 2020–2025") with source attribution
- AI Policy, Word Limit, Embargo, OA APC pricing all sourced from publisher author guidelines (with retrieval dates)
- Reviewer pool characteristics and framing requirements informed by recent publication patterns and (where available) published reviewer reports
- Estimated subjective-judgment uncertainty: ~15%

### Tier 2 — Community estimate (11 entries)

**Backing**: Identity / Metrics / Policies / Format / Subject Density populated from OpenAlex API and publisher author guidelines (high reliability). Soft Metadata authored from community knowledge of HCI as a field rather than journal-specific evidence harvesting.

**Entries**: All 11 HCI journals
- ACM Interactions, ACM Transactions on Computer-Human Interaction (TOCHI), AI and Society, Behaviour & Information Technology, Computers in Human Behavior, Frontiers in Computer Science, Human-Computer Interaction (Journal), Human Factors, Interaction Studies, International Journal of Human-Computer Interaction, International Journal of Human-Computer Studies

**What Tier 2 means in practice**:
- Identity / Metrics / Policies are reliable (OpenAlex + publisher guidelines)
- Subject Density top topics are reliable (OpenAlex output)
- **Reviewer Pool Characteristics, Framing Requirements, sensitive-topic receptiveness without article counts, and methodology receptiveness scores without numbered evidence are community estimates**
- Each Tier 2 entry includes a visible warning banner in its Soft Metadata section
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

All quantitative metrics in the 22 seed entries were sourced from OpenAlex on 2026-05-13 / 2026-05-14. `scripts/update_metrics.py` (run dry-run on 2026-05-14) found no significant metric drift beyond formatting differences. Re-running this script monthly is recommended; we will set up a scheduled GitHub Action after launch.

## Acknowledgments

This honest-disclosure framing was developed in dialogue with the founding author and the ChronicleCore expert system during pre-release quality review. See [AUTHORS.md](AUTHORS.md) for the full team.
