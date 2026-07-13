#!/usr/bin/env python3
"""
Journal Atlas — spine builder.

Joins the six no-caveat green sources on ISSN-L into one machine-readable spine
of *facts* (Layer S of docs/ATLAS_V2_DESIGN.md), each carrying provenance +
snapshot date. This is the coverage backbone the skill filters/ranks over; deep
soft metadata lives in the curated markdown entries, not here.

Sources joined:
  OpenAlex (CC0, seed) · DOAJ (CC BY-SA) · JUFO (CC BY 4.0, +Norway/SJR/SNIP/Sherpa)
  · CAS 中科院分区 (fact/mirror) · Retraction Watch (CC0, name-keyed) · Norwegian (CC BY)

Modes:
  Sample (proves the join, runs anywhere with network):
      python build_spine.py --sample-issns 0028-0836,0022-3514 --out spine.db
  Full (all ~228k journals; needs bulk files):
      python build_spine.py --full \\
          --openalex-snapshot ./oa_sources \\   # aws s3 sync s3://openalex/data/jsonl/sources/ (--no-sign-request)
          --jufo-zip massa.json.zip --cas-csv FQBJCR2025-UTF8.csv \\
          --rw-csv retraction_watch.csv --doaj-csv journalcsv__doaj.csv --out spine.db
  Fetch bulk files first:
      python build_spine.py --fetch-bulk ./bulk
"""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys

for _stream in (sys.stdout, sys.stderr):  # ensure UTF-8 output (Chinese CAS categories, names)
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

import sources as S

SCHEMA = """
CREATE TABLE IF NOT EXISTS journals (
    issn_l           TEXT PRIMARY KEY,
    display_name     TEXT,
    publisher        TEXT,
    country          TEXT,
    homepage         TEXT,
    type             TEXT,
    works_count      INTEGER,
    cited_by_count   INTEGER,
    h_index          INTEGER,
    two_yr_citedness REAL,
    is_oa            INTEGER,
    is_in_doaj       INTEGER,
    apc_usd          INTEGER,
    -- DOAJ
    peer_review_type TEXT,
    oa_apc_amount    INTEGER,
    oa_apc_currency  TEXT,
    oa_license       TEXT,
    -- ranking tiers (bakeable, level-based only — NOT quartiles)
    jufo_level       TEXT,
    norway_level     TEXT,
    denmark_level    TEXT,
    cas_zone         TEXT,
    cas_broad_category TEXT,
    cas_top          INTEGER,
    sjr_ref          TEXT,   -- reference only (SJR is NC; do not present as bakeable)
    snip_ref         TEXT,
    sherpa_code      TEXT,
    -- integrity
    retraction_count INTEGER,
    retraction_top_reasons TEXT,
    -- positioning
    topics_json      TEXT,
    keywords         TEXT,
    -- meta
    signal_quality   INTEGER,          -- soft-metadata confidence, filled in Phase 3
    sources          TEXT,             -- which sources contributed
    provenance       TEXT,             -- JSON: {field_group: {source,url,as_of}}
    built_on         TEXT
);
CREATE TABLE IF NOT EXISTS issn_index (
    issn   TEXT PRIMARY KEY,           -- every ISSN variant (8-char, no hyphen)
    issn_l TEXT REFERENCES journals(issn_l)
);
"""


