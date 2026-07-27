#!/usr/bin/env python3
"""
detect_defunct.py — Find corpus entries for journals that have stopped
publishing, so the recommendation workflow stops proposing dead venues.

This is the worst failure mode this knowledge base has: an uncited score is
soft-wrong, but telling a researcher to submit to a journal that ceased in
1972 wastes their time on something impossible. GAPS_AND_NOTES.md flagged 4
such entries in a 25-entry spot check and explicitly left the full sweep
undone; cached data suggested at least 12. This does the full sweep.

Signal: OpenAlex `counts_by_year` on the Source — one request per journal,
no works pagination (the sibling scripts' works-window fetch costs hundreds
of requests for a large journal; this needs one).

Deliberately reports rather than deletes. Zero recent output is a strong
signal but not proof: OpenAlex indexing can lag for very small or
non-English venues, and a renamed journal's successor may be the thing the
entry should point to rather than something to remove. Every hit gets
classified by how confident the signal is, and the write step adds a banner
naming the evidence — it never silently drops an entry.

    python detect_defunct.py --dry-run
    python detect_defunct.py --write
"""
from __future__ import annotations
import argparse, json, os, re, sys
from datetime import date

for _s in (sys.stdout, sys.stderr):
    try: _s.reconfigure(encoding="utf-8")
    except Exception: pass

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import lint_content  # noqa: E402 - reuse collect_files/relkey
from enrich_methodology_evidence import extract_issn, _retry, normissn  # noqa: E402

try:
    from pyalex import Sources, config
except ImportError:
    print("ERROR: pyalex not installed. Run: pip install pyalex", file=sys.stderr)
    sys.exit(1)

if email := os.environ.get("OPENALEX_EMAIL"):
    config.email = email

SKILL_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
CACHE_DIR = os.path.join(os.path.dirname(__file__), "..", ".cache", "defunct-check")
REPORT_PATH = os.path.join(SKILL_ROOT, "references", "_soft_metadata_drafts", "_defunct_report.json")

THIS_YEAR = date.today().year
RECENT_WINDOW = 5          # years back to judge "still publishing"
DEAD_THRESHOLD = 0         # total works across the window to call it dead
DYING_THRESHOLD = 5        # ...or barely alive


