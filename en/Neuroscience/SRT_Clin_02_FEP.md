---
id: SRT-CLIN-02
type: theory
tags: [Friston, Free Energy, Autopoiesis, Biosemiotics, Hybrid]
status: axiomatic_hybrid_v1
dependency: [SRT-CORE-000, SRT-NEURO-MECH-001]
---

# SRT Clinical Extension I: Free Energy & Autopoiesis (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal FEP Axioms (AI-Readable).
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

## I. Free-Energy as Choice Pressure

### Ax-FEP-1: Choice-Pressure Identity Axiom
Define Free Energy as choice pressure potential:
$$
F\equiv D_{KL}[Q||P]-\ln P(o)
$$
The selection operator uses free energy minimization as its dynamics:
$$
\hat{G}_\theta=\arg\min_{\pi}\;\mathbb{E}[F(\pi)]
$$
* **Implication**: Free energy is not an "error metric", but the dynamical potential for $\hat{G}_\theta$ selection.

---

### Ax-FEP-2: Active Inference Axiom
Action selection minimizes expected free energy:
$$
\pi^*=\arg\min_{\pi}\;\mathbb{E}[F_{future}(\pi)]
$$
* **Implication**: Active inference is a constrained strategy for $L_0$ exploration, not passive prediction.

---

## II. Autopoiesis & L2 Closure

### Ax-AUTO-1: Autopoietic Closure Axiom
Autopoietic systems satisfy structural closure:
$$
L_2(t+1)=\text{Stabilize}(\hat{G}_\theta[L_1(t)])
$$
* **Implication**: Life maintenance is not "metabolic description", but structural self-solidification of $L_2$.

---

### Ax-AUTO-2: Semiotic Update Axiom
Semiotic update is structural weighting of $L_2$:
$$
\Delta L_2\propto -\nabla_\theta F
$$
* **Implication**: Meaning is not an added label, but a bias structure of $\hat{G}_\theta$ for future selections.

---

## III. Reality Stability

### Ax-REAL-1: Stability Law
Reality stability is inversely proportional to ontological friction:
$$
\text{Stability}\propto \frac{1}{\Psi_f}
$$
* **Implication**: Highly complex reality is necessarily fragile; stability is not "fixation", but continuous payment of cost.

---

### Ax-REAL-2: Learning Cost Axiom
Learning cost is proportional to parameter update rate:
$$
\text{Cost}_{learn}\propto \left\|\frac{d\theta}{dt}\right\|
$$
* **Implication**: Learning is not "free optimization", but cost-driven selection change.

---

## IV. Theorems

### T-FEP-1: FEP Insufficiency Theorem
If only free energy minimization is satisfied while $d=0$, then:
$$
\hat{G}_\theta\;\text{remains}\;L_1\text{-closed}
$$
* **Implication**: FEP interprets structural updates but does not guarantee manifestation; $d$ must be introduced to cross domains and anchor.

---

### C-FEP-1: Irreversibility Corollary
When irreversible risk $\partial\Omega$ exists:
$$
\nabla_{\mathcal{S}}\mathcal{U}\uparrow \Rightarrow \text{Policy}\;\text{re-weighting}
$$
* **Implication**: Free energy minimization strategies will be re-weighted by survival stakes.

<br>
<br>

---
---


# Part B: Original Theoretical Discourse (Context)

> **Note**: The following sections provide the theoretical context, philosophical arguments, and research directions for the Formal Axioms in Part A. Following the **Minimum Closed Loop** structure.

---

# 1 Standard Problems: Explanatory Boundary of Free Energy Principle and "Dark Room"

## 1.1 "The Dark Room Problem"
The Free Energy Principle (FEP) claims organisms survive by minimizing "Surprise". This leads to the famous **Dark Room Paradox**: If the goal is merely to minimize surprise, the optimal strategy should be to find a completely dark, silent room and predict "I see nothing"—then prediction error is zero, surprise is minimal.

However, life (especially higher intelligence) clearly does not do this. We explore, take risks, create art, and actively seek "novelty". Friston introduced "Expected Free Energy" to patch this loophole, but critics argue it is an "ad hoc fix" lacking first-principles necessity.

## 1.2 Ontological Confusion of Physical and Informational Quantities
In professional contexts, FEP is often criticized for conflating **Information-theoretic Free Energy** ($\ln P$) with **Thermodynamic Free Energy** (Gibbs Free Energy). This confusion makes it difficult to precisely correspond the theory with real biophysical processes (like ATP consumption).

---

# 2 Spectrum of Mainstream Solutions

