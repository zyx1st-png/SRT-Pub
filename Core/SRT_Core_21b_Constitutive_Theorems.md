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

**L1 Expansion**: `Core_Law/SRT_Irreversibility.md` Def-IRR-2 / T-IRR-1（学习不可逆的非对称 `Ψ_f` 支付）把 `L_0` 不可逆性从 P1-T02 的推论展开为可引用 L1 层；热力学二律与 FEP 自由能最小化**不**由此获得反向定义权。

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

**EX-A / PC-A precision**: This P1 claim is qualitative and distinction-based. It does not require a global entropy `H(L_0^{abs})`, and no unqualified entropy subtraction is part of the theorem. Conditional information-theoretic readouts over declared random variables, partitions, and measures belong to P2/P3-B09 in `Core/SRT_Core_21c_Bridge_Hypotheses.md`.

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

**Statement**: SRT's relevant object is not any one-shot selection event, but a stable ISP: a perspective-bearing, history-bearing process that persists as the same selection center through recurrent historical reconstitution.

**Stable ISP Definition**: Process `P` is a stable ISP if:

1. It is iterative: over the declared interval, it repeatedly encounters live, non-equivalent candidates rather than merely replaying a closed script.
2. It is perspective-bearing: it accumulates a structured view from its position.
3. It is history-bearing: outputs at `t` constrain `A_{t+1}` with writeback.
4. It is **continued-selectable**: the same history-bearing process can continue receiving live candidates and bearing the downstream consequences of what it selected.

**Structural stabilisation (ST-A, 2026-08-11)**: Stability here means recurrent reconstitution of a recognizable history-bearing organization across a declared perturbation range. It does not require microstate identity, convergence to a fixed point, or continuous activity without pause. A later externally reset replica or a fresh process is not, merely by resembling the earlier state, evidence that the same ISP continued.

**Implication**: Stability is not an arbitrary restriction imposed by the observer. It is the entry condition for any process that can bear a continuous perspective.

**ST-A boundary**: Continued selectability is the P1 minimum. The stronger property of **generative reselectability**—consequence-sensitive revision of the process's own comparison rules, boundaries, or candidate-generation conditions—is not required to identify every stable ISP and is not a P1 theorem. It is a P2/P3 criterion for generative health in `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13`. Structural stability therefore does not by itself establish generative health.

**Dynamic Layer**: Why some processes achieve and maintain stable ISP status is treated through `T-L2-Scaffold` in `Core/SRT_Core_12b_Ontology_L2.md` (path-layer trace dynamics) and through the operator-layer self-reference ratio `σ` in `Core_Law/SRT_Individuation.md` (entry-transition dynamics). The four conditions above are the **result-state criterion** for being a stable ISP; `T-IND-2` in the individuation file is the **entry-dynamics criterion** for when a process crosses into that state. Self-consciousness is treated there as a distinct second-order condensate (second phase transition at `σ_self`), not as a precondition for being a stable ISP.

**Precision note (2026-04-21)**: `T-L2-Scaffold` explains how successful stable ISP history can become background scaffold; it does not decide whether that scaffold is healthy support, pathological closure, or lethal `L_2`. Read those distinctions through `Core/SRT_Core_12b_Ontology_L2.md Def-L2-DualLayer / Def-L2-Normative` and `Core/SRT_OPEN_TENSIONS.md §4`.

---

## Former P1-T07: Unconditional Constitutive Asymmetry Claim (Demoted by ST-A)

**Lineage**: former `T-ε-Constitute` and former P1-T07.

**Decision record (ST-A, 2026-08-11)**: The former unconditional statement—"every stable ISP necessarily contains an anti-closure `ε` bias"—is no longer a P1 theorem. Its proof inferred cumulative absorption from a per-step nonzero closure probability without independently defining a neutral kernel, fixing the stability semantics, or proving that the neutral kernel reaches the absorbing state. `L_0` irreversibility alone does not supply those missing premises.

**Unconditional P1 remainder**: If a realized history reaches `A_{t_*}=\varnothing`, that history cannot continue selecting from that state. Any later recovery requires a new event, an external reset, or a separately specified transition; it is not licensed by the terminated history itself.

**What remains open**: A conditional anti-closure result may be recoverable only after (i) a stability semantics is chosen, (ii) an `ε`-neutral kernel is independently defined, and (iii) absorption or comparative closure risk is proved for that kernel over a declared horizon and environment. The current candidate lives at P2/P3 in `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13`; it must not be cited as P1.

**`ε_pg` boundary**: `ε_pg` remains an `L_0` structural postulate and scalar seed. ST-A does not derive an ISP-level anti-closure direction from it, nor from irreversibility alone.

**Audit trail**: `Operations/Audits/SRT_P1_T07_PROOF_HARDENING_AUDIT.md`; `Operations/Proposals/SRT_P1_T07_HARDENING_OPTIONS.md`.

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
| Former `P1-T07 / T-ε-Constitute` unconditional anti-closure theorem | Neutral dynamics, stability semantics, and absorption were not independently established; conditional candidate moved to 21C B13 |
