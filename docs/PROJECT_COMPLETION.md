# What "Finished" Looks Like

The ideal end state for Journal Atlas, independent of any conference
deadline. For the much narrower question of what a JCDL demo submission
needs, see [JCDL_DEMO_READINESS.md](JCDL_DEMO_READINESS.md) — most of what
follows is explicitly *not* required for that.

Status: written 2026-07-27 against the state of `main` at that date.

---

## 0. The honest framing

A community-maintained knowledge base does not have a finish line the way a
paper does. It has a **threshold past which it sustains itself**: enough
coverage that people find their journal in it, enough evidence quality that
they trust what they find, and enough contribution machinery that fixing an
error is easier than complaining about it.

So "finished" here means *self-sustaining*, not *complete*. A version of this
project where the maintainer must personally author every entry forever is a
failed version regardless of how many entries it has.

The graveyard is real and worth naming: Transpose and the CWTS Journal
Observatory were both credible, both crowdsourced, and both died. The
difference this project is betting on is an automated pipeline that keeps the
structural layer fresh without human effort, so that scarce human effort goes
only where it is irreplaceable — the subjective layer.

## 1. Coverage

**Now**: 399 entries across 9 field directories plus conferences. Three
demand-ranked target lists (psychology, philosophy, HCI) at 100%.

**Finished**:

- The fields a user is likely to arrive from are covered densely enough that
  "my journal isn't in here" is rare rather than typical.
- Adding a new field is a documented, repeatable operation — `build_targets.py`
  already generalises to any OpenAlex field/subfield, and the known traps are
  recorded in its comments (misclassified low-volume sources; print/online
  ISSN double-counting; defunct titles in demand rankings).
- The breadth layer answers "is this journal even known to us" for essentially
  any ISSN, which the 166,821-row spine already does.

**Deliberately not a goal**: covering every journal in existence with curated
depth. The spine provides breadth; curated markdown provides depth; conflating
the two is how this project would drown.

## 2. Evidence quality

This is the dimension with the furthest to go, and the one that determines
whether the project is genuinely useful or merely plausible.

**Now**: 11 Tier 1 · 152 Tier 2 · 236 AI-Researched. 312 high-confidence
scores rest on contentless justifications. Most AI-Researched entries sit at
`signal_quality` 2/5 — policy and positioning facts, thin-to-no experiential
signal.

**Finished**:

- **No high-confidence claim without checkable evidence.** A 4-5 receptiveness
  score or a "High" sensitive-topic rating carries a count, a URL, or a named
  source — never "Family norm". The linter already detects the gap and CI
  already blocks new instances; the remaining work is the 312-item backlog.
- **The tail is honest rather than filled.** Entries with no available public
  signal say so. This is already the discipline; it needs to survive scale.
- **Experiential data exists for the venues people actually submit to.** This
  is the layer no automation can produce — it comes from submission-experience
  reports, and it is the project's real moat. A Journal Atlas whose Tier 1 set
  is still 11 entries is not finished no matter what else is true.

**The honest constraint**: automated counting can prove absence and rarity but
can never confirm high receptiveness — counts measure published output, not
what an editor would accept. That asymmetry is already encoded in the tooling
and cannot be engineered away. The gap it leaves is exactly the gap community
contribution has to fill.

## 3. Validation

**Now**: none. `fit_score.py`'s weights are, by its own docstring,
"educated guesses" never checked against real outcomes.

**Finished**:

- A backtest set of real submissions with known outcomes, large enough to say
  something about whether the ranking is informative.
- Scoring weights tuned against that set rather than assumed.
- Published accuracy characterisation, including where the tool is *not*
  reliable — a matcher that says "I don't know enough about this journal to
  rank it" is more useful than one that always produces a number.
- Hard-constraint elimination verified as precision-oriented: wrongly
  eliminating a viable venue is a worse failure than ranking it too low,
  because the user never sees it to overrule.

**Measured evidence coverage (2026-07-30)**, after implementing the two
dimensions that previously returned nothing: the corpus splits cleanly along
the tier boundary rather than degrading evenly.

| Group | n | Coverage |
|---|---|---|
| Tier 1 + Tier 2 | 163 | 85-100% — scored on all or nearly all dimensions |
| AI-Researched | 236 | ~40% — topic density and sensitive topics only |

The 236 are missing exactly the four dimensions the v2 coverage-first pass
deliberately left as honest blanks: methodology receptiveness, reviewer pool,
voice, and strategic notes. So the ranking is fully evidenced for 41% of the
corpus and topic-only for the rest, which is the coverage-versus-depth
trade-off made visible in the scoring rather than hidden by it. Closing it is
§2's work, not a scoring change.

Until this exists, every recommendation is a plausible guess with good
provenance, which is better than most tools but is not the same as a
validated one.

