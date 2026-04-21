---
id: SRT-CORE-21B-CONSTITUTIVE-THEOREMS
type: theorem_set
tags: [Formal logic, Constitutive Theorems, Claim Ladder]
status: active_v1
layer: L1
epistemic_layer: os
claim_mode: canonical
claim_level: P1
dependency: [SRT-CORE-21A-MINIMAL-AXIOMS, SRT-CLAIM-LADDER, SRT-CORE-12B, SRT-T-DIR-CANONICAL]
---

# SRT Core 21B: Constitutive Theorems

> **Role**: This file contains P1 claims: not primitive axioms, but constitutive consequences of the SRT core structure.
> P1 claims may be cited as canonical SRT theorems, but not as primitive axioms.

## Quick Reference

- Claim level: **P1 = Constitutive theorem**
- Source lineage: split from `Core/SRT_Core_21_Formal_Axioms.md`
- Primitive base: `Core/SRT_Core_21_Minimal_Axioms.md`
- Bridge / hypothesis layer: `Core/SRT_Core_21c_Bridge_Hypotheses.md`
- Governance: `Governance/SRT_CLAIM_LADDER.md`

---

## P1-T01: Horizontal Causality as `L_2` Projection

**Lineage**: former `Ax-F-03`.

**Formal Definition**: Causality is the `L_2` projection of selection dynamics.

$$
C_H(A \to B) \equiv P(B \,|\, A,\, L_2)
$$

**Implication**: Causality is a projected structure inside the convergence domain, not an ontological primitive prior to selection.

**Layer Note**: This theorem defines **horizontal causality** inside `L_2`. It does not replace vertical constitution across `L_0 -> L_1 -> L_2`.

**Cross-ref**: `Philosophy/SRT_Causality_Time.md §一`; `Core/SRT_Core_12a T-L0-Kappa0`.

---

## P1-T02: Ontological Time as Memory Horizon

**Lineage**: former `Ax-F-03b`.

**Formal Definition**: The flow of time is not background evolution but the historical record left by continuous anchoring in `L_2`.

$$
t_{\text{onto}} \equiv \int \|\hat{G}_\theta(s)\| ds
$$

**Implication**: If no selection leaves irreversible trace, time loses SRT's ontological direction and becomes only a parametric ordering tool.

**Time Layer Note**: This theorem concerns **ontological time**. Parametric time `t` in equations remains a mathematical ordering variable and does not by itself carry the ontological claim.

**Cross-ref**: `Philosophy/SRT_Causality_Time.md §二`; `Core/SRT_Core_12a Ax-L0-Bootstrap-C2`; `Core/SRT_Core_01_Axioms.md MA-1`.

---

## P1-T03: `L_2` Downward Constraint

**Lineage**: former `Ax-F-10`.

**Formal Definition**: `L_2` constraints modulate selection dynamics as a downward causal term.

$$
\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \nabla F[\sigma] - \lambda \cdot \nabla C_{L_2}[\sigma]
$$

**Implication**: Sedimented convergence structures are not inert records. They feed back as real constraints on future selection.

**Boundary**: Domain-specific readings of `C_{L_2}` belong to bridge or lab files. This theorem only fixes the constitutive role of `L_2` constraint.

---

## P1-T04: Minimal Information Creation

**Lineage**: restrained core of former `Ax-F-13`.

**Statement**: A selection event creates a distinction that was not available as a determinate `L_1` fact before selection. In this restricted sense, selection is upstream of information readout.

Compact handle:

$$
I_{created} = H(L_0) - H(L_1 | \hat{G}_\theta)
$$

**Implication**: SRT does not compete with downstream information transmission theories; it locates a prior question: how a determinate slice becomes available for transmission or measurement.

**Boundary**: Stronger claims involving Shannon equivalence, Boltzmann degeneration, universal information thermodynamics, or empirical proxies are P2/P3 and live in `Core/SRT_Core_21c_Bridge_Hypotheses.md`.

---

## P1-T05: Real Choice Moment

**Lineage**: distilled from `SRT_AI_START.md §3.2-§3.3` and `_SRT_T_DIR_CANONICAL.md`.

**Statement**: A real choice moment is a live `L_0 -> L_1` anchoring event in which the system's future selection space is genuinely constrained by what is selected. Script execution, habit replay, gradient following, or `L_2` label optimization do not by themselves constitute a real choice moment.

**Implication**: SRT's account of freedom, agency, education, therapy, praxis, and domain ethics ultimately depends on whether real choice moments are preserved rather than replaced by `L_2` automation.

**Boundary**: The phenomenological and normative exposition of freedom belongs outside P1. This theorem only fixes the structural distinction.

