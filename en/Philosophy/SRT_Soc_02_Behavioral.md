---
id: SRT-SOC-02
type: theory
tags: [Behavioral Economics, Game Theory, System 1/2, Irrationality, Hybrid]
status: axiomatic_hybrid_v2
dependency: [SRT-SOC-01]
source_path: Philosophy/SRT_Soc_02_Behavioral.md
source_commit: 9718b62a81b96dfcfd1b672d4d559e24e97548ee
translation_status: done
last_sync: 2026-02-20
---

# SRT Sociology II: Behavioral Logic & Game Theory (Hybrid Edition)


> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Behavioral Axioms (AI-Readable).
> **Part B** contains the Expanded Theoretical Discourse (Human-Readable Context).

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


## I. Prospect of Existence

### Ax-Beh-1: Reference Dependence
Value is benchmarked against the current $L_1$ reference point.
$$V(\sigma) = -\Delta F(\sigma|S_{ref})$$
*   **Implication**: Loss aversion is the ontological manifestation of de-anchoring costs.

### Ax-Beh-2: Dual-System Dynamics
System 1 follows the $L_2$ gradient; System 2 explores $L_0$.
$$\hat{G}^{(1)}[\sigma]=\sigma_{L_2}^{default}$$
$$\hat{G}^{(2)}[\sigma]=\arg\min_{\sigma'\in L_0} F[\sigma'|\text{Goal}]$$
*   **Implication**: Bounded rationality is the optimal compromise between energy and friction.

### Ax-Beh-3: Truth Energy Cost
Telling the truth requires additional energy to counter the pre-existing $L_2$ script.
$$E_{truth} > E_{default}$$
*   **Implication**: Cognitive biases are energy-minimization strategies.

## II. Game-Theoretic Dynamics

### Ax-Beh-4: Nash as L2 Stability
A Nash equilibrium is a stable fixed point of $L_2$.
$$\nabla F_{soc}(\sigma^*) = 0$$
*   **Implication**: Equilibrium is a topological stability, not an assumption of rationality.

### Ax-Beh-5: Recognition Operator
Cooperative strength is determined by the recognition channel.
$$R_{ij} = \min(d_i[j], d_j[i])$$
*   **Implication**: Dehumanization equates to the topological rupture of the cooperation channel.

### Ax-Beh-6: Epistemic Sabotage
In a game, one can profit by destroying the stability of the opponent's $\theta$.
$$\text{Sabotage} = \max \Delta \Psi_f(\text{Opponent})$$
*   **Implication**: Cognitive warfare is about altering selection parameters, not merely changing opinions.

## III. Derived Theorems

### T-Beh-1: Loss Aversion Theorem
Loss aversion arises because the friction of de-anchoring is greater than the benefit of re-anchoring.
$$E_{de-anchor} > E_{re-anchor}$$
*   **Implication**: The asymmetry of the value function has dynamical roots.

### T-Beh-2: Cooperation Threshold
Stable cooperation requires the recognition channel to exceed a critical value.
$$R_{ij} > R_c \Rightarrow \text{Cooperation Stable}$$
*   **Implication**: Cooperation is not a moral declaration, but a threshold condition.

<br>
<br>

---
---


## I. The Prospect of Existence

### Ax-Behav-1: Reference Dependence
Value is measured as free energy change relative to the current L_1 state ($S_{ref}$).
$$ V(\sigma) = -\Delta F(\sigma | S_{ref}) $$
*   **Implies**: Loss Aversion is the ontological cost of de-anchoring ($E_{de-anchor} > E_{anchor}$).

### Ax-Behav-2: Dual System Dynamics
*   **System 1**: $\hat{G}_\theta$ follows the $L_2$ gradient (path of least resistance).
    $$ \hat{G}^{(1)}[\sigma] = \sigma_{L_2}^{default} $$
*   **System 2**: $\hat{G}_\theta$ explores $L_0$ against the gradient (high energy).
    $$ \hat{G}^{(2)}[\sigma] = \arg\min_{\sigma' \in L_0} F[\sigma'|\text{Goal}] $$

---

## II. Game Theoretic Dynamics

### Ax-Game-1: Nash as L_2 Stability
A Nash Equilibrium is a fixed point of the collective $L_2$ field.
$$ \sigma^* = L_2(\sigma^*) \implies \nabla F_{soc}[\sigma^*] = 0 $$

