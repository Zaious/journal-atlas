# Journal Atlas

**A community-maintained, AI-native knowledge base of academic journal fit metadata.**

Journal Atlas fills a gap that Impact Factor and Scimago don't cover: **soft metadata** — the unwritten rules about reviewer culture, framing expectations, sensitive topic tolerance, AI policy nuances, and methodological preferences that researchers currently learn only through experience or word of mouth.

## What's Inside

Each journal entry is a structured Markdown file covering 7 dimensions:

| Dimension | What it tells you |
|-----------|-------------------|
| **Identity** | Name, publisher, ISSN, editorial board location |
| **Metrics** | IF, h-index, CiteScore, acceptance rate, review timeline |
| **Policies** | AI policy, preprint rules, OA/APC, embargo periods |
| **Format** | Word limits, article types, reference limits |
| **Subject Density** | What topics this journal actually publishes (OpenAlex data) |
| **Soft Metadata** | Reviewer culture, framing requirements, sensitive topic tolerance, epistemological leanings |
| **Strategic Notes** | Hard blockers, adaptation effort, best/worst fit |

**Soft Metadata is the core differentiator.** Everything else you can find on Scimago. The information in Soft Metadata is what saves you a rejection and 6 months.

## Coverage (v1.0)

- Psychology (clinical, cognitive, theoretical, qualitative)
- HCI (Human-Computer Interaction)
- Qualitative methodology
- Cognitive science & philosophy of mind

~30-50 journals at launch. Growing with community contributions.

---

## How to Use

### Option 1: Claude Code (recommended)

Install as a skill plugin:

```bash
claude /plugin marketplace add Zaious/journal-atlas
claude /plugin install journal-atlas
```

Then ask naturally:

> "I have a 12,000-word theoretical paper on self-state switching in BDSM contexts.
> No IRB, no APC budget, I used AI for writing assistance. Which journals fit?"

The skill reads the knowledge base, filters by your constraints, and ranks by soft fit.

### Option 2: Claude Desktop

1. Clone this repo: `git clone https://github.com/Zaious/journal-atlas.git`
2. Create a new Project in Claude Desktop
3. Upload the `.md` files from `references/journals/` as Project Knowledge
4. Copy the contents of `SKILL.md` into Project Instructions

### Option 3: ChatGPT (GPT Builder)

1. Clone this repo
2. Run `python scripts/bundle-for-upload.py` to merge journal files into uploadable chunks
3. Upload the output files to your GPT's Knowledge section
4. Copy the contents of `SKILL.md` into your GPT's Instructions

### Option 4: Just read it

Browse [`references/journals/`](references/journals/) on GitHub. Every journal is a readable Markdown page. No AI required.

---

## Automation (scripts/)

| Script | Purpose |
|--------|---------|
| `validate-structure.py` | Check that journal `.md` files match the template schema. Runs on every PR. |
| `update-metrics.py` | Fetch latest IF / h-index / CiteScore from OpenAlex API. Proposes a PR draft — never auto-writes. |
| `topic-trend-scan.py` | Scan a journal's recent publications to detect topic trend shifts. |
| `fit-score.py` | Compute a numerical fit score given your paper's attributes vs. each journal. |
| `bundle-for-upload.py` | Merge journal files into larger chunks for platforms with file count limits (e.g. ChatGPT). |

---

## Contributing

We need your journal expertise. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

**Quick version:**
1. Copy [TEMPLATE.md](TEMPLATE.md)
2. Fill in what you know (partial entries welcome — others can fill gaps)
3. Open a PR

The most valuable contributions are **Soft Metadata** — the stuff that isn't in any database. If you've published in a journal and know its unwritten rules, that knowledge helps every researcher who comes after you.

---

## What This Is NOT

- **Not a journal ranking.** We provide metadata; you decide what matters.
- **Not a predatory journal blacklist.** Use [Cabells](https://www2.cabells.com/) for that.
- **Not a replacement for Scimago/JCR.** We aggregate their quantitative metrics as a convenience. Our value is the soft metadata they don't have.

---

## License

[TBD — see CONTRIBUTING.md for discussion]

---

## Acknowledgments

Built by researchers, for researchers. Maintained by the community.

Initial seed data drawn from journal evaluations conducted during active manuscript submission processes in psychology, HCI, and qualitative methodology (2025-2026).
