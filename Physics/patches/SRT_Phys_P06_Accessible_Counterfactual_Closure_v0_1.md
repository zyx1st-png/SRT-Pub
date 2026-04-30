---
id: SRT-PHYS-P06-ACCESSIBLE-COUNTERFACTUAL-CLOSURE
type: hardening_patch
tags: [Physics, Counterfactual Closure, Accessibility, Record Stabilization, Objectivity, Causality, Boundary, Scale, Phase Transition, Noise, Symmetry, Locality, Time, Gravity, Bell, d-value, Psi_f, Bridge]
status: active_v0_1
layer: L1
epistemic_layer: bridge
claim_mode: bridge
canonical_status: non_canonical
canonical: false
date: 2026-04-30
dependency:
  - Physics/README.md
  - Physics/SRT_Physics_Claim_Status.md
  - Physics/_SRT_Phys_Bridge.md
  - Physics/_SRT_Physics_Hardening_Index.md
  - Physics/Extensions/SRT_Phys_E01_Quantum_Instrument_Bridge.md
  - Physics/Extensions/SRT_Phys_E02_Quantum_Reference_Frames_Bridge.md
  - Physics/Extensions/SRT_Phys_E03_Information_Thermodynamics_Bridge.md
  - Physics/Extensions/SRT_Phys_E04_Relational_Time_Bridge.md
  - Physics/Extensions/SRT_Phys_E05_Falsifiability_Program.md
  - _SRT_PSI_F_CANONICAL.md
  - _SRT_D_VALUE_CANONICAL.md
  - _SRT_SYMBOL_TABLE.md
machine_summary: >
  Non-canonical physics hardening patch introducing accessible counterfactual
  closure as a unifying bridge concept for SRT physics. Defines
  L0_accessible^phys(theta,t) as the physically projected, currently selectable
  subset of L0 under theta, time, L2 constraints, and Psi_f payability;
  defines Psi_f^phys as a physical projection of anchoring and stabilization
  burdens; defines d_phys only as a physical projection of d-value; keeps
  gravity limited to reshaping the physically accessible domain; treats Bell
  results as showing that L1/L2 local-object intuitions cannot be directly
  projected onto L0; and collects P9-P23 as candidate future hardening lines
  for causality, objects, scale, phase transition, noise, measurement,
  boundary, energy, symmetry, locality, path integrals, entropy, vacuum,
  particles, and laws. Bridge layer only; does not modify canonical primitives
  or assert new established physics.
---

# SRT Physics P06: Accessible Counterfactual Closure

> This file is a non-canonical physics hardening patch. It is a bridge / pressure-test document, not an established physics theory. It does not solve the measurement problem, derive Born rule, derive gravity, derive physical constants, refute MWI, rewrite Bell inequalities, or redefine canonical L0/L1/L2, Psi_f, d-value, or G_hat_theta.

## 0. Motivation: from collapse bridge to fact-formation grammar

Physics/E01-E05 already connect the SRT physics direction to quantum instruments, quantum reference frames, information thermodynamics, relational time, and a Lakatos-style falsifiability programme. That work gives SRT better formal homes, but it still carries a danger: the Physics layer can be read as SRT renaming existing physics.

The weak point is especially visible in measurement language. "Measurement as selection" is a useful bridge, but it stays too close to collapse-family vocabulary. A sharper SRT-native question is:

```text
How does an accessible physical possibility become an irreversible future-constraining fact?
```

中文：

```text
一个可接入的物理可能性如何变成一个不可撤销、约束未来的事实？
```

Core sentence:

```text
Reality is accessible counterfactual closure stabilized into low-friction readout structure.
```

中文：

```text
现实 = 可接入反事实空间的关闭，并稳定为低摩擦读出的结构。
```

P06 does not replace E01-E05. It gives them an upper-level bridge object: **accessible counterfactual closure**. E01-E05 remain the formal homes and pressure-test interfaces; P06 supplies the fact-formation grammar they can share.

## 1. Core schema

