---
id: SRT-SELECTION-TOTALITY-WAVE-D2-PATCH-SPEC-20260915
type: proposal
status: active
layer: operations
epistemic_layer: os
claim_mode: proposal
canonical: false
date: 2026-09-15
---

# Selection-totality Wave D2 exact patch specification

## 0. Execution contract

This is the single mechanical execution source for Wave D2 semantic landing.

Before editing, read:

1. `Operations/Audits/SRT_SELECTION_TOTALITY_WAVE_D2_PRELANDING_REVIEW_2026-09-15.md`
2. `Operations/Audits/SRT_SELECTION_TOTALITY_WAVE_D1_FINAL_INDEPENDENT_REVIEW_2026-09-15.md`
3. `_SRT_T_DIR_CANONICAL.md`
4. `_SRT_SYMBOL_TABLE.md`
5. `Governance/SRT_CLAIM_LADDER.md §0A`
6. `CANONICAL_REGISTRY.md`

Before semantic landing, recheck live main. If main has changed any D2 owner or its direct current authority dependencies since the verified material-only divergence, STOP and re-audit.

Authorized semantic files are exactly:

```text
_SRT_D_VALUE_CANONICAL.md
Core/SRT_Core_22_Equations.md
Core_Law/SRT_L1_Formalism.md
Core_Law/SRT_L1_Hardening_Notes.md
```

Do not edit D3 files in this pass.

## 1. Fixed upstream boundaries

```text
primitive Selection has no universal direction / goal / value / continuation preference;
L0 is not a completed possibility warehouse;
kappa_0 / epsilon_pg / B-count have no primitive authority by registration or inheritance;
T_dir requires an independently typed declared direction signal;
no declared direction -> T_dir undefined / not admitted;
declared but inaccessible direction -> T_dir may be 0;
T_dir > 0 does not validate the direction or establish good / legitimacy / health / O2-M;
universal d -> T_dir necessity is not established;
script / habit / L2 automation does not itself imply no Selection;
Selection occurrence does not itself imply durable history;
O2-M remains OPEN.
```

## 2. `_SRT_D_VALUE_CANONICAL.md`

### D2-D1 — add a current scope guard near the canonical-status note

Add a concise Selection-totality / Wave-C guard stating:

```text
This file owns d-value, not the source of direction.
A d relation may constrain stake, concern, execution or reorientation in a declared model,
but d does not create the independently typed direction required to admit T_dir.
No universal d -> T_dir necessary/sufficient relation is currently canonical.
L2 automation does not by itself cancel Selection occurrence.
```

Do not change `Def-d-canonical` in this pass.

### D2-D2 — repair §8 `d 与 T_dir 的关系`

Replace the current universal implication block:

```text
d = 0 -> T_dir = 0
d > 0 -/-> T_dir > 0
d is necessary but not sufficient for T_dir
```

with the bounded rule:

```text
There is no universal d -> T_dir necessity theorem.

T_dir admission first requires an independently typed declared direction signal.
Within a declared model, d may constrain stake-coupled access, execution or reorientation capacity,
but the exact d/T_dir relation is model / bridge scoped unless independently proved by the owners.

No declared direction -> T_dir undefined / not admitted, regardless of d.
Declared direction + inaccessible signal -> T_dir may be 0 even when d > 0.
T_dir > 0 does not imply d has any particular universal value, nor does it validate the direction.
```

Update the comparison table wording from `系统对自身选择秩序方向的可读性` to the current declared-direction formulation.

### D2-D3 — repair `选择时刻与 d-value 的连接`

The current text must not say that a selection moment is direct contact with a possibility warehouse or that L2 automation replaces Selection occurrence.

Retain the intended downstream research distinction by retyping it:

```text
In bearer / agency / decision models, episodes that reopen stake-coupled revision or reselection may exercise / develop d-related capacities.
Automated / scaffolded L2 operation may reduce such revision opportunities in a given model,
but script / habit / L2 automation can still contain genuine Selection occurrence.
Therefore d maintenance / shrinkage must be tied to declared stake, consequence return, revision / reselection conditions,
not to a universal active-Selection vs no-Selection dichotomy.
```

Do not define Selection occurrence from d.

### D2-D4 — repair the later `与 T_dir 的关系`

Remove / supersede:

```text
proto-gradient is readable;
T_dir tells the system where the direction is;
d > 0 is necessary for T_dir > 0.
```

Target:

```text
After a direction has been independently admitted, d may be used in a declared model as one constraint on whether the system can act on / sustain reorientation relative to that direction.
T_dir tracks access / reorientation, not the existence or truth of the direction.
No universal d/T_dir necessity is established here.
```

Preserve the distinction `d != T_dir`.

## 3. `Core/SRT_Core_22_Equations.md`

### D2-E1 — add authority truth-up near Terminology Alignment

Add a bounded note:

```text
Current symbol/claim typing overrides historical equation prose.
kappa_0 in this file is not primitive by registration or inheritance;
when used inside an equation it must denote an independently declared curvature / anisotropy / per-direction-cost realization parameter.
No equation in this file may use kappa_0 to supply universal value / order direction.
```

