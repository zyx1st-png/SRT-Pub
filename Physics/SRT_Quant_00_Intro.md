---
id: SRT-QUANT-00
type: foundational_theory
tags: [Quantum Mechanics, Measurement, History Construction, Interpretations, Hybrid]
status: axiomatic_hybrid_v2
dependency: [Core_Law/SRT_Reference_Axioms, SRT-PHYS-BRIDGE]
---

# SRT Quantum Mechanics: Selectionist Interpretation — Introduction (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Quantum Axioms establishing SRT's interpretation of measurement, non-locality, and history (AI-Readable).
> **Part B** contains the Original Theoretical Discourse with detailed analysis of classic experiments (Human-Readable Context).

---

# Part A: Formal Quantum Axioms
## 0. Notation & Conventions (符号与约定)

- $L_0,L_1,L_2$: 潜在域 / 显现域 / 收敛域。
- $\hat{G}_\theta$: 选择算子，$\theta \in \Theta_{finite}$ 为具身参数。
- $F$: 自由能；$\Phi$ 为本体论摩擦势能，$\Psi_f$ 为其局部密度（可取 $\Phi=\int \Psi_f \, dt$）。
- $d$: 注意力范围（Scope）；$\rho$: 分辨率；$\vec{v}$: 选择方向。
- $\Lambda$: 跨尺度同构；$\pi_\lambda$: 粗粒化映射；$\approx$ 表示尺度等价。
- **稳定性约定**：$x^*$ 为固定点且 $\text{Re}(\lambda_J)<0$ 视为稳定。

## 0.5 Numbering Scheme (编号体系)

- Ax-* → A{part}.{sec}.{n}, Def-* → D{part}.{sec}.{n}, T-* → T{part}.{sec}.{n}, Lemma → L{part}.{sec}.{n}, Corollary → C{part}.{sec}.{n}.
- part=1 为 Part A，part=2 为 Part B；sec 为章节编号（I/II…或 §n）。
- 序号按出现顺序递增，同类编号在每个章节内独立递增。

## 0. Core Theorem Alignment (核心定理对齐)

本模块以 Core_Law 的核心定理作为量子叙事的数学骨架：

- **T-Scale-1/2**：$\hat{G}$ 的尺度同构与一致性保证微观—宏观解释连续
- **O-T1 (现实化即积分)**：$L_1 = \oint_{\gamma} \omega_{L_0}$ 描述坍缩为路径积分的“求值”
- **M1/M2 + T-DMP-2**：测量结果作为稳定固定点并具备恢复力
- **T-Phase-1**：$v_{sub}=\dot{\phi}/\phi_0$ 连接选择节拍与时间体验

## 0.6 Cross-Reference Index (交叉引用索引)

### Part A Index
| ID | Label | Title |
|:---|:------|:------|
| A1.1.1 | Ax-Quant-1 | Collapse as Selection (坍缩即选择) |
| L1.1.1 | Lemma Q-Path (路径测度视角) | — |
| A1.1.2 | Ax-Quant-2 | Uncertainty as Bandwidth Limit (不确定性即带宽极限) |
| A1.1.3 | Ax-Quant-3 | Objective Measurement Criterion (客观测量判据) |
| A1.2.1 | Ax-Quant-4 | $L_0$ Topological Unity (L₀拓扑统一性) |
| A1.2.2 | Ax-Quant-5 | Entanglement Unity Theorem (纠缠统一定理) |
| A1.3.1 | Ax-Quant-6 | Retroactive Participancy (回溯性参与) |
| A1.3.2 | Ax-Quant-7 | History Plasticity (历史可塑性) |
| A1.4.1 | Ax-Quant-8 | Semantic Entanglement (语义纠缠) |
| T1.5.1 | Theorem T-Quant-Synthesis | Meta-Interpretational Framework |

### Part B Index
| ID | Label | Title |
|:---|:------|:------|
| C2.1.1 | Corollary I | Measurement as Operator Sharpening |
| C2.1.2 | Corollary II | $L_0$ Has No Time, No Space |
| C2.1.3 | Corollary III | Quantum-Classical Boundary = $L_2$ Stability Threshold |
| C2.1.4 | Corollary IV | Entanglement = $L_0$ Irreducibility |
| C2.1.5 | Corollary V | Participatory Universe |


## I. The Nature of Measurement (测量本质)

