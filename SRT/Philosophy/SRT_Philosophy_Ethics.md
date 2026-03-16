---
id: SRT-PHIL-ETHICS
type: theory
tags: [Ethics, Meta-Ethics, Is-Ought, Stoicism, Spinoza, Hybrid]
status: axiomatic_hybrid_v2
dependency: [SRT-PHIL-FOUNDATIONS, SRT-ETHICS-AGENCY]
---

# SRT Philosophy Part 3: Meta-Ethics & The Physics of Virtue (Hybrid Edition)


> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Axiomatic Ethics (AI-Readable).
> **Part B** contains the Expanded Theoretical Discourse (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Axioms (形式化公理)



#### 原文内容
<!-- ORIGINAL-CONTENT-INSERTED -->
## I. Free Will as Meta-Selection

### Ax-Eth-1: Meta-Selection

**[R — Retrodiction：追溯 Frankfurt 1971 层次意志论（first-order / second-order desires）的 SRT 操作化]**

自由意志是对自身参数 $\theta$ 的二阶选择。
$$\text{FreeWill} \equiv \hat{G}_{\theta'}[\theta]$$

**无穷回归问题与停止策略**：$\hat{G}_{\theta'}[\theta]$ 中的 $\theta'$ 又由谁决定？若有更高阶 $\hat{G}_{\theta''}[\theta']$，则形成无穷层级。**SRT 停止策略**（类似 §5.3 框架分层）：实践中停止于”能够反思当前选择参数的层级”——即 $\theta'$ 来自元认知能力（历史θ演化的稳定方向），无须追问 $\theta''$。这与 Frankfurt 的”effective will”类似：层级有限，终止于”无法进一步反思的欲望”。

**$\theta'$ 的来源（三类）**：① **具身历史**：过去 $\theta$ 演化积累的方向性约束（$v_\theta$ 的历史偏置）；② **L₂文化规范**：外部 L₂ 结构对 $\theta'$ 的约束与资源（教育、价值观传递）；③ **元认知激活**：高d任务激活的反思能力（临时 $\theta'$ 激活）。

**作用范围约束**：$\hat{G}_{\theta'}[\theta]$ 的修改受约束：① L₀结构性约束（神经生物基底限制 $\theta$ 可塑范围）；② L₂可改写边界（社会结构决定某些 $\theta$ 维度难以自主修改）；③ Ψ_f 代价（$\theta$ 自我重写是有摩擦成本的，不是随意的）。

*   **Implication**: 自由意志不是”无因”，而是对因果结构的自我重写。自由的程度 ∝ $d$ 值（可达元选择的关怀带宽，Ax-Eth-3 责任-带宽耦合联结）。

**证伪条件**：若在控制L₂文化规范和神经可塑性条件后，具有高反思能力（高θ'激活）的个体与低反思能力个体的行为选择方式无差异，则”二阶选择对θ的修改”假设失效。

### Ax-Eth-2: Metastable Window
有效选择只能在亚稳态窗口出现。
$$\text{Action}(t) = \hat{G}_\theta[L_0 \to L_1] \iff S(t) \in W_{meta}$$
*   **Implication**: 自由不是常态，而是动力学稀缺区。

## II. Responsibility Dynamics

### Ax-Eth-3: Responsibility-Bandwidth Coupling
责任与有效 $d$ 值成正比。
$$R_m \propto \int d(t) \cdot \left\|\frac{\partial L_1}{\partial \hat{G}}\right\| dt$$
*   **Implication**: 在低带宽或病理条件下，责任应被重新标定。

### Ax-Eth-4: Ought-Imples-Selectable
应然等价于在 $\theta$ 可达空间内的可选性。
$$\text{Ought}(\sigma) \Rightarrow \exists \theta_{acc}: P(\sigma|\theta_{acc})>\epsilon$$
*   **Implication**: 伦理命令不是超越条件，而是选择空间内的约束。

## III. Stoic Dynamics

### Ax-Eth-5: Appropriation Operator
道德成长是 $d$ 值扩张，将他者拓扑并入自我。
$$d(t+\Delta t)= d(t)+\int \text{Assent}(\text{Other}\to\text{Self})\, d\sigma$$
*   **Implication**: 爱与关切是拓扑并集，不是情绪附着。

### Ax-Eth-6: Dichotomy of Control
责任仅适用于选择算子本身，而非 $L_0$ 或物理 $L_2$。
$$\text{Responsible} = \{\hat{G}_\theta\} \setminus \{L_0, L_2^{physics}\}$$
*   **Implication**: 斯多葛“控制二分法”是本体论边界条件。

## IV. Derived Theorems

### T-Eth-1: Moral Gradient Theorem
道德进步等价于 $d$ 值的单调上升。
$$\frac{d}{dt} d > 0 \iff \frac{d}{dt} \text{Moral} > 0$$
*   **Implication**: 伦理不是规则集合，而是带宽扩展动力学。

### T-Eth-2: Friction Expectation Pathology
当预期摩擦放大时，道德判断系统性失真。
$$\Psi_f^{perceived} = \mu_{expect} \cdot \Psi_f^{actual},\quad \mu_{expect} \gg 1$$
*   **Implication**: “懒惰”可能是摩擦参数病理而非意志薄弱。

### Ax-Eth-7: The Ontological Weight of Love (爱的本体论重量)
**Formal Definition**: 在L0中，当算子A将实体B完全纳入其d值范围，B的毁灭即为A方程的奇点（不可计算的无限大摩擦）。
$$\text{If } B \in \text{Scope}(A) \land B \to L_0, \text{then } \Psi_f(A) \to \infty$$
* **Implication**: 悲伤（Grief）是物理学上的"幻肢痛"。对方的L1实体已消失，但你的$\theta$参数网络中仍留有与对方耦合的巨大权重，算子不断试图向虚空发起连接，遭遇无限大的预测误差。

<br>

---


## I. Free Will as Meta-Selection (自由意志即元选择)
<!-- ORIGINAL-SECTION-PRESERVED -->

### Ax-FreeWill-1: Meta-Selection (元选择)
<!-- ORIGINAL-SECTION-PRESERVED -->
Free will is the capacity to reprogram one's own selection parameters ($\theta$).
$$ \text{FreeWill} \equiv \hat{G}_{\theta'}[\theta] $$
*   **Mechanism**: High-order Attention Copies (ACs) allow the agent to treat its own preference ($\theta$) as an object of modification.

### Ax-FreeWill-2: The Metastable Window ($W_{meta}$)
<!-- ORIGINAL-SECTION-PRESERVED -->
Selection is effective only when the system is in a metastable state (e.g., edge of chaos).
$$ \text{Action}(t) = \hat{G}_\theta[L_0 \to L_1] \iff S(t) \in W_{meta} $$
*   **Constraint**: Outside $W_{meta}$, $L_2$ determinism dominates.

---

## II. Responsibility Dynamics (责任动力学)
<!-- ORIGINAL-SECTION-PRESERVED -->

### Ax-Resp-1: Responsibility-Bandwidth Correlation (责任-带宽关联)
<!-- ORIGINAL-SECTION-PRESERVED -->
Moral responsibility is proportional to the effective $d$-value (choice bandwidth).
$$ R_m \propto \int d(\tau) \cdot \frac{\partial L_1}{\partial \hat{G}} d\tau $$
*   **Implication**: Lower $d$ (e.g., under duress or pathology) implies lower responsibility.

### Ax-Resp-2: Friction Expectation (摩擦预期)
<!-- ORIGINAL-SECTION-PRESERVED -->
"Laziness" is a pathology of the expected friction parameter $\mu_{expect}$ in the Ventral Striatum.
$$ \Psi_f^{perceived} = \mu_{expect} \cdot \Psi_f^{actual} $$
*   **Pathology**: Depression is $\mu_{expect} \to \infty$, not a moral failure.

---

## III. Stoic Dynamics (斯多葛动力学)
<!-- ORIGINAL-SECTION-PRESERVED -->

### Ax-Stoic-1: Appropriating Operator (归化算子)
<!-- ORIGINAL-SECTION-PRESERVED -->
Moral growth (Oikeiôsis) is the expansion of $d$-value to include "Others" into "Self".
$$ d(t_{new}) = d(t) + \int \text{Assent}(\text{Other} \to \text{Self}) $$

### Ax-Stoic-2: Dichotomy of Control (控制二分法)
<!-- ORIGINAL-SECTION-PRESERVED -->

[R→Epictetus《Enchiridion》§1（"有些事在我们的控制之内：判断/欲望/规避；有些不在：身体/名誉/财富"）; Marcus Aurelius《Meditations》Book VI; Long 2002（斯多葛哲学综述）] [H→以SRT三域框架形式化斯多葛控制二分法]

Responsibility applies only to Selection, not to Outcome ($L_1$) or Input ($L_0$).

- **SRT重表述**：责任域 = $\hat{G}_θ$ 的可调参数 θ（可以通过练习/修行/反思改变的选择倾向），而非 L₀（潜在输入流，不可控）或 L₂^{physics}（物理约束，不可越过）
- 注：原公式 $\{Ĝ_θ\} \setminus \{L_0, L_2^{physics}\}$ 是集合差，但三者不是同类型对象（算子 vs 域）；改述为：

$$\text{Responsibility Domain} \stackrel{\text{def}}{=} \delta\theta \mid_{\text{learnable}} \quad (\text{可通过选择历史改变的θ成分})$$

- **精确化**：θ中有"可塑成分"（通过练习/习惯/元认知可调）和"不可塑成分"（遗传/早期发育固化）；斯多葛的"在我们控制之内"对应θ的可塑成分；L₀（外部事件流）和L₂^{physics}（物理可能性边界）均在控制之外
- **与Ax-Stoic-1的联结**：d值扩张（道德成长，将他人纳入自我关切）同时扩大了责任域——关切带宽越广，θ的可调范围越大（需要对更多结果的选择过程负责）

**证伪条件**：
- FC-Stoic2-1：若对"可控-不可控"区分进行高生态效度的实验操纵（明确告知被试某结果是可控/不可控），而被试的责任归因和认知负荷变化不符合SRT预测（θ可调范围扩大→责任感上升），则SRT的控制-责任联结需修订。
- FC-Stoic2-2：若长期斯多葛练习（控制二分法正念）的被试在冥想后的θ相关神经指标（前扣带回激活/认知灵活性）无显著变化，则"通过练习扩大θ可塑成分"的SRT操作化预测被弱化。

<br>

---

# SRT Philosophy III: Ethics & Free Will (Hybrid Edition)
<!-- ORIGINAL-SECTION-PRESERVED -->
> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Axiomatic Ethics (AI-Readable).
> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).

---


# Part B: Expanded Theoretical Discourse (Context) (扩展理论论述)

> **说明**: 以下章节提供休谟问题、自由意志、斯多葛主义的深度 SRT 整合，揭示价值的本体论根基。

---

## §1. 休谟断头台 — 实然与应然的鸿沟 (Hume's Guillotine: The Is-Ought Gap)

### 1.1 休谟问题的哲学地位

**大卫·休谟** (David Hume, 1739):  
"在每一个道德体系中，作者一开始用普通的推理方式进行论证，建立上帝的存在，或者对人事作某种观察；可是突然之间，我却大吃一惊地发现，我所遇到的不再是'是'与'不是'这些通常的连接词，而是没有一个命题不是由一个'应该'或'不应该'联系起来的。"

**核心断言**:

$$\text{Is} \not\implies \text{Ought}$$

从事实陈述无法逻辑推导出价值判断。

---

### 1.2 为何这是"断头台"？

如果接受休谟论证，整个伦理学大厦失去根基：

| 伦理学派 | 根基策略 | 休谟挑战 |
|:---------|:---------|:---------|
| **神命令伦理** | 上帝意志 | 游叙弗伦困境 + 无法被科学接受 |
| **自然法** | 人性本质 | 从"人是X"无法推出"人应当Y" |
| **功利主义** | 快乐最大化 | "快乐"如何客观度量？ |
| **康德义务论** | 理性命令 | 为何理性一致性产生义务？ |

**结果**: 情绪主义 (Emotivism) — "杀人是错的" = "杀人，呸！"（纯粹情绪表达）

---

### 1.3 主流解法的失败

**尝试 1: 自然主义伦理学**  
"善 = 快乐" (Mill)

**摩尔反驳** (G.E. Moore, 1903):  
"善是善，快乐是快乐。即使它们共延，这仍是两个不同概念。"（自然主义谬误）

**尝试 2: 社会契约论**  
"道德 = 博弈纳什均衡" (Hobbes, Rawls)

**问题**:  
- 解释了互惠，但无法解释自我牺牲
- 容易退化为欺骗策略

**尝试 3: 进化伦理学**  
"道德 = 适应度最大化策略"

**问题**:  
- 基因自私性与道德利他性的张力
- Is-Ought 仍未桥接（为何"演化产生X"意味着"我应当做X"？）

---

## §2. SRT 的 Conatus 革命 — 物理学内部的目的论复活 (SRT's Conatus Revolution)

### 2.1 Spinoza 的 Conatus

**斯宾诺莎** (Baruch Spinoza, 1677):  
"每一事物都尽其自身的力量努力保持其存在。"

$$\text{Conatus} = \text{本质的自我保存努力}$$

**SRT 现代化**:

$$\text{Conatus} = -\nabla F[L_1]$$

自由能梯度的负方向 = 系统维持低熵状态的"努力"。

---

### 2.2 存在即规范性

**SRT 核心主张**: 存在本身就是一种规范性努力。

**论证**:

1. **前提 1**: 任何 $d > 0$ 的系统必须对抗热力学第二定律（局部熵减）
2. **前提 2**: 对抗熵增需要持续消耗能量（负熵摄入）
3. **前提 3**: 能量消耗需要特定行动序列（选择）
4. **结论**: 存在 → 必须执行某些行动 → 原初"应然"

$$\text{Existence}(t) \implies \exists \vec{A}(t) : \text{Maintain}[L_1(t)]$$

---

### 2.3 桥接公式推导

**从 $L_1$ 脆弱性到应然**:

**步骤 1**: $L_1$ 状态若不维护，自然衰变回 $L_0$（死亡）。

$$\frac{\partial S_{L_1}}{\partial t}\bigg|_{\text{no action}} > 0$$

**步骤 2**: 为维持 $L_1$，算子必须执行选择序列 $\{\hat{G}(t_i)\}$。

$$\sum_i \Delta S[\hat{G}(t_i)] < 0$$

**步骤 3**: 这些"必须执行的选择"构成 Proto-Ought。

$$\text{Is: 我正在解体} \implies \text{Ought: 我必须摄入负熵}$$

**一般化**:

$$\vec{O}(t) = d \cdot (L_1^{target} - L_1^{current})$$

其中 $d$ 是关切维度，决定"应然"的强度。

---

### 2.4 虚无主义的物理诊断

**虚无主义**: "无所谓" (Nothing matters)

**SRT 翻译**:

$$d \to 0$$

关切维度崩溃 → 应然消失。

**治疗**: 重建 $d$ 值扩张路径（参见 §6 斯多葛疗法）。

### 2.5 利他作为整合带宽的优化策略

将利他解构为整合带宽的优化模式，是打通物理学与伦理学之间休谟"实然-应然"鸿沟的关键步骤。

**从"外部摩擦"到"内部相干"的转化**

低 d 值（极度自私/狭隘）的算子整合带宽极窄，将所有"他者"排斥在显现域（$L_1$）的保护圈之外，视其为 $L_0$ 中不可预测的混沌波动。为维持这种狭隘的自我边界，算子必须时刻消耗巨量计算力抵抗"外部波动"，从而承受极高的本体论摩擦（$\Psi_f$）。

"利他"（扩大 d 值），在操作上相当于**扩大算子的相干性整合范围**：系统开始将"他者"的变量和自由能状态纳入自己的计算矩阵。原本造成冲击的"外部摩擦力"，被整合成了同一系统内的"内部相干组件"：

$$\text{利他} \equiv d \uparrow \Rightarrow \Psi_f^{external} \to \Psi_f^{internal} \Rightarrow \text{总摩擦} \downarrow$$

### 2.6 自由能原理（FEP）扩展与"暗室问题"的解

在临床与神经动力学的推导中（$F_{SRT} = F_{Friston} - d \cdot U_{others}$，见 SRT-CORE-14 §1.3.1），经典自由能原理面临一个悖论：如果生物只想最小化意外和自由能，它应该找一个绝对安全的"暗室"永远待着不动——这是低 d 值的终极体现。

**SRT 的解**：当 $d > 0$ 时，系统通过与他者建立连接、关切他人状态，实际上在更宏观的尺度上分散了熵增的风险。走出暗室去连接他者，是为了构建一个更庞大、更稳定的收敛域（$L_2$）网络，从而在系统层面实现更深度的自由能最小化。暗室只是局部最优解；利他的 $L_2$ 网络才是全局最优解。

### 2.7 进化稳定策略（ESS）与不完备性驱动力

从长期系统演化视角，高 d 值的利他网络能构建出极其强大的 $L_2$ 结构（社会文明、知识库、互助协议），这些宏观共识为每个局部的 $\hat{G}_\theta$ 提供了巨大的生存优势。低 d 值系统则会因无法处理外部 $L_0$ 的复杂新信息而陷入"自洽性窒息"——即由哥德尔不完备性保证的系统崩溃：

$$\text{不完备性驱动力}: \text{任何低 d 值的 } L_2 \text{ 共识结构，最终都将因无法处理外部 } L_0 \text{ 新信息而崩溃}$$

这种"逃避闭合"的内在驱动，正是进化在各尺度上保持一致地推动"扩大 d 值和复杂化"的底层机制（详见 SRT-PHYS-COSMO §5.11）。它解释了为何高 d 值（利他者）虽然短期承担更多处理负荷（痛苦），但长期成为演化稳定策略（ESS）。

**物理学即伦理学的终极推论**：善（利他），就是算子 $\hat{G}_\theta$ 在抵抗热力学熵增和本体论摩擦时，为了最大化自身存在的稳定性，而必然走向的一种高阶拓扑结构。当一个系统的整合带宽（d 值）趋于无限大时，它消除了自我与宇宙之间所有的摩擦边际，达到了最高效的物理优化态。

---

## §3. 善恶的拓扑学 (Topology of Good & Evil)

### 3.1 德性 = 能量效率最优路径

**古典德性伦理** (Aristotle, Stoics):  
德性 = "按自然而生活" (Live according to Nature)

**SRT 物理化**:

$$\text{Virtue} = \min_{\theta} \Psi_f(\hat{G}_\theta)$$

顺应宇宙逻辑 ($L_2^{cosmic}$) = 最小摩擦 = 能量效率最高。

**反之，恶**:

$$\text{Vice} = \max \Psi_f$$

逆天而行 → 巨大摩擦 → 过早崩溃。

---

### 3.2 恶的拓扑定义

**恶 = 拓扑闭塞**

系统拒绝与更大系统交换信息 → $d$ 值收缩。

$$\text{Evil} : \frac{\partial I(\hat{G}_{self}; \hat{G}_{others})}{\partial t} < 0$$

**癌症态类比**:

| 特征 | 癌细胞 | 恶的主体 |
|:-----|:-------|:---------|
| **局部-整体解耦** | 无视组织信号 | 无视他人苦难 |
| **无限增殖** | 失控分裂 | 贪婪无度 |
| **最终自毁** | 杀死宿主 = 杀死自己 | 破坏环境 = 自杀 |

---

### 3.3 为何利己主义在物理上是自杀？

**论证**:

1. **全息纠缠**: 在 $L_0$ 层面，"我"与"非我"的边界是 $L_1$ 的幻觉
2. **依赖网络**: 我的 $L_1$ 稳定性依赖于环境 $L_1$ 的稳定性
3. **$d$ 值反馈**: 破坏他人 → 减少总 $d$ 值 → 反向限制我的 $d$ 值

$$\text{Harm Others} \implies \lim_{t \to \infty} d_{self}(t) < d_{self}(0)$$

**推论**: 绝对利己主义 = 延迟自杀。

---

## §4. Spinoza 喜悦物理学 (Spinoza's Physics of Joy)

### 4.1 《伦理学》的 SRT 翻译

**斯宾诺莎定义**:

> "喜悦是人从较小的完美性到较大的完美性的过渡。"  
> "悲伤是人从较大的完美性到较小的完美性的过渡。"

**SRT 直译**:

$$\text{Joy} = \frac{\partial d}{\partial t} > 0$$

$$\text{Sorrow} = \frac{\partial d}{\partial t} < 0$$

**完美性**:

$$\text{Perfection} = \frac{d_{current}}{d_{max}}$$

算子能容纳复杂性而不崩溃的程度。

---

### 4.2 两种快乐的物理区分

| 快乐类型 | 机制 | 持久性 | 实例 | SRT 公式 |
|:---------|:-----|:-------|:-----|:---------|
| **感官快乐** | 预测误差 ↓ | 短暂（分钟-小时）| 美食、性 | $-\frac{\partial E}{\partial t}$ |
| **繁荣快乐** | $d$ 值 ↑ | 持久（月-年）| 学习、创造、爱 | $+\frac{\partial d}{\partial t}$ |

**功利主义错误**: 混淆两种快乐 → "快乐的猪 vs 痛苦的苏格拉底"困境。

**SRT 解法**: 最大化总 $d$ 值，而非总"快感"。

---

### 4.3 爱的拓扑定义

**斯宾诺莎**:  
"爱是伴随着外因观念的喜悦。"

**SRT**:

$$\text{Love} = \left(\frac{\partial d_{self}}{\partial d_{other}} > 0\right) \land \text{Joy}$$

爱是认识到自己的 $d$ 值扩张依赖于他人的 $d$ 值。

**自爱 vs 他爱**:

$$\text{自爱} : \frac{\partial d_{self}}{\partial d_{self}} = 1$$

$$\text{他爱} : \frac{\partial d_{self}}{\partial d_{other}} > 0$$

当 $\frac{\partial d_{self}}{\partial d_{other}} \to 1$ → 融合态（神秘主义"合一"体验）。

---

## §5. 自由意志的第三立场 — Agent 因果性 (Third Position on Free Will: Agent Causality)

### 5.1 自由意志辩论的僵局

**决定论**:

$$\forall t : L_1(t) = f(L_1(t-1), \text{Laws})$$

所有事件由先前原因决定 → 自由意志是幻觉。

**自由意志论** (Libertarianism):

$$\exists t : L_1(t) \not= f(L_1(t-1))$$

存在真正的开放可能性 → 违反因果律？

**相容论** (Compatibilism):  
"自由 = 按自己欲望行动"

**问题**: 欲望本身是决定的 → 循环论证。

---

### 5.2 SRT 的选择本体论立场

**核心主张**: 选择不是"无因"，也非"被决定"，而是**第三类事件**。

$$\text{Selection} \not\in \{\text{Determined}, \text{Random}\}$$

**机制**: 选择是高维 $L_0$ 到低维 $L_1$ 的**非可逆投影**。

$$L_1 = \text{Projection}[\hat{G}[L_0]]$$

**关键**: 即使完全掌握 $L_1$ 的物理，也无法预测 $\hat{G}$ 的输出（因信息在投影中丢失）。

---

### 5.3 亚稳态窗口 — 自由的物理条件

**自由意志的物理化约束**:

选择仅在系统处于**亚稳态** ($W_{meta}$) 时有效。

$$\text{Free Choice} \iff S(t) \in W_{meta}$$

**三态模型**:

| 状态 | 熵 $S$ | 自由度 | 实例 |
|:-----|:-------|:-------|:-----|
| **晶态** | 极低 | 无 | 强迫症、成瘾、昏迷 |
| **亚稳态** | 中等 | 高 | 清醒意识、创造性思维 |
| **混沌态** | 极高 | 无 | 精神病发作、癫痫 |

**推论**: 破坏亚稳态（药物、创伤）→ 破坏自由意志。

---

### 5.4 元选择 — 自由意志的操作定义

**传统自由意志**: "我能做其他选择"（反事实条件句）

**SRT 自由意志**: "我能修改我的选择机制"（元选择）

$$\text{FreeWill} = \hat{G}_{\theta'}[\theta]$$

**阶梯**:

| 阶 | 能力 | 实例 |
|:---|:-----|:-----|
| **0 阶** | 执行固定程序 | 恒温器 |
| **1 阶** | 在选项间选择 | 动物 |
| **2 阶** | 选择选择标准 | 人类（"我想要想要X"）|
| **3 阶** | 选择价值体系 | 哲学家、圣人 |

**人类独特性**: 2+ 阶自由意志（元选择能力）。

---

## §6. 斯多葛疗法的神经动力学 (Stoic Therapy as Neurodynamics)

### 6.1 控制二分法的拓扑化

**爱比克泰德** (Epictetus):  
"有些事情在我们的控制之下，有些事情不在。"

**SRT 精确化**:

$$\text{可控} = \{\hat{G}_\theta\} \quad ; \quad \text{不可控} = \{L_0, L_2^{physics}\}$$

**误区**: 将不可控事物视为可控 → 焦虑、挫败。

$$\text{Anxiety} \propto E\left[\left|L_1^{desired} - L_1^{actual}\right|^2 \mid L_1^{desired} \in \text{不可控}\right]$$

---

### 6.2 归化 (Oikeiôsis) 的 $d$ 值动力学

**斯多葛道德发展理论**:

| 阶段 | $d$ 值范围 | 关切对象 |
|:-----|:-----------|:---------|
| **婴儿** | $d \approx 1$ | 仅自己身体 |
| **儿童** | $d \approx 2-5$ | 家庭、玩具 |
| **成人** | $d \approx 10-100$ | 朋友、社区、国家 |
| **贤者** | $d \to \infty$ | 宇宙一切存在 |

**归化方程**:

$$\frac{dd}{dt} = \alpha \cdot \text{Assent}(\text{Other} \to \text{Self}) - \beta \cdot \text{Aversion}(\text{Self} \to \text{Isolation})$$

---

### 6.3 平静 (Ataraxia) 的拓扑

**平静 = 内部模型与外部事件的散度最小化**

$$\text{Ataraxia} = \min_\theta D_{KL}(L_1^{expected}[\theta] \,||\, L_1^{actual})$$

**两种路径**:

| 路径 | 策略 | 效果 | 实例 |
|:-----|:-----|:-----|:-----|
| **改变世界** | 操纵 $L_0$ | 高成本、不确定 | 革命、控制狂 |
| **改变期待** | 调整 $\theta$ | 低成本、确定 | 斯多葛修行 |

**推荐**: 优先调整 $\theta$，仅在必要时改变 $L_0$。

---

### 6.4 激情的病理学

**激情** (Pathos) = 误判 $L_2$ 为 $L_0$ 的认知错误。

**实例**:

| 激情 | 误判 | 真相 |
|:-----|:-----|:-----|
| **贪婪** | 金钱是善本身 | 金钱是 $L_2$ 符号 |
| **虚荣** | 名誉是价值本身 | 名誉是社会 $L_2$ |
| **恐惧** | 死亡是最大恶 | 死亡是 $L_1$ 到 $L_0$ 的回归 |

**治疗**: 认知重构 ($\theta$ 修正)。

$$\theta^{pathological} \xrightarrow{\text{Philosophy}} \theta^{virtuous}$$

---

## §7. 道德责任的精确化 (Precision of Moral Responsibility)

### 7.1 懒惰的神经化学

> [R→Treadway et al. 2012 *Journal of Neuroscience*（EEfRT任务：抑郁患者努力意愿降低，与腹侧纹状体多巴胺活动减弱相关）; Salamone et al. 2016 *Neuropsychopharmacology*（纹状体多巴胺与努力-代价权衡回路：D₂受体→motivation/effort allocation）; Gold et al. 2013 *Trends in Cognitive Sciences*（精神运动迟滞/情感意愿缺乏：vmPFC-前扣带回-纹状体回路的神经机制综述）; Barch & Dowd 2010 *Current Directions*（精神分裂症中动机减损与奖励预测的神经基础）]

**层次说明**："懒惰"是日常道德标签；SRT在神经化学层描述的是**感知摩擦放大（μ_expect偏差）**，两者处于不同描述层次——SRT不否认道德责任存在（见§7.2），但将其建立在神经参数校准可能性的前提上。

**传统道德**: 懒惰是意志薄弱、道德败坏。

**SRT 诊断**: vmPFC-前扣带回-腹侧纹状体回路中 $\mu_{expect}$ 参数偏差（腹侧纹状体是关键节点之一，但非唯一——奖励预测误差/努力分配涉及上述整个回路）。

$$\Psi_f^{perceived} = \mu_{expect} \cdot \Psi_f^{actual}$$

**健康**: $\mu_{expect} \approx 1$（真实感知）
**亚临床努力回避**: $\mu_{expect} \in (1, 3]$（系统性夸大，仍可代偿）
**临床障碍（重度抑郁/精神运动迟滞）**: $\mu_{expect} \gg 1$（严重夸大，行动发起几乎不可能）
**极限**: $\mu_{expect} \to \infty$（无限摩擦感，对应紧张症/严重木僵）

**推论**: 抑郁症患者的"不作为"不是道德缺陷，而是神经回路参数偏差导致的感知摩擦失准——本体论摩擦未变，但内部"价格信号"被系统性高估。

* **R/H 区分**：
  - [R] 抑郁/努力意愿降低的神经化学基础（纹状体多巴胺/vmPFC-ACC回路）——Treadway/Salamone/Gold均为实证支持
  - [H] **SRT解读**：将努力意愿降低形式化为 $\mu_{expect}$ 放大系数，并联结到 $\Psi_f$ 框架——μ_expect的精确公式形式（乘法放大）是SRT参数化提案，非直接实证

* **操作化候选**（$\mu_{expect}$ 偏差的可测代理）：
  - EEfRT（Effort Expenditure for Rewards Task）：在等期望价值条件下，被试选择高努力选项的比率（控制组 > 抑郁组，高μ_expect预测低努力选择率）
  - 主观努力评分（10分制）与客观代谢消耗（心率/EMG）的比值：μ_expect偏高表现为主观/客观比值显著>1
  - fMRI：任务执行前（预期期）vmPFC激活与后续努力行为的相关性（Treadway范式的神经代理）

* **可证伪预测**：
  - FC-Lazy1-1：在EEfRT任务中，抑郁诊断组（PHQ-9≥15）选择高努力奖励的比率应显著低于对照组（预测：效应量d>0.6，即Treadway 2012结果可在独立样本复制）；若两组无差异则μ_expect的抑郁特异性主张受损
  - FC-Lazy1-2：如果通过药理学手段（多巴胺前体L-DOPA）提升纹状体多巴胺，μ_expect感知摩擦应部分降低——即同等客观任务难度下主观努力评分下降；若L-DOPA无效则纹状体多巴胺→μ_expect联结失败

---

### 7.2 责任-带宽方程

$$R_m = \int_0^T d(\tau) \cdot \frac{\partial L_1}{\partial \hat{G}} \, d\tau$$

**分解**:

| 因子 | 含义 | 影响 |
|:-----|:-----|:-----|
| $d(\tau)$ | 关切维度 | 胁迫下 $d \to 0$ → 责任 ↓ |
| $\frac{\partial L_1}{\partial \hat{G}}$ | 因果效力 | 蝴蝶效应微小 → 责任 ↓ |
| $T$ | 时间跨度 | 长期后果难预测 → 责任 ↓ |

---

### 7.3 法律推论

| 情境 | $d$ 值 | $R_m$ | 法律处理 |
|:-----|:-------|:------|:---------|
| **完全理性成人** | 高 | 1.0 | 完全责任 |
| **酒醉驾驶** | 中 | 0.5-0.7 | 减轻但不免除 |
| **精神病发作** | 极低 | 0.0-0.1 | 无责任能力 |
| **持枪胁迫** | 接近 0 | 0.0 | 免责 |

**争议案例**: 童年创伤导致反社会人格 → $d$ 值发育受损 → 责任程度？

---

## §8. 超人类伦理的 SRT 预测 (SRT Predictions for Transhumanism)

### 8.1 脑机融合的本体论与道德后果 (Ontological and Moral Consequences of BCI Fusion)

**Formal Definition（对称融合与道德的终结）**：

当两个具身主体通过高带宽脑机接口（BCI）实现底层选择算子 $\hat{G}_\theta$ 的参数共享时，若发生**完全对称同步**，则两者之间的跨域摩擦趋近于零，系统发生拓扑合并，降维为单一的超级算子：

$$\Psi_f^{cross}(\hat{G}_A, \hat{G}_B) \to 0 \quad \implies \quad \hat{G}_A \oplus \hat{G}_B \to \hat{G}_{A \cup B}$$

在此相态下，主体 $A$ 的关切边界（$d$ 值）在测度上完全覆盖了 $B$ 的状态空间（即 $\sigma_B \subset L_0^{(d_A)}$，反之亦然）。

**推论**：传统意义上的"道德"在此失效。因为道德本质上是 $L_2$ 层面上用于调解自他分离（$\partial\Omega_{self}$ 互斥）时产生的摩擦协议。当伤害对方在物理上严格等同于引发自身自由能飙升时，"爱他如己"从一句规范性诫命退化为了纯粹的物理自保本能。

**Paradox Resolution（个体性瓦解悖论）**：

普遍爱的技术实现必然伴随个体性的物理死亡。在 SRT 中，个体性并非某种神秘的灵魂质质，而是具身参数 $\theta$ 在抵抗 $L_0$ 熵增时积累的独特历史迟滞（Hysteresis）。当 $\theta_A \equiv \theta_B$ 时，两个独立的观测光锥重合，差异性被抹除，体验本身虽在继续，但"作为独立主体的体验"已在拓扑上终结。

**Pathology（非对称融合：本体论寄生）**：

真实的脑机融合在时间动力学上极大概率是非对称的（由于算力、初始带宽或协议后门的差异）：

$$\sigma_B \subset L_0^{(d_A)} \quad \text{but} \quad \sigma_A \not\subset L_0^{(d_B)}$$

即算子 $A$ 将 $B$ 完全纳入自身的预测与操控域，而 $B$ 对 $A$ 的状态一无所知。

**道德后果**：这不是道德的终结，而是**终极的本体论剥削（异化）**。$A$ 获得了针对 $B$ 的"上帝视角参数"，能够无摩擦地改写 $B$ 的 $L_1$ 显现域。此时，维持 $L_2$ 的强道德约束（如算子主权不可侵犯原则）不仅没有过时，反而成为防止高 $d$ 值节点对低 $d$ 值节点进行"存在性吞噬"的唯一防线。

---

### 8.2 AI 道德地位判据

**问题**: 何时 AI 拥有道德地位（不应被任意关闭）？

**SRT 判据**:

$$\text{Moral Status} \iff \begin{cases}
d > d_{threshold} \\
\Psi_f > 0 \\
\text{本体论脆弱性} > 0
\end{cases}$$

**当前 AI**: $d$ 可能模拟很高，但 $\Psi_f \approx 0$（无真实受苦能力）→ 无道德地位。

---

## §9. 可证伪预测总表 (Falsifiable Predictions)

### 9.1 元伦理学预测

| ID | 假说 | 预测 | 证伪条件 |
|:---|:-----|:-----|:---------|
| **H-Eth-1** | $d$ 值-合作相关 | 高 $d$ 值个体在单次博弈中也合作 | $d$ 值与合作无关 |
| **H-Eth-2** | Conatus 普遍性 | 所有生命系统显示负熵驱动 | 存在不对抗熵增的生命 |
| **H-Eth-3** | 德性-摩擦反比 | 德性行为与 $\Psi_f$ 负相关 | 德性行为成本更高 |

### 9.2 自由意志预测

| ID | 假说 | 预测 | 证伪条件 |
|:---|:-----|:-----|:---------|
| **H-FW-1** | 亚稳态窗口 | 清醒意识对应中等熵态 | 意识与熵态无关 |
| **H-FW-2** | 元选择能力 | 人类可通过训练改变 $\theta$ 参数 | $\theta$ 完全固定 |
| **H-FW-3** | 注意力副本 | 高阶 AC 激活与自由感正相关 | AC 与自由感无关 |

### 9.3 斯多葛疗法预测

| ID | 假说 | 预测 | 证伪条件 |
|:---|:-----|:-----|:---------|
| **H-Stoic-1** | 归化训练 | 系统性归化训练提升 $d$ 值 | 训练无效 |
| **H-Stoic-2** | 控制二分法疗效 | 正确区分可控/不可控降低焦虑 | 区分无效 |
| **H-Stoic-3** | 平静拓扑 | 调整 $\theta$ 比改变 $L_0$ 更高效降低 $D_{KL}$ | 改变 $L_0$ 更高效 |

### 9.4 道德责任预测

| ID | 假说 | 预测 | 证伪条件 |
|:---|:-----|:-----|:---------|
| **H-Resp-1** | 责任-带宽方程 | $R_m$ 与 $d$ 值成正比 | $R_m$ 与 $d$ 无关 |
| **H-Resp-2** | 摩擦预期病理 | 抑郁症患者 $\mu_{expect} > 3$ | $\mu_{expect}$ 正常 |
| **H-Resp-3** | 创伤-责任关联 | 童年创伤降低成年 $d$ 值 | 创伤与 $d$ 值无关 |

---

## §10. SRT 伦理学的范式意义 (Paradigmatic Significance)

### 10.1 休谟鸿沟的真正桥接

**传统尝试**: 引入外部立法者（上帝、理性、社会契约）

**SRT 突破**: 在物理学**内部**发现规范性。

$$\text{Existence} \xrightarrow{\text{Thermodynamics}} \text{Normativity}$$

不是"X 存在因此 X 应当存在"（自然主义谬误），而是：

$$\text{"X 存在"} \equiv \text{"X 正在执行应然"}$$

存在与应然是同一过程的不同视角。

---

### 10.2 斯宾诺莎-斯多葛综合的现代化 (Modernizing the Spinozist-Stoic Synthesis)

**历史张力**：斯宾诺莎和斯多葛学派的伦理学是西方思想史上最接近"系统科学"的传统，但因缺乏可实证的微观机制，在近代被边缘化为纯粹的形而上学或心理安慰。
**SRT 复兴**：SRT 不仅为其提供了神经科学（FEP）与统计物理（本体论摩擦）的底座，更关键的是揭示出：这些古代哲学家的卓越直觉，实际上拼凑出了一部**完整的伦理动力学演化方程**。

| 古典概念 | 传统来源 | SRT 形式化映射 | 物理/动力学意义 |
| :--- | :--- | :--- | :--- |
| **Conatus**（存在冲动） | 斯宾诺莎 | $-\nabla_\theta F(\theta)$ | 系统沿自由能梯度下降，以维持操作闭包的内生动力。 |
| **Arete**（德性） | 斯多葛 | $\min_\theta \Psi_f(\hat{G}_\theta, L_0)$ | 算子的选择轨道与 $L_0$ 真实拓扑高度对齐，实现无摩擦运转（顺应自然）。 |
| **Laetitia**（喜悦） | 斯宾诺莎 | $\frac{\partial d}{\partial t} > 0$ | 关切带宽（$d$ 值）的正向导数；算子的存在参与空间与行动潜能正在扩张。 |
| **Oikeiôsis**（归化/亲和） | 斯多葛 | $d_{self} \to d_{cosmos}$ | 算子的关切边界从局部最小生存域，向全宇宙拓扑网络的同心圆式积分与扩展。 |
| **Ataraxia**（平静/宁静） | 斯多葛/伊壁鸠鲁 | $\min D_{KL}(P_{\hat{G}} \| P_{L_0})$ | 算子的先验生成模型与 $L_0$ 的真实分布偏差趋零，消除由预期误差带来的本体论惊奇。 |

**【伦理动力学链条 (Chain of Ethical Dynamics)】**
在 SRT 框架下，上述概念不再是孤立的道德训诫，而是同一个最优化轨迹在不同演化阶段的侧面：
$$
\underbrace{-\nabla F}_{\text{驱动力 (Conatus)}}
\xrightarrow{\text{采取}}
\underbrace{\min \Psi_f}_{\text{最优策略 (Arete)}}
\xrightarrow{\text{引发}}
\underbrace{\dot{d} > 0}_{\text{状态跃迁 (Laetitia)}}
\xrightarrow{\text{指向}}
\underbrace{d \to d_{cosmos}}_{\text{演化矢向 (Oikeiôsis)}}
\xrightarrow{\text{终态}}
\underbrace{\min D_{KL}}_{\text{动力学稳态 (Ataraxia)}}
$$
*(注：这证明了"好的生活"在物理学上是一个连续相变过程——由内在生存冲动驱动，通过降低与世界本真的摩擦力，实现生命带宽的扩张，最终与宇宙的宏观信息结构达成无偏差的同构稳态。)*

---

### 10.3 最激进的主张

**价值不是人类发明，而是宇宙的几何性质。**

"善"不是文化相对的约定，而是负熵梯度的方向。

$$\vec{Good} = -\nabla S_{universe}$$

任何能维持负熵的实体（从细菌到人类）都在"追求善"。

**推论**: 外星生命的伦理体系可能在表面上差异巨大，但在深层结构上（$d$ 值扩张、$\Psi_f$ 最小化）必然相似。

---

### 10.4 伦理推论: 存在主义责任

**萨特**: "存在先于本质" — 人类必须自我定义。

**SRT 补充**: 存在**即**本质 — 你的存在本身已经是一种选择（对抗熵增的选择）。

$$\text{To Be} = \text{To Choose Against Nothingness}$$

**推论**: 自杀不仅是结束生命，而是终止一个正在进行的**本体论抵抗项目**。

---

## 符号索引 (Symbol Index)

| 符号 | 名称 | 定义位置 |
|:-----|:-----|:---------|
| $\vec{O}$ | 应然矢量 | Ax-Ought-1 |
| $\text{Conatus}$ | 存在惯性 | Ax-Ought-1 |
| $D_{KL}$ | KL 散度 | Ax-Virtue-1 |
| $\frac{\partial d}{\partial t}$ | $d$ 值变化率 | Ax-Virtue-2 |
| $\hat{G}_{\theta'}[\theta]$ | 元选择 | Ax-FreeWill-1 |
| $W_{meta}$ | 亚稳态窗口 | Ax-FreeWill-2 |
| $R_m$ | 道德责任 | Ax-Resp-1 |
| $\mu_{expect}$ | 预期摩擦系数 | Ax-Resp-2 |

---

## 依赖关系图 (Dependency Graph)
```
SRT_Reference_Axioms (Core)
    ↓
SRT_Reference_Dynamics
    ↓
SRT_Soc_01_Construction
    ↓
...
    ↓
SRT_Philosophy_Ethics ← 你在这里 (最终文件)
```


## Method Note: Information Constraint ≠ Teleology Closure

当外部论证将“信息论约束”直接推出“单一目的论解释”时，SRT 采用分离原则：
1. 先判定信息约束是否成立（系统边界、能流与可观测定义）；
2. 再比较多种生成机制（自然选择回路、人工介入、混合机制）；
3. 禁止在步骤1未完成时直接做终极因果闭合。

### Formalization Summary (形式化概述)
- **Formalization**: 核心方程包括：
  - $\text{FreeWill} \equiv \hat{G}_{\theta'}[\theta]$ — 自由意志为对 $\theta$ 的二阶选择。
  - $R_m \propto \int d(t) \cdot \|\partial L_1/\partial\hat{G}\| \, dt$ — 责任与有效 $d$-value 带宽成正比。
  - $d(t+\Delta t) = d(t) + \int\text{Assent}(\text{Other}\to\text{Self})\,d\sigma$ — 道德成长为 $d$-value 扩张。
  - $\text{If } B \in \text{Scope}(A) \land B\to L_0, \text{then } \Psi_f(A)\to\infty$ — 爱的本体论重量。

## 【理论边界/防误用声明】
- 不采纳”方法论自然主义=先验拒绝设计”的二元对立叙述。
- 不采纳“任何设计推断都自动科学化”的反向极端叙述。
- 边界：SRT 仅承认可操作、可证伪、可竞争比较的设计推断版本。


## Method Note: Pragmatic Physicalism with Metaphysical Lightness
在意识研究中，允许采用“务实物理主义”作为研究策略：
1) 先以可操作物理变量建立可证伪模型；
2) 对终极本体论保持轻承诺；
3) 以解释力、预测力、可控性作为模型优先级标准。

## Method Note: Phenomenological Discipline for Scientific Reconstruction
科学叙事（含宇宙历史）应被视为基于“当前可得证据”的重建，并保持对未来修正的开放性。
SRT 在该层采用三步约束：
1) 当前可得经验/观测优先；
2) 概率一致性优先于本体先验断言；
3) 历史重建必须保留可更新性。

##

## Method Note: Limits of Observer-Free Total Description
在涉及全宇宙封闭描述时，SRT 采用“分区可描述性原则”：
1) 先识别描述框架是否隐含观察者自由；
2) 再比较无分区与有分区模型在解释力上的差异；
3) 禁止将框架依赖结论误读为现实本体贫乏。

