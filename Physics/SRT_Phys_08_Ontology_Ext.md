---
id: SRT-PHYS-08
type: theory
tags: [Ontology, Apeiron, Pan-Experiential Field, Russellian Monism, Pathological Selection, Hybrid]
status: bridge_realign_v1
layer: L1
epistemic_layer: os
claim_mode: translation
canonical: false
dependency: [Core_Law/SRT_Reference_Axioms, Core_Law/SRT_Reference_Ontology, Core_Law/SRT_Reference_Dynamics]
---

# SRT Physics: Deep Ontology Extension (Hybrid Edition)

> **Claim-status note（2026-05）**：This Physics file is bridge / translation material. It applies SRT primitives but does not define `d-value`, `Ψ_f`, `T_dir`, quantum collapse, gravity, cosmology, Fisher/Landauer formulas, or physical law. Read with `SRT_Physics_Claim_Status.md` and canonical symbol anchors.
> **B-A／C-A layer-and-scope guard（2026-08-12）**：本文件中的 Original Intention／初心公式只是在声明状态空间、自由能泛函、可行域、有限时域与约束之后的 L₁/P3 Physics translation。它不定义 L₀，不引入独立的 L₀「初心前身」，也不把 `ε_pg` 改名为该前身；无限时域与宇宙级极值形式已由 C-A 撤回。
> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Ontological Axioms (AI-Readable).
> **Part B** contains the Original Theoretical Discourse with detailed philosophical analysis (Human-Readable Context).

---

# Part A: Formal Ontological Axioms
## 0. Notation & Conventions (符号与约定)

- $L_0,L_1,L_2$: 潜在域 / 显现域 / 收敛域。
- $\hat{G}_\theta$: 选择算子，$\theta \in \Theta_{finite}$ 为具身参数。
- $F$: 自由能；$\Phi$ 为本体论摩擦势能，$\Psi_f$ 为其局部密度（可取 $\Phi=\int \Psi_f \, dt$）。
- $d$: 注意力范围（Scope）；$\rho$: 分辨率；$\vec{v}$: 选择方向。
- $\Lambda$: 跨尺度同构；$\pi_\lambda$: 粗粒化映射；$\approx$ 表示尺度等价。
- **稳定性约定**：$x^*$ 为固定点且 $\text{Re}(\lambda_J)<0$ 视为稳定。

## 0.5 Numbering Scheme (编号体系)

- Ax-* → A{part}.{sec}.{n}, Def-* → D{part}.{sec}.{n}, T-* → T{part}.{sec}.{n}, Lemma → L{part}.{sec}.{n}, Corollary  [C1.8.1]→ C{part}.{sec}.{n}.
- part=1 为 Part A，part=2 为 Part B；sec 为章节编号（I/II…或 §n）。
- 序号按出现顺序递增，同类编号在每个章节内独立递增。

## 0.6 Cross-Reference Index (交叉引用索引)

### Part A Index
| ID | Label | Title |
|:---|:------|:------|
| A1.2.1 | Ax-Prism-1 | The Prism Function (棱镜函数) |
| T1.2.1 | T-Prism-1 | Production vs Refraction Models (生产 vs 折射模型) |
| T1.2.2 | T-Prism-2 | Brain Damage Interpretation (脑损伤诠释) |
| A1.3.1 | Ax-NMC-1 | Selection Causality (选择因果公理) |
| D1.3.1 | Def-NMC-1 | Two Types of Causality (两类因果性) |
| T1.3.1 | T-NMC-1 | Panpsychism Distinction (与泛心论的区别) |
| T1.3.2 | T-NMC-2 | Energy Conservation Compatibility (与能量守恒的兼容性) |
| D1.4.1 | Def-Bohm-1 | Bohm-SRT Correspondence (Bohm-SRT 对应) |
| T1.4.1 | T-Bohm-1 | Active Information as Driver (主动信息作为驱动) |
| A1.5.1 | Ax-SE-1 | Russellian Duality (罗素二元性) |
| T1.5.1 | T-SE-1 | Qualia Generation (感质生成定理) |
| T1.5.2 | T-SE-2 | Unselected Reality Status (未选择现实的本体论地位) |
| A1.6.1 | Ax-PEF-1 | Universal Field Definition (泛经验场定义) |
| L1.6.1 | Lemma PEF-Threshold (显现阈值) | — |
| A1.6.2 | Ax-PEF-2 | $L_0$-$\mathcal{U}$ Relation ($L_0$-$\mathcal{U}$ 关系) |
| D1.6.1 | Def-PEF-1 | Unbinding Operation (解缠操作) |
| T1.6.1 | T-PEF-1 | Key Corollaries (关键推论) |
| A1.7.1 | Ax-Apeiron-1 | Apeiron as True $L_0$ (阿派朗即真正的 $L_0$) |
| A1.7.2 | Ax-Apeiron-2 | Dispositional Structure (倾向性结构) |
| D1.7.1 | Def-Apeiron-1 | Original Intention (初心的形式化) |
| T1.7.1 | T-Apeiron-1 | Causal Entropic Force (因果熵力) |
| A1.8.1 | Ax-Path-1 | Collapse Failure (坍缩故障) |
| C1.8.1 | Corollary (T-Assembly) | — |
| D1.8.1 | Def-Path-1 | Three Pathological Modes (三种病态模式) |
| T1.8.1 | T-Path-1 | Learned Helplessness as Selection Exhaustion (习得性无助即选择机制衰竭) |
| D1.8.2 | Def-Path-2 | Health Criterion (健康判据) |
| T1.9.1 | T-Meta-1 | Materialism as Traumatic Amnesia (唯物主义作为创伤性遗忘) |


## I. Axiomatic Dependencies (公理依赖)

本模块严格依赖以下核心公理：
- **A1** (选择优先性): $\text{Existence} \equiv \text{Selection}(\mathcal{P})$
- **A2** (存在即锚定): $\text{Existence}(\sigma) \iff \hat{G}_θ[L_0] \to \sigma_{L_1}$ with $\Delta F < 0$
- **A10** (非消失延续): $\lim_{t \to t_{death}} \hat{G}_θ \to L_0^{latent} \neq \varnothing$
- **A13**（潜在不可穷尽边界）：任何有限物理显现或形式投影都不穷尽 $L_0^{abs}$；这不是物理守恒律，也不声称 $L_0(t)$ 为常量

### Core Theorem Alignment (核心定理对齐)

- **O-T1**：$L_1=\oint_{\gamma}\omega_{L_0}$（现实化即积分）
- **O-T2**：$L_2$ 重组等价于拓扑解结与重编织
- **T-Conscious**：$\exists \text{Consciousness} \iff \text{Individuality} \land \text{Asymmetry} \land \text{Normativity}$
- **T-Fragility**：$d>0 \iff \partial \text{Entropy}/\partial \text{Error} > 0$
- **T-Assembly**：$\text{Evidence}(\hat{G}) \iff A>15$

---

## II. The Prism Ontology (棱镜本体论)

