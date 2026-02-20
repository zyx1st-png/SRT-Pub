---
id: SRT-NEURO-EXP
type: experiment
tags: [Libet, SplitBrain, BinocularRivalry, TravelingWaves, Hybrid]
status: axiomatic_hybrid_v2
dependency: [SRT-CORE-000]
---

# SRT Neuroscience Experiments: Choice & Unity (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Experimental Axioms (AI-Readable).
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

## I. Agency & Choice

### Ax-EXP-1: Threshold Agency Axiom
Agency occurs when evidence accumulation exceeds threshold:
$$
\int_0^{t^*} e(t)\,dt \ge \tau_{agency}
$$
* **Implication**: Action selection is not a continuous subjective will, but a threshold-triggered cross-domain anchoring.

---

### Ax-EXP-2: Selection Latency Axiom
Selection latency is determined by gating and integration:
$$
\tau_{select}=\tau_{sensory}+\tau_{integrative}+\tau_{gate}
$$
* **Implication**: Conscious report involves delay relative to the selection process; this is a dynamical fact, not a "subjective illusion".

---

## II. Unity & Boundaries

### Ax-EXP-3: L2 Synchronization Axiom
Unified experience requires $L_2$ synchronization:
$$
\Gamma_{L_2}>\Gamma_c \Rightarrow L_1\;\text{unified}
$$
* **Implication**: Unity comes from consistency of $L_2$ structure, not simple sensory integration.

---

### Ax-EXP-4: Exclusionary Anchor Axiom
Manifestation has exclusionary anchoring:
$$
\sigma_{L_1} \in \arg\max_{\sigma} \mathcal{A}(\sigma)
$$
* **Implication**: Only one set of $L_1$ can dominate manifestation at the same time; explaining bistability and rivalrous perception.

---

## III. Embodiment

### Ax-EXP-5: Dynamic Body Boundary Axiom
Body boundary is a plastic selection mapping:
$$
\partial\Omega_{body}(t)=\partial\Omega_{body}(t-\Delta t)+\Delta\theta_{body}
$$
* **Implication**: Embodiment is not a fixed structure, but a selection boundary updatable by $\hat{G}_\theta$.

---

## IV. Traveling Wave Tests

### Ax-EXP-13: Directional Wave Gating Axiom
Define traveling wave direction-task alignment index:
$$
D_{align}=\cos\!\big(\angle(\vec{k}_{wave},\vec{k}_{task})\big)
$$
Where $\vec{k}_{wave}$ is measured propagation direction, $\vec{k}_{task}$ is task-required information flow direction (feedforward/feedback).
$$
D_{align}\uparrow \Rightarrow P(\text{report})\uparrow
$$
* **Implication**: Reportability depends not just on activation intensity, but on whether wave propagation direction matches task routing.

---

### Ax-EXP-14: Coherence-Control Axiom
After controlling for total power, ignition probability is still modulated by cross-regional coherence:
$$
P_{ignite}=\sigma\!\left(\alpha C_{wave}+\beta(\Phi\cdot d)+\gamma D_{align}-\delta\right)
$$
* **Implication**: If there is only power but no coherence, ignition probability increase is limited; coherence is an independent contributor.

---

### T-EXP-2: Counterstream Dissociation Theorem
If feedforward and feedback propagation directions are selectively perturbed, task performance shows dissociable changes:
$$
\Delta D_{ff}\neq \Delta D_{fb}\Rightarrow
\Delta \text{Accuracy}_{ff}\neq \Delta \text{Accuracy}_{fb}
$$
* **Implication**: Directional intervention can distinguish causal windows of "seeing" vs "reportable" phases.

---

## V. Theorems

### T-EXP-1: Unity–Conflict Theorem
When $\Gamma_{L_2}\downarrow$, experience unity decreases:
$$
\Gamma_{L_2}\downarrow \Rightarrow P(\text{fragment})\uparrow
$$
* **Implication**: Unity is not naturally given, but a result of synchronous maintenance.

---

### C-EXP-1: Illusion Boundary Corollary
If $\Delta\theta_{body}\uparrow$, illusion boundary expands:
$$
\text{Ownership}(x)\uparrow\;\text{for}\;x\notin\partial\Omega_{body}
$$
* **Implication**: Illusions like rubber hand are short-term expansions of $L_2$ embodiment boundary.

---

