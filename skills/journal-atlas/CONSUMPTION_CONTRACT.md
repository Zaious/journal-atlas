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
| No banner | **Tier 1** | Evidence-backed — specific article counts, source URLs, dates |
| `> [!WARNING]` in Soft Metadata | **Tier 2** | Community / family-level estimate — no per-claim evidence yet |
| `> [!NOTE]` + a `signal_quality` score | **AI-Researched** | Per-journal AI research pass, cited sources, honest blanks where none existed |
| `> [!NOTE]`, Soft Metadata fields are placeholders | **Skeleton** | Structural data only (Identity / Metrics / Subject Density) — no Soft Metadata exists yet |

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
3. **Say the tier out loud when it isn't Tier 1.** Tier 2 → "community
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