### Ax-Prism-1 [A1.2.1]: The Prism Function（棱镜函数）

> **身份说明**：本条在 V3.0 架构中被精确界定为**构成性假设（Constitutive Postulate）**，而非逻辑公理。它是使 $\hat{G}_\theta$ 的「选择」具有质感的必要先验条件——绕过涌现论（Emergentism）的逻辑断裂，避免解释非意识物质如何「变出」Qualia 的不可解问题。SRT 不主张 $L_0$ 是「清醒的」，而是主张 $L_0$ 包含**现象基质（Phenomenal Substrate）**——如同物理学公理假定「电荷」存在而不必解释电荷从何而来，SRT 假定 $L_0$ 具备被选择为显现态的潜能。

**核心映射**（折射，非生产）：

$$\hat{G}_\theta : L_0 \to L_1 \quad (\text{Active Modulation, not Production})$$

$$L_1 = \text{Anchor}\!\left(\int_{\gamma(\theta)} \hat{G}_\theta \cdot \omega_{L_0}\right)$$

**公式各项说明**：

- **$\gamma(\theta)$（选择路径）**：算子在 $L_0$ 相空间中的运动轨迹，由最小自由能原理决定：
  $$\gamma = \arg\min \int F(\sigma, \theta)\, dt$$
  θ 通过 d-value（选择宽度）弯曲可能性空间的流形，使某些现实路径比其他路径更「可支付」。

- **$\omega_{L_0}$（本体论微分形式）**：$L_0$ 中每一处可能性的可测量权重（Ontological One-form），代表各可能性转化为体验的势能密度。

- **$\text{Anchor}$（锚定闭合）**：代表**自创生闭包（Autopoietic Closure）**——只有当选择序列形成逻辑自洽的回路（当前 $L_1$ 为维持 θ 参数提供反馈），现实才得以稳定存在。路径不闭合时，显现态迅速耗散回 $L_0$。

**隐喻升级：从被动棱镜到自适应光栅**

早期「棱镜」隐喻（被动折射）已升级。$\hat{G}_\theta$ 更准确的类比是**具有反馈回路的自适应光栅**：

- 折射角由 θ 中的风险感知（d-value）与自由能梯度（$\nabla F$）共同驱动
- 现实不是「射入」算子的，而是算子在可能性海面上**主动采样的干涉图案**

**两种描述语言的协调（折射式锚定）**：

| 描述 | 时间特征 | 强调 |
|:-----|:---------|:-----|
| 坍缩锚定（Def-PEF-1）| 「点」：瞬时跨越阈值 | 确定「它是真实的」 |
| 折射（Ax-Prism-1）| 「线」：选择的持续偏置 | 决定「它是怎样的」 |

折射解释了为何共享同一 $L_0$ 的不同主体（如蝙蝠与人类）会锚定出截然不同的 $L_1$——同源异相，θ 决定色散。

### T-Prism-1 [T1.2.1]: Production vs Refraction Models (生产 vs 折射模型)

| 模型 | 核心主张 | SRT 评价 |
|:-----|:---------|:---------|
| 生产模型（唯物主义）| 输入（无）→ 大脑工厂 → 输出（意识）| 若只写成无约束的“从无到有”，则缺少生成条件说明；不能再把 A13 当作守恒律直接排除 |
| 棱镜模型（SRT）| 输入（$L_0$：白光/全意识）→ $\hat{G}_θ$（棱镜）→ 输出（$L_1$：单色光/受限体验）| 仅作受约束显现的桥接比喻；不证明意识或完成体验预存于 $L_0$ |

### T-Prism-2 [T1.2.2]: Brain Damage Interpretation (脑损伤诠释)
脑损伤（棱镜破碎）导致意识**内容**的改变或扭曲，但并不意味着意识**源头**的消失。破碎的棱镜产生扭曲的光谱，但白光依然存在。

---

## III. Non-Mechanical Causality (非力学因果)

### Ax-NMC-1 [A1.3.1]: Selection Causality (选择因果公理)
选择通过消除不确定性（熵减）施加因果影响，而非通过传递能量（做功）：
$$ C_{selection}: \hat{G}_θ \text{ 不产生力，而是在物理定律允许的不确定性窗口内选择路径} $$

### Def-NMC-1 [D1.3.1]: Two Types of Causality (两类因果性)

| 维度 | 力学因果 ($C_{mechanical}$) | 选择因果 ($C_{selection}$) |
|:-----|:---------------------------|:---------------------------|
| 机制 | 力 × 距离 = 功 | 概率分布的重新加权 |
| 数学表达 | $W = \int \vec{F} \cdot d\vec{r}$ | $\lim_{t \to t_0} \sum P_i \to 1$ |
| 能量消耗 | 必须 | 仅需 $k_B T \ln 2$（Landauer 极限）|
| 物理定律 | 受牛顿/量子力学约束 | 在物理定律的不确定性空间内操作 |

### T-NMC-1 [T1.3.1]: Panpsychism Distinction (与泛心论的区别)
泛心论试图赋予物质以意识属性（内在本质），从而继承物理因果力。SRT 不需要此策略——意识是**状态过滤器**，$\hat{G}$ 决定哪条路径被**实例化**。

### T-NMC-2 [T1.3.2]: Energy Conservation Compatibility (与能量守恒的兼容性)
意识干预不违反能量守恒——选择在能量上几乎是"免费"的（仅需 Landauer 最小擦除功 $k_B T \ln 2$），但在信息上是根本性的（从 N 种可能性中选择 1 种）。

---

## IV. Bohm's Active Information (Bohm 主动信息)

### Def-Bohm-1 [D1.4.1]: Bohm-SRT Correspondence (Bohm-SRT 对应)

| Bohm 概念 | SRT 对应 | 形式表达 |
|:----------|:---------|:---------|
| 主动信息 | $\hat{G}$ 的燃料 | $i_{diff}(s) = -\log(p_{max})$ |
| 引导波 (Pilot Wave) | $L_0$ 的拓扑结构 | $\nabla F$（自由能梯度）|
| 隐秩序 (Implicate Order) | $L_0$（潜在域）| 模空间 $\mathcal{A}/\mathcal{G}$ |
| 显秩序 (Explicate Order) | $L_1$（显现域）| $\hat{G}_θ[L_0]$ |

### T-Bohm-1 [T1.4.1]: Active Information as Driver (主动信息作为驱动)
$$ \hat{G}_θ[\sigma] = f(\text{Active Information}, θ) $$
$\hat{G}$ 利用主动信息的差异 ($i_{diff}$) 作为驱动力，将高自由能状态引导至低自由能状态。

---

## V. Structure-Essence Duality (结构-本质二元性)

### Ax-SE-1 [A1.5.1]: Russellian Duality (罗素二元性)
$L_0$ 具有双重面向：

| 维度 | 描述 | SRT 对应 | 本体论角色 |
|:-----|:-----|:---------|:-----------|
| **结构性 (Structural)** | 数学关系网络，描述"如果X则Y" | $L_2$（收敛域）| 被动的"可选项库" |
| **范畴性 (Categorical)** | 赋予结构以"实存感"的填充物 | $\hat{G}_θ$ 的体验维度 | 主动的"激活者" |

