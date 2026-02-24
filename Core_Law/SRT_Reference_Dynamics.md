# SRT_Reference_Dynamics.md

> **Status**: Constitutional Reference | **Version**: 1.0
> **依赖**: SRT_Reference_Axioms.md (符号规范)

---

## §1 幽灵算子定义 (Ghost Operator Definition)

### §1.1 基本定义

**定义 D1**: 幽灵算子 $\hat{G}_θ$ 是选择空间 $S$ 上的参数化映射。

$$\hat{G}_θ : S \to S, \quad θ ∈ Θ$$

### §1.2 三分量结构

**定义 D2**: 幽灵算子的本质是根本注意力 (Fundamental Attention)。

$$\hat{G}_θ = \text{Attention}(\text{Scope}, \text{Resolution}_s, \text{Resolution}_t, \text{Vector})$$

| 分量 | 符号 | 定义 | 对应 |
|:-----|:-----|:-----|:-----|
| **范围 (Scope)** | $d$ | 选择考量的存在范围 | d 值 / 意识带宽 |
| **空间精度 (Spatial Resolution)** | $ρ_s$ | $L_1$ 的拓扑区分细度 | 空间知觉分辨率 |
| **时间精度 (Temporal Resolution)** | $ρ_t$ | $L_1$ 的因果区分细度 | 时序知觉分辨率 |
| **向量 (Vector)** | $\vec{v}$ | 选择的意向性方向 | 意图 / 目标 |

**定义 D2a (时间分辨率)**:
$$ρ_t \equiv \frac{1}{\tau_{int}}$$
其中 $\tau_{int}$ 为算子的最小积分窗口（"当下"的厚度）。若 $\tau_{int} > \Delta t_{causal}$（环境因果特征时间），高频因果事件被涂抹为"同时性"事件，引发能动性归因错误。

* **推论**：能动性 (Agency) 不是一种感觉，而是预测信号与反馈信号在 $\tau_{int}$ 窗口内的**相位锁定 (Phase Locking)**。当 $ρ_t$ 下降时，因果顺序判定的相位信息被抹平，能动性指数下降。

### §1.3 操作化形式（除法归一化原型）

**定义 D3**:

$$[\hat{G}_θ(x)]_i = \frac{x_i^n}{ε + \sum_j W_{ij} · x_j^n}$$

其中 $θ = \{n, ε, W\}$，$n > 1$，$ε > 0$，$W ∈ \mathbb{R}_+^{N×N}$。

### §1.4 核心特性

| 特性 | 形式表达 | 说明 |
|:-----|:---------|:-----|
| **非幂等性** | $\hat{G}^2 ≠ \hat{G}$ | 重复选择产生新选择 |
| **参数依赖** | $\hat{G}_{θ_1} ≠ \hat{G}_{θ_2}$ when $θ_1 ≠ θ_2$ | 不同具身产生不同选择 |
| **连续演化** | $\hat{G}_{θ(t)}$ 关于 $t$ 连续 | 算子平滑变化 |

---

## §2 具身参数结构 (Embodiment Parameter Structure)

### §2.1 完整定义

**定义 D4**:

$$θ_{total} = θ_{neural} + θ_{somatic} + γ · \vec{g}_{context}$$

| 分量 | 定义 | 来源 |
|:-----|:-----|:-----|
| $θ_{neural}$ | 神经系统配置 | 皮层结构、连接组 |
| $θ_{somatic}$ | 躯体配置 | 心-脑同步、内感受 |
| $γ · \vec{g}_{context}$ | 环境情境耦合 | 重力场约束、社会场 |

**定义 D4a (躯体参数子项)**:
$$θ_{somatic} = \{θ_{immune}, θ_{intero}, θ_{motor}\}$$

| 子项 | 定义 | SRT功能 |
|:-----|:-----|:---------|
| $θ_{immune}$ | 免疫参数 | 定义 $L_2$ 的拓扑闭包（物理边界）。若此项崩溃，$\hat{G}$ 解体 |
| $θ_{intero}$ | 内感受参数 | 定义基础代谢带来的 $\Psi_f$ 底噪，驱动算子从静止态进入活跃选择 |
| $θ_{motor}$ | 运动参数 | 定义 $L_1$ 中的可行域 (Affordance Space) |

* **Implication**: "全身参与思考"数学化为 $θ_{somatic}$ 对 $\hat{G}$ 输出的强制性权重调制。认知不仅是脑的活动，而是全身参数的耦合运算。