## 4. Trust and governance

Largely done — the piece most projects skip and the one that makes subjective
metadata about real organisations defensible at all.

**Now**: dispute policy adopted, `Disputed` marker implemented and surfaced,
consumption contract canonicalised and referenced by every consumer,
response-time commitment stated publicly.

**Finished**:

- The dispute path has been exercised at least once end to end, so it is a
  process rather than a document.
- The response-time commitment is one the maintainer can actually sustain at
  whatever volume arrives — revised honestly downward if not, rather than
  quietly missed.
- Disputes and their resolutions are visible, so the correction history is
  itself evidence of good faith.

## 5. Freshness

**Now**: monthly metrics refresh scheduled via GitHub Actions, opening a PR
rather than committing. Defunct-journal screening exists but requires human
verification (its automated verdict had a >30% false-positive rate, and OpenAlex
indexes small/humanities/non-English venues poorly — precisely the journals
this project is most useful for).

**Finished**:

- Structural data never silently rots — stale entries are visible as stale.
- `Last verified` dates are meaningful, and the skill's 18-month staleness
  warning fires on real staleness rather than on everything at once.
- Ceased and renamed journals are caught within a reasonable window, with
  successors named. Note where this actually matters: skill evals (2026-07-30)
  found a strong model already knows these cessations unaided — it knew
  Psychonomic Science ended in 1972 and that The Modern Schoolman became Res
  Philosophica in 2013, including the continued volume numbering. The banners
  earn their keep on the **deterministic** path, where `fit_score.py` and
  `similar_journals.py` have no world knowledge at all and did rank both
  ceased titles as top candidates in that same run.
- Policy changes at publisher level (an AI policy revision, an OA conversion)
  propagate without waiting for someone to notice. This one is genuinely hard
  and may stay manual.

## 6. Contribution machinery

The dimension that decides whether §2 is ever reachable.

**Now**: issue templates for adding, updating, disputing, and reporting a
submission experience; contributor skill and slash commands; CI that gives a
contributor immediate feedback.

**Finished**:

- A researcher who has just been rejected can turn that experience into a
  merged contribution in one sitting, without reading the schema.
- Contributions arrive without the maintainer soliciting each one.
- The upgrade path from Tier 2 to Tier 1 is walked by people who are not the
  maintainer.
- Review of incoming contributions does not require the maintainer to
  personally verify every claim — the evidence discipline is legible enough
  that reviewers can check it.

## 7. Technical

**Now**: 64 tests, CI on every push, content linter with a frozen baseline,
regex-based markdown parsing.

**Finished**:

- The parsing layer is not the fragile part of the system. Two severe,
  long-lived bugs have already come from regex-parsing markdown — an
  AI-policy check that matched a template label and defaulted the whole
  corpus, and a topics parser that silently returned nothing for 57 entries.
  Both are now test-covered, but the underlying fragility is structural: a
  parsed-once JSON index with parsing warnings surfaced, rather than every
  consumer re-parsing prose, is the durable fix.
- Adding a consumer does not mean reimplementing extraction. Centralising
  `detect_tier` and `extract_h2_block` was a step; the parse layer is the rest.
- The demo is deployed, rate-limited, and reachable without running anything
  locally.

## 8. Reach

**Now**: private repository, never released.

**Finished**:

- Public, installable from the marketplace, and working in Claude Code,
  claude.ai chat mode, and the hosted demo.
- Cited or used by people with no connection to the maintainer.
- The soft-metadata schema is reusable by adjacent projects — the schema
  arguably matters more than this specific corpus, since anyone can rebuild a
  corpus but agreeing on what soft metadata *is* is the harder problem.

---

## Ranked: what actually moves the needle

If effort were spent strictly in order of how much it changes whether this
project is worth using:

1. **Validation (§3).** Without it every claim about usefulness is a
   hypothesis. This is the single largest gap.
2. **Experiential evidence depth (§2).** The moat. 11 Tier 1 entries is not a
   knowledge base, it is a proof of concept with a large scaffold around it.
3. **Contribution machinery working without solicitation (§6).** The only
   mechanism by which §2 scales past one person.
4. **Public release (§8).** Nothing above matters while the repository is
   private.
5. **Structural robustness (§7).** Prevents silent regressions from eroding
   trust that §1–§4 built.
6. **Coverage breadth (§1).** Already the most advanced dimension; further
   effort here has the lowest marginal return.

The uncomfortable implication of that ordering: the project's most-developed
dimension is its least valuable remaining one, and its least-developed
dimension is its most valuable. Coverage was the right thing to build first —
it made everything else possible — but continuing to add entries is now the
easiest way to feel productive while the things that decide the project's fate
stay untouched.