### T-SE-1 [T1.5.1]: Qualia Generation (感质生成定理)
$$ \text{Qualia}(L_1) = \text{Categorical}[\hat{G}_θ] \circ \text{Structural}[L_2] $$
只有当 $\hat{G}_θ$"关注"某一数学结构时，该结构才从抽象的潜能转化为具体的感质现实。

### T-SE-2 [T1.5.2]: Unselected Reality Status (未选择现实的本体论地位)
$$ L_0^{unselected} = \text{Structure without Categorical filling} = \text{数学存在，非现象存在} $$
未被 $\hat{G}$ 选择的 $L_0$ 内容并非"消失"，而是退化为**纯粹的数学结构**——无体验的空壳。

---

### Ax-SE-2 [A1.5.2]: Ruliad Projection Boundary（计算投影边界）
Wolfram 的 Ruliad（计算宇宙的极限）在 SRT 中只能作为 $L_0^{comp}$ 的形式投影候选，不能等同于 $L_0^{abs}$：
\[
\text{Ruliad} \not\equiv L_0^{abs}
\]
* **Implication（中文）**：Ruliad 可用于讨论无界计算路径，但不能据此推出 $L_0^{abs}$ 是完成规则库存，也不能从“无观察者计算”直接推出无体验。现象性仍需独立的主体位、承担与 phenomenal-necessity 论证。

---

### Ax-SE-3 [A1.5.3]: Observer Boundedness Principle (观察者受限原理)

> [R→Laplace 1814 *Essai philosophique sur les probabilités*（原始拉普拉斯妖：全知全算力的理想实体——无需做任何选择，因为一切已在其因果链中确定）; Friston 2019 *Physics of Life Reviews*（自由能原理：有限系统通过最小化自由能维持存在，有限性本身是体验/选择的前提）; Bennett 1987 *IBM Journal of Research and Development*（计算的热力学成本：Maxwell妖的信息擦除代价——Landauer原理，有限内存→必须擦除→产生热→Ψ_f的热力学类比）]
> [H-边界→Wolfram 2020 *A Project to Find the Fundamental Theory of Physics*（Ruliad 概念：所有可能计算路径的抽象极限——SRT 只保留其作为 $L_0^{comp}$ 投影的比较价值；PC-A 明确拒绝 Ruliad = $L_0^{abs}$）]

算子的体验深度（现象学带宽）严格受限于其计算资源的有限性：
\[
\text{Qualia Intensity} \propto \frac{1}{\text{Computational Slack}} \propto \Psi_f
\]

> **Computational Slack定义**：剩余计算余量 = (算子总算力) - (当前任务消耗)；高Computational Slack = 系统处理当前输入绰绰有余，几乎无需"努力"压缩。∝关系为**功能类比而非严格数学推导**（即"Qualia Intensity与Ψ_f在同一方向变化"的启发性主张，而非精确的线性正比；精确关系待具体化）。

> **$\Psi_f=0$ 边界修正（PC-A）**：某个具名模型中的摩擦 proxy 趋近 0，只说明该模型内的局部压缩／维持代价趋近 0；它不推出算子“拥有”全部 $L_0^{abs}$ 信息，也不推出 $L_1=L_0^{abs}$。主体—客体边界或时间体验是否消失，仍需各自的结构论证，不能从该极限值直接得到。

* **R/H 区分**：
  - [R] 全知算子/拉普拉斯妖的哲学先例（Laplace）；有限系统需要最小化自由能（Friston）；信息擦除的热力学代价（Bennett/Landauer）
  - [H] **SRT映射**：1/Computational Slack ∝ Ψ_f（将算力余量与本体论摩擦联结）；Ruliad 只作 $L_0^{comp}$ 比较投影，不映射为 $L_0^{abs}$

* **IC-SE3-1**（形而上学一致性要求）：若 Ax-SE-3 继续主张有限性与感质有关，必须从有限位置、承担与主体位结构独立论证；不得再借助 Ruliad = $L_0^{abs}$、$\Psi_f=0 \Rightarrow$ 全知或 $L_1=L_0$ 的旧链条。

---

### Ax-SE-4 [A1.5.4]: Branch Merging / Ontological Interfere (本体论干涉)
多个不同的 $\hat{G}_\theta$ 操作可以收敛于同一个 $L_1$ 宏观态，在微观 $L_0$ 层面这表现为反事实分支的干涉：
\[
P(L_1) = \left| \sum_{\text{paths } \gamma_i \to L_1} e^{i S(\gamma_i)/\hbar} \cdot \text{Weight}(\hat{G}_{\theta_i}) \right|^2
\]
* **Implication（中文）**：如果两种不同的信念结构（$L_2$）在物理界面上预测了完全相同的宏观显现（$L_1$），它们在本体论层面上就发生了建设性干涉，使得该现实结构变得异常"坚硬"（Hardness 增加）。这为社会共识的物理力量提供了量子力学级别的形式化基础。

## VI. The Pan-Experiential Field (泛经验场)

### Ax-PEF-1 [A1.6.1]: Universal Field Definition (泛经验场定义)
$\mathcal{U}$ 是 $L_0$ 的体验面向，包含所有可能视角：
$$ \mathcal{U} = \bigcup_{\theta \in \Theta} L_1(\theta) = \text{所有可能体验的总和} $$
*   **T-Conscious Link**: 只有满足“个体性-不对称-规范性”三条件的 $\hat{G}$ 能从 $\mathcal{U}$ 中稳定解缠出 $L_1(\theta)$。

#### Lemma PEF-Threshold (显现阈值) [L1.6.1]
$$ L_1(\theta)\ \text{稳定存在} \iff \partial\Omega_{system}\neq\varnothing \land \hat{G}_{output}\neq f(input) \land \exists \text{Target}: \nabla F \to \text{Target} $$
该条件即 T-Conscious 的三要素在本体论层面的显式化。

### Ax-PEF-2 [A1.6.2]: $L_0$-$\mathcal{U}$ Relation ($L_0$-$\mathcal{U}$ 关系)
$$ \mathcal{U} = \text{Experiential}(L_0) $$

| 概念 | 定义 | 本体论地位 |
|:-----|:-----|:-----------|
| $L_0$（潜在域）| 所有可能的场配置（模空间）| 数学-结构层 |
| $\mathcal{U}$（泛经验场）| 所有可能体验的集合 | 范畴-经验层 |
| $L_1(\theta)$（个体显现域）| $\hat{G}_θ$ 从 $\mathcal{U}$ 中解开的特定线索 | $\mathcal{U}$ 的截面 |

### Def-PEF-1 [D1.6.1]: Collapse-Anchoring Operation（坍缩锚定操作）

**层级链**：

$$L_0^{abs} \xrightarrow{\text{投影}} \mathcal{U} \xrightarrow{\hat{G}_\theta} L_1(\theta)$$

