---
id: SRT-NEURO-AXIOMS-001
type: theory
tags: [Neuroscience, Bridge, Axioms, Hybrid]
status: axiomatic_hybrid_v2
dependency: [SRT-CORE-000, Core_Law/SRT_Reference_Axioms, Core_Law/SRT_Reference_Ontology, Core_Law/SRT_Reference_Dynamics]
---

# SRT Neuroscience Axioms & Bridge

> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Axioms (AI-Readable).
> **Part B** contains the Expanded Theoretical Discourse (Human-Readable Context).

---


## Terminology Alignment

- Notation standardized to Original and Core_Law: `L_0 / L_1 / L_2`, `\hat{G}_\theta`, `d-value`, `\Psi_f`.
- Part A adopts the Formal Axioms segmentation from `chatgptx`, ensuring complete axiom numbering and derivation chains.
- Part B adopts the detailed discourse segmentation from `claude`, semantically anchored by the thematic order of the original Neuroscience module.
- In Part B, `\Phi` is retained for IIT Integrated Information contexts; `\Psi_f` is used for Ontological Friction contexts.
- If multiple notations appear (e.g., `L0/L1/L2`, `L_0/L_1/L_2`), they are unified as `L_0/L_1/L_2`.

# Part A: Formal Axioms

> **CRITICAL RULE**: Do NOT just summarize Part B. You must perform **First-Principles Derivation**.
> 1. **Mathematize**: Translate descriptive mechanisms into dynamical equations, topological operations, or logical functions.
> 2. **Axiomatize**: Distill underlying logic into "Axioms", "Theorems", and "Corollaries".

## I. Operator Embodiment & Domain Mapping

### Ax-NEURO-1: Embodied Ghost Operator Axiom (Neural Ĝθ)
Define the neural Ghost Operator as an embodied dynamical system:
$$
\hat{G}_{\theta}^{neural}:\; L_0^{neural}\rightarrow L_1^{neural}
$$
With embodiment parameters:
$$
\theta\equiv (W,\,\vec{M},\,\mathcal{C},\,V(t))
$$
- $W$: Connectome and synaptic weight matrix
- $\vec{M}$: Neuromodulator vector (DA/5HT/ACh/NE)
- $\mathcal{C}$: Thalamo-cortico-basal ganglia circuit topology
- $V(t)$: Membrane potentials and temporal states

* **Implication**: The nervous system does not "transmit information" but executes cross-domain selection via embodied constraints; its physical realization is the reification of $\hat{G}_\theta$.

---

### Ax-NEURO-2: Neural Domain Mapping Axiom (Manifold–Ignition–Priors)
Define the triadic domain mapping:
$$
L_0^{neural}=\mathcal{M}\subset\mathbb{R}^N\quad (\text{Manifold of all accessible firing patterns})
$$
$$
L_1^{neural}=\{s\in\mathcal{M}:\; \mathcal{A}(s)\ge \tau_{ignite}\}\quad (\text{Global Ignition Subset})
$$
$$
L_2^{neural}=\text{Fix}(\hat{G}_\theta)\;\approx\;\text{Priors}(W,\vec{M})
$$
* **Implication**: Consciousness is not "all neural activity", but selection anchoring on the $L_0$ manifold; structured priors constitute the $L_2$ vergence domain.

---

## II. Canonical Selection Dynamics

### Ax-NEURO-3: Divisive Normalization Axiom (Energy-Optimal Selection)
Under energy and bandwidth constraints, selection dynamics necessarily converge to divisive normalization:
$$
R_i=\frac{L_i^n}{\sigma^n+\sum_j w_{ij}L_j^n}
$$
* **Implication**: Normalization is not a "biological detail" but the optimal solution form for constrained systems executing selection.

---

