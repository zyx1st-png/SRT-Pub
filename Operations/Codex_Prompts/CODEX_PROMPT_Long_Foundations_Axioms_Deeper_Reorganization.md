---
id: CODEX-PROMPT-LONG-FOUNDATIONS-AXIOMS-DEEPER-REORGANIZATION-2026-04-27
type: codex_prompt
tags:
  - Codex
  - Claude-Code
  - Philosophy
  - Long-Files
  - Foundations
  - Axioms
  - Deeper-Reorganization
  - Safe-Patching
  - Legacy-Preservation
  - PH-SS
status: ready_for_codex
layer: operations
epistemic_layer: workflow
claim_mode: prompt
claim_level: P5
canonical: false
date: 2026-04-27
dependency:
  - SRT_NEXT_OPTIMIZATION_TODO.md
  - Philosophy/SRT_Philosophy_Foundations.md
  - Philosophy/_SRT_Phil_Axioms.md
  - Philosophy/SRT_Philosophy_Foundations_CompactCore.md
  - Philosophy/_SRT_Phil_Axioms_PH_SS_Guardrails.md
  - Philosophy/PH_SS_Hardening_Audit_2026-04-27.md
machine_summary: >
  Root-level Claude Code / Codex prompt for optional deeper reorganization of the long Philosophy
  Foundations and Axioms files. It instructs the agent to audit first, produce a reorganization plan,
  preserve legacy material, avoid whole-file rewrites, and perform only small reviewable structural
  patches if safe. It must not change formulas, canonical claims, or companion/canonical boundaries.
---

# Codex / Claude Code Prompt — Long Foundations + Axioms Deeper Reorganization

> **Use this from repository root**: `zyx1st-png/SRT-Pub`  
> **Purpose**: Evaluate whether the long Philosophy Foundations and Axioms files should be reorganized into clearer sections.  
> **Critical rule**: Do **not** rewrite whole files. Do **not** delete legacy material. Do **not** alter formulas. Do **not** promote bridge / companion material to canonical status.

---

## Prompt to Claude Code / Codex

You are working in the `zyx1st-png/SRT-Pub` repository.

Your task is an **optional deeper reorganization pass** for two long Philosophy files:

```text
Philosophy/SRT_Philosophy_Foundations.md
Philosophy/_SRT_Phil_Axioms.md
```

The goal is not to rewrite SRT philosophy. The goal is to make the long files easier for humans and machines to navigate while preserving historical / legacy material.

This pass has two modes:

```text
Mode 1: audit-only plan
Mode 2: small structural patch, only if clearly safe
```

Default to **Mode 1** unless the safe patch is small and obvious.

---

## 0. Verify repository state

Before editing, report:

```bash
git remote -v
git branch --show-current
git rev-parse HEAD
git status --short
```

If not on `zyx1st-png/SRT-Pub` and branch `main`, stop and report the mismatch.

---

## 1. Read context files first

Read these files before auditing:

```text
SRT_NEXT_OPTIMIZATION_TODO.md
SRT_Terminology_Consistency_Audit.md
Core/SRT_Validation_Template.md
Philosophy/PH_SS_Hardening_Audit_2026-04-27.md
Philosophy/SRT_Philosophy_Hardening_TODO.md
Philosophy/SRT_Philosophy_Foundations_CompactCore.md
Philosophy/_SRT_Phil_Axioms_PH_SS_Guardrails.md
Philosophy/SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md
Philosophy/SRT_Philosophy_Tradition_Comparison_PH_SS.md
Philosophy/SRT_Subjecthood_Threshold_Interface.md
Philosophy/SRT_Philosophy_Public_OnePager.md
```

If any context file is missing, report it and continue with visible files. Do not create replacements.

---

## 2. Audit target files

Audit:

```text
Philosophy/SRT_Philosophy_Foundations.md
Philosophy/_SRT_Phil_Axioms.md
```

For each file, identify:

```text
current frontmatter status;
current read-first / pointer sections;
major existing sections;
duplicate or overlapping sections;
legacy sections already marked;
formula-role labels already present;
sections that should remain historical;
sections that are current hardened reading;
sections that should link to compact core / companion files;
sections where reordering would help;
sections where reordering is risky.
```

---

## 3. Desired future structure

Use this as a target shape, not a forced rewrite.

```text
Part A — Current Hardened Reading
Part B — Formal / Semi-formal Claims
Part C — Tradition Interface
Part D — Objection and Withdrawal Conditions
Part E — Legacy Notes / Preserved Drafts
```

### Part A — Current Hardened Reading

Should include or point to:

```text
Compact Core v4;
selection realism;
layered realism;
anti-relativist constraint realism;
L0 / L1 / L2 guardrails;
PH-SS direct pointers;
Current Reading Map.
```

### Part B — Formal / Semi-formal Claims

Should contain formulas, theorem-like statements, axioms, and formal bridge models.

Must preserve formula-role labels.

### Part C — Tradition Interface

Should contain comparisons to:

```text
Kant;
phenomenology;
Whitehead;
pragmatism;
constructivism;
physicalism;
FEP / PP;
IIT / GNW;
panpsychism;
social ontology.
```

If already covered elsewhere, add pointer rather than duplicating.

