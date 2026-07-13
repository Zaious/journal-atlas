#!/usr/bin/env python3
"""
Merge WO2 (soft-metadata AI-research) drafts + the spine (journal_spine.db) into
new curated `.md` entries under `references/journals/<field>/`, for journals
that don't have one yet.

Deliberately does NOT touch existing .md files (114 journals already have one —
those need a separate, careful patch pass, not a templated overwrite, since some
are hand-curated Tier 1 entries with subjective content WO2 has no equivalent
for). This script only CREATES new entries.

Design: renders the fixed TEMPLATE.md v1.3 structure. Fields with no data in
either the spine or the WO2 draft are marked "(pending)" — same convention as
existing entries — rather than invented. New entries get a distinct banner
("AI-Researched, WO2") instead of "Tier 1" / "Tier 2 (community estimate)",
since the evidence basis differs: per-journal sourced facts with per-field
signal_quality, not family-level estimates, but also not the deep manual
evidence-harvesting behind the original 11 Tier 1 entries.

Usage:
    python merge_soft_metadata.py --dry-run                 # preview N samples, write nothing
    python merge_soft_metadata.py --dry-run --sample 5
    python merge_soft_metadata.py --write                   # actually create the new .md files
"""
from __future__ import annotations
import argparse, json, re, sqlite3, sys, glob, os
from datetime import date

for _s in (sys.stdout, sys.stderr):
    try: _s.reconfigure(encoding="utf-8")
    except Exception: pass

REPO_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
SKILL_ROOT = os.path.join(REPO_ROOT, "skills", "journal-atlas")
CONSOLIDATED = os.path.join(SKILL_ROOT, "references", "_soft_metadata_drafts", "consolidated_all.json")
SPINE_DB = os.path.join(os.path.dirname(__file__), "journal_spine.db")
JOURNALS_DIR = os.path.join(SKILL_ROOT, "references", "journals")

# priority order for placing a NEW cross-listed journal (existing files keep their existing location)
DOMAIN_DIR_PRIORITY = ["philosophy", "hci", "psychology"]


def normissn(s):
    if not s: return None
    s = re.sub(r"[^0-9Xx]", "", str(s)).upper()
    return s if len(s) == 8 else None


def hyphenate(issn8):
    return f"{issn8[:4]}-{issn8[4:]}" if issn8 and len(issn8) == 8 else issn8


MAX_SLUG_LEN = 80  # guards against Windows MAX_PATH when a WO2 draft's "name" field
                    # includes a long parenthetical (e.g. "X (formerly Y; publisher Z)")


def slugify(name: str) -> str:
    s = name.lower()
    s = s.replace("&", "and")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    if len(s) > MAX_SLUG_LEN:
        s = s[:MAX_SLUG_LEN].rsplit("-", 1)[0]
    return s


def index_existing_issns():
    existing = {}
    for fp in glob.glob(os.path.join(JOURNALS_DIR, "**", "*.md"), recursive=True):
        txt = open(fp, encoding="utf-8").read()
        for i in re.findall(r"\*\*ISSN \((?:Print|Online)\)\*\*\s*\|\s*([0-9]{4}-[0-9]{3}[0-9Xx])", txt):
            n = normissn(i)
            if n:
                existing[n] = fp
    return existing


def pick_domain_dir(domains):
    for d in DOMAIN_DIR_PRIORITY:
        if d in domains:
            return d
    return domains[0] if domains and domains[0] != "bonus" else "psychology"


def fmt(v, fallback="*(pending)*"):
    if v is None or v == "" or v == []:
        return fallback
    if isinstance(v, list):
        return "; ".join(str(x) for x in v)
    return str(v)


def fmt_num(v, fallback="*(pending)*", digits=2):
    if v is None:
        return fallback
    try:
        return f"{float(v):.{digits}f}"
    except (TypeError, ValueError):
        return str(v)


def issn_variants(conn, issn_l):
    rows = conn.execute("SELECT issn FROM issn_index WHERE issn_l=?", (issn_l,)).fetchall()
    return sorted({r[0] for r in rows} | {issn_l})


