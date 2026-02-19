---
source_path: Core/SRT_Core_21_Formal_Axioms.md
source_commit: d48867e
translation_status: done
last_sync: 2026-02-19
---

# SRT Core Definition 21: Formal Axioms (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the Consolidated Axiom List (AI-readable).
> **Part B** contains the Original Formal Derivations (Human-readable context).

---

## Terminology Alignment

- Notation is normalized to Core/Core_Law conventions: `L_0 / L_1 / L_2`, `\hat{G}_\theta`, `d-value`, `\Psi_f`.
- Part A follows the first formal-axiom segment in the source and keeps only the canonical version when duplicates exist.
- Part B is translated from the original fallback section while preserving the original Core intent and section anchors.
- In Part B, keep `\Phi` only in IIT-specific contexts; use `\Psi_f` for ontological-friction contexts.
- Any symbol variants (e.g., `L0/L1/L2` vs `L_0/L_1/L_2`) are interpreted as `L_0/L_1/L_2`.

# Part A: Formal Axioms

> **CRITICAL RULE**: Do NOT just summarize Part B. You must perform First-Principles Derivation.

## I. The Minimal Core

### Ax-F-01: Primacy of Selection
**Formal Definition**: Selection precedes existence; existence is an image of selection.
$$\exists x \iff x \in \mathrm{Range}(\hat{G})$$
* **Implication**: Existence is not a given background, but the output of a selection mapping.

### Ax-F-02: Existence as Anchoring
**Formal Definition**: Existence equals stable anchoring against entropic flow.
$$E = 1 - \frac{H(L_1)}{H(L_0)}$$
* **Implication**: Reality hardness scales directly with entropy-compression ratio.

### Ax-F-03: Causality as Projection
**Formal Definition**: Causality is the $L_2$ projection of selection dynamics.
$$C(A \to B) \equiv P(B | A, L_2)$$
* **Implication**: Causality is a convergence-domain projection, not an ontological primitive.

## II. Information & Fitness

### Ax-F-04: Information-Existence Equivalence
**Formal Definition**: Existence intensity equals the minimum of differentiation and specification.
$$ii(s) = \min\{i_{diff}(s), i_{spec}(s)\}$$
* **Implication**: Existence intensity is jointly constrained by differentiation and specificity.

### Ax-F-05: Fitness Beats Truth
**Formal Definition**: Operators are tuned for fitness payoff rather than veridical truth.
$$\hat{G}_\theta[σ] = \arg\max_{σ'} P(\text{Fitness}|σ', \theta)$$
* **Implication**: The reality interface prioritizes adaptive compression over truth presentation.

### Ax-F-06: Assembly Criterion
**Formal Definition**: Life requires assembly complexity above threshold.
$$\text{Life} \iff \text{Assembly Index} > 15$$
* **Implication**: Biologicality has a minimum structural assembly requirement.

## III. Holographic & Topological

### Ax-F-07: Holographic Duality
**Formal Definition**: Bulk reality is encoded on the boundary of potentiality.
$$L_{1,\text{bulk}} \cong L_{0,\text{boundary}}$$
* **Implication**: Information in manifestation can be fully represented by latent boundary structure.

### Ax-F-08: Topological Normativity
**Formal Definition**: Survival is maintenance of a topological island in probabilistic space.
$$\text{Life}(σ) \equiv \int_{B_r(σ)} ρ_{L_0}(σ') dσ' > \theta_{life}$$
* **Implication**: Survival is topological maintenance of a high-probability packet.

## IV. Scale Consistency & Downward Constraint

### Ax-F-09: Scale Consistency
**Formal Definition**: Selection commutes with coarse-graining under scale mapping.
$$\pi_\lambda \circ \hat{G}_\theta \approx \hat{G}_{\theta,\lambda} \circ \pi_\lambda$$
* **Implication**: Selection dynamics is consistent across scales.

### Ax-F-10: Downward Causation Constraint
**Formal Definition**: $L_2$ constraints modulate selection dynamics as a downward causal term.
$$\frac{dσ}{dt} = \hat{G}_\theta[σ] - \nabla F[σ] - \lambda \cdot \nabla C_{L_2}[σ]$$
* **Implication**: Normative structures feed back as real dynamical terms.

<br>
<br>

---
---

# Part B: Original Formal Derivations (Context)

> **Note**: The following sections preserve the original derivation targets in English.

### 2.1.1 State Space

**Definition M4 (Ghost Operator):**
$$ [\hat{G}_θ(x)]_i = \frac{x_i^n}{ε + \sum_j W_{ij} \cdot x_j^n} $$

### 2.1.5 Minimal Axiom Set

| Axiom | Content |
|:--|:--|
| A1 | **Primacy of selection:** selection process precedes existence |
| A2 | **Existence as anchoring:** existence is the determinacy anchored by selection |
| A3 | **Causality as projection:** causality is an observational slice of selection |
| A4 | **Dynamical definability:** $\hat{G}_θ$ is measurable and maps $S$ to $S$ |
| A5 | **Scale consistency:** $π_λ \circ \hat{G}_θ \approx \hat{G}_{θ,λ} \circ π_λ$ |

### 2.1.6 Downward Causation Constraint

$$ \frac{dσ}{dt} = \hat{G}_θ[σ] - ∇F[σ] - λ \cdot ∇C_{L_2}[σ] $$

### 2.1.7 Effective-Dimension Formalization of d-value (d = D_eff)

$$ d(\hat{G}) \equiv D_{eff}(M) = \frac{(\sum λ_i)^2}{\sum λ_i^2} $$

### 2.1.8 Information-Theoretic Axiom

**Axiom A7 (Pruning criterion, fitness first):**
$$ \hat{G}_θ[σ] = \arg\max_{σ'∈L_0} P(\text{Fitness}|σ', θ) $$

### 2.1.7a Axiom A9: Holographic Duality

$$ L_{1,\text{bulk}} \cong L_{0,\text{boundary}} $$

### 2.1.9a Assembly Theory: A New Measure of Complexity Emergence

$$ \text{Assembly Index}(x) = \min_{\text{path}} |\text{construction steps}| $$

### 2.1.9b Axiom of Deep Time

$$ Mass_{ontological}(O) = Mass_{energy}(O) + τ \cdot Assembly(O) $$
