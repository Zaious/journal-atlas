"""
One-off: strip the internal work-order codename "WO2" from all OUTPUT-facing
text (rendered .md content), keeping the "AI-Researched" label and its
methodology description intact. Applied to:
  1. The two template scripts (so future regenerations don't reintroduce it).
  2. All already-written curated .md files (236 new + 112 patched).
  3. README.md / README.zh-Hant.md / SEED_DATA_QUALITY.md.
Does NOT touch internal dev comments/docstrings in .py files, or docs/workorders/
(those are internal project-management artifacts, not product output), or
_soft_metadata_drafts/ (explicitly internal scratch/audit trail).
"""
import glob
import re

REPLACEMENTS = [
    # order matters: longer/more specific patterns first
    (r"AI-researched entry \(WO2 pipeline\) — Journal Atlas v2\. See docs/ATLAS_V2_DESIGN\.md and docs/workorders/WO2_SOFT_METADATA_BATCH\.md\.",
     "AI-researched entry — Journal Atlas v2 coverage pipeline. See docs/ATLAS_V2_DESIGN.md for methodology."),
    (r"AI-researched \(WO2\), overall signal_quality", "AI-researched, overall signal_quality"),
    (r"\+ WO2 AI-research \(experiential facts, cited per-field below\)\.",
     "+ AI research (experiential facts, cited per-field below)."),
    (r"WO2 \(see Reviewer Pool Characteristics sources\)", "AI research (see Reviewer Pool Characteristics sources)"),
    (r"\| WO2 \|", "| AI research |"),
    (r"WO2 research \(see sources below\)", "AI research (see sources below)"),
    (r"WO2 defaults to publisher-level policy unless a journal-specific override was found",
     "defaults to publisher-level policy unless a journal-specific override was found"),
    (r"WO2 research note \(not broken down per-stage — see docs/workorders/WO2_SOFT_METADATA_BATCH\.md for why\)",
     "AI-research note (not broken down per-stage)"),
    (r"no evidentiary basis collected by WO2 pipeline", "no evidentiary basis collected"),
    (r"no evidentiary basis collected; IRB requirements, OPSEC compatibility, and independent-scholar friendliness were not part of the WO2 research scope",
     "no evidentiary basis collected; IRB requirements, OPSEC compatibility, and independent-scholar friendliness were not part of this pipeline's research scope"),
    (r"Current positioning \(WO2, what the journal accepts now\)", "Current positioning (what the journal accepts now)"),
    (r"Methods noted as welcome \(WO2, qualitative", "Methods noted as welcome (qualitative"),
    (r"\*\*AI-Researched \(WO2 pipeline, \{today\}\)\*\*", '**AI-Researched ({today})**'),
    (r"AI-Researched \(WO2 pipeline, ", "AI-Researched ("),
    (r"WO2 does not estimate subjective political/epistemological leanings",
     "This pipeline does not estimate subjective political/epistemological leanings"),
    (r"Framing requirement noted by WO2 research:", "Framing requirement noted by AI research:"),
    (r"WO2 intentionally does not assign 0-5", "This pipeline intentionally does not assign 0-5"),
    (r"Not part of the WO2 research scope", "Not part of this pipeline's research scope"),
    (r"AI-Research Notes \(WO2 pipeline — sources, blanks, and cross-language checks\)",
     "AI-Research Notes (sources, blanks, and cross-language checks)"),
    (r"mandatory per WO2 rules\)", "mandatory per methodology)"),
    (r"no fallback-chain research performed by WO2", "no fallback-chain research performed"),
    (r"Policies/Positioning/Experiential Soft Metadata from WO2 AI-research pipeline",
     "Policies/Positioning/Experiential Soft Metadata from AI research"),
    (r"AI-Research Notes \(WO2 supplement, ", "AI-Research Notes (supplementary AI research, "),
    (r'MARKER = "AI-Research Notes \(WO2 supplement"', 'MARKER = "AI-Research Notes (supplementary AI research"'),
    (r"Added by `scripts/spine/patch_existing_entries\.py` as a \*\*supplementary, independent research pass\*\*",
     "Added as a **supplementary, independent research pass**"),
    (r"WO2 AI policy finding:", "AI-research finding (policy):"),
    (r"WO2 positioning finding \(what the journal accepts now\):", "AI-research finding (positioning — what the journal accepts now):"),
    (r"WO2 experiential finding:", "AI-research finding (experiential):"),
    (r"Fields WO2 could not find evidence for:", "Fields no evidence was found for:"),
    (r"Overall WO2 `signal_quality` for this pass:", "Overall `signal_quality` for this pass:"),
    (r"AI-Researched\s+\(per-journal AI research with cited `signal_quality`, v2 coverage-first pivot\)",
     "AI-Researched (per-journal AI research with cited `signal_quality`, v2 coverage-first pivot)"),  # no-op safety net, README already clean of literal WO2
    # generic catch-all for anything left with a bare "WO2" token in OUTPUT text
    (r"\bWO2\b", "AI-research"),
]


def apply(path: str) -> bool:
    text = open(path, encoding="utf-8").read()
    orig = text
    for pattern, repl in REPLACEMENTS:
        text = re.sub(pattern, repl, text)
    if text != orig:
        open(path, "w", encoding="utf-8").write(text)
        return True
    return False


def main():
    targets = []
    targets += glob.glob("../../references/journals/**/*.md", recursive=True)
    targets += ["merge_soft_metadata.py", "patch_existing_entries.py"]
    targets += ["../../../../README.md", "../../../../README.zh-Hant.md", "../../../../SEED_DATA_QUALITY.md"]

    changed = 0
    for t in targets:
        if apply(t):
            changed += 1
    print(f"changed {changed}/{len(targets)} files")


if __name__ == "__main__":
    main()
