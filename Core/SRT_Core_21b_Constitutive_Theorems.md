---
id: SRT-CORE-21B-CONSTITUTIVE-THEOREMS
type: theorem_set
tags: [Formal logic, Constitutive Theorems, Claim Ladder]
status: active
version: v4
layer: L1
epistemic_layer: os
claim_mode: canonical
claim_level: P1
dependency: [SRT-CORE-21A-MINIMAL-AXIOMS, SRT-ONE-FORMATION, SRT-CLAIM-LADDER, SRT-CORE-12B]
---

# SRT Core 21B: Constitutive Theorems

> **Role**: This file contains P1 claims: not primitive axioms, but constitutive consequences of the SRT core structure.
> P1 claims may be cited as canonical SRT theorems, but not as primitive axioms.
>
> **RC-A author decision (2026-08-17)**: former `P1-T05: Real Choice Moment` is demoted out of P1. Its anti-script insight is retained only as a downstream P2/P3 agency / subjecthood guard. It must not be used as a criterion for whether `Selection` occurs. SRT's primary theoretical object remains `Selection`, not a new taxonomy of `Choice`.

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

**Scope**: This statement applies in a declared retained-history / converged-constraint regime in which the relevant `L_2` structure has been independently admitted. `L_2` is an analytic/model-facing aspect of the same Selection reality, not a universal pre-existing ontic container in which causality already lives.

**Implication**: Causality is a projected structure inside the convergence domain, not an ontological primitive prior to selection.

**Layer Note**: This theorem defines **horizontal causality** inside `L_2`. It does not replace vertical constitution across `L_0 -> L_1 -> L_2`.

**Cross-ref**: `Philosophy/SRT_Causality_Time.md §一`; `Core/SRT_Core_12a T-L0-Kappa0`.

---

## P1-T02: Ontological Time as Memory Horizon

**Lineage**: former `Ax-F-03b`.

**Title note**: The historical title is retained for citation stability. The P1 theorem no longer identifies time universally with a memory horizon or continuously retained `L_2` record.

**P1 Statement — occurrence asymmetry**: Once an actual Selection has occurred, later reality is not ontically identical to the counterfactual in which that Selection never occurred.

```text
occurred != never-occurred;
occurred -/> later-readable trace;
occurred -/> durable or localized memory;
occurred -/> retained historical efficacy;
occurred -/> automatic L2 object.
```

This is an asymmetric facticity floor. It does not require the event to remain readable, causally active or represented in a later local structure.

**History boundary**: A historical record is present only where prior Selection remains materially effective in later Selection conditions and that retained efficacy is independently established. Path dependence, anchoring persistence, learning/writeback residue and durable memory are stronger model/domain claims.

**Conditional formalization — model/domain scope**: In a declared regime where anchoring, operator attribution and retained historical efficacy have independently been established, the earlier expression may define a model-specific historical/ontological-time measure:

$$
t_{\text{onto}} \equiv \int \|\hat{G}_\theta(s)\| ds
$$

The equation is not an unconditional P1 identity and does not create a universal time scalar. Its metric, attribution, retention rule and horizon belong to the declared formalization.

**Time distinctions**:

```text
parametric ordering
!= occurrence non-equivalence
!= retained historical record
!= model-specific ontological-time measure.
```

The exact universal theory of time remains **OPEN**. Absence of durable trace or `L_2` retention does not imply that no Selection occurred or that occurrence asymmetry disappears.

**Time Layer Note**: This theorem concerns **ontological time**. Parametric time `t` in equations remains a mathematical ordering variable and does not by itself carry the ontological claim.

**Cross-ref**: `Philosophy/SRT_Causality_Time.md §二`; `Core/SRT_Core_12a Ax-L0-Bootstrap-C2`; `Core/SRT_Core_01_Axioms.md MA-1`.

**L1 Boundary**: `Core_Law/SRT_Irreversibility.md` separates occurrence non-equivalence from durable trace, path dependence, absorbing dynamics and `\Psi_f` accumulation. Its T-IRR-1 learning/writeback material is a conditional P2/P3 model candidate, not a universal expansion of P1-T02. No universal monotonic `\Psi_f` stock or time arrow follows from this theorem.

---

## P1-T03: `L_2` Downward Constraint

**Lineage**: former `Ax-F-10`.

**Formal Definition**: `L_2` constraints modulate selection dynamics as a downward causal term.

$$
\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \nabla F[\sigma] - \lambda \cdot \nabla C_{L_2}[\sigma]
$$

**Implication**: Sedimented convergence structures are not inert records. They feed back as real constraints on future selection.

**Retention Boundary**: `L_2` here means an admitted retained/sedimented structure whose material efficacy in later Selection conditions has been established. P1-T03 does not imply that every Selection automatically creates an `L_2` object, that every past event remains active, or that every event produces a persistent constraint.

**Boundary**: Domain-specific readings of `C_{L_2}` belong to bridge or lab files. This theorem only fixes the constitutive role of an admitted `L_2` constraint.

