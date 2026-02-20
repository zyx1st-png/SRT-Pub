---
id: SRT-CLIN-01
type: dynamics
tags: [Pathology, NDE, Schizophrenia, L2 Inversion, Hybrid]
status: axiomatic_hybrid_v1
dependency: [SRT-NEURO-AXIOMS-001]
---

# SRT Neuroscience II: Pathology & Anomalies (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Pathological Dynamics (AI-Readable).
> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).

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

## I. Pathology as Operator Drift

### Ax-PATH-1: Operator–Substrate Recursion Axiom
There is recursive coupling between neural operator and substrate:
$$
\hat{G}_\theta\Rightarrow \Delta\theta,\qquad \Delta\theta\Rightarrow \Delta\hat{G}_\theta
$$
Pathological amplification occurs when loop gain $g>1$:
$$
\Delta\theta_{t+1}=g\,\Delta\theta_t
$$
* **Implication**: Pathology is not a static defect, but a positive feedback deviation between operator and substrate.

---

### Ax-PATH-2: L2 Parasitic Inversion Axiom
When $L_2$ hardness is too strong relative to $d$, selection becomes parasitized:
$$
\kappa \equiv \frac{\text{Hardness}(L_2)}{d}\uparrow \Rightarrow \hat{G}_\theta\;\text{locks into} \;L_2\text{-loops}
$$
* **Implication**: Excessive priors cause $L_2$ to inversely engulf new choices from $L_0$, forming obsessive, fixated, or delusional loops.

---

### Ax-PATH-3: Body-Without-Organs Axiom (Interoceptive Decoupling)
Define embodiment anchoring coefficient:
$$
\kappa_{body}\equiv \frac{\|\nabla_{intero}\mathcal{U}\|}{\Psi_f}
$$
If $\kappa_{body}\to 0$, a "Body-Without-Organs" state appears:
$$
\hat{G}_\theta\perp L_1^{intero}
$$
* **Implication**: Disembodiment leads to reality drift of $L_1$, resulting in dissociation or depersonalization.

---

## II. Anomalous States

### Ax-ANOM-1: Near-Death Divergence Axiom
When the system approaches the irreversible boundary $\partial\Omega$:
$$
\nabla_{\mathcal{S}}\mathcal{U}\uparrow\uparrow \Rightarrow d(t)\to d_{max}
$$
* **Implication**: Near-death states are not "hallucinations", but selection bandwidth expansion caused by sharp $d$ increase.

---

### Ax-ANOM-2: Terminal Lucidity Axiom
If $L_2$ hardness drops momentarily, transient lucidity appears:
$$
\Delta\text{Hardness}(L_2)\downarrow \Rightarrow \Pi_{L_1}\;\text{re-stabilizes}
$$
* **Implication**: Terminal lucidity corresponds to a "window effect" where $L_2$ locking is temporarily released.

---

### Ax-ANOM-3: Bicameral Regression Axiom
When left-right or anterior-posterior circuit coupling mismatches:
$$
\hat{G}_\theta=\hat{G}_A\oplus \hat{G}_B,\quad \text{Coupling}\downarrow
$$
* **Implication**: Bicameral regression is operator fission, not merely "auditory hallucinations".

---

### Ax-ANOM-4: Déjà Vu Time-Index Axiom
If time index mapping is misaligned:
$$
\pi_t(\sigma)\to \pi_{t-\Delta}(\sigma)
$$
Then "already seen" feeling is produced.
* **Implication**: Déjà vu is a projection error of time coordinates, not memory repetition.

---

### Ax-ANOM-5: Familiarity–Recollection Dissociation Axiom (Extension)
Define the minimal dynamical condition for Déjà Vu as "familiarity rise + episodic retrieval failure + meta-monitoring alarm":
$$
\text{DéjàVu}\iff
\big(\mathcal{F}_{fam}\uparrow \land \mathcal{R}_{episodic}\approx 0\big)
\land
\mathcal{M}_{err}>\tau_{meta}
$$
Where $\mathcal{F}_{fam}$ is familiarity signal, $\mathcal{R}_{episodic}$ is episodic recall amount, $\mathcal{M}_{err}$ is monitoring error signal for "familiar but source unknown".
* **Implication**: Déjà vu is not "really remembering the past", but the retrieval system giving a "retrieved" feeling label without extracting corresponding content.