### D2-E2 — keep `Eq-DValue-Max-1` ID and formula, conditionalize admission

Keep:

```text
d_max(theta) = min(rank_eff(I_F(theta)), Psi_f^budget / kappa_0)
```

but add an explicit status line:

```text
Status: conditional model / realization equation, not a universal d law.
The equation is admitted only when a model independently declares a kappa_0-like per-direction effective cost / curvature parameter with compatible units and scope.
If no such realization is admitted, this equation is not applicable.
```

### D2-E3 — retype all kappa_0 prose inside Eq-DValue-Max-1

Replace:

```text
primitive L0 curvature;
unit cost of aligning one L0 direction;
kappa_0 determines which directions are worth aligning to / direction field.
```

with:

```text
in the declared model, kappa_0 is the effective per-direction stability / curvature / maintenance-cost parameter used by this capacity bound;
it does not choose, rank, value or legitimate directions;
it does not cause first Selection;
it does not establish primitive non-flatness.
```

Replace `L0 curvature directions` with `declared model directions / distinguishable directions` where this equation uses the phrase.

### D2-E4 — retype the implication

Do not claim a universal consciousness-depth ceiling from this equation.

Target:

```text
Within the declared model, the candidate d-capacity upper bound is limited by the smaller of the information-capacity proxy and the declared stability/payability budget.
This does not establish a universal consciousness threshold, subject threshold, value direction or primitive ontology law.
```

Keep equation ID stable for downstream references.

## 4. `Core_Law/SRT_L1_Formalism.md`

### D2-F1 — add direction-admission guard at top / §0

Add:

```text
The T_dir branch of this formalism is conditional on an independently typed declared direction signal as required by `_SRT_T_DIR_CANONICAL.md`.
Without such a direction, T_dir and T_dir^alg are undefined / not admitted for that model; they are not set to zero by default.
The remaining non-T_dir subsystem may still be analyzed.
```

The file does not become a direction owner.

### D2-F2 — update symbol table entry for T_dir / T_dir^alg

`T_dir(P,t)`:

```text
range [0,1] only after direction admission;
otherwise undefined / not admitted.
```

`T_dir^alg`:

```text
model-local accessibility/readability target relative to an already declared direction;
not a direction source.
```

### D2-F3 — retype §3.4

Retain the existing formula as a candidate model expression, but change its semantics:

```text
T_dir^alg is not generated from d/d_c/sigma in the ontological sense.
After direction admission, d/d_c/sigma may parameterize a model-local accessibility / reorientation target.
The formula does not create, rank, validate or discover the direction.
No declared direction -> the expression is not admitted as T_dir^alg for that claim.
```

Remove language that says the formula itself realizes a universal value-occlusion direction.

### D2-F4 — conditionalize §3.5 T_dir ODE

Keep the ODE structure as a candidate access/readability dynamics, with the explicit precondition:

```text
declared direction exists + T_dir admitted in model M.
```

Interpret all terms as modulation of access / reorientation relative to that direction.

Do not say structural suffering / healthy L2 reveals or hides a primitive direction. It may modulate access within the declared pathology model.

### D2-F5 — retype §3.5.3 lethal-L2 criterion

Keep as a **conditional pathology-model criterion** only.

Required guard:

```text
A high or apparently stable T_dir here means apparent access relative to the declared criterion.
It does not prove the declared direction is good, legitimate, healthy or morally authoritative.
The criterion is not universal outside the model assumptions and direction admission.
```

### D2-F6 — retype §5 four-variable closure

The four-variable system is conditional on T_dir admission.

State explicitly:

```text
no direction admitted -> do not insert T_dir=0 merely to close the equations;
omit / marginalize the T_dir branch and analyze the remaining declared subsystem.
```

Do not demote unrelated sigma / d_c / suffering equations merely because the T_dir branch is conditional.

### D2-F7 — truth-up `nu_block = eta * epsilon_pg * kappa_Psi_f`

Preserve the local model if useful, but add:

```text
epsilon_pg must itself be independently admitted as a declared realization/model parameter;
it is not available by primitive inheritance from O0 / Selection.
Algebraic positivity does not promote the relation to P1 by itself.
The relation's claim strength is capped by the weakest independently admitted premise / model status.
```

Remove any blanket statement that the positive-product relation is P1-candidate solely because three factors are positive.

## 5. `Core_Law/SRT_L1_Hardening_Notes.md`

### D2-H1 — add Wave-D2 scope guard to §2

State:

```text
The residual decomposition is a declared-model hardening candidate.
Its projection components do not define primitive ontology.
T_dir components require direction admission;
L0-labelled residual components require an explicit model representation and do not mean primitive L0 exerts latent pressure.
```

### D2-H2 — retype `||R||_{T_dir}`

Current T_dir projection is only defined when the model contains an independently typed declared direction and a corresponding access/readability projection.

No direction -> omit this component / use a reduced decomposition; do not substitute T_dir=0.

