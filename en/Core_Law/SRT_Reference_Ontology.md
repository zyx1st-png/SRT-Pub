---
source_path: Core_Law/SRT_Reference_Ontology.md
source_commit: e212047
translation_status: done
last_sync: 2026-02-19
---

# SRT Reference Ontology

> **Status**: Constitutional Reference | **Version**: 1.0

---

## §1 Triadic Ontology

SRT reconstructs ontology into three relative projection layers under unified selection dynamics.

### §1.1 L0 — Latent Domain

**Definition O1**: The set of high-free-energy states relative to current selection; an unselected possibility field.

$$L_0 \equiv \{σ ∈ S : F[σ] > F[σ_{L_1}]\}$$

**Definition O1a (Absolute Latent Domain)**: The full Ruliad; computational superposition of all logically possible states.

$$L_0^{abs} = Ruliad = \bigcup_{r ∈ Rules} \text{Computation}(r)$$

**Definition O1b (Relative Latent Domain)**: The subset of possibilities accessible to $\hat{G}$ given $L_1(t)$.

$$L_0^{rel}(t+1) = f(L_1(t), \hat{G}_θ)$$

**Unified relation**:

$$L_0^{rel} \subseteq L_0^{abs}|_{physical\ constraints}$$

---

### §1.2 L1 — Manifest Domain

**Definition O2**: The currently selected slice; dynamically maintained present reality.

$$L_1(t) = \hat{G}_θ[σ(t)]$$

**Definition O2a (Hysteresis correction)**:

$$L_1(t) = \hat{G}_θ[L_0(t)] + η · L_1(t - Δt)$$

| $η$ | Effect | Phenomenological appearance |
|:--|:--|:--|
| $η \approx 0$ | no memory | fragmented reality experience |
| $η \approx 0.5$ | balanced | coherent normal reality |
| $η \approx 1$ | locked | cognitive rigidity |

**Definition O2b (Beta-gated mixture)**:

$$L_1^{experienced} = β · L_1^{external} + (1-β) · \hat{G}(L_0)$$

---

### §1.3 L2 — Vergence Domain

**Definition O3**: Long-term attractors of convergent selection; consensus structures across operators.

$$L_2 \equiv \{σ : \hat{G}_θ[σ] = σ \text{ and stable}\}$$

**Definition O3a (Hysteretic accumulation)**:

$$L_2(t) = L_2(t-1) + η · \text{sign}(Δσ) · |Δσ|^α$$

**Definition O3b ($L_2$ hardness)**:

$$\text{Hardness}(L_2) \propto |\text{Aut}(L_2)|$$

| $L_2$ type | Automorphism group | Hardness | Plasticity |
|:--|:--|:--|:--|
| Physical laws | Poincare group | very high | very low |
| Mathematical theorems | logical symmetry group | very high | very low |
| Biological instincts | evolutionarily stable strategies | high | low |
| Cultural norms | context-dependent groups | medium | medium |
| Personal habits | individual history | low | high |

**Definition O3c (Plasticity threshold)**:

$$P_{L_2} = \frac{d_{current} · E_{available}}{Hysteresis(L_2) · C_r}$$

When $P_{L_2} > 1$, $L_2$ can be modified.

---

## §2 Gauge Field Foundation

### §2.1 Moduli-space definition

**Definition O4**: The exact mathematical structure of $L_0$ is a moduli space.

$$L_0^{true} = \mathcal{A}/\mathcal{G}$$

where $\mathcal{A}$ is the set of possible field configurations and $\mathcal{G}$ is the gauge transformation group.

### §2.2 Differential ontology

**Definition O5**: $L_0$ as a differential manifold.

$$L_0 = \mathcal{M}_{differential} = (M, \nabla, \mathcal{S})$$

| Symbol | Definition | Ontological role |
|:--|:--|:--|
| $M$ | base manifold | topological space of potentiality |
| $\nabla$ | connection | potential-gradient structure |
| $\mathcal{S}$ | singular set | attractors, saddles, bifurcation points |

**Theorem O-T1 (Manifestation as integration)**:

$$L_1 = \int_{path(θ)} Structure(L_0) = \oint_γ ω_{L_0}$$

---

## §3 Topological Structure

### §3.1 Topological definition of matter

**Definition O6**: Matter is a topological knot in $L_0$.

$$\text{Matter} = \text{Knot}(L_0) = \text{bound vacuum energy}$$

$$σ_{L_1} = \text{Topology}(\text{Twist}[L_0, θ])$$

### §3.2 Non-Abelian braiding in L2

**Definition O7**: $L_2$ structure is determined by representations of braid group $B_n$.

$$\text{Topology}(L_2) = \text{Rep}(B_n) · \prod_i γ_i$$

**Theorem O-T2 (Unknotting principle)**:

$$L_2^{new} = L_2^{old} · \prod_{i=n}^{1} γ_i^{-1} · \prod_{j=1}^{m} γ'_j$$

---

## §4 Information-Theoretic Quantification

### §4.1 Intrinsic differentiation

**Definition O8**:

$$i_{diff}(s) = -\log(p_{max})$$

### §4.2 Epistemic bandwidth

**Definition O9**:

$$B_e = \frac{I(L_1; L_2)}{H(L_1)}$$

| Entity type | $B_e$ range | Feature |
|:--|:--|:--|
| External objects | $\approx 1$ | highly transmissible |
| Emotional states | 0.3-0.7 | partially expressible |
| Pure qualia | $\to 0$ | ontologically private |

### §4.3 Reality-interface compression

**Definition O10**:

$$\dim(L_1) \ll \dim(L_0)$$

$$\frac{\dim(L_1)}{\dim(L_0)} = f(θ_{cognitive})$$

---

## §5 Conservation and Symmetry

### §5.1 L0 conservation law

**Axiom A13**: Ghost-operator action does not change the cardinality of $L_0$, only its illumination state.

$$L_0(t) = L_0(t + Δt) = \text{Constant}$$

### §5.2 Modal accessibility relation

**Definition O11**:

$$w' \text{ accessible from } w \iff \int_{path(w→w')} Ψ_f(\hat{G}_θ) · dσ < E_{max}$$

**Corollary O-C1 (Accessibility radius)**:

$$R_{accessible} = \frac{E_{available}}{\bar{Ψ}_f} \propto d^{1.5}$$

---

## §6 Cross-Domain Metaphor Table

| Domain | $L_0$ metaphor | $L_1$ metaphor | $L_2$ metaphor |
|:--|:--|:--|:--|
| Physics | Hilbert space | eigenstate | pointer state |
| Cognitive science | possibility space | attentional focus | habit/belief |
| Social science | cultural potential | social practice | institutional norm |
| Spiritual traditions | emptiness/Dao/Brahman | present experience | karma/cyclic pattern |

---

## Symbol Index

| Symbol | Name | Defined in |
|:--|:--|:--|
| $L_0$ | latent domain | §1.1 |
| $L_1$ | manifest domain | §1.2 |
| $L_2$ | vergence domain | §1.3 |
| $\mathcal{A}/\mathcal{G}$ | moduli space | §2.1 |
| $η$ | hysteresis coefficient | §1.2 O2a |
| $β$ | gating coefficient | §1.2 O2b |
| $C_r$ | reality confidence scalar | §1.3 O3c |
| $P_{L_2}$ | $L_2$ plasticity threshold | §1.3 O3c |
| $B_e$ | epistemic bandwidth | §4.2 |
| $i_{diff}$ | intrinsic differentiation | §4.1 |
