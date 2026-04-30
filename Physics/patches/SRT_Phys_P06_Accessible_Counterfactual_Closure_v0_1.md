---
id: SRT-PHYS-P06-ACCESSIBLE-COUNTERFACTUAL-CLOSURE
type: hardening_patch
tags: [Physics, Counterfactual Closure, Accessibility, Record Stabilization, Objectivity, Time, Gravity, d-value, Psi_f, Bridge]
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
  closure as a unifying bridge concept for SRT physics. Reframes physical
  manifestation as selection from L0_accessible rather than L0_total, fact
  formation as irreversible future-constraint, Psi_f as counterfactual-closure
  cost in bridge projection, objectivity as low marginal readout friction,
  time as closure ordering, gravity as accessible-domain reshaping, and d_phys
  as future-consequence bandwidth. Bridge layer only; does not define new
  physical law or modify canonical SRT primitives.
---

# SRT Physics P06: Accessible Counterfactual Closure

> Status note:
> This is a non-canonical physics hardening patch. It does not claim new established physics. It does not solve the measurement problem, derive gravity, derive constants, or redefine canonical Psi_f / d-value / L0-L1-L2 / G_hat_theta. It gives SRT physics a sharper bridge-level research object: accessible counterfactual closure.

## 0. Motivation: why this patch is needed

The current physics-facing path has become much sharper through E01-E05. E01 gives `G_hat_theta` a quantum-instrument bridge; E02 gives `theta_boundary` a quantum-reference-frame projection; E03 gives the physical projection of `Psi_f` a scoped information-thermodynamic proxy; E04 gives manifest time a relational clock bridge; E05 turns the physics layer into a Lakatos-style research programme with explicit falsification windows.

Even after that work, one weakness remains: much of the physics layer can still sound like SRT renaming existing physics. "Measurement as selection" is useful, but it stays too close to collapse language, and collapse language immediately inherits interpretation pressure from Copenhagen, Everett, QRF, and relational readings.

The deeper SRT-facing question is not:

```text
How does possibility become an outcome?
```

The better bridge question is:

```text
How does an accessible physical possibility become an irreversible future-constraining fact?
```

P06 does not replace E01-E05. It gives them an upper-level bridge object: **accessible counterfactual closure**. E01-E05 remain the formal homes and falsifiability scaffolds; P06 names the common thing they are all circling.

## 1. Core thesis

Reality is not merely possibility becoming outcome.

Reality is **accessible counterfactual closure stabilized into low-friction readout structure**.

中文核心句：

> 现实 = 可接入反事实空间的关闭，并稳定为低摩擦读出的结构。

This means:

1. The total latent domain is first cut down by boundaries, reference frames, reservoirs, causal geometry, and history into an accessible latent domain.
2. The accessible counterfactual space is closed through an irreversible record.
3. The record sediments through redundancy, stability, and low marginal readout friction into objective structure.

Overall bridge diagram:

```text
L0_total
  -> accessibility filtering by theta / boundary / reservoir / causal geometry / history
L0_accessible
  -> counterfactual closure with Psi_f cost
L1_record
  -> redundancy / stabilization / low marginal readout friction
L2_phys
```

This is a bridge projection, not a new physical law. It reframes the physics programme around the gap between total possibility and accessible possibility, then around the cost of closing accessible alternatives into durable records.

## 2. P06-1 Accessible Latent Domain

Bridge-local definition:

```text
L0_accessible(theta, boundary, reservoir, history) subset L0_total
```

Physical manifestation does not select from total possibility space. It selects from an access-limited subdomain.

`L0_total` must not be identified with Hilbert space itself. Hilbert space, path integral configuration space, phase space, moduli space, or any other physics formalism is a physical-domain projection. `L0_accessible` is a bridge-level SRT term for the candidate space that a real system can operationally access under a given `theta`, physical boundary, reservoir, causal geometry, and history.

This matters because the real object of physics-side selection is not unconstrained totality. It is the access-filtered domain:

```text
candidate manifestation = selection from L0_accessible, not from L0_total
```

Connections to existing files:

| Existing bridge | P06 reading |
|---|---|
| E01 quantum instrument | instrument choice restricts accessible outcome channels |
| E02 QRF | QRF / `theta_boundary` restricts frame-relative accessibility |
| E04 relational time | clock choice restricts manifest temporal accessibility |

The bridge object is therefore not "collapse" first. It is accessibility first, then closure.

## 3. P06-2 Fact Formation

Bridge-local definition:

```text
An L1 physical fact is not merely an outcome.
It is an outcome whose future counterfactual space has been constrained by an irreversible record.
```

中文：

> 一个 L1 物理事实不是单纯结果，而是一个通过不可逆记录压缩了后续反事实空间的结果。

Formula placeholder:

```text
fact_L1 = outcome + irreversible_future_constraint
```

This turns the physics-facing SRT question away from a collapse problem and toward a fact formation problem.

The useful distinction is:

| Term | P06 bridge reading |
|---|---|
| outcome | a realized value or state in a given access domain |
| record | the stabilized trace that makes the outcome matter for later dynamics |
| fact | an outcome whose record constrains future accessible counterfactuals |

Guardrails:

- Do not say P06 solves quantum measurement.
- Do not say every measurement globally collapses the wavefunction.
- Do not say `L1` is merely subjective observation.

In Everett-compatible language, P06 can be read as branch-relative fact formation: the relevant closure is relative to a record-bearing branch / frame / subsystem, not a global collapse event.

## 4. P06-3 Psi_f as Counterfactual Closure Cost

Bridge-local definition:

```text
Psi_f is the cost of closing accessible counterfactuals into a stabilized record.
```

Bridge formula:

```text
Psi_f_event ~ Cost[L0_accessible before event -> L1_record after event]
```

The `~` marks a bridge-level monotone / structural relation, not strict equality. Canonical `Psi_f` remains in `_SRT_PSI_F_CANONICAL.md`.

In P06, `Psi_f` is not ordinary energy. It names the payability burden of making other still-accessible counterfactuals no longer operationally available. Under different physical projections, that burden may appear as:

- record stabilization burden;
- dissipation or entropy-production proxy;
- Fisher distinguishability / information-geometric path cost;
- apparatus calibration burden;
- reference-frame maintenance cost;
- dilation-environment support cost.

E03's `sigma_f^phys` remains one physical proxy in record-stabilization / dissipative regimes. It is not an identity with canonical `Psi_f`, and it does not exhaust the closure-cost concept.

Forbidden reductions:

- Do not identify `Psi_f` with raw entropy.
- Do not identify `Psi_f` with raw Fisher information.
- Do not identify `Psi_f` with Landauer cost.
- Do not identify `Psi_f` with thermodynamic free energy.

The safe P06 expression is:

```text
sigma_f^phys is a monotone proxy for one physical projection of closure cost.
```

## 5. P06-4 Time as Closure Order

Bridge-local definition:

```text
Manifest time is the ordering structure induced by irreversible counterfactual-closure events.
Clock time is the operational readout of this ordering under a chosen theta-clock.
```

Formula placeholder:

```text
t_order = partial order of irreversible counterfactual closures
```

This means time is not first an external background tick. In the P06 bridge, manifest physical time is the order in which accessible counterfactual domains become irreversibly narrowed by record-forming events. Physical clocks then provide an operational readout of this ordering under a chosen clock subsystem.

Boundary:

- Do not say physical time is Planck-discrete.
- H-Phys-2 remains a speculative alternative.
- E04 relational time remains the primary bridge.

P06 is structurally aligned with E04: a `theta`-chosen clock reads the closure order, but the closure order is not identical to any one clock variable.

## 6. P06-5 Objectivity as Low Marginal Readout Friction

Bridge-local definition:

```text
Objective physical reality is the regime where the marginal Psi_f required for additional readout approaches zero, while the original stabilization cost remains historically embedded.
```

中文：