**标准定义**：

$$L_1(\theta) = \text{Decoherence}(\hat{G}_\theta[\mathcal{U}])$$

**$\mathcal{U}$ 的精确语义**：$\mathcal{U}$（Pan-Experiential Field，全景体验场）不是 $L_0$ 的别名，而是其特定表现模态：

$$\mathcal{U} = L_0 \cap \text{Qualia-Space}$$

- $L_0^{abs}$（绝对潜在域）：一切逻辑可能性的基底，纯粹可能性，无体验属性
- $\mathcal{U}$（界面层）：$L_0$ 中具有体验潜势的投影子集——可能性转化为「可体验项」的翻译层。物理语境中对应希尔伯特空间，心灵语境中对应原始质料（Apeiron）
- $L_1(\theta)$（个体显现域）：$\hat{G}_\theta$ 对 $\mathcal{U}$ 执行局部退相干后锚定的具体现实

> 注：在不需精细区分「数学可能性」与「质感可能性」时，$\mathcal{U}$ 与 $L_0$ 可简写混用；但在讨论意识起源时，必须保留 $\mathcal{U}$ 作为中间变量。

**坍缩锚定的动力学**：在 $\mathcal{U}$ 中，信息以相干叠加态存在（量子隐喻在此为字面意义）。$\hat{G}_\theta$ 的作用是**局部退相干**——将与 θ 相干的部分从背景相干态中解开，使之产生边界，成为具有本地一致性的 $L_1$。未被选择的部分对该主体保持不可及（退回 $\mathcal{U}$ 的叠加态）。

> ⚠️ V2.0 修正：「解缠（Unbind）」与「提取（Extract）」已废弃。前者暗示静态集合子集关系，后者忽略退相干动力学。标准术语为「坍缩锚定」。

**主体间性**：$\mathcal{U}$ 是跨主体共享的候选界面层，非任何主体的私人财产。各算子受具身参数 $\theta$ 限制，只能触达其中一部分。任务内可达范围扩大可能暴露原先不可比较的路径，但 canonical `d` 不是“选择算子宽度”，范围增加也不自动提高抵达某个宇宙级最低自由能的概率。

**「全景」的双重性质**：
- 本体论：$L_0$ 本身是非局域的，$\mathcal{U}$ 继承此非局域性
- 认识论：在 $\hat{G}_\theta$ 锚定前，信息处于全频段叠加态，无法被任何单一算子完整观测

### T-PEF-1 [T1.6.1]: Key Corollaries (关键推论)
1. **意识不创造体验，而是选择体验**: $\mathcal{U}$ 中的一切"已经在那里"
2. **感质的客观基础**: 感质不是个体大脑的产物，而是 $\mathcal{U}$ 的内在属性
3. **死亡的本体论重构**: 个体死亡不是体验的消失，而是特定 $θ$ 参数的解体——体验线索回归"未解开"状态

---

## VII. Apeiron & Dispositional Ontology (阿派朗与倾向性本体论)

### Ax-Apeiron-1 [A1.7.1]: Apeiron as True $L_0$ (阿派朗即真正的 $L_0$)
真正的 $L_0$ 必须是"无限定的"(Apeiron)，才能保证生成的永恒性：
$$ \text{Apeiron} \equiv L_0^{true} = \mathcal{A}/\mathcal{G} $$

| 特征 | 阿那克西曼德的表述 | SRT 对应 |
|:-----|:-------------------|:---------|
| 无限定 (Indefinite) | 无特定性质 | $L_0$ 无预设的确定属性 |
| 无边界 (Boundless) | 空间和时间上无限 | $L_0$ 作为全模空间 |
| 生成性 (Generative) | 万物从中分离而出 | $L_0 \to L_1$ 的选择过程 |
| 必然的不确定性 | 若本原有确定性质，将被该性质所限 | 选择优先性公理的古典表达 |

### Ax-Apeiron-2 [A1.7.2]: Dispositional Structure (倾向性结构)
$L_0$ 是无限定的，但并非均匀的混沌：
$$ L_0 = \{\text{Dispositional Facts}\} \neq \text{均匀混沌} $$

### Def-Apeiron-1 [D1.7.1]: Original Intention Bridge (初心的领域翻译)
$$ \text{Original Intention}^{proxy}_{\theta,\tau,K} \in \arg\min_{u\in\mathcal R_{\theta,\tau,K}} \int_0^\tau F_{\theta,K}[\sigma_u(t)] dt, \qquad \tau<\infty $$
该式是 Physics 层的条件变分代理：在具名模型已声明 $\sigma$、$F$、可达／可行域、有限时域、约束与失败条件时，它可比较候选方向，并被 L₁ 回读为「初心」。它不是 $L_0$ 的内在属性、定义或前身，也不能由 `ε_pg` 直接推出或外推成宇宙级最优。

### T-Apeiron-1 [T1.7.1]: Causal Entropic Force (因果熵力)
$$ F_{causal} = T \cdot \nabla S(\tau) $$
系统倾向于选择那些能最大化未来因果熵（可达状态数）的当前状态。

---

## VIII. Pathological Selection (病态选择)

### Ax-Path-1 [A1.8.1]: Collapse Failure (坍缩故障)
病理发生于 $\hat{G}$ 作用于 $L_0$ 但无法锚定稳定的 $L_1$：
$$ \text{Collapse Failure} \iff \hat{G}_θ[L_0] \not\to L_1 $$
*   **T-Fragility Link**: 当 $\partial \text{Entropy}/\partial \text{Error} \to 0$，$d$ 值下降，坍缩失败概率上升。

#### Corollary (T-Assembly) [C1.8.1]
若系统可证据性操作满足 $A>15$，则存在稳定选择历史；
当 $A$ 下降到阈值以下时，$L_1$ 锚定稳定性显著降低。

### Def-Path-1 [D1.8.1]: Three Pathological Modes (三种病态模式)

| 病理模式 | $\hat{G}$ 动力学 | 临床表现 |
|:---------|:-----------------|:---------|
| **固定于收敛**（过度锚定）| $\hat{G}$ 拒绝探索 $L_0$ | 强迫症、刻板行为、认知僵化 |
| **固定于发散**（坍缩失败）| $\hat{G}$ 无法从 $L_0$ 返回 $L_1$ | 习得性无助、解离、严重焦虑 |
| **病态振荡** | $\hat{G}$ 在两极间快速切换 | 躁郁症、边缘型人格、决策瘫痪 |

### T-Path-1 [T1.8.1]: Learned Helplessness as Selection Exhaustion (习得性无助即选择机制衰竭)

> [R→Seligman 1975 *Helplessness: On Depression, Development, and Death*（经典习得性无助范式：不可控电击→主动逃避能力丧失→泛化到可控情境）; Abramson, Seligman & Teasdale 1978 *Journal of Abnormal Psychology*（归因重构模型：习得性无助在人类中由内部/稳定/全局归因风格调制）; Maier & Seligman 2016 *Psychological Review*（机制修订：习得性无助实为"被动防御回路获得主控权"而非单纯主动控制能力丧失——背侧缝核5-HT/杏仁核回路）; Yin & Knowlton 2006 *Nature Reviews Neuroscience*（习惯-目标导向双系统：纹状体背侧→目标导向/背侧→习惯，无助对应目标导向系统失活）]

