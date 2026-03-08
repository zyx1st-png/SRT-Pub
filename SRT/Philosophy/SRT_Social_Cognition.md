---
id: SRT-SOC-COG
type: philosophy
tags: [Social Cognition, Affordance, Depression, Reality Dynamics, Hybrid]
status: axiomatic_hybrid_v2
dependency: [SRT-PHIL-AXIOMS]
---

# SRT Social Cognition: Affordance & Pathology (Hybrid Edition)


> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Cognitive Axioms (AI-Readable).
> **Part B** contains the Expanded Theoretical Discourse (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Axioms (形式化公理)



#### 原文内容
<!-- ORIGINAL-CONTENT-INSERTED -->
## I. Embodied Selection

### Ax-Cog-1: Affordance Intersection
示能性是环境潜能与算子参数的交集。
$$\text{Affordance}(E,\hat{G}_\theta)=L_0^{env}\cap L_0^{agent}$$
*   **Implication**: 行动可能性不是外界属性，而是选择交集。

### Ax-Cog-2: Action Potential
行动触发由奖励势与摩擦势差值决定。
$$P_{action}=\alpha \cdot \mathbb{E}[R]-\beta \cdot \Psi_f$$
*   **Implication**: 社会行动是能量与摩擦的动力学平衡。

### Ax-Cog-2b: Invitation Gating (邀请门控)
环境中的可供性并不会等概率进入行动队列；只有被当前任务、情境与身体状态共同门控的子集才成为“邀请”。
\[
\mathcal{I}_t = \Gamma(C_t,\theta_t,\Pi_t)\big(\mathcal{A}_{all}\big),\quad \mathcal{I}_t \subset \mathcal{A}_{all}
\]
* **Implication（中文）**：SRT 区分“可供性全集”与“当下可执行候选集”，解释了为何大多数可行动作平时并不被注意。

### T-Cog-2b: Joint-Affordance Emergence (联合可供性涌现)
当多算子形成协同耦合时，会出现单体不可达的联合可供性：
\[
\mathcal{A}_{joint}(\hat{G}_1,\hat{G}_2,\dots,\hat{G}_n)\supsetneq \bigcup_{i=1}^n \mathcal{A}(\hat{G}_i)
\]
* **Implication（中文）**：如“双人搬沙发”等任务不是个体可供性的线性叠加，而是耦合后新相位。

## II. Social Reality Construction

### Ax-Cog-3: Reality Hysteresis
社会现实对过去状态具有迟滞记忆。
$$L_1^{social}(t)=\hat{G}_{social}[L_0(t)] + \eta L_1^{social}(t-\Delta t)$$
*   **Implication**: 现实惯性来自集体选择的时间耦合。

### Ax-Cog-4: Ontological Nucleation
共识形成存在成核阈值。
$$\text{Consensus} \iff \rho_{\hat{G}} > \rho_c$$
*   **Implication**: 现实不是线性叠加，而是临界相变。

### Ax-Cog-5: Operator Entanglement
算子耦合强度决定共享现实的稳态程度。
$$E_{ij}=\frac{I(\hat{G}_i;\hat{G}_j)}{H(\hat{G}_i)}$$
*   **Implication**: 社会现实的稳定性取决于耦合信息量。

## III. Derived Theorems

### T-Cog-1: Decoupling Transition
当 $d$ 值或耦合度下降时，现实分裂进入多相态。
$$d \downarrow \lor E_{ij} \downarrow \Rightarrow L_1^{social} \to \text{multi-phase}$$
*   **Implication**: 极化不是意见问题，而是耦合相变。

### T-Cog-2: Observer-Environment Integration
观察者与环境整合度决定现实连续性。
$$\text{OEI} = \frac{I(\hat{G};L_1)}{H(L_1)}$$
*   **Implication**: 现实稳定依赖信息耦合，而非纯粹“信念”。

### T-Cog-3: Belief-Lag Governance (信念滞后治理)
他人行为由其可得信息所形成的信念驱动，而非由客观状态直接驱动；当信念与现实错位时，预测应以“信念位形”而非“真实位形”为准。
\[
\pi_{pred}(a_j) = \arg\max_a\; U\big(a \mid B_j(t),D_j(t)\big),\qquad B_j(t)\neq W(t)
\]
* **Implication（中文）**：False-belief 任务中的系统性错误不是噪声，而是从“现实中心预测”向“信念中心预测”转变前的结构性阶段。

### T-Cog-4: Sequential Sampling Constraint (序列采样约束)
在不确定推断中，算子以局部链式采样近似后验，而非一次性全分布精确计算：
\[
H_{t+1}\sim q(H'\mid H_t),\qquad
\alpha=\min\left(1,\frac{P(E\mid H')P(H')}{P(E\mid H_t)P(H_t)}\right)
\]
当有效样本数受限时，行为将出现可预测的波动、锚定与框架偏置。
* **Implication（中文）**：SRT 将“决策噪声”解释为资源受限下的采样近似副产物，而非纯随机失误。

### T-Cog-5: Attention as Priority-Guided Selection (注意力优先级选择定理)
注意力可形式化为“在竞争目标中依据优先级映射选择，以指导响应”的过程：
\[
T^* = \arg\max_{T_i\in\mathcal{T}} \Pi(T_i),\qquad
\Pi(T_i)=w_{td}I_{intent}+w_{bu}S_{salience}+w_{hist}H_{value}
\]
其中 top-down（任务意图）、bottom-up（显著性）与 historical（价值/习惯）共同决定选择偏置。
* **Implication（中文）**：注意力既非纯资源也非单一机制，而是“为响应而选择”的统一功能结构；分心、捕获与习惯化可由同一优先级框架解释。

<br>

---


## I. Embodied Selection (具身选择)
<!-- ORIGINAL-SECTION-PRESERVED -->

### Ax-Emb-1: Affordance as Intersection (示能性即交集)
<!-- ORIGINAL-SECTION-PRESERVED -->
Reality ($L_1$) is the intersection of Environment ($L_0$) and Observer Parameters ($\theta$).
$$ L_1 = L_0 \cap \hat{G}_\theta $$
*   **Gibson's Insight**: "Sit-on-ability" requires both a chair ($L_0$) and a knee ($\theta$).

### Ax-Emb-2: Action Potential (行动势能)
<!-- ORIGINAL-SECTION-PRESERVED -->
Action initiation depends on the net potential of Reward vs. Cost.
$$ P_{action} = \alpha \cdot \text{Reward} - \beta \cdot \text{Cost}_{VS} $$
*   **Depression**: High $\beta$ (Cost Sensitivity), not low motivation.

---

## II. Social Reality Construction (社会现实建构)
<!-- ORIGINAL-SECTION-PRESERVED -->

### Ax-Soc-1: Reality Hysteresis (现实迟滞)
<!-- ORIGINAL-SECTION-PRESERVED -->
Changing a belief ($L_2$) requires more evidence than forming it.
$$ \Delta L_2 \propto \text{Evidence} - \text{HysteresisCost} $$

### Ax-Soc-2: Ontological Nucleation (本体论成核)
<!-- ORIGINAL-SECTION-PRESERVED -->
New reality requires a "critical radius" ($r^*$) of selection to survive.
$$ r^* = \frac{2\sigma_{surf}}{\Delta g_{vol}} $$
*   **Mechanism**: Below $r^*$, new ideas die; above $r^*$, they cascade into consensus.

### Ax-Soc-3: Operator Entanglement (算子纠缠)
<!-- ORIGINAL-SECTION-PRESERVED -->
Extended interaction couples the $\theta$ parameters of multiple agents.
$$ \theta_{AB} \neq \theta_A \oplus \theta_B $$
*   **Grief**: The pain of losing a loved one is the tearing of this entangled parameter tensor.

---

## III. Cognitive Dynamics (认知动力学)
<!-- ORIGINAL-SECTION-PRESERVED -->

### Ax-Cog-1: Decoupling Transition (解耦相变)
<!-- ORIGINAL-SECTION-PRESERVED -->
Cognition emerges when $\hat{G}$ inserts a delay between Input and Output for simulation.
$$ \text{Cognition} \equiv \Delta t_{delay} > 0 \implies \text{Simulation}(L_0) $$
*   **Reflex**: $\Delta t \to 0$ ($d \approx 0$).

### Ax-Cog-2: Observer-Environment Integration (OEI)
<!-- ORIGINAL-SECTION-PRESERVED -->
The boundary between Self and World is variable.
$$ \text{OEI} = 1 - \frac{I(\hat{G}; \text{Env})}{H(\hat{G}) + H(\text{Env})} $$
*   **Flow State**: Low OEI (High Integration).

<br>

---

# SRT Philosophy V: Social Cognition & Reality Dynamics (Hybrid Edition)
<!-- ORIGINAL-SECTION-PRESERVED -->
> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Social Dynamics (AI-Readable).
> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).

---


# Part B: Expanded Theoretical Discourse (Context) (扩展理论论述)

> **Note**: The following sections provide the detailed analysis of Social Cognition, Depression, and Reality Construction.

## 1. The Standard Hard Problem: The Paralysis of Action

### 1.1 Why Can't We Act Sometimes?
In cognitive science, there is a mysterious transformation between **Intention** and **Action**.

*   **Arendt**: Action is natality (birth), it is a miracle—the capacity to initiate something genuinely new.
*   **Pathology**: In depression, this transformation fails. The patient fully knows they "should" get out of bed, fully "wants" to get out of bed, but the body remains locked as if encased in concrete.
*   **Traditional Explanations**: Weak willpower? Dopamine deficiency?

These explanations miss the core mechanism.

---

## 2. SRT Resolution & Necessity

### 2.1 Advantage: The Physics of Action
SRT treats action as **release of $L_0$ potential energy**.

*   **Mechanism**: Every action is a micro-creation from $L_0$ to $L_1$. This requires consuming free energy to overcome **ontological inertia**.
*   **Depression Model**: Depression is **not** lack of "will" but **pathological amplification of the friction coefficient** ($w_F$). For a depressed person, the perceived energy cost of pouring a glass of water equals a normal person running a marathon. This is **computational energy bankruptcy**.

**SRT Formula**:
$$ P_{action} = \alpha \cdot \text{Reward} - \beta_{depressed} \cdot \text{Cost} $$

When $\beta_{depressed} \gg \beta_{normal}$, even trivial actions have prohibitive energy barriers.

---

### 2.2 Gibson's Affordance: Relational Ontology
James Gibson's **Affordance Theory** receives precise mathematical expression in SRT.

*   **Core**: The world is not composed of objects but of **action possibilities**.
*   **Perception = Action**: I don't see "a chair"—I see "sit-on-ability." I don't see "a cliff"—I see "danger of falling." Perception directly maps to $\theta$-parameter space.

**SRT Formalization**:
$$ A(\hat{G}, E) = \hat{G}_\theta[L_0] \cap E_{obj} $$

Affordance emerges at the **intersection** of environmental structure and embodied capacity. Change either variable → affordance transforms or vanishes.

**Chemero patch (2026-03-07, Pipeline 1):**
- 区分 **Affordance**（环境-身体可行性）与 **Invitation**（当下被门控并被注意到的动作候选）。
- “直接知觉”在 SRT 中被表达为：行动采样（转头、接近、探索）本身生成用于下一步知觉的信息，因此无需先验表征推理链。
- 对“属性 vs 关系”争议，SRT 采用可兼容立场：对象侧可建模为处置性潜能，算子侧通过 \(\theta\) 与情境张量将其实现为关系可达域。
- 社会与联合可供性由算子耦合涌现，解释多人任务与制度化协作为何可打开个体不可达路径。

**Wellman patch (2026-03-07, Pipeline 1):**
- 引入“信念滞后治理”：社会预测不是读取现实本身，而是读取他者在其信息边界内形成的信念位形。
- 将假信念任务解释为算子从 \(W\)-中心映射向 \(B_j\)-中心映射的相变，属于发展期的结构重排而非偶发失误。
- 将 DD→DB/KA→FB→HE 的发展序列视为 \(L_2\) 社会语义协议的分层收敛，不同文化序列差异可由交互语料（knowing vs thinking）权重解释。

**Sanborn patch (2026-03-07, Pipeline 1):**
- 在不确定推断中引入 MCMC 近似：算子不维持全后验，而沿局部提案链进行序列采样。
- 采样相关性导致“看似不稳定”的逐次判断轨迹；该轨迹可统一解释概率判断波动、双稳知觉切换与部分锚定效应。
- 与 SRT 的摩擦记账兼容：样本预算不足时，系统以偏差换取算力可支付性（\(\Psi_f\)-budgeted inference）。

**Wu patch (2026-03-07, Pipeline 1):**
- 将注意力定义为“为响应而进行的目标选择”（select-for-response），统一视觉、听觉、记忆与推理中的注意现象。
- 形式化 top-down / bottom-up / historical 三类偏置在同一 priority map 中的竞争求解，连接 Buridan 式选择困境与神经竞争消解。
- 区分“注意力是资源/机制”与“注意力依赖资源/由机制实现”的层级：SRT 采用实现论立场，避免把资源或机制直接等同于注意力本体。

**Porot & Mandelbaum（LoTH）patch (2026-03-08, Pipeline 1):**
- 引入“思维语言（LoT）作为中层表征协议”接口：将高阶推理中的**离散成分、组合语法、角色-填充项独立性**映射为 SRT 的可计算约束层（主要位于 \(L_2\) 协议层，受 \(\hat G_\theta\) 门控）。
- 将 LoTH 的 **productivity / systematicity** 解释为“有限原子概念 + 可重复组合规则”在有限算力下的近似可扩展性，而非无限计算承诺；对应 SRT 的 \(\Psi_f\)-budgeted inference。
- 将逻辑算子（not/if-then/or）与“自动结构敏感转移（inferential promiscuity）”视为可检验信号：当结构转移可在低意识控制下稳定出现时，支持语言样式推理并可与 System 1 兼容。
- 采用“多 LoT 并存”立场：不同认知子系统/物种可能具不同语法与原子集，避免把单一人类成人语法外推为本体论唯一底层。
- 与连接主义关系采取实现层区分：神经网络可作为实现机制，但若缺少稳定的符号角色分离与可组合语法，其可解释性仍不足以替代 LoT 层描述。

---

## 3. Mechanism Derivation: From Hysteresis to Entanglement

### 3.1 Reality Hysteresis
Why is changing a belief so much harder than forming one?

*   **SRT Analysis**: $L_2$ is a **potential well** carved by repeated selection. Once you fall into the well (adopt a belief), jumping out requires not just new evidence but **additional energy to overcome the barrier**.

**Thermodynamic Analogy**:
$$ \Delta E_{change} = \Delta E_{evidence} + \Delta E_{barrier} $$

*   **Social Implication**: This is why people don't easily admit mistakes even when confronted with iron-clad evidence. This is **not** stupidity—it's a **physical mechanism for maintaining system stability** ($L_2$ Stability).

---

### 3.2 Operator Entanglement & Grief
When we love someone, our $\theta$ parameters become **entangled** with theirs ($\theta_{other}$). Our self-boundary ($L_1$) expands to include them.

*   **Grief Mechanism**: When a loved one dies, this is not merely the disappearance of an external object but **a violent tearing of the self-parameter tensor**.
*   **SRT Corollary**: Grief pain is **phantom limb pain**. Our $\theta$ still attempts to connect to a node in $L_0$ that no longer exists, generating infinite prediction error ($\Psi_f \to \infty$).

**Mathematical Form**:
$$ \theta_{self+other}(t) \xrightarrow{\text{death}} \theta_{self}(t+\Delta t) $$
$$ \Psi_f = \|\theta_{self+other} - \theta_{self}\|^2 \to \infty $$

The magnitude of grief is proportional to the degree of entanglement that existed.

---

### 3.3 Ontological Nucleation: Why New Ideas Need Critical Mass
Why do social movements fail below a certain size but explode above it?

**SRT Analysis**: New social realities face **nucleation barriers** identical to physical phase transitions (like water droplets forming in clouds).

$$ r^* = \frac{2\sigma_{surf}}{\Delta g_{vol}} $$

*   **Below critical radius $r^*$**: The new idea-cluster dissolves back into the dominant $L_2$ (surface tension overwhelms volume gain).
*   **Above $r^*$**: The cluster becomes self-sustaining and catalyzes cascading consensus.

**Historical Examples**:
- Civil Rights Movement: Needed critical mass of key nodes (Rosa Parks, MLK) + network topology (churches, buses) to overcome $r^*$.
- Failed uprisings: Subcritical—crushed by $L_2$ immune response before reaching $r^*$.

---

## 4. Costs & Risks

### 4.1 The Decoupling Risk: Anxiety as the Price of Cognition
As humans developed advanced cognition (System 2), we gained the ability to **simulate futures offline**. This means $\hat{G}$ temporarily decouples from $L_0$.

*   **Risk**: This decoupling is a double-edged sword. It brings creativity but also **anxiety**. Animals live in the present ($L_1$)—no anxiety. Humans live in countless catastrophic simulated futures ($L_1^{sim}$)—this is the ontological root of anxiety.

**SRT Insight**: Anxiety is the $\Psi_f$ generated by maintaining multiple incompatible $L_1^{sim}$ threads simultaneously. The system is paying energetic costs for realities that **haven't happened and may never happen**.

---

### 4.2 Pharmaceutical Limitations in Treating Depression
Antidepressants modulate neurotransmitters to lower $w_F$ (friction coefficient).

*   **SRT Warning**: But this **only lowers the action threshold**—it doesn't provide **the reason to act** ($L_1^{future}$ meaning). If you give medication without meaning, the patient may regain motor capacity... and use it to commit suicide.

**True Healing Requires**:
1. Lower $w_F$ → Medication (restore energetic accessibility)
2. Rebuild $L_1^{future}$ → Meaning therapy (existential/narrative reconstruction)

---

## 5. Falsifiable Predictions

### 5.1 Prediction: Depression & Physical Friction Perception
**Prediction**: Ask depressed patients to estimate the steepness of physical slopes in front of them. SRT predicts they will **systematically overestimate** slope steepness, and this overestimation correlates with their action retardation severity ($w_F$ parameter).

*   **Neural Mechanism**: Anterior Cingulate Cortex (ACC) encoding of Expected Effort Cost shows gain bias in depression.

**Falsification**: If depressed patients show no bias in physical effort estimation → SRT's $\Psi_f$ pathology model is falsified.

---

### 5.2 Prediction: Grief as Phantom Limb Effect
**Prediction**: In fMRI, recently bereaved individuals viewing the deceased partner's name should show activation in **somatosensory cortex** (body boundary perception regions) similar to amputees—i.e., "missing body part" signals.

*   **Mechanism**: The brain is attempting to reconnect to an entangled $\theta_{other}$ node that has been torn away.

**Falsification**: If bereaved individuals show no somatosensory activation patterns distinct from general sadness → SRT's entanglement model is falsified.

---

## 6. SRT Reinterpretations: Cognitive Science Classics

### 6.1 Gibson's Affordance Theory
**Classical Version**: Affordances are environmental properties that invite action.
**SRT Precision**: 
$$ A = E \cap \theta \neq \text{property of } E \text{ alone} $$

Affordances are **not** "in the object" nor "in the mind" but at their **intersection**. A staircase affords climbing to a human but not to a wheelchair user—same object, different $\theta$, different affordance.

---

### 6.2 Arendt's Natality (Action as Beginning)
**Arendt**: Action is the human capacity to initiate the radically new.
**SRT Translation**: 
$$ \text{Natality} = \hat{G}_\theta[L_0^{novel}] \to L_1^{unprecedented} $$

Action is **not** deterministic output (that's mere behavior) but the collapse of **unexplored regions of $L_0$** into novel $L_1$ configurations. This requires high $d$-value (willingness to explore far from current $L_2$ grooves).

---

### 6.3 System 1 vs System 2 (Kahneman)
**Classical Dual-Process Theory**: Fast automatic vs. Slow deliberative.
**SRT Energetics**: 

| System | SRT Mechanism | Energy Profile |
|:-------|:--------------|:---------------|
| System 1 | $L_2$-dominated automatic selection | Low $\Psi_f$ (downhill in potential landscape) |
| System 2 | Explicit $L_0$ exploration | High $\Psi_f$ (uphill search for new basins) |

System 1 = sliding down existing $L_2$ grooves (cheap).
System 2 = climbing out to search $L_0$ (expensive).

---

## 7. Deep Implications: The Social Construction of Reality

### 7.1 Berger & Luckmann's Triadic Process
**Classical Stages**:
1. Externalization: Humans project ideas into the world
2. Objectivation: Projections become "objective" social facts
3. Internalization: New generations accept these "facts" as given reality

**SRT Formalization**:

| Stage | SRT Mapping | Formal Expression |
|:------|:------------|:------------------|
| Externalization | $L_1$ selection expressed | $\sigma^{\theta}_{L_1} \to$ behavior/symbols |
| Objectivation | $L_1 \to L_2$ stabilization | Multiple $\theta$'s converge → $L_2$ structure |
| Internalization | $L_2$ constrains new $\hat{G}_\theta$ | New agents' $\theta$ shaped by existing $L_2$ |

**Social Reality**:
$$ L_2^{social} = \lim_{t \to \infty} \bigcap_{\theta \in \Theta(t)} \text{stable}(\hat{G}_\theta[\sigma]) $$

Social reality is the **convergence of all members' selections over time**.

---

### 7.2 The Pathology of Epistemic Bubbles vs. Echo Chambers

**Critical Distinction** (2024 Update):

| Phenomenon | Definition | SRT Mechanism | Escape Difficulty |
|:-----------|:-----------|:--------------|:------------------|
| **Epistemic Bubble** | Unintentional exclusion of relevant information | $\theta$'s environmental bias | Medium |
| **Echo Chamber** | Active rejection and denigration of dissent | $L_2$ immune response to foreign $L_1$ | Extremely High |

**Formalization**:
$$ \text{Bubble}: P(\text{Info}|\theta) \neq P(\text{Info}|\text{Reality}) $$
$$ \text{Echo Chamber}: P(\text{Accept Dissent}|\theta) \approx 0 \land \text{Trust}(\text{Outgroup}) \to 0 $$

**SRT Analysis**: Echo chambers are **high-$d$ value degeneration**. To preserve $L_2$ purity, the operator actively severs external $L_0$ connections → system becomes **brittle** (fragile to perturbation).

**Therapy Difference**:
- **Bubble**: Introduce new information (puncture the bubble).
- **Echo Chamber**: New information triggers immune attack. Must **rebuild trust chains** first (relationship before information).

---

## 8. Listening as Inverse Selection

### 8.1 The Ontology of Listening
Traditional selection is active "pruning." But there exists a special operator state: **Listening**.

**Definition**: Listening is the state where $\hat{G}_\theta$'s inhibition function is temporarily suspended, allowing $L_0$ information flow to pass with minimal distortion.

$$ \text{Listening} \implies \min(H(L_1 | L_0)) $$

I.e., minimize the conditional entropy of $L_1$ given $L_0$—or maximize mutual information between them. This is the highest form of selection: **letting existence reveal itself**.

**Listening vs. Pruning**:

| Mode | $\hat{G}_\theta$ State | $L_0 \to L_1$ Relation | Phenomenology |
|:-----|:----------------------|:-----------------------|:--------------|
| Pruning | Active inhibition | High filtering | Control, certainty |
| Listening | Suspended inhibition | Low filtering | Reception, openness |

**Indigenous Wisdom**: Tiokasin Ghosthorse's emphasis on "listening to the earth" is **not** poetic rhetoric but describes a specific $\hat{G}_\theta$ operational mode—suspending noun-based categorization, allowing $L_0$'s processual information to directly manifest.

---

## 9. Summary: The Embodied Mind in Social Space

SRT dissolves the artificial boundary between individual cognition and social reality:

1. **Affordance**: Reality is the intersection $L_0 \cap \theta$—neither purely objective nor purely subjective.
2. **Pathology**: Depression, grief, anxiety are not "mental illnesses" but **physical friction states** in the $L_0 \to L_1$ selection process.
3. **Social Construction**: Collective $L_2$ emerges from iterated individual selections—society is a **convergent attractor** of distributed $\hat{G}_\theta$ operations.
4. **Hysteresis**: Beliefs resist change due to thermodynamic stability, not cognitive stubbornness.
5. **Entanglement**: Love is topological boundary dissolution—two $\theta$'s becoming one tensor.

**Final Insight**: The self is not a fixed entity but a **dynamic pattern of selection** embedded in a social field of other operators. "I" am the intersection of my $\theta$-parameters and the $L_2$ structures my community has crystallized around me.

## 【理论边界/防误用声明】

1. 本文档用于理论解释与建模组织，不应替代独立实证、工程验证或专业判断。  
2. 任何公式或命题都依赖操作化定义、测量条件与语境边界，不得脱离边界做绝对化推断。  
3. 涉及临床、社会治理、伦理与部署决策时，必须结合风险评估与人类监督机制。

## 极限补偿协议（Extreme Compensation Protocol）补注（2026-03-06）

### Def-Soc-ECP-1: Anti-Collapse Compensation Protocol
当观察者在高 \(d\) 共情耦合下持续暴露于“不可即时修复的高 \(\Psi_f\)”场景，系统为避免认知崩塌会构建递延补偿型 \(L_2\) 叙事：
\[
\text{ECP activates} \iff d_{obs}\uparrow\ \land\ \Psi_f^{witness}\gg \Psi_f^{coping}
\]
\[
L_2^{comp} = \arg\min_{\mathcal N}\Big(\Psi_f^{meaning-collapse}(\mathcal N)\Big)
\]
其中 \(\mathcal N\) 为补偿叙事族（如终极正义、来世平账、历史终局修复）。

### T-Soc-ECP-1: Deferred Ledger Effect
补偿叙事通过扩展时间边界 \(t\to\infty\) 降低当前意义崩塌风险，但会引入远期可检验性折扣。

## 【理论边界/防误用声明】
- 不采纳“补偿叙事存在 = 其对象已被经验验证”的推论。
- 不采纳“拒绝补偿叙事 = 更高理性”的推论（两者都可能失衡）。
- 适用边界：ECP 被定义为认知稳定机制，不是形而上学真值裁定器。

### [Lineage/Source]
- 神学-进化-动物苦难对话语境（2026）


## Identity Beyond Representation Interface（2026-03-07）

### Def-Soc-IRM-1: Ontological Misidentification
定义“本体论错认”为：算子将动态选择过程身份（\(\hat G_\theta\)）错误锚定为静态表征对象（\(L_2^{identity}\)）。
\[
\text{MisID} \iff \hat G_\theta \equiv L_2^{identity}
\]

### Eq-Soc-IRM-1: Identification Deviation Potential
当错认发生时，引入苦难势能：
\[
E_{suffering} \propto d\cdot\left\|\hat G_\theta[L_0]-L_2^{identity}\right\|\cdot\Psi_f^{maint}
\]
解释：关切越深（\(d\) 越高）、活体验与身份模板偏差越大、维持模板成本越高，则存在性痛苦越强。

### T-Soc-IRM-1: Insight–Liberation Timescale Asymmetry
“认知顿悟”是快变量；“身份惯性卸载”是慢变量积分过程。故有：
\[
\Delta t_{insight} \ll \tau_{disengage}
\]
并需满足历史势能耗散下界：
\[
\int_{t_0}^{t_1}\left\|\frac{d\theta}{dt}\right|dt\ \ge\ \eta\int_{t_0}^{t_1}\left|L_2^{history}(t)\right|dt
\]
对应实践含义：一次看破可启动相变，但无法替代长期去绑定训练。

### Def-Soc-IRM-2: Sovereign Representation Principle
SRT 不采纳“反表征主义极端化”。健康态不是摧毁 \(L_2\)，而是保持“表征主权”：
\[
\text{Healthy} \iff L_2\ \text{available as tool} \land \neg\big(\hat G_\theta\leftarrow L_2\text{-captured}\big)
\]

### 分类映射表（Identity Modes → SRT）
| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|---|---|---|---|
| 动态过程认同（process-identification） | 中~高 | Open / Semi-open | payable |
| 温和角色认同（flexible L2 identity） | 中 | Semi-open | payable~borderline |
| 刚性概念认同（rigid representation lock） | 中回落 | Closed 倾向 | borderline~overloaded |
| 身份防御极化（violent/arrogant lock-in） | 低~中（高反应低反思） | Closed | overloaded / unsustainable |

### [Lineage/Source]
- Essentia Foundation（Steven Pashko, 2026）: *Consciousness without counterpart: Identity beyond representation*。
- 现象学语境与“表征鸿沟”讨论，映射到 SRT 的 \(L_0/L_1/L_2\) 与 \(\Psi_f\) 记号。

## 【理论边界/防误用声明】
1. 不采纳“\(L_2\) 全部无效或必然有害”的推论；\(L_2\) 仍是协作与文明压缩的必要层。  
2. 不采纳“只要顿悟一次即可永久解脱”的推论；SRT 明确要求慢变量去绑定过程。  
3. 不采纳“拒绝身份标签 = 拒绝伦理责任”的推论；责任归属仍需制度与情境联合建模。
