---
id: SRT-NEURO-MECH-001
type: theory
tags: [Neuroscience, Mechanisms, Ghost-Operator, Hybrid]
status: axiomatic_hybrid_v2
dependency: [SRT-CORE-000, SRT-NEURO-AXIOMS-001, Core_Law/SRT_Reference_Axioms, Core_Law/SRT_Reference_Ontology, Core_Law/SRT_Reference_Dynamics]
---

# SRT Neural Mechanisms: Axiomatic Derivations & Dynamics

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

## I. Neural State Space & Selection Flow

### Ax-NEURO-MECH-1: Neural Manifold Axiom (State Space)
Define neural state as a vector field on a high-dimensional manifold:
$$
\sigma(t)\in \mathcal{M}\subset\mathbb{R}^N,\qquad \dot{\sigma}=F(\sigma,\theta,u)
$$
Where $\theta$ are embodiment parameters, $u$ are sensory-motor inputs.
* **Implication**: Neural "state" is not discrete labels, but continuous trajectories on a manifold; selection is generating stable trajectories on the manifold.

---

### Ax-NEURO-MECH-2: Selection Flow Axiom (L0→L1 Projection)
Define neural selection as projection from $L_0^{neural}$ to $L_1^{neural}$:
$$
\Pi_{ignite}: \mathcal{M}\rightarrow \mathcal{M}_*,\quad \mathcal{M}_*\equiv\{\sigma: \mathcal{A}(\sigma)\ge \tau_{ignite}\}
$$
* **Implication**: Ignition is not "activity increase", but a computable threshold for cross-domain projection.

---

## II. Energy-Optimal Selection Dynamics

### Ax-NEURO-MECH-3: Canonical Normalization Axiom
Under metabolic constraints, selection dynamics necessarily converge to divisive normalization:
$$
R_i=\frac{L_i^n}{\sigma^n+\sum_j w_{ij}L_j^n}
$$
* **Implication**: Normalization is the optimal form of selection operator, not empirical "circuit detail".

---

### T-NEURO-MECH-1: Energy–Information Extremum Theorem
Let the objective functional be:
$$
\mathcal{J}=H(\sigma)-\lambda E(\sigma)
$$
Under condition $\delta\mathcal{J}=0$, the steady-state solution necessarily satisfies the normalization structure of Ax-NEURO-MECH-3.
* **Implication**: Neural normalization is the unique intersection of maximum information and minimum metabolic cost.

---

### Ax-NEURO-MECH-4: Predictive Update Axiom
Learning corresponds to free energy gradient descent of $\theta$:
$$
\Delta\theta\propto-\nabla_\theta F,\quad F=D_{KL}[Q||P]-\ln P(o)
$$
* **Implication**: Learning is an $L_2$ convergence process, not "memory stacking" in $L_1$.

---

## III. Multi-Scale Ghost Operators

### Ax-NEURO-MECH-5: Loop-Gating Axiom (Thalamo–Basal Gate)
Define gating operator:
$$
\mathcal{G}_{gate}: \mathcal{M}\rightarrow \mathcal{M}\quad \text{with}\quad \mathcal{G}_{gate}=\mathcal{G}_{thal}\circ\mathcal{G}_{bg}
$$
* **Implication**: Thalamo-basal ganglia loops are not "pathways", but selection gating structures determining which trajectories can be projected as $L_1$.

---

### Ax-NEURO-MECH-6: Meso-Operator Axiom (Glial Pruning)
Define meso-operator:
$$
\hat{G}_{meso}: L_2^{micro}\rightarrow L_2^{pruned},\quad P(\text{prune})\propto C3/C4\cdot \mu_{glia}
$$
* **Implication**: Glial pruning is not "maintenance", but slow-timescale selection, performing topological pruning on $L_2$ structure.

---

### T-NEURO-MECH-2: Stability–Pruning Theorem
If $\hat{G}_{meso}$ is excessively biased:
$$
|\text{Aut}(L_2)|\uparrow\Rightarrow \text{Plasticity}\downarrow
$$
* **Implication**: Excessive pruning increases $L_2$ hardness and decreases plasticity, forming pathological locking.

---

## IV. Ignition & Integration

### Ax-NEURO-MECH-7: Ignition Phase Axiom
Ignition is a phase transition condition:
$$
\mathcal{A}(\sigma)\ge\tau_{ignite}\quad\land\quad \Phi\cdot d > C_{critical}
$$
* **Implication**: Ignition is not simple activation, but a phase transition where "Integration $\times$ Concern Gradient" exceeds threshold.