---

## P1-T04: Minimal Information Creation

**Lineage**: restrained core of former `Ax-F-13`.

**Statement**: A selection event creates a distinction that was not available as a determinate `L_1` fact before selection. In this restricted sense, selection is upstream of information readout.

**EX-A / PC-A precision**: This P1 claim is qualitative and distinction-based. It does not require a global entropy `H(L_0^{abs})`, and no unqualified entropy subtraction is part of the theorem. Conditional information-theoretic readouts over declared random variables, partitions, and measures belong to P2/P3-B09 in `Core/SRT_Core_21c_Bridge_Hypotheses.md`.

**Implication**: SRT does not compete with downstream information transmission theories; it locates a prior question: how a determinate slice becomes available for transmission or measurement.

**Boundary**: Stronger claims involving Shannon equivalence, Boltzmann degeneration, universal information thermodynamics, or empirical proxies are P2/P3 and live in `Core/SRT_Core_21c_Bridge_Hypotheses.md`.

---

## Former P1-T05: Real Choice Moment (Demoted by RC-A, 2026-08-17)

**Lineage**: distilled from `SRT_AI_START.md §3.2-§3.3` and `_SRT_T_DIR_CANONICAL.md`.

**Former statement**: A real choice moment was described as a live `L_0 -> L_1` anchoring event in which the system's future selection space is genuinely constrained by what is selected, with script execution, habit replay, gradient following, or `L_2` label optimization treated as insufficient by themselves.

**RC-A author decision**: this claim is **no longer a P1 constitutive theorem**.

### Why it was demoted

1. SRT's primary theoretical object is `Selection`, not `Choice`.
2. Canonical L0 already distinguishes basic, unfolding, and subject-level selection. Scripted, habitual, gradient-driven, or `L_2`-scaffolded dynamics therefore cannot be inferred to be selection-free merely because they fail an agency-level criterion.
3. Mature `L_2` is a background scaffold produced by prior selective convergence and remains dynamically operative. Automation can carry / reproduce selection history and can coexist with ongoing selection at other scales or dimensions.
4. A2/A3 adversarial work did not produce a positive, non-circular, rival-discriminating observable that would justify treating the former anti-script boundary as a constitutive theorem of Selection.
5. Treating the anti-script clause as a Selection criterion generated the unnecessary `Live Choice` problem and conflated selection ontology with downstream agency / subjecthood questions.

### What survives

A narrower negative guard remains useful at P2/P3:

> **Script execution, habit replay, gradient following, or `L_2` automation are not by themselves sufficient to establish stronger agency / subject-level revision standing.**

This guard lives downstream in:

`03_Bridges/SRT_Agency_Automation_Guard_2026-08-17.md`.

### Hard inference guards

Do **not** infer:

```text
fails former P1-T05
-> no Selection occurred
```

Do **not** infer:

```text
script / habit / gradient / L2 automation
-> selection-free process
```

Do **not** infer:

```text
passes the downstream agency guard
-> subjecthood / consciousness / freedom / moral responsibility proved
```

No P1 `Real Choice Moment` theorem remains after RC-A.

---

## P1-T06: Stable ISP Standing and Persistent Perspective

**Lineage**: extracted from former `T-ε-Constitute`; R1 standing boundary clarified 2026-09-11 after the author-adjudicated #938 reconstruction repair.

**Statement**: P1-T06 defines a **recurrent standing criterion**, not the definition of `Selection` and not a generation law for upstream formed positional organization. A stable ISP is a perspective-bearing, history-bearing process that persists as the same selection center through recurrent historical reconstitution and remains continued-selectable over a declared interval and perturbation range.

**Stable ISP Definition**: Process `P` is a stable ISP if:

1. It is iterative: over the declared interval, it repeatedly encounters **currently effective, non-equivalent candidates** rather than merely replaying a closed script.
2. It is perspective-bearing: it accumulates a structured view from its position. **At P1-T06 this is a standing condition; it does not assert that perspective first appears only at Stable-ISP standing.**
3. It is history-bearing: outputs at `t` constrain `A_{t+1}` with writeback.
4. It is **continued-selectable**: the same history-bearing process can continue receiving currently effective candidates, while consequences of what it selected can return into that same process's later history / selection conditions.

**Consequence-typing guard (R1, 2026-09-11)**: condition 4's downstream consequence relation means consequence return / coupling to the same history-bearing process. It is **not by itself** a sufficient criterion for the separately reconstructed `Bearer` problem, `承担`, non-outsourcable stake, subject-position, consciousness, or phenomenality.

**Terminology guard (RC-A)**: `currently effective` is descriptive scope language, not a new `Live Choice` / `live selection` concept. P1-T06 concerns stable ISP standing, not the definition of Selection itself.

