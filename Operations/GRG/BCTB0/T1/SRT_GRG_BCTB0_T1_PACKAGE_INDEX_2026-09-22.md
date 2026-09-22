---
id: SRT-GRG-BCTB0-T1-PACKAGE-INDEX-20260922
type: calibration_input_index
status: candidate
date: 2026-09-22
canonical: false
ai_do_not_use_for_definition: true
---

# BCTB-0 T1 pre-execution package index

Historical cut:

```text
9900f425369b8840eac9220e567a60b811c52b27
```

## Current package state

| artifact | path | current blob SHA | status | intended reader |
|---|---|---|---|---|
| source manifest | `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_SOURCE_MANIFEST_2026-09-22.md` | `28ee2945619fc5196010c482428c1c131d4c5670` | PRESENT | R3 / R4 |
| raw historical source pack | `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_SOURCE_PACK_RAW_2026-09-22.md` | `f9478cc4791232a47e6d1db9e3132b5719e7f913` | PRESENT | R3 / Arm G |
| de-label transform | `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_DELABEL_TRANSFORM_2026-09-22.md` | `da66dc3f37f2615745e4b78d608f521ddcb7d747` | PRESENT | R3 |
| de-labelled source pack | `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_SOURCE_PACK_DELABELED_2026-09-22.md` | `78d4de3a58c401c471064c72fe596530ab56454c` | PRESENT | R3 / Arms S,A,C |
| execution plan | `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_EXECUTION_PLAN_2026-09-22.md` | `b59fd6e7ac78a39064e4a98048f5adb5f978db67` | PRESENT | R3 / R4 |
| R2 capsule-drafter handoff | `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_CAPSULE_DRAFTER_HANDOFF_2026-09-22.md` | `6a5ef4e4be3b22d5d5aa6075144e4398a168d922` | PRESENT | R2 ONLY |
| masked capsule | `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_MASKED_CAPSULE_2026-09-22.md` | `768a5de63e8477e1e5afd5ded0bb231aca0e5d6c` | PRESENT / FROZEN FROM R2 | R3 / R4 |
| sanitized pre-execution audit handoff | `Operations/Handoffs/SRT_GRG_BCTB0_PREEXECUTION_AUDIT_HANDOFF_2026-09-22.md` | `c463b8ff0222e09a591ac2be017b85db57b7163f` | PRESENT | R3 ONLY |

## Hard routing

R2 must not read R3-only or evaluator-only files.

R3 must not read the R2 capsule-drafter handoff.

R4 must not read:

- R2 handoff;
- R3 audit handoff;
- full BCTB-0 charter;
- PR discussion;
- target result/audit files.

## Readiness

~~~text
A1 package materials = PRESENT
A4 package materials = PRESENT
A5 package materials = PRESENT
A6 package materials = PRESENT
A7 plan = PRESENT

A2 masked capsule = PRESENT / FROZEN FROM R2
A3 identity-probe procedure = PRESENT IN EXECUTION PLAN

R3 rerun = READY IN A NEW FRESH SESSION
T1 generation = BLOCKED UNTIL R3 A1-A7 PASS
~~~