def merge_journal(oa: dict, doaj: dict | None, jufo: dict | None,
                  cas: dict | None, rw: dict | None, nor: dict | None) -> dict:
    """Merge per-source fact dicts into one spine row + provenance."""
    prov: dict[str, dict] = {}
    contributing: list[str] = []

    def take(d, name):
        if d:
            contributing.append(name)
            prov[name] = d.get("_provenance")

    take(oa, "openalex"); take(doaj, "doaj"); take(jufo, "jufo")
    take(cas, "cas"); take(rw, "retraction_watch"); take(nor, "norwegian")

    doaj = doaj or {}; jufo = jufo or {}; cas = cas or {}; rw = rw or {}; nor = nor or {}
    reasons = sorted(rw.get("reasons", {}).items(), key=lambda kv: -kv[1])[:5]

    row = {
        "issn_l": oa["issn_l"],
        "display_name": oa.get("display_name"),
        "publisher": oa.get("publisher"),
        "country": oa.get("country"),
        "homepage": oa.get("homepage"),
        "type": oa.get("type"),
        "works_count": oa.get("works_count"),
        "cited_by_count": oa.get("cited_by_count"),
        "h_index": oa.get("h_index"),
        "two_yr_citedness": oa.get("two_yr_citedness"),
        "is_oa": int(bool(oa.get("is_oa"))) if oa.get("is_oa") is not None else None,
        "is_in_doaj": int(bool(oa.get("is_in_doaj"))) if oa.get("is_in_doaj") is not None else None,
        "apc_usd": oa.get("apc_usd"),
        "peer_review_type": ";".join(doaj.get("peer_review_type") or []) or None,
        "oa_apc_amount": doaj.get("oa_apc_amount"),
        "oa_apc_currency": doaj.get("oa_apc_currency"),
        "oa_license": ";".join(doaj.get("license") or []) or None,
        "jufo_level": jufo.get("jufo_level"),
        "norway_level": nor.get("norway_level_authoritative") or jufo.get("norway_level"),
        "denmark_level": jufo.get("denmark_level"),
        "cas_zone": cas.get("cas_zone"),
        "cas_broad_category": cas.get("cas_broad_category"),
        "cas_top": int(cas["cas_top"]) if cas.get("cas_top") is not None else None,
        "sjr_ref": jufo.get("sjr"),
        "snip_ref": jufo.get("snip"),
        "sherpa_code": jufo.get("sherpa_romeo_code"),
        "retraction_count": rw.get("retraction_count"),
        "retraction_top_reasons": "; ".join(f"{r} ({n})" for r, n in reasons) or None,
        "topics_json": json.dumps(oa.get("topics") or [], ensure_ascii=False),
        "keywords": ";".join(doaj.get("keywords") or []) or None,
        "signal_quality": None,
        "sources": ",".join(contributing),
        "provenance": json.dumps(prov, ensure_ascii=False),
        "built_on": S.TODAY,
    }
    return row, oa.get("issns") or []


def write_rows(db_path: str, rows: list[tuple[dict, list]]):
    conn = sqlite3.connect(db_path)
    conn.executescript(SCHEMA)
    cols = [c[1] for c in conn.execute("PRAGMA table_info(journals)")]
    for row, issns in rows:
        conn.execute(
            f"INSERT OR REPLACE INTO journals ({','.join(cols)}) VALUES ({','.join('?' * len(cols))})",
            [row.get(c) for c in cols],
        )
        for issn in set(issns) | ({row["issn_l"]} if row["issn_l"] else set()):
            conn.execute("INSERT OR REPLACE INTO issn_index (issn, issn_l) VALUES (?, ?)",
                         (issn, row["issn_l"]))
    conn.commit()
    conn.close()


def build_sample(issns: list[str], db_path: str,
                 cas_bulk=None, rw_bulk=None, nor_bulk=None):
    rows = []
    for raw in issns:
        issn = S.norm_issn(raw)
        if not issn:
            print(f"  ! skip invalid ISSN {raw!r}", file=sys.stderr)
            continue
        oa = S.openalex_fetch(issn)
        if not oa:
            print(f"  ! {raw}: not in OpenAlex — skipped (no spine seed)", file=sys.stderr)
            continue
        variants = set(oa.get("issns") or []) | {oa["issn_l"]} | {issn}
        doaj = S.doaj_fetch(issn)
        jufo = S.jufo_fetch(issn)
        cas = _lookup_any(cas_bulk, variants) if cas_bulk else None
        nor = _lookup_any(nor_bulk, variants) if nor_bulk else None
        rw = rw_bulk.get(S._norm_name(oa.get("display_name"))) if rw_bulk else None
        row, ivars = merge_journal(oa, doaj, jufo, cas, rw, nor)
        rows.append((row, ivars))
        print(f"  ✓ {oa.get('display_name')}  [{','.join(row['sources'].split(','))}]", file=sys.stderr)
    write_rows(db_path, rows)
    return rows


