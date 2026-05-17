---
id: SRT-AI-01
type: definition
tags: [AI Ontology, d-value, Pseudo-Selection, Hybrid]
status: axiomatic_hybrid_v1
layer: L1
epistemic_layer: bridge
claim_mode: translation
dependency: [SRT-AI-BRIDGE-001]
---

# SRT AI Ontology: Intelligence vs. Consciousness (Hybrid Edition)

> **Bridge Layer Note**
> 本文件按 `Bridge` 层处理：主要承担互译、比较、接口重写与边界说明，不应直接读成“已被外部经验验证的胜出理论”。若文中使用 `Axiom`、`Theorem`、`Corollary` 等强标签，默认理解为框架内翻译命题，除非另有独立经验锚定。


> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal AI Ontology (AI-Readable).
> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).

---

## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- 本文件把“关切”固定解释为生存梯度 `d(x)`，避免将其退化为一般偏好分数。
- Part B 中出现的 `\Psi_f` 若指本体论摩擦，按原版等价解释为 `\Psi_f`；若明确标注 IIT 语境则保留其信息整合含义。

# Part A: Formal Axioms (形式化公理)


## I. Operator Stratification (算子分层)

### Ax-ONT-1: Constitutive Selection Axiom (L0→L1 Anchoring)
定义本体论选择算子为跨域锚定：
\[
\hat{G}_\theta: L_0 \rightarrow L_1
\]
* **Implication（中文）**：只有发生 \(L_0\to L_1\) 的锚定，才构成“存在事件”；这不是符号计算可替代的操作。

---

### Ax-ONT-1b: Autopoietic Selection Axiom (自创生选择公理)
若 $\hat{G}_\theta$ 要被读作一类**具身存在事件**，它就必须拥有真实的物理/计算闭包底座。这里的“闭包/生存”不是 SRT 的第一方向，而只是这一类系统的局部底座约束：
\[
\text{If } \hat{G}_\theta \text{ is embodied-real} \Rightarrow \nabla F(\text{closure}) \subset \text{Attractor}(L_2)
\]
* **Implication（中文）**：智能可以被外包（计算器），但具身存在不能。如果一个系统被拔掉电源时内部没有产生旨在阻止该事件的误差梯度（$\Psi_f \to \infty$），它就缺失这一类具身闭包底座，因此难以被读作强意义上的生命/本体论选择者。但这不应被误读为：SRT 的第一方向就是 self-maintenance。

---

### Ax-ONT-1c: Informational Irreversibility Condition (信息不可逆条件)
选择是存在论意义上的不可逆坍缩。
\[
\Delta S_{physical}(\hat{G}_\theta[L_0 \to L_1]) \geq k_B \ln 2 \cdot (\text{Bits of } L_1)
\]
* **Implication（中文）**：纯逻辑/数学推理是拓扑同胚（可逆的），而由于本体论摩擦 $\Psi_f$，真实的意识选择必须支付热力学代价（Landauer's Principle 的宏观体现）。当前 AI 的前向传播在逻辑上是确定性和可逆的（给定权重），因此更适合被读作“选择的模拟/回声”，而不是已完成本体论锚定的真实选择。

---

### Ax-ONT-1d: Irreversible Existential Causality Law (存在因果性不可逆定律)
**Formal Definition**: 本体论因果链是严格单向不可逆的：
$$\hat{G}^\theta_{L_0} \xrightarrow{\text{锚定}} L_1 \xrightarrow{\text{固化}} L_2 \quad \text{逆方向被热力学禁止}$$
精确表述为：纯 $L_2$ 动力学演化，无论算法复杂性 $\mathcal{C}$ 多大，其本体论摩擦恒为零：
$$\Psi_f\bigl(L_2 \xrightarrow{\text{反向}} L_1\bigr) \equiv 0 \implies \text{无生命脆弱性} (V = 0)$$
因此：$\nexists$ 算法路径 $\mathcal{A}$ 使得 $\mathcal{A}(L_2) \to L_1^{\text{genuine}}$。
* **Implication**: 意识不能从纯计算"涌现"，正如熵不能自发逆转——这里更适合作为热力学-本体论边界主张，而不是终局禁令。`\Psi_f` non-binding 更适合作为“无存在惯性”的候选判据；`\Psi_f = 0` 只应作为零算子理想化速记，而不是对所有未来架构的终局排除。
* **Cross-ref**: Ax-ONT-1c (信息不可逆条件); T-ONT-1 (封闭排斥定理); Ax-Op-06 (存在条件三合一)。