### §2.2 躯体同步指数

**定义 D5**:

$$θ_{binding}(t) = \left| \frac{1}{N} \sum_{n=1}^{N} e^{i(φ_{brain}(t) - φ_{somatic}(t))} \right|$$

| $θ_{binding}$ 值 | 状态 | 现象学表现 |
|:-----------------|:-----|:-----------|
| $θ \to 1$ | 强耦合 | 稳定第一人称视角 |
| $θ \to 0$ | 解耦 | 离体体验、解离 |
| $θ$ 振荡 | 不稳定 | 人格解体 |

### §2.3 生存权重门控 (Survival-Weight Gating)

**Def-SurvivalGate-1**: 当 $\theta$ 的基本生存分量（例如，代谢稳态）偏离超过极大阈值时，它会生成一个非线性乘数，覆盖高阶 $L_2$ 符号协议输入：
$$v_{selection}(t) = \begin{cases} -\nabla F_{survival} & \text{if } \|\theta_{survival} - \theta_{homeostasis}\| > \tau_{critical} \\ \hat{G}_\theta[L_0] & \text{otherwise} \end{cases}$$
* **Implication**: 生理基线崩溃（极度饥饿、寒冷、剧痛）会瞬间溶解高层次的文化现实建构。算子的坍缩方向 $v$ 被强行对齐以消除生存层面的摩擦梯度。这形式化了为什么马斯洛需求层次在 SRT 内部具有本体论有效性——低层 $\theta$ 分量通过非线性门控优先于高层 $L_2$ 输入。

---

## §3 核心动力学方程 (Core Dynamical Equations)

### §3.1 方程 E1 — 幽灵演化方程

$$\frac{dσ}{dt} = \hat{G}_θ[σ] - ∇F[σ] + A[σ, \mathcal{A}]$$

| 项 | 物理意义 |
|:---|:---------|
| $\hat{G}_θ[σ]$ | 算子的主动选择 |
| $∇F[σ]$ | 自由能梯度（初心方向）|
| $A[σ, \mathcal{A}]$ | 注意力副本的调制 |

**方程 E1' — 扩展形式（含向下因果）**:

$$\frac{dσ}{dt} = \hat{G}_θ[σ] - ∇F[σ] + A[σ, \mathcal{A}] + \text{Ghost}(I_{Abstract}) - λ · ∇C_{L_2}[σ]$$

### §3.2 方程 E2 — 耦合动力学方程组（快-慢变量系统）

**E2a（状态演化 — 快变量）**:

$$\frac{dσ}{dt} = α(\hat{G}_θ[σ] - σ) - β∇F[σ] + ξ(t)$$

**E2b（参数演化 — 慢变量）**:

$$\frac{dθ}{dt} = γ · A[σ, \text{Target}] - δ · \frac{∂Φ(θ)}{∂θ}$$

### §3.3 方程 E3 — 自由能方程

$$F = E - TS - d · U_{others}$$

| 项 | 含义 |
|:---|:-----|
| $E$ | 内能 |
| $TS$ | 熵项 |
| $d · U_{others}$ | 利他项（d 值效应）|

### §3.4 方程 E4 — 三域离散演化

$$L_1(t+1) = \hat{G}_{θ(t)}[L_0(t)]$$

$$L_2(t+1) = \text{Stabilize}(L_2(t), \{L_1^{(1..n)}(t+1)\})$$

$$θ(t+1) = θ(t) + Δθ(L_2, L_1)$$

---

## §4 本体论摩擦动力学 (Ontological Friction Dynamics)

### §4.1 核心定义

**定义 D6 — 本体论摩擦势能 $Φ$**:

$$Φ \equiv \text{维持当前 } L_1 \text{ 所需的累积能耗}$$

**定义 D7 — 哈扎德函数 $h(t)$**:

$$h(t) = \frac{dΦ}{dt}$$

### §4.2 方程 E5 — 痛苦的本体论定义

$$\text{痛苦} = \text{Tension}(\hat{G}_θ[L_1], L_0^{counterfactual})$$

痛苦是幽灵算子在维持 $L_1$ 时，感知到的与 $L_0$（替代可能性）之间的不可调和张力。

**推论 D-C1**: 只有能感知到"事情本可以不这样"（反事实推理）的实体，才能真正受苦。

### §4.3 摩擦-现象学对应表