### Part D — Objection and Withdrawal Conditions

Should contain or point to:

```text
Objection Ledger;
O-Phil-11..20;
PH-SS Crosswalk;
validation conditions;
failure / narrowing conditions.
```

### Part E — Legacy Notes / Preserved Drafts

Should contain older, stronger, duplicated, poetic, or historically useful material.

Do not delete this material. Mark it as preserved legacy when needed.

---

## 4. Mode 1 — Audit-only plan

First produce an audit plan in your report or, if useful, create a small file:

```text
Philosophy/Long_Foundations_Axioms_Reorganization_Plan_2026-04-27.md
```

Only create this file if the plan is substantial enough to preserve.

Plan should include:

```text
file-by-file section map;
proposed target part for each existing section;
sections safe to move;
sections risky to move;
sections that should remain legacy;
sections needing only pointer / label;
recommended patch sequence;
what not to touch.
```

If the files are too large or ambiguous, stop after Mode 1 and do not patch.

---

## 5. Mode 2 — Small structural patch, only if clearly safe

Only do Mode 2 if the safe patch is small and obvious.

Allowed small patches:

```text
add a top-level section table of contents;
add Part A/B/C/D/E anchor headings without moving content;
add “this section belongs to Part E legacy” labels;
add “see Compact Core / companion file” pointers;
add a brief Current Structure note;
add a brief Future Reorganization Plan section;
update TODO after audit.
```

Forbidden patches:

```text
move large blocks;
rewrite paragraphs;
delete duplicates;
merge companion content into owner files;
change formulas;
change claim levels;
turn legacy into current canonical prose;
create a completely new version of the long file.
```

If you are unsure, do not patch the long files.

---

## 6. Suggested safe patch pattern

If the top of each long file does not already include a clear structure note, add a short note after frontmatter and existing PH-SS pointer sections:

```md
## Long-File Structure Note

This file preserves multiple historical layers of SRT philosophy. For current hardened reading, start with:

- `SRT_Philosophy_Foundations_CompactCore.md`
- `_SRT_Phil_Axioms_PH_SS_Guardrails.md`
- `SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md`
- `PH_SS_Hardening_Audit_2026-04-27.md`

Future deeper reorganization should use this target structure:

1. Part A — Current Hardened Reading
2. Part B — Formal / Semi-formal Claims
3. Part C — Tradition Interface
4. Part D — Objection and Withdrawal Conditions
5. Part E — Legacy Notes / Preserved Drafts

Do not read older sections as overriding the current PH-SS guardrails.
```

If a similar note already exists, do not duplicate it.

---

## 7. TODO update rules

If you only create an audit plan and do not edit long files, update `90_Backstage/Plans_Archive/SRT_NEXT_OPTIMIZATION_TODO.md` minimally:

```text
Long Foundations / Axioms deeper reorganization -> audit plan created; structural patch not yet executed
```

If you add small structure notes but do not actually reorganize content, say:

```text
Long Foundations / Axioms deeper reorganization -> structure notes added; full reorganization not yet executed
```

Do **not** mark deep reorganization fully done unless the long files are actually reorganized and reviewed.

If updating TODO:

- bump `active_v13` to `active_v14` if current;
- add the new plan file to dependency if created;
- keep status of deeper reorganization as optional / not complete unless truly done.

---

## 8. Diff and safety review

After any edits, run:

```bash
git diff -- Philosophy/SRT_Philosophy_Foundations.md Philosophy/_SRT_Phil_Axioms.md Philosophy/Long_Foundations_Axioms_Reorganization_Plan_2026-04-27.md SRT_NEXT_OPTIMIZATION_TODO.md
```

Confirm:

```text
No large moves unless explicitly intended and reviewed.
No whole-file rewrites.
No deletions.
No formula changes.
No canonical status promotion.
Legacy material preserved.
Plan distinguishes safe vs risky reorganization.
TODO does not claim full completion unless actually completed.
```

---

## 9. Commit message

Use one of these:

```text
Plan deeper reorganization for Philosophy Foundations and Axioms
```

or, if small structure notes are added:

```text
Add structure notes for long Philosophy Foundations and Axioms
```

---

## 10. Final report format

Report:

```text
Repository / branch verified:
- ...

Mode used:
- Mode 1 audit-only / Mode 2 small structural patch

Files audited:
- Philosophy/SRT_Philosophy_Foundations.md
- Philosophy/_SRT_Phil_Axioms.md

Plan file created:
- yes/no, path

Patched files:
- ...

Main findings:
- current hardened sections:
- formal / semi-formal sections:
- tradition interface sections:
- objection / withdrawal sections:
- legacy sections:
- risky sections not moved:

Safety checks:
- Full-file rewrites performed: no
- Large block moves: no / list
- Deletions: none
- Formulas altered: no
- Canonical claims promoted: no
- Legacy preserved: yes

TODO updated:
- yes/no

Remaining follow-up:
- optional deeper reorganization still not executed / or next safe patch sequence
```

---

## 11. Completion standard

This task is complete when there is either:

```text
A clear audit plan for reorganizing long Foundations / Axioms safely;
```

or:

```text
Small structure notes / anchor headings added without moving large content.
```

The task is **not** complete if it rewrites the files wholesale or deletes historical material.