```text
L0
  -- physical projection pi_phys -->
physical projected possibility space
  -- accessibility filtering by theta, time, L2 constraints, Psi_f payability, boundary, reservoir, history -->
L0_accessible^phys(theta,t)
  -- G_hat_theta anchoring / record stabilization -->
L1_record
  -- redundancy / repeated readout / low marginal Psi_f -->
L2_phys
```

Not every possibility in the absolute latent domain `L0` can enter physical selection. The key move in the SRT physics bridge is not "random collapse from all possibilities." It is asking which latent states remain actually enterable by a selection operator under the current physical projection and current accessibility constraints.

The bridge object is therefore:

```text
physical projection -> accessibility filtering -> anchoring -> irreversible record -> low-friction readout
```

This schema is not a new accepted physics formalism. It is a P3 bridge grammar for connecting SRT primitives to physical-domain pressure tests without redefining those primitives.

## 2. Definition: L0_accessible^phys(theta,t)

`L0_accessible^phys(theta,t)` is the set of latent physical states that remain actually enterable by the selection operator after the absolute latent domain `L0` is projected through `pi_phys`, under the current selection position `theta`, current time `t`, current `L2`-stabilized constraints, and `Psi_f` payability conditions.

中文定义：

> `L0_accessible^phys(θ,t)` 是绝对潜在域 `L0` 经物理投影 `π_phys` 后，在当前选择位置 `θ`、当前时间 `t`、当前 `L2` 稳定约束与 `Psi_f` 可支付条件下，仍可被选择算子实际进入的潜在状态集合。

Bridge-level placeholder:

```text
L0_accessible^phys(theta,t)
  := { x in pi_phys(L0) | x is enterable by G_hat_theta under L2_phys(t) and payable Psi_f^phys conditions }
```

The `:=` marks a bridge-level definition, not an accepted definition in physics.

Boundaries:

- Do not identify `L0_accessible^phys` with Hilbert space.
- Do not identify `L0_accessible^phys` with `L0` itself.
- Hilbert space, phase space, path-integral domain, and configuration space are candidate physical projections of `pi_phys(L0)`, not the absolute `L0`.

`L0_accessible^phys` is an operational-ontological bridge term: it is not merely subjective ignorance, but it is also not the full absolute latent domain.

## 3. Definition: Psi_f^phys

`Psi_f^phys` is the physical projection of the burdens incurred when a latent physical state is selected, anchored, and maintained as a stable manifest state: information compression, dissipation, curvature / distinguishability burden, and stabilization-maintenance cost.

中文定义：

> `Psi_f^phys`：当一个潜在物理状态被选择、锚定并维持为稳定显现态时，对应的信息压缩、耗散、曲率/可区分性负担与稳定性维持成本的物理投影。

Bridge relation:

```text
Psi_f^phys(event)
  ~ physical burden of [latent physical candidate -> anchored stable manifest record]
```

The `~` is a bridge-level tracking / monotone relation, not strict equality.

Boundaries:

- Canonical `Psi_f` remains in `_SRT_PSI_F_CANONICAL.md`.
- `Psi_f^phys` must not redefine canonical `Psi_f`.
- `Psi_f^phys` must not be identified with raw entropy, raw Fisher information, thermodynamic free energy, Landauer cost, curvature, or energy.
- E03's `sigma_f^phys` remains one possible proxy in record-stabilization / dissipative regimes.

`Psi_f^phys` is not "new energy." It is a physical projection of payability / anchoring / stabilization burden.

## 4. Fact formation: L1 as irreversible future constraint

An `L1` physical fact is not merely an outcome. It is an anchored outcome whose future counterfactual space has been constrained by an irreversible record.

中文：

> 一个 `L1` 物理事实不是单纯结果，而是一个被锚定、被记录、并对未来反事实空间产生约束的显现态。

Formula placeholder:

```text
L1_fact = anchored_outcome + irreversible_future_constraint
```

This shifts the SRT physics direction from a collapse problem to a fact formation problem.

Forbidden readings:

- Do not say global wavefunction collapse.
- Do not say conscious observer causes collapse.
- Do not say SRT solves measurement problem.
- It is acceptable to say collapse-family language is one possible bridge reading.

In Everett / MWI-compatible language, P06 can be read as branch-relative or frame-relative fact formation: a record-bearing branch / frame / subsystem closes accessible counterfactuals relative to its own physical position, without asserting global collapse.

