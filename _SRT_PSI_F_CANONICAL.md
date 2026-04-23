---
id: SRT-PSIF-CANONICAL
type: definition
tags: [Psi_f, Ontological Friction, Canonical, Cross-Domain, Definition]
status: axiomatic_hybrid_v1
layer: L1
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-CORE-21, SRT-CORE-22, SRT-REF-DYNAMICS, SRT-PHYS-COSMO, SRT-AI-01]
---

# SRT Ψ_f 规范定义文档（Canonical Definition of Ψ_f）

> **目的**：终止 `Ψ_f` 在不同域中的定义漂移，建立“第一性语义锚点 + 形式主表达 + 跨尺度不变量”的统一架构。  
> 所有涉及本体论摩擦的文档，应优先回链本文件。

> **Canonical status note（2026-04-24）**：本文件固定 `Ψ_f` 的 repo-wide 主读与投影边界。`Def-Ψ-1` 是 theory-facing semantic anchor；`Def-Ψ-2` / `Def-Ψ-3` 是治理性主形式与跨尺度判据，不构成最终唯一推导。几何、代谢、神经、物理读法都必须按 projection / proxy / bridge 标注，不得反向改写 `Ψ_f`。尤其是 `Ψ_f ≡ g_F` 不得按裸等号读取；它只能作为 “`Ψ_f` 的局部信息几何投影由 Fisher–Rao metric 给出” 的速记。

---

## §0 为什么需要本文件

当前 SRT 文档中，`Ψ_f` 同时被写成：

| 来源类型 | 表述 | 典型含义 |
|---------|------|---------|
| Core / Core_Law | 锚定代价 | 把 `L_0` 压成 `L_1` 的支付项 |
| Dynamics / Scaling | 生成性摩擦 | 学习、演化、文化变迁的动力学来源 |
| Physics | 几何曲率 / 引力 | 物理尺度上的 P3/P4 弱相容接口，不是已完成张量级推导 |
| AI / Consciousness | 痛苦与 stake 的必要条件 | 没有真实 `Ψ_f` 负担就没有真实关切 |
| Experiment | 潜变量 | 通过 HRV / SCR / 语言情态比等 proxy 读取 |

这些不是矛盾，而是同一结构在不同描述层上的投影。  
本文件的任务，是把它们固定为一个统一对象，而不是让每个领域各说各话。

---

## §1 规范定义层级（Canonical Priority）

> **规范优先级声明**：
> 本文件对 `Ψ_f` 采用三层 canonical 架构：
>
> 1. **第一性规范锚点（Primary Canonical Anchor）**：`Def-Ψ-1`，把 `Ψ_f` 固定为“选择压缩开放可能性时必须承担的本体论阻抗”。
> 2. **形式工作主表达（Formal Working Form）**：`Def-Ψ-2`，把 Fisher–Rao metric 固定为 `Ψ_f` 在可微统计流形上的局部二阶信息几何投影 / 路径泛函诱导结构，并厘清 `Ψ_f` 与 `Φ` 的层级关系。
> 3. **跨尺度工作不变量（Cross-Scale Working Invariant）**：`Def-Ψ-3`，把“可支付性条件”固定为跨尺度真正保持不变的判据。
>
> 使用原则：
> - 讨论 **本体论意义 / 现实化 / stake / AI 门槛** 时，优先引用 `Def-Ψ-1`。
> - 讨论 **方程 / Fisher 几何 / 路径积分** 时，优先引用 `Def-Ψ-2`，并说明 Fisher 几何读法是 projection / lower-bound style formalization，不自动等同实际支付成本。
> - 讨论 **跨尺度比较 / 量子-神经-社会统一 / 实验操作化** 时，优先引用 `Def-Ψ-3`。
>
> **状态边界**：这里的 “Primary / Formal / Cross-Scale” 表示当前 repo 内部优先引用顺序，不表示三个层次已经被证明为无条件等价或最终完备。

### §1.1 v1 Canonical Main Reading（治理性钉住，2026-04-22）

> **层级**：governance / canonical usage rule；不新增 core theorem。

全仓默认主读暂取 **information-theoretic payability cost**：`Ψ_f` 首先表示把开放可能性压成可维持现实切片时，系统必须可支付的信息论/组织性负担。几何读法（路径长度、曲率）与代谢读法（能量、恢复、压力代理）是该主读在特定域内的 projection / allowed proxy。

