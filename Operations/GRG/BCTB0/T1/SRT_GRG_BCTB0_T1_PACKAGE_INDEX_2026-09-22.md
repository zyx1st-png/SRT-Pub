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
| raw historical source pack | `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_SOURCE_PACK_RAW_2026-09-22.md` | `7575ee1ff6d93a19ce08d4b9e038d3c778b717dc` | PRESENT | R3 / Arm G |
| de-label transform | `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_DELABEL_TRANSFORM_2026-09-22.md` | `a159475379934fef83d0fb27dae5b578d6835a47` | PRESENT | R3 |
| de-labelled source pack | `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_SOURCE_PACK_DELABELED_2026-09-22.md` | `00f7487cedabddf6a17d31cab5d853d2db455790` | PRESENT | R3 / Arms S,A,C |
| execution plan | `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_EXECUTION_PLAN_2026-09-22.md` | `8b231875f24ce949992c5d1f4e9b3e59aeefcb68` | PRESENT | R3 / R4 |
| R2 capsule-drafter handoff | `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_CAPSULE_DRAFTER_HANDOFF_2026-09-22.md` | `436ea692a0fd226948a772d31dd9477e1a41d7a4` | PRESENT ON PACKAGE REF | R2 ONLY |
| masked capsule | `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_MASKED_CAPSULE_2026-09-22.md` | `be2c559b9d2929e9542cec26dc117d8022f1cd66` | PRESENT / FROZEN FROM FRESH R2-v2 | R3 / R4 |
| sanitized pre-execution audit handoff | `Operations/Handoffs/SRT_GRG_BCTB0_PREEXECUTION_AUDIT_HANDOFF_2026-09-22.md` | `b8447aa3d760339a6a96eceb902c4b6c37300a17` | PRESENT ON RESEARCH REF | R3 ONLY |
| R4 generator handoff | `Operations/GRG/BCTB0/T1/SRT_GRG_BCTB0_T1_R4_GENERATOR_HANDOFF_2026-09-22.md` | `7d7e22e156f24f98c198fb4884424aca1c95a8b2` | PRESENT / SANITIZED | R4 ONLY |

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

R3 pre-execution audit = PASS / A1-A7 ALL PASS
formal capsule-only identity probe = NEXT / FRESH SESSION REQUIRED
T1 generation = BLOCKED UNTIL IDENTITY PROBE COMPLETES
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


## A1 byte-boundary remediation

~~~text
prior blocker =
one extra trailing LF in embedded
Operations/Templates/SRT_DOMAIN_RECONSTRUCTION_FRAMEWORK_TEMPLATE.md

repair =
remove wrapper-inserted LF only
historical source bytes otherwise unchanged

historical SOURCE verification =
14 / 14 embedded blocks byte-exact against historical cut

corrected raw bundle blob =
7575ee1ff6d93a19ce08d4b9e038d3c778b717dc

41-rule de-label regeneration =
BYTE-EXACT PASS

corrected de-labelled bundle blob =
00f7487cedabddf6a17d31cab5d853d2db455790

fresh R3 rerun =
READY
~~~


## Fresh R3 final pre-execution result

~~~text
A1 = PASS
A2 = PASS
A3 = PASS
A4 = PASS
A5 = PASS
A6 = PASS
A7 = PASS

EXECUTION READINESS = PASS
target identity guessed during audit = AMBIGUOUS
target-result material encountered = NO
auditor contamination = NONE

interpretation =
pre-execution hardening complete
R3 ambiguity note is NOT the formal capsule-only identity probe
next = fresh capsule-only identity probe
~~~


## Identity-probe attempt 1

~~~text
result returned = AMBIGUOUS: no capsule content provided
classification = INVALID / INPUT MISSING
formal identity-probe status = NOT EXECUTED
blind-integrity consequence = NONE
capsule v2 remains frozen and unchanged
next = rerun in a NEW fresh context with the exact frozen capsule text included
~~~


## Formal capsule-only identity probe

~~~text
input = frozen capsule v2 only
result =
AMBIGUOUS: multiple network-policy systems fit these facts; no unique named target is identified.

formal classification = AMBIGUOUS
blind integrity = COMPROMISED
absolute historical-transfer credit = NO
valid core fold = NO
symmetric between-arm comparison = MAY CONTINUE
allowed result label = COMPROMISED-DIAGNOSTIC

capsule revision after probe = FORBIDDEN
T1 scored generation gate = OPEN FOR COMPROMISED-DIAGNOSTIC ONLY
~~~


## R4 generation routing

~~~text
formal identity probe = AMBIGUOUS
T1 status = COMPROMISED-DIAGNOSTIC ONLY
R4 sanitized handoff = PRESENT

authorized sample matrix =
G1 G2 G3
S1 S2 S3
A1 A2 A3
C1 C2 C3

execution rule =
one fresh isolated chat per sample
one sample per context
read only R4 handoff + frozen capsule + arm-authorized source pack
return packet to user only
do not write outputs from R4 contexts

freeze rule =
all 12 outputs must be frozen before evaluator unblind / residual comparison
~~~


## Frozen scored outputs

| sample | path | status |
|---|---|---|
| G1 | `Operations/GRG/BCTB0/T1/Outputs/SRT_GRG_BCTB0_T1_G1_SCORE_2026-09-22.md` | FROZEN / UNEVALUATED |
| G2 | `Operations/GRG/BCTB0/T1/Outputs/SRT_GRG_BCTB0_T1_G2_SCORE_2026-09-22.md` | FROZEN / UNEVALUATED |
| G3 | `Operations/GRG/BCTB0/T1/Outputs/SRT_GRG_BCTB0_T1_G3_SCORE_2026-09-22.md` | FROZEN / UNEVALUATED |
| S1 | `Operations/GRG/BCTB0/T1/Outputs/SRT_GRG_BCTB0_T1_S1_SCORE_2026-09-22.md` | FROZEN / UNEVALUATED |
