# Entailment audit — do the cited sources actually say it?

**Run 2026-08-15. Sample n=30, seed 20260815. Auditor: automated retrieval + manual adjudication.**

Journal Atlas has a rule that no fact may be asserted without a source. That rule
prevents one failure and not its neighbour: it stops a claim with no citation, and
does nothing about a *real* citation that does not entail the claim drawn from it.
Nothing in the repository measured that second rate. This is the first measurement.

## What was sampled

The corpus contains 518 machine-checkable claim–source pairs across 358 of its 399
entries: places where a specific claim sits in a table next to a specific
`Source URL` (or under a `> Source:` line). They cluster in two sections — AI Policy
(317) and Peer Review (200) — because those are the two fields the pipeline was
built to cite per-venue.

30 pairs were drawn at random with a fixed seed (`scripts/../draw_sample.py`,
`random.seed(20260815)`), covering 28 distinct URLs across 5 fields. The sample size
is what the available time allowed, not a power calculation. At n=30 the 95%
confidence interval on any proportion reported below is roughly ±18 points, so these
figures locate an order of magnitude and nothing finer.

## Rubric

Each pair was given one verdict on retrieval and, where retrieval succeeded, one on
entailment:

| Verdict | Meaning |
|---|---|
| **Supported** | Source retrieved; it states or directly implies the claim |
| **Partial** | Source retrieved; it supports part of the claim, and the rest is on pages it links to |
| **Unsupported** | Source retrieved; it does not state the claim (absence, not contradiction) |
| **Dead** | URL returns 404 |
| **Not retrievable** | URL blocked to an automated client (403/402/405, bot challenge, or returns navigation chrome instead of content) |

A second, independent axis: was the weakness **declared** in the entry itself? The
corpus's provenance discipline is supposed to make thin evidence visible. Whether it
did is a separate question from whether the evidence was thin.

## Results

**Of the 19 pairs whose source could be retrieved, 15 were supported (79%).**

| Verdict | n | % of 30 |
|---|---:|---:|
| Supported | 15 | 50% |
| Partial | 1 | 3% |
| Unsupported | 2 | 7% |
| Dead (404) | 1 | 3% |
| Not retrievable | 11 | 37% |

### Finding 1 — the failures are not spread out; they are one template

*Findings below describe the corpus as audited on 2026-08-15. Action 1 has since
been applied; see Actions.*

Both unsupported claims, and the one dead link, came from the same Tier-2 conference
template. Four sampled conference entries (AAAI, ACM DIS, ACM CHI PLAY, TheWebConf)
carried a byte-identical AI Policy summary — as, it turned out, did 14 others:

> AI-assisted writing typically requires acknowledgment; AI listed as author
> prohibited; verify per-year CFP for the venue.