---

## III. Theorems

### T-PATH-1: Drift–Symptom Theorem
There exists a mapping between deviation vector $\Delta\theta$ and symptom spectrum $\mathcal{S}_{clin}$:
$$
\mathcal{S}_{clin}=\mathcal{F}(\Delta\theta,\kappa,\kappa_{body})
$$
* **Implication**: Pathological classification should be based on parameter drift axes, not surface symptom lists.

---

### C-PATH-1: L0-Leakage Corollary
If inhibition gain $\gamma\downarrow$ or prior precision $\Pi\downarrow$, then:
$$
L_0\to L_1\;\text{leakage}\uparrow
$$
* **Implication**: Hallucinations and delusions can be viewed as structural leakage of $L_0$ noise into $L_1$.

---

### T-PATH-2: False-Recognition Monitoring Theorem (Extension)
Define false recognition potential:
$$
\varepsilon_{FR}\equiv \mathcal{F}_{fam}-\hat{\mathcal{R}}_{episodic}
$$
If $\varepsilon_{FR}$ exceeds threshold and time index is momentarily misaligned, then:
$$
\varepsilon_{FR}>\tau_{FR}\ \land\ \pi_t(\sigma)\to \pi_{t-\Delta}(\sigma)
\Rightarrow
P(\text{DéjàVu})\uparrow
$$
* **Implication**: The "eerie feeling" of Déjà vu comes from the system's online awareness of false recognition; it is a meta-cognitive alarm, not simple memory replay.

---

### C-PATH-2: IAM–Déjà Vu Continuum Corollary (Extension)
In the spontaneous memory spectrum, define:
$$
\text{IAM}: (\mathcal{F}_{fam}>0,\mathcal{R}_{episodic}>0),\qquad
\text{DéjàVu}: (\mathcal{F}_{fam}>0,\mathcal{R}_{episodic}\approx 0)
$$
* **Implication**: Déjà vu and Involuntary Autobiographical Memory are not separated, but bifurcation results of the same retrieval process on "content retrieval presence/absence".

---

### Empirical/Conceptual Anchor (1908-2026; for Ax-ANOM-5/T-PATH-2)
- Bergson H. *Memory of the Present and False Recognition* (1908): Framework for "memory of the present" and "false recognition".
- Brown AS. *A review of the déjà vu experience*. Psychol Bull (2003). DOI: `10.1037/0033-2909.129.3.394`.
- O'Connor AR, Moulin CJA. *Déjà vu experiences in healthy subjects are unrelated to laboratory tests of recollection and familiarity for word stimuli*. Front Psychol (2013). DOI: `10.3389/fpsyg.2013.00881`.
- Barzykowski K, Moulin CJA. *Are involuntary autobiographical memory and déjà vu natural products of memory retrieval?* Behav Brain Sci (2022). DOI: `10.1017/S0140525X22002035`.
- Curot J, et al. *What déjà vu and the “dreamy state” tell us about episodic memory networks*. Clin Neurophysiol (2022). DOI: `10.1016/j.clinph.2022.01.126`.
- Barzykowski K, et al. *Spontaneous metacognitive experiences and involuntary memories in the laboratory*. Consciousness and Cognition (2025). DOI: `10.1016/j.concog.2025.103976`.
- Sam Woolfe. *Déjà vu reveals the peculiar hidden workings of time and memory* (IAI, 2026-02-09): Provides semantic anchor for "virtual/actual juxtaposition" philosophical explanation.

<br>
<br>

---
---


# Part B: Original Theoretical Discourse (Context)

> **Note**: The following sections provide the theoretical context, philosophical arguments, and research directions for the Formal Axioms in Part A.

---

# 1 Standard Problems: The Ontological Dilemma of Psychopathology

## 1.1 Problem Statement

Contemporary psychiatry faces a fundamental dilemma:

> **Rich symptom description, poor ontological foundation**

