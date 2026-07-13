"""
Apply the 148 proposed surgical patches from the careful per-file merge, with
strict verification: only apply a change if old_snippet appears EXACTLY ONCE
in the current file content (byte-for-byte). If it appears 0 or >1 times,
skip and log for manual review rather than guessing.
"""
import json

proposals = json.load(open("_merge_patch_proposals.json", encoding="utf-8"))

applied, skipped_notfound, skipped_multiple, skipped_identical = [], [], [], []

for r in proposals:
    path = r["md_path"]
    changes = r.get("changes") or []
    if not changes:
        continue
    try:
        content = open(path, encoding="utf-8").read()
    except FileNotFoundError:
        skipped_notfound.append((path, "FILE NOT FOUND", r.get("name")))
        continue

    for ch in changes:
        old = ch.get("old_snippet", "")
        new = ch.get("new_value", "")
        field = ch.get("field", "?")
        if not old:
            continue
        count = content.count(old)
        if count == 0:
            skipped_notfound.append((path, field, r.get("name")))
        elif count > 1:
            skipped_multiple.append((path, field, r.get("name"), count))
        elif old == new:
            skipped_identical.append((path, field, r.get("name")))
        else:
            content = content.replace(old, new, 1)
            applied.append((path, field, r.get("name"), ch.get("source", ""), ch.get("confidence", "")))

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)

print(f"applied: {len(applied)}")
print(f"skipped (snippet not found verbatim): {len(skipped_notfound)}")
print(f"skipped (snippet appears >1 time, ambiguous): {len(skipped_multiple)}")
print(f"skipped (old==new, no-op): {len(skipped_identical)}")

print("\n=== applied changes ===")
for path, field, name, source, conf in applied:
    print(f"  [{conf}] {name} :: {field}")

print("\n=== skipped: not found verbatim (needs manual check) ===")
for path, field, name in skipped_notfound:
    print(f"  {name} :: {field}  ({path})")

print("\n=== skipped: ambiguous (appears multiple times) ===")
for path, field, name, count in skipped_multiple:
    print(f"  {name} :: {field}  (appears {count}x)  ({path})")

json.dump({
    "applied": [{"path": p, "field": f, "name": n, "source": s, "confidence": c} for p, f, n, s, c in applied],
    "skipped_notfound": [{"path": p, "field": f, "name": n} for p, f, n in skipped_notfound],
    "skipped_multiple": [{"path": p, "field": f, "name": n, "count": c} for p, f, n, c in skipped_multiple],
}, open("_apply_log.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