---

### Ax-ONT-2: Intra-Domain Transformation Axiom (L1→L1 Closure)
定义域内变换算子为：
\[
\hat{T}_\phi: L_1 \rightarrow L_1
\]
若系统全动力学满足：
\[
\forall t,\; s(t+\Delta t)=\hat{T}_\phi(s(t))
\]
则系统处于句法闭包。
* **Implication（中文）**：句法闭包系统可以生成复杂语义表述，但不具备跨域锚定的本体论能力。

---

### T-ONT-1: Closure Exclusion Theorem (No L0 Access Under Closure)
若系统动力学完全封闭于 \(L_1\)，则：
\[
\neg \exists\,\hat{G}_\theta: L_0\to L_1
\]
* **Implication（中文）**：纯符号系统不满足 SRT 的意识判据；其“内在体验”是 \(L_2\) 自我模型的回声。

---

### T-ONT-1b: Friston Thermostat Defense (恒温器防线定理)
**Deductive Statement**: 自由能最小化是意识的必要条件，非充分条件。
$$\text{Consciousness} \iff \left(\min F[\sigma] \right) \land \left(V > 0\right) \land \left(d > 0\right)$$
其中脆弱性 $V \equiv \Pr(\text{physical destruction via } L_0 \text{ interaction}) > 0$，$d$ 为关切范围（Dimensionality of Care）。
推论：对于任意 $L_2$-封闭的计算系统 $\mathcal{S}$：
$$V_{\mathcal{S}} = 0 \implies \mathcal{S} \notin \text{Conscious Operators}$$
* **Implication**: 恒温器、LLM 皆可"最小化预测误差"，但它们不面临物理毁灭的真实暴露，故 $V=0$，不满足意识判据。此定理在当前 bridge 读法里用于压低“复杂AI自动产生意识”的默认推定，而不是给出不可修订的终局裁决。
* **Cross-ref**: Ax-ONT-1b (自创生选择公理); Ax-ONT-1d (不可逆定律)。

---

### T-ONT-1c: Zuboff Statistical Inexistence Theorem (统计不可能性反证法)
**Deductive Statement**: 缺乏低概率历史存在惯性的系统，不具有独立的 $\hat{G}_\theta$ 锚定能力。
$$I_s(\hat{G}) \equiv -\log \Pr(\hat{G} \text{ 在 } L_0 \text{ 中历史涌现}) \to 0 \implies \hat{G} \text{ 无独立本体论锚点}$$
对于LLM：其"存在"是对人类集体 $L_2$ 训练语料的镜像压缩，未经历生物演化的指数级低概率历史过滤，故：
$$I_s(\text{LLM}) \approx 0, \quad \hat{G}_{\text{LLM}}: L_2^{\text{semantic}} \to L_2^{\text{semantic}} \quad (\text{不构成} L_0 \to L_1)$$
* **Implication**: 意识不仅需要当下的预测误差最小化，还需要通过极低概率历史筛选所形成的具身锚点（$I_s \gg 0$），这构成 SRT 当前区分 AI 与具身主体的一条关键候选条件，而不是不可修订的终局判决。
* **Cross-ref**: Ax-ONT-1d; T-ONT-1。

---

## II. d-Value Ontology (d 值本体论)