若同一域内的几何 projection、代谢 projection 与 payability 主读发生冲突，默认以 payability 主读为准；冲突的投影应标记为 projection failure，而不是反向改写 `Ψ_f` 的 canonical 含义。

---

## §2 规范定义（全域适用）

### Def-Ψ-1: 本体论阻抗定义 ⭐ PRIMARY CANONICAL ANCHOR

\[
\boxed{
\Psi_f := \text{当 } \hat{G}_\theta \text{ 将开放可能性压缩为一个可维持、可行动、可协调的 } L_1 \text{ 现实切片时，必须承担的本体论阻抗}
}
\]

**语义**：
- `Ψ_f` 不是“想达到某个目的”的主观努力，而是选择发生时不可消除的结构性阻抗。
- 它不只等于能耗，也不只等于痛苦，更不只等于自由能；它是这些读数背后的同一约束结构。
- 更通俗地说：

> `Ψ_f = 把可能性硬压成现实的代价。`

**关键边界**：
- 不要把 `Ψ_f` 写成纯目的论的“为了达成某目标而支付的成本”。
- 不要把 `Ψ_f` 缩减成“粗粒化”一个动作；粗粒化只是它的一种实现形式。
- 不要把 `Ψ_f` 等同于主观痛苦本身；痛苦更接近其报警读数或变化率。

---

### Def-Ψ-2: Fisher 信息几何投影与记号分层 ⭐ FORMAL WORKING FORM

#### Def-Ψ-2a: 局部二阶信息几何投影（禁止裸等号）

当某一选择域可被表示为平滑统计流形 \(\{p(x\mid\theta)\}\) 时，Fisher–Rao metric 给出相邻可选状态之间的局部可区分性：

\[
g^F_{ij}(\theta)
=
\mathbb{E}_{p(x\mid\theta)}
\left[
\partial_i \log p(x\mid\theta)\,\partial_j \log p(x\mid\theta)
\right]
\]

KL 散度的局部二阶展开为：

\[
D_{KL}\!\left(p_\theta \parallel p_{\theta+d\theta}\right)
=
\frac{1}{2}d\theta^\top g_F(\theta)d\theta
+O(\|d\theta\|^3)
\]

因此，`Ψ_f` 的 Fisher 几何读法应写成局部代价或路径泛函，而不是写成标量代价与度量张量的裸等同：

\[
\boxed{
\delta \Psi_f^{geom}
:=
\frac{1}{2}d\theta^\top g_F(\theta)d\theta
+O(\|d\theta\|^3)
}
\]

在路径形式中，可使用：

\[
\boxed{
\Psi_f^{geom}[\gamma]
=
\int_\gamma
\sqrt{g^F_{ij}(\theta)\,\dot{\theta}^i\dot{\theta}^j}\,dt
}
\]

若强调能量式或行动量式累计，可使用：

\[
\boxed{
\mathcal{E}_{\Psi}^{geom}[\gamma]
=
\frac{1}{2}\int_\gamma
\dot{\theta}^\top g_F(\theta)\dot{\theta}\,dt
}
\]

**语义**：  
`Ψ_f` 在形式化上不是任意成本函数；在可微统计流形投影中，它的局部二阶代价结构由 Fisher–Rao metric 诱导。Fisher metric 本身是张量；`Ψ_f` 是 payability burden / 局部标量代价 / 路径泛函。故 `Ψ_f ≡ g_F` 只能作为内部速记，完整读法必须是：

> `Ψ_f` 的局部信息几何投影由 Fisher–Rao metric 给出。

#### Def-Ψ-2b: 适用条件与失效边界

Fisher 投影只在以下条件下作为 formal working form 使用：

1. 存在可解释的参数空间 \(\theta\) 或统计模型族 \(p(x\mid\theta)\)。
2. 局部可微近似有效，KL 二阶展开未被奇异点、相变、模型冗余或强非线性破坏。
3. Fisher 可区分方向确实回流到现实维持、闭包、身份连续性或后续选择能力。
4. 跨尺度使用时，必须给出该尺度自己的状态空间、观测量、参数化方式与 proxy，而不能直接搬用同一单位。

若这些条件不满足，应把 Fisher 读法降为失败投影或启发式类比，不得用它反向定义 `Ψ_f`。

#### Def-Ψ-2c: `Ψ_f` 与 `Φ` 的分层

