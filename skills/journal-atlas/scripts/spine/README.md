# Spine — ISSN-keyed coverage backbone

The **spine** joins the six no-caveat, license-clean sources into one
machine-readable table of *facts* (Layer S of
[docs/ATLAS_V2_DESIGN.md](../../../../docs/ATLAS_V2_DESIGN.md)), one row per
journal, keyed on ISSN-L, every fact carrying a source + snapshot date.

It is the **coverage** half of Journal Atlas (breadth across ~228k journals).
Deep soft metadata stays in the curated `references/journals/**.md` entries
(depth on the shortlist). The spine never stores verbatim prose — only facts —
per the "facts, not verbatim" rule.

## Sources joined

| Source | License | Join key | Fills |
|--------|---------|----------|-------|
| OpenAlex (seed) | CC0 | ISSN-L | identity, metrics, `topics`, OA/APC |
| DOAJ | CC BY-SA 4.0 | ISSN | OA/APC/license, peer-review type, keywords |
| JUFO | CC BY 4.0 | ISSN | JUFO level **+ Norway/Denmark level + SJR + SNIP + Sherpa code** |
| CAS 中科院分区 | fact (mirror) | ISSN | 大类分区 (一–四区), 大类, Top — *frozen 2025* |
| Retraction Watch | CC0 | **journal name** (no ISSN col — fuzzy) | retraction count + top reasons |
| Norwegian Register | CC BY 4.0 | ISSN | authoritative Norwegian level (optional; JUFO already bundles it) |

Quartile systems (SJR / CiteScore / JIF) are **not baked in** — they are
paywalled or NonCommercial and clash with CC BY-SA. `sjr_ref` / `snip_ref` are
stored as *reference only* (they arrive free inside JUFO's record). Bakeable
quality tiers are the level-based systems (JUFO / Norway / CAS).

## Usage

### Sample build (live per-ISSN — runs anywhere with network)
```bash
python build_spine.py --sample-issns 0028-0836,0022-3514,1046-1310 --out sample_spine.db
# add CAS + Retraction Watch enrichment (needs the bulk files):
python build_spine.py --sample-issns 0028-0836,1046-1310 \
    --cas-csv bulk/FQBJCR2025-UTF8.csv --rw-csv bulk/retraction_watch.csv --out sample_spine.db
```

### Fetch bulk files (for CAS / Retraction Watch / JUFO / Norwegian)
```bash
python build_spine.py --fetch-bulk bulk
# OpenAlex + DOAJ bulk are fetched separately (large / different tooling):
aws s3 sync 's3://openalex/data/jsonl/sources/' ./bulk/oa_sources --no-sign-request
curl -L 'https://doaj.org/csv' -o bulk/doaj.csv
```

### Full build (~228k journals)
```bash
python build_spine.py --full \
    --openalex-snapshot ./bulk/oa_sources \
    --jufo-zip bulk/massa.json.zip \
    --cas-csv bulk/FQBJCR2025-UTF8.csv \
    --rw-csv bulk/retraction_watch.csv \
    --doaj-csv bulk/doaj.csv \
    --out journal_spine.db
```

### Inspect an existing spine
```bash
python build_spine.py --summary --out journal_spine.db
```

## Output schema

SQLite. `journals` (one row per ISSN-L) + `issn_index` (every ISSN variant →
ISSN-L, so any ISSN resolves to its journal). Key columns: identity/metrics,
`jufo_level` / `norway_level` / `cas_zone` (tiers), `retraction_count` /
`retraction_top_reasons` (integrity), `topics_json` (scope, no LLM),
`signal_quality` (NULL until the Phase-3 soft-metadata layer), and a
`provenance` JSON column mapping each contributing source → `{source, url, as_of}`.

## Notes & caveats

- **Retraction Watch has no ISSN column** — it joins on normalized journal name,
  which is fuzzy. Only rows whose `RetractionNature` is a true retraction count
  (corrections / expressions of concern are excluded).
- **OpenAlex is the seed**: a journal must be in OpenAlex to enter the spine.
  Full builds should use the anonymous S3 snapshot (no API key); the live API
  is for single-ISSN / incremental refresh (2026-02 key/credit limits apply).
- **CAS 中科院分区 is frozen at the 2025 upgraded version** (CAS stopped updating
  in 2026) — the static mirror file needs no periodic sync.
- Field names were verified live against each API on 2026-07-13. Don't "fix"
  them from memory — re-verify against the source if one breaks.
- Stdlib only (no pip install). Python 3.10+.