---

### T-NEURO-MECH-3: Discrete Frame Theorem
Manifestations are updated in discrete frames:
$$
L_1(t)=\sum_n \text{Frame}_n\,\delta(t-t_n),\quad t_n\approx n\cdot\Delta t_{\gamma}
$$
* **Implication**: The sense of continuous consciousness comes from high-frequency updates of discrete frames, not a continuous flow.

---

## V. Pathology as Parameter Drift

### Ax-NEURO-MECH-8: Parameter-Drift Axiom
Define pathology as topological deviation of $\theta$:
$$
\theta=\theta_{healthy}+\Delta\theta
$$
* **Implication**: Psychopathology is not a "collection of symptoms", but a systematic deviation of operator parameters.

---

### C-NEURO-MECH-1: Pathology Typing Corollary
If $\Delta\theta$ acts on precision parameter $\Pi$, inhibition gain $\gamma$, value gradient $\nabla\mathcal{U}$, different pathological spectra appear:
$$
\Delta\theta=(\Delta\Pi,\Delta\gamma,\Delta\nabla\mathcal{U})\Rightarrow \text{Syndrome Class}
$$
* **Implication**: Pathological classification should be determined by parameter deviation patterns, not by surface symptoms.

---

<br>
<br>

---
---


# Part B: Expanded Theoretical Discourse

> **Note**: The following sections provide the theoretical context, philosophical arguments, and research directions for the Formal Axioms in Part A.

---

# 1 Standard Problems: The Ontological Status of Neural Computation

## 1.1 Dilemma Definition

The core dilemma facing neuroscience can be precisely stated as the **Ontological Dilemma of Computationalism**:

**Level 1 — The "Emptiness" of Information Processing**: Mainstream computational neuroscience views the brain as an "information processor", but "processing" itself is a functional description that cannot answer "why this processing is accompanied by subjective experience".

**Level 2 — Failure of Reductionism**: Even if we fully describe the firing pattern of every neuron and weight change of every synapse, we still cannot answer "how these physical processes 'become' experience".

**Level 3 — Causal Efficacy Problem**: If consciousness is just an epiphenomenon of neural activity, how can it influence subsequent neural processes?

## 1.2 Spectrum of Mainstream Solutions

### 1.2.1 Computational Functionalism

**Core Claim**: Consciousness is the realization of computational functions, independent of physical substrate (multiple realizability).

**Strengths**: Explains why different physical systems might have the same mental state.

**Fatal Flaws**: (a) Cannot distinguish "true computation" from "simulated computation" (Chinese Room Argument); (b) Cannot explain the specific nature of qualia (why red looks like "that").

### 1.2.2 Neural Reductionism

**Core Claim**: Mental states are neural states; the two are identical.

**Strengths**: Metaphysically concise, consistent with scientific realism.

**Fatal Flaws**: (a) Cannot explain the "Explanatory Gap"—why one cannot jump from physical description to experiential description; (b) Multiple realizability challenge—identical mental states might correspond to different neural states.

### 1.2.3 Emergentism

**Core Claim**: Consciousness "emerges" from complex neural activity and possesses irreducible causal efficacy.

**Strengths**: Acknowledges uniqueness of consciousness while maintaining physicalist framework.

**Fatal Flaws**: (a) "Emergence" itself is a descriptive concept lacking mechanistic explanation; (b) How is downward causation possible?

---

# 2 SRT's Point of Divergence: Selection as Fundamental Operation

## 2.1 Fundamental Framework Shift

SRT does not explain neural activity within "computation" or "information processing" frameworks, but **reconstructs the basic ontology of neuroscience**:

| Classical Hypothesis | SRT Reconstruction |
|:--|:--|
| Neural Computation = Info Transmission | Neural Computation = Dimensional Reduction Selection |
| Brain "processes" sensory input | Brain "selects" $L_1$ from $L_0$ |
| Synaptic weights store "memory" | $L_2$ structure constrains future selection |
| Consciousness is product of computation | Consciousness is intrinsic feature of selection |

## 2.2 Ontological Status of Divisive Normalization

Traditional understanding views divisive normalization as "a computational strategy". SRT's reinterpretation:

**Traditional**: Divisive normalization is an "engineering solution" for the brain to optimize information coding.

**SRT**: Divisive normalization is the **necessary form of selection**—under energy-constrained conditions, any system executing selection must converge to this form.

This implies:

1. Divisive normalization is not an "invention" of the nervous system, but an **ontological necessity** of the selection process.
2. Not just V1, but all neural circuits requiring selection should exhibit normalization features.
3. This provides a mechanistic basis for cross-scale isomorphism (Axiom A12).