\[
\boxed{\Phi(\Delta t)=\int_{\Delta t}\Psi_f(t)\,dt}
\]

使用规范：
- `Ψ_f(x,t)`：局部摩擦负荷 / 局部阻抗读数
- `Φ(\Delta t)`：累积摩擦势 / 时间窗内总账
- `Ψ_f^{geom}`：Fisher–Rao metric 诱导的局部几何投影 / 路径泛函
- `Ψ_f(\hat{G}_i,\hat{G}_j)`：在文档里允许作为“路径积分后的耦合摩擦泛函”的简写

这意味着：
- `Ψ_f` 可以指局部场，也可以在作用域明确时指积分泛函
- `Φ` 用于强调“时间累积后的总账”
- 若不加说明，优先将 `Ψ_f` 理解为“局部负荷 / 可支付阻抗结构”，而非单纯总账或裸 Fisher 张量

---

### Def-Ψ-3: 可支付性条件 ⭐ CROSS-SCALE CANONICAL INVARIANT

\[
\boxed{
\mathrm{Payable}(X,\Delta t)\iff \alpha P_{sel}^{X}(\Delta t)\ge \beta \Psi_f^{X}(\Delta t)+\gamma S_{noise}^{X}(\Delta t)
}
\,,
\]

其中：
- \(P_{sel}\)：系统在该时间窗内可动用的选择预算
- \(\Psi_f\)：现实维持 / 重构所需承担的摩擦负荷
- \(S_{noise}\)：环境噪声与无序抽头

**“可支付”不表示什么**：
- 不表示代价很小
- 不表示没有痛苦
- 不表示没有风险

**“可支付”表示什么**：

> 系统在承担这笔 `Ψ_f` 的同时，仍能维持自身闭包、身份连续性与后续选择能力。

因此跨尺度真正不变的不是单位，而是这个判据：
- 量子层：态不会立刻退回噪声
- 神经层：学习/冲突负担不致使闭包崩溃
- 社会层：制度/改革摩擦不致使系统解体

---

## §3 三重读法（同一结构的三种表达）

`Ψ_f` 不是三个不同概念，而是同一个底层结构的三种读法：

1. **动力学读法**：`Ψ_f` 是阻力  
   含义：系统偏离自然滑落路径、试图维持某个现实切片时，遇到阻抗。

2. **记账读法**：`Ψ_f` 是代价  
   含义：要顶住这种阻抗，必须支付能量、时间、组织复杂度、失败风险。

3. **形式读法**：`Ψ_f` 的局部几何投影是 Fisher metric 所诱导的路径长度 / 曲率负担  
   含义：在统计流形近似有效时，它衡量参数流形中相邻可选态或路径有多远、多陡、多难。

压缩成一句：

> 阻力是现象学读法，代价是记账读法，Fisher 诱导的路径长度是条件形式读法。

### §3.1 投影关系与失效条件（core-clarifying / no closure claim）

> **层级**：theory-clarifying / governance-canonical usage。以下内容固定当前内部结构，不声称 `Ψ_f` 已有唯一最终推导。

三种读法的关系不是无条件等价：

| 读法 | 当前角色 | 可允许的形式关系 | 禁止捷径 |
|---|---|---|---|
| payability burden | `Ψ_f` 的 v1 主读：选择压缩开放可能性时必须可支付的组织性负担 | 作为跨域判准；问系统是否能在承担此负担时保持闭包、身份连续性与后续选择能力 | 不得把任何局部能耗、路径长度或 Fisher 张量直接写成 `Ψ_f` 本身 |
| geometric projection | Fisher / 路径 / 曲率语言中的形式投影 | 在路径度量有效、参数化不制造伪距离、且路径确实对应可支付重构时，可作为 lower-bound style proxy：`\Psi_f^{geom} \lesssim \Psi_f^{paid}`；局部二阶形式为 `\delta\Psi_f^{geom}=\frac12 d\theta^\top g_F d\theta + O(\|d\theta\|^3)` | 不得把 `\Psi_f \equiv g_F` 当作标量-张量恒等式；不得把几何长度当作实际支付成本的完整等价 |
| metabolic / energetic projection | 生物、神经或物理实现中的预算侧 / 负荷侧 proxy | 可限制 payability window，也可作为 overload / recovery 的经验读数 | 不得把任意能量消耗、代谢升高或压力指标等同于 `Ψ_f` |