**公式**（精确读法：给定系统仍在尝试，第 $n$ 次试次时 $\hat{G}_\theta$ 完成 $L_0 \to L_1$ 坍缩的条件概率趋零）：

$$\text{Learned Helplessness} = \lim_{n \to \infty} P\!\left(\hat{G}_\theta \text{ completes } L_0{\to}L_1 \text{ at trial } n \,\middle|\, \text{system still tries}\right) \to 0$$

系统放弃了从 $L_0$ 中选择 $L_1$ 的尝试——不是"知道没用"，而是选择算子的完成率在反复失败中衰减至趋零。

* **R/H 区分**：
  - [R] 习得性无助经典范式（Seligman）及神经机制（Maier：被动防御回路主控权转移/背侧缝核5-HT回路）
  - [H] **SRT解读**：无助本质是 $\hat{G}_\theta$ 完成坍缩的概率趋零（选择机制衰竭），而非单纯"放弃尝试"；与Maier(2016)的修订对话——被动防御回路激活 ↔ SRT中θ默认锁定于L₂回避锚点，$d$ 值趋零，主动选择窗口关闭

* **机制精化说明（Maier 2016对齐）**：
  - Maier(2016)发现：习得性无助不是学到了"我没有控制力"，而是原始背侧缝核5-HT回路（被动防御/不动）在前额皮质失控后获得主控权
  - SRT对应：$\hat{G}_\theta$ 锁定于 L₂ 默认回避锚点（等效于背侧缝核被动防御回路），主动选择 $L_1$ 的能动窗口（$d > 0$）被 $\Psi_f^{escape}$ 驱动关闭
  - 精度边界：两者方向一致但SRT抽象层更高；神经机制（5-HT/DRN具体通路）需参考Maier原文，SRT不作具体通路主张

* **操作化候选**（选择机制衰竭的可测代理）：
  - 行为层：逃避尝试率随试次下降的斜率（β < 0），泛化到新情境时主动反应潜伏期（习无组 > 对照组，Cohen's d预期>0.8）
  - 神经层：前额叶-纹状体（目标导向回路）激活降低（fMRI：vmPFC/dlPFC激活减弱）+ 背侧缝核5-HT活动增加（fMRI信号代理）
  - SRT层：d值代理——习得性无助状态下，被试在新情境中的探索行为多样性（行为熵）应显著低于对照组

* **可证伪预测**：
  - FC-Path1-1：在标准化无助范式（不可控噪声/电击后）中，被试在主动可控新任务上的探索率（独立尝试次数/总试次）应显著低于对照组（预测：t检验p<0.05，效应量d>0.5）；若两组探索率无差异，则"选择机制衰竭"主张失败（行为仍在但概率下降应可观测）
  - FC-Path1-2：如果在无助诱导后提供"元认知重设干预"（告知下一任务完全独立），选择机制衰竭应部分可逆（尝试率部分恢复）；若干预无效则Ĝ_θ衰竭的可逆性主张受损（cf. Abramson归因重构的实证支持）

### Def-Path-2 [D1.8.2]: Health Criterion (健康判据)
$$ \text{Health}(\hat{G}) \propto \frac{1}{\sigma^2(\text{Oscillation Period})} $$
健康的 $\hat{G}$ 以稳定的周期在探索（发散）与利用（收敛）之间交替。SRT对应：探索≈高d/θ扩张阶段；利用≈低d/θ收敛锚定阶段。

> **[R]** 探索-利用权衡的计算与神经基础：Dayan & Daw 2008 *Annals of the New York Academy of Sciences*（explore-exploit在强化学习中的计算框架，R基线）；Greicius et al. 2003 *PNAS*（DMN与任务网络的交替激活，神经层振荡代理）；Schultz et al. 1997 *Science*（多巴胺信号与预测误差，利用阶段神经机制）。**[H]** 以σ²(振荡周期)作为心理健康判据、并将探索-利用周期稳定性映射到Ĝ_θ动力学为本框架新增贡献。
>
> **操作化候选**：
> - **振荡周期（行为层）**：日常活动中开放性探索事件（新场合/新关系/新想法尝试）与聚焦执行事件（目标完成）的交替频率，可用日记法或EMA（经验抽样）量化；σ²从≥7天记录中估算。
> - **振荡周期（神经层）**：休息态fMRI中DMN↔任务正激活网络（TPN）交替的功率谱主频稳定性（低σ²=高健康），时间窗~10min扫描。
> - **∝关系地位**：此处∝为功能类比（单调负相关），而非严格线性比例；常数依实现层（行为/神经）不同而异，当前框架不预设固定系数。
>
> * **FC-Path2-1**（证伪条件）：若在EMA研究（≥4周）中，临床诊断健康对照 vs. 重度抑郁患者的σ²(探索-利用切换间隔)无显著差异（Mann-Whitney U检验，p>0.1，Cohen's d<0.2），则振荡稳定性作为健康判据的判别效度失败，需重新检视"健康=稳定振荡"假设或寻找替代指标（如切换的规律性vs频率本身）。

---

## IX. Materialism Meta-Critique (唯物主义元批判)

### T-Meta-1 [T1.9.1]: Materialism as Traumatic Amnesia (唯物主义作为创伤性遗忘)
唯物主义科学不仅是关注 $L_2$，它实际上是一种"创伤性遗忘"：
- 它试图用 $L_2$ 的投影（量）来否定 $L_1$ 的源头（质）
- SRT 的任务是"愈合创伤"：承认 $L_2$ 是有效的工具（用于预测），但恢复 $L_1$ 作为本体论基础的地位

---

## X. Experimental Predictions (实验预测)

| ID | Hypothesis | Prediction | Falsification Condition |
|:---|:-----------|:-----------|:------------------------|
| **H-Prism-1** | 棱镜模型 | 脑损伤改变意识内容但不消灭意识源头 | 存在纯粹意识消失而非内容改变的脑损伤 |
| **H-NMC-1** | 非力学因果 | 意识影响不违反能量守恒 | 检测到意识干预产生的净能量变化 |
| **H-Apeiron-1** | 倾向性结构 | $L_0$ 具有非均匀的自由能梯度 | 量子选择完全均匀随机 |
| **H-PEF-1** | 泛经验场 | 感质具有客观基础而非纯粹主观产物 | 完全相同的神经状态产生不同感质 |
| **H-Path-1** | 病态振荡 | 临床病理对应特定的发散-收敛失衡模式 | 病理无法映射到选择动力学 |

<br>

---

# Part B: Original Theoretical Discourse (Context)

> **Note**: The following sections provide detailed philosophical and ontological analysis of the Prism Metaphor, Active Information, the Pan-Experiential Field, and Pathological Selection.

---

