<!-- design-doc: v2 | drafted: 2026-07-13 | status: proposed -->

# Journal Atlas v2 — Coverage-First, AI-Bootstrapped Architecture

> **Status**: Proposed design (2026-07-13). Supersedes the implicit v1 model
> (curated, personal-experience-gated entries). Grounded in four verification
> workflows run 2026-07-13; source access/license facts are cited inline and
> summarized in [§6 Source Catalog](#6-source-catalog).

---

## 1. Why this pivot

v1 treated **first-hand submission experience** as the quality gate: soft
metadata was only "Tier 1" once the maintainer (or a contributor) had actually
submitted to the journal. The result after one intensive build sprint: **163
entries, only 11 evidence-backed** — far below the ~50,000 active journals a
usable atlas needs. At that volume, coverage-driven usability is effectively
zero.

The diagnosis: we applied a **precision product's** quality bar to what is
inherently a **recall product**. A map's value is breadth with honest
confidence, not per-cell certification. Wikipedia was not written by
eyewitnesses; it was seeded from public sources with provenance and corrected
over time.

**v2 reframes the product:**

| | v1 (implicit) | v2 (this doc) |
|---|---|---|
| Primary goal | Per-journal certified accuracy | Broad coverage + honest confidence |
| Soft-metadata origin | Lived experience (gate) | AI-bootstrapped from public sources; experience is the *top* tier, not the *entry* gate |
| Empty fields | Blocker | First-class, labeled `signal_quality` |
| Scale | 10s–100s | Spine ~228k (OpenAlex), deep subset demand-tiered |
| Trust mechanism | "we submitted here" | Provenance URL + snapshot date on every fact; correct-on-report |

This does **not** lower honesty — it raises it. Every fact carries a source and
a date; unknowns are stated as unknowns instead of quietly missing.

---

## 2. The layered model

Soft/semi-soft metadata splits into three layers with **very different
recoverability, cost, and legality**. Treat them separately; do not promise the
expensive layer uniformly.

### Layer S — Structural / Ranking (cheap, scalable, deterministic)
Identity, metrics, indexing status, quality tiers. **Never AI-answered** —
imported from authoritative sources, ISSN-keyed, snapshot-dated. This is the
[spine](#5-data-model) and the first thing built. See [§6.1](#61-structuralranking-importers).

### Layer P — Positioning / Scope (scalable, mostly free)
What the journal actually accepts *now*. Recoverable even for the long tail:
- **Default (free, no LLM):** OpenAlex per-source `topics` / `topic_share` —
  precomputed, ~100% source coverage, CC0.
- **Deep (demand-tiered):** LLM synthesis over a sample of recent article
  `title + abstract`. OpenAlex abstracts are an `abstract_inverted_index` (CC0,
  reconstructable) with ~83% coverage on recent journal articles, ~60% overall,
  ~45% pre-2000, and known publisher gaps (Elsevier pulled closed-access
  abstracts 2024-11; Springer Nature ~48%). Abstracts help most for *method /
  framing*, which titles hide.
- **Current signals:** special-issue CFPs + new-editor editorials + taglines —
  fresher than static aims&scope, usually unwalled. See [§6.3](#63-current-signals).

### Layer E — Experiential (most wanted, least recoverable, honest-blank on the tail)
Acceptance difficulty, review speed, reviewer behavior, desk-reject patterns.
- **Cross-language is the moat.** Chinese sources (小木虫, fabiaoji, 知乎) are
  often *richer* than English for journals Chinese scholars target — a mid-tier
  journal scored higher signal (4/5) than a flagship (3/5) in prototype purely
  from Chinese forums. Western competitors structurally miss this.
- **The long-tail cliff is real and universal.** Every English/Chinese forum
  discusses famous or notorious journals; obscure journals return near-zero.
  Prototype long-tail journal: LetPub 0 reviews, SciRev 0 reviews, forums 0.
- **Rule:** with no first-hand source, the field stays **blank + `signal_quality`
  scored**. Generic filler is forbidden — the honest blank *is* the feature, and
  "0 reviews on LetPub/SciRev" is itself a recordable signal.

---

## 3. The unifying rule: **facts, not verbatim**

One legal/architectural line runs through all three layers and simplifies the
whole system:

- **Facts** (review took 3 months; journal has N retractions; word limit 8000;
  CFP deadline 2026-09-01; JUFO level 2) are **not copyrightable** (Feist) →
  **bake into the repo** with source + date.
- **Verbatim prose** (forum posts, policy text, full abstracts, CFP
  descriptions) is copyrighted and often license-incompatible with CC BY-SA →
  **query-time only, or rewritten short summaries.**

**Therefore: the repo stores normalized facts + source URLs. Anything verbatim
is fetched live.** This single rule resolves copyright, CC BY-SA
compatibility, *and* the "AI makes things up" complaint at once — because every
stored cell is a sourced fact, not a paraphrase or a guess.

---

## 4. Ingestion modes

Each source is either **bake-in** (facts stored in the repo/spine) or
**query-time** (fetched live at recommendation time, not persisted).

```
                    ┌──────────────────────────────┐
  BAKE-IN  ──────►  │  spine DB (ISSN-keyed facts)  │  ◄── the KB the skill reads
  (CC0 / CC BY-SA / │  + curated markdown entries   │
   facts-only)      └──────────────────────────────┘
                                 ▲
                                 │ enrich on demand
  QUERY-TIME ───────────────────┘
  (NC / ARR / UGC sources: SciRev, Reddit, Sherpa, SJR, PubPeer)
  → fetch live, show fact + link, do NOT persist verbatim
```

---

## 5. Data model

Two tiers of storage, not one:

1. **Spine** — a database (SQLite / Parquet / JSONL), **ISSN-L keyed**, one row
   per journal, holding Layer-S facts + Layer-P `topics` for **all ~228k**
   journals. Machine-generated, cheap, refreshable. *This replaces the idea of
   228k markdown files, which would be unmanageable.*
2. **Curated entries** — the existing `references/journals/**.md` files, for the
   **deep subset** that has real Layer-E/P depth. These are the human- and
   AI-authored soft-metadata write-ups.

The skill reads the spine for breadth (filter/rank across everything) and the
markdown entries for depth (soft metadata on the shortlist).

### Per-field provenance
Every fact stores `{value, source, source_url, as_of}`. The spine keeps a
`provenance` JSON column; markdown entries keep inline source tags (already the
convention in v1 soft-metadata tables).

### Confidence labeling (replaces the Tier gate)
`signal_quality` (0–5) per soft-metadata **field group**, not a per-entry gate:

| Score | Meaning |
|---|---|
| 5 | First-hand experience (SciRev n≥5, submission reports, article-count evidence) |
| 3–4 | Multiple public discussions synthesized (incl. cross-language) |
| 1–2 | Publisher-level policy inherited / scope inferred from titles only |
| 0 | No public signal — **field left blank, labeled, not filled** |

The old `Tier 1` becomes "signal_quality 5" — the *ceiling*, not the *turnstile*.

---

## 6. Source catalog

Verdicts from 2026-07-13 verification workflows. 🟢 bake-in + license-compatible ·
🟡 conditional · 🔴 query-time only / excluded.

### 6.1 Structural / ranking importers
| Source | Verdict | License | Coverage | Fills | How |
|---|---|---|---|---|---|
| **OpenAlex** sources | 🟢 | CC0 | ~228k journals | Identity, metrics, topics, OA/APC | Anonymous S3 snapshot `s3://openalex/data/jsonl/sources/` (no key); API for single/incremental |
| **DOAJ** | 🟢 | CC BY-SA 4.0 (**same as us**) | ~22k OA | OA/APC/license, peer-review type, scope | Free CSV `doaj.org/csv` / API |
| **JUFO** (FI, 0–3) | 🟢 | CC BY 4.0 | 42,670 channels | JUFO level **+ Norway/Denmark level + SJR + SNIP + Sherpa code** per record | `massa.json.zip` nightly; `kanava/{id}` per-ISSN |
| **Norwegian Register** (0–2) | 🟢 | CC BY 4.0 / NLOD | ~40k | Norwegian level | CSV `kanalregister.hkdir.no/.../tidsskrift` |
| **CAS 中科院分区** (一–四区) | 🟢 (fact via mirror) | data © CAS; mirror code GPL/MIT | 21,773 | 大类/小类 zone, Top | `hitfyd/ShowJCR` `FQBJCR2025-UTF8.csv` — **frozen 2025, static** |
| **Scopus** inclusion + ASJC | 🟢 | © Elsevier, free file | ~47k sources | in-Scopus, subject | monthly `ext_list_*.xlsx` via content page |
| **Retraction Watch** DB | 🟢 | CC0 | all | retraction count/reasons (integrity flag) | GitLab `retraction_watch.csv`, daily. **Name-keyed, no ISSN — fuzzy join** |
| **ABDC** (AU business) | 🟢 | © ABDC, free | ~2.7k | tier A*–C | xlsx |
| WoS index (SCIE/SSCI/ESCI) | 🟡 | Clarivate | ~24k | index membership | MJL undocumented `rank-search` (fragile) or logged-in Excel |
| **JIF number / JCR quartile** | 🔴 | subscription | — | — | **paywalled — AI's #1 error source.** Proxy: OpenAlex 2yr-citedness / SJR / CiteScore, *labeled not-JCR* |
| SJR + quartile | 🟡 | **NC** (clashes CC BY-SA) + Cloudflare | ~32k | SJR, quartile | query-time reference only; or JUFO's `SJR_SJR` field |
| CiteScore | 🟡 | Elsevier | all Scopus | CiteScore | free-key Serial Title API / sources page |
| 北大核心 / CSSCI / CSCD | 🟡 | © respective bodies | ~2k–1.5k | Chinese-core membership | EasyScholar free-key API + university-library mirror PDFs |
| ABS/CABS AJG (UK business) | 🔴 | login-walled | ~1.8k | — | proxy: Norwegian + ABDC |
| Sherpa Romeo / Jisc | 🔴 | CC BY-NC-ND (NC) | ~28k | OA/preprint policy | query-time link-out only |

> **CC BY-SA consequence:** bakeable *quality tiers* are the level-based systems
> (JUFO / Norwegian / CAS / ABDC), **not** the quartile systems (SJR / CiteScore /
> JIF — all paywalled or NC). Serve quartiles as query-time references.

### 6.2 Experiential sources
| Source | Verdict | Note |
|---|---|---|
| **Retraction Watch** | 🟢 CC0 | integrity signal, bake-in (see above) |
| **Academia StackExchange** | 🟡 CC BY-SA | use **community archive.org mirror** (official dump added an anti-LLM clause 2024-07); thin per-journal → general red-flag corpus, not journal facts |
| **SciRev** | 🔴 ARR + EU DB right | best structured first-hand (review time / desk-reject % / accept %) — **extract individual facts, never copy the DB**; query-time |
| **Reddit** | 🔴 UGC | 2026: OAuth, 100 QPM free, non-commercial, must honor deletions → query-time only, no persistence |
| **EconJobRumors** | 🟡 UGC | rich for economics (has a Journal Submission Wiki), econ-only |
| **PubPeer** | 🔴 keyed API, ARR | query-time counts + links only |
| **小木虫 / fabiaoji / 知乎** | 🟡 UGC | **highest-value non-English**; facts only, query-time / rewritten |
| non-CN/non-EN forums | 🔴 | predatory-broker spam; not usable |

### 6.3 Current signals (Layer P + P)
| Source | Verdict | Note |
|---|---|---|
| **Frontiers Research Topics** | 🟢 (facts) | bot-friendly, ~50k topics, structured special-issue CFPs |
| **WikiCFP** | 🟡 CC BY-SA 3.0 (compatible) | HTTP-only, RSS/sitemap, CS/eng-skewed; bake-in facts only |
| **T&F call-for-papers** | 🟡 | public, query-time / facts |
| new-editor editorials | 🟡 | via PMC / Europe PMC OA full text; extract vision/priorities |
| MDPI / ScienceDirect CFPs | 🔴 (eng) | Cloudflare bot wall → headless or query-time |
| **ICORE** | — | *conference ranking*, not a CFP aggregator (corrects an earlier assumption) |

---

## 7. Fetching & anti-wall notes

- **Headless browser is mostly unnecessary.** APA/T&F/Springer policy pages that
  403'd are not auth walls — the causes were a missing browser `User-Agent`
  (T&F Cloudflare) and an unpreserved cookie/redirect handshake (Springer →
  `idp.springer.com`). A **hardened HTTP client (browser UA + cookie jar +
  follow redirects + gzip)** opens all three; APA opens to plain `curl`.
  Reserve headless as a narrow fallback for T&F's occasional managed challenge.
- **Publisher-level modeling + inherit.** Model ~20 big publishers' policies
  once from their public pages; journals inherit unless a journal-specific
  policy is found. This sidesteps most per-journal walls.
- **Respect robots.txt, rate-limit, cache.** Cloudflare on T&F is
  reputation-adaptive; hammering *raises* the wall.
- **OpenAlex:** bulk via anonymous S3 (no key); the 2026-02 API-key/credit
  system only constrains the REST API. Set a `mailto` for the polite pool.

---

## 8. Roadmap

- **Phase 1 — Spine (this cycle).** Build the ISSN-keyed importer joining the
  six no-caveat green sources: OpenAlex + DOAJ + JUFO(+Norway/SJR/SNIP/Sherpa) +
  Norwegian + CAS + Retraction Watch. Output: `journal_spine.db`. Runnable in
  sample mode (live per-ISSN) and full mode (bulk). → `scripts/spine/`.
- **Phase 2 — Positioning.** Fold OpenAlex `topics` into the spine; add the
  current-signals fetchers (Frontiers/WikiCFP/PMC).
- **Phase 3 — Experiential (demand-tiered).** Facts-only pipeline: SciRev +
  Chinese forums fact extraction at query-time; `signal_quality` scoring;
  honest-blank enforcement.
- **Phase 4 — Query surface (done, 2026-07-20).** Point the skill at the spine
  for breadth (filter/rank across all journals) and curated markdown for
  depth. → `scripts/query_spine.py`, cross-referenced against the curated set
  via `in_curated_kb`; SKILL.md's Query Mode routes breadth questions there.
- **Phase 5 — Governance & release.** Soft-metadata dispute/rebuttal mechanism;
  OPSEC de-fingerprinting of examples; push the pending license commit; make the
  GitHub repo public.

---

## 9. Open decisions & risks

1. **Reputational / defamation governance** for subjective Layer-E fields
   (political leanings, reviewer culture). Needs: mandatory source citation, a
   rebuttal/dispute issue path, and a "no unsourced subjective claim" rule.
   *Blocking for public release, not for the spine.*
2. **OPSEC.** v1 examples embed the founder's paper fingerprint (§10.6 of the
   original work order). De-fingerprint before public release.
3. **License consistency.** A local commit upgraded content to CC BY-SA 4.0 but
   was never pushed; GitHub still shows CC BY-NC-SA. Push it before release.
4. **OpenAlex credit budget.** Full spine via S3 snapshot (no key); reserve the
   keyed API for incremental single-ISSN refresh.
5. **Retraction Watch join is name-based** (no ISSN column) — accept fuzzy
   matching and flag low-confidence matches rather than asserting.
6. **Spine ≠ recommendation engine.** The spine holds facts; ranking weights
   stay user-controlled per the original scope boundary.
