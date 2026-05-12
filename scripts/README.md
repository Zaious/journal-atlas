# Scripts

Automation tools for Journal Atlas. All scripts are Python 3.10+.

| Script | Purpose | Status |
|--------|---------|--------|
| `validate-structure.py` | Check journal `.md` files match TEMPLATE schema | 🔲 Planned (P0) |
| `fit-score.py` | Compute fit score for a paper vs. journals | 🔲 Planned (P1) |
| `update-metrics.py` | Fetch latest metrics from OpenAlex API | 🔲 Planned (P2) |
| `topic-trend-scan.py` | Scan recent publication topics for trend shifts | 🔲 Planned (P2) |
| `bundle-for-upload.py` | Merge journal files for platforms with file limits | 🔲 Planned (P2) |

## Design Principles

- **Propose, don't overwrite.** Scripts that modify journal data generate diffs for human review. They never auto-commit.
- **Minimal dependencies.** `requests` + standard library. No frameworks.
- **Dry-run by default.** Every script supports `--dry-run`.

See `SCRIPTS_SPEC.md` in the project workspace for detailed input/output definitions.