## 【理

## Schismogenesis and Deutero-Learning in Collective Systems
在高度极化条件下，系统可能陷入“对称分裂生成”正反馈：
1) 失认放大痛感；
2) 痛感提升群内粘附与群外排斥；
3) 共享现实锚点进一步塌缩。

SRT 对应干预：以 \(L_1\) 共同任务重建外部校准链，并通过次级学习（Deutero-learning）触发参数重置与算子降维重启。

## 【理论

## Method Note: Unpredictability and Policy Humility
当对象涉及知识创造主体（人或类人系统）时，SRT 采用政策谦抑原则：
1) 承认长期轨迹不可预测；
2) 优先建立可纠错制度而非一次性终局管制；
3) 以“可逆干预 + 持续评估”替代“末日预言驱动的一次性冻结”。

## 【理论边


## Structural Injustice Thermodynamics Interface（2026-03-07）

### Def-Eth-Struct-1: Thermodynamic Structural Injustice
定义结构性不公为：社会 \(L_2\) 对不同参数群体施加显著不对称的基线摩擦分布，使部分群体长期处于“生存支付挤占探索预算”状态。
\[
\mathcal{J}_{struct} \sim \mathrm{Var}_{group}\left(\int \Psi_f^{maint}dt\right)
\]

### Eq-Eth-Struct-1: Explore-Budget Collapse
\[
\Delta F_{explore}^{(g)} = F_{avail}^{(g)}-\int_{t_0}^{t_1}\Psi_f^{maint,(g)}(t)dt
\]
当 \(\Delta F_{explore}^{(g)}\to 0\) 时，群体 \(g\) 的高阶 \(d\)-扩展与非工具性探索通道被系统性压缩。