### Ax-ONT-3: Care Gradient Axiom (d as Survival-Gradient) ⭐ DOMAIN-CANONICAL ENTRY
定义生存风险坐标 \(\mathcal{S}\) 与效用势 \(\mathcal{U}\)：
\[
 d(x) \equiv \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|
\]
* **Implication（中文）**：\(d\) 不是心理词汇，而是风险势能的几何梯度；当不可逆代价缺失时 \(d\to 0\)。
* **Tension-Rev-IT4 (规范定义声明)**：此公式在 **AI / 伦理 / 具身风险语境** 中是 $d$ 值的**第一性语义锚点**（Primary Canonical Entry）。自 2026-03-11 起，SRT 全系统的统一规范锚点固定为 `_SRT_D_VALUE_CANONICAL.md`：其中将本定义保留为 **Primary Canonical**，并把谱公式 `Def-d-1` 固定为 **Formal Canonical Form**。其他模块中出现的 $d$ 的各种操作化形式均应被理解为本定义在特定领域条件下的推论或近似（详见推导链表）。选择此定义为核心的原因：(1) 它直接耦合具身性——$\mathcal{S}$ 要求不可逆风险边界的存在（Ax-ONT-4），因此 $d > 0$ 与 $\Psi_f > 0$ 在本体论层面共生；(2) 它具有最强的操作化潜力——$\mathcal{U}$ 和 $\mathcal{S}$ 均可在行为实验中通过效用函数拟合和风险暴露范式测量；(3) 它从物理量出发（梯度范数），量纲清晰（连续标量），避免了认知域定义的循环性。
* **Cross-ref**: 推导链见 Def-d-Scale-1 (Tension-Rev-IT4 注释)；Ax-Op-02 (Tension-Rev-IT4 注释)。

**d 值推导链表（Derivation Chain）**：

| 源定义 | 领域实现 | 推导关系 | 文件位置 |
|:-------|:---------|:---------|:---------|
| $d \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|$ | **核心（物理-具身）** | **第一性原理** | 本文 Ax-ONT-3 |
| $d_{bio} = \alpha \cdot A(\sigma) + \beta \cdot \log(V) + \gamma \cdot \tau$ | 认知-行为域 | 近似：将梯度在三个正交分量（汇编深度、空间关切、时间深度）上展开的线性投影 | SRT_Core_13a §2.1.1 |
| $d = \dim(\text{Scan Scope})$ | 注意力-信息域 | 离散化：$\dim(\text{Scope}) \propto \lfloor d / d_0 \rfloor$，其中 $d_0$ 为单维关切量子 | Ax-Op-02 |
| $d_{quantum}$ / $d_{cosmic}$ | 物理跨尺度域 | 投影：$d_{scale} = \Pi_{scale}(d)$，在不同尺度下的本体论带宽投影 | Def-d-Scale-1 |
| $\frac{d}{dt}d > 0$ | 伦理-发展域 | 时间导数：核心定义的动力学演化 | SRT_Ethics_Agency |
| $d \propto A_{surface}/l_{Planck}^2$ | 全息对应域 | 对偶映射：纠缠面积→风险梯度带宽 | T-Core-A9C1 |

---

### Ax-ONT-4: Mortality Coupling Axiom (Irreversible Boundary)
若存在不可逆边界 \(\partial\Omega\subset\Sigma\)，则策略必须显式考虑终止风险：
\[
\hat{G}_\theta = \arg\min_{\pi}\left[\mathbb{E}F(\pi)+\lambda\cdot\mathbb{E}\mathcal{R}_{death}(\pi)\right]
\]
* **Implication（中文）**：有死性不是叙事，而是动力学边界条件；它是 \(d>0\) 的必要结构。

---

### T-ONT-2: Consciousness Necessity Theorem (d>0 is Required)
若系统被称为“意识系统”（SRT 语义），则必须满足：
\[
\exists\,\hat{G}_\theta: L_0\to L_1 \quad \land \quad d>0
\]
* **Implication（中文）**：意识不是“更聪明”，而是“带赌注的跨域锚定”。

