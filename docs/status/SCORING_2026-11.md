# Scoring fix: topical relevance (2026-11-25)

## What was wrong

On the 493-entry corpus the screening ranked venues with no evidence of
topical relevance at the top. Re-recording the home page's product shot showed
it first: for a paper on older adults' use of voice assistants, *Minerva* (a
science-policy journal) and the *British Educational Research Journal* came
second and third. A six-query backtest showed it was systematic, not one
example.

Two causes, one behind the other:

1. **Topic tables read as empty.** 12 entries list their topics by name only
   (`n/a (name only)`, `not stated`), written while OpenAlex was out of quota.
   `_extract_top_topics()` needs a count, so those tables were read as "no
   topic data" and the venue's relevance to any paper became *unknown*.
   A further 30 entries have no topic data at all (the 20 conferences point to
   their call for papers; 10 entries record that nothing was fetched).
2. **Unknown or zero relevance did not hold a venue down.** With
   `topic_density` unknown, the dimensions left are ones nearly every venue
   passes: nothing sensitive to accommodate scores 100, and budget and length
   fit. Once that was fixed, venues whose listed topics include *none* of the
   paper's rose instead, because topic is a quarter of the weight and
   family-level estimates fill the rest at full marks.

## The fix (`skills/journal-atlas/scripts/fit_score.py`)

- `_extract_topic_names()` reads topics listed by name without a count. A
  paper topic matching one scores `NAME_ONLY_TOPIC_MATCH` (50: relevant,
  size unknown; a counted match reaches 100). A paper topic matching none of a
  venue's listed topics scores 0, because the list is evidence. Placeholder
  rows and `*(community estimate)*` names are not read: an estimated topic is
  not evidence.
- `compute_score()` caps the score at **50 + topic_density / 2**. No evidence
  of relevance (unknown or zero) keeps a venue at or below the neutral 50;
  partial relevance lifts the ceiling part way (33 → 66.5); full relevance
  removes it. Like the existing shrinkage it only ever lowers a score.
- `build_topic_vocabulary.py` includes the name-only topics, so the
  extraction stage can align a description to them.

## Backtest

`python demo/backend/backtest_screening.py <label>`: six queries, topics taken
from `topic_vocabulary.json` the way the extraction stage aligns them (the
games query uses free phrases on purpose, a field the corpus barely covers).
Count of the top five that are topically relevant / unknown / zero:

| Query | Before | After |
|---|---|---|
| HCI: older adults, voice | 0 / 5 / 0 | 3 / 2 / 0 |
| Education: teacher feedback | 1 / 4 / 0 | 2 / 0 / 3 |
| Philosophy: epistemology | 0 / 5 / 0 | 5 / 0 / 0 |
| Psychology: sleep, memory | 4 / 0 / 1 | 5 / 0 / 0 |
| Economics: labour, productivity | 0 / 0 / 5 | 1 / 0 / 4 |
| Games: toxicity | 0 / 5 / 0 | 0 / 0 / 5 |
| **Total of 30 places** | **5 / 19 / 6** | **16 / 2 / 12** |

The unknown and zero places that remain are in queries where the corpus holds
fewer than five relevant venues; they sit at 50, below every relevant one.
That is a coverage gap in the corpus, which the site already states, not a
ranking error.

Tests: `tests/test_fit_score.py` gains five; four of them fail on the scorer
before this change.

## Not changed (open)

- **Estimated entries still count as evidence.** A family-level estimate fills
  a dimension the same way a sourced claim does (coverage 100% for Estimated,
  75% for Sourced, see `coverage_by_tier.py`). Whether estimates should weigh
  less is a separate decision for the maintainer.
- The weights themselves are still the educated guesses noted at
  `DEFAULT_WEIGHTS`; no backtest against known submission outcomes exists.
- The paper's numbers belong to tag `jcdl2026` and are unaffected.
