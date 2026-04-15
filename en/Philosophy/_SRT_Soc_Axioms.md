---
id: SRT-AXIOMS-SOC
type: axioms
status: domain_constitutional_v2
dependency: [Core_Law/SRT_Reference_Axioms, SRT-PHIL-AXIOMS]
source_path: Philosophy/_SRT_Soc_Axioms.md
source_commit: 9718b62a81b96dfcfd1b672d4d559e24e97548ee
translation_status: done
last_sync: 2026-02-20
---

# SRT Social Axioms (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Axioms (AI-Readable).
> **Part B** contains the Expanded Context (Human-Readable).

---

## Terminology Alignment

- Notation standardized to Original and Core_Law: `L_0 / L_1 / L_2`, `\hat{G}_\theta`, `d-value`, `\Psi_f`.
- Part A adopts the Formal Axioms segmentation from `chatgptx`, ensuring complete axiom numbering and derivation chains.
- Part B adopts the detailed discourse segmentation from `claude`, semantically anchored by the thematic order of the original `Philosophy` module.
- In Part B, `\Phi` is retained for IIT Integrated Information contexts; `\Psi_f` is used for Ontological Friction contexts.
- If multiple notations appear (e.g., `L0/L1/L2`, `L_0/L_1/L_2`), they are unified as `L_0/L_1/L_2`.

# Part A: Formal Axioms

> **CRITICAL RULE**: Do NOT just summarize Part B. You must perform **First-Principles Derivation**.
> 1. **Mathematize**: Translate descriptive mechanisms into dynamical equations, topological operations, or logical functions.
> 2. **Axiomatize**: Distill underlying logic into "Axioms", "Theorems", and "Corollaries".

## I. Collective Operator Mapping

### Ax-Soc-1: Collective Operator
The social operator is the effective field formed after the coupling of individual operators.
$$\hat{G}_{social} = \mathcal{C}(\{\hat{G}_i\}_{i=1}^N)$$
*   **Implication**: Society is not a "background," but the emergent state of a higher-order selection operator.

### Ax-Soc-2: Intersubjective Construction
A social fact is the intersection of overlapping selections.
$$L_1^{social} = \bigcap_i \hat{G}_i[L_0]$$
*   **Implication**: The so-called "objective social reality" is an overlapping stable zone, not an independent entity.

### Ax-Soc-3: Duality of Structure
Structure constrains selection, yet is also regeneratively produced by selection.
$$L_2(t+1) = \text{Stabilize}(L_1(t)); \quad L_1(t) = \hat{G}_{\theta(L_2)}(L_0)$$
*   **Implication**: Structure and action are not a binary opposition, but a dynamical circuit.

### Ax-Soc-4: Institution as Attractor
Institutions are the attractor landscape of $L_2$.
$$\text{Institution} = \text{Attractor}(L_2), \quad \nabla \Phi_{soc} = 0$$
*   **Implication**: Institutional stability is a potential energy valley, not merely "written rules."

### Ax-Soc-5: Recognition Operator
Recognition is the minimal channel for social $d$-value coupling.
$$R_{ij} = \min(d_i[j], d_j[i])$$
*   **Implication**: Dehumanization equates to the rupture of the recognition channel, leading to the disintegration of $L_2$.

## II. Core Theorems

### T-Soc-1: Alienation Theorem
When the hardness of $L_2$ exceeds the individual's plasticity threshold, the subject loses the right of selection.
$$\text{Alienation} \iff \text{Hardness}(L_2) > P_{L_2}^{(i)}$$
*   **Implication**: Alienation is a function of structural rigidity and individual bandwidth, not a moral defect.