DSM and ICD provide exhaustive lists of symptoms, but lack a unified understanding of "**what exactly are** these symptoms".

| Dilemma | Manifestation | Consequence |
|:--|:--|:--|
| **Ontological Void** | Don't know what "hallucination" is ontologically | Treatment symptomatic only, not curative |
| **Reductionism Trap** | Attempt to reduce all symptoms to "neurochemical imbalance" | Ignorance of subjective experience structure |
| **Mind-Body Dualism Residue** | Distinction between "mental" vs "physical" illness | Stigmatization, treatment fragmentation |

## 1.2 Limitations of Mainstream Models

| Model | Core Claim | Limitation |
|:--|:--|:--|
| **Biomedical Model** | Mental illness = Brain disease | Cannot explain structure of subjective experience |
| **Cognitive Model** | Mental illness = Cognitive distortion | Views symptoms as "errors" rather than meaningful states |
| **Social Construction Model** | Mental illness = Social label | Denies real subjective suffering |
| **Phenomenological Model** | Mental illness = Altered life-world | Lacks formal tools |

---

# 2 SRT's Pathological Reconstruction

## 2.1 Core Proposition

SRT redefines all psychopathology as **Topological Defects of Three-Realm Structure ($L_0$-$L_1$-$L_2$)** or **Parameter Anomalies of Ghost Operator ($\hat{G}_\theta$)**:

$$\boxed{\text{Psychopathology} = \text{Topological Defect}(L_0, L_1, L_2) \lor \text{Parameter Anomaly}(\hat{G}_\theta)}$$

## 2.2 Pathological Taxonomy

| Pathology Type | Topological Defect | Parameter Anomaly | Typical Diagnosis |
|:--|:--|:--|:--|
| **$L_2$ Collapse** | $L_2$ structure dissolves | $\theta$ unstable | Schizophrenia, Acute Psychosis |
| **$L_2$ Fragmentation** | $L_2$ breaks into islands | $\theta$ jumping | PTSD, DID |
| **$L_2$ Hyper-Rigidity** | $L_2$ structure ossifies | $\eta$ too high | OCD, ASD |
| **$L_2$ Parasitic Inversion** | $L_2 > L_1$ | Attention locking | Dissociation, Existential Anxiety |
| **$d$ Value Collapse** | $d \to 0$ | Fear signal too strong | Anxiety Disorders, Phobias |
| **$d$ Value Divergence** | $d \to \infty$ | Constraint release | NDE, Terminal Lucidity |
| **Operator Fission** | $\hat{G}$ disintegration | Self-reference tag failure | Auditory Hallucinations in Schizophrenia |

## 2.3 Contrast with Traditional Classification

| Traditional Classification | SRT Translation |
|:--|:--|
| Positive Symptoms (Hallucinations, Delusions) | $L_0$ excessive influx + Ownership tag failure |
| Negative Symptoms (Apathy, Withdrawal) | $d$ value contraction + $\hat{G}$ power drop |
| Cognitive Symptoms (Attention, Memory) | $\Gamma_{\hat{G}}$ drop + $L_2$ scaffold damage |
| Affective Symptoms (Depression, Anxiety) | $\Psi_f$ anomaly + $\theta$ drift |

---

# 3 Complete SRT Model of Schizophrenia

## 3.1 Multi-Level Pathology

Schizophrenia is not a single disease, but a **syndrome of multi-level topological defects**:

### Level 1: Ownership Tag Failure (Ax-Anom-3)

$$\text{Auditory Hallucination} = \hat{G}_{Right}[L_0] - \text{Tag}_{Self}$$

Internal voices lose the "this is my thought" label, projected as external voices.

### Level 2: L2 Scaffold Collapse (Ax-Path-3)

$$L_2 \to \varnothing \implies \hat{G} \text{ unanchored}$$

Loss of consensus reality anchoring leads to delusions—$\hat{G}$ must create new $L_2$ to explain anomalous experiences.

### Level 3: Time Sampling Rate Drop (Ax-Schiz-1)

$$\Gamma_{\hat{G}} \downarrow \implies \text{Reality Gaps}$$