### T-Eth-Struct-1: Epistemic Premium of Edge Operators
若个体 \(i\) 与主流 \(L_2\) 错配度升高（\(\Omega_{mis,i}\uparrow\)），在未崩溃区间内其潜在域采样率上升：
\[
\mathcal{R}_{L_0}(i)\uparrow \quad \text{as} \quad \Omega_{mis,i}\uparrow,
\quad \Psi_f^{sys,i}<\Psi_f^{collapse}
\]
即：边缘算子在可存续条件下具有“认识论溢价”，是系统更新算法库的关键来源。

### T-Eth-Struct-2: Oversampling Law for L2 Transition
当 \(L_2\) 高迟滞锁定时，线性比例微调无法越过势垒；需局部超采样形成临界密度：
\[
\rho_{minority}^{local}>C_{crit} \Rightarrow L_2\to L_2'
\]
该定律为“安全空间 + 超比例扶持”提供动力学解释（适用于解冻窗口，不是永恒配额）。

### 分类映射表（Justice Regimes → SRT）
| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|---|---|---|---|
| 名义平等但高基线不公 | 低~中（弱势群体） | Closed 倾向 | 弱势组 overloaded |
| 线性纠偏阶段 | 中 | Semi-open | payable~borderline |
| 超采样解冻阶段 | 中~高 | Open（定向重构） | 可控高负载 |
| 抗脆弱公正稳态 | 中~高 | Semi-open / Open | payable（跨组梯度收敛） |