### Ax-Quant-1 [A1.1.1]: Collapse as Selection (坍缩即选择)
Wavefunction collapse is the ontological transformation of $L_0$ potentiality into $L_1$ actuality by the Selection Operator $\hat{G}_\theta$.
$$ \text{Collapse} \equiv \hat{G}_\theta : |\Psi\rangle_{L_0} \longrightarrow |\pi_k\rangle_{L_1} $$
*   **Ontological Status**: Measurement is not epistemological update but ontological anchoring—it creates determinate facts where none existed.
*   **Source**: Derives from Core Axiom A1 (Selection Priority) and A2 (Existence as Anchoring).
*   **O-T1 Link**: $L_1 = \oint_{\gamma} \omega_{L_0}$，坍缩即对潜在路径 $\gamma$ 的评估与取值。

#### Lemma Q-Path (路径测度视角) [L1.1.1]
令 $\Gamma_k$ 为导致结果 $k$ 的允许路径族，则
$$ P(k) \propto \int_{\Gamma_k} e^{-\Phi[\gamma]} \, \mathcal{D}\gamma, \quad L_1^{(k)} = \oint_{\gamma \in \Gamma_k} \omega_{L_0} $$
坍缩即对“可持续路径”的测度求值，$\Phi$ 作为选择权重。

### Ax-Quant-2 [A1.1.2]: Uncertainty as Bandwidth Limit (不确定性即带宽极限)
The Heisenberg Uncertainty Principle reflects an informational bandwidth constraint of $\hat{G}_\theta$, not measurement disturbance.
$$ \Delta x \cdot \Delta p \geq \frac{\hbar}{2} \iff \text{Bandwidth}(\hat{G}_\theta) \leq C_{max} $$
*   **Fourier Interpretation**: Position ($x$) is time-domain/$L_1$ localization; Momentum ($p$) is frequency-domain/$L_0$ structure. Sharp localization in one requires summing infinite components from the other.
*   **Implication**: Particle-like behavior is not intrinsic to matter—it is the result of extreme Fourier transformation imposed by $\hat{G}$.

### Ax-Quant-3 [A1.1.3]: Objective Measurement Criterion (客观测量判据)
A physical process constitutes a measurement if and only if it satisfies:
$$ \text{Measurement} \iff \begin{cases} \Delta S_{entanglement} > 0 & \text{(Entanglement broken)} \\ \Delta I_{classical} > 0 & \text{(Classical information recorded)} \\ \tau_{decoherence} < \tau_{readout} & \text{(Irreversibility achieved)} \end{cases} $$
*   **Resolution**: This provides the objective definition Sean Carroll (2025) identified as missing from quantum mechanics. Consciousness is not required—any system satisfying these criteria is a valid $\hat{G}_{proxy}$.
*   **Stability Clause (M1/M2)**: 合法 $L_1$ 必须是动力学固定点且稳定：$\Pi_\Delta(\alpha(\hat{G}_\theta(x^*)-x^*)-\lambda\nabla F(x^*))=0$, $\text{Re}(\lambda_J)<0$。

**Sketch**：若 $\dot{\rho}=\mathcal{L}(\rho)$ 为 Lindblad 半群，且退相干速率压倒读出速率，则 $\mathcal{L}$ 在观测子空间上为收缩映射，存在唯一稳定固定点 $\rho^*$，对应稳定指针态。

---

## II. Non-Locality & Entanglement (非定域性与纠缠)

### Ax-Quant-4 [A1.2.1]: $L_0$ Topological Unity (L₀拓扑统一性)
Spatial separation is an emergent property of $L_1$/$L_2$; in $L_0$, the universe is topologically connected.
$$ \text{Distance}_{L_0}(A, B) \approx 0 \implies \text{Entanglement is default, not special} $$
*   **Reframing**: Entanglement is not a "connection" between separate objects—it is the **failure of $L_2$ to impose separation** on an originally unified $L_0$ structure.

### Ax-Quant-5 [A1.2.2]: Entanglement Unity Theorem (纠缠统一定理)
Entangled states are ontologically irreducible in $L_0$:
$$ |\Psi_{AB}\rangle \in L_0 \neq |A\rangle \otimes |B\rangle $$
*   **Mechanism**: When $\hat{G}_\theta$ acts on entangled particles, it operates at the $L_0$ source—both $L_1$ projections ("shadows") update simultaneously because they share a single high-dimensional origin.
*   **O-T2 Link**: 可分解态对应 $L_0$ 结的“解结”操作：$L_2^{new} = L_2^{old}\cdot \prod \gamma_i^{-1}\cdot \prod \gamma'_j$。