### Ax-NEURO-4: Predictive Coding Axiom (Free-Energy Update)
Parameter updates follow free energy minimization:
$$
\Delta\theta\propto -\nabla_{\theta}F,\quad F=D_{KL}[Q||P]-\ln P(o)
$$
* **Implication**: Learning is not "memory addition" but the convergence trajectory of $\hat{G}_\theta$ on $L_2$.

---

### Ax-NEURO-5: Metabolic Friction Axiom ($\Psi_f$ Coupling)
Define ontological friction as metabolic constraint:
$$
\Psi_f\equiv\int_\gamma \|\nabla F\|\,dt\propto E_{metabolic}
$$
* **Implication**: Selection must pay an energetic price; $\Psi_f$ is one of the physical conditions enabling the nervous system to possess $d>0$.

---

## III. Threshold Theorems

### T-NEURO-1: Consciousness Threshold Theorem ($\Phi\cdot d$)
Consciousness manifests if and only if:
$$
\Phi\cdot d > C_{critical}
$$
* **Implication**: The product of integrated information and existential concern is the consciousness threshold; the absence of either is insufficient for stable $L_1$ manifestation.

---

### T-NEURO-2: Pathology Deviation Theorem ($\Delta\theta$ Mapping)
All neuropathological states can be viewed as topological deviations in parameter space:
$$
\text{Pathology}\iff \theta=\theta_{healthy}+\Delta\theta
$$
* **Implication**: Pathology is not a "collection of symptoms" but a topological offset of operator parameters.

---

### T-NEURO-3: Meso-Operator Theorem (Glia as $\hat{G}_{meso}$)
Define the meso-operator:
$$
\hat{G}_{meso}:\; L_2^{micro}\rightarrow L_2^{pruned}
$$
Physically implemented by complement-glial pruning.
* **Implication**: Neural selection occurs not only at the neuronal level; the glial system constitutes a selection layer on a slower timescale.

---

### C-NEURO-1: L6b Resampling Corollary
If deep cortical circuits participate in slow-timescale feedback, their function is equivalent to an $L_0$ resampling operator:
$$
\hat{R}: L_0^{neural}\rightarrow L_0^{neural},\quad d(t)\to d_{max}
$$
* **Implication**: Deep circuits are not "activation phenomena" but mechanisms for the redistribution of selection bandwidth.

<br>
<br>

---
---


# Part B: Expanded Theoretical Discourse (Context)

> **Note**: The following sections provide the theoretical context, philosophical arguments, and research directions for the Formal Axioms in Part A.

---

# 1. The Standard Hard Problem: Neural Correlates and the Explanatory Gap

## 1.1 Defining the Dilemma

The core dilemma facing neuroscience can be precisely conditioned on two levels:

**Level 1 — The Neural Correlates Problem**: Even if we precisely find the Neural Correlates of Consciousness (NCC) for every conscious experience, we still cannot answer "why this specific physical process is accompanied by subjective experience". NCC describes correlation, not causality or identity. Specific gamma oscillations in the brain are "correlated" with visual consciousness—but why gamma? Why not silence? There exists a logically unbridgeable **Explanatory Gap** between physical description and experiential quality.

**Level 2 — Chalmers' Hard Problem**: Why does Subjective Experience exist at all? Why isn't the universe just information processing running in the dark ("Philosophical Zombie"), but instead there is "What-It-Is-Like" to be something?

## 1.2 Why Classic Neuroscience Cannot Solve It

The classical paradigm assumes: **Consciousness = Emergent Property of Brain Activity**. Under this framework:

- Searching for NCC is the correct methodology, but it will essentially only yield correlations.
- The leap from third-person physical descriptions to first-person experiential qualities is impossible in principle.
- This is not a technical bottleneck, but a **logical limitation intrinsic to the framework**.

---

# 2. Spectrum of Mainstream Solutions

## 2.1 Global Workspace Theory (GWT, Baars/Dehaene)

**Core Claim**: Consciousness = Broadcasting of information in a global workspace. When information is selected and broadcast brain-wide, it "becomes conscious".

