---
id: SRT-GRG-R1-O3-V0-1-PREEXECUTION-VALIDITY-AUDIT-20260921
type: audit
status: active
date: 2026-09-21
layer: operations
epistemic_layer: experimental
claim_mode: audit
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Experiments/grg_r1_o3_causal_mediation/O3_CAUSAL_MEDIATION_PROTOCOL_v0_1.md
  - Experiments/grg_r1_o3_causal_mediation/run_o3.py
  - Operations/Audits/SRT_GRG_R1_PRODUCTIVE_ADEQUACY_O_CRITERION_REVISION_PASS1_2026-09-20.md
tags: [GRG, GRGR1, O3, PreExecutionAudit, Superseded]
---

# GRG-R1 O3 v0.1 pre-execution validity audit

## Verdict

~~~text
v0.1 execution = DO NOT RUN
status = SUPERSEDED BEFORE OUTCOME GENERATION
target/result inspection = NONE
~~~

No O3 recipient outcome was generated before this audit.

## 1. Eigenvalue rank mismatch

v0.1 scaffold extraction does:

~~~text
vals = numpy.linalg.eigvals(W)
vals = numpy.sort(vals)[::-1]
take vals[:4]
~~~

but recipient transplantation does:

~~~text
e, V = numpy.linalg.eig(W)
e_new = e.copy()
e_new[:4] = scaffold
~~~

The recipient eigenvalues in e are not sorted by the scaffold rule.

Therefore scaffold rank 1..4 is not guaranteed to replace recipient rank 1..4.

This violates the intended intervention identity.

## 2. Real-matrix conjugacy problem

A real recurrent matrix can have complex-conjugate eigenvalue pairs.

Averaging ranked complex eigenvalues across donors and inserting them into arbitrary recipient eig slots does not guarantee conjugate symmetry.

v0.1 then reconstructs a complex matrix and applies:

~~~text
W_new = real(W_complex)
~~~

That silent projection can materially change the intended spectrum.

A post hoc imaginary-residual report does not repair intervention identity.

## 3. Missing matched generic-perturbation control

The post-v0.1 productive-adequacy revision required a control that distinguishes organization-specific intervention from generic operator damage.

O3 v0.1 compares:

~~~text
S scaffold
D scaffold
intact
~~~

but does not include a parameter-distance-matched structure-randomized control.

Therefore even a positive IS effect would remain vulnerable to generic intervention-magnitude explanation.

## 4. Disposition

Do not patch v0.1 in place after execution.

Because no O3 outcome exists yet, create a new visible v0.2 protocol before any run.

v0.2 should:

- use a real-valued, numerically stable operator spectrum;
- include an exact-feature donor admission for the actual intervention feature;
- include a parameter-distance-matched random spectral-direction control;
- remain source/base-domain only;
- preserve O4 / new transfer target HOLD.

v0.1 remains in the repository as a pre-execution design failure record.