### D2-H3 — retype `||R||_{L0}`

Preserve notation where needed for lineage, but define it as:

```text
a model-declared residual over unrealized / still-accessible candidates in the chosen open-state representation;
not a pressure field emitted by primitive L0;
not evidence that L0 is a warehouse of pregiven states.
```

Replace phrases like `L0 candidate states not entering L1 produce pressure` with representation-scoped language.

### D2-H4 — retype A2 / projection orthogonality

The `T_dir / Psi_f / L0` projection decomposition and approximate orthogonality are explicit model assumptions only after all included projections are defined.

Do not call them universal structural subspaces of reality.

### D2-H5 — retype T-DELTA-1 claim status

Keep the formal result and ID, but the full three-component theorem may not stand as an unqualified repo-wide P1-candidate while direction and L0 projection structure are model-scoped.

Target status:

```text
conditional formal/model theorem / P2 formal candidate by default;
may carry stronger local status only inside a declared model whose direction, residual representation, projection geometry and stake weighting are independently established.
```

Do not treat algebraic derivability under A1-A3 as primitive/constitutive ontology proof.

### D2-H6 — repair sign / modeler-independence language

The direction of a projected residual may be objective relative to the declared model geometry and declared direction criterion, but it is not primitive because the modeler cannot arbitrarily change the sign.

State the distinction:

```text
non-arbitrary within declared model
!= primitive / universal direction.
```

## 6. Acceptance gate D2-01..D2-20

```text
D2-01  Def-d-canonical main definition is not reopened.
D2-02  no universal d -> T_dir necessity remains.
D2-03  d-value file no longer uses proto-gradient / intrinsic Selection direction as T_dir source.
D2-04  d-value file no longer says L2 automation itself removes Selection occurrence.
D2-05  Core22 Eq-DValue-Max-1 keeps stable ID but is explicitly conditional/model-scoped.
D2-06  Core22 kappa_0 does not choose / rank / value directions.
D2-07  Core22 kappa_0 does not regain primitive L0 authority or first-Selection causality.
D2-08  Eq-DValue-Max-1 no longer establishes a universal consciousness ceiling.
D2-09  L1 Formalism requires direction admission before T_dir / T_dir^alg.
D2-10  no declared direction -> T_dir undefined/not admitted, not automatically zero.
D2-11  d/d_c/sigma may modulate accessibility but do not supply direction.
D2-12  T_dir ODE is conditional access/readability dynamics, not direction ontology.
D2-13  lethal-L2 equation is model-conditional and non-legitimating.
D2-14  four-variable closure is conditional; non-T_dir subsystem remains analyzable.
D2-15  epsilon_pg use in nu_block requires independent model admission and cannot inherit P1 strength algebraically.
D2-16  Hardening T_dir residual component requires a declared direction.
D2-17  Hardening L0 residual is representation/model scoped, not primitive latent pressure.
D2-18  T-DELTA-1 full three-component claim is conditional/model scoped at appropriate claim level.
D2-19  no new primitive symbol / layer / O2-M closure is introduced.
D2-20  semantic diff touches exactly the four authorized D2 files; D3 remains untouched.
```

Any FAIL -> STOP before derivatives and before D3.

## 7. Targeted grep / review list

Review at minimum:

```text
d = 0
necessary condition
proto-gradient
选择时刻被 L₂ 替代
T_dir tells
T_dir 告诉
kappa_0
原初曲率
值得被对齐
L0 direction
L₀ 方向
consciousness depth
T_dir^alg
four-variable
四变量
lethal L2
致命 L₂
nu_block
epsilon_pg
L_0 residual pressure
L₀ residual pressure
候选状态中未进入 L_1
Pi_{T_dir}
Pi_{L_0}
P1-candidate
```

A hit may remain only if classified as one of:

```text
current bounded statement
explicit rejection / guard
OPEN
conditional model / realization / bridge
historical / superseded lineage
FAIL
```

## 8. Derivative obligations

`LONGFORM_SPLITS.md` currently registers:

```text
Core/Equations_Split/README.md
Core_Law/L1_Formalism_Split/README.md
```

Therefore, if their owners change, regenerate those split bodies with the official splitter. Do not perform metadata-only refresh.

No D-value or L1-Hardening split is currently registered in the longform split registry; do not invent one in D2 unless governance independently requires it.

After semantic PASS:

1. regenerate changed registered splits with `scripts/create_reading_split.py` using the existing README IDs/titles;
2. run split metadata check;
3. regenerate official context bundles;
4. run bundle `--check`;
5. `git diff --check`;
6. normal Governance Preflight;
7. inspect semantic vs generated diff separately.

## 9. Landing discipline

Recommended commits:

```text
Truth-up Wave D2 formal consumers
Regenerate Wave D2 derivatives
```

Do not enter D3 after a self-reported green D2. D2 requires an independent final semantic review.

```text
D2 LANDING AUTHORIZED BY THIS SPEC: YES, WITH GATES
D3: HOLD
MERGE #976: NO
```