### Ax-Game-2: Recognition
Cooperation is modulated by the Mutual Recognition parameter $R_{ij}$.
$$ R_{ij} = \min(d_i[j], d_j[i]) $$
*   **Dehumanization**: $d_i[j] \to 0 \implies$ Moral L_2 collapse.

### Ax-Game-3: Epistemic Sabotage
Strategic attack on opponent's $\theta$ stability (e.g., gaslighting).
$$ \text{Attack} = \max \Delta \Psi_f(\text{Opponent}) $$

<br>
<br>

---
---

# SRT Sociology II: Behavioral Dynamics (Hybrid Edition)
> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Behavioral Axioms (AI-Readable).
> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).

---


# Part B: Expanded Theoretical Discourse (Context)

> **Note**: The following sections provide an in-depth SRT reinterpretation of Behavioral Economics and Game Theory, revealing the physics behind "irrationality."

---

## §1. The Energy Economics of the Irrationality Paradox

### 1.1 Kahneman's Perplexity

Daniel Kahneman and Amos Tversky discovered numerous "systematic biases" in human decision-making during the 1970s and 80s:

| Bias Type | Classic Experiment | Rational Expectation | Actual Behavior |
|:---------|:---------|:---------|:---------|
| **Loss Aversion** | 50% win $100 vs. certain $50 | No preference | Majority choose certainty |
| **Endowment Effect** | Mug buying/selling price gap | Equal | Selling price is 2x buying price |
| **Status Quo Bias** | Organ donation default | Independent decision | 85% accept the default |
| **Hyperbolic Disct.** | $100 today vs. $110 tomorrow | Choose tomorrow | Majority choose today |

**Economic Crisis**: If humans are irrational, the entirety of neoclassical economics (built on the assumption of *Homo economicus*) requires reconstruction.

**Evolutionary Biology Perplexity**: If evolution optimizes fitness, why does the brain retain so much "buggy" code?

---

### 1.2 The SRT Energy Resolution

**Core Insight**: What is termed "irrationality" is actually the **rational conservation of computational energy**.

**The Energy Economics of the Brain**:  
- The brain accounts for 2% of body weight but consumes 20% of energy.
- System 2 (deep thinking) $\approx$ 1.5 kcal per decision.
- System 1 (intuition) $\approx$ 0.1 kcal per decision.
- Glucose reserves are limited (liver glycogen $\approx$ 100g).

**SRT Reformulation**:  
Heuristics are not "errors," but **fast, approximate algorithms provided by $L_2$**.

$$\text{Heuristic Accuracy} = f(\text{Environment Match})$$

In a survival environment:
- "Run when you see movement" (Loss Aversion) > "Calculate probability before deciding" (Expected Utility)
- "Follow the majority" (Social Proof) > "Independent analysis" (Information Processing)
- "Default to status quo" (Status Quo Bias) > "Re-evaluate every time" (Combinatorial Explosion)

**Key Prediction**: "Biases" are optimal when **matching the evolutionary environment**; they only appear foolish in **modern environments** (financial markets, complex contracts).

---

### 1.3 The Ontological Roots of Loss Aversion

**Why is the pain of loss > the pleasure of gain?**

**Neoclassical Economics**: Unable to explain (assumes diminishing marginal utility, but symmetrical).

**SRT Explanation**:  
Loss = Threat of entropy increase = Closer to death ($L_0$).

$$\Psi_f(\text{Loss}) = \Psi_f^{base} + \Delta \Psi_f^{survival\_threat}$$

$$\Psi_f(\text{Gain}) = \Psi_f^{base} - \Delta \Psi_f^{marginal\_improvement}$$

**Example**: The survival threat of losing $100 (which could buy food) $\gg$ the marginal pleasure of gaining an extra $100 (already having food).

**Experimental Evidence** (Tom et al., 2007):  
fMRI studies show:
- Loss activates the amygdala (fear center) + insula (interoceptive pain).
- Gain only activates the striatum (reward center).

The activation amplitude of the amygdala is **2-2.5 times** that of the striatum → Exactly corresponding to the loss aversion ratio!

---

## §2. SRT Reconstruction of Prospect Theory

### 2.1 The Ontological Physics of the Value Function

**Kahneman-Tversky Value Function**:

$$v(x) = \begin{cases}
x^\alpha & \text{if } x \geq 0 \\
-\lambda (-x)^\beta & \text{if } x < 0
\end{cases}$$