def fetch_or_cache(issn: str) -> dict:
    os.makedirs(CACHE_DIR, exist_ok=True)
    path = os.path.join(CACHE_DIR, f"{normissn(issn)}.json")
    if os.path.exists(path):
        return json.loads(open(path, encoding="utf-8").read())

    def _fetch():
        res = Sources().filter(issn=issn).get()
        if not res:
            raise ValueError(f"no OpenAlex source for ISSN {issn}")
        return res[0]

    try:
        src, exc = _retry(_fetch)
    except Exception as exc:
        result = {"error": str(exc)}
        json.dump(result, open(path, "w", encoding="utf-8"))
        return result
    if src is None:
        return {"error": f"transient failure after retries: {exc}", "transient": True}

    counts = {c["year"]: c["works_count"] for c in (src.get("counts_by_year") or [])}
    result = {
        "display_name": src.get("display_name"),
        "issn_l": src.get("issn_l"),
        "openalex_id": src.get("id"),
        "works_count_total": src.get("works_count"),
        "counts_by_year": counts,
        "alternate_titles": src.get("alternate_titles") or [],
    }
    json.dump(result, open(path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    return result


def _norm_name(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def find_live_sibling(name: str, own_issn_l: str | None) -> dict | None:
    """Is there another OpenAlex source with the SAME journal name that is
    still publishing? If so, this entry's ISSN points at a stale/partial
    source record rather than the journal being dead.

    This distinction is the whole reason the first version of this scan was
    unusable: querying by the entry's ISSN alone reported BMJ, Philosophical
    Studies and International Journal of Design as ceased. All three are very
    much alive — their entry ISSN just resolves to a historical source whose
    data stops decades ago (BMJ's stops at 2001), while current content sits
    under a different ISSN. Publishing a "ceased publication" banner on BMJ
    would have been flatly false.
    """
    target = _norm_name(name)
    try:
        candidates, _ = _retry(lambda: Sources().search(name).get())
    except Exception:
        return None
    for s in (candidates or []):
        if _norm_name(s.get("display_name")) != target:
            continue
        if own_issn_l and s.get("issn_l") == own_issn_l:
            continue  # the same stale record we already have
        counts = {c["year"]: c["works_count"] for c in (s.get("counts_by_year") or [])}
        recent = sum(counts.get(y, 0) for y in range(THIS_YEAR - RECENT_WINDOW, THIS_YEAR + 1))
        if recent > DYING_THRESHOLD:
            return {"display_name": s.get("display_name"), "issn_l": s.get("issn_l"),
                    "issn": s.get("issn"), "openalex_id": s.get("id"), "recent_works": recent}
    return None


def classify(counts: dict[int, int]) -> tuple[str, int, int | None]:
    """(verdict, works_in_window, last_active_year)."""
    window = range(THIS_YEAR - RECENT_WINDOW, THIS_YEAR + 1)
    recent = sum(counts.get(y, 0) for y in window)
    active_years = [y for y, n in counts.items() if n > 0]
    last_active = max(active_years) if active_years else None
    if recent <= DEAD_THRESHOLD:
        return "DEAD", recent, last_active
    if recent <= DYING_THRESHOLD:
        return "NEARLY_DEAD", recent, last_active
    return "ACTIVE", recent, last_active


BANNER_MARKER = "**Publication status:**"


def process_file(path: str) -> dict:
    content = open(path, encoding="utf-8").read()
    rel = lint_content.relkey(path)
    name = (re.search(r"^# +(.+?)\s*$", content, re.MULTILINE) or [None, os.path.basename(path)])[1]

    issn = extract_issn(content)
    if not issn:
        return {"rel": rel, "name": name, "skip": "no ISSN (conference entry)"}

    data = fetch_or_cache(issn)
    if "error" in data:
        return {"rel": rel, "name": name, "issn": issn, "skip": f"lookup failed: {data['error']}"}

    counts = {int(k): v for k, v in (data.get("counts_by_year") or {}).items()}
    verdict, recent, last_active = classify(counts)
    result = {
        "path": path, "rel": rel, "name": name, "issn": issn,
        "openalex_name": data.get("display_name"),
        "verdict": verdict, "works_in_window": recent, "last_active_year": last_active,
        "works_count_total": data.get("works_count_total"),
        "already_banner": BANNER_MARKER in content,
    }
    if verdict in ("DEAD", "NEARLY_DEAD"):
        sibling = find_live_sibling(data.get("display_name") or name, data.get("issn_l"))
        if sibling:
            # Not dead — this entry is just keyed to the wrong source record.
            result["verdict"] = "STALE_ISSN"
            result["live_source"] = sibling
    return result


def build_banner(r: dict) -> str:
    last = r["last_active_year"]
    if r["verdict"] == "DEAD":
        detail = (f"OpenAlex records **no publications since {last}**" if last
                  else "OpenAlex records no publications at all for this ISSN")
        head = "Appears to have ceased publication"
    else:
        detail = (f"OpenAlex records only {r['works_in_window']} publication(s) in the last "
                  f"{RECENT_WINDOW} years (most recent {last})")
        head = "Appears largely inactive"
    return (
        f"> [!CAUTION]\n"
        f"> {BANNER_MARKER} {head} — {detail} (checked {date.today().isoformat()}, "
        f"ISSN {r['issn']}). This entry is retained for historical reference and for "
        f"rejection-fallback context, but **should not be recommended as a live submission "
        f"target**. If the title was renamed or merged, the successor journal is the correct "
        f"target; if this is an OpenAlex indexing gap rather than a real closure, please open "
        f"an issue (see [docs/GOVERNANCE.md](../../../../../docs/GOVERNANCE.md)).\n\n"
    )


def apply_results(results: list[dict]) -> None:
    today = date.today().isoformat()
    applied = skipped = 0
    for r in results:
        if r.get("verdict") not in ("DEAD", "NEARLY_DEAD") or r.get("already_banner"):
            continue
        content = open(r["path"], encoding="utf-8").read()
        m = re.search(r"^# +.+?\n", content, re.MULTILINE)
        if not m:
            skipped += 1
            continue
        at = m.end()
        content = content[:at] + "\n" + build_banner(r) + content[at:]
        row = (f"| {today} | Flagged as {'ceased' if r['verdict']=='DEAD' else 'largely inactive'}: "
               f"OpenAlex shows {r['works_in_window']} publication(s) in the last {RECENT_WINDOW} years"
               + (f" (last active {r['last_active_year']})" if r["last_active_year"] else "")
               + ". Entry retained for historical/fallback context but marked not-a-live-target; "
                 "see scripts/spine/detect_defunct.py. | @Zaious (AI-assisted) |\n")
        idx = content.rindex("## Changelog")
        cm = re.search(r"\|[-\s|]+\|\n", content[idx:])
        if cm:
            insert = idx + cm.end()
            content = content[:insert] + row + content[insert:]
        open(r["path"], "w", encoding="utf-8").write(content)
        applied += 1
    print(f"Banner added to {applied} entries ({skipped} skipped — no H1 found)", file=sys.stderr)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not args.dry_run and not args.write:
        ap.error("specify --dry-run or --write")

    if args.write:
        if not os.path.exists(REPORT_PATH):
            ap.error(f"no report at {REPORT_PATH} — run --dry-run first")
        apply_results(json.load(open(REPORT_PATH, encoding="utf-8")))
        return

    files = lint_content.collect_files([])
    import time as _time
    results = []
    for i, path in enumerate(files, 1):
        r = process_file(path)
        results.append(r)
        if r.get("verdict") in ("DEAD", "NEARLY_DEAD", "STALE_ISSN"):
            extra = (f"-> live at ISSN {r['live_source']['issn_l']}" if r.get("live_source")
                     else f"{r['works_in_window']} works since {THIS_YEAR-RECENT_WINDOW}")
            print(f"[{i}/{len(files)}] {r['verdict']:11s} {r['name'][:40]:40s} {extra}", file=sys.stderr)
        _time.sleep(0.15)

    dead = [r for r in results if r.get("verdict") == "DEAD"]
    dying = [r for r in results if r.get("verdict") == "NEARLY_DEAD"]
    skips = [r for r in results if "skip" in r]
    print(f"\n=== {len(files)} entries | {len(dead)} ceased | {len(dying)} nearly inactive | "
          f"{len(skips)} skipped ===", file=sys.stderr)
    json.dump(results, open(REPORT_PATH, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"Report -> {REPORT_PATH}", file=sys.stderr)


if __name__ == "__main__":
    main()
