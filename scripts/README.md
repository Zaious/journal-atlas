# Scripts

Automation tools for Journal Atlas. All scripts are Python 3.10+.

| Script | Purpose | Status |
|--------|---------|--------|
| `import_openalex.py` | Auto-populate a new journal entry from OpenAlex (Identity / Metrics / Subject Density / OA) | ✅ Implemented |
| `validate-structure.py` | Check journal `.md` files match TEMPLATE schema | 🔲 Planned (P0) |
| `fit-score.py` | Compute fit score for a paper vs. journals | 🔲 Planned (P1) |
| `update-metrics.py` | Fetch latest metrics from OpenAlex API (proposes diffs for existing entries) | 🔲 Planned (P2) |
| `topic-trend-scan.py` | Scan recent publication topics for trend shifts | 🔲 Planned (P2) |
| `bundle-for-upload.py` | Merge journal files for platforms with file limits | 🔲 Planned (P2) |

## Setup

```bash
pip install -r scripts/requirements.txt
# Optional: set OPENALEX_EMAIL for higher rate limits (polite pool)
export OPENALEX_EMAIL=your-email@example.com
```

## Quick Start: Adding a Journal

```bash
# Dry-run first to preview the generated entry
python scripts/import_openalex.py --issn 0959-3543 --field psychology --dry-run

# When happy, write the file
python scripts/import_openalex.py --issn 0959-3543 --field psychology

# Then open the file and fill in the *(fill manually)* sections
# — especially Soft Metadata and Strategic Notes (the core value)
```

## Design Principles

- **Propose, don't overwrite.** Scripts that modify journal data generate diffs for human review. They never auto-commit.
- **Minimal dependencies.** `requests` + standard library. No frameworks.
- **Dry-run by default.** Every script supports `--dry-run`.

See `SCRIPTS_SPEC.md` in the project workspace for detailed input/output definitions.