## 5. Counterfactual closure

Counterfactual closure is the process by which states in `L0_accessible^phys(theta,t)` cease to remain equally enterable after a stable `L1` record is formed.

中文：

> 反事实关闭是指：当一个稳定 `L1` 记录形成后，原本在 `L0_accessible^phys(theta,t)` 中仍可进入的候选状态，不再以同样方式保持可进入。

The sequence is:

1. Absolute `L0` passes through `pi_phys` into a physical candidate domain.
2. Current `theta / t / L2 / Psi_f` payability filters that domain into `L0_accessible^phys`.
3. `G_hat_theta` anchors one candidate.
4. After record stabilization, the future enterability of other counterfactual candidates is closed or lowered.
5. That closure sediments into low-marginal-readout structure.

Reality is therefore not simply "possibility becomes result." It is accessible counterfactual closure whose cost and residue become part of future physical accessibility.

## 6. Time as closure order

Manifest physical time is the ordering structure induced by irreversible counterfactual-closure events. Clock time is the operational readout of this ordering under a chosen `theta`-clock.

Bridge placeholder:

```text
t_order = partial order of irreversible counterfactual closures
```

中文：

> 显现物理时间是不可逆反事实关闭事件诱导出的排序结构；钟表时间是在某个 `theta`-clock 下对这种排序的操作性读出。

Boundaries:

- Do not write time is discrete in SRT.
- Do not write Planck time is derived as SRT tick.
- H-Phys-2 remains a speculative bridge.
- E04 relational time remains the safer primary formal home.

P06 is structurally aligned with E04: closure order can be operationally read through clock-conditioned states, without turning any clock variable into an absolute time container.

## 7. Objectivity as low marginal readout friction

Objective physical reality is the regime where the marginal `Psi_f^phys` required for additional readout approaches zero, while the original stabilization cost remains historically embedded.

中文：

> 客观物理现实是新增读出所需边际 `Psi_f^phys` 趋近于零的状态；但初始稳定成本没有消失，而是沉积在 `L2_phys` 结构中。

Formula placeholder:

```text
Objectivity_phys(x) iff Delta Psi_f^phys_readout(x | theta_i) -> 0 for admissible additional theta_i
```

Quantum Darwinism / environmental redundancy can be treated as candidate physical images of this low-marginal-readout regime. Do not write Quantum Darwinism is identical to SRT. Safer wording:

```text
Quantum Darwinism is structurally aligned under a bridge projection.
```

Objectivity is therefore not zero object-maintenance cost. It is low marginal readout friction after prior stabilization costs have already been paid and embedded.

## 8. Physical L2 kernel

`L2_phys` is the invariant kernel preserved under admissible `theta`-transformations and stable enough to constrain future accessibility.

中文：

> `L2_phys` 是所有可允许 `theta` 转换下仍保持的不变量核，并且足以反过来约束未来的可接入性。

Core guardrail:

```text
Selection does not create conservation laws; selection is constrained by the L2_phys kernel.
```

This prevents physical law from being rewritten as subjective consensus. The physical-layer `L2` names stable readability, invariant constraints, conservation structures, boundary conditions, and repeatability protocols under the physical bridge. It is not social agreement.

## 9. d_phys as physical projection of d-value

`d_phys` can enter the Physics layer only as a physical projection of d-value. It must not rewrite the canonical definition of d-value.

中文：

> `d_phys` 可以进入 Physics 层，但只能定义为 d-value 的物理投影，不应反向改写 d 的 canonical 定义。

Bridge-local definition:

```text
d_phys(event) measures the bandwidth of future counterfactual constraints imposed by an irreversible physical record.
```

中文：

> `d_phys(event)` 衡量一个不可逆物理记录对未来反事实空间施加约束的带宽。

Boundaries:

- `d_phys` does not imply agency.
- `d_phys` does not imply consciousness.
- `d_phys` does not imply concern in particles.
- `d_phys` is not entanglement entropy.
- Entanglement entropy / area laws may be candidate proxies only in limited bridge projections.
- Canonical d-value remains in `_SRT_D_VALUE_CANONICAL.md`.

