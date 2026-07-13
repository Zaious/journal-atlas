# WO1 + WO3 Merge — Gaps & Notes (2026-07-13)

## Coverage: zero gaps

All three target lists reached **100% coverage** — every journal in
`targets_psychology.json` (185), `targets_philosophy.json` (107), and
`targets_hci.json` (64) has a corresponding soft-metadata research entry.
Plus 1 bonus entry (Journal of Happiness Studies, ISSN 1389-4978) researched
in the original hand-picked batch1 but not present in any of the three
demand-ranked target lists — kept as extra coverage, not a gap.

| Domain | Target | Covered | Missing |
|---|---|---|---|
| Psychology | 185 | 185 | 0 |
| Philosophy | 107 | 107 | 0 |
| HCI | 64 | 64 | 0 |

7 journals are legitimately cross-listed across two domains (kept in both
domain views, not duplicated as separate research — same entry, tagged
`domains: [...]`): ACM Transactions on Interactive Intelligent Systems,
Applied Ergonomics, Interacting with Computers, Universal Access in the
Information Society (psychology+hci); Analysis, Mind, Phenomenology and the
Cognitive Sciences (psychology+philosophy).

## What "gap" actually means here: honest-blank distribution, not missing journals

The real gaps are inside entries — where the researching agent found no public
signal and correctly left the field blank per the WO2 honest-blank rule,
rather than where a journal is missing entirely.

**`overall_signal_quality` distribution:**

| Domain | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Psychology (185) | 3 | 21 | 118 | 39 | 4 |
| Philosophy (107, incl. cross-listed) | 1 | 24 | 60 | 18 | 1 |
| HCI (64, incl. cross-listed) | 0 | 5 | 41 | 14 | 0 |

Total `blanks[]` entries recorded (honest "no source found" notes, not
missing data — each one names the field and why): 867 (psychology) + 520
(philosophy) + 304 (HCI) = **1,691 honestly-blank field notes**. This is the
expected shape given the long-tail-cliff finding from the earlier prototype —
most of these low-signal journals are exactly the kind (niche, low
citation-volume, no English/Chinese forum discussion) predicted to cliff.

**Journals with `overall_signal_quality <= 1`** (thin — mostly policy-layer
facts only, little/no experiential signal) are listed in
`_low_signal_quality_list.txt` in this directory for anyone wanting to
prioritize a second research pass (e.g. via a different source angle, or
accept as permanently thin niche entries).

## Deduplication: 17 journals got two independent research passes

Some journals were researched twice — once in an earlier batch
(`batch1_psychology-core.json` or `psych-b*`/`hci-b*`) and again in the later
`retry-b*` continuation run, which appears to have re-covered a few journals
already done while also covering the remainder of all three target lists.
Kept the version with the higher `overall_signal_quality` (tie → prefer the
original `batch1_psychology-core.json` high-effort run). Full list of which
version was kept: see merge log (reproducible from
`scripts/spine/build_targets.py`-adjacent tooling; not persisted as a
separate file — the raw batch files below retain both versions if a re-check
is ever needed).

## Real gap found: 4 defunct/historical ISSNs slipped into the target lists

A stratified 25-entry compliance audit (across all `overall_signal_quality`
levels, all three domains) found the drafting agents' honest-blank discipline
held up well — every low-signal entry checked correctly cited sources, checked
Chinese sources even when the result was "0 found," and never invented a
plausible-sounding number. But 13 entries self-flagged (in `sensitive_topics_note`)
that their ISSN might belong to a discontinued/renamed/merged title. Most of
these are fine — a currently-active journal that happens to have a historical
former name (e.g. *Journal of Psychopathology and Clinical Science*, formerly
*Journal of Abnormal Psychology*, `sq=3`, correctly profiled under its current
identity). But **4 have `overall_signal_quality=0` and are genuinely dead
ISSNs with no live content to profile** — these slipped into
`targets_psychology.json` / `targets_philosophy.json` from either OpenAlex's
historical-works ranking or a stale ISSN in a repo-curated `.md` file:

| ISSN | Name | Status (per agent's research) |
|---|---|---|
| 0095-8891 | Journal of Consulting Psychology | Ceased 1968, became *Journal of Consulting and Clinical Psychology* (different ISSN) |
| 0022-1015 | Journal of Experimental Psychology | Split 1974/75 into the modern JEP:General/HPP/LMC/Applied/ABP family |
| 0033-3131 | Psychonomic Science | Ceased 1972 (Psychonomic Society) |
| 0028-6621 | The New Scholasticism | Renamed 1990 to *American Catholic Philosophical Quarterly* (different ISSN) |

**Action needed (not done in this pass):** drop these 4 ISSNs from the target
lists (or replace with their live successor's correct ISSN if the intent was
to profile the successor), and audit whether the same defunct-ISSN pattern
exists in the untouched majority of `consolidated_all.json` beyond this
25-entry sample — this was a spot-check, not an exhaustive sweep.

## Files in this directory

- **`consolidated_all.json`** — the deliverable. 350 unique journals
  (deduplicated), each tagged `domains: [...]`. Non-lossy master.
- **`consolidated_psychology.json` / `consolidated_philosophy.json` /
  `consolidated_hci.json`** — per-domain views filtered from the master
  (cross-listed journals appear in more than one view; this is intentional,
  not a duplicate).
- **`consolidated_bonus.json`** — the 1 out-of-scope-but-researched entry.
- **Raw batch files** (`batch1_psychology-core.json`, `psych-b*.json`,
  `phil-b*.json`, `hci-b*.json`, `retry-b*.json`) — kept as the audit trail /
  raw research output. Not the deliverable; superseded by `consolidated_*`.
- **`targets_*.json`** — the input target lists (unchanged, for reference).

## Not yet done (next decision point)

These consolidated JSON files are **research drafts**, not yet merged into
the permanent knowledge base (`references/journals/**.md`). Per
`docs/ATLAS_V2_DESIGN.md` §9, before merging into public-facing curated
entries the project still owes:
1. A quality/rule-compliance audit (facts-only, no verbatim, no unsourced
   subjective claims) — spot-checked a sample during this merge (see session
   notes), not yet 100% audited.
2. A dispute/rebuttal mechanism for subjective Layer-E claims (political
   leaning, reviewer culture) before public release.
3. For the ~165 journals with no existing `.md` file, new entries need to be
   scaffolded from the spine (`journal_spine.db`) for Identity/Metrics before
   the soft-metadata draft can be merged in — the two data layers (spine facts
   + soft-metadata draft) haven't been joined yet.
