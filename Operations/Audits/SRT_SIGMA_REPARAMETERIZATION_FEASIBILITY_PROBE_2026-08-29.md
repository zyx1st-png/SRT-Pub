---
id: SRT-OPS-AUDIT-SIGMA-REPARAMETERIZATION-FEASIBILITY-PROBE-20260829
type: audit_record
status: active
record_stage: executed_probe
date: 2026-08-29
layer: meta
epistemic_layer: os
claim_mode: evidence
claim_level: P3/P4_governance
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/Audits/SRT_SIGMA_ATTRIBUTION_CONTROL_INVARIANCE_AUDIT_2026-08-29.md
  - Core_Law/SRT_Individuation.md
  - Core_Law/SRT_L1_Formalism.md
  - Core/SRT_Core_22_Equations.md
  - _SRT_SYMBOL_TABLE.md
tags: [SigmaSR, Reparameterization, Invariance, Fisher, Feasibility, NoGoProbe]
---

# σ_sr Minimal Reparameterization Feasibility Probe (2026-08-29)

> **Scope:** executed mathematical feasibility probe, read-only. No canonical definition, equation, threshold, or claim level is changed.
>
> **Question:** can the current bare-norm ratio
>
> \[
> \sigma_{sr}=
> \frac{\|\theta^{trace}\|}
> {\|\theta^{trace}\|+\|\theta^{ext}\|}
> \]
>
> remain invariant under an admissible change of parameter coordinates that leaves the realized operator/model unchanged?

---

## 0. Result

```text
BARE EUCLIDEAN-NORM SIGMA:
NOT invariant under generic invertible linear reparameterization.

FISHER-Rao LOCAL TANGENT NORM:
can repair coordinate invariance inside a declared regular statistical model,
but does not by itself solve trace/ext attribution uniqueness
and does not automatically equal causal control.
```

This is evidence against treating the current bare norm ratio as representation-independent without additional assumptions.

It is **not** yet a verdict to demote `σ_sr`, because T-PROJ-1 may intend a narrower admissible representation class / projection family. The next owner-level question is whether C1-C4 already restrict that class strongly enough.

---

## 1. Minimal counterexample

Take a two-dimensional parameter decomposition:

\[
\theta^{trace}=
\begin{bmatrix}1\\0\end{bmatrix},
\qquad
\theta^{ext}=
\begin{bmatrix}0\\1\end{bmatrix}.
\]

Then under the ordinary Euclidean norm:

\[
\sigma_{sr}
=
\frac{1}{1+1}
=
\frac12.
\]

Now apply the invertible coordinate transformation

\[
A=
\begin{bmatrix}
10 & 0\\
0 & 1
\end{bmatrix},
\qquad
\theta'=A\theta.
\]

The two components transform as:

\[
\theta'^{trace}=
\begin{bmatrix}10\\0\end{bmatrix},
\qquad
\theta'^{ext}=
\begin{bmatrix}0\\1\end{bmatrix}.
\]

The same bare ratio becomes:

\[
\sigma'_{sr}
=
\frac{10}{10+1}
=
\frac{10}{11}
\approx 0.9091.
\]

So:

\[
\boxed{
\sigma_{sr}=0.5
\quad\not=\quad
\sigma'_{sr}\approx0.9091
}
\]

under a pure invertible coordinate scaling.

---

## 2. Why the realized operator can remain unchanged

The counterexample is not required to change physical/model behavior.

For a simple linear/logistic-style operator with score

\[
z=\theta^T x,
\]

use the reparameterized coordinates

\[
\theta'=A\theta,
\qquad
x'=A^{-T}x.
\]

Then:

\[
\theta'^T x'
=(A\theta)^T(A^{-T}x)
=\theta^T x.
\]

Hence every score, and any output depending only on that score, is unchanged.

Therefore:

```text
same realized input-output function
+ different parameter coordinates
-> different bare Euclidean sigma
```

This is the exact representation-dependence pressure the audit preregistered.

---

## 3. General form of the counterexample

The issue is not special to the numbers `10` and `1`.

For two linearly independent nonzero component vectors `t` and `e`, an invertible linear map can be chosen so that:

```text
A t = lambda * t_bar
A e = e_bar
```

for any positive scaling `lambda` in a suitable basis.

Then the bare ratio has the form:

\[
\sigma'(\lambda)
=
\frac{\lambda\|t\|}
{\lambda\|t\|+\|e\|}.
\]

As `lambda` varies:

\[
\sigma'(\lambda)\to0
\quad(\lambda\to0^+),
\]

and

\[
\sigma'(\lambda)\to1
\quad(\lambda\to\infty).
\]

Thus, absent a restricted coordinate class or invariant metric, the same functional model can in principle be assigned almost any self-reference ratio in `(0,1)` by coordinate rescaling.

### Edge case

If trace and ext components are forced into one shared one-dimensional direction and every admissible transformation scales them identically, the ratio can survive. But that is a special restriction, not generic invariance.

---

## 4. Immediate interpretation

The probe establishes only:

```text
bare coordinate norm
!= representation-invariant structural magnitude
```

It does **not** establish:

```text
sigma is useless
sigma cannot be repaired
no natural transition exists
Fisher is the required repair
```

The burden now moves to T-PROJ-1:

> Do C1-C4 imply a privileged coordinate/gauge, a restricted admissible transformation family, or an invariant projection metric sufficient to block the counterexample?

If YES, the current formula may survive inside that declared model class.

If NO, `SURVIVES` in the broad representation-independent sense is unavailable without repair/retyping.

---