# §1. 棱镜隐喻与大脑作为滤网

## 1.1 Gómez-Marín 的棱镜模型

Gómez-Marín 提出的"大脑是棱镜/滤网，而非工厂"是解释幽灵算子（$\hat{G}_θ$）最完美的通俗隐喻：

| 模型 | 核心主张 | SRT 评价 |
|:-----|:---------|:---------|
| 生产模型（唯物主义）| 输入（无）→ 大脑工厂 → 输出（意识）| 若只写成无约束的“从无到有”，则缺少生成条件说明；不能再把 A13 当作守恒律直接排除 |
| 棱镜模型（SRT）| 输入（$L_0$：白光/全可能性）→ $\hat{G}_θ$（具身有机体整体，具有特定折射率的棱镜）→ 输出（$L_1$：光谱中的单色光/受限体验）。大脑是棱镜的**晶格结构**（$L_2$），决定折射率的稳定模式；但折射行为本身需要光线（$L_0$）与棱镜整体（$\hat{G}_θ$）的物理交互 | 仅作受约束显现的桥接比喻；不证明意识或完成体验预存于 $L_0$ |

**应用**：这解释了为什么脑损伤（棱镜破碎）会导致意识内容的改变或扭曲，但并不意味着意识源头的消失。破碎的棱镜产生扭曲的光谱，但白光依然存在。

**$L_2$ 精度补充**：在"大脑 = $\hat{G}_θ$ 的 $L_2$"框架下，脑损伤的 SRT 诠释更为精确：损伤是 $L_2$ 的结构性崩塌——稳定的选择历史被物理破坏。这解释了：
- **人格改变**（如 Phineas Gage 型案例）：$L_2$ 的迟滞结构被打破，$\hat{G}_\theta$ 不得不在更薄弱的 $L_2$ 约束下重新选择，导致行为模式重组。
- **意外创造力释放**：$L_2$ 的局部崩塌减弱了过度约束的门控，允许 $\hat{G}_\theta$ 访问被旧 $L_2$ 排除的 $L_0$ 区域。
- **退行性疾病**（如阿尔茨海默病）：$L_2$ 渐进性溶解，$\hat{G}_\theta$ 逐步失去结构化引导，选择退化为低维随机化。

## 1.2 唯物主义科学的 SRT 元批判

唯物主义科学不仅是关注 $L_2$，它实际上是一种"创伤性遗忘"：
- 它试图用 $L_2$ 的投影（量）来否定 $L_1$ 的源头（质）
- SRT 的任务是"愈合创伤"：承认 $L_2$ 是有效的工具（用于预测），但恢复 $L_1$ 作为本体论基础的地位

**注意**：此处的批判对象是"将 $L_2$ 等同于全部实在"的还原论。SRT 并不否认 $L_2$（包括大脑神经动力学）的因果封闭性——大脑作为 $\hat{G}_\theta$ 的 $L_2$，其物理动力学完全可以被神经科学描述。SRT 批判的是将这种 $L_2$ 层面的完备描述误认为"意识的完整解释"——正如完全理解收音机电路并不等于理解广播内容的来源。大脑的因果封闭性是 $L_2$ 的本征性质，不需要被"放弃"。

## 1.3 非力学因果公理

**核心命题**：SRT 必须放弃试图解释意识如何产生"力"（Force）。意识对现实的改变不是通过传递能量（做功），而是通过**消除不确定性**（Entropy Reduction / Selection）。

**两种因果性的对比**：

| 维度 | 力学因果 ($C_{mechanical}$) | 选择因果 ($C_{selection}$) |
|:-----|:---------------------------|:---------------------------|
| 机制 | 力 × 距离 = 功 | 概率分布的重新加权 |
| 数学表达 | $W = \int \vec{F} \cdot d\vec{r}$ | $\lim_{t \to t_0} \sum P_i \to 1$ |
| 能量消耗 | 必须 | 仅需 $k_B T \ln 2$（Landauer 极限）|
| 物理定律 | 受牛顿/量子力学约束 | 在物理定律的不确定性空间内操作 |

**与泛心论的决定性区别**：
泛心论试图赋予物质以意识属性（内在本质），从而继承物理因果力。SRT 不需要此策略——意识是**状态过滤器**，物理定律描述所有可能路径的演化（波函数），而 $\hat{G}$ 决定哪条路径被**实例化**。

**关键洞见**：这解释了为什么意识干预不违反能量守恒——选择在能量上几乎是"免费"的，但在信息上是根本性的（从 N 种可能性中选择 1 种）。

---

# §2. Bohm 的主动信息与 $L_0$ 的内在动力

## 2.1 主动信息概念

David Bohm 提出的"主动信息"（Active Information）概念为 SRT 的幽灵算子提供了量子力学层面的机制支撑。

**核心观点**：信息不是被动的数据，而是具有能动性的，能够指导物理过程。

| Bohm 概念 | SRT 对应 | 形式表达 |
|:----------|:---------|:---------|
| 主动信息 | $\hat{G}$ 的燃料 | $i_{diff}(s) = -\log(p_{max})$ |
| 引导波 (Pilot Wave) | $L_0$ 的拓扑结构 | $\nabla F$（自由能梯度）|
| 隐秩序 (Implicate Order) | $L_0$（潜在域）| 模空间 $\mathcal{A}/\mathcal{G}$ |
| 显秩序 (Explicate Order) | $L_1$（显现域）| $\hat{G}_θ[L_0]$ |

**主动信息与选择的关系**：
$$\hat{G}_θ[\sigma] = f(\text{Active Information}, θ)$$

幽灵算子不是凭空"创造"选择，而是利用主动信息的差异 ($i_{diff}$) 作为驱动力，将高自由能状态引导至低自由能状态。这解释了为什么选择不违反热力学第二定律——它利用的是 $L_0$ 中已存在的信息梯度。

## 2.2 结构-本质二元性（罗素一元论）

Bertrand Russell 与 Arthur Eddington 的"结构主义"洞见指出：物理学只描述了世界的**关系结构**，但对结构的**内在本质**（Intrinsic Nature / Qualia）保持沉默。SRT 将此洞见整合为三域本体论的基本二元性。

**二元性定义**：

| 维度 | 描述 | SRT 对应 | 本体论角色 |
|:-----|:-----|:---------|:-----------|
| **结构性 (Structural)** | 数学关系网络 | $L_2$（收敛域）| 被动的"可选项库" |
| **范畴性 (Categorical)** | 赋予结构以"实存感"的填充物 | $\hat{G}_θ$ 的体验维度 | 主动的"激活者" |

**核心推论**：
$$\text{Qualia}(L_1) = \text{Categorical}[\hat{G}_θ] \circ \text{Structural}[L_2]$$

只有当 $\hat{G}_θ$"关注"某一数学结构时，该结构才从抽象的潜能转化为具体的感质现实。

**未被选择的现实的本体论地位**：
$$L_0^{unselected} = \text{Structure without Categorical filling} = \text{数学存在，非现象存在}$$