**Structural stabilisation (ST-A, 2026-08-11)**: Stability here means recurrent reconstitution of a recognizable history-bearing organization across a declared perturbation range. It does not require microstate identity, convergence to a fixed point, or continuous activity without pause. A later externally reset replica or a fresh process is not, merely by resembling the earlier state, evidence that the same ISP continued.

**Formation / standing boundary (R1, 2026-09-11)**: recurrent historical reconstitution and writeback are relevant to continuity and Stable-ISP standing. They must not, by themselves, be used to derive active vertical organization, a formed position, `Bearer`, or subjecthood. P1-T06 therefore does not organize the ontology as `formed process -> Stable ISP -> subject-position`. The canonical semantic owner for the thinner upstream formation is `Core_Law/SRT_One_Formation.md`; P1-T06 still does not supply a necessary-and-sufficient theorem for One formation.

**Implication**: Stability is not an arbitrary restriction imposed by the observer. P1-T06 identifies a **strong persistent-perspective standing** for a recurrent selection process. It does not claim to mark the first ontological appearance of perspective, and Stable-ISP standing does not by itself establish subject-position.

**ST-A boundary**: Continued selectability is the P1 minimum. The stronger property of **generative reselectability**—consequence-sensitive revision of the process's own comparison rules, boundaries, or candidate-generation conditions—is not required to identify every stable ISP and is not a P1 theorem. It is a P2/P3 criterion for generative health in `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13`. Structural stability therefore does not by itself establish generative health.

**Dynamic-layer boundary (R1, 2026-09-11)**: downstream L1 models may propose mechanisms or coordinates for entry into, maintenance of, or departure from Stable-ISP standing. P1-T06 does not by itself authorize any model coordinate—including a `σ` threshold—as the ontological event of formed-position, Stable-ISP, or subject entry. Exact threshold ownership remains separately governed by the relevant L1/formal owner and current OPEN register.

**Precision note (2026-04-21)**: `T-L2-Scaffold` explains how successful stable ISP history can become background scaffold; it does not decide whether that scaffold is healthy support, pathological closure, or lethal `L_2`. Read those distinctions through `Core/SRT_Core_12b_Ontology_L2.md Def-L2-DualLayer / Def-L2-Normative` and `Core/SRT_OPEN_TENSIONS.md §4`.

---

## Former P1-T07: Unconditional Constitutive Asymmetry Claim (Demoted by ST-A)

**Lineage**: former `T-ε-Constitute` and former P1-T07.

**Decision record (ST-A, 2026-08-11)**: The former unconditional statement—"every stable ISP necessarily contains an anti-closure `ε` bias"—is no longer a P1 theorem. Its proof inferred cumulative absorption from a per-step nonzero closure probability without independently defining a neutral kernel, fixing the stability semantics, or proving that the neutral kernel reaches the absorbing state. `L_0` irreversibility alone does not supply those missing premises.

**Unconditional P1 remainder**: If a realized history reaches `A_{t_*}=\varnothing`, that history cannot continue selecting from that state. Any later recovery requires a new event, an external reset, or a separately specified transition; it is not licensed by the terminated history itself.

**What remains open**: A conditional anti-closure result may be recoverable only after (i) a stability semantics is chosen, (ii) an `ε`-neutral kernel is independently defined, and (iii) absorption or comparative closure risk is proved for that kernel over a declared horizon and environment. The current candidate lives at P2/P3 in `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13`; it must not be cited as P1.

**`ε_pg` boundary**: `ε_pg` is a separately owned formal / model-facing quantity where independently admitted. P1-T07 does not derive an ISP-level anti-closure direction from it, nor from irreversibility alone. Its exact inheritance from primitive Selection remains separately governed / **OPEN**.

```text
epsilon_pg -/> universal primitive direction;
epsilon_pg -/> continuation preference;
epsilon_pg -/> health or goodness;
epsilon_pg -/> consciousness seed.
```

**Audit trail**: `Operations/Audits/SRT_P1_T07_PROOF_HARDENING_AUDIT.md`; `Operations/Proposals/SRT_P1_T07_HARDENING_OPTIONS.md`.

---

## Not P1 Without Further Hardening

The following former `Core_21` claims remain valuable but are not treated here as constitutive theorems:

| Claim | Reason for demotion |
|---|---|
| Former `P1-T05 / Real Choice Moment` | RC-A: anti-script exclusion is an agency/subjecthood bridge guard, not a constitutive theorem or Selection criterion |
| Fitness beats truth | Requires cross-theory mapping and empirical interpretation |
| Assembly threshold | Depends on empirical thresholding |
| Holographic duality | Strong physical / formal bridge |
| Ghost operator universality | High-ambition cross-scale unification |
| Fisher-form `\Psi_f` generativity | Contains a canonical interpretation plus external mathematical borrowing |
| Strong information-creation unification | Mixes SRT core with information-theoretic and thermodynamic bridges |
| Former `P1-T07 / T-ε-Constitute` unconditional anti-closure theorem | Neutral dynamics, stability semantics, and absorption were not independently established; conditional candidate moved to 21C B13 |