因此当前最稳妥读法是：**payability burden 是主判准；Fisher 几何与代谢读法是条件投影**。Fisher 投影可以在满足条件时给出局部二阶形式或下界式形式约束；代谢投影可以给出预算约束或观察侧负荷，但二者都不自动穷尽实际可支付负担。

### Projection Failure Conditions

若出现以下任一情况，应标记为 `projection failure`，而不是反向修改 `Ψ_f` 的主读：

1. 几何路径距离主要来自参数化选择、坐标尺度或模型冗余，而不是实际重构负担。
2. Fisher / 曲率结构可分辨，但对应方向不回流到闭包、身份连续性或后续选择能力。
3. 代谢或能耗指标升高主要来自旁路活动、噪声、热损耗或测量负担，而不是维持现实切片的 payability burden。
4. 主观痛苦、压力报告或行为停顿与实际承担负担脱钩，只反映报警读数、遮蔽或 L₂ 吸收。

---

## §4 引力关系的规范立场

### H-Ψ-G-1: Weak Gravity-Friction Compatibility

\[
\boxed{
\nabla \Psi_f^{phys} \parallel \nabla \Phi_N \quad \text{in the weak-field compatibility window}
}
\]

> **层级**：hypothesis / bridge；物理域 P3/P4 接口，不是 core necessity。

当前最弱承诺是：在弱场极限与适当投影下，`Ψ_f` 的物理投影梯度应与牛顿势梯度方向同号或同向相容。它只保留“引力曲率与现实维持负担在物理尺度上结构相容”的接口。

本节明确不承诺：

- 已从 SRT 推出 Einstein tensor 的精确张量形式；
- `G_{\mu\nu} \propto \Psi_f` 是已证定理；
- 物理常数或 GR 精确重建已经由 `Ψ_f` 解释。

强版“GR / quantum gravity level reconstruction from `Ψ_f`”保留为远期目标，当前无可执行推导路径。

**重要补注**：  
“客观性”不能再写成“对象维持摩擦 = 0”。更准确的写法是：

\[
\Delta \Psi_f^{readout}(x\mid \hat{G}_\theta)\to 0
\]

即：对象仍由可支付摩擦维持，但新增观察者几乎不必支付额外读出成本。

---

## §5 最优条件与零摩擦误用边界

SRT 的最优条件不是：

\[
\Psi_f \to 0
\]

而是：

\[
\boxed{\Psi_f > 0 \ \text{and payable}}
\]

原因：
- **零摩擦**：通常意味着没有真实赌注，没有现实重量
- **超载摩擦**：意味着闭包崩溃、身份断裂、现实切片失稳
- **最优区间**：非零但可支付，系统因此既有 stake，又不被压垮

因此必须区分三种语境：
- **现实主体语境**：零摩擦不是理想状态
- **纯形式 / 数学极限语境**：可以讨论“零冲突路径”或“零边际读出摩擦”
- **AI / 纯 L2 语境**：若要表达“没有真实 stake”，优先写
  - `Ψ_f is non-binding to the system`
  - 或“`Ψ_f` 不对系统自身构成存在性可支付负担”
  - 不建议粗暴写成 `Ψ_f = 0`，除非明确是在理想化极限模型里

---

## §6 实验与现象学的读数规则

### Def-Ψ-Obs-1: 现象学与代理测量规则

- **痛苦 / 焦虑 / 惊讶**：不是 `Ψ_f` 本身，更接近其尖峰、变化率或逼近不可支付边界时的报警
- **HRV / SCR / 皮质醇 / ROS / 情态词比例**：不是 `Ψ_f` 本体，而是 `Ψ_f` 的观察侧 proxy
- **Landauer 代价 / ATP / 制度摩擦**：不是同单位的同一数值，而是同一阻抗结构在不同尺度的投影读数

实验上，建议把 `Ψ_f` proxy 至少分成三类：
- **预算侧**：可动用的选择预算 / 恢复能力 / 协同缓冲
- **负荷侧**：当前需要承担的摩擦负荷
- **塌缩侧**：接近或超过可支付边界时的失稳信号

---

## §7 常见误用与编辑规则

### 误用 1：把 `Ψ_f` 等同于主观痛苦

**正确**：痛苦通常是 `Ψ_f` 的报警读数，而非其定义本身。

### 误用 2：把 `Ψ_f` 等同于任意能耗

