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
- `journal_spine.db` with **~167k** `journals` rows — one per OpenAlex source that
  carries a registered ISSN-L. Note: the OpenAlex snapshot has ~229k `type=="journal"`
  records, but ~62k lack an ISSN-L and can't key into an ISSN-primary-key table; the
  spine is *ISSN-bearing journals only*. 166,821 measured on the 2026-07-13 snapshot.
- Coverage sanity (2026-07-13 measured): CAS join 21,600; JUFO 29,843; DOAJ 21,304;
  Norway 32,774; Retraction Watch 5,881; OpenAlex-only 112,718; issn_index 247,097.
  (The earlier ~20k/~40k/~22k estimates were sized against raw source counts — JUFO's
  61k ISSN keys include book series / non-OpenAlex channels, so its journal join is
  lower.) Print the coverage counts.
- Spot-check 3 journals across the fame spectrum resolve with provenance
  (verified: Nature 5 sources / 110 retractions; PLoS ONE 6 sources / 1226 retractions;
  Indian Geotechnical Journal — obscure, CAS+JUFO+Norway).

## Notes
- No API key needed (S3 snapshot is anonymous; the 2026-02 OpenAlex key/credit
  limits only affect the REST API, which full mode does NOT use).
- If `aws` CLI is unavailable, the simplest fix (verified 2026-07-13, Windows +
  Python 3.10) is `pip install awscli`, then run it as `python -m awscli s3 sync ...`
  — no separate installer needed. HTTPS bucket-listing works too but is fiddlier.
- `journal_spine.db` is git-ignored — it's a build artifact, regenerated, not committed.
- Runtime is dominated by the OpenAlex snapshot parse; expect minutes, not hours.