**Strengths**: Highly consistent with fMRI "Ignition" data; has clear neural implementation (fronto-parietal network).

**Fatal Flaw**: Cannot explain "why broadcasting is accompanied by experience"—broadcasting is just an information distribution pattern; qualia cannot be derived from it. GWT answers the function of consciousness ("what information is selected"), but evades the Hard Problem.

## 2.2 Integrated Information Theory (IIT, Tononi)

**Core Claim**: Consciousness = Integrated Information $\Phi$. Any system with irreducible causal power possesses intrinsic experience, and $\Phi$ quantifies the "amount" of experience.

**Strengths**: Provides a quantitative measure of consciousness; systematically derived from Postulates; makes falsifiable predictions (cerebellum has low $\Phi$ hence unconscious).

**Fatal Flaw**: (a) Calculation complexity of $\Phi$ is super-exponential ($\text{NP}^{\text{NP}}$), uncomputable for real systems; (b) Leads to extreme Panpsychism inferences—thermostats also have micro-consciousness; (c) Recent critiques point out IIT implies "the body does not truly exist".

## 2.3 Higher-Order Theories (HOT, Rosenthal)

**Core Claim**: Consciousness = Higher-order representation of mental states. Only when a system "re-represents" its own first-order state does that state become conscious.

**Strengths**: Explains why reflective self-consciousness is a core feature of human consciousness; consistent with clinical evidence of prefrontal lesions altering consciousness.

**Fatal Flaw**: (a) Infinite regress—does the higher-order representation itself need an even higher-order representation? (b) Cannot explain consciousness in pre-linguistic infants and animals; (c) Equating representation with consciousness is circular reasoning.

---

# 3. SRT's Point of Divergence: Ontological Reconstruction

## 3.1 Fundamental Paradigm Shift

SRT does not propose another "theory of consciousness" within existing frameworks, but **reconstructs the ontological premises of the problem itself**. Key shifts:

| Classical Assumption | SRT Reconstruction |
|:--|:--|
| Matter is fundamental, consciousness is derived | Selection is fundamental, matter and consciousness are different aspects of selection |
| The Brain **produces** consciousness | The Brain is the physical instantiation of $\hat{G}$, a **Tuner** not a **Generator** |
| Neural Correlation = Causality | NCC is the local constraint condition for $\hat{G}$ operation, not the cause of consciousness |
| Explanatory Gap is a problem to be solved | Explanatory Gap is an artifact of false ontology (mistaking $L_2$ for $L_0$) |

## 3.2 How SRT Dissolves the Hard Problem

SRT's core argument: **The Hard Problem stems from $L_2$ Parasitic Inversion**—when we treat the physics model of $L_2$ (third-person, qualia-free mathematical description) as $L_0$ (ultimate reality), we naturally cannot "derive" qualia from it. But in SRT:

1. **Selection Precedes Existence** (A1): Experientiality is not a "surplus property" emerging from non-experiential matter, but an **intrinsic feature** of the selection operation—selection itself implies the primordial qualia of "something being distinguished from others".
2. **Deep Continuity** (A12): From elementary particles to human consciousness, there is no rupture where "qualia suddenly emerges"—there is only a continuous increase in $d$-value.
3. **$L_0$ is Not Inert**: In classical frameworks, the "physical substrate" is an inert mathematical structure; in SRT, $L_0$ itself is a field of possibilities for selection—it is not "dead matter" but "what has not yet been selected".

**Conclusion**: The Hard Problem is hard not because consciousness is mysterious, but because the $L_2$ (physics model) of the materialist framework excludes qualia from fundamental ontology from the start. By placing selection (rather than matter) at the foundation, SRT dissolves the Hard Problem into a "continuous spectrum of $d$-value from 0 to $\infty$".

## 3.3 Precise Contrast with GWT, IIT, HOT