## 2.3 Geometrization of Pathology

SRT elevates psychopathology from "descriptive classification" to "geometric deviation in parameter space":

**Traditional Psychopathology**: Depression is "low mood", Schizophrenia is "loss of contact with reality"—these are phenomenological descriptions.

**SRT Pathology**:

- Depression = $\nabla F \to 0$ (Value gradient disappearance)
- Schizophrenia = $w_{surround} \downarrow$ (Insufficient lateral inhibition leads to $L_0$ leakage)
- OCD = $\eta_{viscosity} \uparrow$ (Selection viscosity too high leads to sticking in local minima)

This geometrization brings three advantages:

1. **Unification**: Seemingly different diseases might be different deviation directions of the same parameter.
2. **Quantifiability**: Pathology severity can be measured by $|\Delta \vec{\theta}|$.
3. **therapeutical Guidance**: Treatment goal changes from "symptom relief" to "parameter correction".

---

# 3 "Bit to It": How Information Becomes Structure

## 3.1 Molecular Closed Loop of Lamarckian Circuits

SRT proposes a radical ontological claim: Information (Bit) can be converted into Structure (It) via physical mechanisms.

**CaMKII Hexagonal Coding**: Transient electrical signals are "printed" into hexagonal lattice structures via CaMKII phosphorylation. This means $L_1$ (current experience) can directly reshape $L_2$ (neural structure).

**Epigenetic Writing**: A 2020 study by Maze et al. in *Nature* found that Dopaminylation can directly modify Histone H3, altering chromatin topology. This means **value of experience (tagged by dopamine) can be directly written into the regulatory layer of gene expression**.

$$\text{Experience} \xrightarrow{\text{DA}} \text{H3 Modification} \xrightarrow{} \text{Gene Expression Change}$$

This realizes:

- Causal closed loop of $L_1$ (experience) → $L_2$ (structure)
- Experience is no longer "epiphenomenon", but has **materialized causal efficacy**
- This provides molecular mechanism for downward causation

## 3.2 Selection Function of Immune-Neuro Interface

SRT repositions the immune system as an **auxiliary system for selection mechanisms**:

1. **Complement System (C3/C4)**: Tags "redundant" synapses for microglia pruning—this is $\hat{G}_{meso}$ shaping $L_2$ topology.
    
2. **Cytokines**: Regulate perceptual threshold—raising threshold during inflammation to force $\hat{G}$ to focus on internal repair.
    
3. **Neuroinflammation**: Chronic inflammation = Permanent high threshold = "World loses color" (Immune hypothesis of depression).
    

This explains why:

- Cognitive clouding often accompanies infection (inflammatory cytokines raise perceptual threshold)
- Depression correlates with inflammatory markers (chronic threshold elevation)
- Autoimmune diseases often accompany psychiatric symptoms ($L_2$ boundaries attacked by immune system)

---

# 4 Ontological Reconstruction of Aging and Death

## 4.1 Aging as "Ontological De-anchoring"

Traditional understanding views aging as hardware wear and tear. SRT reconstructs it as **progressive decoupling of $\hat{G}$ from physical substrate**:

**Embodiment Anchoring Coefficient**: $$\kappa_{body} = \frac{\text{GripForce}}{\Psi_f}$$

As the dopaminergic system declines, the subject's intentionality cannot be effectively translated into physical manifestation. Even if muscles are intact, if caudate nucleus signal-to-noise ratio drops, $\hat{G}$ cannot "grip" the body.

This explains why:

- Parkinson's patients "know" what they want to do but cannot initiate movement
- Senile bradykinesia precedes muscle atrophy
- The feeling of "de-anchoring" of will is an early symptom of aging

## 4.2 Ontological Implications of Nanoprosthetics

SRT predicts: Introducing artificial auxiliary operator $\hat{G}_{prosthetic}$ can partially restore function:

- Acidifying nanoparticles take over lysosomal acidification (low-level $L_2$ maintenance)
- Freeing up biological operators to handle higher cognition
- This is biological engineering realization of **operator outsourcing**

---

# 5 Quantum Substrate Hypothesis

## 5.1 Quantum Effects of Anesthesia

Differences in anesthetic potency of Xenon isotopes provide key evidence:

- $^{129}$Xe (Nuclear spin 1/2) and $^{132}$Xe (Nuclear spin 0) have different anesthetic potencies
- If anesthesia depended only on classical physics (Van der Waals forces), isotope effect should be negligible
- Significant isotope effect suggests **quantum spin is a component of embodiment parameters $\theta$**