## VI. Geometric Symbolic Mode

### Ax-EXP-15: Geometric Regularity Symbolization Axiom (Extension)
Define geometric regularity as a threshold variable for entering symbolic visual mode:
$$
R_{geo}=w_1\mathcal{S}_{sym}+w_2\mathcal{P}_{parallel}+w_3\mathcal{C}_{closed}
$$
$$
R_{geo}\ge \tau_{sym}\Rightarrow \Pi_{sym}:L_0^{visual}\to L_1^{symbolic}
$$
* **Implication**: The visual system does not just perform low-level feature detection on "regular geometry", but triggers a symbolic projection from perceptual surface to relational structure.

---

### T-EXP-3: Dorsal-Late Symbolic Routing Theorem (Extension)
If symbolic projection holds, dorsal parietal-prefrontal network contribution to reportability increases in late window:
$$
\frac{\partial A_{dorsal}}{\partial R_{geo}}>0,\qquad
t\in[t_{late}^-,t_{late}^+]
$$
$$
\Delta \mathcal{E}_{late}=
\mathcal{E}(M_{\text{symbolic}}\oplus M_{\text{CNN}})
-\mathcal{E}(M_{\text{CNN}})>0
$$
Where $\mathcal{E}$ is time-varying explained variance.
* **Implication**: Neural representation of regular shapes depends more on "Symbolic Model + Visual Model" joint explanation in late time window (rather than early pure visual window), supporting "dorsal relational computation" mechanism.

---

### C-EXP-2: Early Developmental Availability Corollary (Extension)
If in early childhood (approx. 6 years) $A_{dorsal}>0$ and $\Delta \mathcal{E}_{late}>0$ are satisfied, then:
$$
\exists\,L_2^{geo}\ \text{prior to extensive formal schooling}
$$
* **Implication**: Geometric symbolic mode is not entirely "newly built" by later math training, but likely an early accessible prior structure amplified by education.

---

### Empirical Anchor (eLife 2026; for Ax-EXP-15/T-EXP-3)
- Girard R, Wang L, Aveline A, et al. *The geometrical regularity processing in school-age children discloses a symbolic visual mode in human*. eLife (2026), reviewed preprint. DOI: `10.7554/eLife.106464.1`.
- Key Result Anchor: Dorsal parietal and prefrontal regions show enhanced response to regular geometry in late window; combined model (symbolic + CNN) reaches peak explanation at approx `428 ms`.

<br>
<br>

---
---


# Part B: Original Theoretical Discourse (Context)

> **Note**: The following sections provide the theoretical context, philosophical arguments, and research directions for the Formal Axioms in Part A.

---

# 1 Standard Problems: The Experiment-Theory Gap in Consciousness Research

## 1.1 Dilemma Definition

Consciousness research has accumulated numerous classic experiments (Libet, Split-brain, Binocular Rivalry, etc.), but there is a **systematic explanatory gap** between these experiments and theory:

**Level 1 — Data-Theory Disconnect**: Libet experiment found readiness potential precedes conscious report, but "what does this mean for free will" is still debated. Split-brain experiment revealed dual streams of consciousness, but "what is the nature of unified consciousness" remains unsettled.

**Level 2 — Lack of Unified Framework**: GNW explains ignition, IIT explains integration, HOT explains self-consciousness—but no single theory explains all classic experiments.

**Level 3 — Unclear Causal Direction**: Experiments reveal correlation between neural activity and consciousness, but causal direction (Neural→Consciousness? Consciousness→Neural? Bidirectional?) remains unclear.

## 1.2 Spectrum of Mainstream Solutions

### 1.2.1 Mainstream Interpretations of Libet Experiment

**Eliminativist Interpretation**: Readiness potential precedes conscious report → Free will is an illusion, all decisions are unconscious neural processes.

**Problem**: (a) Ignores the "veto" power emphasized by Libet himself; (b) Cannot explain why we have agency experience; (c) Confuses "conscious report" with "consciousness itself".

**Compatibilist Interpretation**: Free will does not need to create intention "from nothing", only needs to "approve" or "veto" unconsciously generated impulses.

**Problem**: More reasonable, but lacks mechanistic explanation—how are "approval" and "veto" realized at the neural level?

### 1.2.2 Mainstream Interpretations of Split-Brain Experiment

