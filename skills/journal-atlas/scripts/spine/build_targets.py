#!/usr/bin/env python3
"""
Generate a demand-ranked target list of journals for a field, with real ISSNs,
for feeding WO2 (soft-metadata batches). Ranking = article volume in the field
(OpenAlex works group_by), which is the demand-tiering the design calls for.

Usage:
    python build_targets.py --field 32 --limit 280 --out targets_psychology.json
    # field 32 = Psychology. Add --extra-fields 33,17 to merge adjacent fields.

Uses the live OpenAlex API (no key needed for low volume; polite mailto honored).
Outputs JSON: [{name, issn, openalex_id, works_in_field}] sorted by volume.
"""
from __future__ import annotations
import argparse, json, sys, time, urllib.request, urllib.parse

for _s in (sys.stdout, sys.stderr):
    try: _s.reconfigure(encoding="utf-8")
    except Exception: pass

UA = "JournalAtlas-targets/0.1 (+https://github.com/Zaious/journal-atlas)"
API = "https://api.openalex.org"


def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    for a in range(3):
        try:
            with urllib.request.urlopen(req, timeout=45) as r:
                return json.loads(r.read())
        except Exception as e:
            if a == 2: raise
            time.sleep(2 * (a + 1))


def rank_journals(field_id: str, mailto: str | None):
    m = f"&mailto={mailto}" if mailto else ""
    url = (f"{API}/works?filter=primary_topic.field.id:{field_id},type:article,"
           f"primary_location.source.type:journal&group_by=primary_location.source.id&per-page=200{m}")
    groups = _get(url).get("group_by", [])
    out = []
    for g in groups:
        sid = (g.get("key") or "").rstrip("/").split("/")[-1]
        if sid.startswith("S"):
            out.append({"openalex_id": sid, "name": g.get("key_display_name"),
                        "works_in_field": g.get("count")})
    return out


def _primary_field(source: dict) -> str | None:
    topics = source.get("topics") or []
    if not topics:
        return None
    fid = ((topics[0].get("field") or {}).get("id") or "")
    return fid.rstrip("/").split("/")[-1] or None


def resolve_issns(rows: list[dict], mailto: str | None):
    m = f"&mailto={mailto}" if mailto else ""
    by_id = {r["openalex_id"]: r for r in rows}
    ids = list(by_id)
    for i in range(0, len(ids), 50):
        batch = ids[i:i + 50]
        url = (f"{API}/sources?filter=ids.openalex:{'|'.join(batch)}"
               f"&per-page=50&select=id,display_name,issn_l,issn,type,works_count,topics{m}")
        try:
            for s in _get(url).get("results", []):
                sid = (s.get("id") or "").rstrip("/").split("/")[-1]
                if sid in by_id:
                    by_id[sid]["issn"] = s.get("issn_l")
                    by_id[sid]["type"] = s.get("type")
                    by_id[sid]["works_count"] = s.get("works_count")
                    by_id[sid]["primary_field"] = _primary_field(s)
        except Exception as e:
            print(f"  ! ISSN batch {i}-{i+50} failed ({e}); leaving those unresolved", file=sys.stderr)
        time.sleep(0.3)
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--field", default="32", help="OpenAlex field id to rank by (32=Psychology)")
    ap.add_argument("--extra-fields", default="", help="comma-separated extra field ids to also rank by")
    ap.add_argument("--allow-fields", default="", help="fields a journal's OWN dominant topic may be in to be kept (default = ranking fields). e.g. 32,28 keeps Psychology+Neuroscience")
    ap.add_argument("--limit", type=int, default=280)
    ap.add_argument("--mailto", default=None)
    ap.add_argument("--out", default="targets.json")
    args = ap.parse_args()

    fields = [args.field] + [f for f in args.extra_fields.split(",") if f.strip()]
    merged: dict[str, dict] = {}
    for fid in fields:
        print(f"ranking field {fid}...", file=sys.stderr)
        for r in rank_journals(fid, args.mailto):
            cur = merged.get(r["openalex_id"])
            if not cur or (r["works_in_field"] or 0) > (cur["works_in_field"] or 0):
                merged[r["openalex_id"]] = r

    rows = sorted(merged.values(), key=lambda r: -(r["works_in_field"] or 0))
    print(f"resolving ISSNs + primary field for {len(rows)} journals...", file=sys.stderr)
    resolve_issns(rows, args.mailto)

    allowed = set(f for f in args.allow_fields.split(",") if f.strip()) or set(fields)
    kept, off_field, no_issn = [], [], []
    for r in rows:
        if not r.get("issn"):
            no_issn.append(r["name"]); continue
        if r.get("primary_field") not in allowed:
            off_field.append(f"{r['name']} (field {r.get('primary_field')})"); continue
        kept.append(r)
    final = kept[:args.limit]
    json.dump(final, open(args.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nwrote {len(final)} targets -> {args.out}")
    print(f"  dropped {len(no_issn)} without ISSN; {len(off_field)} off-field (e.g. {', '.join(off_field[:6])})")
    print("  top 12 by field volume:")
    for r in final[:12]:
        print(f"    {r['issn']}  {r['works_in_field']:>7,}  {r['name']}")


if __name__ == "__main__":
    main()