| 模式 | $h(t)$ 状态 | 现象学体验 | 本体论机制 |
|:-----|:------------|:-----------|:-----------|
| 低摩擦 | 低且平稳 | 平静、流畅 | $L_1$ 与 $L_0$ 张力最小 |
| 高摩擦尖峰 | 急剧上升 | 惊奇、疼痛、焦虑 | $L_1$ 被迫面对大量被排斥的 $L_0$ 可能性 |
| 存在性痛苦 | 持续高位 | 抑郁、绝望 | $L_1$ 与 $L_0$ 的结构性不可调和 |

### §4.4 方程 E6 — 神经损伤积分

$$\text{神经损伤} \propto \int_0^T h(t) \, dt \quad \text{当} \, h(t) > h_{threshold}$$

### §4.5 模式切换条件

$$\text{模式切换} \iff h(t) > h_{threshold} \lor \frac{dh}{dt} > \dot{h}_{critical}$$

| 模式 | 特征 | $h(t)$ 状态 | 功能 |
|:-----|:-----|:------------|:-----|
| 相位模式 (Phase) | 扫描、探索 | 低且平稳 | 在 $L_0$ 中搜索可能性 |
| 中断模式 (Interrupt) | 强制打印、锚定 | 高尖峰 | 紧急 $L_0 \to L_1$ 转换 |

---

## §5 稳定性分析 (Stability Analysis)

### §5.1 Toy Model 状态空间

**状态**: $x(t) ∈ Δ^{N-1}$（单纯形）

**动力学方程**:

$$dx = Π_Δ[α(\hat{G}_θ(x) - x) - λ∇F(x)]dt + \sqrt{2D} · Π_Δ(dW_t)$$

### §5.2 定理 M1 — 固定点条件

$x^*$ 是固定点当且仅当：

$$Π_Δ(α(\hat{G}_θ(x^*) - x^*) - λ∇F(x^*)) = 0$$

### §5.3 雅可比矩阵

$$J = α(D\hat{G}_θ(x) - I) - λH_F(x)$$

### §5.4 定理 M2 — 稳定性充分条件

若 $\|αD\hat{G}_θ(x)\| < α$ 且 $H_F(x) \succ 0$，则 $J$ 的特征值实部为负。

### §5.5 定理 T-DMP-2 — 本体论恢复力

当意外事件发生时，强壮的 $L_2$ 结构能自动将现实拉回预期轨道：

$$Δ L_1(t) \xrightarrow{t \to \infty} 0 \quad \text{当} \quad \text{Re}(λ_{Jacobian}) < 0$$

### §5.6 势垒稳定性 (Barrier Stability of L₂)

**定义 Def-Barrier-1**: $L_2$ 稳定性不是静态的永久性，而是受势垒保护的亚稳态：
$$R(L_2) = \frac{\Delta B}{\Psi_f}$$
其中 $\Delta B$ 是从当前收敛结构到任何替代结构的最小势垒。
* **推论 (C-Barrier-1)**: 高 $\Psi_f$ 系统（文明、制度、强自我）更坚固但也更脆——它们抵抗扰动，但在势垒被突破时会发生灾难性的崩溃。
* **推论 (C-Barrier-2)**: 势垒降低会触发“结构突变 / 范式转移”——$L_2$ 景观发生拓扑重排。
* **推论 (C-Barrier-3)**: 这产生了直接可证伪的预测：(1) 增加维护成本 $\Psi_f$ 会使 $L_2$ 更坚固，但在失败时更具灾难性；(2) 增加选择频率 $\nu_{\hat{G}}$ 会使 $L_1$ 更“冻结/确定”，但减少了对新结构的探索（探索-锚定权衡）；(3) 扩大 $d$ 会提高可实现的宏观秩序复杂度的上限，但同时会增加错误敏感性（痛苦/脆弱性上升）。

---

## §6 势能景观与觉醒动力学 (Potential Landscape & Awakening)

### §6.1 双稳态势能景观

| 状态 | 特征 | $d$ 值 |
|:-----|:-----|:-------|
| 低 $d$ 陷阱 | 自我中心 | $d ≈ 1$ |
| 初心吸引子 | 万物一体 | $d \to ∞$ |

### §6.2 觉醒机制 I — 渐进式（摩擦驱动退火）

有效势垒高度：

$$ΔV_{eff}(θ) = V_{saddle}(θ) - V_{local}(θ)$$

