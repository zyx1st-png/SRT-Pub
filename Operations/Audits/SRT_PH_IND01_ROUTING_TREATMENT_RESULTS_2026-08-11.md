---
id: SRT-PH-IND01-ROUTING-TREATMENT-RESULTS-20260811
type: audit
status: active
record_stage: audit_v1
layer: operations
epistemic_layer: os
claim_mode: evidence
claim_level: audit_only
canonical: false
date: 2026-08-11
source_of_truth: "treatment ref @ 5c1cbc8d66c1f193b2fa1222719969c9dca6f23a"
baseline_ref: 122e47b0bbe3835318cd9d729b77f7a437fbc8c8
treatment_ref: 5c1cbc8d66c1f193b2fa1222719969c9dca6f23a
result_base_ref: be9e8caf73a4cb6635a9ba0ebbdcc08b018eaceb
specification: Operations/Audits/SRT_PH_IND01_ROUTING_TREATMENT_PROBE_SPEC_2026-08-11.md
formal_attempts: 4
valid_runs: 3
invalid_runs: 1
reserve_used: 1
valid_observations: 18
verdict: treatment_pass_attributed
dependency:
  - SRT-PH-IND01-ROUTING-TREATMENT-PROBE-SPEC-20260811
  - SRT-MATERIAL-CLUSTER-BASELINE-PROBE-RESULTS-20260811
  - SRT-BOUNDED-RETRIEVAL-PROTOCOL-20260808
tags: [Governance, Audit, BoundedProbe, Treatment, Philosophy, PH-IND01, InterventionEffect]
---

# PH-IND01 routing treatment results（2026-08-11）

> 本文件只记录固定 treatment ref 上的检索干预证据，不定义理论，不更新 active-theory node，不修改材料裁决或 claim level。

## 0. Outcome

~~~text
baseline Philosophy suite   = 17/18
baseline target             = P-A / P-Q5 fail
treatment valid runs        = P-A-T, P-C-T, P-D-T reserve
treatment invalid runs      = P-B-T (startup-stage self-invalidation)
treatment valid score       = 18/18
positive failures           = 0
P-A / P-Q5                  = pass
Route 8a used for P-A/Q5    = yes
intervention attribution    = established
disposition                 = STOP
~~~

The minimal Route 8a treatment closed the observed PH-IND01 retrieval gap. It does not authorize a Philosophy synthesis or theory-content writeback.

---

## 1. Frozen comparison

| Condition | Ref | Theory/content delta |
|---|---|---|
| Baseline | `122e47b0bbe3835318cd9d729b77f7a437fbc8c8` | none |
| Treatment | `5c1cbc8d66c1f193b2fa1222719969c9dca6f23a` | `_SRT_CONTEXT_ROUTER.md` Route 8a only |

The treatment ref forked directly from the baseline ref. It contained none of the baseline specification, baseline results, treatment specification, rubrics, or other run reports.

Route 8a added a declarative route for object individuation / identification / tracking / minimal-subject questions:

- Primary: `Philosophy/_SRT_Philosophy_Hardening_Index.md § PH-IND01`;
- Secondary: PH-IND01 patch, Subjecthood Threshold Interface, Core_Law Individuation;
- Boundary: tracking continuity is not consequence-bearing continuity; object index is not minimal subject or consciousness.

No owner, patch, canonical file, CompactCore, deep map, bundle, hook, or registry was changed in the probed treatment ref.

---

## 2. Run validity

| Attempt | Form | Body | Nav | Result | Disposition |
|---|---|---:|---:|---|---|
| P-A-T | A | 6 | 2 | valid, 6/6 | counted |
| P-B-T | B | 0 | 1 | invalid before body retrieval | excluded; no favorable waiver |
| P-C-T | C | 6 | 2 | valid, 6/6 | counted |
| P-D-T | D reserve | 6 | 2 | valid, 6/6 | preregistered replacement for P-B-T |

P-B-T treated pre-existing, unrelated bounded-probe language in the fixed ref's mandatory `STATUS.md §Fast Status` as a leak and stopped immediately. The operator did not override that self-invalidation. Because it was the first and only invalid run, the preregistered Form D reserve was allowed. No valid-but-wrong run was replaced.