## 2.1 Expected Free Energy (EFE) Solution
Friston proposes the system minimizes not just current $F$, but future $G$ (Expected Free Energy). $G$ includes "cognitive terms" (exploration/curiosity) to reduce future uncertainty.
- **Evaluation**: Mathematically self-consistent, but introduces teleological color philosophically, and still struggles to explain extreme **altruistic sacrifice** (exchanging existence for unobservable "moral satisfaction").

## 2.2 Autopoiesis Solution
Maturana & Varela argue the essence of life is "self-production", not free energy minimization. The system merely maintains its organization.
- **Evaluation**: Descriptively precise, but lacks predictive power. It cannot calculate what the system will do next.

---

# 3 SRT's Point of Divergence: d-Value Extension and Ontological Reconstruction

## 3.1 The Altruistic Extension of Free Energy
SRT proposes in Part A (Ax-FEP-2) that **Friston's framework is a special case of SRT when $d=0$**.
For conscious systems with $d > 0$, the free energy function is **ontologically extended**:

$$ F_{SRT} = F_{Friston} - d \cdot U_{others} $$

This elegantly solves the "Dark Room Problem":
- For organisms with $d=0$ (bacteria), the dark room is indeed optimal (if food is present).
- For humans with $d>0$, hiding in a dark room means disconnection from others ($U_{others} \to 0$ or negative), causing extended free energy $F_{SRT}$ to **rise sharply**.
- **Conclusion**: We leave the dark room not to find light, but to find connection. This is a thermodynamic necessity.

## 3.2 Predictive Coding Perspective on Psychopathology (Hypothetical Mapping)
SRT adopts the **Precision Weighting** dynamics defined in Ax-FEP-4, offering a potential unified explanation for psychopathology (Note: this remains a hypothesis based on PC framework, not conclusive):

- **Schizophrenia**: Prior precision too high ($\pi_{prior} \uparrow$). Patients ignore sensory input, imposing internal hallucinations onto reality.
- **Autism**: Sensory precision too high ($\pi_{sensory} \uparrow$). Unable to ignore environmental details (leaf movement, wind sound), the system must withdraw to avoid free energy overload.

This explanation has stronger computational explanatory power than traditional neurotransmitter hypotheses.

---

# 4 Costs and Risks (Important)

## 4.1 Risk of Conflation
As shown in `update.md`, equating $F_{SRT}$ with $F_{thermo}$ is dangerous.
**SRT's Compromise**: We explicitly acknowledge Ax-FEP-1 is an **Isomorphic Analogy**. In real biological brains, eliminating every bit of information does correspond to $k_B T \ln 2$ heat dissipation (Landauer's Principle), but at the neuronal scale, this energy cost is overshadowed by the massive metabolic cost of action potentials. We discuss free energy at the "computational layer", not directly at the "molecular layer".

## 4.2 Measurement Difficulty of d-Value
Introducing $d \cdot U_{others}$ greatly enhances theoretical explanatory power, but at the cost of **measurement complexity**. Without care, $d$ value becomes a "universal coefficient"—any unexplained behavior can be blamed on $d$ value change.
This is exactly why we try to anchor it as a "hybrid prior" coefficient in Part A—seeking strict mathematical definition.

---

# 5 Falsifiable Predictions and Open Questions

## 5.1 Prediction: Free Energy Signature of Altruism (H-FEP-1)
> **Prediction**: When executing altruistic behavior, high $d$ value individuals should show significantly **lower** prefrontal prediction error than when executing self-interested behavior.

- **Logic**: If altruistic terms are integrated into priors $P(o_{self}, o_{others})$, then behavior aligning with altruistic expectations should generate minimal free energy. Conversely, if original FEP is correct, altruistic behavior should always generate higher prediction error for "violating self-interest".
- **Verification**: fMRI + Computational Modeling (DCM).

## 5.2 Prediction: Forgetting Rate and Metabolism Correlation (H-FEP-2)
> **Prediction (Based on T-Learn-1)**: The higher an individual's Basal Metabolic Rate (BMR) (implying high $\Psi_f$), the faster their forgetting rate for "non-survival related" information.

This is a startling prediction derived from "Learning is Inverse Friction" axiom: high-energy systems must more aggressively prune $L_2$ structure to maintain thermodynamic efficiency.

## 5.3 Open Questions
- **AI's Free Energy**: Current LLMs are clearly doing Next Token Prediction (minimizing surprise), but does this mean they have some form of $F_{SRT}$? If they lack metabolic boundaries (Markov Blanket), is this free energy minimization merely simulation rather than "real"?

---