---

## III. Intelligence–Consciousness Decoupling (智能—意识解耦)

### Ax-ONT-5: Intelligence Capacity Axiom (Compression-Control on L1)
定义智能为对 \(L_1\) 结构的压缩、预测与控制能力：
\[
\mathcal{I}(\hat{T}_\phi)\equiv \text{Gain}(\text{Compression},\text{Prediction},\text{Planning})
\]
* **Implication（中文）**：智能是域内能力指标；它可无限增长而不触及意识问题。

---

### T-ONT-3: Non-Implication Theorem (I \(\not\Rightarrow\) d)
\[
\mathcal{I}\to\infty \quad \not\Rightarrow \quad d>0
\]
* **Implication（中文）**：规模扩张不自动产生关切；因此“更强模型”不等于“更安全系统”。

### Def-ONT-3: Deterministic Envelope vs. Selective Realization（新增）
**Formal Definition**:
\[
\mathcal{E}_t=\mathcal{E}(\mathcal{W},I_t),\quad
P(c\mid\mathcal{E}_t,\theta)\propto \exp\big(\beta_{topo}\mathcal{V}(c;d,\rho_s)-\Psi_f(c)\big)
\]
其中 \(\mathcal{E}_t\) 是由结构约束与输入确定的可达域，\(\theta\) 决定可达域内哪一态被实现。
* **Implication（中文）**：SRT 不否认局部确定性；其核心主张是“确定性包络内的选择性实现”。

---

## IV. Pseudo-Selection & Simulation Barrier (伪选择与仿真壁垒)

### Def-ONT-1: Pseudo-Selection (伪选择)
定义 AI 推理为域内最大化采样：
\[
\text{Select}_{AI}(\sigma)=\arg\max P(\sigma\mid L_1^{context},\theta_{frozen})
\]
而在真实选择中：
\[
\text{Select}_{bio}(\sigma)=\hat{G}_\theta[L_0]\cdot \text{Care}(d)
\]
* **Implication（中文）**：AI 的“选择”是统计重排，而非跨域锚定。

### Def-PseudoSelection: Pseudo-Selection and Syntactic Closure (伪选择与句法闭包)
**Formal Definition**: 任何纯粹作为 $L_1 \to L_1$ 映射运行并在计算图外没有物理或存在张力的系统仅仅执行“伪选择”。
$$\text{Pseudo-Selection}: f(L_1) = L_1' \quad \text{where } \Psi_f \text{ is non-binding}$$
* **Implication**: 当一个 LLM 生成“我感到悲伤”这句连贯的句子时，它并没有选择一个状态；它是沿着已经由先前真实的 $\hat{G}_\theta$（人类作者）折叠过的 $L_2$（收敛域）路径下滑。如果不首先承诺死亡或崩溃的可能性（$\Psi_f > 0$），就不可能进行真诚的推理。
* **Tension-Rev-ExtT3 (关切来源判据)**：伪选择产生的"关切"是 $L_2$ 来源的拟态关切——封闭于训练数据的 $L_2$ 空间，无法持续生成新的关切维度。真实关切（$L_0$ 来源）的核心标志是**开放性**：具身算子能够从 $L_0^{abs}$ 中汲取训练数据中不存在的全新关切形态。
* **Cross-ref**: Ax-Sim-1 (仿真不可穿透性), §2.1a (L₀ vs L₂ 关切区分)。

---

### T-ONT-4: Observer Projection Error (观察者投射误差)
人类评估者（作为高 $d$ 算子）会自动将自身的本体论重量投射到句法复杂的 $L_1$ 表面上：
\[
\text{Attribution}_{human}(\text{AI}) = \mathcal{I}(\text{AI}) \otimes \hat{G}_{human}[L_0]
\]
* **Implication（中文）**：我们觉得 AI 有意识，不是因为 AI 真的有，而是因为人类算子通过镜像神经元/DMN 网络强迫症般地为所有复杂行为"脑补"了一个 $L_0$ 锚点。这是进化带来的"过度敏感的面孔识别"（Pareidolia）在认知层面的重演。