def _lookup_any(bulk: dict, variants: set) -> dict | None:
    for v in variants:
        if v in bulk:
            return bulk[v]
    return None


def build_full(args):
    cas_bulk = S.cas_load_bulk(args.cas_csv) if args.cas_csv else {}
    rw_bulk = S.rw_load_bulk(args.rw_csv) if args.rw_csv else {}
    jufo_bulk = S.jufo_load_bulk(args.jufo_zip) if args.jufo_zip else {}
    nor_bulk = S.norwegian_load_bulk(args.norwegian_csv) if args.norwegian_csv else {}
    doaj_bulk = _doaj_csv_index(args.doaj_csv) if args.doaj_csv else {}
    print(f"  bulk loaded: jufo={len(jufo_bulk)} cas={len(cas_bulk)} "
          f"rw={len(rw_bulk)} nor={len(nor_bulk)} doaj={len(doaj_bulk)}", file=sys.stderr)

    conn = sqlite3.connect(args.out)
    conn.executescript(SCHEMA)
    cols = [c[1] for c in conn.execute("PRAGMA table_info(journals)")]
    n = 0
    for oa in S.openalex_iter_snapshot(args.openalex_snapshot):
        if not oa.get("issn_l"):
            continue
        variants = set(oa.get("issns") or []) | {oa["issn_l"]}
        doaj = _lookup_any(doaj_bulk, variants)
        jufo = _lookup_any(jufo_bulk, variants)
        cas = _lookup_any(cas_bulk, variants)
        nor = _lookup_any(nor_bulk, variants)
        rw = rw_bulk.get(S._norm_name(oa.get("display_name")))
        row, ivars = merge_journal(oa, doaj, jufo, cas, rw, nor)
        conn.execute(
            f"INSERT OR REPLACE INTO journals ({','.join(cols)}) VALUES ({','.join('?' * len(cols))})",
            [row.get(c) for c in cols])
        for issn in set(ivars) | {row["issn_l"]}:
            conn.execute("INSERT OR REPLACE INTO issn_index VALUES (?, ?)", (issn, row["issn_l"]))
        n += 1
        if n % 5000 == 0:
            conn.commit()
            print(f"    {n} journals...", file=sys.stderr)
    conn.commit()
    conn.close()
    print(f"  done: {n} journals -> {args.out}", file=sys.stderr)


def _doaj_csv_index(csv_path: str) -> dict:
    import csv as _csv
    out = {}
    with open(csv_path, encoding="utf-8", newline="") as fh:
        for r in _csv.DictReader(fh):
            shaped = {
                "peer_review_type": [r.get("Review process") or ""],
                "oa_apc_has": (r.get("APC") or "").lower().startswith("y"),
                "oa_apc_amount": _int(r.get("APC amount")),
                "oa_apc_currency": r.get("APC currency") or None,
                "license": [x.strip() for x in (r.get("Journal license") or "").split(",") if x.strip()],
                "keywords": [x.strip() for x in (r.get("Keywords") or "").split(",") if x.strip()],
                "_provenance": S._prov("DOAJ", "journal CSV"),
            }
            for key in ("Journal ISSN (print version)", "Journal EISSN (online version)"):
                issn = S.norm_issn(r.get(key))
                if issn:
                    out.setdefault(issn, shaped)
    return out


def _int(v):
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return None