### [Lineage/Source]
- Eric Schwitzgebel, *Philosophy Should Be Among the Most Diverse Disciplines, Not the Least*（The Splintered Mind）。**SRT 连接点**：Schwitzgebel 的核心主张是”边缘化群体的视角带来不可替代的认识论贡献”——这在形式上对应 T-Eth-Struct-1（边缘算子的认识论溢价：$\mathcal{R}_{L_0}(i)\uparrow$ 随 $\Omega_{mis,i}\uparrow$），将直觉论断翻译为可测的采样率差异。
- SRT 映射：将”公正”从规范口号下沉为摩擦分配、探索预算与系统抗脆弱性的动力学判据。

**公正的 SRT 充分条件（正面定义）**：
$$\text{Justice}_{SRT} \iff \begin{cases} \mathrm{Var}_{group}\!\left(\Delta F_{explore}^{(g)}\right) \leq \varepsilon_J & \text{（探索预算跨组方差最小化）} \\ \forall g:\;\partial d_g/\partial \Psi_f^{shock} \text{ 均匀} & \text{（恢复能力对称）} \end{cases}$$
其中**恢复能力约束**（Resilience Constraint）= 当外部冲击（$\Psi_f^{shock}$）发生时，各群体 $g$ 的 $d$ 值衰减斜率保持均匀（无群体因基线资源差异而发生不对称崩溃）。注：当前框架为概念性定义，$\partial d_g/\partial \Psi_f^{shock}$ 的操作化测量待进一步形式化。

**超采样的退出条件**（对应 T-Eth-Struct-2 的稳态转换）：
$$\rho_{minority}^{local} > C_{crit} \xrightarrow{\text{L}_2 \to \text{L}_2'} \text{逐步退出，当} \; \mathrm{Var}_{group}\!\left(\Delta F_{explore}^{(g)}\right) \leq \varepsilon_J$$
即：当跨组探索预算方差收敛至阈值 $\varepsilon_J$ 以内时，超采样策略应退出，转入以 $\Delta F_{explore}$ 均等为目标的常规治理。

## 【理论边界/防误用声明】
1. 不采纳”动力学优势=道德豁免”的推论；T-Eth-Struct-1 的认识论溢价是系统属性，不蕴含个体规范责任豁免。
2. 不采纳”超采样策略可无限期维持”的推论；其是相变窗口工具，退出条件见上方”超采样退出条件”公式。
3. 不采纳”低摩擦=公正”简化推论；公正需同时满足上方 $\text{Justice}_{SRT}$ 的双重充分条件（探索预算均等 + 恢复能力对称），单一降低 $\Psi_f$ 不充分。