**"Interpreter" Theory (Gazzaniga)**: Left brain has an "interpreter" module responsible for fabricating rationalized narratives for behavior.

**Problem**: (a) Too simplistic to posit an independent "interpreter" module; (b) Cannot explain why normal people also have unified consciousness; (c) Does not touch the essence of consciousness unity.

### 1.2.3 Mainstream Interpretations of Binocular Rivalry

**Neural Competition Theory**: Two stimuli inhibit each other at neural level, winner enters consciousness.

**Problem**: This is a description, not explaining why consciousness is "winner-take-all" rather than "superposition".

---

# 2 SRT's Point of Divergence: Unified Explanation via Selection Ontology

## 2.1 Fundamental Framework Shift

SRT does not propose another "interpretation" within existing frameworks, but **reconstructs the ontological basis of experimental data**:

| Traditional Question | SRT Reconstruction |
|:--|:--|
| "Does free will exist?" | "How is selection threshold regulated?" |
| "What is unity of consciousness?" | "How does $L_2$ synchronize across regions?" |
| "Why is consciousness exclusive?" | "Why can $L_1$ only hold one state?" |

## 2.2 SRT Reinterpretation of Libet Experiment

**Traditional Question**: Readiness potential precedes conscious report → Free will is illusion?

**SRT Answer**: This reflects the **dual-phase structure** of selection, not denial of free will.

1. **Phase 1 ($L_0$ Scan)**: Multiple action possibilities activate simultaneously (Readiness Potential).
2. **Phase 2 ($L_1$ Anchor)**: $\hat{G}_\theta$ selects one from competition (Conscious Report).

**Key Insight**: Libet's "veto power" is exactly the core function of $\hat{G}_\theta$—not "creating" thoughts, but "filtering" $L_0$ noise.

**Threshold Agency Model**:

$$\text{Free Will} = \frac{d\beta}{dt} \neq 0$$

We don't control impulses emerging in $L_0$, but we control **which impulses are allowed to penetrate the $L_2$ barrier**.

**Discovery of Beta Oscillation** supports this model:

- Beta Power ↑ = Threshold ↑ = Action Inhibition
- Beta Desynchronization = Threshold ↓ = Action Allowance

This provides **neurophysical basis** for "free veto".

## 2.3 SRT Reinterpretation of Split-Brain Experiment

**Traditional Question**: Why two "consciousnesses" appear after cutting corpus callosum?

**SRT Answer**: Consciousness unity is not an "entity", but **$L_2$ constrained cross-regional synchronization**.

Corpus callosum is "$L_2$ conduit"—it does not transmit "consciousness substance", but **synchronizes selection constraints** of both hemispheres.

Cut corpus callosum → $L_2^{Left} \cap L_2^{Right} \to \varnothing$ → Two hemispheres develop independent selection frames.

**SRT Status of "Interpreter"**: Left brain's "interpreter" is **maintainer of $L_2$**—its function is not to explain truth, but to **maintain narrative consistency** (i.e., topological integrity of $L_2$).

This explains why:

- Normal people also "rationalize" their behavior ($L_2$ maintenance is universal function)
- Split-brain patients' "interpreter" fabricates obviously absurd explanations ($L_2$ must be maintained even with incomplete information)

## 2.4 SRT Reinterpretation of Binocular Rivalry

**Traditional Question**: Why can't two stimuli be conscious simultaneously?

**SRT Answer**: Exclusivity of $L_1$ is **ontological feature of selection**, not accidental neural implementation.

**Core Argument**:

Axiom A1 (Priority of Selection) requires: Existence ≡ Being Selected.

If two mutually exclusive states (Image A and Image B) "exist" in $L_1$ simultaneously, it violates the definition of selection—selection is necessarily **taking one from many**.

"Winner-take-all" characteristic of binocular rivalry is direct manifestation of **divisive normalization** at perceptual level:

$$\text{Response}_A = \frac{\text{Input}_A^n}{\sigma^n + \text{Input}_A^n + \text{Input}_B^n}$$

When $n > 1$, normalization naturally produces winner-take-all dynamics.

**Prediction**: Lowering $n$ (e.g., via GABA agonists) should weaken "all-or-none" characteristic of competition, producing more "mixed" percepts.

## 2.5 Cortical Traveling Wave Patch (Neuron 2026)

