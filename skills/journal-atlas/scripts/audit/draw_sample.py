# -*- coding: utf-8 -*-
"""Draw a fixed-seed random sample of claim-source pairs to audit.

Seeded so the sample is reproducible and cannot be re-drawn until it looks
good. n=30 is what fits the time available, not a power calculation, and the
paper must say so.
"""
import io, os, json, random, re

D = os.path.dirname(os.path.abspath(__file__))
pairs = json.load(io.open(os.path.join(D, "audit_pairs.json"), encoding="utf-8"))
random.seed(20260815)
sample = random.sample(pairs, 30)

for i, p in enumerate(sample, 1):
    p["id"] = i
json.dump(sample, io.open(os.path.join(D, "audit_sample.json"), "w",
          encoding="utf-8"), ensure_ascii=False, indent=1)

for p in sample:
    cl = "; ".join("%s=%s" % (k, v[:60]) for k, v in p["claims"])
    print("%2d [%s] %s :: %s" % (p["id"], p["tier"][:4], p["file"], p["section"]))
    print("     URL: %s" % p["url"])
    print("     %s" % cl[:200])
print()
print("distinct URLs to fetch:", len({p["url"] for p in sample}))