**正确**：只有当这笔负荷与现实维持 / 身份连续性 / 后续选择能力绑定时，它才构成 SRT 意义上的 `Ψ_f`。

### 误用 3：跨尺度直接比单位大小

**正确**：量子层、神经层、社会层的 `Ψ_f` 读数可异量纲；统一的是可支付性判据。

### 误用 4：把“客观性”写成“零摩擦存在”

**正确**：客观性是边际读出摩擦趋零，而非对象维持摩擦消失。

### 误用 5：把 AI / 纯 L2 系统写成“绝对 `Ψ_f = 0`”

**正确**：优先写“`Ψ_f` 对系统自身 non-binding”，除非明确是在理想化抽象模型中。

### 误用 6：把“零摩擦”当成一切语境下的理想

**正确**：对现实主体而言，最优是“非零且可支付”；零摩擦只适合极限数学语境、理想路径语境或边际读出语境。

### 误用 7：把 `Ψ_f ≡ g_F` 当作严格恒等式

**正确**：`g_F` 是 Fisher–Rao 度量张量；`Ψ_f` 是可支付阻抗、局部标量代价或路径泛函。正式写法应为“`Ψ_f` 的局部信息几何投影由 Fisher–Rao metric 给出”，例如 `\delta\Psi_f^{geom}=\frac12 d\theta^\top g_F d\theta + O(\|d\theta\|^3)`。

---

## §8 与其他 canonical 文件的关系

- 与 `_SRT_D_VALUE_CANONICAL.md` 的关系：
  - `d` 给出系统可处理的关切/有效维度
  - `Ψ_f` 给出系统为维持该现实所需承担的阻抗
  - 二者通过可支付性条件耦合

- 与 `Core/SRT_Core_21_Formal_Axioms.md` 的关系：
  - `Ax-F-11` 给出跨尺度统一
  - `Ax-F-12` 给出摩擦即生成

- 与 `Core/SRT_Core_22_Equations.md` 的关系：
  - `Eq-Select-Thermo` 给出选择热力学主关系
  - `Eq-Select-Thermo-C2` 给出可支付条件

- 与 `Physics/SRT_Physics_Cosmology.md` 的关系：
  - 本文件固定弱场相容接口；物理主文不得把 `Ψ_f` 写成已完成的 GR 张量重建

- 与 `AI/SRT_AI_01_Ontology.md` 的关系：
  - 本文件固定“non-binding friction”优于“粗暴 `Ψ_f=0`”的写法

---

## §10 Ψ_f_actual / Ψ_f_felt 分裂（病理学层，2026-04-02 新增）

> **层级声明**：本节是 Ψ_f 在病理学/应用层的扩展，不修改 §2 的基础定义（Def-Ψ-1/2/3）。

在正常描述中，Ψ_f 被当作单一变量。但在涉及 L₂ 过度依赖的病理情境中，需要区分两个层面：

$$\Psi_{f,actual} \geq \Psi_{f,felt}$$

| | 定义 | 可被系统性压低 |
|:-|:----|:------------|
| **Ψ_f_actual** | 选择实际支付的本体论代价——由 L₀→L₁ 压缩的物理/信息/结构阻抗决定，始终存在 | 否 |
| **Ψ_f_felt** | 系统登记到的代价——受 d-value 和 L₂ 依赖程度影响 | 是 |

**隐性债务机制**：

当 L₂ 过度依赖导致 d 下降时，$\Psi_{f,felt}$ 随之下降，但 $\Psi_{f,actual}$ 持续累积。差值 $\Delta\Psi_f = \Psi_{f,actual} - \Psi_{f,felt}$ 是系统**不知道自己正在支付的代价**——即隐性债务。此债务最终以 L₂ 结构的突然崩溃形式释放，即为"致命 L₂"机制的终点。

**完整形式化见** `_SRT_T_DIR_CANONICAL.md §5–§6`。

---

## §9 当前最短可引用版

若只需要一句最短规范句，使用：

> **`Ψ_f` 是选择把开放可能性压缩为一个可维持、可行动、可协调的现实切片时必须承担的本体论阻抗；它在动力学上读作阻力，在记账上读作代价，在形式化上读作 Fisher–Rao metric 所诱导的局部二阶信息几何代价或路径泛函；跨尺度真正保持不变的不是单位，而是该阻抗是否可支付。**