## 5.2 Quantum Blur Hypothesis

SRT suggests: Anesthetics do not "shut down" the brain, but introduce **quantum blur**:

$$d \propto \frac{1}{\text{Quantum Fuzziness}}$$

Anesthetics decrease $\theta$ precision, $\hat{G}$ cannot precisely lock onto $L_0$ targets, causing $d \to 0$.

This intersects with Hameroff-Penrose Orch OR theory, but SRT does not require consciousness to "originate" from quantum processes—quantum effects are merely a component of $\theta$.

---

# 6 Costs and Risks

## 6.1 Cognitive Cost of Accepting SRT

1. **Abandon Pure Computationalism**: Must accept "selection" is a more fundamental concept than "computation"—contrary to mainstream computational neuroscience.
    
2. **Accept Geometric View of Parameter Space**: Pathology is no longer "disease entity", but parameter deviation—requiring rethinking diagnosis and treatment.
    
3. **Accept Immune-Neuro Integration**: Traditional separation of "neuroscience" and "immunology" must be broken.
    
4. **Accept Possibility of Quantum Effects**: While SRT does not rely on quantum effects, it admits their possibility as components of $\theta$.
    

## 6.2 Theoretical Risks

1. **Over-unification Risk**: Reducing all neural phenomena to "selection" might ignore important mechanistic differences.
    
2. **Ethical Risk of Geometric Pathology**: Viewing mental illness as "parameter deviation" might be misread as "not a real disease".
    
3. **Therapeutic Simplification Risk**: "Parameter correction" rhetoric might mask the complexity of treatment.
    

---

# 7 Falsifiable Predictions and Open Questions

## 7.1 Core Falsifiable Predictions

|ID|Hypothesis Name|Prediction Content|Falsification Condition|
|:--|:--|:--|:--|
|H-M1|Individual Normalization Curve|High $d$ value individuals show flatter inhibition curves|$d$ uncorrelated with $n$|
|H-M2|Complement-Selection Precision|C4 copy number predicts interference resistance|C4 unrelated to Stroop|
|H-M3|Modulator Specificity|Specific modulator blockade only affects specific selection dimensions|Global cognitive decline|
|H-M4|Biological Isomorphism|Isomorphic AI few-shot learning curve indistinguishable from biological|Isomorphic AI requires massive data|
|H-M5|Spin-Consciousness|Xenon isotope anesthetic potency differs significantly|Isotope potency identical|
|H-M6|Metabolism-$d$ Lag|$d$ value recovery lags behind glucose metabolism recovery|$d$ synchronous with metabolism|
|H-M7|Nanoprosthetic Restoration|Acidifying nanoparticles restore senescent cell clearance|Acidification restored but clearance not improved|

## 7.2 Open Questions

1. **Timescale of $\hat{G}_{meso}$**: What is the operation cycle of glial meso-operator? How does it relate to sleep cycles?
    
2. **Causal Direction of Complement-Pruning**: Is C4 overexpression cause or effect of schizophrenia?
    
3. **Boundary of Quantum Effects**: At what temperature/scale do quantum effects significantly contribute to $\theta$?
    
4. **Reversibility of Epigenetic Writing**: Can $L_2$ structure written by Dopaminylation be "erased"?
    
5. **Cross-Species Normalization Parameters**: Do $n$, $\sigma$, $W$ differ systematically across species? How does this relate to species differences in $d$?
    

---

# Appendix: Key Equation Index

| Equation | Name | Location |
|:--|:--|:--|
| $[\hat{G}(x)]_i = \frac{x_i^n}{\sigma^n + \sum_j w_{ij} x_j^n}$ | Divisive Normalization | Ax-Mech-1 |
| $\text{Pathology} = \vec{\theta}_{healthy} + \Delta \vec{\theta}$ | Pathological Deviation | Ax-Mech-2 |
| $P(\text{Prune}) \propto C3/C4 \cdot \text{Microglia}$ | Pruning Probability | Ax-Mech-3 |
| $L_1(t) = \sum_n \text{Frame}_n \cdot \delta(t - t_n)$ | Frame Rendering | Ax-Mech-5 |
| $P(\text{Perceive}|S) = \sigma(S - (T_0 + \alpha[\text{IL-17}]))$ | Immune Gating |
| $\kappa_{body} = \text{GripForce}/\Psi_f$ | Embodiment Anchoring | Ax-Mech-9 |

---

**End of File**

---