> 客观物理现实是新增读出所需边际 Psi_f 趋近于零的状态；但初始稳定成本没有消失，而是沉积在 L2 结构中。

The key distinction:

```text
low marginal readout friction != zero object-maintenance friction
```

Relation:

```text
environmental redundancy -> lowers marginal readout friction
Quantum Darwinism -> candidate physical image of L2 redundancy
L2_phys -> low marginal readout regime
```

Quantum Darwinism is structurally aligned under a bridge projection: environmental redundancy can make many additional observers / apparatuses read the same record with very low extra cost. P06 does not claim mathematical identity between Quantum Darwinism and SRT.

In this sense, objectivity is not the absence of `Psi_f`; it is the historical embedding of paid stabilization cost into a record environment where further access becomes cheap.

## 7. P06-6 Physical L2 Kernel

Bridge-local definition:

```text
L2_phys is the invariant kernel preserved under all admissible theta-transformations.
A physical selection is legal only if it maps accessible possibilities into this invariant kernel.
```

中文：

> 物理 L2 是所有可允许 theta 转换下仍保持的不变量核；合法物理选择不能破坏这个核。

This avoids writing conservation laws as subjective consensus. Physical `L2` is not social agreement. It is the hard invariant kernel constraining what may count as a legal physical selection under admissible changes of frame, apparatus, and clock.

Safe formulation:

```text
Selection does not create conservation laws; selection is constrained by the L2_phys kernel.
```

P06 therefore preserves the Physics/Claim-Status boundary: conservation-law language remains a physics bridge image of `L2` invariance, not a claim that subjective observation invents physical law.

## 8. P06-7 Gravity as Accessible-Domain Reshaping

Bridge-local definition:

```text
In the physical projection, gravity does not equal Psi_f.
Gravity modifies the geometry of L0_accessible by constraining causal reachability, clock relations, and path availability.
```

中文：

> 在物理投影中，引力不等于 Psi_f；引力通过约束因果可达性、钟表关系与路径可用性，重塑 L0_accessible 的几何。

This is the safer version of the gravity / `Psi_f` interface. The dangerous move is to identify gravity with friction or to treat a scalar closure-cost intuition as a tensor-level field equation. P06 instead says:

```text
gravity reshapes the accessible counterfactual domain
```

Examples of reshaping under a physical projection:

- causal reachability changes;
- available paths change;
- clock relations change;
- horizon structure changes;
- record-access and signal-propagation constraints change.

Boundary:

- Do not write `G_mu_nu` proportional to `Psi_f` as a result.
- Do not claim a derivation of GR.
- H-Phys-4 remains weak compatibility / analogy unless tensor derivation is supplied.

The bridge keeps `Psi_f` and gravity related but not identical: gravity changes which counterfactuals are physically accessible; `Psi_f` tracks the payability / closure burden of stabilizing accessible alternatives into records.

## 9. P06-8 Physical d-value as Future-Consequence Bandwidth

Bridge-local definition:

```text
d_phys(event) measures the bandwidth of future counterfactual constraints imposed by an irreversible record.
```

中文：

> 物理 d-value 衡量一个不可逆记录对未来反事实空间施加约束的带宽。

Canonical d-value remains broader and is defined in `_SRT_D_VALUE_CANONICAL.md`. `d_phys` is only a bridge-local physical projection. It does not anthropomorphize particles, and it does not attribute concern, care, suffering, or consciousness to ordinary physical systems.

In P06:

```text
physical d is not consciousness
physical d is consequence bandwidth
```

Cross-layer reading:

| Layer | d-value reading |
|---|---|
| Physical | future-consequence bandwidth |
| Biological | viability-relevant constraint bandwidth |
| Conscious | concern / stake bandwidth |
| Social | institutional future-action constraint bandwidth |

This table is a bridge map. It does not redefine canonical `d`, and it does not collapse the physical projection into the conscious / concern-bearing reading.

## 10. Relation to E01-E05