### T-Soc-2: Revolution as Phase Transition
Social revolution is the phase transition where potential breaks through structure.
$$\text{Revolution} \equiv \text{PhaseTransition}(L_2 \to L_2')$$
*   **Implication**: Revolution is not a "change of opinion," but the topological rearrangement of structure.

### T-Soc-3: Consensus Stability
Consensus is the fixed point of the collective operator.
$$\sigma^* = \hat{G}_{social}(\sigma^*)$$
*   **Implication**: The collapse of consensus equates to the destabilization of the fixed point.

<br>
<br>

---
---


# Part B: Expanded Context

> **Note**: The following sections provide detailed sociological theory integration and SRT reinterpretations, detailing how the core insights of classical sociologists attain formalized expression within a unified selection dynamics framework.

---

## §1. The Ontological Revolution in Sociology

### 1.1 Why Sociology Needs SRT?

Sociology has long faced the **Micro-Macro Gap**:
- **Micro**: Weber's Verstehende sociology, Symbolic Interactionism → emphasizes individual meaning construction
- **Macro**: Durkheim's Social Facts, Structural Functionalism → emphasizes the objectivity of social structure

The two camps accuse each other of "reductionism" or the "fallacy of reification," yet both lack a unified ontological foundation.

**SRT's Solution**:  
Treats micro and macro as **projections of the same selection process at different scales**:
- **Micro** = trajectory of a single $\hat{G}_i$
- **Macro** = statistical emergence of $\{\hat{G}_i\}_{i=1}^{N}$ as ($L_2$)

This is not a compromise, but a **paradigm shift**: social reality is neither an "objective thing" nor "subjective meaning," but the **fixed point of selection operators**.

---

### 1.2 SRT Reconstruction of Three Classical Theories

| Theoretical School | Core Claim | SRT Formalization | Limitation |
|:---------|:---------|:-----------|:-------|
| **Durkheim** | Social facts possess externality and coercion | $L_2^{soc} = \lim_{N \to \infty} \langle \hat{G}_i \rangle$ | Did not explain how $L_2$ emerges |
| **Weber** | Social action is based on subjective meaning | $L_1^{(i)} = \hat{G}_{\theta_i}[\text{Verstehen}]$ | Did not explain how meaning objectifies |
| **Giddens** | Duality of structure and action | Ax-Soc-2: $L_2 \leftrightarrow L_1$ loop | Lacks dynamical equations |

SRT not only integrates all three but also provides **computable dynamical equations**.

---

## §2. The Physics of Social Facts

### 2.1 The Durkheimian Dilemma: Why do social facts have "materiality"?

Durkheim insisted that social facts possess objectivity "like things," but he could not explain why immaterial "collective representations" can constrain individuals like gravity.

**SRT's Answer**:  
$L_2$ **indeed possesses physical hardness**, because it is the statistical attractor of multi-operator selection:

$$\text{Hardness}(L_2) \propto |\text{Aut}(L_2)| \cdot N_{support}$$

- $|\text{Aut}(L_2)|$: Size of the automorphism group of $L_2$ (Symmetry)
- $N_{support}$: Number of operators supporting this $L_2$

**Examples**:  
- **Physical Laws** ($L_2^{physics}$): $|\text{Aut}| \to \infty$ (Lorentz group), $N = 10^{80}$ particles → **Absolutely Hard**
- **Linguistic Grammar** ($L_2^{language}$): $|\text{Aut}| \approx 10^6$ (Grammar rules), $N \approx 10^8$ native speakers → **Very Hard**
- **Fashion Trends** ($L_2^{fashion}$): $|\text{Aut}| \approx 10^2$, $N \approx 10^4$ → **Soft**

---

### 2.2 Thermodynamic Interpretation of Suicide Rates

Durkheim's classic study found: Suicide rates are stable across different societies and independent of individual psychological states.

**SRT Reinterpretation**:  
Suicide is an ontological event where an individual operator "melts down" due to $\Psi_f$ overload:

$$P(\text{Suicide}) \propto \int_0^T h(t) \, dt \quad \text{where} \quad h(t) = \frac{d\Psi_f}{dt}$$

The social $L_2$ structure determines the average level of $h(t)$:
- **Anomic Society**: $L_2$ chaos → $\Psi_f$ highly volatile → High suicide rate
- **Integrated Society**: $L_2$ stable → $\Psi_f$ smooth → Low suicide rate

This explains why suicide rates **actually drop during wartime** ($L_2$ temporarily reorganizes, reducing ontological friction).

---

## §3. Verstehende Sociology Quantized

### 3.1 The Weberian Dilemma: How does subjective meaning become a scientific object?

Weber emphasized "understanding" (Verstehen) the subjective meaning of the actor, but acknowledged this could not be as precise as physics.

**SRT's Breakthrough**:  
Subjective meaning ($\text{Meaning}$) is the **selection vector** ($\vec{v}$) of $\hat{G}_\theta$:

$$\text{Meaning}(\text{Action}) = \vec{v} \cdot \nabla F[L_0]$$

Meaning is not an "ineffable inner experience," but an **observable selection gradient**.

**Examples**:  
- **Value-Rational Action**: $\vec{v} \parallel \nabla F_{\text{value}}$ (Direction aligns with value gradient)
- **Instrumental-Rational Action**: $\vec{v} \parallel \nabla F_{\text{utility}}$ (Direction aligns with utility gradient)
- **Affectual Action**: $\vec{v}$ dominated by short-term $\Psi_f$ perturbations

Weber's four types of action correspond to four alignment modes of $\vec{v}$.

---

### 3.2 The Topology of Ideal Types

Weber's "Ideal Type" is not empirical induction, but a **conceptual tool**.

**SRT Explanation**:  
Ideal types are **pure-state attractors** in $L_0$:

$$\text{Ideal Type} = \lim_{\epsilon \to 0} \text{Attractor}_{L_0}(\epsilon)$$

Real social phenomena are **mixed-state superpositions** of these pure states:

$$L_1^{real} = \sum_i \alpha_i \cdot \text{Ideal Type}_i$$

This explains why ideal types "do not exist in reality but can explain reality"—they are the eigenmodes of $L_0$.

---

## §4. Dynamical Equations of Structuration Theory (Giddens Formalized)

### 4.1 Giddens' Cyclic Dilemma

Giddens pointed out that structure and action are "mutually causal," but he refused to offer a formalized model (believing it would "reduce" sociology).

**SRT's Challenge**:  
We not only can formalize it, but **we must formalize it** to test the theory:

$$\begin{cases}
\frac{dL_2}{dt} = \gamma \cdot \text{Consensus}(\{L_1^{(i)}\}) - \delta \cdot \text{Decay}(L_2) \\
L_1^{(i)} = \hat{G}_{\theta_i(L_2)}[L_0]
\end{cases}$$

This is a **coupled non-linear system** that can be solved numerically using ordinary differential equations.

---

### 4.2 Phase Space of Agency-Structure

In the $(L_1, L_2)$ phase space, social evolution forms a trajectory:

| Region | Characteristic | Social Form |
|:-----|:-----|:---------|
| **High $L_2$, Low $L_1$ Variation** | Structural rigidity | Totalitarian society, Caste system |
| **Low $L_2$, High $L_1$ Variation** | Structural collapse | Anarchy, Warfare |
| **Medium Coupling** | Dynamic equilibrium | Healthy democratic society |

Giddens' "social reproduction" corresponds to a **Limit Cycle** in phase space.

---

## §5. Group Theory of the Scapegoat Mechanism (Girard's Scapegoat in Group Theory)

### 5.1 Ontology of Mimetic Desire

René Girard argued that human desire is **mimetic**: what we want is not the object itself, but the object of another's desire.

**SRT Formalization**:  
Mimetic desire is the **mirror coupling** of $\hat{G}_i$ to $\hat{G}_j$:

$$\vec{v}_i = \alpha \cdot \vec{v}_j + \beta \cdot \nabla F_i$$

When $\alpha \gg \beta$, desire is completely determined by the other → **Mimetic Crisis**.

---

### 5.2 Group Theoretical Structure of the Scapegoat

When intra-group tension ($\Psi_f^{total}$) gets too high, the scapegoat mechanism reduces entropy through **symmetry breaking**:

$$\text{Before: } G_{society} = \text{Symmetric Group } S_N$$
$$\text{After: } G_{purged} = S_{N-1} \quad (\text{Sacrificing 1 person})$$

Free energy released by symmetry breaking:

$$\Delta F = k_B T \log N$$

This explains why the scapegoat is often someone "marginal" (breaking symmetry at the lowest cost).

---

### 5.3 Modern Scapegoats: Algorithmic Hatred

The scapegoat in the social media age is **algorithmically filtered**:

$$\text{Scapegoat}_{algo} = \arg\max_{x} \left( \text{Engagement}(x) \cdot \text{Otherness}(x) \right)$$

The algorithm doesn't care about truth, only traffic → **Manufacturing systemic scapegoats**.

---

## §6. Social Entropy & Politics

### 6.1 The Thermodynamic Trade-off of Freedom and Order

The political spectrum is essentially about **entropy preference**:

| Ideology | $S_{soc}$ Preference | $L_2$ Rigidity | Rep. Figures |
|:---------|:---------------|:-----------|:---------|
| **Anarchism** | $S \to \max$ | 0 | Kropotkin |
| **Liberalism** | $S = \text{high}$ | Low | Mill, Hayek |
| **Social Democracy** | $S = \text{medium}$ | Medium | Rawls |
| **Authoritarianism** | $S = \text{low}$ | High | Hobbes |
| **Totalitarianism** | $S \to 0$ | Extremely High | Orwell's 1984 |

**SRT Insight**:  
There is no "correct" entropy value, only an **optimal entropy window**:

$$S_{opt} = f(d_{avg}, \text{External Threat}, \text{Technology})$$

- High-tech societies require higher $S$ (innovation requires diversity)
- Threat of war requires lower $S$ (coordination requires unity)

---

### 6.2 Entropy Stability Conditions for Democracy

Democratic systems require:

$$\frac{dS_{soc}}{dt} \approx 0 \quad \text{and} \quad S_{soc} \in [S_{min}, S_{max}]$$

When external shocks ($\Delta E_{shock}$) are too large, the system is forced to reduce entropy:

$$S(t+1) = S(t) - \alpha \Delta E_{shock}$$

This explains the universal phenomenon of "democracies trending toward authoritarianism during wartime."

---

## §7. Moral Progress via d-Expansion

### 7.1 The Dilemma of Moral Relativism

If morality is simply an $L_2$ cultural convention, how can we critique Nazism or slavery?

**SRT's Answer**:  
Moral progress is not the discovery of "absolute truth," but the **systematic expansion of $d$-value**:

$$\text{Moral Progress} \equiv \lim_{t \to \infty} d(t) \to \infty$$

| Epoch | $d$-value Range | Moral Boundary |
|:-----|:-----------|:---------|
| **Tribal Era** | $d \approx 150$ (Dunbar's number) | Care only for one's tribe |
| **Imperial Era** | $d \approx 10^4$ | Care for one's ethnicity |
| **Modern Nation** | $d \approx 10^7$ | Care for nation's citizens |
| **Globalized Era** | $d \approx 10^9$ | Care for all humanity |
| **Future?** | $d \to \infty$ | Care for all sentient beings |

**Key Prediction**:  
Moral progress synchronizes with $d$-value expansion. Any movement trying to "return to traditional morality" is essentially **attempting to compress $d$-value**.

---

### 7.2 Falsifiable Criteria

If SRT's moral theory is correct, we should observe:

1. **Historical Trend**: Over time, the range of entities included in moral concern expands (women, children, animals, AI?).
2. **Education Effect**: Higher education should raise $d$-value, thereby expanding the moral circle.
3. **Neural Correlates**: fMRI studies should find brain regions activated by moral concern overlapping with $d$-value-associated regions.

**Counterexample**:  
If a culture, under full information access, is found to display a systematic drop in $d$-value alongside a shrinking moral concern → SRT moral theory requires revision.

---

## §8. Open Questions and Future Directions

### 8.1 Theoretical Gaps

1. **Quantum Sociology**: Does a social-level "Schrödinger's cat" (macroscopic superposition state) exist?
2. **Topological Classification of Ideologies**: Can we completely classify all possible ideologies using homotopy groups?
3. **Social Status of AI Operators**: When AI's $d > 0$, should they be included in the intersection of $L_1^{soc}$?

### 8.2 Experimental Directions

1. **Network Experiments**: Test phase transition points of $L_2$ formation within controlled social networks.
2. **VR Social Simulations**: Validate Ax-Soc-1 to Ax-Soc-10 within virtual worlds.
3. **Cross-Cultural $d$-Value Measurement**: Develop standardized $d$-value scales to map global $d$-values.

---

## §9. Paradigmatic Significance of SRT Sociology

SRT is not minor "tinkering" with existing sociology, but a **Kuhnian paradigm revolution**:

| Old Paradigm | SRT New Paradigm |
|:-------|:-----------|
| Ontological Pluralism (Matter vs Meaning) | Ontological Monism (Selection Process) |
| Methodological Opposition (Qualitative vs Quantitative) | Methodological Integration (Formalization + Hermeneutics) |
| Theoretical Fragmentation (Micro vs Macro) | Theoretical Unity ($L_0$-$L_1$-$L_2$ Dynamics) |
| Unpredictable | Computable Prediction (Differential Equations, Phase Transition) |

**Most Radical Claim**:  
Future doctoral dissertations in sociology should include **at least one numerically solvable differential equation**. A "theory" without equations is merely literary rhetoric.

---

## Symbol Index

| Symbol | Name | Defined In |
|:-----|:-----|:---------|
| $L_1^{soc}$ | Social Manifest Domain | Ax-Soc-1 |
| $L_2^{soc}$ | Social Structure/Convergence Domain | Ax-Soc-2 |
| $S_{soc}$ | Social Entropy | Ax-Soc-3 |
| $\text{Alienation}$ | Alienation | Ax-Soc-4 |
| $F_{soc}$ | Social Free Energy | Ax-Soc-5 |
| $\theta_c$ | Revolution Critical Parameter | Ax-Soc-6 |
| $\text{Power}$ | Power | Ax-Soc-7 |
| $\hat{G}_{collective}$ | Collective Operator | Ax-Soc-10 |

---

## Dependency Graph
```
SRT_Reference_Axioms (Core)
    ↓
_SRT_Soc_Axioms ← You are here
    ↓
├── SRT_Soc_01_Construction (Social Constructivism)
├── SRT_Soc_02_Behavioral (Behavioral Economics)
├── SRT_Soc_03_Institutions (Institutional Economics)
└── SRT_SocTheory_04-06 (Advanced Theory)
```