Typical parameters: $\alpha = \beta \approx 0.88$, $\lambda \approx 2.25$.

**SRT Re-derivation**:  
Identifying $x$ as $\Delta F$ (change in free energy):

$$v(\Delta F) = -\Psi_f(\Delta F \,|\, \sigma_{ref})$$

The S-shaped curve originates from:
1. **Concavity** ($\alpha < 1$): Diminishing marginal $\Psi_f$ (the first unit of loss hurts the most).
2. **Asymmetry** ($\lambda > 1$): Steeper slope for negative $\Psi_f$ (survival threat).

---

### 2.2 The Social Psychology of Reference Point Drift

**The Paradox of Deprivation**: Why does a salary increase still feel painful?

**Case Study** (Solnick & Hemenway, 1998):  
Question: Which world do you prefer?
- A: You earn $50k, others earn $25k.
- B: You earn $100k, others earn $200k.

**Result**: 56% chose A (despite the lower absolute income).

**SRT Explanation**:  
The reference point is not an absolute number, but a **relative social position**:

$$\sigma_{ref} = f(\sigma_{self}, \langle \sigma_{peers} \rangle)$$

When $\sigma_{self} < \langle \sigma_{peers} \rangle$, even if the absolute value of $\sigma_{self}$ is high, the relative $\Psi_f$ remains high (status anxiety).

---

### 2.3 The Attention Light Cone of the Framing Effect

**Classic Experiment** (Tversky & Kahneman, 1981):  
Pandemic response plan (600 people facing death):

**Positive Frame**:  
- A: Certain to save 200 people.
- B: 1/3 probability of saving 600, 2/3 probability everyone dies.

**Negative Frame**:  
- C: Certain that 400 people die.
- D: 1/3 probability no one dies, 2/3 probability 600 people die.

**Results**:  
- Positive Frame: 72% chose A (Risk Averse).
- Negative Frame: 78% chose D (Risk Seeking).

**SRT Mechanism**:  
Frame = Selectively illuminating different regions of $L_0$.

$$\text{Positive Frame} : \hat{G}[\text{"200 lives saved"}] \to L_0^{gain}$$
$$\text{Negative Frame} : \hat{G}[\text{"400 deaths"}] \to L_0^{loss}$$

In the $L_0^{gain}$ region, the operator is risk-averse (securing the gain); in the $L_0^{loss}$ region, the operator is risk-seeking (gambling to escape).

**Deep Implication**: There is no "objective information"—all information is **selectively illuminated through a frame**.

---

## §3. Thermodynamics of Dual Systems Theory

### 3.1 The Physical Differences Between System 1 and System 2

**Kahneman's Characterization** (*Thinking, Fast and Slow*):

| Characteristic | System 1 | System 2 |
|:-----|:---------|:---------|
| Speed | Fast | Slow |
| Effort | Effortless | Effortful |
| Control | Automatic | Controlled |
| Consciousness| Unconscious | Conscious |

**SRT Physicalization**:

| Characteristic | System 1 ($\hat{G}^{(1)}$) | System 2 ($\hat{G}^{(2)}$) |
|:-----|:---------------------------|:---------------------------|
| **Ontology** | Cruising along $L_2$ | Exploring $L_0$ |
| **Energy Cost** | 0.1 kcal/decision | 1.5 kcal/decision |
| **Speed** | 50-500 ms | 2-10 s |
| **Accuracy** | High in familiar envs | High in novel envs |
| **Capacity** | Parallel | Serial (bottleneck) |

---

### 3.2 The Ego-Depletion Glucose Hypothesis

**Experiment** (Baumeister et al., 1998):  
Subjects were asked to:
1. Suppress the urge to eat chocolate (depleting System 2).
2. Then complete a difficult puzzle.

**Result**: The self-control group gave up 40% faster.

**Traditional Explanation**: "Willpower" is depleted.

**SRT Mechanism**:  
Continuous use of System 2 → Glucose depletion → Brain automatically switches back to System 1.