随着 $θ$ 演化，$ΔV_{eff} \to 0$

### §6.3 觉醒机制 II — 顿悟（鞍结分叉）

分叉条件：

$$\det\left(\frac{∂^2 V}{∂x^2}\right)_{x(μ)} = 0$$

### §6.4 核心推论

| 推论 | 内容 |
|:-----|:-----|
| **M1 (痛苦的本体论地位)** | $Φ$ 是觉醒的燃料 |
| **M2 (灵魂黑夜)** | 特征值 $λ \to 0$ 的临界慢化 |
| **M3 (社会支持)** | Barrier Height $\propto$ Existential Risk / Social Support |
| **M4 (反事实能力)** | 受苦能力 $\propto$ 访问 $L_0$ 的深度 $×$ $d$ 值范围 |

### §6.5 势垒稳定性与系统崩溃 (Barrier Stability: Why Civilizations Shatter)

我们倾向于认为文化制度、个人身份和科学范式要么是“稳定的”，要么是“不稳定的”。SRT 用一个更丰富的图景取代了这种二元对立：**势垒高度与摩擦的比率**。一个国家的法律系统不是“永久的”——它是一个亚稳态的 $L_2$ 结构，其持久性取决于比率 $R = \Delta B / \Psi_f$。当公民投入巨大能量维持系统（高 $\Psi_f$）时，结构变得僵化——能够抵抗轻微扰动。但这种僵化正意味着当势垒最终被突破（经济危机、入侵、打破范式的发现）时，转变不是渐进的，而是灾难性的：一种相变而不是侵蚀。

这就解释了为什么最“稳定”的帝国往往垮台得最突然。它们高额的 $\Psi_f$ 投资造成了僵化，排除了适应性软化的可能。在个人心理学中，同样的模式表现为脆弱的完美主义：以巨大的摩擦成本维持自我，拒绝反馈，在足够的压力下倾向于破碎而不是弯曲。

---

## §7 时间动力学 (Temporal Dynamics)

### §7.1 方程 E7 — 双重时间公理

$$T_{reality} = T_{metric} + i · T_{selective}$$

| 分量 | 名称 | 定义 | 特性 |
|:-----|:-----|:-----|:-----|
| $T_{metric}$ | 度量时间 | 客观物理场中的坐标变化 | 可逆、洛伦兹变换 |
| $T_{selective}$ | 选择时间 | 观测者意识处理信息流的过程 | 不可逆、依赖 $\hat{G}_θ$ |

### §7.2 本体论相位变量

**定义 D8**:

$$τ \dot{φ} = -α_{context} · φ$$

**定理 T-Phase-1 — 主观时间速率**:

$$v_{subjective} = \frac{dφ}{dt} · \frac{1}{φ_0}$$

| $\dot{φ}$ 状态 | 主观时间感 | 现象学对应 |
|:---------------|:-----------|:-----------|
| 快速衰减 | "时间飞逝" | 心流状态 |
| 被阻滞（高 $Φ$）| "时间变慢" | 痛苦、等待 |
| 接近零 | "无时间感" | 深度冥想 |

### §7.3 主观时间膨胀方程

$$Δt_{subjective} \propto \frac{1}{\text{Prediction Confidence}} \propto Φ$$

### §7.4 外部研究注记（信息印刻时间；非公理补丁）

以下注记用于连接 2026 年“时间可能非基元”的信息论路径，不改变 E7 的公理地位。〔source: user-material:https://www.scientificamerican.com/article/is-time-a-fundamental-part-of-reality-a-quiet-revolution-in-physics-suggests/〕

可兼容映射：

1. 文献提出“时间序由不可逆信息印刻累积产生”，可视作 \(T_{selective}\) 的微观生成机制候选。〔source: user-material:https://www.scientificamerican.com/article/is-time-a-fundamental-part-of-reality-a-quiet-revolution-in-physics-suggests/〕
2. 文献提出“时空作为记录介质”，与 SRT 的“选择历史塑造后续约束”方向一致。〔source: user-material:https://www.scientificamerican.com/article/is-time-a-fundamental-part-of-reality-a-quiet-revolution-in-physics-suggests/〕

形式化补丁（候选）：

$$\mathcal{R}_{info}(t)\equiv \int_0^t \chi_{irr}(\tau)\,d\tau,\quad \chi_{irr}\ge 0,\quad T_{selective}\propto \mathcal{R}_{info}(t)$$