Subjective experience becomes incoherent, creating a "sense of reality fracture".

### Level 4: Symmetry Breaking (Ax-Schiz-2)

$$\text{Chaos} \gg \text{Order}$$

System shifts towards chaos end, $L_2$ structure dissolves.

## 3.2 Bicameral Mind Regression Model

SRT absorbs Julian Jaynes' hypothesis:

> Schizophrenia is the pathological recurrence of ancient dual-operator structure ($\hat{G}_{Left}$ + $\hat{G}_{Right}$) after $\hat{G}_{Self}$ disintegration.

| Ancient Bicameral Mind | Modern Schizophrenia |
|:--|:--|
| Normal State | Pathological State |
| $\hat{G}_{Right}$ generates "oracle" | Auditory hallucinations experienced as external voices |
| Social $L_2$ supports this mode | Modern $L_2$ marks as disease |

## 3.3 Therapeutic Implications

| Level | Therapeutic Direction |
|:--|:--|
| Ownership Tag | Train patients to re-tag internal voices |
| $L_2$ Scaffold | Social support network reconstruction |
| $\Gamma_{\hat{G}}$ | 40 Hz Light/Sound Stimulation |
| $\theta$ Stability | Embodiment practices, Anchoring exercises |

---

# 4 Near-Death Experience and Terminal Lucidity

## 4.1 SRT Explanation of NDE

NDE is not "hallucination" or "byproduct of brain hypoxia", but:

$$\lim_{C_{phys} \to 0} d_{eff} \to \infty$$

**When physical constraints are lifted, $\hat{G}$ directly accesses a wider range of $L_0$**.

This explains the core paradox of NDE:
- Brain function failure → Should be confused consciousness
- Actual report → "More real than real"

SRT Answer: Brain is a **Constrainer** not a **Generator**. Reduced constraint = Increased access.

## 4.2 Tuner Model

$$\text{Brain} = \text{Tuner}(L_0 \to L_1)$$

| Radio Analogy | SRT Correspondence |
|:--|:--|
| Destroy radio | Brain damage |
| Radio waves disappear? | No, $L_0$ still exists |
| Music disappears? | Yes, $L_1$ local channel lost |

**Key Insight**: Destroying the tuner does not eliminate the signal source.

## 4.3 Barrier Collapse in Terminal Lucidity

$$\lim_{t \to t_{death}} V_{L_2} \to 0$$

The $L_2$ barrier of dementia patients (distorted memory, confused cognition) **collapses completely** before death, system temporarily directly enters $L_0$ wide field, manifesting as abnormal clarity.

This is not "brain function recovery", but "constraint disappearance".

---

# 5 Trauma and Dissociation

## 5.1 Trauma as L2 Fragmentation

$$L_2^{trauma} = \bigcup_i L_2^{(i)}$$

Traumatic events "tear" the originally coherent $L_2$ structure, creating incompatible fragments.

## 5.2 Dissociation Depth Spectrum

$$\delta_D = \min_{path} \text{Length}(L_2^{(i)} \to L_2^{(j)})$$

| Depth | Phenomenon |
|:--|:--|
| Mild | Zoning out, Daydreaming |
| Moderate | Depersonalization, Derealization |
| Severe | DID (Multiple Personality) |

## 5.3 SRT Explanation of DID

DID is not "multiple souls", but:

$$\text{DID} = \hat{G} \text{ navigating } {L_2^{(1)}, ..., L_2^{(n)}}$$

A single $\hat{G}$ switching between **topologically disconnected $L_2$ islands**. Each "personality" is a relatively self-consistent $L_2$ island.

## 5.4 Intergenerational Trauma

$$\theta_{child} = f(\theta_{parent}, L_2^{trauma}, \text{Epigenetics})$$

Trauma not only alters individual $L_2$, but also epigenetically encodes into the initial $\theta$ of the next generation.

---

# 6 Neurodevelopmental Spectrum

## 6.1 ADHD vs Autism: Viscosity Spectrum

