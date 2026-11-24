# Consumption Contract

How any AI agent — a Claude Code skill session, a claude.ai chat-mode skill
session, or this repo's own demo backend — must read and cite Journal Atlas
data. This is the single source for these rules. [SKILL.md](SKILL.md)'s
checklist, the chat-mode package, and the demo's synthesis prompt all point
here (or inline this file's text, where the caller has no file-read tool)
instead of restating the rules independently — restating them in three
places is exactly how they drift out of sync with each other.

For *why* the tiers exist, how the data was produced, and how to help
upgrade an entry, see [SEED_DATA_QUALITY.md](../../SEED_DATA_QUALITY.md).
This document only covers what to do with what you read, not how it was made.

## Recognize the tier before you cite anything

| Signal in the entry | Tier | What it means |
|---|---|---|
| No banner | **Sourced** | AI-researched, each claim cites a source — specific article counts, source URLs, dates. Not human-verified |
| `> [!WARNING]` in Soft Metadata | **Estimated** | Family-level estimate — not sourced per journal. Not human-verified |
| `> [!NOTE]` + a `signal_quality` score | **AI-Researched** | Per-journal AI research pass, cited sources, honest blanks where none existed |
| `> [!NOTE]`, Soft Metadata fields are placeholders | **Skeleton** | Structural data only (Identity / Metrics / Subject Density) — no Soft Metadata exists yet |

None of these tiers means a person has verified the entry. No entry carries a
first-hand account from someone who submitted to or reviewed for the journal
(none, as of 2026-11-23). Never describe Sourced as "human-verified" or Estimated as written or
checked by a community; say how the claims are sourced. (Until 2026-11-24 these were called
Tier 1 and Tier 2.) Scoring reads evidence
coverage, not the tier, so an Estimated score is built on estimates even when its
coverage figure is high.

Separately, `> [!CAUTION]` + **Disputed** marks a claim someone has formally
contested (see [docs/GOVERNANCE.md](../../docs/GOVERNANCE.md)). It is
**orthogonal to tier** — it can sit on any tier, and it names the specific
disputed field(s), so the rest of the entry still stands. Never present a
disputed claim as confidently as an undisputed one; say it's under dispute
and cite the linked issue.

## Rules

1. **Never state a placeholder as a fact.** `*(pending)*` and
   `*(fill manually)*` mean no one has written a real value yet — not "make
   a plausible estimate." Say "the entry doesn't specify" instead of
   guessing from training data.
2. **Cite the specific row, not the category.** Every claim — article
   count, h-index, embargo months, APC, reviewer-pool / framing /
   sensitive-topic receptiveness — needs a specific source in a file you
   actually read this session. If you can't point to one, don't make the
   claim.
3. **Say the tier out loud when it isn't Sourced.** Estimated → "family-level
   estimate, not per-journal evidence." AI-Researched → cite the per-field
   or overall `signal_quality` score and name any field the entry honestly
   left blank. Skeleton → say Soft Metadata doesn't exist yet; don't
   recommend on structural metadata alone.
4. **Don't rank by Impact Factor alone.** Soft metadata (reviewer culture,
   framing requirements, sensitive-topic tolerance) often matters more than
   IF for non-mainstream research.
5. **Check `Last verified`.** 18+ months old → warn that policy fields may
   have changed since.
6. **Only name journals whose file you actually read this session** — not
   from memory of the journal's general reputation.
7. **If a user disputes a claim, don't argue it yourself.** Point them to
   [docs/GOVERNANCE.md](../../docs/GOVERNANCE.md)'s dispute process — that's
   how a subjective claim actually gets corrected, not a conversational
   back-and-forth.