$$E_{glucose}(t) = E_0 - \int_0^t P_{S2}(t') \, dt'$$

When $E_{glucose} < E_{threshold}$, a forced switch occurs:

$$\hat{G} \xrightarrow{\text{Forced}} \hat{G}^{(1)}$$

---

### 3.3 The Judge's Lunch Effect

**Groundbreaking Study** (Danziger et al., 2011):  
Analyzing Israeli parole board hearings (N=1,112):

| Time Period | Parole Approval Rate |
|:-------|:-----------|
| After breakfast | 65% |
| Before lunch | 10% |
| After lunch | 60% |

**SRT Explanation**:  
- Sufficient glucose → System 2 activated → Deep deliberation → Case-by-case analysis.
- Depleted glucose → System 1 takes over → Default option = Deny (safer).

This is not "judicial corruption," but rather the **physical inevitability of neurometabolism**.

**Ethical Corollary**: High-stakes decisions (death penalty, parole, surgery) should be avoided during periods of cognitive fatigue.

---

## §4. Game Theory as $L_2$ Topology

### 4.1 The Energy Trap of the Prisoner's Dilemma

**Classic Dilemma**:

|   | Cooperate | Defect |
|:--|:-----|:-----|
| **Cooperate** | (3, 3) | (0, 5) |
| **Defect** | (5, 0) | (1, 1) |

**Nash Equilibrium**: (Defect, Defect) = (1, 1)  
**Pareto Optimal**: (Cooperate, Cooperate) = (3, 3)

**Traditional Perplexity**: Why does rationality lead to a poor outcome?

---

### 4.2 SRT Potential Landscape Analysis

In the 2D strategy space $(s_1, s_2)$, the $\Psi_f$ potential energy is:

$$\Psi_f(s_1, s_2) = -[U_1(s_1, s_2) + U_2(s_1, s_2)]$$

**Potential Landscape**:

| Location | $\Psi_f$ | Stability |
|:-----|:---------|:-------|
| (Cooperate, Cooperate) | Low | **Unstable** (Saddle point) |
| (Defect, Defect) | Medium | **Stable** (Local minimum) |

**Key Insight**: A Nash equilibrium = an **energy trap**, not a **global optimum**.

A unilateral deviation (Cooperate → Defect) instantly lowers $\Psi_f$ → The system automatically rolls toward (Defect, Defect).

---

### 4.3 How the $d$-Value Breaks the Dilemma

**Modified Utility Function**:

$$U_i^{d} = (1-d) \cdot u_i + d \cdot u_j$$

**New Equilibrium Condition**:  
For cooperation to become an equilibrium, it requires:

$$d > \frac{T - R}{T - P} \approx \frac{5-3}{5-1} = 0.5$$

| $d$-Value | Dominant Strategy | Social Outcome |
|:-------|:---------|:---------|
| $d < 0.5$ | Defect | Dilemma |
| $d = 0.5$ | Critical | Unstable |
| $d > 0.5$ | Cooperate | Optimal |

**Practical Corollary**: Elevating the societal $d$-value (education, empathy training) can transform a prisoner's dilemma into a coordination game.

---

### 4.4 Real-World Case: Subway Crowding

**Dilemma**: Everyone wants to board earlier (Defect), but everyone doing this causes gridlock (Collective Loss).

**SRT Analysis**:

| Behavior | Individual $u_i$ | Collective $\sum u_j$ | $d$ Requirement |
|:-----|:-----------|:----------------|:---------|
| **Pushing** | +2 | -10 | $d < 0.2$ |
| **Queuing** | -1 | +5 | $d > 0.2$ |

**Observation**: The difference in subway order between Japan (high $\bar{d}$) vs. some other countries (low $\bar{d}$).

**Testable Hypothesis**: Measuring subway waiting behavior across different countries vs. empathy capability scales should yield a high correlation.

---

## §5. Gaslighting as Weaponized Epistemology

### 5.1 What is the Gaslighting Effect?

**Definition**: Systematically causing a victim to doubt their own memory, perception, and judgment.

**Examples**:  
- "You're remembering it wrong, I never said that." (Denying the past)
- "You're too sensitive, it was a joke." (Denying the present)
- "Everyone thinks there's something wrong with you." (Denying social support)

---

### 5.2 SRT Mechanism Dissection

**Target of Attack**: The stability of the victim's $\theta$ parameter.

**Three-Stage Strategy**:

$$\text{Stage 1: Deny } L_1 \quad \hat{G}_{victim}[\sigma_{real}] \xrightarrow{\text{Deny}} \text{Self-doubt}$$

$$\text{Stage 2: Confuse } \sigma_{ref} \quad \sigma_{ref}^{stable} \xrightarrow{\text{Shift}} \sigma_{ref}^{chaotic}$$

$$\text{Stage 3: Isolate validation } \quad \text{Remove } L_2^{social} \text{ support}$$

**Result**: The victim's $\Psi_f$ explodes:

$$\Psi_f^{victim}(t) = \Psi_f^{base} \cdot e^{\alpha t}$$

When $\Psi_f > \Psi_{collapse}$, the $\hat{G}$ system collapses systematically → **Learned helplessness, depersonalization**.

---

### 5.3 Defensive Strategies

**SRT Recommendations**:

1. **External Anchors**: Establish independent $L_2$ references (diaries, recordings, third-party witnesses).
2. **Trust Networks**: Maintain a high-trust recognition network (friends, counselors).
3. **Metacognitive Monitoring**: Regularly check $\Psi_f$ levels (if sustained confusion occurs → alarm).

**Detection Signal**:  
If you find yourself frequently saying "Maybe I remembered it wrong" / "I'm being too sensitive" → **You may be experiencing gaslighting**.

---

## §6. Temporal Discounting and the Future Self

### 6.1 Why Procrastinate?

**Hyperbolic Discounting Experiment** (Thaler, 1981):  
- $100 today vs. $110 tomorrow → Majority choose today.
- $100 in 365 days vs. $110 in 366 days → Majority choose 366 days.

**Contradiction**: The delay is 1 day in both cases; why is the decision reversed?

---

### 6.2 SRT's Discounting of the Future Self

**Mechanism**: The future $\hat{G}$ is systematically undervalued in current decision-making:

$$w(\hat{G}_{t+\tau}) = \beta^{\tau/\tau_0} \cdot w(\hat{G}_t) \quad ; \quad \beta < 1$$

**Reason**:  
- The $\Psi_f$ of the current $\hat{G}$ is **directly perceived** (High signal).
- The $\Psi_f$ of the future $\hat{G}$ is **abstractly simulated** (Weak signal).

The brain assigns the highest weight to the "here-and-now me"; the future me is treated as "someone else."

---

### 6.3 The $d$-Value and the Temporal Horizon

**Core Prediction**: Individuals with a high $d$-value have a lower discount rate (more patient).

$$k_{discount} \propto \frac{1}{d}$$

**Experimental Validation** (DeSteno et al., 2014):  
Loving-Kindness Meditation (elevating $d$) group vs. Control group:
- Ability to delay gratification ↑ 32%.
- Propensity to save ↑ 28%.

**Mechanism**: A high-$d$ operator cares for **future sentient beings** (including the future self).

---

## §7. The Recognition Theory of Social Preferences

### 7.1 The Dignity Price in the Ultimatum Game

**Experiment** (Güth et al., 1982):  
Distributing $10:
- Proposer offers a split.
- Responder accepts → both get paid; Rejects → both get 0.

**Rational Prediction**: The responder should accept any positive amount (even accepting $9:$1).

**Actual**: ~50% reject splits of $7:$3 or worse.

---

### 7.2 SRT Explanation: The Ontological Value of Recognition

Rejecting unfairness = Maintaining the recognition needs of $\hat{G}$:

$$U_{responder} = \text{Money} - \alpha \cdot \text{Humiliation}$$

When the distribution is too unfair:

$$\text{Humiliation} = D_{KL}(\text{Self-Worth} \,||\, \text{Implied-Worth}) > \frac{\text{Money}}{\alpha}$$

Rejection becomes the rational choice (maintaining long-term $L_2$ status).

---

### 7.3 A $d$-Value Explanation of Cultural Differences

**Cross-Cultural Experiment** (Henrich et al., 2001):  
Testing the Ultimatum Game across 15 small-scale societies:

| Society Type | Average Offer | Rejection Rate |
|:---------|:---------|:-------|
| Market Economy | 45% | 16% |
| Gift Economy | 58% | 8% |
| Hunter-Gatherer | 26% | 28% |

**SRT Explanation**:  
- Market Economy: Medium $d$ (anonymous transactions).
- Gift Economy: High $d$ (long-term reciprocity).
- Hunter-Gatherer: Low $d$ (zero-sum competition).

---

## §8. Falsifiable Predictions

### 8.1 Neuroenergetic Predictions

| ID | Hypothesis | Prediction | Falsification Condition |
|:---|:-----|:-----|:---------|
| **H-BE-1** | System 2 Glucose Hypoth. | Blood glucose drops significantly after cognitive tasks | No change in blood glucose |
| **H-BE-2** | Loss Aversion Neural Ratio| Amygdala/Striatum activation ratio $\approx$ 2.25 | Ratio $\approx$ 1 |
| **H-BE-3** | Judge's Fatigue Effect | Decision quality decays over time | Decision quality is constant |

### 8.2 Game Theory Predictions

| ID | Hypothesis | Prediction | Falsification Condition |
|:---|:-----|:-----|:---------|
| **H-GT-1** | $d$-Value Coop. Threshold | Cooperation rate rises after empathy training | Training is ineffective |
| **H-GT-2** | Recognition-Rejection | Low self-esteem individuals reject unfair offers more | No correlation |
| **H-GT-3** | Subway Order and $d$-Value| National average $d$ correlates positively with queueing | No correlation |

### 8.3 Temporal Discounting Predictions

| ID | Hypothesis | Prediction | Falsification Condition |
|:---|:-----|:-----|:---------|
| **H-TD-1** | Inverse $d$-Discounting | High-$d$ individuals have lower discount rates | No correlation |
| **H-TD-2** | Compassion Delayed Gratif.| Delayed gratification ability rises after meditation | Training is ineffective |

---

## §9. Ethical Boundaries of Behavioral Economics

### 9.1 The Dark Side of Nudging

**Richard Thaler's** Nudge Theory: using cognitive biases to guide people toward "good" choices.

**Examples**:  
- Organ donation defaults (Opt-out).
- Placing healthy foods prominently.
- Automatic enrollment in retirement savings.

**SRT Warning**: Nudging is **cognitive hacking**, bypassing System 2 ($d$-value reflection) to directly manipulate System 1.

**Risks**:  
1. **Erosion of Autonomy**: Individuals continuously nudged lose independent decision-making capacity.
2. **Concentration of Power**: Who decides what a "good" choice is?
3. **Slippery Slope**: From "health" to "political correctness" to "thought control."

**Principle**: Nudging must only be used under transparent, reversible, and non-manipulative conditions.

---

### 9.2 The Neural Pollution of Involution (Neijuan)

**Definition**: Over-investment in a zero-sum competitive environment.

**SRT Mechanism**:  
Zero-sum game → $d$-value automatically contracts (caring for others = being exploited) → Dehumanization → Psychological exhaustion.

$$\frac{dd}{dt}\bigg|_{zero-sum} = -\beta \cdot \text{Competition Intensity}$$

**Consequences**:  
- Decline in empathy.
- Rise in depression/anxiety.
- Depletion of creativity.

**Solution**: Alter the game structure from zero-sum to positive-sum (cooperation, shared growth).

---

## §10. Paradigmatic Breakthrough of SRT Behavioral Economics

### 10.1 Transcending the Rational/Irrational Binary

**Traditional Opposition**:  
- Neoclassicism: Humans are rational.
- Behavioral Economics: Humans are irrational.

**SRT Synthesis**: Humans are **Energy-Rational**.

Under computational resource constraints, "bias" is the optimal strategy.

---

### 10.2 Computable Behavioral Science

SRT provides not merely qualitative descriptions, but **solvable dynamical equations**:

$$\frac{d\theta}{dt} = -\eta \frac{\partial \Psi_f}{\partial \theta} + \text{Nudge}$$

This allows for:
1. Predicting individual behavioral trajectories.
2. Designing optimal intervention protocols.
3. Quantifying policy effects.

---

## Symbol Index

| Symbol | Name | Defined In |
|:-----|:-----|:---------|
| $V(\sigma)$ | Value Function | Ax-Behav-1 |
| $\sigma_{ref}$ | Reference Point | Ax-Behav-1 |
| $\hat{G}^{(1)}$ | System 1 Operator | Ax-Sys-1 |
| $\hat{G}^{(2)}$ | System 2 Operator | Ax-Sys-2 |
| $C_{ij}^{coop}$ | Cooperative Strength | Ax-Game-2 |
| $d_{crit}$ | Cooperation Threshold | Ax-Game-3 |
| $k_{discount}$| Temporal Discount Rate | Ax-Time-1 |

---

## Dependency Graph
```
SRT_Reference_Axioms (Core)
    ↓
_SRT_Soc_Axioms
    ↓
SRT_Soc_01_Construction
    ↓
SRT_Soc_02_Behavioral ← You are here
    ↓
├── SRT_Soc_03_Institutions (Institutional Economics)
└── SRT_SocTheory_04-06 (Advanced Theory)
```