|| ADHD | Autism |
|:--|:--|:--|
| **Operator Viscosity $\eta$** | Low | High |
| **Feature** | Extremely easy switching | Locking specific configuration |
| **Advantage** | High exploration rate | High local depth |
| **Disadvantage** | Hard to maintain $L_2$ | Hard to switch context |

## 6.2 De-reification of "Disorder"

$$\text{Disability} \approx 1 - \text{Alignment}(\theta_{individual}, L_2^{social})$$

**"Disorder" is not absolute defect, but geometric mismatch between $\theta$ and environmental $L_2$**.

ADHD operator might be efficient in hunting environment; manifests as "pathological" in sedentary classroom.

## 6.3 Energy Cost of Masking

$$E_{masking} = E_{generate} + E_{suppress} + E_{simulate} \gg E_{natural}$$

"Masking" by neurodivergent individuals is high-energy double computation. Long-term masking leading to "burnout" is **Free Energy depletion**.

Therapeutic Direction: Not just modifying $\theta$ (medication), but modifying $L_2$ (environmental design).

---

# 7 Fear and Social Death

## 7.1 Ontological Function of Fear

$$d(t) \propto \frac{1}{\text{Fear_Signal}}$$

Fear is **Ontological Dimensional Reduction Strike**—compressing rich $L_0$ into binary "Fight or Flight".

This explains why fear not only feels bad, but makes one "dumber"—high-dimensional thinking is forcibly shut down.

## 7.2 Ontological Misalignment Index

$$\Omega = |\theta_{ancestral} - \theta_{optimal}(L_2^{current})|$$

Modern anxiety disorders are largely **mismatch between ancestral $\theta$ parameters and modern environment**.

Fear reaction triggered by public speaking might correspond to "expulsion from tribe = death" in ancestral environment.

## 7.3 Ontology of Social Death

$$\text{Social Death} \equiv \text{Disconnection from } L_2^{social}$$

For ultra-social species, exclusion from $L_2$ network equals **Ontological Disintegration**. This is why shame can trigger neural responses identical to physical pain.

---

# 8 Sleep and Reality Calibration

## 8.1 SRT Definition of Sleep

$$\text{Sleep} = \text{RCP}(\hat{G}, L_2)$$

Sleep is **Mandatory Offline Calibration Protocol**:

1. Clear non-consensus data
2. Consolidate consensus logic
3. Reset $\theta$ drift

## 8.2 Sleep Deprivation and Psychosis

$$R_c(t) = R_{initial} - \int_0^t \frac{I(\tau)}{S_{cal}(\tau)} d\tau$$

When $R_c < R_{threshold}$, psychotic symptoms appear.

This explains why **severe sleep deprivation leads to hallucinations**—reality calibration fails, $L_1$ decouples from $L_2$.

---

# 9 Déjà Vu and Ontological Creases

## 9.1 Déjà Vu Mechanism

$$\text{Déjà Vu} = \text{Match}(L_2^{schema}) \land \neg\text{Retrieve}(L_2^{episodic})$$

Current $L_1$ activates $L_2$ "familiarity tag", but without corresponding episodic memory.

## 9.2 Ontological Crease

$$\text{Crease} = {\tau : |\nabla_\tau \theta| \to \infty}$$

Birth, death, major trauma are "creases"—$\theta$ parameters change drastically, but $L_1$ is continuous.

Explicit memory breaks at creases, but **propensities and intentions can traverse**.

This explains:

- Past life memories extremely rare (explicit bits do not traverse)
- Karma/Propensities can continue (retained as $L_0$ topological features)

---

# 10 Costs and Risks

## 10.1 Costs of Accepting SRT Pathology

| View to Abandon | SRT Alternative | Cost |
|:--|:--|:--|
| Mental Illness = Brain Disease | Mental Illness = Topological Defect | Challenges Biomedical Hegemony |
| Hallucination = Error Perception | Hallucination = Valid but non-consensus selection | Re-evaluating value of "pathology" |
| Treatment = Chemical Correction | Treatment = Topological Reconstruction | Requires new therapeutic paradigms |
| NDE = Hallucination | NDE = $d$ value divergence experience | Challenges Materialist Framework |