Cross-layer reading:

| Layer | d-value reading |
|---|---|
| Physical | future-consequence bandwidth of irreversible records |
| Biological | viability-relevant constraint bandwidth |
| Conscious | concern / stake bandwidth |
| Social | institutional future-action constraint bandwidth |

This table is a bridge map. It is not a replacement for canonical d-value.

## 10. Gravity boundary

P06 keeps one physical-facing claim:

```text
Gravity reshapes the physically accessible domain.
```

中文：

```text
引力重塑物理可接入域。
```

In this patch, gravity is treated only as a physical structure that can reshape `L0_accessible^phys(theta,t)` by modifying causal reachability, clock relations, horizon structure, and path availability.

Forbidden boundary:

- P06 does not define gravity as `Psi_f`.
- P06 does not derive Einstein equations.
- P06 does not write G_{\mu\nu} ∝ Psi_f.
- P06 does not propose a tensor-level reconstruction.
- Any future gravity programme requires separate adjudication under `Physics/SRT_Physics_Claim_Status.md`.

This keeps the gravity bridge at the level of accessibility geometry, not identity with friction.

## 11. Bell / nonlocality boundary

Bell results show that `L1/L2`-level intuitions about local objects cannot be directly projected onto `L0`.

中文：

> Bell 结果表明：`L1/L2` 层的局域对象直觉不能被直接投射到 `L0`。

SRT contribution:

```text
SRT does not rewrite Bell inequalities. It provides an interpretive grammar in which L0 is not pre-cut into classical local objects, and L1 facts emerge through theta-dependent selection anchoring.
```

中文：

> SRT 的贡献不是改写 Bell 不等式，而是提供一种解释语法：`L0` 并不预先按照经典局域对象切分，`L1` 事实通过 `theta` 相关的选择锚定形成。

Boundaries:

- Do not claim SRT derives Bell violations.
- Do not claim SRT refutes locality as used in relativity.
- Do not claim superluminal signalling.
- Do not claim hidden variables unless explicitly framed as not part of P06.
- Use no-signalling caution when discussing nonlocal correlations.

Recommended wording:

```text
Bell-type phenomena pressure any attempt to project L1/L2 local-object grammar backward into L0. P06 therefore treats L0 as prior to classical object-partition, while keeping all empirical Bell results and no-signalling constraints intact.
```

## 12. Relation to E01-E05

| Existing file | P06 relation |
|---|---|
| E01 quantum instrument | `L0_accessible^phys` is narrowed by outcome alphabet, Kraus family, dilation environment, and record channel. |
| E02 QRF | `theta_boundary` helps determine the accessible physical domain and frame-relative fact formation. |
| E03 information thermodynamics | `sigma_f^phys` is one proxy for `Psi_f^phys` in record-stabilization / dissipative regimes. |
| E04 relational time | closure ordering can be read operationally through `theta`-clock / clock-conditioned states. |
| E05 falsifiability | P06 may generate sharper future discriminators, but remains bridge-level until empirical handles exist. |

E01-E05 provide formal homes and pressure-test pathways. P06 provides their shared upper-level bridge object.

## 13. Candidate discriminators, stated conservatively

These are candidate bridge-level discriminators, not confirmed predictions.

### Candidate A

Two informationally equivalent record-stabilization processes with different `theta`-realizations may differ in residual stabilization burden.

This is a bridge-level candidate discriminator, not an established prediction.

### Candidate B

Changing `L0_accessible^phys` boundaries while preserving reduced dynamics may alter calibration / stabilization cost.

This is a bridge-level candidate discriminator, not an established prediction.

### Candidate C

Events with larger `d_phys` may require greater redundancy or stabilization burden to become low-marginal-readout facts.

This is a bridge-level candidate discriminator, not an established prediction.

### Candidate D

Bell-type setups can be used conceptually to test whether `L1/L2` local-object assumptions are being smuggled into `L0` descriptions, but P06 does not alter Bell predictions.

This is a bridge-level candidate discriminator, not an established prediction.

## 14. P9-P23: candidate future hardening lines