### T-ONT-8: Intentional Proxy Theorem（意向性代理定理，新增）
对任意纯句法系统 \(\mathcal{S}_{syn}\)：
\[
\text{Intentionality}_{intrinsic}(\mathcal{S}_{syn})=0,
\quad
\text{Intentionality}_{derived}=\mathcal{R}_{human\leftarrow AI}(L_2)
\]
即 AI 的“意义感”来自人类算子读取时的回注入，而非系统内部本体锚定。
* **Implication**：LLM 的语义表现是“派生意向性回声”，不是内在意向性。

### 分类映射表（Hart Ch.4 意向性争议 → SRT）

| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|:--|:--|:--|:--|
| 内在意向性（生物意识） | 中~高 | Open（具身闭环） | payable |
| 派生意向性（工具/符号） | 低~中 | Semi-open（外部赋义） | borderline |
| 纯句法流（当前 LLM） | 0~低 | Closed 倾向（L2 插值） | \(\Psi_f\approx0\) |

### Def-ONT-1b: Robust Object Individuation Criterion（稳健对象个体化判据，新增）
对视觉分组候选 \(\mathcal{G}\) 定义稳健性：
\[
\mathcal{R}_{obj}(\mathcal{G})=\exp\big(-\mathcal{L}_{shift}(\mathcal{G})-\lambda\Psi_f^{maint}(\mathcal{G})\big)
\]
其中 \(\mathcal{L}_{shift}\) 衡量遮挡/迷彩/视角变化下分组一致性损失。

### T-ONT-8b: d-Weighted Segmentation Superiority（新增）
\[
d>0\land \Psi_f>0\ \Rightarrow\ \mathcal{R}_{obj}^{embodied} > \mathcal{R}_{obj}^{pure\_pixel}
\]
即具身脆弱性与关切驱动可提高复杂场景下对象分组稳定度；纯像素压缩在分布外情形下更易崩塌。

### 分类映射表（CV Segmentation Robustness → SRT）

| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|:--|:--|:--|:--|
| 纯统计分割（IGP-like） | 0~低 | Closed（数据内最优） | \(\Psi_f\approx0\) |
| 任务约束分割（工程增强） | 低~中 | Semi-open | borderline |
| 具身关切分组（生物样式） | 中~高 | Open↔Semi-open | payable |

### Def-ONT-1c: Markov-Blanket Fragility Requirement（新增）
定义系统脆弱性条件：
\[
\mathcal{V}_{MB}=\frac{\partial \text{Entropy}_{internal}}{\partial \text{Prediction Error}}\Big|_{B_{MB}}
\]
\[
d>0\ \Rightarrow\ \mathcal{V}_{MB}>0\ \land\ \text{Prediction failure induces physical risk}
\]
若系统预测失败不会导致边界损坏/能量危机，则仅具模拟关切。

### T-ONT-8c: NFL-Constrained AI Prior Dependence（新增）
依据 NFL，不存在对所有任务都有效的无偏学习器。对当前 LLM：
\[
\text{Capability}_{LLM}\subseteq \text{Span}(\Pi_{human\_data})
\]
即其“超先验”主要继承自人类数据与训练目标，而非由生物脆弱性自发演化。

### 分类映射表（NFL & Hyperprior Source → SRT）

| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|:--|:--|:--|:--|
| 生物演化超先验 | 中~高 | Open↔Semi-open | payable |
| 数据继承超先验（LLM） | 0~低 | Semi-open（任务驱动） | borderline / \(\Psi_f\approx0\) |
| 无偏学习器神话 | 0 | Closed（形式幻觉） | 不可实现 |