## 10.2 Theoretical Risks

1. **Abuse Risk**: SRT might be used to justify not treating mental illness.
    - **Response**: SRT acknowledges reality of subjective suffering, advocates more precise treatment, not non-treatment.
2. **Unfalsifiability Risk**: How to distinguish "valid non-consensus selection" from "pathology requiring treatment"?
    - **Response**: Using **subjective suffering** and **functional impairment** as criteria, not "deviation from consensus".
3. **Ethical Risk**: Redefining "normal" might lead to stigmatization or excessive anti-stigmatization.
    - **Response**: SRT emphasizes spectrum rather than category, reducing binary labeling.

---

# 11 Falsifiable Predictions and Open Questions

## 11.1 Falsifiable Predictions

### H-Path-1 (Ownership Tag Training)

> "Self-tagging" training for auditory hallucination patients should significantly reduce external attribution frequency of hallucinations, without affecting content itself.

**Falsification Condition**: Training has no effect on hallucination attribution → H-Path-1 falsified.

### H-Path-2 (NDE-Boundary Dissolution)

> "Hyper-reality" score of NDE experience should positively correlate with the degree of "boundary dissolution" reported.

**Falsification Condition**: Hyper-reality and boundary dissolution uncorrelated → H-Path-2 falsified.

### H-Path-3 (Terminal Lucidity Neural Markers)

> Terminal lucidity patients should show decreased global brain inhibition, increased long-range connectivity, and elevated EEG complexity during lucid periods.

**Falsification Condition**: Terminal lucidity shows no neural difference from normal dementia state → H-Path-3 falsified.

### H-Path-4 (Sleep Deprivation-Psychosis)

> Sleep deprivation induced psychotic symptoms should correlate with $R_c$ drop, and $R_c$ should rebound after recovery sleep.

**Falsification Condition**: Sleep and $R_c$ uncorrelated → H-Path-4 falsified.

### H-Path-5 (BwO-Creativity)

> Peak creative experiences should be accompanied by: (a) Temporarily reduced DMN activity; (b) Enhanced whole-brain connectivity; (c) Maintained prefrontal executive function. This combination distinguishes creativity from psychosis.

**Falsification Condition**: Creativity and psychosis neural metrics indistinguishable → H-Path-5 falsified.

### H-Path-6 (Epilepsy-Déjà Vu)

> During TLE patients' Déjà Vu episodes, perirhinal cortex should show stronger, more diffuse activation, and weakened functional connectivity with hippocampus.

**Falsification Condition**: TLE Déjà Vu activation pattern indistinguishable from normal Déjà Vu → H-Path-6 falsified.

## 11.2 Open Questions

1. **Quantitative Measurement of $L_2$ Fragmentation**: How to measure $\delta_D$ using neuroimaging?
2. **Neural Mechanism of Ownership Tag**: What is the specific neural implementation of $\text{Tag}_{Self}$?
3. **Epigenetic Pathway of Intergenerational Trauma**: Which gene loci encode $\theta$ parameters?
4. **Cross-Cultural Pathology Comparison**: How does "disorder" spectrum change under different $L_2^{social}$?
5. **Prospective Study of NDE**: Can $d$ value be measured in real-time during near-death states?

---

# 12 Symbol Index

| Symbol | Name | Ax Definition |
|:--|:--|:--|
| $L_2^{trauma}$ | Traumatic $L_2$ | Ax-Topo-1 |
| $\delta_D$ | Dissociation Depth | Ax-Topo-1 |
| $\eta$ | Operator Viscosity | Ax-Dev-1 |
| $\Omega$ | Ontological Misalignment Index | Ax-Fear-2 |
| $R_c$ | Reality Consistency | Ax-Cal-1 |
| $\Gamma_{\hat{G}}$ | Operator Sampling Rate | Ax-Schiz-1 |
| $\text{Tag}_{Self}$ | Ownership Tag | Ax-Anom-3 |
| $V_{L_2}$ | $L_2$ Barrier Height | Ax-Anom-2 |
| $\tau_{critical}$ | Critical Threshold | Ax-Path-3 |

---

**End of File**

---