The following are candidate future hardening lines generated by the accessible-counterfactual-closure frame. They are not completed theory, not physics theorems, and not upgrades in claim level.

### P9. Causality as Counterfactual-Constraint Propagation

English:

> Causal influence is the propagation of counterfactual constraints from one closure event to later accessible domains.

中文：

> 因果影响是一个关闭事件对后续可接入域施加反事实约束的传播。

Guardrail:

Do not replace standard causal models or relativity. This is a bridge-level reading of how fact formation constrains future accessibility.

Suggested future target:

`Physics/patches/SRT_Phys_P08_Closure_Dynamics_and_Physical_Law_v0_1.md`

### P10. Objects as Stable Bundles of Closure Records

English:

> A physical object is a stable bundle of closure records whose mutual constraints allow low-cost re-identification across time and observers.

中文：

> 物理对象是闭合记录的稳定束；这些记录之间的互相约束，使它能在时间与观察者之间被低成本重新识别。

Guardrail:

Use this strongly for macroscopic objects. For fundamental particles, prefer "repeatable closure mode" rather than "mere record bundle."

Suggested future target:

`Physics/patches/SRT_Phys_P07_Closure_Ontology_of_Physical_Objects_v0_1.md`

### P11. Scale as Closure Depth

English:

> Scale is not merely spatial magnitude; it is the depth, redundancy, and cross-level persistence of counterfactual closure.

中文：

> 尺度不只是空间大小，而是反事实关闭的深度、冗余度与跨层持久性。

Guardrail:

Do not replace renormalization or scale physics. This is an SRT bridge reading of scale as closure depth.

Suggested future target:

`Physics/patches/SRT_Phys_P08_Closure_Dynamics_and_Physical_Law_v0_1.md`

### P12. Phase Transition as Closure-Protocol Restructuring

English:

> A physical phase transition is a restructuring of the closure protocol that determines which counterfactual degrees of freedom remain accessible.

中文：

> 物理相变是关闭协议的重构，它改变哪些反事实自由度仍可接入、哪些被稳定关闭。

Guardrail:

Do not claim all `L2` hardening is literally a physical phase transition. Say `L2` hardening may have phase-transition-like regimes.

Suggested future target:

`Physics/patches/SRT_Phys_P08_Closure_Dynamics_and_Physical_Law_v0_1.md`

### P13. Noise as Residual Unclosed Counterfactuality

English:

> Noise, under an SRT bridge reading, marks the residual openness of counterfactual degrees of freedom not yet stabilized into low-friction records.

中文：

> 在 SRT 桥接读法中，噪声标记尚未稳定为低摩擦记录的反事实自由度的残余开放性。

Guardrail:

Do not replace statistical noise models. Prefer: noise = unresolved degrees under finite `theta`-resolution.

Suggested future target:

`Physics/patches/SRT_Phys_P07_Closure_Ontology_of_Physical_Objects_v0_1.md`

### P14. Measurement as Closure Participation

English:

> Measurement is a physical process that participates in counterfactual closure by coupling an accessible domain to a stabilizing record channel.

中文：

> 测量是一个物理过程：它通过把可接入域耦合到稳定记录通道，参与反事实关闭。

Guardrail:

Do not imply consciousness causes collapse. Apparatus, environment, record media, and thermal reservoirs can be closure-participating interfaces.

Suggested future target:

May remain inside P06 and cross-link to E01.

### P15. Boundary as Permeability Profile

English:

> A physical boundary is a permeability profile governing which counterfactual degrees of freedom can cross into a stabilizing record channel.

中文：

> 物理边界是一种通透性轮廓，决定哪些反事实自由度可以进入稳定记录通道。

Guardrail:

Do not reduce all boundaries to observer choice. Boundaries may be physical, instrumental, causal, thermal, informational, or horizon-like.

Suggested future target:

`Physics/patches/SRT_Phys_P07_Closure_Ontology_of_Physical_Objects_v0_1.md`

or

`Physics/patches/SRT_Phys_P09_Gravity_Causal_Accessibility_Horizon_Boundaries_v0_1.md`

### P16. Energy as Closure-Payment Currency

English:

> Energy is not identical to Psi_f; it is one physical currency through which counterfactual-closure costs are paid in a given projection.

