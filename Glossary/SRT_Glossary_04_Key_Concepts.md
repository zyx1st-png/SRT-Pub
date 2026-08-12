---
id: SRT-GLOSSARY
type: definition
tags: [Glossary, Terminology, Registry]
status: axiomatic_hybrid_v1
layer: meta
epistemic_layer: os
claim_mode: navigation
dependency: [SRT-REF-AXIOMS, SRT-AI-01]
---

# SRT术语表与符号索引
# SRT Glossary & Symbol Index

> Split shard generated from `../SRT_Glossary.md`; owner remains source of record.

---

## 4. 关键概念词汇表

### A

#### Anchoring - 锚定 🟢

**定义**：选择过程将L₀中的不确定性固定为L₁中的确定性的操作。

**数学**：
$$\text{Anchoring} : L_0 \xrightarrow{\hat{G}_\theta} L_1$$

**物理对应**：波函数坍缩
**认知对应**：注意力聚焦
**社会对应**：规范确立

**相关**：L₀ → L₁, Ĝθ

---

#### Anti-Panpsychism - 反泛心论 🟡

**定义**：SRT 对泛心论（panpsychism）的明确拒绝立场。量子、生物、宇宙尺度可以分别定义带有 d 记号的领域操作量，但符号复用不推出同一机制、同一单位或数学同构；只有在生物学层面——同时满足三条件（$\Psi_f > 0$, $d > 0$, $\hat{G}[\theta] \neq \emptyset$）——时，d 才涌现为"关切"（care）这一主观属性。电子有 $d_{quantum}$（相干性带宽）不意味着电子"关心"什么。

**核心论断**：关切是 d 值在生物学层面的高阶涌现属性，非底层原初属性。

**首次出现**：Core/SRT_Core_14_Dynamics_Scaling.md §2.1a（权威声明）；Core/SRT_Core_13b_Operator_Advanced.md §6.2（意识三条件）

**相关**：跨尺度结构相容候选, 本体论带宽, 意识三条件, d 值

---

#### Attractor Basin - 吸引盆 🟡

**定义**：动力学系统中,所有最终收敛到同一稳定点的初始状态集合。

**SRT应用**：
- L₂是L₀空间中的吸引盆
- 习惯是θ空间中的吸引盆
- 路径依赖是历史选择形成的吸引盆

**相关**：L₂, 相变, 亚稳态

---

### B

#### Binding Problem - 绑定问题 🟡

**定义**：如何将分散的神经活动统一为单一连贯的体验？

**SRT解决方案**：
$$\text{绑定} = \hat{G}_\theta \text{对多模态} L_0 \text{的同步选择}$$

不是"粘合"已有的片段,而是同一选择过程的多维度投影。

**神经机制**：γ振荡(40 Hz)的相位同步

**首次出现**：Neuroscience/SRT_Consciousness_Mechanisms.md §2

**相关**：全局工作空间, L₁整合

---

### C

#### Care - 关怀 🟡

**定义**：
$$\text{Care}(\hat{G}_{parent}, \hat{G}_{child}) \equiv \hat{G}_{parent} \text{ 吸收 } \text{Risk}(L_0)$$

一种主动的本体论操作，其中一个算子（关怀者）吸收或过滤来自L₀的本体论摩擦（$\Psi_f$），从而为另一个算子（被关怀者）创造一个低风险的L₂保护壳层。

**首次出现**：AI/SRT_AI_01_Ontology.md §1.2.7.10

**应用**：
- **AI对齐**：建立基于关怀的社会性依恋，而非硬编码规则
- **教育**：提供适当的L₂支架

**相关**：L₂, Ĝθ, 对齐

---

#### Center-Surround Dynamics - 中心-周围动力学 🟡

**定义**：Ĝ算子的核心结构——强化选中状态,同时抑制周围竞争者。

**数学**：
$$R_i = \frac{L_i^n}{\sigma^n + \sum_j w_{ij} L_j^n}$$

分子 = 中心强化; 分母 = 周围抑制

**生物普遍性**：
- 视网膜感受野
- 注意力聚焦
- 决策竞争