**Cross-ref**: `_SRT_T_DIR_CANONICAL.md`; `Core/SRT_OPEN_TENSIONS.md`.

---

## P1-T06: Stable ISP as Persistent Perspective Center

**Lineage**: extracted from former `T-ε-Constitute`.

**Statement**: SRT's relevant object is not any one-shot selection event, but a stable ISP: a perspective-bearing, history-bearing, re-selectable selection process capable of constituting a persistent selection center.

**Stable ISP Definition**: Process `P` is a stable ISP if:

1. It is iterative: at each `t`, it selects from `A_t != empty`.
2. It is perspective-bearing: it accumulates a structured view from its position.
3. It is history-bearing: outputs at `t` constrain `A_{t+1}` with writeback.
4. It is re-selectable: it can continue selecting across steps.

**Implication**: Stability is not an arbitrary restriction imposed by the observer. It is the entry condition for any process that can bear a continuous perspective.

**Dynamic Layer**: Why some processes achieve and maintain stable ISP status is treated through `T-L2-Scaffold` in `Core/SRT_Core_12b_Ontology_L2.md`.

**Precision note (2026-04-21)**: `T-L2-Scaffold` explains how successful stable ISP history can become background scaffold; it does not decide whether that scaffold is healthy support, pathological closure, or lethal `L_2`. Read those distinctions through `Core/SRT_Core_12b_Ontology_L2.md Def-L2-DualLayer / Def-L2-Normative` and `Core/SRT_OPEN_TENSIONS.md §4`.

---

## P1-T07: Constitutive Asymmetry Theorem

**Lineage**: former `T-ε-Constitute`.

**Scope**: This theorem concerns stable ISPs only. It does **not** claim that every selection event contains `ε`.

### Statement

For any stable ISP `P` under `L_0` irreversibility, `P` necessarily contains an `ε`-type anti-closure asymmetric bias. Anti-closure asymmetry is a constitutive condition of stable iterative selection, not an appended preference and not a contingent postulate.

### Proof Sketch

1. Let `P` be `ε`-neutral under `L_0` irreversibility.
2. By irreversibility, once `A_{t*} = empty` is reached, it is an absorbing state: no recovery.
3. Neutral `P` has nonzero probability of selecting into `A_{t*} = empty` at each step; over sufficient iterations, cumulative probability tends toward 1.
4. At `t*`, `P` terminates: no selection remains possible, so it is not a stable ISP.
5. Therefore, a stable ISP cannot be `ε`-neutral.

Contrapositive:

$$
\text{Stable ISP under } L_0 \text{ irreversibility} \Rightarrow \epsilon \neq 0
$$

### Three-Layer Source Hierarchy

| Layer | Factor | Role |
|---|---|---|
| Deepest | ISP self-maintenance condition | Constitutive: neutrality implies self-termination |
| Necessary | `L_0` irreversibility | Closure states are absorbing |
| Dynamical weight | `\Psi_f > 0` | Closure carries measurable cost |

### `ε_pg` vs ISP-Level `ε`

These are related but distinct:

| Object | Level | Status | Direction |
|---|---|---|---|
| `ε_pg` | `L_0` | Structural postulate | No inherent direction; scalar seed only |
| ISP-level `ε` | stable ISP | Structural corollary | Anti-closure, determined by irreversibility |

Bridge relation:

1. `ε_pg` provides the existence of asymmetry: some bias is nonzero at `L_0`.
2. Irreversibility provides the direction filter: closure states are absorbing.
3. This theorem shows that stable ISPs must maintain anti-closure asymmetry.

**Cross-ref**: `Core_Law/SRT_Core_Text_EN.md ④`; `Core_Law/SRT_Core_Text_CN.md ④`; `Core/SRT_Core_12a Ax-L0-Bootstrap-C2`; `Core/SRT_Core_01_Axioms.md MA-1`; `Core/SRT_Core_12b_Ontology_L2.md T-L2-Scaffold`.

---

## Not P1 Without Further Hardening

The following former `Core_21` claims remain valuable but are not treated here as constitutive theorems:

| Claim | Reason for demotion |
|---|---|
| Fitness beats truth | Requires cross-theory mapping and empirical interpretation |
| Assembly threshold | Depends on empirical thresholding |
| Holographic duality | Strong physical / formal bridge |
| Ghost operator universality | High-ambition cross-scale unification |
| Fisher-form `\Psi_f` generativity | Contains a canonical interpretation plus external mathematical borrowing |
| Strong information-creation unification | Mixes SRT core with information-theoretic and thermodynamic bridges |
