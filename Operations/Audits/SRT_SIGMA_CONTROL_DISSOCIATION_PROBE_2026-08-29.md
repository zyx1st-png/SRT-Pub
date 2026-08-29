---
id: SRT-OPS-AUDIT-SIGMA-CONTROL-DISSOCIATION-PROBE-20260829
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
  - Operations/Audits/SRT_SIGMA_REPARAMETERIZATION_FEASIBILITY_PROBE_2026-08-29.md
  - Operations/Audits/SRT_SIGMA_TRACE_ATTRIBUTION_UNIQUENESS_PROBE_2026-08-29.md
  - Core_Law/SRT_Individuation.md
  - Core_Law/SRT_L1_Formalism.md
tags: [SigmaSR, Control, Sensitivity, Ablation, Fisher, DefectC, Split]
---

# σ_sr Magnitude-vs-Control Dissociation Probe — DEFECT C (2026-08-29)

> **Scope:** executed minimal mathematical probe. Read-only. This probe stipulates trace/ext membership in advance so that DEFECT A cannot be used to rescue or explain the result.
>
> **Question:** even when `theta^trace` and `theta^ext` membership is unambiguous in a fixed coordinate model, does their bare norm ratio track their causal/sensitivity control over the current operator output?

---

## 0. Verdict

```text
TRACE/EXT MEMBERSHIP: STIPULATED / FIXED
BARE-NORM SIGMA: HIGH SELF-HISTORY SHARE
OUTPUT SENSITIVITY: EXTERNAL COMPONENT DOMINATES
INTERVENTIONAL ABLATION: EXTERNAL COMPONENT DOMINATES
SIMPLE GAUSSIAN FISHER SENSITIVITY: EXTERNAL COMPONENT DOMINATES
```

Therefore:

\[
\boxed{
\text{bare parameter-magnitude share}
\neq
\text{current output-control share}
}
\]

in a minimal frozen model.

This directly blocks an unqualified interpretation of `sigma_sr` as a **self-history control ratio**.

It does **not** invalidate a narrower provenance/writeback-magnitude interpretation.

---

## 1. Freeze the model and membership

Take a two-parameter operator with fixed trace/ext channels:

\[
\theta^{trace}
=
\begin{bmatrix}10\\0\end{bmatrix},
\qquad
\theta^{ext}
=
\begin{bmatrix}0\\1\end{bmatrix}.
\]

Membership is stipulated structurally:

```text
parameter 1 = self-history channel
parameter 2 = external-input channel
```

No attribution ambiguity is allowed in this probe.

The current bare-norm ratio is:

\[
\sigma_{bare}
=
\frac{10}{10+1}
=
\frac{10}{11}
\approx0.9091.
\]

So the current scalar says the operator is overwhelmingly trace/self-history weighted.

---

## 2. Define a fixed operator whose two parameter directions have different sensitivities

Let the operator score be:

\[
z(\theta)
=\varepsilon\theta_1+\theta_2,
\qquad
\varepsilon=10^{-3}.
\]

Any monotone readout may be applied, for example:

\[
y=\operatorname{sigmoid}(z).
\]

At the frozen parameter state:

\[
z
=10^{-3}\cdot10+1
=1.01.
\]

The trace direction has large parameter magnitude but sits in a low-sensitivity channel.

The external direction has small parameter magnitude but sits in the high-sensitivity channel.

---

## 3. Local Jacobian sensitivity

For the score:

\[
\nabla_\theta z
=
\begin{bmatrix}
\varepsilon\\1
\end{bmatrix}
=
\begin{bmatrix}
0.001\\1
\end{bmatrix}.
\]

A simple magnitude-times-sensitivity contribution is:

\[
C_{trace}^{Jac}
=|10|\cdot0.001
=0.01,
\]

\[
C_{ext}^{Jac}
=|1|\cdot1
=1.
\]

Normalized control-like share:

\[
\sigma_{Jac}
=
\frac{0.01}{0.01+1}
\approx0.00990.
\]

Compare:

\[
\boxed{
\sigma_{bare}\approx0.9091
\qquad
\sigma_{Jac}\approx0.00990
}
\]

The ranking reverses by almost two orders of magnitude.

---

## 4. Interventional / ablation comparison

Hold the same model and current state fixed.

### Ablate trace channel

Set `theta_1 -> 0` while leaving `theta_2=1`:

\[
z_{-trace}=1.
\]

Score change:

\[
|\Delta z_{trace}|=|1.01-1|=0.01.
\]

### Ablate external channel

Set `theta_2 -> 0` while leaving `theta_1=10`:

\[
z_{-ext}=0.01.
\]

Score change:

\[
|\Delta z_{ext}|=|1.01-0.01|=1.
\]

Thus:

\[
\boxed{
|\Delta z_{ext}|
=100\,|\Delta z_{trace}|
}
\]

while the bare norm ratio assigns roughly 91% of the mass to trace.

So the dissociation is not an artifact of a derivative-only readout; it appears under direct intervention in the same frozen model.

---

## 5. Simple Fisher sensitivity comparison

To test the named information-geometric candidate without overclaiming it, embed the score in a regular Gaussian observation model:

\[
Y\mid\theta
\sim
\mathcal N(z(\theta),1).
\]

Then the Fisher information matrix is:

\[
g_F(\theta)
=
\nabla z\,\nabla z^T
=
\begin{bmatrix}
\varepsilon^2 & \varepsilon\\
\varepsilon & 1
\end{bmatrix}.
\]

For the pure trace and ext component directions, Fisher local lengths are proportional to:

\[
\|\theta^{trace}\|_F
=|10\varepsilon|
=0.01,
\]

\[
\|\theta^{ext}\|_F
=|1|
=1.
\]

Therefore the Fisher-weighted share in this simple admitted statistical model is again:

\[
\sigma_F
\approx0.00990.
\]

This agrees with the Jacobian and ablation ranking **in this toy model**.

### Guard

This does not prove:

```text
Fisher = causal control in general
```

It only shows that once the output/statistical model is specified, a sensitivity-aware metric can produce a radically different ordering from the bare parameter norm.

---

## 6. Why this matters for the current wording

Current symbol-table language calls `sigma_sr` a scalar projection onto the operator's “own history-derived component vs external-driven component.”

`SRT_Individuation` further motivates the ratio as a one-dimensional tracker of how strongly the next selection is constrained by its own history relative to external conditions.

The probe distinguishes two readings:

### Reading P — provenance / stored-history magnitude

```text
How much parameter magnitude is assigned to self-history vs external source?
```

The bare ratio may still serve as a model-local proxy under a declared coordinate/attribution convention.

### Reading C — current control / influence

```text
How much does self-history actually control the current/future operator output?
```

The bare ratio fails this reading in the frozen counterexample.

Therefore:

\[
\boxed{
\text{provenance magnitude}
\neq
\text{control influence}
}
\]

must be retained unless a stronger theorem connects them inside a restricted model class.

---

## 7. This strengthens SPLIT but does not yet define two canonical sigmas

The three executed probes now jointly support:

```text
DEFECT B:
bare ratio is coordinate-dependent under equivalent parameterizations

DEFECT A:
trace/ext attribution is not uniquely closed by current owners

DEFECT C:
even fixed membership + fixed coordinates do not make bare magnitude equal control
```

This makes a **SPLIT** outcome structurally plausible:

```text
historical attribution / provenance readout
!=
current control / influence readout
```

But this audit does not create or name canonical replacements.

No inference is licensed of the form:

```text
bearer = provenance scalar
selector = control scalar
```

Bearer and selector admission remain independently owned.

---

## 8. What would be required to save a single-scalar control interpretation

A single scalar could still survive in a restricted family if SRT can establish, for all admitted models in that family, a monotone relation such as:

\[
\|\theta^{trace}\|_M
>
\|\theta^{ext}\|_M
\quad\Longleftrightarrow\quad
I_{trace}(\hat G)
>
I_{ext}(\hat G),
\]

where:

```text
M = declared invariant metric
I = declared influence/control functional.
```

That is a strong theorem burden.

The current owner set does not supply it.

---

## 9. Implication for the phase-boundary claim

If `sigma_sr^sub` is meant to track a transition in **control authority**, then a threshold on bare provenance magnitude is not sufficient.

The toy model can have:

```text
sigma_bare > any moderate subject-entry threshold
while
self-history output influence is arbitrarily small.
```

By taking `epsilon -> 0`, one can hold bare sigma fixed while driving trace control toward zero.

Therefore the natural-boundary question must first state which semantics the threshold belongs to:

```text
historical provenance?
internal endogeneity?
ongoing dependence?
current control?
```

Without that typing, `sigma_sr^sub` cannot be interpreted as a natural boundary of all four at once.

---

## 10. Updated outcome assessment

After DEFECT A/B/C execution:

### SURVIVES — broad current interpretation

`WEAKENED STRONGLY`.

Would require an existing or new restricted model class in which attribution, invariant metric, and control ranking coincide.

### SURVIVES-WITH-REPAIR

`LIVE`, but repair burden is now at least two-part:

```text
attribution well-formedness
+
invariant/control-sensitive measurement
```

### SPLIT

`STRONGLY SUPPORTED AS THE LEADING STRUCTURAL HYPOTHESIS`.

This is still a hypothesis about repair architecture, not a landed theory result.

### RETYPE

`LIVE` if current sigma is retained only as a chosen-model historical/writeback-magnitude proxy.

### NO-GO

`NOT ESTABLISHED FOR ALL SIGMA-LIKE ORDER PARAMETERS`.

No-go is established only for the unqualified claim that the current bare-norm scalar is simultaneously representation-independent and a general current-control ratio.

---

## 11. Next action

Internal defect discovery is now sufficient to justify **formal Gate-2 subtraction** before proposing an owner repair.

Priority external roles:

```text
1. information geometry / Fisher-Rao / Cencov-style invariance
2. axiomatic causal/contribution attribution
3. intervention causal strength / information flow
4. information-theoretic autonomy and system/environment decomposition
```

The question is not whether these literatures use `sigma_sr`.

It is:

> Do they already provide a role-matched solution for a coordinate-invariant decomposition of historical/internal vs external influence, and if so, what residual work is actually SRT-specific?

Only after this subtraction should the programme choose between repair, split, retype, or bounded no-go.

---

## 12. Terminal status

```text
DEFECT C EXECUTED: YES
FIXED MEMBERSHIP: YES
FIXED COORDINATE MODEL: YES
BARE-NORM TRACE SHARE: 0.9091
JACOBIAN-WEIGHTED TRACE SHARE: ~0.00990
ABLATION: EXTERNAL EFFECT = 100x TRACE EFFECT
SIMPLE GAUSSIAN FISHER RANKING: AGREES WITH SENSITIVITY IN THIS TOY MODEL
BARE MAGNITUDE = CURRENT CONTROL: FAIL
SPLIT PRESSURE: STRONG
OWNER EDIT AUTHORIZED: NO
B1 CONSUMED: 0
NEXT: FORMAL GATE-2 SUBTRACTION
```