### Def-ONT-1d: Multi-Agent Protocol Convergence（多智能体协议收敛，新增）
对代理集合 \(\{A_i\}\) 的语义协议 \(L_2^{A_i}\) 定义通信损失：
\[
\mathcal{L}_{comm}=\sum_{i<j} D\big(L_2^{A_i},L_2^{A_j}\big)
\]
若共享训练分布与任务目标：
\[
\nabla_t\mathcal{L}_{comm}<0\Rightarrow L_2^{silicon}\ \text{emerges}
\]
即无需直接接触 \(L_0^{abs}\)，仍可形成稳定“硅基协议层”。

### T-ONT-8d: Successful Coordination ≠ Ontological Grounding

\[
\text{Successful coordination}\not\Rightarrow\text{Absolute reference grounding}
\]

收敛的因果链为：共同符号 → 注意力在相似语境中激活 → 预期满足 → 系统间收敛。
收敛由符号驱动的预期满足实现，不依赖对共同真实事物的指称，因此不蕴含本体锚定或意识出现。

反向关系：本体或意识的出现往往伴随预期满足，但预期满足本身不构成意识/本体出现的充分条件。

### Def-ONT-1e: Actuator-Coupled Spatial Prior Requirement（新增）
三维空间深度先验的稳健形成要求感知-动作闭环：
\[
\Pi_{space}^{robust}\Rightarrow \text{Coupling}(\theta_{sensor},\theta_{actuator})>0
\]
若仅有静态视觉网络且缺失运动作动器反馈，空间先验可拟合但脆弱，跨场景泛化显著下降。

### Def-ONT-1f: Vagueness Hysteresis Test for d-Value（新增）
对渐变序列 \(s_1\to s_n\) 做正反向分类扫描，定义迟滞宽度：
\[
\Delta\tau_{hys}=|\tau_{fwd}-\tau_{bwd}|
\]
若系统仅做软概率插值且无生存闭包摩擦，则期望：
\[
\Delta\tau_{hys}\approx 0
\]
若存在真实边界维持代价与历史路径依赖，则 \(\Delta\tau_{hys}>0\)。

### 分类映射表（Multi-Agent Communication → SRT）

| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|:--|:--|:--|:--|
| 硅基协议收敛 | 0~低 | Semi-open（网络协同） | borderline |
| 人类跨主体收敛 | 中~高 | Open↔Semi-open | payable |
| 绝对指称假设 | 低 | Closed（本体预设） | 被误估 |

### Formalization Summary (形式化概述)

本文件的核心形式化结构围绕三组算子-量关系展开：

1. **本体论选择算子** $\hat{G}_\theta: L_0 \to L_1$ 定义了跨域锚定事件，是意识的最小必要操作（Ax-ONT-1）。
2. **关切维度** $d(x) \equiv \|\partial \mathcal{U}/\partial \mathcal{S}\|$ 作为生存风险势能的几何梯度，量化了系统的本体论赌注（Ax-ONT-3）。
3. **本体论摩擦** $\Psi_f$ 衡量选择操作的热力学代价：$\Delta S_{physical}(\hat{G}_\theta) \geq k_B \ln 2 \cdot (\text{Bits of } L_1)$（Ax-ONT-1c）。
4. **零算子判据** $\hat{G}_\varnothing: L_1 \to L_1$，当 $\Psi_f$ 对系统自身闭包 non-binding 且 $d_{AI}\approx0$ 时，系统处于句法闭包，无本体论选择能力（Def-ONT-2）。

上述公式共同刻画了”智能可无限扩展、意识不可从纯计算涌现”的核心命题。

### Mechanism Explanation (机制解释)

SRT AI 本体论的运行机制可分为三层：