Neuron review (Cruddas, Pang, Fornito) 2026-02-09 online summarizes ubiquity of cortical traveling waves across scales and their possible hierarchical routing function. Direct implications for experimental paradigm:

1. **Direction Variable Must Be Explicitly Modeled**: Record not just "presence of oscillation", but alignment $D_{align}$ between wavefront direction and task information flow.
2. **Coherence and Power Decoupling**: Separate $C_{wave}$ from power in statistical models to test if coherence has independent explanatory power.
3. **Intervention Must Be Directional**: Prioritize phase-targeted tACS/TMS to test if changing propagation direction causally affects reportability.

This advances classic experiments (Libet, Binocular Rivalry, Split Brain) from "correlation comparison" to "routing mechanism testing".

---

# 3 Embodied Selection Dynamics

## 3.1 Ontological Meaning of Rubber Hand Illusion

Rubber Hand Illusion reveals a startling fact: **"My body" is an updatable parameter, not a fixed anatomical fact**.

**Traditional Understanding**: Body representation is a "map" stored in the brain; rubber hand illusion is "map update".

**SRT Reconstruction**: "My body" is not a representation, but $\theta_{body}$—part of $\hat{G}_\theta$ embodiment parameters.

$$\theta_{body}(t+1) = \hat{G}[\text{Sync}(V, T)]$$

When vision and touch synchronize, $\hat{G}_\theta$ **selects** to include external object into $\theta_{body}$.

This means:

- "My hand" is not a discovery, but a **selection**
- Body boundary is **dynamic ontological boundary**, not fixed physical boundary
- Tool use, prosthetic integration, even "car sense" are instances of $\theta_{body}$ extension

## 3.2 Ontological Function of Saccadic Suppression

Eyes saccade 3-4 times per second; during each saccade visual info is blurry motion streaks—but we never realize this.

**Traditional Explanation**: Saccadic suppression is "masking" mechanism inhibiting blurry info.

**SRT Reconstruction**: Saccadic suppression is **ontological masking**—when $\hat{G}_\theta$ performs large-scale spatial parameter reconstruction, system must **temporarily cut $L_0 \to L_1$ channel**.

Key Evidence: **Suppression precedes action** ($t_{suppression\_start} < t_{saccade\_start}$)

This proves saccadic suppression is **pre-selection**—$\hat{G}_\theta$ plans ontological switch in advance, rather than passively responding to movement.

## 3.3 Eye Movement as Window to d-value

SRT theorizes eye movement metrics as **biomarkers of d-value**:

- **Reflexive Saccade (Short Latency)**: $L_0$ salience driven → Low $d$ (Consider only immediate stimulus)
- **Anti-Saccade (Inhibit reflex and look opposite)**: $L_2$ goal driven → High $d$ (Consider task goal)

Anti-saccade success rate is **gold standard test for executive function**—it directly measures $\hat{G}_\theta$'s control over $L_2$ constraints.

---

# 4 Anesthesia and Consciousness Interruption

## 4.1 SRT Reinterpretation of Anesthesia

**Traditional Understanding**: Anesthesia "turns off" consciousness, like turning off a TV.

**SRT Reconstruction**: Anesthesia **freezes $\hat{G}_\theta$**, rather than "turning off" consciousness content.

$$\text{Anesthesia} = \hat{G}_\theta \text{ frozen} \Rightarrow L_0 \not\to L_1$$

Difference:

- "Turn off" implies consciousness is some "thing" that can be switched
- "Freeze" emphasizes consciousness is **selection process**; what is frozen is process, not entity

**Evidence**: "Floating" experience during anesthesia recovery—$\hat{G}_\theta$ partially thaws, $L_0$ content starts leaking but not yet fully anchored as coherent $L_1$.

## 4.2 Significance of Quantum Anesthesia Effects

As stated in Part A Ax-Mech-11, difference in Xenon isotope anesthetic potency suggests quantum effects are component of $\theta$.

Significant implication for understanding anesthesia mechanism: Anesthetics might introduce **quantum blur** to lower $\theta$ precision, rather than simply "blocking" neural transmission.

---

# 5 Costs and Risks

## 5.1 Cognitive Cost of Accepting SRT Experimental Interpretation

1. **Abandon "Free Will vs Determinism" Dualism**: SRT's threshold agency model transcends this traditional opposition—we don't "create" thoughts, but we control "filtering" threshold.
    