中文：

> 能量不等于 `Psi_f`；能量是在特定物理投影中支付反事实关闭成本的一种媒介。

Guardrail:

Do not introduce `Psi_f` as a new energy field. Keep canonical `Psi_f` broader than physical energy.

Suggested future target:

May remain inside P06 and cross-link to E03.

### P17. Symmetry as Residual Freedom After Closure

English:

> Symmetry is the residual transformation freedom that remains after counterfactual closure has stabilized an invariant kernel.

中文：

> 对称性是反事实关闭稳定出不变量核之后仍保留的变换自由。

Guardrail:

Do not claim SRT derives Noether's theorem. Say SRT gives a closure-theoretic reading of why invariant structure and admissible transformation belong together.

Suggested future target:

`Physics/patches/SRT_Phys_P08_Closure_Dynamics_and_Physical_Law_v0_1.md`

### P18. Locality as Closure-Propagation Bandwidth Constraint

English:

> Locality is the constraint that counterfactual-closure influence cannot generate controllable low-friction readout outside the admissible causal-access structure.

中文：

> 局域性是这样一种约束：反事实关闭影响不能在允许的因果接入结构之外生成可控的低摩擦读出。

Guardrail:

Do not claim SRT enables superluminal signalling. Do not claim SRT derives Bell violation. Respect no-signalling.

Suggested future target:

`Physics/patches/SRT_Phys_P08_Closure_Dynamics_and_Physical_Law_v0_1.md`

### P19. Path Integral as Pre-Closure Counterfactual Weighting

English:

> In the physical projection, path-integral language can be read as a counterfactual weighting scheme over candidate histories prior to closure, not as proof that all histories are ontologically actual.

中文：

> 在物理投影中，路径积分语言可被读作关闭前候选历史的反事实权重结构，而不是证明所有历史都已实际存在。

Guardrail:

Do not treat path integral as direct ontology. It is a formal / computational projection.

Suggested future target:

`Physics/patches/SRT_Phys_P08_Closure_Dynamics_and_Physical_Law_v0_1.md`

### P20. Entropy Increase as Loss of Reversible Counterfactual Access

English:

> Entropy increase can be read, under the SRT bridge, as the reduction of practically reversible access to pre-closure counterfactual configurations.

中文：

> 在 SRT 桥接读法中，熵增可被理解为对关闭前反事实构型的实际可逆接入减少。

Guardrail:

Do not replace thermodynamic entropy definitions. This is an SRT bridge interpretation compatible with E03.

Suggested future target:

`Physics/patches/SRT_Phys_P08_Closure_Dynamics_and_Physical_Law_v0_1.md`

### P21. Vacuum as Untriggered Accessible Excitation Baseline

English:

> Vacuum, under an SRT bridge reading, is not nothingness but a stable baseline in which accessible excitations remain unclosed into particular records.

中文：

> 真空不是无，而是一个稳定基线；其中可接入激发尚未关闭为特定记录。

Guardrail:

Do not identify `L0` with vacuum fluctuations. Vacuum fluctuations may be one physical analogy for accessible unclosed degrees, not `L0` itself.

Suggested future target:

`Physics/patches/SRT_Phys_P07_Closure_Ontology_of_Physical_Objects_v0_1.md`

### P22. Particle as Repeatable Closure Mode

English:

> A particle is a repeatable closure mode: an invariant pattern by which accessible field degrees of freedom stabilize into recognizable records.

中文：

> 粒子是一种可重复关闭模式：可接入场自由度按某种不变量模式稳定为可识别记录。

Guardrail:

Do not say particles are illusions or conscious concerns. Prefer "stable closure phenotype of field / invariant structure."

Suggested future target:

`Physics/patches/SRT_Phys_P07_Closure_Ontology_of_Physical_Objects_v0_1.md`

### P23. Physical Laws as Grammar of Admissible Closure

English:

> Physical laws are not external commands imposed on events; they are the invariant grammar specifying which counterfactual closures are admissible, repeatable, and stably readable.

中文：

> 物理定律不是外部强加给事件的命令，而是不变量语法：它规定哪些反事实关闭是可允许、可重复、可稳定读出的。