| Existing file | P06 relation |
|---|---|
| E01 quantum instrument | P06 says instrument choice restricts `L0_accessible` and changes closure cost. |
| E02 QRF | P06 says `theta_boundary` changes the accessible counterfactual domain. |
| E03 information thermodynamics | P06 says `sigma_f^phys` is one proxy for counterfactual closure cost in record-stabilization regimes. |
| E04 relational time | P06 says manifest time is closure ordering read through a `theta`-clock. |
| E05 falsifiability | P06 proposes a candidate upper-level bridge object that may generate sharper future falsification windows. |

This relation is intentionally asymmetric. E01-E05 provide formal homes and tests; P06 supplies a conceptual upper bridge:

```text
accessibility -> closure -> record -> redundancy -> low-friction readout
```

## 11. Candidate falsification windows, but keep them conservative

The following are candidate bridge-level discriminators. None is an established prediction.

### Window A: residual stabilization cost under theta-realization changes

Two informationally equivalent record-stabilization processes with different `theta`-realizations may differ in residual stabilization cost.

This is a bridge-level candidate discriminator, not an established prediction.

Possible overlap:

- E01 dilation-environment selection;
- E02 frame-maintenance cost;
- E03 record-stabilization residual.

### Window B: accessible-boundary changes with preserved reduced dynamics

Changing accessible-domain boundaries while preserving reduced dynamics may alter calibration / stabilization burden.

This is a bridge-level candidate discriminator, not an established prediction.

Possible overlap:

- engineered-reservoir comparisons;
- QRF frame-role swaps;
- continuous-measurement unraveling tests.

### Window C: future-consequence bandwidth and redundancy burden

Events with larger future-consequence bandwidth `d_phys` may show larger stabilization / redundancy burden in carefully controlled record systems.

This is a bridge-level candidate discriminator, not an established prediction.

Possible overlap:

- E03 `d`-value scaling window;
- high-irreversibility record systems;
- redundant environmental encoding / Quantum-Darwinism-style platforms.

These windows should be treated as pressure-test prompts. They require future operational definitions before they can function as P4 lab hypotheses.

## 12. Forbidden overclaims

- P06 does not solve the measurement problem.
- P06 does not derive Born rule.
- P06 does not prove collapse.
- P06 does not refute MWI.
- P06 does not derive GR.
- P06 does not identify gravity with Psi_f.
- P06 does not derive physical constants.
- P06 does not identify d-value with entanglement entropy.
- P06 does not claim particles have concern.
- P06 does not redefine canonical Psi_f, d-value, L0/L1/L2, or G_hat_theta.

## 13. One-paragraph abstract

**English abstract.** Accessible counterfactual closure is a non-canonical bridge object for SRT physics: the physical layer is read as selection from `L0_accessible`, not from `L0_total`; fact formation is an irreversible record that constrains future counterfactuals; `Psi_f` is interpreted in bridge projection as closure cost rather than as raw entropy, energy, Fisher information, or free energy; objectivity is low marginal readout friction after historical record stabilization; time is closure order read through a chosen clock; gravity is accessible-domain reshaping rather than identity with `Psi_f`; and `d_phys` is future-consequence bandwidth rather than consciousness or concern. This patch gives E01-E05 a shared upper-level research object while preserving bridge status and leaving all canonical SRT primitives unchanged.

**中文摘要。** P06 将 SRT 物理方向压缩为一个非 canonical 的桥接对象：现实来自可接入潜域中的反事实关闭，而不是从总潜在域中无约束地产生；事实形成是通过不可逆记录压缩未来反事实空间；记录稳定之后，客观性表现为低边际读出摩擦；物理 L2 核是可允许 `theta` 转换下仍保持的不变量约束；时间是关闭事件的排序并由物理钟表读出；引力重塑可接入域，而不是等同于 `Psi_f`；物理 d-value 只是不可逆记录的后果带宽，不是意识、关切或主体性定义。该 patch 只提供 bridge-level pressure-test 对象，不修改 canonical `Psi_f`、d-value、`L0/L1/L2` 或 `G_hat_theta`。