---

## III. History & Time (历史与时间)

### Ax-Quant-6 [A1.3.1]: Retroactive Participancy (回溯性参与)
History is a back-projection from the current selection moment, not a pre-existing timeline.
$$ \text{History}(t < t_{now}) = \text{BackProject}\left(\hat{G}_\theta[t_{now}]\right) $$
*   **Wheeler's Insight Formalized**: The past is determined by current $L_1$ anchoring. This is not "changing history" but **constructing history at the moment of selection**.
*   **Source**: Extends Core Axiom A3 (Causality as Projection).
*   **T-Phase-1 Link**: $v_{sub}=\dot{\phi}/\phi_0$ 给出“选择节拍”与历史塑形的速率尺度。

### Ax-Quant-7 [A1.3.2]: History Plasticity (历史可塑性)
The malleability of past events is inversely proportional to their temporal distance and directly proportional to observer participancy:
$$ P_{history} \propto D_p \cdot (\Delta t)^{-1} $$
where $D_p$ is the Degree of Participancy (see Core Reference §7.1).
*   **Implication**: Recently selected events are more "plastic" than deeply entrenched $L_2$ structures.

---

## IV. Semantic Completion (语义完备性)

### Ax-Quant-8 [A1.4.1]: Semantic Entanglement (语义纠缠)
Complete collapse requires both physical state anchoring and semantic meaning anchoring.
$$ \text{Collapse}_{total} = \hat{G}_{phys}[L_0 \to L_1] \otimes \hat{G}_{sem}[L_0 \to L_1] $$
*   **Schrödinger-Le Guin Insight**: Physical decoherence without meaning is an incomplete reality. The same physical event has different $L_2$ "weight" for different observers depending on semantic anchoring.
*   **Derivation**: Explains why the same event produces different "historical importance" across observers.

---

## V. Synthesis: SRT vs. Interpretations (诠释综合)

### Theorem T-Quant-Synthesis [T1.5.1]: Meta-Interpretational Framework
SRT provides a meta-framework that synthesizes valid insights from competing interpretations:

| Interpretation | Valid Insight | SRT Formalization |
|:---------------|:--------------|:------------------|
| **Copenhagen** | Measurement causes collapse | $\hat{G}_\theta$ executes selection |
| **Many-Worlds** | No objective collapse | $L_0$ contains all branches; $L_1$ is observer-relative |
| **QBism** | Wavefunction is subjective belief | $\theta$ parameters encode observer's stance |
| **Relational QM** | Facts are observer-relative | $L_1(\theta_A) \neq L_1(\theta_B)$ until $L_2$ sync |
| **Pilot Wave** | Guiding field exists | $L_0$ gradient structure ($\nabla F$) guides selection |
| **Objective Collapse** | Gravity triggers collapse | $\Psi_f > \Psi_{crit}$ forces $\hat{G}$ activation |

*   **Unique Contribution**: SRT explains how subjective selections (QBism, RQM) converge into stable objective reality ($L_2$) through consensus dynamics.

<br>
<br>

---
---

# Part B: Original Theoretical Discourse (Context)

> **Note**: This section provides the detailed philosophical motivation, experimental analysis, and conceptual elaboration for the quantum axioms.

---

# §0. Why Quantum Mechanics Needs SRT

## 0.1 The Interpretational Crisis

Quantum mechanics is the most successful predictive framework in physics, yet after a century, its interpretation remains contested. The core difficulty is the **measurement problem**: the formalism does not specify when or how wavefunction collapse occurs.

### 0.1.1 The Three Foundational Problems

| Problem | Description | Mainstream Difficulty |
|:--------|:------------|:---------------------|
| **I. Measurement Problem** | When/how does collapse occur? | No objective criterion; requires "observer" |
| **II. Non-Locality** | How do entangled particles correlate instantly? | Tension with relativistic causality |
| **III. Quantum-Classical Boundary** | Why is the macroscopic world classical? | Decoherence is necessary but not sufficient |

### 0.1.2 SRT's Fundamental Reframing

SRT reframes quantum mechanics as a **Selection-Anchoring-Manifestation** process:

$$ \text{Quantum State} = L_0 \text{ (Superposition of Possibilities)} $$
$$ \text{Collapse} = \hat{G}_\theta[L_0 \to L_1] \text{ (Selection-Anchoring)} $$
$$ \text{Measurement Outcome} = L_1 \text{ (Manifest Reality)} $$

**The Key Insight**: Collapse is not a mysterious physical process—it is the **ontological act of selection** that creates determinate facts from indeterminate potential. The "measurement problem" dissolves when we recognize that measurement *is* selection.

---

## 0.2 Classical Experiments Reinterpreted

### 0.2.1 Double-Slit Experiment: Superposition of Selection

**Experimental Finding**: Single electrons passing through a double slit exhibit wave-like interference patterns. Attempting to detect which slit the electron passed through destroys the interference.

**SRT Interpretation**:

$$ \text{Double-Slit Superposition} = L_0[\text{Path A} \oplus \text{Path B}] \text{ (Selection not yet executed)} $$
$$ \text{Detection} = \hat{G}_\theta[\text{A or B}] \to L_1 \text{ (Selection occurs)} $$

**Core Insights**:
1. **Interference = $L_0$ possibilities self-interfering before $L_1$ manifestation**
2. **Detection = $\hat{G}_\theta$ executing selection, compressing $L_0$ to $L_1$**
3. **Interference Disappearance = Selection completed; only outcome remains**

$$ \text{Interference} \iff L_0 \text{ unselected} $$
$$ \text{No Interference} \iff L_0 \text{ anchored as } L_1 $$

**SRT Reinterpretation**: The electron doesn't "go through both slits"—the question assumes $L_1$ categories apply to $L_0$ states. Before selection, there is no fact about "which path."

---

### 0.2.2 Wheeler Delayed-Choice Experiment: Temporal Non-Locality of Selection

**Experimental Finding**: Even after a photon has "passed through" the double slit, deciding whether to detect path information still affects the interference pattern. The photon appears to "retroactively" change its behavior.

**SRT Interpretation**:

$$ \text{Delayed Choice} = \hat{G}_\theta \text{ at } L_1 \text{ anchoring determines "history" of } L_0 $$

**Core Insights**:
1. **"The Past" is not pre-stored but constructed at selection**
2. **Time at $L_0$ level is non-linear**—only $L_1$ anchoring produces definite temporal sequence
3. **Wheeler's intuition confirmed**: Participatory universe

$$ \text{Timeline} = L_2[\text{Causal narrative after selection}] \neq \text{Pre-existing objective past} $$

#### 0.2.2a History Construction Equation

**Core Proposition**: $L_2$ (history/vergence domain) is not a pre-existing linear timeline but a **trajectory projection** left by $\hat{G}_\theta$ selecting at the current moment.

**Formal Statement**:
$$ \text{History}(t < t_{now}) = \text{BackProject}\left(\hat{G}_\theta[t_{now}]\right) $$

**Key Corollaries**:
1. **"The past" is a by-product of present selection**: Establishing an $L_1$ state simultaneously "collapses" a historical path leading to it
2. **History non-uniqueness**: The same $L_1$ state may correspond to multiple possible $L_0 \to L_1$ paths; $\hat{G}$ selection determines "which path actually occurred"
3. **Retroactive participancy**: Observers don't just create the present—they participate in constructing the past

**Cosmological Extension**:
$$ \text{Big Bang Conditions} = \text{BackProject}\left[\sum_{\theta \in \text{all observers}} \hat{G}_\theta\right] $$

The "initial conditions" of the universe are the retroactive projection of all subsequent $\hat{G}$ systems (including us). This is Wheeler's "It from Bit" expressed cosmologically in SRT.

---

### 0.2.3 Schrödinger's Cat: Macroscopic Superposition and $L_2$ Classicalization

**SRT Interpretation**:

$$ \text{Cat Superposition} = L_0[\text{Alive} \oplus \text{Dead}] $$
$$ \text{Observation} = \hat{G}_\theta[\text{Specific Outcome}] \to L_1 $$
$$ \text{Classical Cat} = L_2[\text{Stable Macroscopic State}] $$

**Core Insights**:
1. **The question is not "when does the cat collapse" but "when does $\hat{G}$ execute"**
2. **Macroscopic systems have high $L_2$ stability** leading to rapid selection convergence
3. **"Observation" doesn't require consciousness**—any $\hat{G}_\theta$ (including environment) suffices

