from pathlib import Path

path = Path("STATUS.md")
text = path.read_text(encoding="utf-8")

replacements = [
    (
        "### 0. R2-B Bearer semantic quarantine — 2026-09-12",
        "### 0. R2-C supersession infrastructure — 2026-09-12",
    ),
    (
        "R2-C F3/F7 = NEXT SEPARATE GATE / NOT STARTED",
        "#955 R2-C supersession infrastructure = AUTHOR OPTION A ACCEPTED / BOUNDED GOVERNANCE LANDING\nR2-C F3/F7 = COMPLETE IN THIS LANDING\nOLD-CANONICAL REVERSE AUDIT = NEXT SEPARATE PROGRAMME STEP / NOT STARTED BY #955",
    ),
    (
        "R2-C (F3/F7) = NEXT SEPARATE GATE / NOT STARTED\nOLD-CANONICAL REVERSE AUDIT = QUEUED AFTER R2-C",
        "R2-C (F3/F7) = COMPLETE / AUTHOR A / BOUNDED GOVERNANCE LANDING IN #955\nOLD-CANONICAL REVERSE AUDIT = NEXT SEPARATE PROGRAMME STEP / NOT STARTED BY #955",
    ),
    (
        "local One / Selection-position owner = `Core_Law/SRT_One_Formation.md`\nStable ISP standing owner = P1-T06, stronger and separate",
        "local One / Selection-position owner = `Core_Law/SRT_One_Formation.md`\nOne Formation freeze class = A / EDIT-SAFETY ONLY / `draft`, `P1-candidate` UNCHANGED\nIndividuation freeze class = B / downstream hybrid / subject-entry and sigma reconstruction remain OPEN\nfreeze class != epistemic truth / P-level / theorem status / programme Level standing\ncanonical retype ledger = `Operations/Audits/SRT_CANONICAL_RETYPE_LEDGER.md` / noncanonical per-claim working surface\nStable ISP standing owner = P1-T06, stronger and separate",
    ),
    (
        "> **2026-09-12 R2-A closeout override:** the legacy reverse-audit queue below remains useful as the eventual audit path, but it is not the immediate next execution sequence. R2-B (`F2/F5/F9`) and R2-C (`F3/F7`) must be separately closed before that reverse audit proceeds. This closeout does not enter either group. #949 creator–AI final-skeleton alignment still precedes any L0 canonical rewrite.",
        "> **2026-09-12 post-R2-C override:** R2-A, R2-B and R2-C are complete. The old-canonical reverse audit is now the next separate programme step and must use `Operations/Audits/SRT_CANONICAL_RETYPE_LEDGER.md` claim by claim. This #955 closeout does not itself begin claim edits. #949 creator–AI final-skeleton alignment still precedes any L0 canonical rewrite.",
    ),
]

for old, new in replacements:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"expected exactly one STATUS match for {old!r}, got {count}")
    text = text.replace(old, new, 1)

path.write_text(text, encoding="utf-8")
print("R2-C STATUS closeout patch applied")
