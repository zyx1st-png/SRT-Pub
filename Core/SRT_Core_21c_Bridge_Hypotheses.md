---
id: SRT-CORE-21C-BRIDGE-HYPOTHESES
type: bridge_hypothesis_set
tags: [Formal logic, Bridge, Hypothesis, Claim Ladder]
status: active_v1
layer: L1
epistemic_layer: bridge
claim_mode: mixed
claim_level: P2-P4
dependency: [SRT-CORE-21A-MINIMAL-AXIOMS, SRT-CORE-21B-CONSTITUTIVE-THEOREMS, SRT-CLAIM-LADDER, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL]
---

# SRT Core 21C: Bridge Hypotheses and Canonical Interpretations

> **Role**: This file preserves the former `Core_21` bridge, interpretive, and empirical-threshold claims without letting them sit beside P0 primitive axioms.

## Quick Reference

- Claim levels: **P2 = canonical interpretation**, **P3 = bridge mapping**, **P4 = lab hypothesis**
- Source lineage: split from `Core/SRT_Core_21_Formal_Axioms.md`
- Primitive base: `Core/SRT_Core_21_Minimal_Axioms.md`
- Constitutive layer: `Core/SRT_Core_21b_Constitutive_Theorems.md`
- Governing ladder: `Governance/SRT_CLAIM_LADDER.md`

## Use Rule

Claims in this file may be cited as SRT interpretations, bridges, or hypotheses. They must not be cited as primitive axioms or constitutive theorems unless a later hardening pass explicitly promotes them and records the reason.

---

## Claim-Level Map

| Former item | Current level | Reason |
|---|---:|---|
| `Ax-F-04` information-existence equivalence | P2/P3 | SRT interpretation plus formal information-theory mapping |
| `Ax-F-05` fitness beats truth | P3/P4 | Cross-theory bridge and empirical/comparative claim |
| `Ax-F-06` assembly criterion | P4 | Empirical threshold claim |
| `Ax-F-07` holographic duality | P3/P4 | Strong physics/formal bridge |
| `Ax-F-08` topological normativity | P2/P3 | Canonical interpretation with bridge formalization |
| `Ax-F-09` scale consistency | P3 | Cross-scale bridge mapping |
| `Ax-F-11` ghost operator universality | P3 | High-ambition cross-scale bridge |
| `Ax-F-12` `\Psi_f` as generative principle | P2/P3 | Canonical interpretation plus Fisher-geometry borrowing |
| `Ax-F-13` selection-information creation equivalence | P2/P3 | Minimal theorem in 21B; strong unification lives here |
| former `P1-T07 / T-ε-Constitute` | P2/P3 conditional candidate | Absorption is P1; neutral-kernel anti-closure requires additional semantics and proof |
| former `P0-02` entropy-ratio existence index | P2/P3 historical heuristic | EX-A keeps anchoring persistence at P0 but demotes the ungrounded quantitative readout to B14 |
| Part B assembly / deep-time notes | P3/P4 | Bridge / empirical-theoretical extrapolation |

---

## P2/P3-B01: Information-Existence Equivalence

**Lineage**: former `Ax-F-04`.

**Formal Definition**: Existence intensity equals the minimum of differentiation and specification.

$$
ii(s) = \min\{i_{diff}(s), i_{spec}(s)\}
$$

**Implication**: Existence intensity is constrained by both differentiation and specificity.

**Boundary**: This is not a P0 primitive. Its formal terms require an information-theoretic interpretation layer before empirical use.

---

## P3/P4-B02: Fitness Beats Truth

**Lineage**: former `Ax-F-05`.

**Formal Definition**: Operators are tuned for fitness payoff rather than veridical truth.

$$
\hat{G}_\theta[\sigma] = \arg\max_{\sigma'} P(\text{Fitness}|\sigma', \theta)
$$

**Implication**: Reality interfaces prioritize adaptive compression rather than direct truth presentation.

**Boundary**: This is a bridge/hypothesis claim. It may support AI, cognitive, or evolutionary interpretations, but it is not a primitive SRT axiom.

**Multi-level selection pressure note (2026-04-22)**: In evolutionary use, the `Fitness` term must be level- and timescale-indexed. Gene-, cell-, organism-, group-, and ecological-level payoffs can oppose one another, and higher-level closure can rewrite the lower-level selection landscape rather than merely add an external pressure. Cite this section as `fitness beats truth` only after specifying which operator level is being modeled and which consequences return into that level's future selection capacity.