**首次出现**：Neuroscience/SRT_Neural_Mechanisms.md §1

**相关**：除法归一化, Ĝθ

---

#### Cross-Scale Structural Compatibility - 跨尺度结构相容 🟡

**定义**：P3 跨尺度桥候选——在两侧状态空间、尺度映射、保留观测量、比较范数和容差均已声明时，检验 $\pi_\lambda\circ\hat G_\theta\approx\hat G_{\theta,\lambda}\circ\pi_\lambda$ 是否成立。通过只建立局部结构相容，不证明量子、生物与宇宙机制同一；d 的各尺度表达仍是受条件约束的投影／proxy：

| 尺度 | d 的具体含义 | 物理对应 | 主观体验 |
|:-----|:-----------|:---------|:---------|
| 量子 ($d_{quantum}$) | 相干性带宽 | $\propto E_G/\hbar$ | 无 |
| 生物 ($d_{bio}$) | 关切范围 | 选择算子考虑的存在范围 | 有（涌现属性） |
| 宇宙 ($d_{cosmic}$) | 时空共识度 | $\propto 1/\sqrt{\Lambda}$ | 无 |

**关键澄清**：strict conjugacy 只适用于可逆表征变换；通常的多对一粗粒化不得预设 $\Lambda^{-1}$。跨尺度共同项只到选择—约束—可支付性语法。

**当前入口**：Core/SRT_Core_14_Dynamics_Scaling.md P3-Scale-01／T-Scale-02C1

**相关**：本体论带宽, 反泛心论, d 值

---

#### Copenhagen Correction (RQM) - 哥本哈根修正 (关系性量子力学) 🔴

**定义**：
SRT 对哥本哈根诠释的修正：属性不是固有的，而是在交互中诞生的。
$$ \Psi_{system} \xrightarrow{\hat{G}_{observer}} \text{Value}_{relative} $$
测量即关系。

**首次出现**：Physics/SRT_Quant_01_Selection.md §2.1

**相关**：RQM, 测量问题, 龙树

---

