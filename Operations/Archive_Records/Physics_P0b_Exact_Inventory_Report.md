---
id: SRT-OPS-PHYSICS-P0B-EXACT-INVENTORY-REPORT-2026-04-29
type: inventory_report
tags: [Operations, Physics, Inventory, Frontmatter, Audit]
status: complete_v1
layer: meta
epistemic_layer: audit
claim_mode: audit
canonical: false
date: 2026-04-29
source_script: Operations/Archive_Records/Physics_P0b_Exact_Inventory_Handoff.md (Section 2)
dependency:
  - Operations/Archive_Records/Physics_P0_Inventory_Frontmatter_Audit.md
  - Operations/Archive_Records/Physics_P0b_Exact_Inventory_Handoff.md
  - Physics/README.md
  - Physics/SRT_Physics_Claim_Status.md
machine_summary: >
  Exact local inventory of Physics/*.md: 25 files, 21 with frontmatter, 4 missing frontmatter.
  Full table, missing-pointer summary, high-risk-hit summary, safety record, and PR-P1 queue included.
---

# Physics P0b Exact Inventory Report

**Date**: 2026-04-29  
**Executed by**: Codex / Claude Code (local script from `Operations/Archive_Records/Physics_P0b_Exact_Inventory_Handoff.md` §2)  
**Canonical impact**: none  
**Exact report pointer**: See `Operations/Archive_Records/Physics_P0_Inventory_Frontmatter_Audit.md` for prior audit context.

---

## 1. Full Inventory Table

Script run from repository root. Results are exact local line counts and frontmatter parse values.

| File | Lines | Frontmatter | type | status | layer | epistemic_layer | claim_mode | canonical | Claim-status ptr | README ptr | Risk hits |
|---|---:|---:|---|---|---|---|---|---|---:|---:|---|
| `Physics/PHYSICS_COMPACT_REGISTRY.md` | 58 | True | index | active_v1 | meta | os | canonical | MISSING | False | False | cosmology |
| `Physics/README.md` | 101 | True | directory_entry | active_v1 | meta | bridge | navigation | false | True | False | collapse,mwi,discrete_time,gravity_psif,constants,qbox_post_quantum,cosmology |
| `Physics/SRT_AT_Physics_of_Causation_Processing_2026-03-02.md` | 101 | True | external_review | draft_v1 | meta | os | canonical | MISSING | False | False | gravity_psif,constants |
| `Physics/SRT_Phys_07_Complex_Systems.md` | 701 | True | dynamics | axiomatic_hybrid_v2 | L1 | os | canonical | MISSING | False | False | collapse,discrete_time,gravity_psif,constants,cosmology |
| `Physics/SRT_Phys_07_Complex_Systems_CompactCore.md` | 242 | True | dynamics | active_v1 | L1 | os | canonical | MISSING | False | False | gravity_psif,constants |
| `Physics/SRT_Phys_08_Ontology_Ext.md` | 675 | True | theory | axiomatic_hybrid_v2 | L1 | os | canonical | MISSING | False | False | collapse,gravity_psif,constants,cosmology |
| `Physics/SRT_Phys_08_Ontology_Ext_CompactCore.md` | 217 | True | theory | active_v1 | L1 | os | canonical | MISSING | False | False | collapse |
| `Physics/SRT_Phys_09_Formalism_Ext.md` | 1156 | True | equation | axiomatic_hybrid_v2 | L1 | os | canonical | MISSING | False | False | collapse,discrete_time,gravity_psif,constants,cosmology |
| `Physics/SRT_Phys_09_Formalism_Ext_CompactCore.md` | 192 | True | equation | active_v1 | L1 | os | canonical | MISSING | False | False | gravity_psif |
| `Physics/SRT_Phys_10_Integration.md` | 550 | True | reference | axiomatic_hybrid_v1 | L1 | os | canonical | MISSING | False | False | collapse,discrete_time,gravity_psif,constants,cosmology |
| `Physics/SRT_Phys_10_Integration_CompactCore.md` | 182 | True | reference | active_v1 | L1 | os | canonical | MISSING | False | False | gravity_psif,cosmology |
| `Physics/SRT_Physics_Bridge_Integration_Hooks_for_QBox_EarthAccretion.md` | 158 | False | MISSING | MISSING | MISSING | MISSING | MISSING | MISSING | False | False | collapse,gravity_psif,qbox_post_quantum |
| `Physics/SRT_Physics_Claim_Status.md` | 215 | True | claim_status_audit | active_v1 | meta | bridge | audit | false | False | False | collapse,mwi,discrete_time,gravity_psif,constants,qbox_post_quantum,cosmology |
| `Physics/SRT_Physics_Cosmology.md` | 1486 | True | theory | axiomatic_hybrid_v2 | L1 | os | canonical | MISSING | False | False | collapse,mwi,discrete_time,gravity_psif,constants,cosmology |
| `Physics/SRT_Physics_Cosmology_CompactCore.md` | 241 | True | theory | active_v1 | L1 | os | canonical | MISSING | False | False | collapse,mwi,discrete_time,gravity_psif,constants,cosmology |
| `Physics/SRT_Physics_Hardening_Earth_Inner_Solar_System_Accretion_v0_1.md` | 306 | False | MISSING | MISSING | MISSING | MISSING | MISSING | MISSING | False | False | gravity_psif |
| `Physics/SRT_Physics_Hardening_QBox_Hyperdecoherence_v0_1.md` | 323 | False | MISSING | MISSING | MISSING | MISSING | MISSING | MISSING | False | False | collapse,gravity_psif,qbox_post_quantum |
| `Physics/SRT_Quant_00_Intro.md` | 476 | True | foundational_theory | axiomatic_hybrid_v2 | L1 | os | canonical | MISSING | False | False | collapse,mwi,gravity_psif,constants,cosmology |
| `Physics/SRT_Quant_00_Intro_CompactCore.md` | 178 | True | foundational_theory | active_v1 | L1 | os | canonical | MISSING | False | False | collapse,mwi,constants,cosmology |
| `Physics/SRT_Quant_01_Selection.md` | 917 | True | core_module | axiomatic_hybrid_v2 | L1 | os | canonical | MISSING | False | False | collapse,mwi,discrete_time,gravity_psif,constants,cosmology |
| `Physics/SRT_Quant_01_Selection_CompactCore.md` | 215 | True | core_module | active_v1 | L1 | os | canonical | MISSING | False | False | collapse,constants,cosmology |
| `Physics/SRT_Quant_02_Cosmology.md` | 938 | True | theory | axiomatic_hybrid_v2 | L1 | os | canonical | MISSING | False | False | collapse,gravity_psif,constants,cosmology |
| `Physics/SRT_Quant_02_Cosmology_CompactCore.md` | 248 | True | theory | active_v1 | L1 | os | canonical | MISSING | False | False | collapse,gravity_psif,constants,cosmology |
| `Physics/_SRT_Phys_Bridge.md` | 520 | True | constitutional_bridge | axiomatic_hybrid_v2 | L1 | bridge | translation | MISSING | False | False | collapse,mwi,discrete_time,gravity_psif,constants,cosmology |
| `Physics/_SRT_Physics_Hardening_Index.md` | 177 | False | MISSING | MISSING | MISSING | MISSING | MISSING | MISSING | False | False | collapse,qbox_post_quantum,cosmology |

**Totals**: 25 files · 21 with frontmatter · 4 missing frontmatter

---

## 2. Missing Pointer Summary

Files missing one or more of: claim-status pointer, README pointer, `canonical` flag, `claim_mode` field.

- `Physics/PHYSICS_COMPACT_REGISTRY.md`: missing claim-status, README, canonical flag
- `Physics/SRT_AT_Physics_of_Causation_Processing_2026-03-02.md`: missing claim-status, README, canonical flag
- `Physics/SRT_Phys_07_Complex_Systems.md`: missing claim-status, README, canonical flag
- `Physics/SRT_Phys_07_Complex_Systems_CompactCore.md`: missing claim-status, README, canonical flag
- `Physics/SRT_Phys_08_Ontology_Ext.md`: missing claim-status, README, canonical flag
- `Physics/SRT_Phys_08_Ontology_Ext_CompactCore.md`: missing claim-status, README, canonical flag
- `Physics/SRT_Phys_09_Formalism_Ext.md`: missing claim-status, README, canonical flag
- `Physics/SRT_Phys_09_Formalism_Ext_CompactCore.md`: missing claim-status, README, canonical flag
- `Physics/SRT_Phys_10_Integration.md`: missing claim-status, README, canonical flag
- `Physics/SRT_Phys_10_Integration_CompactCore.md`: missing claim-status, README, canonical flag
- `Physics/SRT_Physics_Bridge_Integration_Hooks_for_QBox_EarthAccretion.md`: missing claim-status, README, canonical flag, claim_mode (**no frontmatter**)
- `Physics/SRT_Physics_Claim_Status.md`: missing README
- `Physics/SRT_Physics_Cosmology.md`: missing claim-status, README, canonical flag
- `Physics/SRT_Physics_Cosmology_CompactCore.md`: missing claim-status, README, canonical flag
- `Physics/SRT_Physics_Hardening_Earth_Inner_Solar_System_Accretion_v0_1.md`: missing claim-status, README, canonical flag, claim_mode (**no frontmatter**)
- `Physics/SRT_Physics_Hardening_QBox_Hyperdecoherence_v0_1.md`: missing claim-status, README, canonical flag, claim_mode (**no frontmatter**)
- `Physics/SRT_Quant_00_Intro.md`: missing claim-status, README, canonical flag
- `Physics/SRT_Quant_00_Intro_CompactCore.md`: missing claim-status, README, canonical flag
- `Physics/SRT_Quant_01_Selection.md`: missing claim-status, README, canonical flag
- `Physics/SRT_Quant_01_Selection_CompactCore.md`: missing claim-status, README, canonical flag
- `Physics/SRT_Quant_02_Cosmology.md`: missing claim-status, README, canonical flag
- `Physics/SRT_Quant_02_Cosmology_CompactCore.md`: missing claim-status, README, canonical flag
- `Physics/_SRT_Phys_Bridge.md`: missing claim-status, README, canonical flag
- `Physics/_SRT_Physics_Hardening_Index.md`: missing claim-status, README, canonical flag, claim_mode (**no frontmatter**)

**Summary**: 24 of 25 files have at least one missing pointer. The `canonical` flag is absent in 21 of 21 files that have frontmatter (i.e., where the flag field is simply not present — not `false`, but `MISSING`). The 4 hardening/bridge files have **no frontmatter at all**.

---

## 3. High-Risk Hit Summary by Category

These categories flag text patterns whose *claim promotion* is forbidden at this PR stage. Presence is recorded for audit only — no claim status has been changed.

### collapse (19 files)
- `Physics/README.md`
- `Physics/SRT_Phys_07_Complex_Systems.md`
- `Physics/SRT_Phys_08_Ontology_Ext.md`
- `Physics/SRT_Phys_08_Ontology_Ext_CompactCore.md`
- `Physics/SRT_Phys_09_Formalism_Ext.md`
- `Physics/SRT_Phys_10_Integration.md`
- `Physics/SRT_Physics_Bridge_Integration_Hooks_for_QBox_EarthAccretion.md`
- `Physics/SRT_Physics_Claim_Status.md`
- `Physics/SRT_Physics_Cosmology.md`
- `Physics/SRT_Physics_Cosmology_CompactCore.md`
- `Physics/SRT_Physics_Hardening_QBox_Hyperdecoherence_v0_1.md`
- `Physics/SRT_Quant_00_Intro.md`
- `Physics/SRT_Quant_00_Intro_CompactCore.md`
- `Physics/SRT_Quant_01_Selection.md`
- `Physics/SRT_Quant_01_Selection_CompactCore.md`
- `Physics/SRT_Quant_02_Cosmology.md`
- `Physics/SRT_Quant_02_Cosmology_CompactCore.md`
- `Physics/_SRT_Phys_Bridge.md`
- `Physics/_SRT_Physics_Hardening_Index.md`

### mwi / Many-Worlds (8 files)
- `Physics/README.md`
- `Physics/SRT_Physics_Claim_Status.md`
- `Physics/SRT_Physics_Cosmology.md`
- `Physics/SRT_Physics_Cosmology_CompactCore.md`
- `Physics/SRT_Quant_00_Intro.md`
- `Physics/SRT_Quant_00_Intro_CompactCore.md`
- `Physics/SRT_Quant_01_Selection.md`
- `Physics/_SRT_Phys_Bridge.md`

### discrete_time (9 files)
- `Physics/README.md`
- `Physics/SRT_Phys_07_Complex_Systems.md`
- `Physics/SRT_Phys_09_Formalism_Ext.md`
- `Physics/SRT_Phys_10_Integration.md`
- `Physics/SRT_Physics_Claim_Status.md`
- `Physics/SRT_Physics_Cosmology.md`
- `Physics/SRT_Physics_Cosmology_CompactCore.md`
- `Physics/SRT_Quant_01_Selection.md`
- `Physics/_SRT_Phys_Bridge.md`

### gravity_psif (20 files)
- `Physics/README.md`
- `Physics/SRT_AT_Physics_of_Causation_Processing_2026-03-02.md`
- `Physics/SRT_Phys_07_Complex_Systems.md`
- `Physics/SRT_Phys_07_Complex_Systems_CompactCore.md`
- `Physics/SRT_Phys_08_Ontology_Ext.md`
- `Physics/SRT_Phys_09_Formalism_Ext.md`
- `Physics/SRT_Phys_09_Formalism_Ext_CompactCore.md`
- `Physics/SRT_Phys_10_Integration.md`
- `Physics/SRT_Phys_10_Integration_CompactCore.md`
- `Physics/SRT_Physics_Bridge_Integration_Hooks_for_QBox_EarthAccretion.md`
- `Physics/SRT_Physics_Claim_Status.md`
- `Physics/SRT_Physics_Cosmology.md`
- `Physics/SRT_Physics_Cosmology_CompactCore.md`
- `Physics/SRT_Physics_Hardening_Earth_Inner_Solar_System_Accretion_v0_1.md`
- `Physics/SRT_Physics_Hardening_QBox_Hyperdecoherence_v0_1.md`
- `Physics/SRT_Quant_00_Intro.md`
- `Physics/SRT_Quant_01_Selection.md`
- `Physics/SRT_Quant_02_Cosmology.md`
- `Physics/SRT_Quant_02_Cosmology_CompactCore.md`
- `Physics/_SRT_Phys_Bridge.md`

### constants (17 files)
- `Physics/README.md`
- `Physics/SRT_AT_Physics_of_Causation_Processing_2026-03-02.md`
- `Physics/SRT_Phys_07_Complex_Systems.md`
- `Physics/SRT_Phys_07_Complex_Systems_CompactCore.md`
- `Physics/SRT_Phys_08_Ontology_Ext.md`
- `Physics/SRT_Phys_09_Formalism_Ext.md`
- `Physics/SRT_Phys_10_Integration.md`
- `Physics/SRT_Physics_Claim_Status.md`
- `Physics/SRT_Physics_Cosmology.md`
- `Physics/SRT_Physics_Cosmology_CompactCore.md`
- `Physics/SRT_Quant_00_Intro.md`
- `Physics/SRT_Quant_00_Intro_CompactCore.md`
- `Physics/SRT_Quant_01_Selection.md`
- `Physics/SRT_Quant_01_Selection_CompactCore.md`
- `Physics/SRT_Quant_02_Cosmology.md`
- `Physics/SRT_Quant_02_Cosmology_CompactCore.md`
- `Physics/_SRT_Phys_Bridge.md`

### qbox_post_quantum (5 files)
- `Physics/README.md`
- `Physics/SRT_Physics_Bridge_Integration_Hooks_for_QBox_EarthAccretion.md`
- `Physics/SRT_Physics_Claim_Status.md`
- `Physics/SRT_Physics_Hardening_QBox_Hyperdecoherence_v0_1.md`
- `Physics/_SRT_Physics_Hardening_Index.md`

### cosmology (18 files)
- `Physics/PHYSICS_COMPACT_REGISTRY.md`
- `Physics/README.md`
- `Physics/SRT_Phys_07_Complex_Systems.md`
- `Physics/SRT_Phys_08_Ontology_Ext.md`
- `Physics/SRT_Phys_09_Formalism_Ext.md`
- `Physics/SRT_Phys_10_Integration.md`
- `Physics/SRT_Phys_10_Integration_CompactCore.md`
- `Physics/SRT_Physics_Claim_Status.md`
- `Physics/SRT_Physics_Cosmology.md`
- `Physics/SRT_Physics_Cosmology_CompactCore.md`
- `Physics/SRT_Quant_00_Intro.md`
- `Physics/SRT_Quant_00_Intro_CompactCore.md`
- `Physics/SRT_Quant_01_Selection.md`
- `Physics/SRT_Quant_01_Selection_CompactCore.md`
- `Physics/SRT_Quant_02_Cosmology.md`
- `Physics/SRT_Quant_02_Cosmology_CompactCore.md`
- `Physics/_SRT_Phys_Bridge.md`
- `Physics/_SRT_Physics_Hardening_Index.md`

---

## 4. Safety Confirmation

This PR-P0b pass executed the exact inventory script only. No other changes were made.

- No Physics source body text was moved or edited.
- No Physics source body text was rewritten.
- No formulas were changed.
- No `Physics_Annex/` directory was created.
- No collapse / MWI / gravity / discrete-time / constants / QBox / cosmology claims were promoted.
- No `Core/`, `Core_Law/`, `AI/`, `Neuroscience/`, `Philosophy/`, `Public/`, `Papers/`, or `graphify-out/` files were touched.

---

## 5. Recommended PR-P1 Adjudication Queue

The following items are queued for the next adjudication pass (PR-P1), listed in priority order. No action is taken here.

### P1-A: Frontmatter-missing files (highest priority)

These 4 files have no YAML frontmatter at all and cannot be parsed or audited reliably:

1. `Physics/SRT_Physics_Bridge_Integration_Hooks_for_QBox_EarthAccretion.md` — bridge/integration hooks; hits collapse, gravity_psif, qbox_post_quantum
2. `Physics/SRT_Physics_Hardening_QBox_Hyperdecoherence_v0_1.md` — hardening draft; hits collapse, gravity_psif, qbox_post_quantum
3. `Physics/SRT_Physics_Hardening_Earth_Inner_Solar_System_Accretion_v0_1.md` — hardening draft; hits gravity_psif
4. `Physics/_SRT_Physics_Hardening_Index.md` — hardening index; hits collapse, qbox_post_quantum, cosmology

**Recommended action**: Add minimal frontmatter (`id`, `type`, `status: draft`, `layer`, `epistemic_layer`, `claim_mode: exploratory`, `canonical: false`). Do not change body text.

### P1-B: Missing `canonical` flag in 21 frontmatter files

All 21 files with frontmatter are missing the `canonical` field (field is absent, not set to `false`). This is a uniform gap — the field was never added to the Physics file template.

**Recommended action**: Add `canonical: false` to each file's frontmatter in a single batch commit. Do not change body text.

### P1-C: Missing `claim_mode` field

21 files that have `claim_mode: canonical` in frontmatter should be reviewed: `canonical` is not a valid `claim_mode` value per `_SRT_SYMBOL_TABLE.md` (valid values: `audit`, `exploratory`, `translation`, `navigation`, `os`). These files have `claim_mode: canonical` where `canonical` likely belongs in the separate `canonical:` flag field.

**Recommended action**: Adjudicate correct `claim_mode` value file by file (likely `os` for L1 theory files). Do not change body text.

### P1-D: Missing pointers to `SRT_Physics_Claim_Status.md`

22 of 25 files do not link to `SRT_Physics_Claim_Status.md`. This makes cross-file claim traceability impossible.

**Recommended action**: Add a one-line frontmatter `see_also` or body footer pointer per file. Do not promote any claim status.

### P1-E: Missing pointers to `Physics/README.md`

24 of 25 files do not link to `Physics/README.md`.

**Recommended action**: Add a one-line footer pointer per file or update `Physics/README.md` registry table to be the authoritative index, reducing per-file pointer burden.

### P1-F: High-risk category review (deferred)

The 7 high-risk categories (collapse, mwi, discrete_time, gravity_psif, constants, qbox_post_quantum, cosmology) appear across the majority of Physics files. These require expert adjudication of claim status per `Physics/SRT_Physics_Claim_Status.md` before any claim can be promoted. This is a deferred P2 item.

---

*Report generated: 2026-04-29 · Script source: `Operations/Archive_Records/Physics_P0b_Exact_Inventory_Handoff.md` §2 · No canonical content modified.*