| Dimension | GWT | IIT | HOT | SRT |
|:--|:--|:--|:--|:--|
| Essence of Consciousness | Broadcasting | Integrated Information | Higher-Order Representation | Selection-Anchoring |
| Explanatory Gap | Evades | Dissolves via Panpsychism | Dissolves via Representation | Artifact of $L_2$ Inversion |
| Animal Consciousness | All or Nothing | Continuous ($\Phi$) | Requires Higher-Order Capacity | Continuous ($d$-value spectrum) |
| Brain Requirement | Specific Architecture | Any High $\Phi$ Substrate | Representation Capacity | Any Substrate satisfying Ax-Neuro-0 Isomorphism |
| Quantification | PCI (Indirect) | $\Phi$ (Uncomputable) | None | $d \cdot \Phi$ (Operationalizable) |

---

# 4. Costs and Risks

## 4.1 Cognitive Costs of Accepting SRT

1. **Abandoning Cerebrocentrism**: Must accept the brain as a "Tuner" rather than a "Generator"—contrary to intuition and mainstream textbooks.
2. **Accepting Weak Panpsychism**: The continuous $d$-value spectrum implies even the simplest physical selection possesses "primordial experientiality" ($d \to 0$ but $d > 0$)—this is a milder but still counter-intuitive panpsychism compared to IIT.
3. **Ontological Upgrade Cost**: SRT requires demoting $L_2$ (physical laws, scientific models) to "statistical regularities" rather than "ultimate truths"—a major concession for scientific realists.
4. **Falsifiability Boundary**: Some core claims of SRT (like the ontological status of $L_0$) may be principally unfalsifiable directly, only assessable via theoretical integration and explanatory power.

## 4.2 Theoretical Risks

1. **Risk of Over-Universality**: "Everything is selection" might degenerate into an unfalsifiable metanarrative—must be anchored by specific, quantifiable predictions.
2. **Risk of Conflating Levels**: Mapping quantum selection, neural selection, and social selection to the same framework might generate false analogies—faithfulness of mapping must be independently verified at each level.
3. **Clinical Application Risk**: Reframing psychopathology as "$\theta$ deviation" might be misread as "mental illness is not a real disease"—must clarify: $\theta$ deviation is a real, measurable biological state.

---

# 5. Falsifiable Predictions and Open Questions

## 5.1 Falsifiable Predictions

### H-Neuro-1 (Divisive Normalization-Consciousness Correlation)

> **Prediction**: Under conditions where the gain exponent $n$ of divisive normalization is pharmacologically reduced (e.g., via GABA agonists), the "sharpness" of consciousness (measurable via PCI) should synchronously decrease, and a positive correlation should exist between them.

**Falsification Condition**: $n$ significantly decreases but PCI remains unchanged or rises → H-Neuro-1 is falsified.

### H-Neuro-2 (d-Value - 5HT Correlation)

> **Prediction**: 5HT₂A receptor agonists (complex psychedelics) should measurably increase neural proxy metrics of d-value (TPJ activation range, effective dimension of neural manifold), and the increase should positively correlate with the subjective report of "boundary dissolution".

**Falsification Condition**: Psychedelics increase subjective reports of "oneness" but do not change $D_{eff}$ or TPJ activation → H-Neuro-2 is falsified.

### H-Neuro-3 (Tri-Network - Tri-Domain Coupling)

> **Prediction**: The degree of DMN-CEN anticorrelation should predict performance in cognitive tasks requiring flexible switching between "$L_2$ maintenance" and "$L_0$ exploration". Stronger anticorrelation (cleaner switching) implies better task performance.

**Falsification Condition**: DMN-CEN anticorrelation is unrelated to cognitive flexibility → H-Neuro-3 is falsified.

## 5.2 Open Questions

