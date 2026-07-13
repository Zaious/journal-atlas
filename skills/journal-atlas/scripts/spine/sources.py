"""
Journal Atlas — spine data sources.

One fetcher/loader per authoritative, license-clean source. Every function
returns a dict of *facts* (never verbatim prose) tagged with provenance, per the
"facts, not verbatim" rule in docs/ATLAS_V2_DESIGN.md §3.

Live per-ISSN fetchers (fast, for sample mode):  openalex_fetch, doaj_fetch, jufo_fetch
Bulk loaders (for full mode):                    *_load_bulk, openalex_iter_snapshot

Stdlib only — no third-party deps, so the spine builds in any Python 3.10+.
Field names below were verified live against each API on 2026-07-13; do not
"fix" them from memory.
"""

from __future__ import annotations

import csv
import gzip
import io
import json
import sys
import time
import urllib.parse
import urllib.request
import zipfile
from datetime import date

TODAY = date.today().isoformat()
UA = "JournalAtlas-spine/0.1 (+https://github.com/Zaious/journal-atlas)"

# --- Source endpoints (verified live 2026-07-13) --------------------------------
OPENALEX_SOURCE = "https://api.openalex.org/sources/issn:{issn}"
DOAJ_JOURNAL = "https://doaj.org/api/search/journals/issn%3A{issn}"
JUFO_FIND = "https://jufo-rest.csc.fi/v1.1/etsi.php?issn={issn}"
JUFO_CHANNEL = "https://jufo-rest.csc.fi/v1.1/kanava/{jufo_id}"
JUFO_MASSA = "https://jufo-rest.csc.fi/v1.1/massa.json.zip"
NORWEGIAN_CSV = "https://kanalregister.hkdir.no/publiseringskanaler/csvliste/tidsskrift?request_locale=en"
CAS_CSV = ("https://raw.githubusercontent.com/hitfyd/ShowJCR/master/"
           "%E4%B8%AD%E7%A7%91%E9%99%A2%E5%88%86%E5%8C%BA%E8%A1%A8%E5%8F%8AJCR"
           "%E5%8E%9F%E5%A7%8B%E6%95%B0%E6%8D%AE%E6%96%87%E4%BB%B6/FQBJCR2025-UTF8.csv")
RW_CSV = "https://gitlab.com/crossref/retraction-watch-data/-/raw/main/retraction_watch.csv"


# --- helpers --------------------------------------------------------------------

def norm_issn(s: str | None) -> str | None:
    """Normalize an ISSN to 8 chars, no hyphen, uppercase X. Returns None if invalid."""
    if not s:
        return None
    t = str(s).strip().upper().replace("-", "").replace(" ", "")
    if len(t) == 8 and t[:7].isdigit() and (t[7].isdigit() or t[7] == "X"):
        return t
    return None


def hyphenate(issn8: str) -> str:
    return f"{issn8[:4]}-{issn8[4:]}"


def _get(url: str, timeout: int = 30, retries: int = 3, accept_json: bool = True):
    """HTTP GET with polite UA + retries. Returns parsed JSON or raw bytes."""
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": UA,
                "Accept": "application/json,*/*",
                "Accept-Language": "en,zh;q=0.8",
                "Accept-Encoding": "gzip",
            })
            with urllib.request.urlopen(req, timeout=timeout) as r:
                raw = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    raw = gzip.decompress(raw)
                return json.loads(raw) if accept_json else raw
        except Exception as e:  # noqa: BLE001 — network audit tool, surface & retry
            last = e
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"GET failed after {retries}x: {url}\n  {last}")


def _prov(source: str, url: str) -> dict:
    return {"source": source, "source_url": url, "as_of": TODAY}


# --- OpenAlex (CC0) — the spine seed --------------------------------------------

def _openalex_shape(src: dict, url: str) -> dict:
    stats = src.get("summary_stats") or {}
    issns = [norm_issn(x) for x in (src.get("issn") or [])]
    return {
        "issn_l": norm_issn(src.get("issn_l")),
        "issns": [i for i in issns if i],
        "display_name": src.get("display_name"),
        "publisher": src.get("host_organization_name"),
        "country": src.get("country_code"),
        "homepage": src.get("homepage_url"),
        "type": src.get("type"),
        "works_count": src.get("works_count"),
        "cited_by_count": src.get("cited_by_count"),
        "h_index": stats.get("h_index"),
        "two_yr_citedness": stats.get("2yr_mean_citedness"),
        "is_oa": src.get("is_oa"),
        "is_in_doaj": src.get("is_in_doaj"),
        "apc_usd": src.get("apc_usd"),
        "topics": [{"name": t.get("display_name"), "count": t.get("count")}
                   for t in (src.get("topics") or [])[:15]],
        "_provenance": _prov("OpenAlex", url),
    }