def render_entry(e: dict, spine: dict, conn, today: str) -> str:
    name = e["name"]
    issn_l = spine["issn_l"]
    variants = [v for v in issn_variants(conn, issn_l) if v != issn_l]
    issn_print = hyphenate(issn_l)
    issn_online = hyphenate(variants[0]) if variants else "*(pending)*"

    sq = e.get("overall_signal_quality")
    domains = e.get("domains", [])

    ai = e.get("ai_policy") or {}
    pr = e.get("peer_review") or {}
    pp = e.get("preprint") or {}
    pos = e.get("positioning") or {}
    exp = e.get("experiential") or {}
    blanks = e.get("blanks") or []
    xlang = e.get("cross_language_checked") or []

    topics = json.loads(spine["topics_json"] or "[]")
    topics_rows = "\n".join(
        f"| {t.get('name','?')} | {t.get('count','?')} |" for t in topics[:10]
    ) or "| *(pending)* | |"

    tier_facts = []
    if spine.get("cas_zone"):
        tier_facts.append(f"CAS 中科院分区: {spine['cas_zone']} ({spine.get('cas_broad_category') or '?'})")
    if spine.get("jufo_level") not in (None, ""):
        tier_facts.append(f"JUFO (Finland): level {spine['jufo_level']}")
    if spine.get("norway_level") not in (None, ""):
        tier_facts.append(f"Norwegian Register: level {spine['norway_level']}")
    tier_line = "; ".join(tier_facts) if tier_facts else "*(pending)*"

    oa_model = "Full OA" if spine.get("is_oa") else ("Hybrid/Unknown" if spine.get("is_in_doaj") else "*(pending)*")
    apc = spine.get("oa_apc_amount") or spine.get("apc_usd")
    apc_cur = spine.get("oa_apc_currency") or ("USD" if spine.get("apc_usd") else "")
    apc_line = f"{apc} {apc_cur}".strip() if apc else "*(pending)*"

    ai_policy_url = ai.get("source_url") or "*(pending)*"
    ai_summary = fmt(ai.get("summary"))
    ai_leniency = fmt(ai.get("leniency_1_5"))
    ai_gate = fmt(ai.get("gate"))

    peer_review_type = fmt(pr.get("type"))
    peer_review_url = pr.get("source_url") or ""

    preprint_note = fmt(pp.get("allowed"))
    preprint_url = pp.get("source_url") or ""

    accepts_now = fmt(pos.get("accepts_now"))
    framing = fmt(pos.get("framing_required"))
    methods_welcome = pos.get("methods_welcome") or []
    methods_line = ", ".join(methods_welcome) if methods_welcome else "*(pending)*"
    pos_sources = pos.get("sources") or []

    review_time = fmt(exp.get("review_time_months"))
    desk_reject = fmt(exp.get("desk_reject_pct"))
    acceptance_note = fmt(exp.get("acceptance_note"))
    reviewer_culture = fmt(exp.get("reviewer_culture"))
    exp_sources = exp.get("sources") or []

    blanks_md = "\n".join(f"- **{b.get('field','?')}**: {b.get('why','')}" for b in blanks) or "*(none recorded)*"
    xlang_md = "\n".join(f"- {x}" for x in xlang) or "*(not recorded)*"
    all_sources = sorted(set(pos_sources) | set(exp_sources) | ({ai_policy_url} if ai_policy_url != "*(pending)*" else set()))
    sources_md = "\n".join(f"- {u}" for u in all_sources) or "*(none)*"

    return f"""<!-- schema: v1.3 -->
<!-- AI-researched entry (WO2 pipeline) — Journal Atlas v2. See docs/ATLAS_V2_DESIGN.md and docs/workorders/WO2_SOFT_METADATA_BATCH.md. -->
<!-- Generated by scripts/spine/merge_soft_metadata.py on {today}. -->

# {name}

> **Last verified**: {today}
> **Maintainer**: @Zaious
> **Venue type**: Journal
> **Evidence basis**: AI-researched (WO2), overall signal_quality **{fmt(sq, "0")}/5** — per-journal sourced facts with honest blanks, distinct from "Tier 1" (deep manual evidence-harvesting) and "Tier 2" (family-level community estimate). See [SEED_DATA_QUALITY.md](../../../../SEED_DATA_QUALITY.md).

---

## Identity

| Field | Value |
|-------|-------|
| **Abbreviation** | *(pending)* |
| **Venue type** | Journal |
| **Publisher** | {fmt(spine.get('publisher'))} |
| **ISSN (Print)** | {issn_print} |
| **ISSN (Online)** | {issn_online} |
| **Founded** | *(pending)* |
| **URL** | {fmt(spine.get('homepage'))} |
| **Author / Submission Guidelines** | {ai_policy_url if ai_policy_url != "*(pending)*" else peer_review_url or "*(pending)*"} |
| **Society / Association** | *(pending)* |
| **Editorial Board Location** | *(pending)* |

---

## Metrics

> Source: OpenAlex + JUFO + CAS 中科院分区 + Norwegian Register (spine, snapshot {spine.get('built_on', today)}) + WO2 AI-research (experiential facts, cited per-field below).

| Metric | Value | Date |
|--------|-------|------|
| **Impact Factor** | *(pending — not baked in; JCR is subscription-only, see docs/ATLAS_V2_DESIGN.md §6.1)* | |
| **5-Year IF** | *(pending)* | |
| **h-index** | {fmt(spine.get('h_index'))} | {spine.get('built_on', today)} (OpenAlex, via spine) |
| **2-Year Mean Citedness** | {fmt_num(spine.get('two_yr_citedness'))} | {spine.get('built_on', today)} (OpenAlex, via spine) |
| **CiteScore** | *(pending)* | |
| **Acceptance Rate** | {acceptance_note} | WO2 (see Reviewer Pool Characteristics sources) |
| **Desk Rejection Rate** | {desk_reject} | WO2 |
| **Quality-tier facts (not JCR/SJR quartile)** | {tier_line} | {spine.get('built_on', today)} (spine) |

### Review Cycle Time

| Stage | Typical Time | Notes |
|-------|-------------|-------|
| **Time to first decision** | *(pending)* | |
| **Time to first review** | *(pending)* | |
| **Time to acceptance (total)** | {review_time} | WO2 research (see sources below); may be a range/qualitative note, not a precise figure |
| **Time to publication (after acceptance)** | *(pending)* | |

### Publication Frequency

| Aspect | Detail |
|--------|--------|
| **Schedule** | *(pending)* |
| **Articles per year (approx.)** | *(pending)* |
| **Special issues?** | *(pending)* |

---

## Policies

### Peer Review

| Aspect | Detail |
|--------|--------|
| **Type** | {peer_review_type} |
| **Transferable / Cascade?** | *(pending)* |
| **Reviewer reports published?** | *(pending)* |
| **Typical R+R rounds** | *(pending)* |
| **Reviewer recommendations** | *(pending)* |

> Source: {peer_review_url or "*(pending)*"}

### AI Policy

| Aspect | Detail |
|--------|--------|
| **Has journal-specific AI policy?** | *(see summary — WO2 defaults to publisher-level policy unless a journal-specific override was found)* |
| **Explicit permission gate?** | {ai_gate} |
| **Leniency (1-5)** | {ai_leniency} |
| **Summary** | {ai_summary} |
| **Source URL** | {ai_policy_url} |

### Preprint Policy

> WO2 research note (not broken down per-stage — see docs/workorders/WO2_SOFT_METADATA_BATCH.md for why): {preprint_note}
> Source: {preprint_url or "*(pending)*"}

| Stage | Allowed? | Notes |
|-------|----------|-------|
| Pre-submission | *(see note above)* | |
| Under review | *(pending)* | |
| Post-acceptance (AAM) | *(pending)* | |
| Version of Record | *(pending)* | |

### Open Access

| Aspect | Detail |
|--------|--------|
| **Model** | {oa_model} |
| **APC (if OA chosen)** | {apc_line} |
| **Read & Publish agreements** | *(pending)* |

---

## Format

| Aspect | Detail |
|--------|--------|
| **Article types accepted** | *(pending)* |
| **Word limit** | *(pending)* |
| **Word limit negotiability** | *(pending)* |
| **Abstract limit** | *(pending)* |
| **Reference limit** | *(pending)* |
| **Supplementary material** | *(pending)* |
| **Figure/Table limits** | *(pending)* |

---

## Subject Density

> Source: OpenAlex per-source topics (spine, CC0, no LLM inference — see docs/ATLAS_V2_DESIGN.md §2 Layer P). Snapshot {spine.get('built_on', today)}.

### Top Topics

| Topic | Article Count |
|-------|--------------|
{topics_rows}

### Orientation

| Dimension | Assessment |
|-----------|------------|
| **Empirical vs. Theoretical** | *(pending — no evidentiary basis collected by WO2 pipeline; would require reading a sample of recent articles)* |
| **Quantitative vs. Qualitative** | *(pending)* |
| **Cross-disciplinary openness** | *(pending)* |

**Current positioning (WO2, what the journal accepts now):** {accepts_now}

**Methods noted as welcome (WO2, qualitative — not a scored 0-5 table, see Methodological Preferences below):** {methods_line}

---

## Soft Metadata

> [!NOTE]
> **AI-Researched (WO2 pipeline, {today})** — the fields below were researched per-journal from public sources (publisher policy pages, recent publications, SciRev, and mandatory cross-language checks against 小木虫/fabiaoji/知乎) rather than adapted from a family-level template. Every populated field cites its source; fields with no public evidence were left `(pending)` rather than estimated — see "AI-Research Notes" at the end of this section for exactly what was checked and why any field is blank. This entry's overall `signal_quality` is **{fmt(sq, "0")}/5**. This is a *different* evidence basis than "Tier 1" (deep manual evidence-harvesting) or "Tier 2" (family-level community estimate) — see [SEED_DATA_QUALITY.md](../../../../SEED_DATA_QUALITY.md).

### Epistemological & Political Leanings

*(pending — WO2 does not estimate subjective political/epistemological leanings without a specific public source; none was found. A future contributor with submission/review experience can fill this in via `/ja-validate`.)*

### Framing Requirements

- **Mandatory framing?** *(pending — see "Current positioning" and "Framing requirement" note below)*
- **Framing requirement noted by WO2 research:** {framing}
- **Consequences of ignoring it**: *(pending)*

### Methodological Preferences

*(pending — WO2 intentionally does not assign 0-5 receptiveness scores without per-method evidence; see "Methods noted as welcome" above for the qualitative, unscored finding.)*

### Voice & Style

*(pending — no evidentiary basis collected)*

### Reviewer Pool Characteristics

{reviewer_culture if reviewer_culture != "*(pending)*" else "*(pending — no first-hand reviewer-culture source found; see AI-Research Notes below for what was checked, including cross-language forums.)*"}

### Sensitive Topics

*(pending — no evidentiary basis collected by WO2 pipeline)*

### Practical Concerns

*(pending — no evidentiary basis collected; IRB requirements, OPSEC compatibility, and independent-scholar friendliness were not part of the WO2 research scope)*

### AI-Research Notes (WO2 pipeline — sources, blanks, and cross-language checks)

**Sources cited across this entry:**
{sources_md}

**Fields deliberately left blank, and why:**
{blanks_md}

**Cross-language checks performed (mandatory per WO2 rules):**
{xlang_md}

---

## Strategic Notes

> Not part of the WO2 research scope — these require either deep evidence-harvesting or community contribution. See [CONTRIBUTING.md](../../../../CONTRIBUTING.md).

### Hard Blockers

*(pending)*

### Soft Tax

*(pending)*

### Best Suited For

*(pending)*

### Not Recommended For

*(pending)*

### Rejection Fallback Chain

*(pending — no fallback-chain research performed by WO2)*

---

## Changelog

| Date | Change | By |
|------|--------|----|
| {today} | Auto-generated: Identity/Metrics/Subject Density from spine (OpenAlex + JUFO + CAS + Norwegian Register + DOAJ, snapshot {spine.get('built_on', today)}); Policies/Positioning/Experiential Soft Metadata from WO2 AI-research pipeline (signal_quality {fmt(sq,'0')}/5). Subjective Soft Metadata subsections (political leanings, sensitive topics, voice/style, scored methodology preferences) and Strategic Notes intentionally left pending — no evidentiary basis collected by this pipeline. | @Zaious |
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--sample", type=int, default=3)
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not args.dry_run and not args.write:
        ap.error("specify --dry-run or --write")

    consolidated = json.load(open(CONSOLIDATED, encoding="utf-8"))
    existing = index_existing_issns()
    conn = sqlite3.connect(SPINE_DB)
    conn.row_factory = sqlite3.Row

    today = date.today().isoformat()
    new_entries = []
    for e in consolidated["entries"]:
        issn = normissn(e.get("issn"))
        if not issn or issn in existing:
            continue
        row = conn.execute("SELECT * FROM journals WHERE issn_l=?", (issn,)).fetchone()
        if not row:
            r2 = conn.execute("SELECT issn_l FROM issn_index WHERE issn=?", (issn,)).fetchone()
            row = conn.execute("SELECT * FROM journals WHERE issn_l=?", (r2["issn_l"],)).fetchone() if r2 else None
        if row:
            new_entries.append((e, dict(row)))

    print(f"{len(new_entries)} new journals to render (of {len(consolidated['entries'])} total consolidated)", file=sys.stderr)

    written, skipped_domain = [], []
    for e, spine in new_entries:
        domains = [d for d in e.get("domains", []) if d != "bonus"]
        domain_dir = pick_domain_dir(domains) if domains else "psychology"
        slug = slugify(e["name"])
        rel = os.path.join("references", "journals", domain_dir, f"{slug}.md")
        abspath = os.path.join(SKILL_ROOT, rel)

        if args.dry_run:
            written.append((rel, e, spine))
        else:
            os.makedirs(os.path.dirname(abspath), exist_ok=True)
            content = render_entry(e, spine, conn, today)
            with open(abspath, "w", encoding="utf-8") as fh:
                fh.write(content)
            written.append(rel)

    if args.dry_run:
        import random
        random.seed(7)
        sample = random.sample(written, min(args.sample, len(written)))
        for rel, e, spine in sample:
            print(f"\n{'='*100}\n{rel}\n{'='*100}")
            print(render_entry(e, spine, conn, today))
        print(f"\n\n[dry-run] would write {len(written)} new files. Showed {len(sample)} samples above.", file=sys.stderr)
    else:
        print(f"wrote {len(written)} new journal entries.", file=sys.stderr)
        from collections import Counter
        by_dir = Counter(rel.split(os.sep)[2] for rel in written)
        print("by field directory:", dict(by_dir), file=sys.stderr)


if __name__ == "__main__":
    main()