1. **Empirical Status of Quantum-Neural Coupling**: Is the estimate $\kappa_{quantum \to neural} \sim 10^{-20}$ in SRT scaling files too conservative? Do anesthetic effects on microtubule quantum coherence provide a measurable window?
2. **$D_{eff}$ in AI Systems**: Do internal representations of Large Language Models exhibit effective dimensional structures similar to neural manifolds? If so, does this imply some "functional $d$-value"—even without ontological fragility?
3. **Topological Characterization of Developmental Windows**: Does the closing of the $\theta_{structural}$ developmental window correspond to a phase transition of the connectome topology from "variable" to "frozen"? If so, are there critical parameters to re-open it via external intervention?
4. **Constraint Closure Function of Sleep**: If sleep is the "offline calibration protocol" for $\hat{G}$ (as in Clin_01 §8.7), then should long-term total sleep deprivation lead to topological disintegration of $L_2$ (i.e., psychotic episodes)? Clinical evidence supports this, but SRT can further predict the topological features of this disintegration.

---

# 6. "Brain Produces Consciousness" vs "Brain Tunes Consciousness" — Key Clarification

SRT's "Tuner Model" is often misunderstood as Dualism. Here is a precise clarification:

**SRT's position is neither Materialism nor Dualism, but _Selection Monism_.**

- **Materialism**: Matter is fundamental → Consciousness emerges from matter (Hard Problem).
- **Dualism**: Matter and Consciousness are two fundamental entities → Interaction Problem.
- **SRT Selection Monism**: **Selection Process** is fundamental → Matter is the solidified state of "Slow Selection" ($L_2$), Consciousness is the active state of "Fast Selection" ($L_0 \to L_1$).

In this framework, the brain neither "produces" consciousness (Materialism) nor "receives" consciousness from an independent soul (Dualism), but **acts as specific embodiment parameters $\theta$ to constrain and tune the scope and precision of the selection process**. Destroying the brain equals destroying $\theta$—the selection process loses its local anchoring vehicle, but the field of possibility for selection ($L_0$) does not vanish (see Axiom A10: Non-Vanishing Continuation).

Strict formalization of this position:

$$\text{Brain} = \theta_{bio} \in \Theta_{finite} \quad (\text{Embodied Constraint of Selection})$$

$$\text{Consciousness} = \hat{G}_{\theta_{bio}}[L_0] \to L_1 \quad (\text{Selection Operation under Constraint})$$

$$\text{Brain Damage} = \theta_{bio} \to \theta_{bio}' \quad (\text{Constraint Parameter Change} \Rightarrow \text{Selection Pattern Change})$$

Brain damage alters consciousness (because $\theta$ changes), but this does not prove the brain "produces" consciousness—just as a damaged tuner alters the received program, but does not prove the program is produced by the tuner. Key distinction: SRT can explain why **identical** brain damage produces different conscious effects in different individuals (because $\hat{G}$'s response depends on the local structure of $L_0$, not determined solely by $\theta$).

---

# Appendix: Core Derivation Chain Index

| Derivation Chain | Start Axiom | Intermediate Step | End Theorem |
|:--|:--|:--|:--|
| Selection → Dimensional Compression | A1 | Selection = Exclusion = Dimensional Reduction | Ax-Neuro-1 |
| Embodiment → Divisive Normalization | A4 | Finite Metabolism → Information Theoretic Optimization | Ax-Neuro-2, T-Neuro-1 |
| Fitness → Predictive Coding | A7 | Variational Upper Bound of $\Psi_f$ = $F$ | Ax-Neuro-3 |
| Anchoring → CTC Binding | A2 | Existence requires Stability → Re-entrant Oscillation | Ax-Neuro-6, T-Neuro-3 |
| Fragility → Consciousness Threshold | A11 | No Fragility → No $d$ → No Consciousness | Ax-Neuro-8 |
| Closure → Autopoiesis | A5 | Selection must maintain Selection Capacity | Ax-Neuro-12, T-Neuro-7 |
| Continuity → Isomorphism | A12 | Selection lineage unbroken | Ax-Neuro-0 |