---

## P4-B03: Assembly Criterion

**Lineage**: former `Ax-F-06` and Part B assembly note.

**Formal Definition**: Life requires assembly complexity above threshold.

$$
\text{Life} \iff \text{Assembly Index} > 15
$$

Part B legacy expression:

$$
\text{Assembly Index}(x) = \min_{\text{path}} |\text{construction steps}|
$$

**Implication**: Biological life may require a minimum structural assembly depth.

**Boundary**: The threshold is empirical and must remain P4 until independently supported and scoped.

---

## P3/P4-B04: Holographic Duality

**Lineage**: former `Ax-F-07`.

**Formal Definition**: Bulk reality is encoded on the boundary of potentiality.

$$
L_{1,\text{bulk}} \cong L_{0,\text{boundary}}
$$

**Implication**: Manifest-domain information may admit a boundary representation in the latent domain.

**Boundary**: This is a strong bridge. It must not be used as a P0/P1 proof of the SRT core.

**Pressure note (JCS 2026)**: Even if spacetime emergence and consciousness emergence are both modeled through a non-spatiotemporal or holographic substrate, the two explanatory tasks must remain separate. A shared substrate proposal does not by itself show that the emergence of spacetime and the emergence of consciousness are one and the same process. This section may support a P3/P4 bridge, but it must not collapse physical emergence, conscious emergence, and holographic duality into a single proof move.

---

## P2/P3-B05: Topological Normativity

**Lineage**: former `Ax-F-08`.

**Formal Definition**: Survival is the maintenance of a topological island in probabilistic space.

