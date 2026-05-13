# Scripts

Automation tools for Journal Atlas. All scripts are Python 3.10+ and licensed under MIT (see [LICENSE-CODE](../LICENSE-CODE)).

| Script | Purpose | Status |
|--------|---------|--------|
| `import_openalex.py` | Auto-populate a new journal entry from OpenAlex (Identity / Metrics / Subject Density / OA). Uses pyalex (MIT). | ✅ Implemented |
| `validate_structure.py` | Check journal `.md` files match TEMPLATE schema. Runs in CI on every PR via `.github/workflows/validate.yml`. | ✅ Implemented |
| `bundle_for_upload.py` | Merge journal files into bundles for ChatGPT GPTs (20-file limit) or Claude Desktop projects. | ✅ Implemented |
| `fit_score.py` | Compute fit score for a paper vs. journals (regex-based parser, default weights). | ⚠️ v0.1 — needs validation against backtest data once seed grows |
| `update_metrics.py` | Fetch latest metrics from OpenAlex API; propose diffs for existing entries. | 🔲 Planned |
| `topic_trend_scan.py` | Scan recent publication topics for trend shifts. | 🔲 Planned |

## Setup

```bash
pip install -r scripts/requirements.txt
# Optional: set OPENALEX_EMAIL for higher rate limits (polite pool)
export OPENALEX_EMAIL=your-email@example.com
```

## Common Workflows

### Adding a new journal

```bash
# Dry-run first to preview the generated entry
python scripts/import_openalex.py --issn 0959-3543 --field psychology --dry-run

# When happy, write the file
python scripts/import_openalex.py --issn 0959-3543 --field psychology

# Validate before committing
python scripts/validate_structure.py references/journals/psychology/theory-and-psychology.md

# Then open the file and fill in the *(fill manually)* sections —
# especially Soft Metadata and Strategic Notes (the core value)
```

### Validating the whole knowledge base

```bash
# Human-readable output
python scripts/validate_structure.py

# JSON output (for tooling / CI)
python scripts/validate_structure.py --json
```

### Scoring a paper against the knowledge base

```bash
# Quick CLI form
python scripts/fit_score.py \
    --topics "embodied cognition,collaborative learning" \
    --methodology theoretical \
    --word-count 12000 \
    --apc-budget 0 \
    --fields psychology,hci

# Or use a JSON paper description
python scripts/fit_score.py --paper-json my-paper.json --top-n 10
```

### Bundling for ChatGPT GPT / Claude Desktop upload

```bash
# One bundle per field, output to dist/
python scripts/bundle_for_upload.py

# Single mega-file (for very small knowledge bases)
python scripts/bundle_for_upload.py --single-file
```

## Design Principles

- **Propose, don't overwrite.** Scripts that modify journal data generate diffs for human review. They never auto-commit.
- **Minimal dependencies.** `pyalex` + standard library. No web frameworks.
- **Dry-run by default where applicable.** Destructive or write-heavy operations default to preview mode.
- **CI-friendly.** Every script supports `--json` output (where meaningful) and uses standard exit codes.