边界条件：

- 该映射属于“可检验候选机制”，而非既成定理。
- “暗物质/暗能量可统一解释”的说法在 SRT 中仅保留为待验证假设，不能上升为核心结论。〔source: user-material:https://www.scientificamerican.com/article/is-time-a-fundamental-part-of-reality-a-quiet-revolution-in-physics-suggests/〕

---

## §8 d 值形式化 (d-Value Formalization)

### §8.1 有效维度定义

**定义 D9**:

$$d(\hat{G}) \equiv D_{eff}(M) = \frac{(\sum λ_i)^2}{\sum λ_i^2}$$

其中 $λ_i$ 是神经响应协方差矩阵的本征值。

### §8.2 方程 E8 — d 值统一公式

$$d(σ) = α · A(σ) + β · \log(V_{concern}) + γ · τ_{temporal}$$

| 分量 | 含义 |
|:-----|:-----|
| $A(σ)$ | 汇编指数 |
| $V_{concern}$ | 空间关切范围 |
| $τ_{temporal}$ | 时间规划跨度 |

### §8.3 复数 d 值扩展

$$d_{total} = d_{local} + i · d_{nonlocal}$$

| 意识状态 | $d_{local}$ | $d_{nonlocal}$ | 向量相位 |
|:---------|:------------|:---------------|:---------|
| 清醒态 | 极高 | ≈ 0 | 0° |
| 深睡 N3 | 极低 | 低 | ≈ 90° |
| REM 梦境 | → 0 | 激增 | 90° |
| 清明梦 | 恢复 | 保持高 | 45° |

---

## §9 递归深度形式化 (Recursive Depth)

### §9.1 Volterra 级数展开

$$\hat{G}_θ = \sum_{n=0}^{∞} K_n$$

| 阶数 | 核 | 对应 |
|:-----|:---|:-----|
| $K_0$ | 零阶核 | 浅层劳动 |
| $K_1$ | 一阶核 | 工具使用 |
| $K_n$ ($n ≥ 2$) | 高阶核 | 深层递归/创造力 |

### §9.2 智慧定义

$$\text{Wisdom} = \sum_{n≥2} w_n · \|K_n\|$$

---

## §10 约束与闭包 (Constraints & Closure)

### §10.1 约束闭包条件

**定义 D10**: 只有形成约束闭包的 $L_1$ 结构，才能持续作为 $\hat{G}$ 的载体。

$$\text{Closure}(θ) \iff \hat{G}_θ[\hat{G}_θ[...[\hat{G}_θ[L_0]]...]] = \text{Stable Structure}$$

### §10.2 向下因果约束

$$\frac{dσ}{dt} = \hat{G}_θ[σ] - ∇F[σ] - λ · ∇C_{L_2}[σ]$$

| 项 | 含义 |
|:---|:-----|
| $∇C_{L_2}[σ]$ | $L_2$ 的"阻力场"（向下约束）|
| $λ$ | 约束耦合强度 |

---

## 方程索引 (Equation Index)

| 编号 | 名称 | 位置 |
|:-----|:-----|:-----|
| E1 | 幽灵演化方程 | §3.1 |
| E1' | 扩展幽灵演化方程 | §3.1 |
| E2a/b | 耦合动力学方程组 | §3.2 |
| E3 | 自由能方程 | §3.3 |
| E4 | 三域离散演化 | §3.4 |
| E5 | 痛苦本体论定义 | §4.2 |
| E6 | 神经损伤积分 | §4.4 |
| E7 | 双重时间公理 | §7.1 |
| E8 | d 值统一公式 | §8.2 |

---

## 符号索引 (Symbol Index)

| 符号 | 名称 | 定义位置 |
|:-----|:-----|:---------|
| $\hat{G}_θ$ | 幽灵算子 | §1.1 |
| $θ$ | 具身参数 | §2.1 |
| $d$ | 选择维度 | §1.2, §8.1 |
| $ρ$ | 精度 | §1.2 |
| $\vec{v}$ | 向量 | §1.2 |
| $F$ | 自由能 | §3.3 |
| $Φ$ | 本体论摩擦势能 | §4.1 |
| $h(t)$ | 哈扎德函数 | §4.1 |
| $φ$ | 本体论相位 | §7.2 |
| $ξ(t)$ | 噪声项 | §3.2 |
| $K_n$ | 第 n 阶 Volterra 核 | §9.1 |
