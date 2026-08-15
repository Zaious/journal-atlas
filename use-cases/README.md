# Use Cases

> 🌐 **Languages**: English | [繁體中文](zh-Hant/README.md)

Real(istic) walkthroughs of Journal Atlas in action — full session transcripts showing how an AI agent reasons over the journal knowledge base to produce submission strategy.

These aren't abstract feature lists. They are end-to-end demonstrations of what the skill actually does when an author describes their paper and asks for help.

## Why this exists

The skill's `SKILL.md` specifies *how* the AI should reason. Each use case here shows *what that reasoning looks like in practice* — including:

- The full back-and-forth between author and AI
- How constraint changes (e.g. "now I need immediate OA") cascade through the recommendation logic
- How the rejection-fallback chain gets walked
- How comparison mode produces head-to-head verdicts
- How the AI handles out-of-coverage fields honestly

For first-time contributors, these are also the clearest way to see what a "good" Journal Atlas session feels like.

## Available cases

| Case | Field | Methodology | Paper attributes | Highlights |
|------|-------|-------------|------------------|------------|
| [Self-state Dynamics in Altered-State Autoethnography](self-state-altered-states-autoethnography.md) | Psychology | Autoethnography (single-author, no IRB) | 12K words, $0 APC, AI-assisted (disclosed), sensitive topic | Hybrid OA reasoning, Sage zero-embargo loophole, rejection-recovery pivot (Trojan-horse framing), comparison verdict |

*(more cases as the community contributes)*

## Contributing a use case

If you've used Journal Atlas (or could plausibly use it) for a real paper and the session produced something worth showing:

1. Read [TEMPLATE.md](TEMPLATE.md) for the format
2. Anonymize anything that would deanonymize the author
3. Open a PR

Strong use cases share three traits:

- **Multi-turn**: shows how constraint changes shift recommendations
- **Honest about limits**: includes at least one moment where the AI admits it can't help (out-of-coverage field, missing data, ambiguous attribute)
- **Strategically illustrative**: the reasoning generalizes beyond the specific paper

Single-question demos (e.g. "give me one journal recommendation") are less useful. We prefer cases that walk the skill through its full workflow.

## How these relate to the test suite

[`E2E_TEST_GUIDE.md`](../../E2E_TEST_GUIDE.md) (kept in the workspace, not committed) defines the six scenarios that every release should pass. Each case study here is anchored to one or more of those scenarios so reviewers can verify the skill's behavior hasn't regressed.

The first use case (Self-state Dynamics) covers all six scenarios end-to-end.