## 5. Fisher-Rao candidate repair — what it actually repairs

Suppose `theta` parameterizes a regular statistical model `p(y|theta)` with Fisher information metric `g_F(theta)`.

Under a smooth reparameterization `phi=h(theta)`, the Fisher tensor transforms covariantly. A tangent displacement has invariant local squared length:

\[
d\ell^2
=d\theta^T g_F(\theta)d\theta
=d\phi^T g'_F(\phi)d\phi.
\]

For the simple linear map `phi=A theta`:

\[
g'_F
=A^{-T}g_F A^{-1},
\qquad
d\phi=A d\theta,
\]

so:

\[
d\phi^Tg'_F d\phi
=d\theta^Tg_Fd\theta.
\]

This directly addresses **DEFECT B** for local tangent/update magnitudes in a licensed statistical-model representation.

### But the current sigma components are not automatically tangent displacements

Current owner notation is an additive decomposition of the parameter state:

\[
\theta=\theta^{trace}+\theta^{ext}.
\]

Under a nonlinear reparameterization `phi=h(theta)`, generally:

\[
h(\theta^{trace}+\theta^{ext})
\ne
h(\theta^{trace})+h(\theta^{ext}).
\]

Therefore Fisher geometry does not tell us, by itself, what the transformed `trace` and `ext` components are.

Before a Fisher-norm sigma is well-defined, the theory still needs one of:

```text
a tangent-space decomposition rule
an update-path decomposition rule
a privileged affine parameterization
or another explicit attribution structure
```

That is **DEFECT A**, and Fisher does not solve it automatically.

---

## 6. Fisher does not automatically solve control semantics either

Fisher information measures sensitivity/distinguishability of a statistical distribution with respect to parameter changes.

That can be highly relevant to **DEFECT C**, but only if the distribution whose sensitivity is measured is the correct control/output object.

The stronger claim:

```text
Fisher magnitude of a trace component
=
causal control of the selector's next realized output/future candidate space
```

requires additional bridge assumptions.

Possible missing distinctions:

```text
statistical distinguishability
!= action-selection influence
!= intervention causal strength
!= future candidate-space control
```

Therefore the audit should compare Fisher sensitivity against intervention/ablation or causal-strength measures before calling any repaired scalar a `control ratio`.

---

## 7. Relation to existing repository Fisher language

`Core/SRT_Core_22_Equations.md` already contains conditional information-geometric bridge equations and explicitly says Fisher geometry does **not** redefine the canonical SRT objects by itself.

This probe therefore preserves:

```text
Fisher-Rao = candidate model-level invariant geometry
!= canonical theta-space metric by default
!= primitive ontology
```

A future Fisher repair must inherit the existing claim ceiling unless separately promoted through governance.

---

## 8. Relation to T-CHI-1 / family invariance

Existing L1 hardening asks a different invariance question:

```text
within an admissible chi / channel-function family,
which dynamical structures survive replacement of the function form?
```

The present probe asks:

```text
under equivalent parameter representations of the same operator/model,
does the scalar used as the independent variable itself remain invariant?
```

The first can remain mathematically valid conditional on a chosen `sigma` representation even if the second fails.

But interpretation of a `chi(sigma)` transition as a representation-independent natural phase boundary inherits the current sigma problem.

---

## 9. Updated outcome pressure after the first probe

The probe changes the prior over the preregistered outcomes:

### Broad SURVIVES

Requires evidence that T-PROJ-1 C1-C4 already restrict admissible representations enough to exclude the counterexample or supply an equivalent invariant structure.

### SURVIVES-WITH-REPAIR

Now a live and plausible branch if a legitimate invariant metric/projection exists.

### SPLIT

Still live. Invariance of historical provenance magnitude and invariance of causal-control magnitude may require different objects.

### RETYPE

Live if current bare ratio is best understood only inside a chosen parameterization as an operational/model-specific source-weight proxy.

### NO-GO

Not yet reached. The current result is a no-go only for **unqualified Euclidean representation invariance**.

---

## 10. Next bounded test

Do not move to external novelty claims yet.

Next internal test:

```text
T-PROJ-1 C1-C4
-> inspect whether any assumption fixes:
   (a) an admissible coordinate/gauge class,
   (b) a trace/ext decomposition under reparameterization,
   (c) an invariant norm/metric,
   (d) the intended semantic target of sigma.
```

Decision table:

| C1-C4 result | Consequence |
|---|---|
| explicitly fixes all four | counterexample out of admitted class; test the restricted class |
| fixes coordinate class but not attribution | DEFECT A remains |
| fixes attribution but not metric | DEFECT B remains |
| fixes metric but not control semantics | DEFECT C remains |
| fixes none | current broad order-parameter interpretation requires repair/retyping |

Only after this check should Gate 2 formal-literature subtraction begin.

---

## 11. Terminal probe status

```text
EXECUTED: yes
BARE EUCLIDEAN SIGMA UNDER GENERIC INVERTIBLE LINEAR REPARAMETERIZATION: FAIL
FUNCTIONAL OPERATOR EQUIVALENCE: PRESERVABLE
FISHER LOCAL TANGENT INVARIANCE: PLAUSIBLE / STANDARD INSIDE DECLARED STATISTICAL MODEL
FISHER SOLVES ATTRIBUTION UNIQUENESS: NO
FISHER SOLVES CAUSAL CONTROL SEMANTICS: NOT ESTABLISHED
CURRENT OWNER EDIT AUTHORIZED: NO
B1 CONSUMED: 0
NEXT: T-PROJ-1 C1-C4 SUFFICIENCY CHECK
```