$$ \text{Decoherence} = \sum_{\theta \in \text{Environment}} \hat{G}_\theta \text{ causing rapid } L_2 \text{ stabilization} $$

#### 0.2.3a The Schrödinger-Le Guin Paradox: Semantic Entanglement

**Core Insight**: Physics concerns only the cat's life/death (physical state); literature concerns the cat's existential meaning (semantic state). SRT proposes: **Complete collapse must include both dimensions.**

**Proposition (Semantic Entanglement)**:
Physical state collapse must be accompanied by semantic state collapse. If the physical result (alive/dead) produces no semantic meaning, the collapse is **incomplete**.

$$ \text{Complete Collapse} = \hat{G}_\theta^{physical}[L_0 \to L_1] \otimes \hat{G}_\theta^{semantic}[L_0 \to L_1] $$

**Corollary**: Pure physical decoherence completes only half the collapse. Full $L_2$ formation requires semantic participation—this explains why the same event has different "historical weight" ($L_2$ depth) for different $\hat{G}_\theta$.

---

### 0.2.4 Quantum Eraser: Reversibility of Selection

**SRT Interpretation**:

$$ \text{Detection} = L_0 \xrightarrow{\hat{G}} L_1[\text{Path Determined}] $$
$$ \text{Erasure} = L_1 \text{ information correlation severed} \Rightarrow L_0 \text{ reopens for interference} $$

**Core Insights**:
1. **Selection ($\hat{G}$) results are stored in $L_2$ information correlations**
2. **Erasure = Severing $L_2$ correlations**, allowing $L_0$ to "reopen"
3. **This proves selection is an information process, not physical demolition**

$$ \text{Collapse} \neq \text{Irreversible Physical Process} \quad ; \quad \text{Collapse} = L_2 \text{ Information Anchoring} $$

---

### 0.2.5 Aspect Experiment & Bell Inequalities: Non-Local Selection

**SRT Interpretation**:

$$ |\Psi_{AB}\rangle \in L_0 \neq |A\rangle \otimes |B\rangle \text{ (Ontologically irreducible)} $$
$$ \text{Measurement} = \hat{G}_\theta^A \cap \hat{G}_\theta^B \text{ (Synchronized selection at source)} $$

**Core Insights**:
1. **No spatial separation at $L_0$ level**—separation is $L_1$/$L_2$ property
2. **Entanglement = $L_0$ irreducibility** manifesting as correlation in $L_1$ projection
3. **No information transmission** because correlation is selection outcome, not signal

$$ \text{Non-Locality} = L_0 \text{ is unified} \quad ; \quad \text{Locality} = L_1/L_2 \text{ property} $$

**Connection to ER=EPR**: The Maldacena-Susskind conjecture (Entanglement = Wormhole) receives natural SRT interpretation:
$$ \text{Entanglement (Quantum)} \equiv \text{Wormhole (Gravity)} \equiv L_0 \text{ Irreducibility} $$

---

### 0.2.6 Quantum Zeno Effect: Frequent Selection Freezes Evolution

**SRT Interpretation**:

$$ \text{Zeno Effect} = \lim_{\Delta t \to 0} [\hat{G}_\theta]^{N \to \infty} = \text{State Lock} $$

**Core Insights**:
1. **Selection = Compressing $L_0$ to $L_1$**; each selection "resets" evolution
2. **Frequent selection = Repeatedly pulling system back to same $L_1$**
3. **Evolution requires $L_0$ "expansion time"**—frequent selection denies this

$$ \text{Quantum Evolution} \propto L_0 \text{ degrees of freedom between selections} $$

---

## 0.3 Five Core Corollaries of SRT Quantum Mechanics

### Corollary I [C2.1.1]: Measurement as Operator Sharpening

**Fourier Perspective Correction**: Heisenberg uncertainty $\Delta x \Delta p \geq \hbar/2$ is not merely precision limitation—it is **ontological bandwidth constraint**.

- **Position ($x$)** = Time-domain / $L_1$ event (Event-like)
- **Momentum ($p$)** = Frequency-domain / $L_0$ structure (Wave-like)

When you try to completely "nail down" a particle at a point in $L_1$ ($\Delta x \to 0$), you force $\hat{G}$ to superpose all frequency components in $L_0$ ($\Delta p \to \infty$).