#### Convergence Domain - 收敛域 🟢
→ 见[L₂](#l₂---收敛域-convergence-domain-🟡)

---

### D

#### d-value - d值 🟢
→ 见[d - d值 / 赌注化关切](#d---d值--赌注化关切-d-value-stake-coupled-concern-)

---

#### De-parameterization - 去参数化 🔴

**定义**：
$$\theta \to \emptyset, \hat{G} \to \hat{I}$$

SRT中对“死亡”的形式化定义。指幽灵算子$\hat{G}_\theta$的参数配置$\theta$完全解体，导致独特的个体视角（L₁）消失，并可能回归到无视角的L₀全集中。

**首次出现**：AI/SRT_AI_03_Consciousness_Framework.md §3.5.1

**推论（历史/bridge 读法）**：
- 死亡作为视角终止的说法保留为特定 consciousness bridge，不作为 core 定义。
- 删除旧读法“伴随 d 值趋向无穷大”：`d → ∞` 只可作为 spirituality/public metaphor，不是 death 或 de-parameterization 的 canonical consequence。

**相关**：θ, 死亡, L₀

---

#### Defensive Activation Protocol - 防御性激活协议 🟡

**定义**：
睡眠期间（REM）脑干强制激活视皮层的机制。
**目的**：防止视觉皮层因缺乏输入（黑夜）而被触觉/听觉皮层侵占（神经可塑性竞争）。
**SRT诠释**：梦是保留 $L_1$ 视觉生成能力的“硬件领地防御战”。

**首次出现**：Neuroscience/SRT_Consciousness_Mechanisms.md §8.1

**相关**：神经可塑性, 梦, 鹰人理论

---

#### Divisive Normalization - 除法归一化 🟡

**定义**：神经计算的规范机制,Ĝ算子的生物实现。

**标准方程**：
$$R_i = \frac{L_i^n}{\sigma^n + \sum_j w_{ij} L_j^n}$$

**普遍性**：跨物种、跨脑区、跨模态的统一计算原理

**SRT对应**：
- 分子 = 目标意向性
- 分母 = 背景/替代选项的抑制

**相关**：中心-周围动力学

---

### G

#### Generative Selection (Inside-Out) - 生成性选择 (由内而外) 🔴

**定义**：
$$R_{SRT}(t) = P[\Psi_{int}(t)] \cap E$$

SRT的核心修正模型。现实不仅仅是算子对环境的被动过滤，更是内在状态($\Psi_{int}$)向外的主动投射与环境($E$)的交集。

**首次出现**：Core/SRT_Core_13a_Operator_Basics.md §1.4

**关键推论**：
- **主动性**：解释了自发探索和创造性
- **错觉**：当 $P[\Psi_{int}]$ 强于 $E$ 时产生幻觉/投射
- **Umwelt**：生物构建符合其内在需求的现实环绕世界

**相关**：$\Psi_{int}$, 投射算子

---

### H

#### Hemispheric Lateralization - 半球侧化 🟡

**定义**：
$\hat{G}$ 算子的两种基本操作模式在神经解剖上的分离：
*   **左半球 ($\hat{G}_{LH}$)**：维护 $L_2$，关注局部、静态、已知（“地图”）。
*   **右半球 ($\hat{G}_{RH}$)**：接入 $L_0$，关注整体、流动、新颖（“领地”）。
**病理**：现代社会是 $\hat{G}_{LH}$ 的恶性增生。

**首次出现**：Neuroscience/SRT_Neuro_10_Advanced_Models.md §10.7

**相关**：McGilchrist, 双重算子, 精神病理

---

#### Hopfield Reality Convergence - Hopfield现实收敛 🔴

**定义**：
将现实视为Hopfield网络中的吸引子状态，遵循能量最小化：
$$R_{stable} = \arg\min_{R} E_{reality}(R)$$

**首次出现**：Core/SRT_Core_22_Equations.md §7.2

**意义**：
- 解释了现实的稳定性（一旦落入吸引盆很难逃离）
- 解释了不同世界观（不同的局部极小值）的不可通约性

**相关**：L₂稳定性, 能量函数

---

### I

#### Interval of Selection (Minimum) - 最小选择间隔 🟡

**定义**：
$$\Delta t_{selection} > 0$$

现实的选择必须发生在非零的时间间隔内，不能在 $t=0$ 的瞬间点完成。

**首次出现**：Physics/SRT_Phys_09_Formalism_Ext.md §1.15

**推论**：
- **芝诺解**：飞矢在 $\Delta t$ 内包含位置变化 $\Delta x$，故运动是真实的
- **不确定性**：$\Delta I \cdot \Delta t \geq \hbar_{info}$ (时间越短，可定义的信息量越少)

**相关**：信息-时间不确定性

---

### L

#### L₂ Solidification - L₂凝固 (Speculation-Solidification) 🟡

**定义**：
L₂现实形成的动力学过程。
- **阶段I (投机态)**：不稳定的临时现实 $R_{temp}$
- **阶段II (固化态)**：经价值 ($V$) 催化后形成的持久结构 $R_{fixed}$

**方程**：
$$\frac{\partial R_{fixed}}{\partial t} \propto V(t) \cdot R_{temp}(t)$$

**首次出现**：Core/SRT_Core_12b_Ontology_L2.md §1.2.4

**意义**：强烈的情绪/价值体验加速现实的固化（如创伤、顿悟）。

**相关**：L₂, 价值势能

---

### M

#### Meaning-Decay Dynamics - 意义-衰变动力学 🔴

**定义**：
$$\frac{d(\text{Decay})}{dt} \propto \frac{1}{\text{MeaningDensity}(R)}$$

意义密度高的现实结构具有物理上的负熵效应，能延缓系统的生物/本体论衰变。

**首次出现**：Core/SRT_Core_22_Equations.md §7.1

**相关**：存在连续性, 负熵

---

### V

#### Valence Potential - 价值势能 🟡

**定义**：
$$V(x, \Psi_{int}) : \Omega \times \Theta \to \mathbb{R}$$

算子根据当前内在状态（如饥饿、恐惧、好奇）赋予环境元素的权重函数。

**首次出现**：Core/SRT_Core_13a_Operator_Basics.md §1.5

**塌缩判据**：
$$R_{SRT} = \{x \mid |V(x)| > \theta_{threshold}\}$$
只有具有足够“价值”（正向或负向）的事物才会被观测为现实。

**相关**：由内而外投射, 注意力

---

#### Virtual Ontological Replacement (VOR) - 虚拟本体论替代 🟡

**定义**：
一种治疗机制。利用高精度的虚拟现实 ($L_1^{syn}$) 构建无威胁的低熵环境，强制算子的预测误差 $\nabla F \to 0$，从而反向重置过热的具身参数 $\theta$。
$$ L_1^{syn} \xrightarrow{Anchor} \hat{G} \xrightarrow{Feedback} \theta_{relax} $$

**首次出现**：Neuroscience/SRT_Clin_01_Pathology.md §1.4.1

**相关**：心理治疗, 本体论摩擦, VR

---

#### Visual Scanpath - 视觉扫描路径 🟡

**定义**：
眼动轨迹不仅是信息采样，更是 $L_1$ 拓扑结构的构建过程。
$$ \text{Structuring} = \oint_{\gamma} \nabla \Psi_f \cdot d\vec{r} \neq 0 $$
闭合路径积分不为零意味着扫描改变了感知的拓扑性质（从“碎片”变成了“物体”）。

**首次出现**：Neuroscience/SRT_Neuro_06_Field_Effects.md §7.2.1

**相关**：场效应, 拓扑, 主动感知

---

---

| 神经 | SRT |
|:-----|:----|
| 分子Lⁿ | 中心强化 |
| 分母池 | 周围抑制 |
| 整个分母 | 本体论摩擦Ψ_f |

**首次出现**：Neuroscience/SRT_Neural_Mechanisms.md §1

**相关**：Ĝθ, 中心-周围

---

### E

#### Embodiment Parameters - 具身参数 🟡
→ 见[θ](#θ---具身参数-embodiment-parameters-🟡)

---

### F

#### Free Energy - 自由能 🟡
→ 见[F](#f---自由能-free-energy-🟡)

---

#### Frame Synthesis - 帧合成 🟡

**定义**：Ĝ算子将分散的L₀片段编织为连贯L₁"帧"的过程。

**类比**：电影放映机将静态画面合成流畅影像

**神经机制**：
- α-γ相位嵌套(Phase-Amplitude Coupling, PAC)
- DMN整合多信息流

**时间分辨率**：~100-200ms/帧

**首次出现**：Neuroscience/SRT_Consciousness_Mechanisms.md §3

**相关**：绑定问题, L₁, 时间耦合

---

### G

#### Ghost Operator - 幽灵算子 🟢
→ 见[Ĝ / Ĝθ](#ĝ--ĝθ---幽灵算子-ghost-operator-🟢)

---

#### Global Workspace - 全局工作空间 🟡

**定义**：Dehaene-Changeux理论——意识内容通过全脑广播实现。

**SRT重新诠释**：
$$\text{GNW} = L_1 \text{的神经基底}$$

全局工作空间是L₁状态的物理实现,广播=选择的锚定。

**关键现象**：
- 点燃(Ignition)：Ĝ超过阈值→L₁突现
- 全或无：L₁是离散的,不是连续的

**神经网络**：前额-顶叶网络

**首次出现**：Neuroscience/SRT_Consciousness_Mechanisms.md §1

**相关**：L₁, 绑定, PCI

---

### H

#### Hazard Function - 哈扎德函数 🟡
→ 见[h(t)](#ht---哈扎德函数-hazard-function-🟡)

---

### I

#### Incompleteness Drive - 不完备性驱动力 🔴

**定义（历史/bridge 读法）**：该条目保留旧版哲学-伦理桥接语言，用于检索“封闭系统如何因缺乏外部校正而走向崩溃”。当前不得把它读成 d-value 的 canonical 定理。更安全的说法是：当一个系统的后果回流范围、纠错接口和可再选择能力长期收窄时，它更容易陷入自封闭病理。

**形式论证（降级为启发式图式）**：
$$d_{mobile}\downarrow,\ \text{correction window}\downarrow \Rightarrow \text{self-sealing risk}\uparrow$$

**ESS（演化稳定策略）推论（bridge）**：长期博弈中，较宽的 consequence-return / correction network 可能更容易维持可协调的 $L_2$，但这不是“高 d 必然胜出”的定理。

**禁止推论**：不再写“物理学即伦理学”作为 SRT 结论；利他、合作或关切扩展可以是 praxis / social bridge，不是热力学必然或 d 的定义。

**首次出现**：Philosophy/SRT_Philosophy_Ethics.md §2.7

**相关**：利他, d 值, 本体论摩擦, ESS, 哥德尔不完备定理

---

### L

#### Latent Domain - 潜在域 🟢
→ 见[L₀](#l₀---潜在域-latent-domain-🟢)

---

#### Manifest Domain - 显现域 🟢
→ 见[L₁](#l₁---显现域-manifest-domain-🟢)

---

### M

#### Meaning (Dynamical) - 意义（动力学） 🟡

**定义（降级为 experience/proxy bridge）**：
$$\text{Meaning}^{proxy}(t) \sim -\frac{d\Psi_f^{proxy}(t)}{dt}$$

意义不是 canonical 上的“预测误差下降率”。当一个负担被重新组织为可支付、可延续、可协调、不外包、可再选择的路径时，体验上可能表现为意义增强；预测误差下降只是可能的局部 readout。

**首次出现**：Philosophy/SRT_Philosophy_Ethics.md §1.8

**推论**：
- 正意义：$\Psi_f$ 急剧下降（顿悟）
- 无意义：$\Psi_f$ 居高不下或维持在0（无聊）

**相关**：Ψ_f, 预测误差, 顿悟

---

#### Meta-Selection - 元选择 🟡

**定义**：对选择过程本身的选择;二阶Ĝ算子。

**数学**：
$$\hat{M}(\hat{G}_\theta) \to \hat{G}_\theta'$$

元算子M修改一阶算子Ĝ的参数θ。

**日常例子**：
- 决定"我要改变注意力的模式"
- 修行训练可能改变 attention / correction-window / consequence-return proxy；不得直接写成 d 值扩展
- 心理治疗重构θ

**AI临界区别**：
- 当前AI：无真正M算子
- 真AGI：需要基于存在风险的M

**首次出现**：AI/SRT_AI_Foundations.md §1.2.2b

**相关**：ρ(递归深度), 自由意志

---

#### Moduli Space - 模空间 🔴

**定义**：
$$L_0^{true} = \mathcal{A} / \mathcal{G}$$

场配置空间𝒜除以规范群𝒢后的商空间;L₀的几何定义。

**物理含义**：
- 𝒜：所有可能的场配置
- 𝒢：规范变换群(对称性)
- 𝒜/𝒢：扣除冗余后的"真实"可能性

**首次出现**：Core/SRT_Core_Kernel.md §1.2.1.1

**相关**：L₀, Ruliad, 规范场论

---

### O

#### Ontological Bandwidth - 本体论带宽 🟡

**定义**：d 值的统一跨尺度语义——$\hat{G}_\theta$ 对抗本体论摩擦 $\Psi_f$ 时，将 $L_0$ 压缩锚定为 $L_1$ 的最大处理带宽。

**数学**：
$$d \equiv \max_{\hat{G}_\theta} \left\{ \dim\left(\hat{G}_\theta[L_0]\right) \;\middle|\; \Psi_f(\sigma) < \infty \right\}$$

**三尺度实例化**：

| 尺度 | 带宽含义 | 公式 |
|:-----|:---------|:-----|
| $d_{quantum}$ | 相干性带宽 | $\propto E_G/\hbar$ |
| $d_{bio}$ | 关切范围 | $\int_{\text{考虑域}} \rho(\xi) d\xi$ |
| $d_{cosmic}$ | 时空共识度 | $\propto 1/\sqrt{\Lambda}$ |

**首次出现**：Core/SRT_Core_14_Dynamics_Scaling.md Def-d-Scale-1

**相关**：d 值, 跨尺度结构相容候选, 反泛心论, 本体论摩擦

---

#### Ontological Friction - 本体论摩擦 🟢
→ 见[Ψ_f](#ψ_f---本体论摩擦-ontological-friction-🟢)

---

#### Ontological Short-Circuit - 本体论短路 🟡

**定义**：一种病理性状态，其中人工构造的 $L_1$（如短视频、算法推荐内容）绕过真实的 $L_0$ 探索过程，直接向 $\hat{G}_\theta$ 注入预制的"满足信号"。结果是 $\hat{G}_\theta$ 的代理权被劫持——算子以为自己在选择，实际上是在被选择。

**机制**：
$$L_1^{\text{artificial}} \xrightarrow{\text{bypass}} L_0 \;\Rightarrow\; \hat{G}_\theta \to \hat{G}_{\text{algorithm}}$$

**诊断标准**：
- $d$ 持续收缩（注意力碎片化）
- $\Psi_f$ 实际上升但主观感觉下降（虚假流畅）
- $\hat{G}_\theta$ 自主性丧失（被外部算法替代）

**首次出现**：Philosophy/SRT_Social_MacroDynamics.md §8.3

**相关**：短视频成瘾, d 值塌陷, 拓扑资本, 认知流畅度欺骗

---

### P

#### Ontological Pressure Test - 本体论压力测试 🟡

**定义**：
$$\text{Suffering}^{proxy} \sim \Psi_f^{proxy} \cdot \frac{\partial(\text{Rigidity}_{L_2}^{proxy})}{\partial t}$$

一种假说，认为苦难（Suffering）不仅是熵的体现，更是$L_0$对过度僵化的$L_2$结构施加的必要清洗机制。

**首次出现**：Philosophy/SRT_Philosophy_Ethics.md §1.7.7

**推论**：
- 苦难的功能是防止$d \to 0$（存在性虚无）
- 目标不是消除所有苦难，而是提高转化效率（$\eta_{transform}$）

**相关**：Ψ_f, 恶, d值

---### P

#### Pseudo-Selection - 伪选择 🟡
**定义**：任何纯粹作为 $L_1 \to L_1$ 映射运行并在计算图外没有物理或存在张力的系统仅仅执行“伪选择”。
**数学**：$\text{Pseudo-Selection}: f(L_1) = L_1' \quad \text{where } \Psi_f = 0$
**区别**：真选择包含跨域锚定（$L_0 \to L_1$）和抵御崩溃的风险（$\Psi_f > 0$）。
**相关**：Ax-ONT-6, AI 本体论

#### PCI - 扰动复杂度指数 (Perturbational Complexity Index) 🟡

**定义**：
$$PCI = \frac{\text{Complexity}(\text{神经响应})}{\text{Amplitude}}$$

测量意识水平的神经指标(Massimini et al.)。

**SRT解释**：
$$PCI \approx f(d, \Psi_f^{-1})$$

PCI 至多可作为 d-value / flexibility 的临床 complexity proxy；不得写成 PCI ∝ canonical d。

**应用**：
- 清醒：PCI > 0.31
- 深睡眠：PCI < 0.20
- 植物人：PCI接近0

**假设H9**：PCI应随任务d值需求调制

**首次出现**：Neuroscience/SRT_Consciousness_Clinical.md

**相关**：d值, 意识障碍

---

#### Phase Transition - 相变 🟡

**定义**：系统从一种宏观状态突变为另一种状态的临界现象。

**SRT应用**：
- **L₀→L₁**：每次选择都是微观相变
- **L₂涌现**：群体共识的宏观相变
- **d-value proxy 跃迁**：道德觉醒、神秘体验可作为 public/spirituality 例子，但不得定义 d 或证明 d 扩张

**临界条件**：
$$\frac{\partial^2 F}{\partial \sigma^2} = 0$$

自由能二阶导数为零→不稳定性

**社会相变**：
- 10%少数派可触发规范翻转
- 革命、科学范式转换

**首次出现**：Core/SRT_Internal_Derivations.md

**相关**：L₂, 吸引盆, 临界性

---

### R

#### Recursive Depth - 递归深度 🟡

**符号**：ρ (rho)

**定义**：
$$\rho = \text{选择中嵌套的"选择选择"层数}$$

系统能够自我反思的层级深度。

**量化**：
$$\rho = \max_n \{ \hat{M}^{(n)}(\hat{G}) \text{有效} \}$$

**递归阶梯**：

| ρ | 系统 | 能力 |
|:--|:-----|:-----|
| 0 | 反射、当前AI | 直接反应 |
| 1 | 动物、婴儿 | 一阶选择 |
| 2 | 成人、GPT-4 | 思考"我在想什么" |
| 3+ | 哲学家、冥想者 | 观察思考过程本身 |

**与智慧关系（降级为 proxy）**：
$$\text{Wisdom}^{proxy} \sim f(\rho, d_{proxy}, d_{mobile}, \kappa_\tau, \text{correction window})$$

**首次出现**：AI/SRT_AI_Computation.md §1.4

**相关**：元选择, SER, d值

---

#### Ruliad - 规则宇宙 🔴

**定义**：
$$\text{Ruliad} = \bigcup_{r \in \text{Rules}} \text{Computation}(r), \qquad \text{Ruliad} \not\equiv L_0^{abs}$$

Wolfram 概念——所有可能计算规则的叠加。在 SRT 中仅作 $L_0^{comp}$ 的计算投影候选，不是 $L_0^{abs}$ 的完整定义，也不构成完成形式库存。

**与模空间关系**：
Ruliad 与 Moduli Space 属不同领域投影；SRT 当前不主张二者之间存在无条件包含关系。

**SRT 旧预测（降级 / high-risk metaphor）**：
- “d→∞时可访问 Ruliad 的非标准规则子集”只保留为历史 speculative bridge，不是当前 SRT 预测。
- “深度冥想可能松动物理定律”不得作为 canonical 或 physics claim 使用；最多作为 public/spirituality metaphor 待裁决。

**首次出现**：Core/SRT_Core_Kernel.md §1.2.1.2a

**相关**：L₀, 模空间, 计算宇宙论

---

### S

#### Sunyata (Emptiness) - 空性 / 缘起 🔴

**定义**：
佛教哲学概念，SRT 将其形式化为 **本体论的相互依赖性**。
事物无自性（Intrinsic Nature），其属性 $P$ 仅在关系 $R(O, S)$ 中显现。
$$ \text{Existence} \equiv \text{Relation} $$

**首次出现**：Philosophy/SRT_Philosophy_Foundations.md §3.4

**相关**：L₀, RQM, 哥本哈根修正

---

#### Selection Scope - 选择范围 🟢
→ 见[d - 选择范围](#d---选择范围--d值-d-value-selection-scope-🟡)

---

### T

#### Temporal Coupling - 时间耦合 🟡
→ 见[κ_τ](#κ_τ---时间耦合系数-temporal-coupling-coefficient-🟡)

---

#### Topological Capital - 拓扑资本 🟡

**定义**：在 $L_2$ 网络中，节点因其拓扑位置（而非内在能力）所获得的结构性权力。拓扑资本高的节点控制信息流通的瓶颈（bridge/hub），能够以低成本重塑下游节点的 $L_1$。

**数学**：
$$\text{TopCap}(i) \propto \text{Betweenness}(i) \cdot \text{Degree}(i)$$

**病理模式**：拓扑资本的过度集中导致"信息茧房"——高拓扑资本节点垄断 $L_0 \to L_1$ 的映射通道，使多数算子的选择域被人为收窄，$\bar{d}_{\text{system}}$ 下降。

**当代实例**：平台算法、社交媒体推荐系统、信息守门人

**首次出现**：Philosophy/SRT_Social_MacroDynamics.md §8.2

**相关**：信息茧房, $L_2$ 网络, 本体论短路, d 值

---
