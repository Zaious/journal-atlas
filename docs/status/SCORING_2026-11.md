# Scoring fix: topical relevance (2026-11-25)

## What was wrong

On the 493-entry corpus the screening ranked venues with no evidence of
topical relevance at the top. Re-recording the home page's product shot showed
it first: for a paper on older adults' use of voice assistants, *Minerva* (a
science-policy journal) and the *British Educational Research Journal* came
second and third. A six-query backtest showed it was systematic.

Three causes, each found behind the previous one:

1. **Missing or unreadable topic tables.** 25 entries had no usable Top Topics
   table (some listed topics by name with no count, written while OpenAlex was
   out of quota; `_extract_top_topics()` needs a count). Their relevance to any
   paper was *unknown*.
2. **Unknown relevance did not hold a venue down.** Without `topic_density`
   what remains are dimensions nearly every venue passes: nothing sensitive to
   accommodate scores 100, and budget and length fit.
3. **Zero relevance did not hold a venue down either.** Once unknowns were
   held at the prior, venues whose listed topics include *none* of the paper's
   rose instead: topic is a quarter of the weight and family-level estimates
   fill the rest at full marks (Computers and Composition at 71 for a paper on
   teacher feedback).

## The fixes

Two pull requests, made in parallel by two sessions and reconciled:

- **#6 (content session):** added the missing OpenAlex Top Topics tables to 25
  entries (cause 1), and held a venue with unknown topical relevance at or
  below the neutral prior when the paper names topics (cause 2).
- **#7 (site session):** extended that rule to zero relevance (cause 3). The
  score is capped at **50 + topic_density / 2**: no evidence of relevance
  (unknown or zero) keeps a venue at or below the prior, partial relevance
  lifts the ceiling part way (33 → 66.5), full relevance removes it. Like the
  shrinkage it only ever lowers a score, and it does not apply when the paper
  names no topics (then every venue's topic dimension is unknown for a query
  reason). #7 also reads topic tables that list names without counts (a match
  scores 50, a miss 0; placeholders and `*(community estimate)*` names are
  not read). After #6 no entry has such a table, so today this changes no
  ranking; it keeps the next batch written without counts from repeating
  cause 1. The vocabulary includes those names.

## Backtest

`python demo/backend/backtest_screening.py <label>`: six queries, topics taken
from `topic_vocabulary.json` the way the extraction stage aligns them (the
games query uses free phrases, a field the corpus barely covers). Count of the
top five that are topically relevant / unknown / zero:

| Query | Before both | After #6 | After #6 and #7 |
|---|---|---|---|
| HCI: older adults, voice | 0 / 5 / 0 | 3 / 0 / 2 | 3 / 0 / 2 |
| Education: teacher feedback | 1 / 4 / 0 | 1 / 0 / 4 | 4 / 0 / 1 |
| Philosophy: epistemology | 0 / 5 / 0 | 4 / 0 / 1 | 5 / 0 / 0 |
| Psychology: sleep, memory | 4 / 0 / 1 | 4 / 0 / 1 | 5 / 0 / 0 |
| Economics: labour, productivity | 0 / 0 / 5 | 0 / 0 / 5 | 1 / 0 / 4 |
| Games: toxicity | 0 / 5 / 0 | 0 / 0 / 5 | 0 / 0 / 5 |
| **Total of 30 places** | **5 / 19 / 6** | **12 / 0 / 18** | **18 / 0 / 12** |

The zero places that remain are in queries where the corpus holds fewer than
five relevant venues; they sit at or below 50, under every relevant one. That
is a coverage gap in the corpus, which the site already states, not a ranking
error.

Tests: `tests/test_fit_score.py` carries both sessions' tests.

## Not changed (open)

- **Estimated entries still count as evidence.** A family-level estimate fills
  a dimension the same way a sourced claim does (coverage 100% for Estimated,
  75% for Sourced, see `coverage_by_tier.py`). Whether estimates should weigh
  less is a separate decision for the maintainer.
- The weights themselves are still the educated guesses noted at
  `DEFAULT_WEIGHTS`; no backtest against known submission outcomes exists.
- The paper's numbers belong to tag `jcdl2026` and are unaffected.