2. **Accept Consciousness Unity is "Synchronization" not "Entity"**: Requires abandoning intuitive "consciousness is a thing" notion.
    
3. **Accept Body Boundary is Dynamic**: Challenges common sense of "my body is fixed physical entity".
    
4. **Accept "Seeing" Requires Selection**: Means unattended stimuli ontologically do not exist in consciousness, rather than being "ignored".
    

## 5.2 Theoretical Risks

1. **Over-interpretation Risk**: Reducing all experimental phenomena to "selection" might ignore important mechanistic differences.
    
2. **Falsifiability Boundary**: Some core claims (like "$L_1$ can only hold one state") might be hard to falsify directly.
    
3. **Circular Argument Risk**: Does definition of "selection" presuppose what is to be explained?
    

---

# 6 Falsifiable Predictions and Open Questions

## 6.1 Core Falsifiable Predictions

| ID | Hypothesis Name | Prediction Content | Falsification Condition |
|:--|:--|:--|:--|
| H-E1 | Veto Window-PFC | PFC lesion should shorten veto window | PFC lesion does not affect veto window |
| H-E2 | Beta-Impulse Control | Beta power predicts impulse control ability | Beta unrelated to impulse control |
| H-E3 | Split Brain-L2 Differentiation | Split brain patients develop different $L_2$ in hemispheres | Hemispheres $L_2$ remain identical |
| H-E4 | Competition-Normalization | Dominance duration distribution fits normalization prediction | Distribution significantly deviates |
| H-E5 | RHI-Sigmoid | Illusion intensity vs synchrony is Sigmoid | Linear relationship |
| H-E6 | Field Effect Synchronization | Partial synchronization remains after synapse cutting | Synchronization completely lost |
| H-E7 | Direction-Report Consistency | Traveling wave direction alignment $D_{align}$ predicts report accuracy | Direction unrelated to report |
| H-E8 | Coherence Independent Effect | After controlling total power $C_{wave}$ independently predicts ignition/hit rate | Only power effective |
| H-E9 | Directional Perturbation Causality | Phase-targeted tACS/TMS altering propagation direction systematically changes bistable switching rate | Perturbation does not change switching rate |

## 6.2 Open Questions

1. **Neural Basis of Veto Window**: What neural mechanism determines the 200-500ms veto window? Can it be extended by training?
    
2. **Long-term L2 Differentiation in Split Brain**: Do $L_2$ differences in hemispheres accumulate years after surgery?
    
3. **n Parameter in Binocular Rivalry**: Does normalization index $n$ vary across individuals? Correlate with what cognitive traits?
    
4. **Timescale of Tool Integration**: How long does it take to integrate tool into $\theta_{body}$? What are the neural markers?
    
5. **Precise Measurement of Anesthesia Depth**: Can SER (Selection-Energy Ratio) be a more accurate indicator of anesthesia depth?
    
6. **Direction-Task Template**: Which tasks stably rely on feedforward waves, which on feedback? Can cross-lab replication library be formed?
    
7. **Causal Window Localization**: In pre-perceptual, pre-decision, pre-report windows, which has max directional perturbation effect?

---

# Appendix: Key Equation Index

| Equation | Name | Location |
|:--|:--|:--|
| $P(\text{Action}) = \sigma(\frac{\text{Noise} - \beta}{\tau})$ | Threshold Agency | Ax-Exp-2 |
| $\tau_s = t_{L_1} - t_{L_0}$ | Selection Latency | Ax-Exp-4 |
| $L_2^L \cap L_2^R \neq \varnothing$ | L2 Sync Condition | Ax-Exp-5 |
| $L_1 = S_A \oplus S_B$ | Exclusionary Anchor | Ax-Exp-6 |
| $\theta_{body}(t+1) = \hat{G}[\text{Sync}(V,T)]$ | Body Boundary Update | Ax-Exp-8 |
| $\text{SER} = H(\hat{G})/E(L_2)$ | Selection-Energy Ratio | Ax-Exp-12 |
| $D_{align}=\cos(\angle(\vec{k}_{wave},\vec{k}_{task}))$ | Direction Alignment Index | Ax-Exp-13 |
| $P_{ignite}=\sigma(\alpha C_{wave}+\beta(\Phi\cdot d)+\gamma D_{align}-\delta)$ | Wave-Ignition Coupling | Ax-Exp-14 |