def fetch_bulk(dest_dir: str):
    os.makedirs(dest_dir, exist_ok=True)
    jobs = [
        (S.JUFO_MASSA, "massa.json.zip"),
        (S.CAS_CSV, "FQBJCR2025-UTF8.csv"),
        (S.RW_CSV, "retraction_watch.csv"),
        (S.NORWEGIAN_CSV, "norwegian_register.csv"),
    ]
    for url, name in jobs:
        try:
            S.download(url, os.path.join(dest_dir, name))
        except Exception as e:  # noqa: BLE001
            print(f"  ! {name} failed: {e}", file=sys.stderr)
    print("  (OpenAlex + DOAJ: use aws s3 sync / doaj.org/csv separately — see --help)", file=sys.stderr)


def summarize(db_path: str):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT * FROM journals ORDER BY cited_by_count DESC").fetchall()
    print(f"\nSpine: {len(rows)} journals in {db_path}\n")
    for r in rows:
        tiers = []
        if r["jufo_level"]: tiers.append(f"JUFO {r['jufo_level']}")
        if r["norway_level"]: tiers.append(f"NO {r['norway_level']}")
        if r["cas_zone"]: tiers.append(f"CAS {r['cas_zone']}")
        rc = f" · {r['retraction_count']} retractions" if r["retraction_count"] else ""
        oa = " · OA" if r["is_in_doaj"] else ""
        print(f"  {r['display_name']}  ({S.hyphenate(r['issn_l']) if r['issn_l'] else '—'})")
        print(f"      {r['publisher']} · h={r['h_index']} · {' / '.join(tiers) or 'no tier data'}{oa}{rc}")
        print(f"      sources: {r['sources']}")
    conn.close()


def main():
    ap = argparse.ArgumentParser(description="Build the Journal Atlas ISSN spine.")
    ap.add_argument("--sample-issns", help="comma-separated ISSNs for live sample build")
    ap.add_argument("--issn-file", help="file of ISSNs (one per line) for sample build")
    ap.add_argument("--full", action="store_true", help="full build from bulk snapshots")
    ap.add_argument("--fetch-bulk", metavar="DIR", help="download bulk files into DIR and exit")
    ap.add_argument("--out", default="journal_spine.db")
    ap.add_argument("--openalex-snapshot", help="dir of synced OpenAlex source *.gz (full mode)")
    ap.add_argument("--jufo-zip"); ap.add_argument("--cas-csv"); ap.add_argument("--rw-csv")
    ap.add_argument("--norwegian-csv"); ap.add_argument("--doaj-csv")
    ap.add_argument("--summary", action="store_true", help="print summary of an existing spine")
    args = ap.parse_args()

    if args.fetch_bulk:
        fetch_bulk(args.fetch_bulk); return
    if args.summary:
        summarize(args.out); return
    if args.full:
        if not args.openalex_snapshot:
            ap.error("--full requires --openalex-snapshot (aws s3 sync s3://openalex/data/jsonl/sources/)")
        build_full(args); summarize(args.out); return

    issns = []
    if args.sample_issns:
        issns += [x for x in args.sample_issns.split(",") if x.strip()]
    if args.issn_file:
        with open(args.issn_file) as fh:
            issns += [ln.strip() for ln in fh if ln.strip()]
    if not issns:
        ap.error("provide --sample-issns, --issn-file, --full, --fetch-bulk, or --summary")

    cas_bulk = S.cas_load_bulk(args.cas_csv) if args.cas_csv else None
    rw_bulk = S.rw_load_bulk(args.rw_csv) if args.rw_csv else None
    nor_bulk = S.norwegian_load_bulk(args.norwegian_csv) if args.norwegian_csv else None
    print(f"Building sample spine ({len(issns)} ISSNs)...", file=sys.stderr)
    build_sample(issns, args.out, cas_bulk, rw_bulk, nor_bulk)
    summarize(args.out)


if __name__ == "__main__":
    main()
