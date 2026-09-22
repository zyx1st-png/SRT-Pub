---
id: SRT-GRG-BCTB0-T1-PACKAGE-INDEX-20260922
type: calibration_input_index
status: candidate
date: 2026-09-22
canonical: false
ai_do_not_use_for_definition: true
---

# BCTB-0 T1 pre-execution package index

Package ref: `experiments/grg-bctb0-t1-preexec-package-20260922`

R3 handoff ref: `research/grg-bctb0-temporal-replay-20260922`

Historical cut:

```text
9900f425369b8840eac9220e567a60b811c52b27
```

## Current package state

| artifact | path | current blob SHA | status | intended reader |
|---|---|---|---|---|
| source manifest | `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_SOURCE_MANIFEST_2026-09-22.md` | `28ee2945619fc5196010c482428c1c131d4c5670` | PRESENT | R3 / R4 |
| raw historical source pack | `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_SOURCE_PACK_RAW_2026-09-22.md` | `f9478cc4791232a47e6d1db9e3132b5719e7f913` | PRESENT | R3 / Arm G |
| de-label transform | `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_DELABEL_TRANSFORM_2026-09-22.md` | `a159475379934fef83d0fb27dae5b578d6835a47` | PRESENT | R3 |
| de-labelled source pack | `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_SOURCE_PACK_DELABELED_2026-09-22.md` | `78d4de3a58c401c471064c72fe596530ab56454c` | PRESENT | R3 / Arms S,A,C |
| execution plan | `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_EXECUTION_PLAN_2026-09-22.md` | `8b231875f24ce949992c5d1f4e9b3e59aeefcb68` | PRESENT | R3 / R4 |
| R2 capsule-drafter handoff | `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_CAPSULE_DRAFTER_HANDOFF_2026-09-22.md` | `436ea692a0fd226948a772d31dd9477e1a41d7a4` | PRESENT ON PACKAGE REF | R2 ONLY |
| masked capsule | `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_MASKED_CAPSULE_2026-09-22.md` | `be2c559b9d2929e9542cec26dc117d8022f1cd66` | PRESENT / FROZEN FROM FRESH R2-v2 | R3 / R4 |
| sanitized pre-execution audit handoff | `Operations/Handoffs/SRT_GRG_BCTB0_PREEXECUTION_AUDIT_HANDOFF_2026-09-22.md` | `df06fb2a39bbeba9c7d4adee6cdb900bbd903a49` | PRESENT ON RESEARCH REF | R3 ONLY |

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

A2 masked capsule v1 = PRESENT / A2 LEAKAGE PASS / IDENTIFIABILITY WARNING
A2 masked capsule v2 = PRESENT / FROZEN FROM FRESH R2-v2
A3 identity-probe procedure = PRESENT IN EXECUTION PLAN

R3 rerun = READY IN A NEW FRESH SESSION
T1 generation = BLOCKED UNTIL R3 A1-A7 PASS
~~~


## Latest remediation after R3 BLOCKED

~~~text
A3 consequence freeze = PATCHED
A4 transform wrapper completeness = PATCHED
A4 deterministic reproduction = BYTE-EXACT PASS / 41 replacements
A5 common context-budget ceiling = PATCHED

prior R3 target identity guessed = YES
formal capsule-only identity probe = NOT YET RUN
interpretation = IDENTIFIABILITY WARNING, NOT FORMAL PROBE RESULT

next =
new fresh R3 A1-A7 audit
-> only if PASS, capsule-only identity probe
~~~