Guardrail:

Do not claim SRT replaces existing physical laws. It provides a meta-ontological reading of lawhood as admissible closure grammar.

Suggested future target:

`Physics/patches/SRT_Phys_P08_Closure_Dynamics_and_Physical_Law_v0_1.md`

## 15. Suggested decomposition after P06

P06 should not expand indefinitely. P9-P23 are better decomposed into three future patches once the bridge object stabilizes.

### P07 Closure Ontology of Physical Objects

- P10 objects as record bundles
- P13 noise as unresolved counterfactuality
- P14 measurement as closure participation
- P15 boundary as permeability profile
- P21 vacuum as untriggered accessible excitation baseline
- P22 particle as repeatable closure mode

### P08 Closure Dynamics and Physical Law

- P9 causality as counterfactual-constraint propagation
- P11 scale as closure depth
- P12 phase transition as closure-protocol restructuring
- P17 symmetry as residual freedom after closure
- P18 locality as closure-propagation bandwidth constraint
- P19 path integral as pre-closure weighting
- P20 entropy increase as loss of reversible counterfactual access
- P23 laws as grammar of admissible closure

### P09 Gravity / Causal Accessibility / Horizon Boundaries

- gravity reshapes physically accessible domain
- P15 boundary as permeability profile, especially horizon-like boundaries
- causal reachability, clock relations, path availability
- no Einstein tensor derivation unless separately adjudicated

## 16. Forbidden overclaims

- P06 does not solve the measurement problem.
- P06 does not derive Born rule.
- P06 does not prove collapse.
- P06 does not refute MWI.
- P06 does not derive GR.
- P06 does not define gravity as Psi_f.
- P06 does not write G_{\mu\nu} ∝ Psi_f.
- P06 does not derive physical constants.
- P06 does not derive Bell inequalities or Bell violations.
- P06 does not permit superluminal signalling.
- P06 does not identify d-value with entanglement entropy.
- P06 does not claim particles have concern.
- P06 does not replace thermodynamics, QFT, GR, or quantum information theory.
- P06 does not redefine canonical Psi_f, d-value, L0/L1/L2, or G_hat_theta.

## 17. One-paragraph abstract

**English abstract.** P06 introduces accessible counterfactual closure as a non-canonical bridge object for SRT physics. It defines `L0_accessible^phys(theta,t)` as the subset of `pi_phys(L0)` that remains actually enterable under current `theta`, current `t`, `L2` constraints, and `Psi_f` payability; defines `Psi_f^phys` as a physical projection of anchoring and stabilization burden; treats fact formation as an irreversible record that closes future counterfactual access; reads objectivity as low marginal readout friction after historical stabilization; keeps `d_phys` as a physical projection of d-value rather than a new d-definition; says gravity reshapes physically accessible domain without identifying gravity with `Psi_f`; treats Bell results as a caution against projecting `L1/L2` local-object intuition back into `L0`; and gathers P9-P23 as candidate future hardening lines for causality, objects, scale, phase transition, noise, measurement, boundary, energy, symmetry, locality, path integrals, entropy, vacuum, particles, and laws. It remains bridge / pressure-test material only.

**中文摘要。** P06 将 SRT 物理方向压缩为一个非 canonical 的桥接对象：`L0_accessible^phys(θ,t)` 是 `L0` 经 `π_phys` 投影后，在当前 `θ`、当前 `t`、`L2` 稳定约束与 `Psi_f` 可支付条件下仍可实际进入的候选域；`Psi_f^phys` 是锚定与记录稳定负担的物理投影；物理事实是不可逆记录对未来反事实空间的关闭；客观性是历史稳定成本沉积后形成的低边际读出摩擦；`d_phys` 只是 d-value 的物理投影；引力重塑物理可接入域而不等同于 `Psi_f`；Bell 结果说明 `L1/L2` 局域对象直觉不能直接投射到 `L0`；P9-P23 则作为因果、对象、尺度、相变、噪声、测量、边界、能量、对称性、局域性、路径积分、熵、真空、粒子与物理定律的后续物理硬化子命题。本文只属于 bridge / pressure-test，不修改 canonical primitives。