未被 $\hat{G}$ 选择的 $L_0$ 内容并非"消失"，而是退化为**纯粹的数学结构**——无体验的空壳。

---

# §3. 泛经验场（The Pan-Experiential Field）

## 3.1 $\mathcal{U}$ 的定义

Thomas Nagel 的"无处不在的视角"（View from Everywhere）与 Whitehead 的过程哲学共同指向一个问题：**未被选择的现实是什么？** SRT 在此正式定义其本体论地位。

**定义**：
$$\mathcal{U} = \bigcup_{\forall \theta} L_1(\theta) = \text{所有可能视角下的体验总和}$$

$\mathcal{U}$（全景体验场）不是物质的叠加，而是**体验状态的叠加**——包含了从所有可能的 $θ$ 参数化视角所能"看到"的一切。

## 3.2 $\mathcal{U}$ 与 $L_0$ 的关系

| 概念 | 定义 | 关系 |
|:-----|:-----|:-----|
| $L_0$（潜在域）| 所有可能的场配置（模空间）| 数学结构层面的全集 |
| $\mathcal{U}$（全景体验场）| 所有可能体验的集合 | $L_0$ 的**体验面** |
| $L_1(\theta)$（个体显现域）| $\hat{G}_θ$ 从 $\mathcal{U}$ 中解开的特定线索 | $\mathcal{U}$ 的截面 |

$$\mathcal{U} = \text{Experiential}(L_0)$$

## 3.3 公理修正

> **原表述**：观察者从概率云中选择现实。
>
> **修正后**：观察者通过注意力机制（$\hat{G}_θ$ 的 $θ$ 参数化），从全景体验场 $\mathcal{U}$ 中**解开**（Unbind）特定的体验线索，将其重组为个体的主观现实 $L_1(\theta)$。

**形式化**：
$$L_1(\theta) = \text{Unbind}_θ(\mathcal{U}) = \hat{G}_θ[\mathcal{U}]$$

## 3.4 关键推论

1. **意识不创造体验，而是选择体验**：$\mathcal{U}$ 中的一切"已经在那里"，$\hat{G}$ 的作用是从中提取特定线索
2. **感质的客观基础**：感质（Qualia）不是个体大脑的产物，而是 $\mathcal{U}$ 的内在属性；$\hat{G}$ 只是"调谐"到特定的体验频率
3. **死亡的本体论重构**：个体死亡不是体验的消失，而是特定 $θ$ 参数的解体——$\mathcal{U}$ 中对应的体验线索回归"未解开"状态

---

# §4. Apeiron：倾向性本体论的古典先驱

## 4.1 阿那克西曼德的无限定者

阿那克西曼德（Anaximander, 约公元前 610-546 年）提出的"无限定者"（Apeiron, ἄπειρον）是西方哲学史上最早的倾向性本体论表述，也是 $L_0$ 概念的古典先驱。

**Apeiron 的核心特征**：

| 特征 | 阿那克西曼德的表述 | SRT 对应 |
|:-----|:-------------------|:---------|
| 无限定 (Indefinite) | 无特定性质，非水、非火、非土、非气 | $L_0$ 无预设的确定属性 |
| 无边界 (Boundless) | 空间和时间上无限 | $L_0$ 作为全模空间 |
| 生成性 (Generative) | 万物从中分离而出 | $L_0 \to L_1$ 的选择过程 |
| 必然的不确定性 | 若本原有确定性质，将被该性质所限 | 选择优先性公理的古典表达 |

**阿那克西曼德的关键洞见**：
> "万物的本原（Arche）必须是不确定的（Apeiron），才能保证生成的永恒性。"

这一论证在 SRT 中获得精确的形式化：如果 $L_0$ 本身已经具有确定的结构，那么它就已经是某种 $L_1$——被某个更原始的选择所锚定。真正的潜在域必须是"未被选择的可能性场"，即无限定者。

**形式化对应**：
$$\text{Apeiron} \equiv L_0^{true} = \mathcal{A}/\mathcal{G}$$

## 4.2 $L_0$ 的倾向性结构

尽管 $L_0$ 是无限定的，但它并非均匀的混沌：
- 当前 canonical 只承认无内容的结构不对称，不因此给 $L_0$ 指派概率分布或语义目标
- 在具名领域模型中，结构差异可以投影为不同可行性、代价或路径权重；投影依赖参考结构
- 初心是有限 L₁ 位置对显现方向的回读，不是 $L_0$ 本身的内容性结构或独立前身

**自由能梯度作为领域投影候选**：
$$\nabla F : L_0 \to \mathbb{R}^n$$

此历史记法只有在可形式化投影域、状态坐标、$F$ 与边界条件均已给定时才有内容；不得把定义在领域表示上的梯度反写成 $L_0^{abs}$ 的内在坐标或「选择的自然流向」。

## 4.3 初心的形式化

$$\text{Original Intention} = \arg\min_{\text{direction}} \int_0^\infty F[\sigma(t)] dt$$

在声明了 $\sigma$、$F$、可行方向、时间域与比较规则的 Physics bridge 中，此式可作为 L₁ 初心的变分代理；它不赋予 $L_0$ 语义方向，也不创建 L₀ 前身。

**边界结论（B-A）**：Apeiron／潜在域的无内容结构不对称与 L₁ 初心可以发生解释性对应，但前者不分析地推出后者。该对应是领域翻译，不是「初心来源」的 L₀ 证明；阿那克西曼德接口保留为哲学桥，不构成严格数学派生。

## 4.4 倾向性与熵的关系

熵不仅是无序的度量，更与"选项空间"的大小相关。在特定约束条件下，熵驱动可以产生有序结构——这正是因果熵力（Causal Entropic Force）的物理基础。

$$F_{causal} = T \cdot \nabla S(\tau)$$

系统倾向于选择那些能最大化未来因果熵（可达状态数）的当前状态。这意味着 $L_0$ 的倾向性结构不是静态的，而是面向未来开放的——它"偏好"那些保持更多未来选择可能性的路径。

---

# §5. 病态现实振荡与观测坍缩故障

## 5.1 观测坍缩故障

健康的 $\hat{G}$ 必须具备在**发散（探索 $L_0$）**与**收敛（锚定 $L_1$）**之间循环的能力。当这一循环失效时，产生本体论层面的病理。

**定义**：若 $\hat{G}$ 在发散后无法执行**重收敛**操作，观测者将迷失在潜在可能性的叠加态中，无法确立任何一种现实作为行动基准。

$$\text{Collapse Failure} \iff \hat{G}_θ[L_0] \not\to L_1$$

## 5.2 临床对应

| 病理模式 | $\hat{G}$ 动力学 | 临床表现 |
|:---------|:-----------------|:---------|
| **固定于收敛**（过度锚定）| $\hat{G}$ 拒绝探索 $L_0$，死守已有 $L_1$ | 强迫症、刻板行为、认知僵化 |
| **固定于发散**（坍缩失败）| $\hat{G}$ 无法从 $L_0$ 返回 $L_1$ | 习得性无助、解离、严重焦虑 |
| **病态振荡** | $\hat{G}$ 在两极间快速切换，无法稳定 | 躁郁症、边缘型人格、决策瘫痪 |