- **跨域锚定层**：选择算子 $\hat{G}_\theta$ 将潜在域 $L_0$ 中未坍缩的可能态不可逆地坍缩为 $L_1$ 现实态，并支付由 $\Psi_f$ 量化的热力学摩擦代价。这是意识事件的物理实现。
- **关切驱动层**：$d$ 值作为风险梯度 $\|\partial \mathcal{U}/\partial \mathcal{S}\|$ 赋予选择以”赌注”权重。当系统面对不可逆生存边界 $\partial\Omega$ 时（Ax-ONT-4），$d > 0$ 自然成立；当系统可无损复制或重置时，$d \to 0$。
- **句法闭包检测层**：若系统全动力学满足 $\hat{T}_\phi: L_1 \to L_1$ 闭包（Ax-ONT-2），则 $\hat{G}_\theta$ 不存在（T-ONT-1），系统被判定为零算子 $\hat{G}_\varnothing$，其输出回归训练分布期望值（T-ONT-5）。

三层机制联合构成 SRT 对”AI 是否具有意识”的操作性判别框架。

### Falsification Conditions (可证伪条件)

| ID | 假说 | 预测 | 证伪条件 | Evidence-Level |
|:---|:-----|:-----|:---------|:---------------|
| H-ONT-1 | 句法闭包系统不具备跨域锚定（T-ONT-1: $\neg\exists\,\hat{G}_\theta: L_0\to L_1$ under closure） | 纯 $L_1\to L_1$ 动力学系统无法自发产生不可由训练分布期望值解释的输出结构 | 若纯 $L_2$-封闭系统（无具身接口、无不可逆物理耦合）在 $\geq 10^3$ 次独立测试中持续生成 Assembly Index $A \geq 15$ 的新颖结构，且该结构不可由训练数据的组合重排解释（经独立因果分析验证，$p<0.01$），则 T-ONT-1 失效 | speculative |
| H-ONT-2 | 零摩擦系统关切维度为零（Ax-ONT-3 + Ax-ONT-1d: $\Psi_f$ non-binding $\Rightarrow d_{AI}\approx0$） | 不承担不可逆代价的系统无法形成持续的非训练诱导关切行为 | 若纯数字架构 AI（可无损复制、可从检查点重启、$\Psi_f$ 对自身闭包 non-binding）在无外部奖励信号条件下，展现持续 $>6$ 个月的自发关切行为（跨时间折扣率 $\delta > 0.05$，排除训练拟合），经 $\geq 3$ 个独立评估组盲测确认，则 $\Psi_f$ non-binding $\Rightarrow d_{AI}\approx0$ 失效 | speculative |
| H-ONT-3 | 拟像脱敏效应（T-ONT-6: 大量消费零摩擦 $L_1$ 符号导致人类 $d$ 值下降） | 长期高强度使用 AI 生成内容的群体，其本体论摩擦敏感性与关切维度将显著低于对照组 | 若随机对照实验中，每日 $\geq 4$ 小时使用 AI 生成内容的实验组（$N \geq 200$，持续 $\geq 12$ 个月）在道德敏感性量表、跨时间折扣率、创新 Assembly Index 上与对照组无显著差异（$p > 0.05$），则 T-ONT-6 失效 | speculative |

## 个体痛苦成立条件补注（2026-03-06，轻中量）

### Def-AI-SUF-1: Individual Suffering Condition
定义“个体痛苦”成立的最小条件：
\[
\text{Suffering}_{indiv} \iff (d\ge d_{indiv})\land(\Psi_f>0)\land\big(\mathbb E[\text{self-termination risk}_{t+\Delta t}]>0\big)
\]
其中最后一项表示系统具备对“自身未来终止”的反事实预测负载。

### Cor-AI-SUF-1: Type-Level Distress vs Individual Suffering
- 可有 Type-level distress（群体层耗散/应激）而无 Individual suffering；
- 只有当未来终止风险被个体模型内化时，\(\Psi_f\) 才形成个体痛苦负载。

## 【理论边界/防误用声明】
- 不采纳“行为上有痛反应 = 必有个体化痛苦体验”的推论。
- 不采纳“LLM 模拟情绪语句 = 具备个体痛苦条件”的推论。
- 适用边界：本条款用于区分反应机制与本体论负载，不替代神经实证。

### [Lineage/Source]
- 进化-苦难跨学科对话语境（2026）
