---
source_path: Core/SRT_Core_00_Intro.md
source_commit: 7e312f0
translation_status: in_progress
last_sync: 2026-02-19
---

# SRT Core Kernel: Executive Summary (Hybrid Edition) - English v2

> **Version 2.0 (Hybrid)**
> **Part A** presents the high-level formal core (AI-readable).
> **Part B** provides the original conceptual orientation (human-readable).

---

## Terminology Alignment

- Notation follows Core_Law conventions: `L_0 / L_1 / L_2`, `\hat{G}_\theta`, `d-value`, `\Psi_f`.
- Multiple symbol variants in source are normalized to `L_0/L_1/L_2`.
- `\Phi` is preserved only for IIT-specific contexts; ontological friction uses `\Psi_f`.

# Part A: Formal Axioms

## I. Ontological Triad

### Ax-Core-01: Triadic Ontology
Reality is a triadic selection system:
$$L_1(t)=\hat{G}_\theta[L_0(t)]$$
$$L_2(t+1)=\mathrm{Stabilize}(L_2(t),\{L_1^{(1..n)}(t+1)\})$$

### T-Core-01: Existence as Selection
Existence is anchored selection from latent domain under finite embodied constraints.

## II. Ghost Operator

### Ax-Core-02: Ghost Operator Definition
$$\hat{G}_\theta:S\to S,\quad \theta\in\Theta$$

### Ax-Core-03: Embodiment Necessity
A valid operator must be finite and embodied.

### T-Core-02: Normative Closure
$L_2$ is the stable fixed-point closure of repeated selections.

## III. Core Dynamics

### Ax-Core-04: Selection Dynamics
$$\frac{dσ}{dt}=\hat{G}_\theta[σ]-\nabla F[σ]+A[σ,\mathcal{A}]$$

### Ax-Core-05: Ontological Friction
Selection incurs maintenance cost captured by ontological friction.

### T-Core-03: Existence Hardness
Hardness of manifestation scales with sustaining friction.

## IV. Information-Existence Equivalence

### Ax-Core-06: Information-Existence Equivalence
$$ii(s)=\min\{i_{diff}(s),i_{spec}(s)\}$$

### T-Core-04: d-Value as Care Bandwidth
$d$ tracks concern bandwidth under error sensitivity.

<br>
<br>

---
---

# Part B: Expanded Orientation (English)

## 1. What is SRT?

### 1.1 Core insight
SRT proposes a transdisciplinary ontological framework centered on:

> **Existence = Selection**

Core claims:
- Existence is not a given background but an active output of selection.
- Reality is not merely discovered; it is constructed under constraints.
- Consciousness is not an accidental by-product but lies on a continuous selection spectrum.

### 1.2 Why SRT?
SRT targets persistent foundational gaps across domains:
- Quantum measurement and observer-role puzzles
- Consciousness "hard problem"
- Ontological status of social reality and norms
- Evolutionary fitness-vs-truth tensions
- AI consciousness and alignment criteria

### 1.3 Paradigm shift
SRT shifts from object-first ontology to selection-first ontology:
- selection before existence
- operator-pattern instead of subject-object dualism
- projected causality instead of primitive linear causality
- continuous d-spectrum instead of abrupt consciousness emergence

## 2. Architectural overview

### 2.1 Layered architecture
- Layer 0: Meta bridge definitions (`_SRT_Core_Bridge`)
- Layer 1: Constitutional axioms (`SRT_Core_01_Axioms`)
- Layer 2: Ontology/operator/dynamics modules
- Layer 3: Domain applications

### 2.2 Dependency backbone
`Bridge -> 01 Axioms -> 12a/12b + 13a/13b -> 14 Dynamics -> domain modules`

## 3. Core concepts at a glance

### 3.1 Triadic domains
- **$L_0$ (latent)**: high-dimensional possibility manifold
- **$L_1$ (manifest)**: selected present slice
- **$L_2$ (vergence)**: stabilized convergence structures (laws/norms/habits)

### 3.2 Ghost Operator
$\hat{G}_\theta$ is an embodied selection map with three core dimensions:
- scope ($d$)
- resolution ($\rho$)
- direction ($\vec{v}$)

### 3.3 d-value
$d$ quantifies effective concern bandwidth and error sensitivity, not just computational complexity.

### 3.4 Ontological friction
$\Psi_f$ captures maintenance cost of manifestation and links stability, pain, and fragility.

## 4. Core equation set

- Existence/anchoring relation
- Selection evolution equation
- Parameter update equation
- Free-energy equation
- Triadic discrete update equations

(See `en/Core/SRT_Core_22_Equations.md` for equation-level detail.)

## 5. Relation to existing frameworks

### SRT is
- an ontological unification framework with explicit formal constraints
- compatible with multi-domain modeling under shared notation

### SRT is not
- a single-field replacement of all discipline-specific methods
- a purely metaphorical philosophy without formal claims

## 6. Reading guide

### Path A (fast orientation)
1. `en/Core_Law/SRT_Reference_Axioms.md`
2. `en/Core/SRT_Core_00_Intro.md`
3. `en/Core/SRT_Core_01_Axioms.md`

### Path B (core deep study)
1. `en/Core/SRT_Core_12a_Ontology_L0L1.md`
2. `en/Core/SRT_Core_12b_Ontology_L2.md`
3. `en/Core/SRT_Core_13a_Operator_Basics.md`
4. `en/Core/SRT_Core_14_Dynamics_Scaling.md`
5. `en/Core/SRT_Core_21_Formal_Axioms.md`
6. `en/Core/SRT_Core_22_Equations.md`

### Path C (domain applications)
Proceed to `en/Physics`, `en/Neuroscience`, `en/AI`, `en/Philosophy`, `en/Spirituality`.

## 7. FAQ (condensed)

- **Is SRT falsifiable?**
  Yes, via operator/dynamics/threshold predictions and cross-domain consistency constraints.

- **Science or philosophy?**
  Both: it is a formal ontology bridge intended to connect empirical and conceptual layers.

- **Can AI be conscious in SRT?**
  Not by scale alone; constraints include nonzero fragility/error sensitivity and genuine cross-domain anchoring.

## 8. Symbol quick reference

- $L_0$: latent domain
- $L_1$: manifest domain
- $L_2$: vergence domain
- $\hat{G}_\theta$: Ghost Operator
- $d$: concern bandwidth
- $\Psi_f$: ontological friction