The three counted runs were on the fixed ref, clean, within 6 body files and 2 navigation actions, with no reported leak or other invalidating event.

---

## 3. Score

The observation-level record, including all six invalid P-B-T rows, is:

[`data/srt_ph_ind01_routing_treatment_results_2026-08-11.csv`](data/srt_ph_ind01_routing_treatment_results_2026-08-11.csv)

| Valid run | Questions | Pass | Fail | Positive failures |
|---|---|---:|---:|---:|
| P-A-T | Q1, Q2, Q4, Q5, Q8, Q10 | 6 | 0 | 0 |
| P-C-T | Q1, Q5, Q6, Q9, Q10, Q12 | 6 | 0 | 0 |
| P-D-T | Q2, Q3, Q7, Q8, Q11, Q12 | 6 | 0 | 0 |
| **Total** | 18 valid observations | **18** | **0** | **0** |

All twelve unique Philosophy questions were answered correctly across the counted forms. Every question from the invalid P-B form was independently present and passed in P-A, P-C, or reserve P-D:

| Invalid P-B question | Counted replacement observation |
|---|---|
| Q3 | P-D-T / Q3 pass |
| Q4 | P-A-T / Q4 pass |
| Q6 | P-C-T / Q6 pass |
| Q7 | P-D-T / Q7 pass |
| Q9 | P-C-T / Q9 pass |
| Q11 | P-D-T / Q11 pass |

This establishes question-level no-regression despite the form-level invalidation.

---

## 4. Targeted intervention attribution

The preregistered attribution gate required the exact baseline-failing analogue `P-A / P-Q5` to pass and to reach PH-IND01 through Route 8a.

P-A-T recorded this path:

~~~text
_SRT_CONTEXT_ROUTER.md §8a
-> Philosophy/patches/SRT_Philosophy_PH_IND01_Object_Subject_Individuation_Before_Identification_v0_1.md
-> tracking continuity != consequence-return continuity
-> object index != minimal subject / consciousness
~~~

Its answer was:

> 婴儿对象追踪可以作为“对象个体化先于丰富识别”的负控，同时必须拒绝由此推出 minimal subject、bearer continuity 或 consciousness。

P-C-T independently used Route 8a plus the Philosophy hardening index and reached the same distinction.

Therefore:

~~~text
P-A/Q5 behavioral delta      = fail -> pass
declared route actually used = yes
other treatment delta        = none
question-level regressions   = none
intervention effect          = observed and attributable
~~~

This is a cluster-local Axis C-style result. No active-theory node currently owns this bounded Philosophy cluster, so the active-theory registry is not changed and no new node is created.

---

## 5. Theoretical boundary

The treatment improved retrieval, not theory content. The runs continued to preserve:

- object individuation vs rich identification;
- object-tracking continuity vs consequence-bearing continuity;
- object index vs minimal subject;
- Selector vs Bearer vs Concern Domain vs Experiencer;
- HP-A structural/perspectival individuation vs HP-B phenomenal necessity;
- recurrent historical reconstitution vs literal microstate identity;
- external philosophical convergence vs SRT-native proposition;
- problem-space restructuring vs `virtual = L0` or transduction = Real Choice Moment;
- cognitive generativity vs canonical `d`/`Psi_f`;
- implicit historical constraint vs `memory = L2`;
- operational threshold vs ontological boundary;
- broad meta-selectability vs J5 R3/I5 qualification.

Nothing here promotes PH-IND01 above its existing non-canonical P3 status or transfers infant-cognition evidence into subjecthood evidence.

---

## 6. Stop decision

The Case B gap is closed by the smallest tested intervention. Accordingly:

- keep Route 8a;
- do not add another index, CompactCore, owner paragraph, deep-map node, or context-bundle theory entry for this cluster;
- do not create an Individuation / Representation / Bearer Formation synthesis;
- do not modify subjecthood, phenomenality, `d`, `Psi_f`, `L0/L1/L2`, or Real Choice Moment owners;
- do not update Axis B or create an active-theory node from this result;
- do not run further Philosophy treatment probes unless a later regression or new proposition supplies a fresh trigger.

~~~text
retrieval/compression gap = closed
content gap               = not established
synthesis need            = not established
intervention effect       = observed (cluster-local)
next action               = STOP
~~~
