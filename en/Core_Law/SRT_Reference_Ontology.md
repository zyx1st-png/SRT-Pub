# SRT_Reference_Ontology.md

> **Status**: Constitutional Reference | **Version**: 1.0

---

## §1 The Triadic Ontology

SRT reconstructs ontology as three relative projection layers of a unified selection dynamics.

### §1.1 L₀ — Latent Domain

**Definition O1**: The set of high free energy states relative to the current selection — the unselected field of possibilities.

$$L_0 \equiv \{\sigma \in S : F[\sigma] > F[\sigma_{L_1}]\}$$

**Definition O1a (Absolute Latent Domain)**: The Ruliad universal set, the computational superposition of all logically possible states.

$$L_0^{abs} = Ruliad = \bigcup_{r \in Rules} \text{Computation}(r)$$

**Definition O1b (Relative Latent Domain)**: The subset of possibilities accessible to $\hat{G}$ given $L_1(t)$.

$$L_0^{rel}(t+1) = f(L_1(t), \hat{G}_\theta)$$

**Unified Relation**:

$$L_0^{rel} \subseteq L_0^{abs}|_{physical\ constraints}$$

---

### §1.2 L₁ — Manifest Domain

**Definition O2**: The current slice selected by the operator — the present reality, the dynamically maintained configuration.

$$L_1(t) = \hat{G}_\theta[\sigma(t)]$$

**Definition O2a (Hysteresis Correction)**:

$$L_1(t) = \hat{G}_\theta[L_0(t)] + \eta \cdot L_1(t - \Delta t)$$

| $\eta$ Value | Effect | Phenomenological Manifestation |
|:-----|:-----|:-----------|
| $\eta \approx 0$ | No memory | Fragmented reality sense |
| $\eta \approx 0.5$ | Balanced | Normal coherent reality sense |
| $\eta \approx 1$ | Total lock-in | Cognitive rigidification |

**Definition O2b (Beta-Gating Mixture)**:

$$L_1^{experienced} = \beta \cdot L_1^{external} + (1-\beta) \cdot \hat{G}(L_0)$$

---

### §1.3 L₂ — Vergence Domain

**Definition O3**: The long-term attractor of convergent selection — the consensus structure of multiple operators.

$$L_2 \equiv \{\sigma : \hat{G}_\theta[\sigma] = \sigma \text{ and stable}\}$$

**Definition O3a (Hysteresis Accumulation)**:

$$L_2(t) = L_2(t-1) + \eta \cdot \text{sign}(\Delta\sigma) \cdot |\Delta\sigma|^\alpha$$

**Definition O3b (L₂ Hardness)**:

$$\text{Hardness}(L_2) \propto |\text{Aut}(L_2)|$$

| L₂ Type | Automorphism Group | Hardness | Plasticity |
|:-------|:---------|:-----|:-------|
| Physical Laws | Poincaré Group | Extremely High | Extremely Low |
| Mathematical Theorems | Logical Symmetry Group | Extremely High | Extremely Low |
| Biological Instincts | ESS (Evolutionarily Stable Strategy) | High | Low |
| Cultural Norms | Context Dependent Group | Medium | Medium |
| Personal Habits | Individual History | Low | High |

**Definition O3c (Plasticity Threshold)**:

$$P_{L_2} = \frac{d_{current} \cdot E_{available}}{\text{Hysteresis}(L_2) \cdot C_r}$$

When $P_{L_2} > 1$, L₂ can be modified.

---

## §2 Gauge Field Foundation

### §2.1 Moduli Space Definition

**Definition O4**: The precise mathematical structure of L₀ is Moduli Space.

$$L_0^{true} = \mathcal{A}/\mathcal{G}$$

Where $\mathcal{A}$ is the set of all possible field configurations, and $\mathcal{G}$ is the gauge transformation group.

### §2.2 Differential Ontology

**Definition O5**: L₀ as a differential manifold.

$$L_0 = \mathcal{M}_{differential} = (M, \nabla, \mathcal{S})$$