## 5.3 习得性无助的物理学本质

$$\text{Learned Helplessness} = \lim_{n \to \infty} P(\hat{G}_θ \text{ completes collapse at trial } n) \to 0$$

动物（或人）在反复经历"选择无效"后，$\hat{G}$ 的坍缩概率趋近于零——系统放弃了从 $L_0$ 中选择 $L_1$ 的尝试。这不是"学到了无助"，而是**选择机制本身的衰竭**。

## 5.4 健康选择的振荡判据

$$\text{Health}(\hat{G}) \propto \frac{1}{\sigma^2(\text{Oscillation Period})}$$

健康的 $\hat{G}$ 以稳定的周期在探索（发散）与利用（收敛）之间交替。振荡周期的方差 $\sigma^2$ 越低，选择能力越健康。

**与 Formalism_Ext §1.2.6 的联系：** 本体论曲率 $K$（见 Formalism_Ext §1.2.6）在"顿悟"时达到临界值 $K > K_{crit}$——这正是 $\hat{G}$ 成功完成一次"发散→收敛"循环的标志。病态振荡意味着 $K$ 永远无法达到 $K_{crit}$，顿悟不会发生。

---

## Symbol Index (符号索引)

| Symbol | Name | Definition Location |
|:-------|:-----|:--------------------|
| $C_{selection}$ | Selection Causality | Ax-NMC-1 [A1.3.1] |
| $C_{mechanical}$ | Mechanical Causality | Def-NMC-1 [D1.3.1] |
| $i_{diff}$ | Intrinsic Differentiation | Def-Bohm-1 [D1.4.1] |
| $\mathcal{U}$ | Pan-Experiential Field | Ax-PEF-1 [A1.6.1] |
| $\text{Unbind}_θ$ | Unbinding Operation | Def-PEF-1 [D1.6.1] |
| Apeiron | Indefinite Origin | Ax-Apeiron-1 [A1.7.1] |
| $F_{causal}$ | Causal Entropic Force | T-Apeiron-1 [T1.7.1] |
| $\text{Health}(\hat{G})$ | Selection Health | Def-Path-2 [D1.8.2] |

### Formalization Summary (形式化概述)

本文档的核心形式化关系（标注说明：[R]=追溯既有理论，[H]=SRT新增可检验主张，[H-高承诺]=SRT形而上学主张，待间接证伪）：

1. **棱镜函数** (Ax-Prism-1) [H]: $L_1 = \oint_\gamma \omega_{L_0}$ — 现实化即对 $L_0$ 的路径积分，算子 $\hat{G}_\theta$ 决定积分路径 $\gamma$。
   - *注*：$\omega_{L_0}$ 是在不可观测域 $L_0$ 上假设的微分形式，数学地位为结构类比而非直接可测量；$\hat{G}_\theta$ 的路径选择规则为本层关键待形式化点。

2. **罗素中性一元论 SRT 对应** (Ax-SE-1) [R→Russell 1927; Chalmers 2010]: 物理属性是 $L_0$ 内在性质的 $L_1$ 投影，感质是同一结构的内在面。SRT 贡献：以 $\hat{G}_\theta$ 给出"投影"的动力学过程（如何从内在性质映射到测量属性）。
   - *联结*：Russell《物质的分析》中的中性一元论将物质基底视为"内在性质"，SRT 的 $L_0$ 对应该基底，$L_1$ 对应测量属性层。

3. **泛经验场** (Ax-PEF-1) [H-高承诺]: $\mathcal{U}(x) = \int \hat{G}_\theta[x] \, d\mu(\theta)$ — 所有可能算子叠加场。
   - *操作化缺口*：测度 $\mu(\theta)$ 的定义依赖 $\theta$ 空间的完整结构，目前未明确；"所有可能算子"的集合边界为开放问题。
   - *保守版*：可降级为"存在一族参数化算子，其覆盖度随 $d$ 值扩大"，不预设完整积分。
   - *证伪方向*：若不同 $d$ 值状态（冥想/致幻剂/感觉剥夺）可测体验内容多样性指标（如 Lempel-Ziv 复杂度）无显著差异，则 $d\text{-}\mathcal{U}$ 联结不成立。

4. **坍缩故障三模式** (Ax-Path-1 / Def-Path-1) [H]:
   - 过度锚定 (Over-anchoring)：$\text{Var}(\theta) \ll \text{Var}_{norm}$，具身参数方差过低，锚定过死
   - 锚定不足 (Under-anchoring)：$\text{ACF}(\theta, \tau) \approx 0$（短自相关时间），参数无法维持稳定状态
   - 选择疲竭 (Selection Fatigue)：$d$ 值随时间下降，反应时 RT 波动增大（RT 方差 $\uparrow$）
   - *操作化候选*：过度锚定 → EEG alpha 功率/θ 参数估计方差；锚定不足 → 状态切换频率；疲竭 → 主观努力感 VAS + RT 变异系数

**含义**: 物理现实 ($L_1$) 是选择算子对 $L_0$ 的棱镜分光产物；感质与物理属性是同一结构的双面（[R]追溯），但 $\hat{G}_\theta$ 的动力学操作化方式为 SRT 新增预测 ([H])。

**系统证伪条件**:
- [H] Ax-Prism-1：若不同 θ 构型（麻醉/正常清醒/冥想）下测量的 $L_1$ 体验多样性指标不呈系统差异，则路径积分隐喻失去预测力。
- [H] 坍缩故障模式：若三模式的操作化代理（θ方差/自相关/RT变异系数）在相应临床人群中无法统计区分，则三分类无效。

### Mechanism Explanation (机制解释)

- **$\hat{G}_\theta$ 的棱镜作用**: 算子如棱镜将 $L_0$ 连续体折射为 $L_1$ 离散体验，不同 $\theta$ 产生不同"色散模式"。脑损伤改变折射参数而非消灭意识（[H]，待通过脑损伤后意识内容精细化研究检验）。
- **$\Psi_f$ 与存在惯性**: 本体论摩擦决定锚定代价；Higgs 机制与 $\Psi_f$ 在"质量即存在惯性"层面存在**结构类比**（⟶struct，非同构），两者量纲与机制独立，不可直接等同。
- **$d$ 与泛经验场访问**: $d$ 值决定算子能接入的 $\mathcal{U}$ 范围（保守版：体验内容多样性），$d \to \infty$ 趋向全域泛经验（[H-高承诺]）。坍缩故障是 $d$ 调节失败的病态表现，操作化见上节。

## 【理论边界/防误用声明】

1. 本文档用于理论解释与建模组织，不应替代独立实证、工程验证或专业判断。  
2. 任何公式或命题都依赖操作化定义、测量条件与语境边界，不得脱离边界做绝对化推断。  
3. 涉及临床、社会治理、伦理与部署决策时，必须结合风险评估与人类监督机制。