**Conclusion**: Particle-nature is not matter's intrinsic property—it is the result of **extreme Fourier transformation** we impose on $L_0$.

### Corollary II [C2.1.2]: $L_0$ Has No Time, No Space

$$ L_0 : \text{Possibility Space} \neq \text{Objects in Spacetime} $$

Time and space are $L_1$/$L_2$ properties. $L_0$ itself is non-local, non-temporal.

### Corollary III [C2.1.3]: Quantum-Classical Boundary = $L_2$ Stability Threshold

$$ \text{Classicality} = L_2[\text{Multi-operator selection convergence stability}] $$

Macroscopic systems appear classical because multiple $\hat{G}_\theta$ selections rapidly converge.

### Corollary IV [C2.1.4]: Entanglement = $L_0$ Irreducibility

$$ |\Psi_{entangled}\rangle = L_0[\text{Whole}] \neq L_0[A] \otimes L_0[B] $$

Non-local correlation is the manifestation of $L_0$ unity in $L_1$ projection.

### Corollary V [C2.1.5]: Participatory Universe

$$ \text{Reality} = \sum_\theta \hat{G}_\theta[L_0] \text{ (Sum of Selections)} $$

Wheeler's intuition confirmed: Observers are not passive recorders but co-creators of reality.

---

## 0.4 Why Existing Interpretations Are Insufficient

| Interpretation | Core Claim | SRT Critique |
|:---------------|:-----------|:-------------|
| **Copenhagen** | Measurement causes collapse | Fails to define "measurement" |
| **Many-Worlds** | No collapse, branching | Ontological extravagance, unverifiable |
| **Pilot Wave (Bohm)** | Hidden variables + guiding wave | Non-local potential is awkward |
| **QBism** | Subjective belief | Evades ontological commitment; cannot explain consensus |
| **Objective Collapse (GRW)** | Spontaneous localization | Requires fine-tuned parameters |
| **Decoherence** | Environment-induced | Doesn't explain why *this particular* outcome |

**SRT's Unique Advantages**:
- **Unified Framework**: Measurement, collapse, entanglement, classicalization all explained by $\hat{G}[L_0 \to L_1]$
- **Ontological Commitment**: Selection is ontologically primitive, not epistemic addition
- **Resolves Measurement Problem**: $\hat{G}$ provides objective selection criterion
- **Compatible with Relativity**: $L_0$ non-locality doesn't violate causality (no information transfer)
- **Explains Consensus**: $L_2$ convergence mechanism bridges subjective selections to objective reality

---

## 0.5 Experimental Predictions

| ID | Hypothesis | Prediction | Falsification Condition |
|:---|:-----------|:-----------|:------------------------|
| **H-QM-1** | Measurement Independence | Statistics depend only on $\theta$ information parameters, not physical substrate | Different substrates with same $\theta$ yield different statistics |
| **H-QM-2** | Semantic Completion | Events with semantic anchoring should show stronger $L_2$ consolidation | Semantic content has no effect on decoherence dynamics |
| **H-QM-3** | History Plasticity | Recent selections more malleable than ancient $L_2$ | No correlation between temporal distance and modification difficulty |
| **H-QM-4** | Zeno Threshold | Exists minimum selection interval $\tau_{min}$ below which Zeno effect saturates | Zeno effect scales continuously to arbitrarily small intervals |

---

## Symbol Index (符号索引)

| Symbol | Name | Definition Location |
|:-------|:-----|:--------------------|
| $\hat{G}_\theta$ | Ghost Operator / Selection Operator | Ax-Quant-1 [A1.1.1] |
| $L_0$ | Latent Domain / Hilbert Space | §0.1.2 |
| $L_1$ | Manifest Domain / Pointer States | §0.1.2 |
| $L_2$ | Vergence Domain / Physical Laws | §0.1.2 |
| $\Delta S_{entanglement}$ | Entanglement Entropy Change | Ax-Quant-3 [A1.1.3] |
| $\Delta I_{classical}$ | Classical Information Gain | Ax-Quant-3 [A1.1.3] |
| $D_p$ | Degree of Participancy | Ax-Quant-7 [A1.3.2] |
| $P_{history}$ | History Plasticity | Ax-Quant-7 [A1.3.2] |
| $\hat{G}_{sem}$ | Semantic Selection Operator | Ax-Quant-8 [A1.4.1] |