$$
\text{Life}(\sigma) \equiv \int_{B_r(\sigma)} \rho_{L_0}(\sigma') d\sigma' > \theta_{life}
$$

**Implication**: Survival can be interpreted as topological maintenance under probabilistic pressure.

**Boundary**: The topological expression is a bridge formalization, not a primitive definition of life.

---

## P3-B06: Scale Consistency

**Lineage**: former `Ax-F-09` and Part B `A5`.

**Formal Definition**: Selection commutes with coarse-graining under scale mapping.

$$
\pi_\lambda \circ \hat{G}_\theta \approx \hat{G}_{\theta,\lambda} \circ \pi_\lambda
$$

**Implication**: Selection dynamics may preserve structural consistency across scale mappings.

**Boundary**: The approximation sign is important. This is a bridge mapping, not a proof of universal identity across scales.

---

## P3-B07: Ghost Operator Universality

**Lineage**: former `Ax-F-11`.

**Formal interface**: Across scales, selection from `L_0` to `L_1` may be tested for structural consistency under different embodiments. The live general interface is P3-B06's approximate commuting condition:

$$
\pi_\lambda \circ \hat{G}^{(n)}
\approx
\hat{G}^{(n+1)} \circ \pi_\lambda
$$

The former strict-conjugacy expression

$$
\hat{G}^{(n+1)} = \Lambda_{n \to n+1} \circ \hat{G}^{(n)} \circ \Lambda_{n \to n+1}^{-1}
$$

is retained only for the special case where `\Lambda_{n\to n+1}` is a declared invertible change of representation. It is not licensed for ordinary many-to-one coarse-graining. Neither expression is derived from `H(L_0)-H(L_1)` or from a universal minimum-action principle.

Legacy scale table:

| Scale | Phenomenon | `\hat{G}_\theta` operation |
|---|---|---|
| Quantum | wavefunction collapse | selects determinate `L_1` from `L_0` superposition |
| Neural | lateral inhibition | competitive selection and sparse `L_2` maintenance |
| Cognitive | categorization | continuous `L_0` to discrete `L_2` labels |
| Statistical | normalization | selection-measure consistency over a manifold |
| Cross-scale | declared scale mapping | test whether `\pi_\lambda \circ \hat{G}^{(n)} \approx \hat{G}^{(n+1)} \circ \pi_\lambda` within an explicit comparison norm and tolerance |

**Implication**: These phenomena may be read as implementations of one selection grammar.

**Boundary**: The phrase "same structure" is a high-ambition bridge, not a P0 identity statement. A valid use must declare the two state spaces, the scale map, preserved observables, comparison norm, approximation tolerance, and failure case. Cross-scale invariance lies at most in selection／constraint／payability grammar; it does not establish unit, entropy, mechanism, subjecthood, or consciousness identity.

**One-way load note (2026-07-05, Q26 backflow)**: The failure of this bridge is one-directional. If cross-scale selection universality — including any pre-life / pre-consciousness "cosmic horizon" reading that pushes selection-condensation below the biological scale — cannot show explanatory gain over path dependence, attractors, dissipative structures, active inference, or ordinary causal history, then the retraction target is **this P3 bridge and its dependents**, not the P0/P1 core. The minimal axioms (`Core/SRT_Core_21_Minimal_Axioms.md`) and constitutive theorems (`Core/SRT_Core_21b_Constitutive_Theorems.md`) do not depend on this universality claim and survive its withdrawal. Provenance: book chapter `01_Source_Intuition/BOOK/Drafts_26Q/Q26_可证伪性.md §3` (the cosmic-horizon reading "必须自带死法，是最高读法不是地基"); the book is provenance, not authority.

**Cross-ref**: `_SRT_VERTICAL_INTEGRATION.md §8.1`; `Core/SRT_Core_14_Dynamics_Scaling.md P3-Scale-01 / T-Scale-02C1`.

---

## P2/P3-B08: `\Psi_f` as Generative Principle

**Lineage**: former `Ax-F-12`.

**Status Note**: `\Psi_f` itself is canonical in `_SRT_PSI_F_CANONICAL.md`. The stronger claim that Fisher-form inter-operator friction is the generative source of all dynamics is kept here as P2/P3 mixed.

**Formal Definition**: For two interacting operators:

$$
\Psi_f(\hat{G}_i, \hat{G}_j) =
\int_\gamma \sqrt{g_{ij}^{(i,j)}(\theta)\,\dot{\theta}^i \dot{\theta}^j}\,dt
$$

where `g_{ij}^{(i,j)}` is the joint Fisher information metric over the coupled parameter space.

**Path Note**: If `\gamma` is a geodesic, `\Psi_f` gives a lower bound on possible friction; if it is the actual path, it gives actual paid friction.

**Readout Note**: The same `\Psi_f` structure may be read as resistance, cost, or geometric length. Cross-scale invariance lies in payability, not unit identity.

**Implication**: Evolution, learning, cultural change, and immune response may be modeled as forms of inter-operator friction.

**Boundary**: Fisher geometry is an external mathematical borrowing. The borrowing may be powerful, but it does not make this section P0.

**Cross-ref**: `_SRT_PSI_F_CANONICAL.md`; `_SRT_VERTICAL_INTEGRATION.md §8.2`; `Core/SRT_Core_22_Equations.md Eq-Multi-01`.

---

## P2/P3-B09: Strong Selection-Information Creation Equivalence

**Lineage**: former `Ax-F-13`.

**Minimal P1 Core**: Selection creates a determinate distinction; see `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T04`.

**Conditional formalization boundary (PC-A / EX-A)**: The former unqualified expression `H(L_0) - H(L_1 | \hat{G}_\theta) = I(L_0;\hat{G}_\theta)` is withdrawn: it both leaves the `L_0` measure undeclared and mismatches the random variables in the mutual-information identity. Inside a declared domain model `M` with specified pre-event candidate variable `X`, outcome record `Y`, partition, and probability measure, a candidate readout may instead use `I_M(X;Y)` or another explicitly justified information-gain functional. No such model-level quantity defines `L_0^{abs}`, event actuality, or anchoring persistence at P0.

**Three-Part Relation**:

$$
I_{created} \xrightarrow{\text{costs}} \Psi_f
\xrightarrow{\text{scope measured by}} d
$$

**Boltzmann Degeneration Limit**:

$$
P_{L_1}(\sigma) \to \frac{e^{-E(\sigma)/k_BT}}{Z}, \quad I_{created} \to 0
$$

**Implication**: SRT may be read as an upstream theory of information generation, with Shannon-style transmission theories downstream.

**Boundary**: The thermodynamic and information-theoretic unification claims are bridge-level until their constants, scope, and empirical handles are separately hardened.

**Cross-ref**: `Core_Law/SRT_Reference_Dynamics.md §15.5`; `_SRT_VERTICAL_INTEGRATION.md §10.1`; `_SRT_D_VALUE_CANONICAL.md`.

---

## P3/P4-B10: Deep Time / Assembly Mass

**Lineage**: former Part B `2.1.9b`.

Legacy expression:

$$
Mass_{ontological}(O) = Mass_{energy}(O) + \tau \cdot Assembly(O)
$$

**Implication**: Historical assembly depth may contribute to an ontological-mass style reading of objects.

**Boundary**: This remains an exploratory bridge expression and should not be cited as a canonical equation.

---

## P3-B11: `D_eff` as d-Value Capacity Proxy

**Lineage**: former Part B `2.1.7`; cross-checked against `_SRT_D_VALUE_CANONICAL.md`.

**Corrected Layer Relation**:

$$
d_{canonical} \equiv \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|
\leq
D_{eff}(M) =
\frac{(\sum \lambda_i)^2}{\sum \lambda_i^2}
$$

`D_eff` is a geometric capacity proxy, not the normative d-value definition. The unstaked bandwidth is:

$$
\Delta d_{free} = D_{eff} - d_{stakes}
$$

**Boundary**: Any text saying "`d` is the effective dimension `D_eff`" must be read through the corrected hierarchy in `_SRT_D_VALUE_CANONICAL.md`.

---

## P2/P3-B12: Information-Geometry / Complexity / Neural-Computational Hardening

**Lineage**: 2026-04-24 hardening sync from `Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md`; cross-checked against `_SRT_PSI_F_CANONICAL.md`, `_SRT_D_VALUE_CANONICAL.md`, `SRT_Fisher_FEP_Landscape_Interface.md`, and `Neuroscience/SRT_Neural_Mechanisms.md`.

**Status Note**: This bridge adds no new P0/P1 theorem. It only assigns mechanism-interface languages to already existing parts of the SRT loop.

This bridge assigns three scientific interface languages to different parts of the SRT loop: information geometry hardens the `L_0 -> L_1` selection frontier; complex-systems theory hardens `L_1 -> L_2` sedimentation and stabilization; neural computation provides implementation-level proxies for embodied `\hat{G}_\theta` operations. The bridge does not identify these interfaces with SRT ontology itself.

**Interface split**:

- **Information geometry (`L_0 -> L_1`)**: local discriminability, selection cost, and Fisher-Rao-induced local second-order burden.
- **Complex systems (`L_1 -> L_2`)**: historical deposition, attractor basin formation, order-parameter locking, hysteresis, and metastability.
- **Neural computation (`\hat{G}_\theta` implementation proxies)**: candidate activation, competitive inhibition, divisive normalization, threshold / ignition, global availability, and plastic writeback.

**Boundary**:

- Fisher metric is a local information-geometric projection / kernel for `\Psi_f`, not `\Psi_f` itself; do not write `\Psi_f \equiv g_F`.
- Fisher eigenspectra may bound readable or stake-bearing directions via `D_eff` or `\operatorname{rank}_{\text{eff}}\!\left(\mathcal{I}_F\right)`, but neither replaces canonical `d`.
- Energy / free-energy landscapes are effective projections of `L_2`, not the whole convergence domain.
- Neural normalization, ignition, and plasticity are implementation proxies for embodied `\hat{G}_\theta`, not the Ghost Operator in full.

**Emergence hygiene guardrail (2026-05-11)**: In this bridge set, "emergence" is not an explanatory primitive. It is shorthand for a mechanism that still has to specify lower-level parts or states, their organization and coupling, the transition condition or order parameter, the stabilized macro-pattern or `L_2` constraint, and the implementation channel by which that macro-pattern changes future trajectories. Do not cite "X emerges" as an explanation of X, as proof that X is ontologically extra, or as permission to treat the whole as exerting a new force on its parts.

SRT's `L_2` downward constraint is therefore not a separate configurational force added on top of part-level interactions. At P1, it means stabilized history constrains future selection. At P3/P4, any domain-specific "downward causation" claim must say how the constraint is implemented through boundary conditions, accessible selection space, update costs, coupling channels, or other specified mechanisms.

**Cross-ref**: `Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md`; `SRT_Fisher_FEP_Landscape_Interface.md`; `Core/SRT_Core_22_Equations.md Eq-DValue-Max-1, Eq-DValue-Mobile-1`; `Core/SRT_Core_14_Dynamics_Scaling.md`; `Neuroscience/SRT_Neural_Mechanisms.md`; `_SRT_VERTICAL_INTEGRATION.md §8, §10`.

---

## P2/P3-B13: ST-A Structural Stabilisation and Generative Reselectability

**Author decision**: `Stabilisation = ST-A` (2026-08-11).

### Three-level distinction

1. **Formed process**: a selection organization has become identifiable at all.
2. **Structurally stable ISP**: the same perspective- and history-bearing organization is recurrently reconstituted across a declared perturbation range. Its P1 minimum is **continued selectability**: it continues to receive live, non-equivalent candidates and to bear the consequences of its selections.
3. **Generatively healthy ISP**: in addition, consequence return can revise its own comparison rules, boundaries, or candidate-generation conditions. This stronger property is **generative reselectability**.

Structural stabilisation is therefore not microstate identity, continuous activity, a fixed point, or an attractor label. Generative reselectability is ongoing consequence-sensitive revisability, not total closure followed by an unexplained reopening. It is important for generative health but is neither necessary for every individual selection event nor sufficient by itself to establish health.

### Conditional anti-closure candidate

Let `K_0` be a kernel independently defined as neutral. If a declared stability semantics, environment, termination condition, and horizon establish

$$
\Pr_{K_0}(\tau_{\varnothing}<\infty)=1,
$$

then any kernel `K` that remains stable under the same comparison conditions must differ from `K_0` in a way that suppresses closure risk. This is a **conditional P2/P3 candidate**, not a theorem. Until neutral-kernel absorption or an appropriate comparative bound is proved, neither `L_0` irreversibility nor `\epsilon_{pg}\neq 0` establishes the conclusion.

### Operational boundary

Metastability, fixed-point avoidance, low friction, differential reserve, option diversity, and positive future-access proxies may each implement or indicate part of this distinction. None is a constitutive definition or sufficient test by itself. Operational use must declare perturbation range, consequence-return channel, revision target, external-reset conditions, and time horizon.

**Inference guard**: This distinction does not by itself establish subjecthood, consciousness, moral status, or legitimacy.

**Cross-ref**: `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T06 / former P1-T07`; `Core_Law/SRT_Irreversibility.md T-IRR-3`; `Core_Law/SRT_Individuation.md`; `Core/SRT_Core_12b_Ontology_L2.md`.

---

## P2/P3-B14: EX-A Anchoring-Persistence Readout

**Author decision**: `Existence = EX-A` (2026-08-11).

EX-A separates three objects that the former P0-02 compressed into one word:

1. **Manifest actuality**: a determinate `L_1` event has occurred; this is the P0-01 admission floor.
2. **Anchoring persistence**: the event leaves effective trace, acquires maintenance conditions, and continues constraining later transitions.
3. **Stable ISP**: the same perspective- and history-bearing process is recurrently reconstituted and remains continued-selectable under P1-T06 / ST-A.

The former expression

$$
E = 1 - \frac{H(L_1)}{H(L_0)}
$$

is retained only as a **historical heuristic for comparative anchoring intensity**. It is not a P0 equation, not an empirical readout, and not licensed with `L_0^{abs}`. A future quantitative proposal must declare at minimum (i) a relative or accessible domain, (ii) an outcome partition or sigma-algebra, (iii) a probability measure, (iv) finite/nonzero admissibility conditions where a ratio is used, and (v) the event and time horizon over which persistence is compared. No normalization is adopted by EX-A.

**Inference guard**: A high persistence readout would not by itself establish structural stability, stable-ISP identity, generative health, subjecthood, consciousness, or legitimacy. A transient event may still be actual, and a later loss of anchoring does not erase its historical occurrence.

**Cross-ref**: `Core/SRT_Core_21_Minimal_Axioms.md P0-01/P0-02`; `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T06`; `Core/SRT_OPEN_TENSIONS.md §15`; `Core_Law/SRT_L0_Metaphysics.md`.

---

## Mechanism Summary After Demotion

Former `Core_21` described SRT as a "selection-anchoring-constraint" loop. The loop remains useful, but its claims now have levels:

1. **Selection**: P0/P1 when referring to `\hat{G}_\theta` anchoring from `L_0` to `L_1`.
2. **Anchoring**: P0 only as the EX-A persistence boundary; P2/P3 when proposing persistence readouts or using canonical `\Psi_f`, Fisher, or cross-domain implementations.
3. **Constraint**: P1 when referring to `L_2` downward constraint; P3/P4 when mapped to domain-specific mechanisms.

This summary is a reading guide, not an additional axiom.