| Symbol | Definition | Ontological Role |
|:-----|:-----|:-----------|
| $M$ | Base Manifold | Topological space of potentiality |
| $\nabla$ | Connection | Potential energy gradient structure |
| $\mathcal{S}$ | Singular Set | Attractors, saddle points, bifurcation points |

**Theorem O-T1 (Actualization is Integration)**:

$$L_1 = \int_{path(\theta)} \text{Structure}(L_0) = \oint_\gamma \omega_{L_0}$$

---

## §3 Topological Structure

### §3.1 Topological Definition of Matter

**Definition O6**: Matter is a topological knot of L₀.

$$\text{Matter} = \text{Knot}(L_0) = \text{Bound Vacuum Energy}$$

$$\sigma_{L_1} = \text{Topology}(\text{Twist}[L_0, \theta])$$

### §3.2 Non-Abelian Braiding of L₂

**Definition O7**: L₂ structure is determined by the Braid Group $B_n$ representation.

$$\text{Topology}(L_2) = \text{Rep}(B_n) \cdot \prod_i \gamma_i$$

**Theorem O-T2 (Unknotting Principle)**:

$$L_2^{new} = L_2^{old} \cdot \prod_{i=n}^{1} \gamma_i^{-1} \cdot \prod_{j=1}^{m} \gamma'_j$$

---

## §4 Information-Theoretic Quantification

### §4.1 Internal Differentiation

**Definition O8**:

$$i_{diff}(s) = -\log(p_{max})$$

### §4.2 Epistemic Bandwidth

**Definition O9**:

$$B_e = \frac{I(L_1; L_2)}{H(L_1)}$$

| Object Type | $B_e$ Value | Feature |
|:---------|:---------|:-----|
| External Objects | $\approx 1$ | Highly communicable |
| Emotional States | 0.3–0.7 | Partially communicable |
| Pure Qualia | $\to 0$ | Ontologically private |

### §4.3 Reality Interface Compression

**Definition O10**:

$$\dim(L_1) \ll \dim(L_0)$$

$$\frac{\dim(L_1)}{\dim(L_0)} = f(\theta_{cognitive})$$

---

## §5 Conservation & Symmetry

### §5.1 L₀ Conservation Law

**Axiom A13**: The operation of the Ghost Operator does not change the cardinality of L₀, only its illumination state.

$$L_0(t) = L_0(t + \Delta t) = \text{Constant}$$

### §5.2 Modal Accessibility Relation

**Definition O11**:

$$w' \text{ accessible from } w \iff \int_{path(w\to w')} \Psi_f(\hat{G}_\theta) \cdot d\sigma < E_{max}$$

**Corollary O-C1 (Access Radius)**:

$$R_{accessible} = \frac{E_{available}}{\bar{\Psi}_f} \propto d^{1.5}$$

---

## §6 Cross-Domain Metaphor Table

| Domain | L₀ Metaphor | L₁ Metaphor | L₂ Metaphor |
|:-----|:--------|:--------|:--------|
| **Physics** | Hilbert Space | Eigenstate | Pointer State |
| **Cognitive Science** | Probability Space | Attentional Focus | Habit/Belief |
| **Social Science** | Cultural Potential | Social Practice | Institutional Norm |
| **Spiritual Tradition** | Emptiness/Tao/Brahman | Present Experience | Karma/Samsara |

---

## Symbol Index

| Symbol | Name | Definition Location |
|:-----|:-----|:---------|
| $L_0$ | Latent Domain | §1.1 |
| $L_1$ | Manifest Domain | §1.2 |
| $L_2$ | Vergence Domain | §1.3 |
| $\mathcal{A}/\mathcal{G}$ | Moduli Space | §2.1 |
| $\eta$ | Hysteresis Coefficient | §1.2 O2a |
| $\beta$ | Gating Coefficient | §1.2 O2b |
| $C_r$ | Reality Confidence Scalar | §1.3 O3c |
| $P_{L_2}$ | L₂ Plasticity Threshold | §1.3 O3c |
| $B_e$ | Epistemic Bandwidth | §4.2 |
| $i_{diff}$ | Internal Differentiation | §4.1 |
