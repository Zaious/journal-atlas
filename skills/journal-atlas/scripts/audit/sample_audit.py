# -*- coding: utf-8 -*-
"""Enumerate machine-checkable (claim, source URL) pairs in the corpus.

The audit the paper says it needs is: does the cited source entail the fact
drawn from it? Only pairs where a specific claim sits next to a specific URL
can be checked at all, so first count how many of those exist and where.
"""
import io, os, re, glob, collections, hashlib

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "..", "..", "references", "journals")
files = sorted(glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True))

PENDING = re.compile(r"\*?\(pending")
pairs = []
per_file = collections.Counter()

for f in files:
    t = io.open(f, encoding="utf-8").read()
    field = os.path.basename(os.path.dirname(f))
    tier = ("AI-Researched" if "AI-researched entry" in t or "AI-Researched (" in t
            else "Tier1/2")
    # Sections are '### Name' followed by a table and/or a '> Source: url' line.
    for sec in re.split(r"\n(?=### )", t):
        head = sec.split("\n", 1)[0].lstrip("# ").strip()
        # form A: a "| **Source URL** | <url> |" row inside the section table
        m = re.search(r"\|\s*\*\*Source URL\*\*\s*\|\s*(\S+)\s*\|", sec)
        # form B: a "> Source: <url>" line under the section heading
        if not m:
            m = re.search(r"^>\s*Source:\s*(https?://\S+)", sec, re.M)
        if not m:
            continue
        url = m.group(1).strip()
        if not url.startswith("http"):
            continue
        # the claim = the section's own populated rows, minus the source row
        rows = re.findall(r"\|\s*\*\*([^|*]+)\*\*\s*\|\s*([^|]+?)\s*\|", sec)
        claims = [(k.strip(), v.strip()) for k, v in rows
                  if not PENDING.search(v) and k.strip().lower() != "source url"]
        if not claims:
            continue
        pairs.append(dict(file=os.path.relpath(f, ROOT).replace("\\", "/"),
                          field=field, tier=tier, section=head, url=url,
                          claims=claims))
        per_file[os.path.relpath(f, ROOT)] += 1

print("entries scanned          :", len(files))
print("entries with >=1 pair    :", len(per_file))
print("checkable claim-URL pairs:", len(pairs))
print()
print("by section:")
for k, v in collections.Counter(p["section"] for p in pairs).most_common(10):
    print("  %-32s %4d" % (k, v))
print()
print("by tier:")
for k, v in collections.Counter(p["tier"] for p in pairs).most_common():
    print("  %-32s %4d" % (k, v))
print()
print("distinct source hosts:", len({re.sub(r"^https?://([^/]+).*", r"\1", p["url"]) for p in pairs}))

import json
json.dump(pairs, io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
          "audit_pairs.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
