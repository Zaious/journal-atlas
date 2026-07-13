# WO1 — Full Spine Load (~228k journals)

> **Type**: mechanical data pipeline (token-cheap — mostly download + a Python run).
> **Run anywhere** with disk + network + `aws` CLI. Does *not* meaningfully consume
> model/subscription usage. Hand to a background job or a separate session.
> **Depends on**: `skills/journal-atlas/scripts/spine/` (already built & tested).

## Goal
Produce `journal_spine.db` — the full ISSN-keyed fact backbone across all
OpenAlex journals, joined with DOAJ / JUFO / CAS / Retraction Watch / Norwegian.

## Steps

```bash
cd skills/journal-atlas/scripts/spine
mkdir -p bulk

# 1. OpenAlex sources snapshot (CC0, no API key). ~hundreds of MB (sources only,
#    NOT works). Requires aws CLI.
aws s3 sync 's3://openalex/data/jsonl/sources/' ./bulk/oa_sources --no-sign-request

# 2. The rest (JUFO / CAS / Retraction Watch / Norwegian) — one command:
python build_spine.py --fetch-bulk bulk

# 3. DOAJ full journal CSV (CC BY-SA):
curl -L 'https://doaj.org/csv' -o bulk/doaj.csv

# 4. Build:
python build_spine.py --full \
    --openalex-snapshot ./bulk/oa_sources \
    --jufo-zip bulk/massa.json.zip \
    --cas-csv bulk/FQBJCR2025-UTF8.csv \
    --rw-csv bulk/retraction_watch.csv \
    --norwegian-csv bulk/norwegian_register.csv \
    --doaj-csv bulk/doaj.csv \
    --out journal_spine.db

# 5. Verify:
python build_spine.py --summary --out journal_spine.db | head -40
```

## Acceptance
- `journal_spine.db` with ~200k+ `journals` rows.
- Coverage sanity: CAS join hits ~20k WoS journals; JUFO ~40k; DOAJ ~22k; the
  rest OpenAlex-only (identity+metrics+topics). Print the coverage counts.
- Spot-check 3 journals across the fame spectrum resolve with provenance.

## Notes
- No API key needed (S3 snapshot is anonymous; the 2026-02 OpenAlex key/credit
  limits only affect the REST API, which full mode does NOT use).
- If `aws` CLI is unavailable, the snapshot can be pulled over HTTPS from the
  `openalex` S3 bucket listing, but `aws s3 sync` is by far the simplest.
- `journal_spine.db` is git-ignored — it's a build artifact, regenerated, not committed.
- Runtime is dominated by the OpenAlex snapshot parse; expect minutes, not hours.