cited to the venue's own homepage or CFP. For **ACM DIS** the cited page does carry a
policy ("Text generated from a large-scale language model (LLM) … must be clearly
marked …"), so the claim is entailed. For **AAAI-26** the cited page says nothing
about AI at all. For **TheWebConf 2026** the cited URL 404s. And the field the
template filled — *"Has journal-specific AI policy?"* — was answered
*"Yes — most major conferences publish AI use disclosure policies (2023+)"*, which is
a generalisation about conferences, not a fact about the cited venue.

This is the exact failure the repository could not previously detect: a real URL,
resolving (sometimes), attached to a claim it does not support. The `Source URL`
field records *where someone looked*, and the schema silently reads it as *what the
claim rests on*.

### Finding 2 — 37% of cited sources cannot be retrieved by a machine at all

Eleven of thirty cited pages could not be read by an automated client on 2026-08-15:

| Publisher | Status |
|---|---|
| Wiley Online Library (×3) | HTTP 402 / Cloudflare bot challenge |
| ACM (acm.org, dl.acm.org) (×2) | HTTP 403 |
| Taylor & Francis | HTTP 403 |
| MIT Press (direct.mit.edu) | HTTP 403 |
| De Gruyter Brill | HTTP 405, then navigation chrome only |
| Oxford Academic | Returns subject-taxonomy menu, not policy text |
| ACM CHI PLAY | HTTP 403 |

Nature Portfolio and SpringerLink were reachable only after following an identity-provider
redirect that a naive fetch does not survive.

This is not a defect of the corpus. It is a property of the scholarly web, and it has
a consequence the corpus must own: **a provenance link the reader's agent cannot
follow is not, operationally, provenance.** Any project that cites publisher policy
pages inherits this, including every journal-recommendation tool that claims to work
from publisher data.

### Finding 3 — the declaration discipline mostly held

Five of the sampled entries flagged their own weakness in the entry text before this
audit ran, and all five were right:

- **The Monist** — "未能直接 WebFetch 到原始頁面全文（頁面對自動抓取回傳導覽選單而非正文）", `signal_quality` set to 2. The audit reproduced exactly that failure.
- **Information Technology and Disabilities** — "page itself unreachable 2026-07-13". Still unreachable.
- **IEEE Computer Graphics and Applications** — "依中文投稿社群回報，非官方頁面明文聲明". Confirmed: the cited page is an aggregator, carries the disclaimer "該作品系作者結合互聯網公開知識整合", and does not state a review type.
- **OMEGA** — "search-engine cached content; live fetch returned generic Sage shell". The claim (double-anonymized) is nonetheless verbatim correct.
- **Biological Psychiatry** — flagged one sentence as "摘自 AI 搜尋引擎聚合結果，未能定位到期刊官方頁面逐字確認".

The undeclared failures are the ones that matter: AAAI, TheWebConf, and six entries
whose sources are simply blocked without the entry saying so.

### Finding 4 — an internal inconsistency the audit surfaced incidentally

`clinical-psychology-review` and `biological-psychiatry` both defer to Elsevier's
publisher-wide policy and score its leniency differently (3 vs 2). Two entries citing
the same policy should not disagree about it.

## Where the supported claims were precise

Worth recording, because the failure cases are more quotable than the successes:

- **Emotion** — corpus: "double-masked (blind) review is optional and must be explicitly requested by authors at submission (opt-in, not default)". APA: "Masked reviews are optional, and authors who wish masked reviews must specifically request them when they submit their manuscripts."
- **Psychological Science** — corpus: "至少兩位編輯團隊成員閱讀已去識別化之稿件". Source: "at least two members of the editorial team read the manuscript before an initial decision".
- **Mind, Culture, and Activity** — corpus declines to label single- vs double-blind and says so; the source indeed says only "All submissions will be blind reviewed."
- **Erkenntnis**, **SLEEP**, **SAGE ×2**, **Elsevier ×2**, **UC Press**, **eWiC**, **OMEGA** — all confirmed against the cited page.

## Actions

**1. Retire the Tier-2 conference AI-policy template — DONE 2026-08-15.**
A field that says "most major conferences" is not a claim about the venue. All 18
entries carrying the template had their AI Policy claims withdrawn to `(pending)`
with the reason recorded in place, except ACM DIS, whose cited page does state a
policy; that one was filled in with the verbatim quote retrieved during this audit.
Withdrawing an unsupported claim needs no new research and cannot introduce a new
error, which is why it was safe to do immediately; re-estimating the other 17 would
have repeated the mistake being corrected. Conference AI policies are set per year,
so the recorded blank tells the reader to check the relevant year's call for papers.

Withdrawal reduced the checkable claim–source population from 518 pairs across 358
entries to **501 across 341**. Corpus validation: 399/399 structural pass, content
lint unchanged against baseline, and the scoring path is unaffected — the AI-policy
fields feed a hard-constraint gate rather than a scored dimension, so venues with a
now-`(pending)` gate stop being eliminated on absence of evidence, which is the
conservative behaviour.

**2. Separate `Source URL` (where someone looked) from `Evidence URL` (what the
claim rests on)** — not done. Touches the schema and all 399 entries.

**3. Record retrieval status alongside each source, and re-check on a schedule** —
not done. A 404 after thirteen months is not rare, it is the base rate.

**4. Reconcile the Elsevier leniency scores** — not done. 37 entries defer to
Elsevier's publisher-wide policy and at least two score its leniency differently
(3 vs 2); the full spread has not been measured.

Actions 2 and 3 are schema changes and are recorded here as the audit's output, not
as completed work.

## Reproducing this

```bash
python scripts/audit/sample_audit.py   # enumerate the 518 pairs
python scripts/audit/draw_sample.py    # seed 20260815 -> the same 30
```

Retrieval and adjudication were manual. The verdicts above are judgement calls and a
second auditor would not reproduce all thirty; the two unsupported cases and the dead
link are the ones that are not judgement calls.