def openalex_fetch(issn: str) -> dict | None:
    url = OPENALEX_SOURCE.format(issn=hyphenate(norm_issn(issn)))
    try:
        src = _get(url)
    except RuntimeError:
        return None
    if not src or src.get("id") is None:
        return None
    return _openalex_shape(src, url)


def openalex_iter_snapshot(snapshot_dir: str):
    """Yield shaped source records from a synced OpenAlex S3 snapshot dir.

    Full-mode path:  aws s3 sync 's3://openalex/data/jsonl/sources/' <dir> --no-sign-request
    Reads every *.gz under the dir as JSON Lines. No API key needed.
    """
    import glob
    import os
    files = sorted(glob.glob(os.path.join(snapshot_dir, "**", "*.gz"), recursive=True))
    if not files:
        raise FileNotFoundError(f"No *.gz under {snapshot_dir} — sync the OpenAlex sources snapshot first.")
    for fp in files:
        with gzip.open(fp, "rt", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    src = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if src.get("type") == "journal" or src.get("issn_l"):
                    yield _openalex_shape(src, "OpenAlex snapshot")


# --- DOAJ (journal metadata CC BY-SA 4.0 — same license as us) ------------------

def _doaj_shape(bib: dict, url: str) -> dict:
    ed = bib.get("editorial") or {}
    apc = bib.get("apc") or {}
    apc_max = (apc.get("max") or [{}])
    return {
        "in_doaj": True,
        "peer_review_type": ed.get("review_process") or [],
        "oa_apc_has": apc.get("has_apc"),
        "oa_apc_amount": apc_max[0].get("price") if apc_max else None,
        "oa_apc_currency": apc_max[0].get("currency") if apc_max else None,
        "license": [l.get("type") for l in (bib.get("license") or [])],
        "keywords": bib.get("keywords") or [],
        "weeks_to_publication": (bib.get("plagiarism") or {}).get("url") and None
                                or bib.get("publication_time_weeks"),
        "_provenance": _prov("DOAJ", url),
    }


def doaj_fetch(issn: str) -> dict | None:
    url = DOAJ_JOURNAL.format(issn=hyphenate(norm_issn(issn)))
    try:
        d = _get(url)
    except RuntimeError:
        return None
    results = d.get("results") or []
    if not results:
        return None
    return _doaj_shape(results[0].get("bibjson") or {}, url)


# --- JUFO (CC BY 4.0) — bundles Norway/Denmark level + SJR + SNIP + Sherpa -------

def _jufo_shape(ch: dict, url: str) -> dict:
    def clean(v):
        return v if (v not in ("", None)) else None
    return {
        "jufo_level": clean(ch.get("Level")),
        "jufo_history": clean(ch.get("Jufo_history")),
        "norway_level": clean(ch.get("Norway_Level")),
        "denmark_level": clean(ch.get("Denmark_Level")),
        "sjr": clean(ch.get("SJR_SJR")),
        "snip": clean(ch.get("SNIP")),
        "sherpa_romeo_code": clean(ch.get("Sherpa_Romeo_Code")),
        "jufo_publisher": clean(ch.get("Publisher")),
        "_provenance": _prov("JUFO (Publication Forum, Finland)", url),
    }


def jufo_fetch(issn: str) -> dict | None:
    find_url = JUFO_FIND.format(issn=hyphenate(norm_issn(issn)))
    try:
        hits = _get(find_url)
    except RuntimeError:
        return None
    if not hits:
        return None
    jufo_id = hits[0].get("Jufo_ID")
    if not jufo_id:
        return None
    ch_url = JUFO_CHANNEL.format(jufo_id=jufo_id)
    ch = _get(ch_url)
    if isinstance(ch, list):
        ch = ch[0] if ch else {}
    return _jufo_shape(ch or {}, ch_url)


def jufo_load_bulk(zip_path: str) -> dict[str, dict]:
    """Load JUFO massa.json.zip into {issn8: shaped}. Bulk full-mode path."""
    out: dict[str, dict] = {}
    with zipfile.ZipFile(zip_path) as z:
        name = next(n for n in z.namelist() if n.endswith("massa.json"))
        rows = json.loads(z.read(name).decode("utf-8"))
    for ch in rows:
        shaped = _jufo_shape(ch, "JUFO massa.json")
        for key in ("ISSNL", "ISSN1", "ISSN2"):
            issn = norm_issn(ch.get(key))
            if issn:
                out.setdefault(issn, shaped)
    return out


# --- CAS 中科院分区 (fact via GitHub mirror; frozen 2025 — static) ----------------

def cas_load_bulk(csv_path: str) -> dict[str, dict]:
    """Load FQBJCR2025-UTF8.csv into {issn8: shaped}. ISSN/EISSN is a '/'-joined field."""
    out: dict[str, dict] = {}
    with open(csv_path, encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            shaped = {
                "cas_broad_category": (row.get("大类") or "").strip() or None,
                "cas_zone": (row.get("大类分区") or "").strip() or None,  # e.g. "1 [1/118]"
                "cas_top": (row.get("Top") or "").strip() in ("是", "Y", "Yes"),
                "cas_year": (row.get("年份") or "").strip() or None,
                "_provenance": _prov("CAS 中科院分区 (via hitfyd/ShowJCR)", CAS_CSV),
            }
            for part in (row.get("ISSN/EISSN") or "").split("/"):
                issn = norm_issn(part)
                if issn:
                    out.setdefault(issn, shaped)
    return out


# --- Retraction Watch (CC0) — integrity signal, NAME-keyed (no ISSN column) ------

def rw_load_bulk(csv_path: str) -> dict[str, dict]:
    """Aggregate retraction_watch.csv by normalized journal NAME -> {count, reasons}.

    Caveat (design §9.5): RW has no ISSN column, so this joins on journal name,
    which is fuzzy. Only rows whose RetractionNature is a true retraction count.
    """
    agg: dict[str, dict] = {}
    with open(csv_path, encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            nature = (row.get("RetractionNature") or "").strip().lower()
            if "retraction" not in nature:  # skip corrections / expressions of concern
                continue
            name = _norm_name(row.get("Journal"))
            if not name:
                continue
            rec = agg.setdefault(name, {"retraction_count": 0, "reasons": {},
                                        "_provenance": _prov("Retraction Watch (Crossref)", RW_CSV)})
            rec["retraction_count"] += 1
            for reason in (row.get("Reason") or "").split(";"):
                reason = reason.strip().lstrip("+").strip()
                if reason:
                    rec["reasons"][reason] = rec["reasons"].get(reason, 0) + 1
    return agg


def _norm_name(s: str | None) -> str | None:
    if not s:
        return None
    return " ".join(str(s).lower().split()).strip(" .")


# --- Norwegian Register (CC BY 4.0 / NLOD) — standalone authoritative level ------

def norwegian_load_bulk(csv_path: str) -> dict[str, dict]:
    """Load the Norwegian register CSV (semicolon-separated) -> {issn8: {level}}.

    JUFO already bundles Norway_Level; use this only when you want the
    authoritative full register (e.g. latest year not yet mirrored by JUFO).
    """
    out: dict[str, dict] = {}
    with open(csv_path, encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=";")
        level_cols = sorted([c for c in (reader.fieldnames or []) if c.lower().startswith("level")])
        issn_cols = [c for c in (reader.fieldnames or []) if "issn" in c.lower()]
        for row in reader:
            level = None
            for c in reversed(level_cols):  # latest non-empty year
                if (row.get(c) or "").strip():
                    level = row[c].strip()
                    break
            shaped = {"norway_level_authoritative": level,
                      "_provenance": _prov("Norwegian Register (HK-dir)", NORWEGIAN_CSV)}
            for c in issn_cols:
                issn = norm_issn(row.get(c))
                if issn:
                    out.setdefault(issn, shaped)
    return out


def download(url: str, dest: str, timeout: int = 120) -> str:
    """Download a bulk file to dest (for --fetch-bulk)."""
    print(f"  downloading {url} -> {dest}", file=sys.stderr)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    with urllib.request.urlopen(req, timeout=timeout) as r, open(dest, "wb") as out:
        raw = r.read()
        if r.headers.get("Content-Encoding") == "gzip" and not url.endswith(".zip"):
            raw = gzip.decompress(raw)
        out.write(raw)
    return dest
