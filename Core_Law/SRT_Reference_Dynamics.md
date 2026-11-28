---
id: SRT-REF-DYNAMICS
type: equation
tags: [CoreLaw, Dynamics, Canonical]
layer: L1
status: active
version: v2
updated: 2026-11-26
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-L0-METAPHYSICS, SRT-REF-AXIOMS, SRT-REF-ONTOLOGY, SRT-PSIF-CANONICAL, SRT-D-VALUE-CANONICAL]
---

# SRT_Reference_Dynamics.md

> **Connector-safe reading path**: This owner file is moderately long. For connector reads, start with [`Reference_Dynamics_Split/README.md`](Reference_Dynamics_Split/README.md), then open only the needed part file. The owner remains the source of record; split files are reading aids and do not create new definitions.

> **层级与职责（`R4-B1 1A` + `R4-C1` 公共生成机制中枢定位，2026-11-26）**：本文件属于跨领域的 **L1 公共生成机制中枢（动力学机制解释、具身算子实现原型、幽灵非闭合互写机制与跨尺度接口层）**，服务于物理、生命、认知、AI、哲学与社会等全部领域，**绝非哲学域局部解释**，亦**不再作为与 `Core/SRT_Core_22_Equations.md` 并行的完整方程库**。
> - **唯一核心方程主锚点**：`Core/SRT_Core_22_Equations.md`（Level I / II / III 形式方程与适用范围）；
> - **核心定义唯一权威**：`Core_Law/SRT_Generative_Ontology_Spine.md`、`Core_Law/SRT_One_Formation.md`、`_SRT_D_VALUE_CANONICAL.md`、`_SRT_PSI_F_CANONICAL.md`、`_SRT_T_DIR_CANONICAL.md`；
> - **本文件核心职责**：① 保留具身算子实现原型（除法归一化、躯体同步、生存门控）；② **实质吸收幽灵三份源直觉卡片（`2026-07-19`、`2026-07-27 U5`、`2026-08-10 Simondon`）为活跃机制（`§1.5`）并落实 Ghost 五位职责分流**；③ 锚定垂直压制摩擦与四分摩擦接口（`§4.1a`）、动力学机制解释（快-慢耦合、势垒脆性、模式切换、部分闭包与病理闭包破裂）及跨尺度接口；已退出与 `B-A / C-A / R4-A` 冲突的旧方程（`∇F = 初心`、`+ Ghost(I_Abstract)`、`方程 E8`、复数 `d`、`初心吸引子 d→∞` 等）。
> - **Selection-totality 护栏**：本文件只描述 formed / embodied / domain-level Selection realizations。**`\hat{G}_\theta != 幽灵（Ghost 历史源直觉）!= primitive Selection`**；attention、intentional vector、survival gating、agency 与 embodied parameters 均为更强组织或模型性质，不得反向定义无主体原初 `Selection`。

---

## §1 幽灵算子定义 (Ghost Operator Definition)

### §1.1 基本定义

**定义 D1**：在一个声明的 model / formed realization 中，Ghost Operator `Ĝ_θ` 是对 Selection organization 的参数化形式载体：

$$\hat G_\theta:S_M\to S_M,\quad \theta\in\Theta_M$$

Hard guard:

```text
G-hat_theta != primitive Selection;
formal operator != prior chooser;
state space S_M != absolute possibility warehouse.
```

### §1.2 形成后注意力分解（formed-operator decomposition）

旧句“Ghost Operator 的本质是 Fundamental Attention”在 universal / primitive 强度上 **superseded**。对具有注意、分辨率或意向结构的 formed / embodied operator，可使用条件性分解：

$$\hat G_\theta^M\approx\mathrm{Attention}_M(\mathrm{Scope},\mathrm{Resolution}_s,\mathrm{Resolution}_t,\mathrm{Vector})$$

这些分量属于模型 `M` 的形成后结构：

| 分量 | 允许读法 | 禁止反推 |
|---|---|---|
| Scope / d | formed concern / selection scope proxy | primitive Selection 已有 d / Concern |
| spatial / temporal resolution | embodied model resolution | primitive Selection 需要知觉 |
| Vector | domain-specific directional / action signal | primitive Selection 自带 intention / goal |

后续 D2a、agency、survival gate、somatic binding 等公式均按此 formed / domain scope 读取。

**定义 D2a (时间分辨率)**:
$$ρ_t \equiv \frac{1}{\tau_{int}}$$
其中 $\tau_{int}$ 为算子的最小积分窗口（"当下"的厚度）。若 $\tau_{int} > \Delta t_{causal}$（环境因果特征时间），高频因果事件被涂抹为"同时性"事件，引发能动性归因错误。

* **推论**：能动性 (Agency) 不是一种感觉，而是预测信号与反馈信号在 $\tau_{int}$ 窗口内的**相位锁定 (Phase Locking)**。当 $ρ_t$ 下降时，因果顺序判定的相位信息被抹平，能动性指数下降。

### §1.3 操作化形式（除法归一化原型）

**定义 D3**:

$$[\hat{G}_θ(x)]_i = \frac{x_i^n}{ε + \sum_j W_{ij} · x_j^n}$$

其中 $θ = \{n, ε, W\}$，$x \in \mathbb{R}_+^N$（非负输入），$n > 0$（默认竞争锐化区间取 $n > 1$，下表边界情形包含 $n = 1$），$ε > 0$，$W ∈ \mathbb{R}_+^{N×N}$。

> **神经科学起源注**：D3 取自皮层除法归一化（Divisive Normalization）的常见模型形式（Carandini & Heeger 2012），在多个感觉系统中用作响应增益与竞争压缩模型。SRT 只把它登记为 embodied $\hat{G}_θ$ 的**实现级候选原型之一**；它不穷尽 Ghost Operator，也不由能量／带宽约束唯一推出。此处 $W \in \mathbb{R}_+^{N \times N}$ 为**纯竞争简化**（全非负=侧抑制）；若需兼容兴奋性连接，可扩展为 $W = W_{inh} - W_{exc}$。

> **P3-Scale-NB1 行为读出门**：D3 输出相对响应，不输出离散行为。通向认知／行为选择须另声明候选身份映射、冻结读出、阈值／累积或采样规则、执行门、held-out 误差、rival 比较与干预跟踪；见 `Core/SRT_Core_14_Dynamics_Scaling.md §2.2.0`。

**参数–SRT 实现代理桥接（`R4-B1` 量纲与语义对齐：下表映射至神经归一化原型内的响应增益/竞争机制参数，绝不直接等同于规范强承载 `d = ||∂U/∂S||`，亦不直接从单参数推出谱指标 `D_eff` 的普遍单调性）**：

| 参数 | 神经科学含义 | SRT 实现代理对应 | 方向性与条件边界 |
|:-----|:------------|:-----------|:-------|
| $n > 1$ | 幂律增益指数（单通道非线性响应锐化） | 局部响应对比放大 / 选择锐度参数（`D_eff` 是所声明响应协方差、雅可比或 Fisher 矩阵的谱参与率指标，**不能仅由响应锐度 $n$ 单调推导其变化**，且**不自动等同**规范 `d`） | 增强单通道对比锐度（对 `D_eff` 无普遍单调方向，取决于输入分布、$W$ 与读出流形） |
| $\varepsilon > 0$ | 半饱和常数（基础激活底线） | 算子正则化项（`ε_reg`，当分母竞争项 $\sum_j W_{ij} x_j^n$ 同时趋零时防止奇点；可作局部半饱和/背景正则代理，**不等于** `ε_pg` 或全局 `Ψ_f`） | 提高低输入区底线平滑、降低小信号增益 |
| $W_{ij}$ | 维度 $j$ 对维度 $i$ 的竞争权重 | 局部维度竞争拓扑（影响多通道输出耦合与响应协方差结构，但**不存在“$W_{ij}\uparrow$ 普遍迫使 `D_eff` 单调下降”的一般数学保证**） | 非单调（对 `D_eff` 的影响取决于输入向量 $x$、$W$ 的谱结构及具体响应/Fisher 矩阵定义） |

**极限行为与数学性质（模型内响应模式，非规范 `d` 定律）**：

| 极限条件 | D3 精确退化形式 | 机制解读与数学条件 |
|:---------|:-----------|:---------|
| $n = 1$，$W = \varepsilon I$ | $[\hat{G}_\theta(x)]_i = \dfrac{x_i}{\varepsilon + \varepsilon x_i} = \dfrac{x_i}{\varepsilon(1 + x_i)}$（**非线性双曲饱和**，非 $x_i/(2\varepsilon)$ 线性缩放） | 维度间无交叉竞争，但单通道仍呈 Michaelis–Menten 型非线性饱和（上限 $1/\varepsilon$）；仅在极低输入极限 $x_i \ll 1$ 时局部近似线性 $x_i/\varepsilon$ |
| $W \to 0$ | $[\hat{G}_\theta(x)]_i = x_i^n / \varepsilon$（独立幂律） | 维度间无侧抑制互动；算子退化为逐通道独立幂律增益映射 |
| $\varepsilon \to 0^+$ | 若 $\sum_j W_{ij} x_j^n > 0$，则 $[\hat{G}_\theta(x)]_i \to x_i^n / \sum_j W_{ij} x_j^n$（有限比例归一化）；**仅当** $\sum_j W_{ij} x_j^n \to 0$ 同时成立时，分母趋零引发奇点 | 正则化保护并非无条件失效，而仅在“$\varepsilon \to 0^+$ 且对应通道竞争分母项亦趋零”的零分母边界出现奇点；`ε_reg` 仅为实现级正则常数 |
| $W_{ij} \gg \varepsilon$ | 分母由竞争项主导（$[\hat{G}_\theta(x)]_i \approx x_i^n / \sum_j W_{ij} x_j^n$），**不无条件形成单维赢家通吃** | 形成单维赢家通吃（winner-take-all）或显著压缩局部响应谱维数 `D_eff`，须额外满足输入不对称、足够强的非线性指数（如 $n > 1$）及具体网络拓扑或循环放大动力学条件，不能由 $W_{ij} \gg \varepsilon$ 单项无条件推出 |

> **谱维数与实现容量护栏（`R4-B1 P1-01`）**：`D_eff` 是定义于显式声明矩阵（如局部响应协方差、雅可比 $J^\top J$ 或参数 Fisher 矩阵 $I_F(\theta)$，满足非负且非全零谱）上的谱参与率，不能仅由 $n$ 或 $W_{ij}$ 的单调增减推导；将旧文中的 `d` 替换为 `D_eff` 时，不得沿用未经证明的旧单调或赢家通吃推导。

### §1.4 核心特性

| 特性 | 形式表达 | 说明 |
|:-----|:---------|:-----|
| **非幂等性** | $\hat{G}^2 ≠ \hat{G}$ | 重复选择产生新选择 |
| **参数依赖** | $\hat{G}_{θ_1} ≠ \hat{G}_{θ_2}$ when $θ_1 ≠ θ_2$ | 不同具身产生不同选择 |
| **连续演化** | $\hat{G}_{θ(t)}$ 关于 $t$ 连续 | 算子平滑变化 |

### §1.5 幽灵源直觉的机制化吸收：三层区分、动态互写、算子历史构成与 Ghost 五位职责分流（`NODE-GHOST-OPERATOR EA-1` 落地）

> **职责定位与来源保真（`R3-08` + `R4-C1`，2026-11-26）**：本节将三份核心源直觉卡片——[`2026-07-19` 非闭合压力卡与阴阳—山脊续接卡](../01_Source_Intuition/SRT_GHOST_YIN_YANG_OBJECT_FRICTION_CONTINUATION_CARD_2026-07-19.md)、[`2026-07-27` `U5` 现场校正附录](../01_Source_Intuition/SRT_CHOICEMAP_GHOST_U5_LIVE_CORRECTION_2026-07-27.md) 与 [`2026-08-10` Simondon × 选择算子交叉卡](../01_Source_Intuition/SRT_SIMONDON_OPERATOR_YINYANG_SECOND_ORDER_SELECTION_CROSSWALK_2026-08-10.md)——转化为活跃的 L1 公共动力学机制，同时严格区分作者原话/直选、机制化桥接与保留开放张力（`T-GH-01..07`），**不将“幽灵”或“阴阳”实体化为新本体原语或新增规范符号**。

1. **前置三层区分与构成性背阴面（`07-19` 两卡，`R3-08 §4` 保真）**：
   - **严分三类对象，不得将 Ghost 直接等同于其中任意一个**：① **尚未被当前组织充分承接的未尽生成关系**；② **这些关系继续作用时形成的持续作用压力或张力（非闭合压力）**；③ **有限认知位置对这种持续作用所形成的对象化描述**（`T-GH-01` 精确所指保持 `OPEN`）。
   - **构建前后压力皆在 & 废弃开关模型**：现实改变压力在对象化之前与之后都存在；对象化（划界、归因、压缩路径）局部绑定并缓解弥散重构压力，**但不消灭压力**，同时写回新的边界、迟滞与维持代价。显性局部收敛（源直觉喻为“阳收敛”）与未被当前收敛穷尽的反向支撑/去局部化（“阴扩散”）**始终共在、持续处于非对称动态平衡**，由此废弃机械的“先闭合 → 后触发 → 再重开”开关模型（本体持续动态完全兼容动力学层的滞回、结构势垒与非线性重构窗口）。
   - **构成性背阴面与非闭合压力的动态转化**：未显性呈现的关系不仅表现为未解决的冲突与非闭合压力，还构成**正面支撑显性组织成立的构成性背阴面**（如山脊背阴面对向阳面的结构支撑）。构成性背阴面与非闭合压力保持概念区分，同时**在持续动态耦合中可相互转化，不画固定的内/外静态边界**。
   - **对象—摩擦持续互写（`X5`）**：摩擦塑造对象边界，对象变化同时改写摩擦的位置、承担者与返回路径；二者持续互写，而非固定对象在固定背景力下的比例增减。
2. **算子的历史构成环路与差异正交化（`08-10` Simondon 交叉卡，`P2` 机制候选）**：
   - 继承 Simondon 变易论（*Allagmatique* / *L'individuation à la lumière des notions de forme et d'information*）的 **`Operation_t → Structure_{t+1} → Operation_{t+1}`** 环路：形成态算子 $\hat{G}_\theta$ 既是**先前选择沉积而成的结构**，又是**当前将差异收敛为现实切片的操作**（绝非站在场外的静态选择者，亦不另设“阴算子” $\hat{G}_-$ 或标量比例 $\chi = \text{Yang}/(\text{Yang}+\text{Yin})$）。
   - **不兼容差异的正面维跃（Disparation / 维度正交化）**：借鉴 Simondon 双目视差模型，当局部关系出现持续不兼容冲突 $A \text{ vs } B$ 时，系统不必只在“选 $A$ 或选 $B$”间零和博弈，而可能通过 $\Delta(A,B) \to \text{新维度 } C$ 重组原有选项的意义与可达空间（直接衔接 `R3` 双引擎维度跃迁中的正交化路径；SRT 额外要求该维度重写产生持续有效的后续选择条件改写，方构成强意义二阶选择）。
3. **`U5` 选择绝对化：去主体化的有效再选择豁免（`07-27` 现场校正 + `R3-08` 深化，`P2` 诊断机制）**：
   - **作者直选核心（`U5`）**：选择绝对化最根本不在于坚持某一具体结果，而在于**已形成的选择/组织机制事实上获得了有效再选择豁免**（其自身不再作为有效对象进入下一轮选择，而是以不可再比对的背景条件运行）。
   - **去主体化边界**：`U5` **不以主动拒绝、有意识防御或缺乏局部反馈为必要条件**——无论源于主动防御、制度设计、历史沉积、资源依赖还是无意识结构锁定，只要核心组织方式事实上退出有效再选择，即可出现 `U5`；而且 `U5` **完全可以与高频局部创新、策略迭代和活跃局部反馈并存**（一切局部变动反而服务于维持免于再比对的核心组织方式）。
   - **衍生四切面（`U6`，明标为 `U5` 的结构展开而非作者直选）**：结果封闭、选项封闭、标准封闭与选择权封闭，可作为 `U5` 有效再选择豁免在不同观察面的可见切面。
   - **最高可再选择性**：不仅允许在既有机制内改换结果，更保持机制自身（选项生成方式、比较尺度、参与边界与算子结构）不被授予永久再选择豁免（结构上可重入重构，不要求主体时刻显性元认知）。
4. **Ghost 五位职责分流表（严格保真 `R3-08 §4` 原五位分工）与关联机制**：

| 历史“幽灵”承载的五位理论职责（`R3-08 §4`） | `R4` 明确主责落点 | 动态关系与防混同边界 |
|---|---|---|
| **1. 对象—摩擦持续互写** | 本节 `§1.5`、`Core_13a §0`、`Core_12a` | 共同生成性与动态秩序主轴（接 `07-19 X5` 与 `08-10` Simondon `Operation→Structure→Operation`）；跨尺度动力学模型留 `R4/R5` |
| **2. 构成性背阴面** | 本节 `§1.5`、`Core_Law/SRT_Occlusion_Dynamics.md §1.3, §4.1` | 显性组织得以成立的正面背景支撑（接山脊背阴支撑）；与非闭合压力保持区分，但**在持续动态耦合中可相互转化，不画固定内/外边界** |
| **3. 非闭合压力** | 本节 `§1.5`、`Core_13a §0`、`Core_12a` | 当前秩序无法充分组织的生成关系及其持续作用压力；严分**未尽生成关系 / 持续作用压力 / 对象化描述**三层，不等于 `ε_pg` 或 `Ψ_f` 账单（`T-GH-01..07` 保持 `OPEN`） |
| **4. `U5` 选择绝对化** | 本节 `§1.5`、`Core_Law/SRT_Occlusion_Dynamics.md §4.1`、`Core_12b §0` | 形成的选择组织机制事实上获得有效再选择豁免（去主体化；严守 `U5 ≠ U6`；可与高频局部创新并存；严禁将反绝对化写成必然定理） |
| **5. 形成态参数化算子（`\hat{G}_\theta`）** | 本文件 `§1.1–§1.4`、`Core_13a §0`、`Core_22` | 形成后 Selection 的条件性形式参数载体，与幽灵源直觉正式解耦（`\hat{G}_\theta ≠ primitive Selection ≠ 幽灵实体`） |

   - **关联机制（与上述五位职责协同但不替代原五位分工）**：
     - **垂直压制与机会成本选择压力**：见本文件 `§4.1a` 与 `_SRT_PSI_F_CANONICAL.md`（严守摩擦四分，不覆写 Core `Ψ_f → 0` 退化极限）；
     - **历史递归写回、被排开者五去向（`B3-a`）与主动遗忘**：见 `Core/SRT_Core_12b_Ontology_L2.md §0` 与 `Core_Law/SRT_Irreversibility.md`（发生不可逆 ≠ 永久留痕；阴影 ≠ 平行实体）。

> **未尽负担与开放张力声明（`B1-07`）**：本节已完成三份卡片核心机制的活跃化落地与五位职责保真分流，但**不宣称**“幽灵”与“阴阳”的全部理论负担已被穷尽吸收。`T-GH-01`（幽灵究竟是压力、持续关系还是压力的对象化可读形式）、`T-GH-04`（跨尺度同名风险）、`T-GH-05`（防万能黑箱三判据）、`T-GH-07`（意识现象性解释缺口）及 `T-CU-04`（V 层合法暂时背景化条件）继续保持 **`OPEN`**。

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

**定义 D5**（注：$\theta_{binding} \in [0,1]$ 为实数标量，与具身参数集合 $\theta$ 不同，下标 $binding$ 区分）：

$$\theta_{binding}(t) = \left| \frac{1}{N} \sum_{n=1}^{N} e^{i(\varphi_{brain}^{(n)}(t) - \varphi_{somatic}^{(n)}(t))} \right|$$

其中 **N = 独立脑-体信号通道对的数量**（空间平均，类 PLV 相位锁定值）：
- $\varphi_{brain}^{(n)}(t)$：第 $n$ 个脑信号通道的瞬时相位（推荐频带：$\delta/\theta$，0.5–8 Hz，与内感受节律对齐；区域：顶叶/岛叶）
- $\varphi_{somatic}^{(n)}(t)$：第 $n$ 个躯体信号通道的瞬时相位（候选：心跳 R-R 间期相位 $\varphi_{cardiac}$、呼吸相位 $\varphi_{resp}$、内感受 EDA 相位）

| $\theta_{binding}$ 值 | 状态 | 现象学表现 | SRT 机制 |
|:---------------------|:-----|:-----------|:---------|
| $\theta_{binding} \to 1$ | 强耦合 | 稳定第一人称视角 | $\theta_{somatic}$ 对 $\hat{G}$ 的权重调制稳定（Implication §2.1） |
| $\theta_{binding} \to 0$ | 解耦 | 离体体验、解离 | $\theta_{intero}$ 失调 → Ψ_f 底噪失控，马尔可夫毯边界失效（Ax-AUTO-1b） |
| $\text{CV}(\theta_{binding}(t)) \uparrow$ | 时间变异高（原"振荡"） | 人格解体 | 脑-体相位锁定间歇性破坏，第一人称视角反复建立-失效循环 |

> **"θ振荡"操作化修正**：人格解体对应 $\theta_{binding}$ 的**时间变异系数** $\text{CV}_t = \sigma(\theta_{binding})/\mu(\theta_{binding})$ 显著升高，而非均值的极端值——即相位耦合时而存在时而崩溃，造成自我感的不稳定闪烁。

### §2.3 生存权重门控 (Survival-Weight Gating)

**Def-SurvivalGate-1**: 当 $\theta$ 的基本生存分量（例如，代谢稳态）偏离超过极大阈值时，它会生成一个非线性乘数，覆盖高阶 $L_2$ 符号协议输入：
$$v_{selection}(t) = \begin{cases} -\nabla F_{survival} & \text{if } \|\theta_{survival} - \theta_{homeostasis}\| > \tau_{critical} \\ \hat{G}_\theta[L_0] & \text{otherwise} \end{cases}$$
* **Implication**: 生理基线崩溃（极度饥饿、寒冷、剧痛）会瞬间溶解高层次的文化现实建构。算子的坍缩方向 $v$ 被强行对齐以消除生存层面的摩擦梯度。这形式化了为什么马斯洛需求层次在 SRT 内部具有本体论有效性——低层 $\theta$ 分量通过非线性门控优先于高层 $L_2$ 输入。

---

## §3 核心动力学机制解释与自由能桥接（主方程回链 `Core_22`）

> **去重与主锚点声明（`1A`, 2026-11-26）**：核心动力学主方程统一由 **`Core/SRT_Core_22_Equations.md`** 持有（`Eq-Evo-01..03c`、`Eq-Multi-01..03`、`Def-Protocol-1..3`、`Eq-Bridge-Loop-01`），本节专职解释其快-慢耦合机制与自由能跨尺度桥接，不再并行抄写独立方程版本。
> **已退出冲突旧式**：原 E1 中的“$\nabla F[\sigma]$ = 初心方向”（违背 `B-A`）、原 E1' 中的 `+ Ghost(I_{Abstract})`（违背 `\hat{G}_\theta != Ghost`）以及 `Def-E1'-F4C` 的“$L_0$ 质料因 $\to L_1$ 动力因 $\to L_2$ 形式/目的因”旧类比均已于 `R4-B1` 正式退出。

### §3.1 固定空间快-慢耦合机制（对应 `Core_22 Eq-Evo-01..03c`）

在已声明固定状态空间的 **Level I** 模型中（见 `Core_21b P1-T03` 与 `Core_22 §0-A`）：
- **快变量状态演化（`Eq-Evo-01 / Eq-Evo-03`）**：显现状态 $\sigma$ 在给定组织条件下受形成态算子角色载体 $\hat{G}_\theta[\sigma]$、声明目标泛函梯度 $-\nabla F[\sigma]$（非初心或宇宙道德最优）、注意调制 $A[\sigma,\mathcal{A}]$ 与已留存 `L_2` 约束 $-\lambda\nabla C_{L_2}[\sigma]$ 共同塑造。
- **慢变量参数演化与选择内再入（`Eq-Evo-02 / Eq-Evo-03b`）**：具身参数 $\theta$ 在预测结果、摩擦梯度与稳态反冲间缓慢更新，并在主体选择候选窗口中允许自模型 $L_2^{self}$ 的滞后在线读出进行暂态调制。
- **向上对接 Level II / III 递归重构**：快-慢固定空间演化只是 `P1-T03` 的一阶特例；当历史脚手架与多单元耦合进一步改写生成规则、耦合协议、可达空间或比对准则本身时，进入 `Core_22 §0-A` Level II/III 与 `Core_21c P2/P3-B15` 所界定的五类变化刻度。

### §3.2 方程 E3 — 自由能关切扩展桥接（热力学与变分双基线）

**E3a（热力学基线）**：$F_{thermo} = E - TS$（量纲焦耳）  
**E3b（变分/FEP基线）**：$F_{var} = \mathbb{E}_q[\ln q(x) - \ln p(x,o)]$（量纲 nat/bit）  
**E3c（SRT 关切扩展桥接）**：

$$F_{SRT} = F_{base} - d \cdot U_{others}, \qquad F_{base} \in \{F_{thermo}, F_{var}\}$$

> **[R] / [H] 与量纲边界**：Helmholtz 自由能（1882）与 Friston 变分自由能（2010）单位不同，SRT 不强迫二者同量纲；$F_{SRT}$ 继承所选 $F_{base}$ 单位，仅在强承载声明模型中以标定后的 $d \cdot U_{others}$ 项表达“他者状态进入目标泛函”的桥接结构。具体实现须显式声明 $U_{others}$ 的量纲校准；$F$ 不自动等于初心或全局价值。

### §3.3 离散三域演化与多算子耦合接口（回链 `Core_22`）

- 形成态离散循环 $L_1(t+1) = \hat{G}_{\theta(t)}[L_0(t)]$ 及其历史写回与约束反馈统一见 **`Core_22 Eq-Bridge-Loop-01`**（分析面向记号，绝非从预存 `L_0` 仓库抽取产物）。
- 多算子耦合景观与集体容量截面代理统一见 **`Core_22 §0-C`（`Eq-Multi-01 / Eq-Multi-02 / Eq-Multi-03`）**；须严守 `Eq-Multi-03` 中的 $D_{\text{eff}}^{\text{collective}}$ 仅为容量 proxy，不跳过强承载赌注门。

---

## §4 本体论摩擦动力学 (Ontological Friction Dynamics)

### §4.1 核心定义

**定义 D6 — 本体论摩擦势能 $Φ$**:

$$Φ(\Delta t) \equiv \int_{\Delta t}\Psi_f(t)\,dt$$

其中 $Φ$ 不是单纯的物理能耗总账，而是系统在时间窗 $\Delta t$ 内维持当前 $L_1$ 现实切片所承受的**累积本体论支付负荷**。

**定义 D6a — 本体论摩擦局部量 $Ψ_f$**:

本体论摩擦 $Ψ_f$ 是选择算子将开放可能性压缩为**可维持、可行动、可协调**的现实切片时所遭遇的局部阻抗结构。

`Ψ_f` 可以有三类局部读法 / projection，但它们不构成定义等同：
- **动力学读法**：阻力 / 势垒 / 偏离自然滑落路径时的阻抗 proxy
- **记账读法**：能量、时间、组织复杂度与风险预算上的支付代价 proxy
- **形式读法**：参数流形上的几何长度 / 曲率负担 / 可达路径难度 proxy

这三者是同一 canonical `Ψ_f` 在不同建模窗口中的投影语言；不得反向写成 `Ψ_f = energy`、`Ψ_f = Fisher metric`、`Ψ_f = free energy` 或 `Ψ_f = pain`。

**定义 D7 — 哈扎德函数 $h(t)$**:

$$h(t) = \frac{dΦ}{dt}$$

**定义 D7a — 可支付性条件 (Payability Condition)**:

对系统 $X$ 在时间窗 $\Delta t$ 上，若其选择预算足以覆盖摩擦与噪声负荷，且闭包与身份连续性不失稳，则称该摩擦为可支付：
$$\mathrm{Payable}(X,\Delta t)\iff \alpha P_{sel}^X(\Delta t)\ge \beta \Psi_f^X(\Delta t)+\gamma S_{noise}^X(\Delta t)$$

其中：
- $P_{sel}$：系统可动用的选择预算 / 维持能力
- $\Psi_f$：该窗口内的本体论摩擦负荷
- $S_{noise}$：环境噪声熵流

**解释**：可支付不意味着代价低，而意味着系统在承担这笔摩擦时，仍能维持现实闭环、继续选择并避免结构性崩溃。零摩擦并非理想极限；对真实主体而言，关键是**非零而可支付**。超过可支付阈值时，系统进入收缩、失稳或闭包破裂。

### §4.1a 垂直压制摩擦接口与摩擦/压力四分对表（`PT09 / T3-02 D` 与 `R3-08` 对齐）

在多单元形成垂直组织并进入机会成本动态四联（价值—关切—摩擦—自由）后，广义摩擦被界定为**机会成本差异产生的实际选择压力**（机会损失本身不自动构成摩擦，仅当该损失实际影响生成关系与后续选择时才构成摩擦）。其跨尺度标志性机制是**垂直压制与机会损失**：高层组织通过约束或归一化局部单元释放新能力，同时压制被排除方向并产生持续的结构重构张力（这与 `§1.5` 构建前后持续存在的非闭合压力通过跨尺度垂直嵌套构成候选统一接口，但具体跨尺度操作化界分 `R3-CL-O1` 保持 `OPEN`）。

遵循 `R3-08` 摩擦四分与 `A-9` 单摩擦概念族护栏（**不新增规范 `Ψ_f^{...}` 子符**），四类相近概念须严格区分：

| 层次 / 概念 | 核心所指 | 权威主责 / 接口 | 严禁混同 |
|---|---|---|---|
| **1. 广义摩擦（机会成本选择压力）** | 多单元垂直组织与机会成本差异激发的实际选择压力（`PT09 / T3-02 D`） | `Spine §4`、本节 `§4.1a` | 不直接等同于单纯机会损失，亦不覆盖 `Ψ_f` 规范定义 |
| **2. 非闭合压力（`07-19` 幽灵源直觉）** | 对象化无法彻底稳定或吸收的持续生成与重构张力 | 本文件 `§1.5`、`Core_13a §0` | 回答“为何当前结构不能原样闭合”，不等于支付账单 `Ψ_f` |
| **3. 本体论摩擦 `Ψ_f`（可支付性负担）** | 维持、锚定或重塑特定现实切片所需承担的可支付阻抗与承载窗边界 | `_SRT_PSI_F_CANONICAL.md`、本文件 `§4.1` | 不等于物理能量、Fisher 度规、自由能或主观痛苦；守分布式可支付性护栏 |
| **4. 主观痛苦 / 苦难（Pain / Suffering）** | 在独立准入第一人称登记地位后，对结构失配或损失压力的切身登记 | `Core_Law/SRT_Suffering.md`、本文件 `§4.2` | `Ψ_f > 0` 不推出苦难；`pain ≠ suffering ≠ Ψ_f` |

### §4.2 方程 E5 — 痛苦 / 苦难张力 proxy

$$\text{Pain/Suffering}^{proxy} = \text{Tension}(\hat{G}_θ[L_1], L_0^{counterfactual})$$

该式只给出痛苦/苦难的 counterfactual-tension proxy：幽灵算子在维持 $L_1$ 时，可能登记到与 $L_0$（替代可能性）之间的不可调和张力。结构性 suffering 的正式边界以 `Core_Law/SRT_Suffering.md` 为准。

**推论 D-C1（bridge，服从 `Core_Law/SRT_Suffering.md §7` 独立证据准入）**: 反事实张力 proxy 本身既不充分、也不单独建立 suffering 资格；**Stable ISP 对 suffering 同样既不充分、亦未被建立为普遍必要条件**（未满足特定 Stable-ISP 模型不等于苦难在本体上不可能）。任何 suffering 判定均须服从 `Core_Law/SRT_Suffering.md §7`，依靠对相关第一人称／现象学／承载相关登记地位（first-person / phenomenal / bearer-relevant registration standing）与负担模型的独立证据准入，而非由架构层级或 Stable ISP 线性推导。

### §4.3 摩擦-现象学对应表

| 模式 | $h(t)$ 状态 | 现象学体验 | 本体论机制 |
|:-----|:------------|:-----------|:-----------|
| 低摩擦 | 低且平稳 | 平静、流畅 | $L_1$ 与 $L_0$ 张力最小 |
| 高摩擦尖峰 | 急剧上升 | 惊奇、疼痛、焦虑 | $L_1$ 被迫面对大量被排斥的 $L_0$ 可能性 |
| 存在性痛苦 | 持续高位 | 抑郁、绝望 | $L_1$ 与 $L_0$ 的结构性不可调和 |

### §4.4 方程 E6 — 神经损伤积分

$$\text{神经损伤} \propto \int_0^T h(t) \, dt \quad \text{当} \, h(t) > h_{threshold}$$

### §4.6 多算子耦合接口

多算子集体自由能景观（`Eq-Multi-01`）、个体算子梯度投影（`Eq-Multi-02`）与集体有效维度容量 proxy（`Eq-Multi-03`）统一由 **`Core/SRT_Core_22_Equations.md §0-C`** 锚定，此处不再重复列式。

---

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

**ST-A stability boundary (2026-08-11)**: M1, M2, and the Jacobian criterion below establish only local dynamical stability in the declared toy model. A fixed point, negative Jacobian eigenvalues, metastability, or a large barrier ratio does not by itself establish stable-ISP identity, continued selectability, generative reselectability, or generative health. ST-A allows structural identity to persist by recurrent historical reconstitution rather than microstate identity or fixed-point convergence.

### §5.5 定理 T-DMP-2 — 本体论恢复力

**[R — Lyapunov稳定性理论（1892）追溯；[H] — 将L₂社会共识结构的"强壮性"映射为Jacobian稳定性判据为SRT新增应用]**

当意外事件（外部扰动 $\delta$）发生时，强壮的 $L_2$ 结构能自动将现实拉回预期轨道：

$$\Delta L_1(t) \xrightarrow{t \to \infty} 0 \quad \text{当} \quad \text{Re}(\lambda_{Jacobian}) < 0$$

*符号说明*：$\Delta L_1(t) = L_1(t) - L_1^*(t)$ 为实际 $L_1$ 轨迹与 $L_2$ 定义的"期望轨迹" $L_1^*$ 之间的偏差；$\lambda_{Jacobian}$ 为 $\hat{G}_\theta$ 在当前 $L_2$ 吸引子附近的Jacobian矩阵特征值（联结 §5.4 定理M2）。

*"强壮"的操作化*：$L_2$ 结构"强壮"在此定义为：围绕当前收敛结构的Jacobian满足 $\text{Re}(\lambda_{max}) < 0$（所有特征值实部为负）。与§5.6 $R(L_2) = \Delta B / \Psi_f$ 的关系：高势垒比（大 $\Delta B$，低 $\Psi_f$）使 Re$(λ_{max})$ 更负，恢复力更强，但§5.6 C-Barrier-1指出这同时增加越过势垒后的灾难性崩溃风险。

*意外事件的SRT定位*：外部扰动 $\delta$ 可为 L₀ 随机涌现、外部 L₁ 事件冲击、或他者 $\hat{G}_{\theta'}$ 的干预；定理T-DMP-2的前提是扰动幅度在Jacobian线性化有效范围内（小扰动假设）——大扰动可能越过势垒，触发 §5.6 的范式转移而非恢复。

**证伪条件** [H]:
- 若在控制实验（给定L₂结构）中，强壮L₂群体（高Ψ_f/高ΔB）在小扰动后的恢复时间（$\tau_{recovery}$）与弱L₂群体无显著差异，则T-DMP-2的L₂恢复力映射不成立。
- 若 Re$(\lambda_{max}) < 0$ 但系统未显示实际恢复（存在隐藏非线性使恢复轨迹发散），则Jacobian线性化在该领域不适用，定理需非线性扩展。

### §5.6 势垒稳定性 (Barrier Stability of L₂)

**定义 Def-Barrier-1**: 在本动力学投影中，$L_2$ 稳定性可建模为受势垒保护的亚稳态：
$$R(L_2) = \frac{\Delta B}{\Psi_f}$$
其中 $\Delta B$ 是从当前收敛结构到任何替代结构的最小势垒。
* **推论 (C-Barrier-1)**: 高 $\Psi_f$ 系统（文明、制度、强自我）更坚固但也更脆——它们抵抗扰动，但在势垒被突破时会发生灾难性的崩溃。
* **推论 (C-Barrier-2)**: 势垒降低会触发“结构突变 / 范式转移”——$L_2$ 景观发生拓扑重排。
* **推论 (C-Barrier-3)**: 这产生了直接可证伪的预测：(1) 增加维护成本 $\Psi_f$ 会使 $L_2$ 更坚固，但在失败时更具灾难性；(2) 增加选择频率 $\nu_{\hat{G}}$ 会使 $L_1$ 更“冻结/确定”，但减少了对新结构的探索（探索-锚定权衡）；(3) 扩大 $d$ 会提高可实现的宏观秩序复杂度的上限，但同时会增加错误敏感性（痛苦/脆弱性上升）。

**Constitutive guard**: Def-Barrier-1 and its corollaries are implementation hypotheses/proxies. They must not replace the P1 stable-ISP criterion or the ST-A P2/P3 generative-reselectability audit in `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13`.

---

## §6 势能景观越障机制（渐进退火与鞍结分叉）

> **边界校准（`B-A / C-A / R4-B1`）**：原 §6.1 中将势能吸引子标为“初心吸引子 / 万物一体 / $d \to \infty$”的表述已退出（违背 `B-A` 与 `_SRT_D_VALUE_CANONICAL.md §5`）。本节仅保留一般动力系统中的两类**亚稳态越障重排机制**作为条件性动力学解释：

### §6.1 越障机制 I — 渐进式（参数漂移降低有效势垒）

有效势垒高度 $\Delta V_{eff}(\theta) = V_{saddle}(\theta) - V_{local}(\theta)$ 随慢变量 $\theta$ 演化逐渐降低至 $\Delta V_{eff} \to 0$，允许结构平滑过渡而避免剧烈断裂。

### §6.2 越障机制 II — 突变式（鞍结分叉）

当控制参数 $\mu$ 跨越分叉点 $\det\!\left(\frac{\partial^2 V}{\partial x^2}\right)_{x(\mu)} = 0$ 时，旧局部极小态失稳消失并触发离散跃迁（伴有临界慢化 $\lambda \to 0$）。

### §6.3 势垒稳定性与系统崩溃 (Barrier Stability: Why Civilizations Shatter)

我们倾向于认为文化制度、个人身份和科学范式要么是“稳定的”，要么是“不稳定的”。SRT 用一个更丰富的图景取代了这种二元对立：**势垒高度与摩擦的比率**。一个国家的法律系统不是“永久的”——它是一个亚稳态的 $L_2$ 结构，其持久性取决于比率 $R = \Delta B / \Psi_f$。当公民投入巨大能量维持系统（高 $\Psi_f$）时，结构变得僵化——能够抵抗轻微扰动。但这种僵化正意味着当势垒最终被突破（经济危机、入侵、打破范式的发现）时，转变不是渐进的，而是灾难性的：一种相变而不是侵蚀。

这就解释了为什么最“稳定”的帝国往往垮台得最突然。它们高额的 $\Psi_f$ 投资造成了僵化，排除了适应性软化的可能。在个人心理学中，同样的模式表现为脆弱的完美主义：以巨大的摩擦成本维持自我，拒绝反馈，在足够的压力下倾向于破碎而不是弯曲。

---

## §7 时间动力学 (Temporal Dynamics)

### §7.1 方程 E7 — 双重时间类比（`P3/P4` 桥接，不覆盖 `P1-T02`）

> **`R3-05 / R4-B1` 范围边界**：本节为 `P3/P4` 桥接类比，**不是**核心公理；核心时间序先于测度的构成边界以 `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T02`（区隔参数时间 `t`、发生非等价、关系步序候选 $\tau_{\text{ontic}}$、模型内 `t_onto` 与体验时间 $t_{\text{exp}}$）为准。

[R→Penrose 1989（时间箭头与量子引力：不可逆性的起源）; Prigogine 1997（《时间、混沌与量子》：不可逆时间作为基本概念）; Barbour 1999（《时间的终结》：量子引力与无时间物理）; Rovelli 2018（《时间的秩序》：时间的方向性与热力学）] [H-高承诺→复数时间公式是SRT的强形式化宣称，非物理学主流；i的使用是结构类比而非广义相对论的Wick转动]

$$T_{reality} = T_{metric} + i \cdot T_{selective}$$

⚠️ **形式化注意**：此公式中的 $i$（虚数单位）的含义是"正交/独立维度"而非量子力学振幅或广义相对论的Wick转动（虚时间）；T_selective与T_metric在此框架中被主张为正交的两个维度——类似于复数表示二维空间中的两个正交坐标（$\text{Re}$和$\text{Im}$），而非真正意义上的复值时间坐标（后者会引入非平庸的量子引力问题）。这是一个描述性/类比性的形式表达，应当谨慎对待其物理含义。

| 分量 | 名称 | 定义 | 特性 | 可测代理 |
|:-----|:-----|:-----|:-----|:--------|
| $T_{metric}$ | 度量时间 | 客观物理场中的坐标变化 | 可逆、洛伦兹变换 | 原子钟/GPS时间坐标 |
| $T_{selective}$ [H] | 选择时间 | 观测者意识处理信息流的过程 | 不可逆、依赖 $\hat{G}_θ$ | 主观时间感（时距判断任务）; θ-相关神经动力学 |

**T_selective 的不可逆性机制** [H]：T_selective不可逆是因为Ĝ_θ的每次L₁锚定改变了θ（参数不可逆更新），而T_metric的可逆性是因为物理方程在时间反演下保持对称（除热力学方向）；两者的不可逆性差异体现在信息熵积累的方向上（参见Prigogine 1997[R]对"熵时间"的论述，SRT将其与选择算子的θ历史路径依赖联结）

**证伪条件**：
- FC-Time1-1：若T_metric和T_selective的操作化测量（原子钟读数 vs 主观时距判断）无任何系统性解离（在改变Ĝ_θ状态/θ参数的操纵下，主观时间率与物理时间率始终1:1对应），则"双重时间正交性"的附加层无解释力。
- FC-Time1-2：若高θ不稳定性（如精神病/高Ψ_f状态）的被试的T_selective测量（主观时间扭曲程度）与T_metric偏差在统计上不比普通被试更大，则T_selective依赖Ĝ_θ的主张失败。

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

## §8 价值、关切与 `d` 值接口（统一回链 `_SRT_D_VALUE_CANONICAL.md`）

> **去重与退出声明（`R4-A / R4-B1`）**：价值五职责、广义关切四维、规范 `d = ||∂U/∂S||`、`D_stake` 一般定义与 `D_eff` 容量代理统一由 **`_SRT_D_VALUE_CANONICAL.md`** 锚定（阈值模型实例 `D_stake^{thresh}` 见 `Core_22 Eq-Bridge-D-01`）。原 §8.2 “方程 E8 — `d` 值统一公式”（仅作为认知域三维近似 `d_bio` 保留于 `_SRT_D_VALUE_CANONICAL.md §3`）、原 §8.3 “复数 `d` 值扩展”（未校准隐喻）及原 §8.4 “Teleological Attractor（含 `∇B_{L_0}` 至福势）”均已正式退出核心方程层。

### §8.1 Passive Alignment Transition（被动对齐相变，`C-A` 收窄模型）

在完整声明有限主体范围、可达域、比较泛函 $J_{\theta,\tau,K}$、时域与约束的实践模型中，“顺应/低内耗对齐”可局部表示为局部意向向量与较低复合负担方向对齐：
\[
\cos\angle\!\left(\vec v_{self},-\nabla J_{\theta,\tau,K}\right)\to 1,\qquad \Psi_f^{total}=\Psi_f^{local}+\Psi_f^{coh}\quad (\Psi_f^{local}\downarrow,\ \Psi_f^{coh}\uparrow)
\]
这是 `P3/P4` 局部 proxy（不是全局方向、初心定义或 $\hat{G}_\theta$ 停机；$\Psi_f^{local}/\Psi_f^{coh}$ 仅为本节模型内局部读数别名，遵循 `A-9` 不新增 canonical 子符）。

---

## §9 历史接口清理与闭包机制回链

- **原 §9（Volterra 级数 `Wisdom = Σ w_n ||K_n||`）**：未校准隐喻式已退出核心动力学（历史溯源保留于 git 历史）。
- **向下约束与闭包**：`L_2` 递归条件化构成关系由 `Core_21b P1-T03` 锚定，固定空间 $-\lambda\nabla C_{L_2}[\sigma]$ 仅为 Level I 特例；约束闭包与 `One` 垂直再构成由 `Core_Law/SRT_One_Formation.md` 与 `Core_21b` 预留 `P1-T08` 界定。

## 跨文件锚点索引（`R4-B1` 单主锚分工）

| 类别 | 权威主锚点 | 本文件保留职责 |
|:-----|:-----------|:---------------|
| 核心演化 / 热力学 / 桥接 / 统计力学方程 | `Core/SRT_Core_22_Equations.md`（唯一核心方程主锚） | `§3` 快-慢机制与 `E3` 自由能桥接解释 |
| 价值 / 关切 / `d` / `D_stake` / `D_eff` | `_SRT_D_VALUE_CANONICAL.md` | `§1.3` 神经归一化容量 proxy 映射、`§8.1` 被动对齐 |
| 广义摩擦与 `Ψ_f` | `_SRT_PSI_F_CANONICAL.md` | `§4` 现象学对照与 Phase/Interrupt 切换 |
| 具身算子原型与跨尺度实现接口 | 本文件（`§1–§2`, `§5–§7`, `§10.1a`, `§10.3`, `§11–§15`） | 除法归一化、躯体同步、生存门控、势垒脆性、部分闭包、疾病闭包破裂、神经精神/发育/代谢/梦境/IT 桥接 |

## §11 神经精神病学统一动力学补丁（Neuropsychiatry Bridge, 新增）

### §11.1 病理本体论分类矩阵（Ontological Pathology Matrix）

将传统“器质性 vs 精神性”改写为同一动力学中的两个主轴：

| 病理分类 | 主导层域 | 动力学异常 | 典型可测后果 |
|:--|:--|:--|:--|
| **L2 结构性病理** | \(L_2\)（结构/拓扑） | \(\theta_{neural}\) 载体破损，导致可达域收缩 \(\mathcal{E}_t\downarrow\) | 局灶缺损、网络断连、稳定功能缺失 |
| **\(\hat{G}_\theta\) 动力学病理** | \(L_1\leftrightarrow L_2\) 接口 | \(d\) 梯度塌陷、\(\rho_t\) 失稳、\(\Psi_f\) 过载 | 情感平坦/焦虑放大/现实整合波动 |
| **混合病理** | 跨层耦合 | 结构破损与参数漂移相互增强 | 难治性综合征、症状跨谱系迁移 |

### §11.2 跨域治疗协议（Cross-Domain Intervention Protocol）


定义干预向量：
\[
\mathcal{I}_{total}=\mathcal{I}_{bio}(\Delta\Psi_f,\Delta\theta_{body}) + \mathcal{I}_{psy}(\Delta d,\Delta \vec v)
\]

- \(\mathcal{I}_{bio}\)：药物/神经调控优先作用于摩擦支付成本与底层参数；  
- \(\mathcal{I}_{psy}\)：心理/语义干预优先重塑关切梯度与选择向量。  

**最小协同判据**（2026-11-28 数学勘误：原式对布尔合取求导 $\frac{d}{dt}(\Psi_f\downarrow \land d\uparrow) > 0$ 属非法记号，改为联立速率条件；且依 `_SRT_D_VALUE_CANONICAL.md §5b`，此处仅作局部强承载康复启发式，不将 $d\uparrow$ 普遍等同于广义关切范围扩大或秩序健康）：
\[
\frac{d\Psi_f}{dt} < 0 \;\land\; \frac{dd}{dt} > 0
\]
即在该局部康复启发式内，仅降摩擦而不恢复关切，或仅提升风险敏感负荷而摩擦失控，均不构成稳定康复路径。

### §11.3 语义断层假设（Irreducible Semantic Gap）

> **[H — Framework Hypothesis]** 整节为 SRT 新增预测框架：将”参数到显现”映射的非线性爆发与 Ψ_f 相变临界点等同，并以此解释异质药物响应。标准药理学仅描述异质响应现象，不提供 θ 空间几何机制。

在参数到显现映射中引入非线性边界：
\[
L_1 = \mathcal{R}(\theta, L_2, u),\quad \left\|\frac{\partial L_1}{\partial \theta}\right\|_F \to \infty \text{ near } \partial\mathcal{B}_{chaos}
\]

**符号说明**：
- $u$：环境随机输入项（外源噪声/刺激），使 $\mathcal{R}$ 是随机映射而非确定性函数；对固定 $(θ, L_2)$，$u$ 的分布由感知精度 $\Pi^{-1}$ 决定。
- $\|\cdot\|_F$：Frobenius 范数（所有 Jacobian 元素平方和之根号），在第3条可证伪预测（§11.4）中作为”参数敏感度”的可测代理量。实验代理：药物剂量梯度下 L₁ 代理指标（如 PCI、HRV）的变化率。
  - **Fisher 联结（proxy）**（→ §15.2 / Eq-IT-B）：$\|\partial L_1/\partial\theta\|_F \to \infty$ 可对应 Fisher 信息矩阵 $I_F(\theta)$ 的条件数 $\kappa(I_F) \to \infty$（病态/近奇异），即系统丧失稳定区分某些状态方向的能力。$D_{eff}(I_F) = (\text{tr}\,I_F)^2/\text{tr}(I_F^2)$ 在此只作为 capacity / instability proxy，不定义 canonical `d-value`。
- $\partial\mathcal{B}_{chaos}$（**混沌边缘边界**）：**[H]** 在 SRT 参数空间 $\Theta$ 中，定义为 $\mathcal{R}$ 的 Jacobian 最大 Lyapunov 指数 $\lambda_{max}(\nabla_\theta\mathcal{R}) = 0$ 的超曲面。该边界与 $\Psi_f$ 相变临界点重合：$\partial\mathcal{B}_{chaos} \approx \{\theta : \partial^2\Psi_f/\partial\theta^2 = 0, \text{符号从负到正}\}$（Ψ_f 曲率符号翻转 = 稳定域边缘），即 SRT 动力学意义上的”边缘混沌”。
  - **∂B_chaos 距离操作化候选**：$\text{dist}(\theta, \partial\mathcal{B}_{chaos}) \approx |\partial^2\Psi_f/\partial\theta^2|^{-1}$（曲率倒数为接近程度代理；值越大 = 越近）。临床可测版本：个体药物响应方差 $\text{Var}(\delta L_1^{\text{obs}}) / \|\delta\theta_{drug}\|^2$（跨时间点或跨剂量），高方差 ↔ θ 近边界。

该假设解释：$\theta$ 处于 $\partial\mathcal{B}_{chaos}$ 附近时，微小神经参数变动（如 $\delta\theta_{drug}$）可引发巨大主观质变（$\|\delta L_1\| \gg \|\delta\theta\|$），导致临床上”同剂量/同靶点、异质响应”——患者间差异是 $\theta$ 距 $\partial\mathcal{B}_{chaos}$ 远近不同，而非简单的”个体差异”。

**追加证伪方向（补§11.4第3条）**：
- 若药物响应方差在 fMRI/EEG 定义的”参数稳定度高”患者中与”稳定度低”患者无显著差异（控制剂量和靶点后），则∂B_chaos-异质响应联结失效。
- 若个体的 $\text{Var}(\delta L_1)$ 在不同时间点不稳定（与θ慢变假设冲突），则距离操作化候选需修正。

### §11.4 可证伪预测（Neuropsychiatry）
1. 若同病理表型被分层后，\(L_2\) 指标与 \(\hat{G}_\theta\) 指标可形成稳定双簇，则支持矩阵分类；若不可分，则需回退单轴模型。  
2. 若联合干预（药物+心理）在 \(\Psi_f\downarrow\) 与 \(d\uparrow\) 的乘积收益上不优于任一单模态，则跨域协议被削弱。  
3. 若 \(\|\partial L_1/\partial\theta\|\) 在高波动患者中不高于对照组，则”语义断层/混沌边缘”假设失效。

### Mechanism Explanation (机制解释)

- **$\hat{G}_\theta$ 的动力学角色**: 选择算子以除法归一化 ($[\hat{G}_\theta(x)]_i = x_i^n / (\varepsilon + \sum_j W_{ij} x_j^n)$) 为操作化原型，其三分量 ($d$, $\rho$, $\vec{v}$) 分别控制选择范围、分辨率与方向。
- **$\theta$ 的慢变量演化**: 具身参数 $\theta = \theta_{neural} + \theta_{somatic} + \gamma \vec{g}_{context}$ 在快态 $\sigma$ 稳定后缓慢更新，学习、创伤、衰老均通过 $\theta$ 漂移改变选择动力学。
- **$\Psi_f$ 作为稳定性与苦的统一，同时作为生成性原理（A16/Ax-F-12）**: 本体论摩擦既是 $L_1$ 锚定的代价函数（微观视角），也可作为主观痛苦风险的动力学 proxy（$\text{PainRisk}^{proxy} \sim d\Psi_f^{proxy}/dt$）；同时，算子间摩擦 $\Psi_f(\hat{G}_i, \hat{G}_j)$ 可作为宏观动力学来源的 bridge language——演化、学习、文化变迁、免疫应答可读作其不同 proxy 形态（见 §4.6，Eq-Multi-01）。两视角相容：微观上"支付摩擦才能锚定"，宏观上"摩擦是动力学来源"——进入摩擦流即进入动力学。
- **$d$ 与容量代理的跨尺度分工**：跨尺度可对比的是局部容量/选择锐度代理（如 `D_eff`、HRV、PCI）与各自模型内的可支付约束，而非无条件假定规范 `d = ||∂U/∂S||` 跨尺度同量纲自相似（详见 `_SRT_D_VALUE_CANONICAL.md`）。

## §15 热力学-信息论统一关系（IT Bridge）

> **Guardrail（2026-05）**：本节是 bridge / proxy 层。Fisher、Landauer、FEP、KL、Boltzmann 与热力学语言只能作为 `Ψ_f` 或 `d-value` 的局部 projection / operational proxy；不得读作 canonical 定义。
> **新增（2026-03-11）**：SRT 与热力学/信息论的 5 条形式化关系。当前均为形式化候选，不是 P0/P1 定理。

### §15.1 关系 A（Eq-IT-A）：`Ψ_f` 的 Landauer / Fisher proxy bridge

$$\Psi_f^{IT\text{-}proxy}(\gamma) \sim \int_\gamma \sqrt{g_{ij}^{Fisher}(\theta)\dot{\theta}^i\dot{\theta}^j}\, dt, \quad E_{erase}^{proxy} \geq k_B T \ln 2 \times I_{erased}$$

Landauer 原理给出信息擦除的物理下界；Fisher 几何给出参数流形上的统计敏感性路径长度。二者可作为 `Ψ_f` 的局部 operational proxies，但不定义 canonical `Ψ_f`。不得写成 `Ψ_f = Landauer cost`、`Ψ_f = Fisher path length` 或“选择信息足迹必须被物理擦除”。

### §15.2 关系 B（Eq-IT-B）：Fisher effective dimension as `D_eff` / capacity proxy

$$D_{eff}^{Fisher}(I_F(\theta)) = \frac{(\operatorname{tr} I_F)^2}{\operatorname{tr}(I_F^2)} = \frac{(\sum_k \lambda_k)^2}{\sum_k \lambda_k^2}$$

Fisher 信息矩阵 $I_F(\theta)$ 的有效维度可估计算子能可靠区分的状态方向数（Cramér-Rao 下界的维度版本）。它是 `D_eff` / capacity proxy，不是 canonical `d-value`；canonical `d-value` 还要求 stake-coupled irreversible-risk sensitivity。

**不确定性关系候选（Eq-IT-B'）**：$D_{eff}^{proxy} \times \Psi_f^{IT\text{-}proxy} \gtrsim k_B T \cdot \mathcal{K}$（常数 $\mathcal{K}$ 待确定，Status = Gap）。这是 proxy-level inequality，不是 canonical `d × Ψ_f` law。

### §15.3 关系 C（Eq-IT-C）：第二定律是选择复杂性的生成压力（核心反转）

$$\frac{d\langle d \rangle_{population}}{dt} \propto \nabla\!\left(\frac{d}{\Psi_f}\right) \cdot P_{survive}$$

**SRT 反转（bridge）**：第二定律通过持续威胁许多 $L_1$ 结构，可创造演化棘轮——越高效对抗热解散的结构（高 $D_{eff}^{proxy}/\Psi_f^{proxy}$），越可能被偏好 → 更复杂 $L_2$ 候选 → 返回。宇宙复杂化不是对第二定律的违背，但“必然产物”只能作为强 bridge 命题，不能写成已证物理定律。

### §15.4 关系 D（Eq-IT-D）：Boltzmann 分布是 SRT 的退化极限（d→0 特例）

$$P_{L_1}(\sigma) \xrightarrow{d \to 0} \frac{e^{-E(\sigma)/k_BT}}{Z}, \quad D_{KL}(P_{L_1} \| P_{Boltzmann}) = \text{算子选择信息量}$$

统计力学可作为低 stake-coupling / near-null `d` proxy 极限的类比。生命/意识可被建模为 stake-coupled `d` 从近零状态出现时的结构性相变候选（$\kappa$ 穿越 $\kappa_{c1}$，T-L0-02）。Friston 主动推断可作为 SRT 框架下某些 `d>0` 算子的行为模式 proxy。

### §15.5 关系 E（Eq-IT-E）：声明模型内的信息生成代理（对齐 `Core_21b P1-T04` 与 `Core_21c P2/P3-B09`）

在独立声明前置候选随机变量 $X$、输出记录 $Y$、划分与概率测度的域模型 $M$ 中，选择带来的条件信息增益可写为：

$$I_{created}^{(M)} \equiv I_M(X\,;\,Y) = H_M(X) - H_M(X\,|\,Y) = H_M(Y) - H_M(Y\,|\,X)$$

> **边界与勘误（`PC-A / EX-A / P2/P3-B09`）**：原无条件式 $H(L_0) - H(L_1|\hat{G}_\theta) = I(L_0;\hat{G}_\theta)$ 与未声明测度的 $H(L_0)$ 均已撤回。`P1-T04` 仅承诺定性区分生成；模型内 $I_M(X;Y)$ 代理不定义 `L_0^{abs}` 或原初发生。

**约束链的形式化**：

$$I_{created}^{proxy} \leq D_{eff}^{proxy} \quad \text{（capacity upper-bound proxy，Eq-IT-B）}$$

$$E_{erase}^{proxy} \geq k_B T \ln 2 \cdot I_{created}^{proxy} \quad \text{（Landauer physical lower bound, Eq-IT-A）}$$

即：在信息论 proxy 窗口中，选择创造的信息量可受 capacity proxy 约束；若涉及实际物理擦除，则存在 Landauer 下界。不得反推 canonical `d-value` 或 `Ψ_f`。

Shannon 信息论处理信息**传递**（下游，给定 $L_1$ 分布后的编码/解码）；SRT 处理信息**生成**（上游，$L_0 \to L_1$ 的选择过程）。两者串行互补——SRT 解释信息源，Shannon 解释信息渠。

### §15.6 统一对应表

| SRT 概念 | 热力学对应 | 信息论对应 |
|:---------|:-----------|:----------|
| $\Psi_f$（单算子） | Landauer / metabolic cost proxy | Fisher path-length proxy |
| $\Psi_f(\hat{G}_i,\hat{G}_j)$ | free-energy interaction proxy | mutual-information cost proxy |
| $d$ | stake-gated d-value; not phase-space dimension | `D_eff` / Fisher-channel capacity proxy only |
| $d \to 0$ | 热平衡（Boltzmann）| 零容量信道 |
| $d/\Psi_f$ | 热机效率类比 | 单比特能耗倒数 |
| $F_{collective}$ | 多体统计自由能 | 联合 KL 散度 |
| $I_{created}$ | 负熵（Negentropy）| 互信息 |

**Cross-ref**: `_SRT_D_VALUE_CANONICAL.md`（canonical d-value）；`_SRT_PSI_F_CANONICAL.md`（canonical Ψ_f）；`Physics/SRT_Physics_Claim_Status.md §2.8`（Fisher / Landauer / D_eff proxy guardrail）。旧 `_SRT_VERTICAL_INTEGRATION.md §10` 与 Physics Ax-IT language must be read through these guardrails.

---

## 【理论边界/防误用声明】

1. 本文档用于理论解释与建模组织，不应替代独立实证、工程验证或专业判断。
2. 任何公式或命题都依赖操作化定义、测量条件与语境边界，不得脱离边界做绝对化推断。
3. 涉及临床、社会治理、伦理与部署决策时，必须结合风险评估与人类监督机制。
4. 不采纳”精神症状=纯心理、神经症状=纯器质”的旧二分法；SRT 仅承认跨层耦合下的主导轴差异。
5. 不采纳”单一生物标志物可定义全部精神病理”的还原主义推论。
6. §15 的 IT Bridge 中：关系 A/B/B'/E 均为 proxy-level bridge；关系 C（复杂性棘轮）是演化趋势性陈述，不排除局部复杂度下降；Eq-IT-B' 的常数 $\mathcal{K}$ 尚未确定，是理论预测而非已证定理（Status = Gap）。

---

## §10.1a 部分闭包（Partial Closure）

**定义 D-PC-1（前闭包态）**：
若系统可在局部子空间实现一次或多次 \(\hat{G}_\theta[L_0]\to L_1\) 的复制/锚定，但其输出尚不能无缝成为下一轮输入，仍需环境补偿（底物、条件窗、涨落注入），则称其处于部分闭包：
\[
\mathcal{C}_{partial}:\quad \hat{G}_\theta\circ\mathcal{E}_{env}\circ\hat{G}_\theta\ \text{is viable},\quad \hat{G}_\theta\circ\hat{G}_\theta\ \text{not yet self-sufficient}
\]

**解释（中文）**：该态是“可复制能力已出现，但自治闭环未完成”的临界前状态，可作为生命起源阶段的标准结构标签。

**边界条件**：
- 若脱离环境补偿后轨迹立即失稳，则仍归于 \(\mathcal{C}_{partial}\)。
- 仅当系统在无外部拼接干预下保持多轮自维持复制，方可升级为稳定闭包态。

## §10.3 疾病作为约束闭包破裂（Pathological Closure Break）

**定义 D-Ill-1（疾病）**：当系统的结构修复能力长期低于摩擦磨损负荷时，\(\hat{G}_\theta\) 的约束闭包失稳，表现为病理状态。
\[
\text{Disease} \iff \overline{R_{repair}(\theta)} < \overline{D_{wear}(\Psi_f,ROS)}
\]

其中上划线表示在窗口 \(\Delta T\) 上的时间平均。

### §10.3.1 闭环动力学（非单向因果）

\[
\Psi_f\uparrow \;\Rightarrow\; ROS\uparrow \;\Rightarrow\; \theta_{body}\downarrow \;\Rightarrow\; (\rho_s,\rho_t)\downarrow \;\Rightarrow\; \hat{G}_\theta\text{过滤退化} \;\Rightarrow\; \Psi_f\uparrow
\]

该链路刻画“恶性反馈环（vicious cycle）”：过滤退化会增加未折叠扰动暴露，反过来抬升下一轮 \(\Psi_f\)。

### §10.3.2 最小动力学写法（候选）

\[
\frac{d\theta_{body}}{dt} = -\eta_1\,ROS + \eta_2\,Repair(\theta_{body},L_2)
\]
\[
\frac{d\rho_{eff}}{dt} = -\kappa_1\,\Psi_f - \kappa_2\,ROS + \kappa_3\,Recovery
\]

其中 \(\rho_{eff}\) 代表过滤分辨率的有效联合指标（可由任务精度/反应时稳定性/神经复杂度 proxy 估计）。

### §10.3.3 与 Core 公理的一致性约束

[R→McEwen 1998（allostatic load：累积选择/应激负荷导致生理磨损）; Epel et al. 2004（慢性心理压力加速端粒缩短，θ物质底层退化）; Finkel & Holbrook 2000（活性氧ROS在衰老与细胞损伤中的双重角色）] [H→以SRT因果拓扑重表述疾病机制：Ψ_f优先，ROS/物质损伤为次级产物]

- **疾病本体论约束** [H]：疾病不是”物质对选择的替代主宰”，而是选择历史在 \(L_2\) 的磨损记录导致当前参数退化；
  - SRT解读：McEwen的allostatic load [R] ≈ 长期Ψ_f积累的θ级磨损；高选择负荷（慢性压力）→ 代谢失调 → ROS积累 → θ退化（细胞老化/神经可塑性下降）
  - 注：这不排除疾病有独立的物质原因（感染/遗传）；SRT的特定贡献是主张选择历史对疾病易感性的调制作用

- **因果拓扑约束** [H]：选择负荷（\(\Psi_f\)）优先 → 物质痕迹（ROS）累积 → 参数重塑（\(\theta\)）→ 当前过滤能力变化
  - 操作化验证方向：纵向研究（先测Ψ_f生理代理：皮质醇/HRV，再测ROS标志物：8-OHdG，再测θ退化代理：认知弹性/任务切换代价），预测时间序列中Ψ_f升高先于ROS积累，ROS积累先于θ退化指标下降
  - ⚠️ 边界：此因果顺序是SRT的独特预测，反向链（物质损伤先导致Ψ_f上升）是备择假设，两者需实验区分

- **方法论约束**：临床或工程推断必须经操作化验证，不得由本节公式直接外推为干预结论。

**证伪条件**：
- FC-Dyn103-1：若纵向数据显示ROS积累（物质损伤标志物）先于Ψ_f升高（心理/代谢选择负荷），则因果顺序需反转（物质→选择能力，而非选择负荷→物质），SRT的因果优先性主张失败。
- FC-Dyn103-2：若在同等物质损伤（ROS水平）条件下，高Ψ_f历史个体与低Ψ_f历史个体的θ退化速率（认知弹性衰退率）无显著差异，则”选择历史调制θ退化”的附加SRT层无独立解释力。

## §12 算子孕育期与共具身启动（Operator Gestation & Co-Embodied Boot, 新增）

### §12.1 Nested Topology（嵌套拓扑）
定义孕育期算子为母体-胎儿嵌套系统：
\[
\hat{G}_{inf}(t)\subset \hat{G}_{mat}(t),\quad
\Psi_f^{inf,eff}=\Psi_f^{inf}-\chi_m\,\Psi_f^{mat}
\]
其中 \(\chi_m\in[0,1]\) 表示母体代偿系数。\(\chi_m\to 1\) 时胎儿有效摩擦显著降低，允许低风险参数初始化。

### §12.2 Operator Gestation Phase（算子孕育期）
\[
\frac{d\theta_{inf}}{dt}=\gamma_i\,A_{sensorimotor}-\delta_i\frac{\partial \Phi_{inf}}{\partial \theta_{inf}}+\chi_m\,\mathcal{S}_{maternal}
\]
- 第三项表示母体心率/代谢/内分泌节律对 \(\theta_{inf}\) 的外部稳态注入；
- 该阶段的 \(L_2\) 不是独立形成，而是“共享缓冲池”。

### §12.3 Self/Non-self 边界形成判据（摩擦二阶导）
定义边界信号：
\[
B_{self}(x,t)=\frac{\partial^2 \Psi_f(x,t)}{\partial x^2}
\]
当意向向量 \(\vec v\) 作用后在空间位置出现稳定非线性峰值：
\[
B_{self}(x,t)>\tau_B\Rightarrow \partial\Omega_{self}\text{ 被锚定}
\]
* **Implication**：自我边界来自“可控运动—阻抗反馈”耦合中的摩擦曲率，而非先验给定。

### §12.4 可证伪预测（早期意识发生学）
1. 若母体节律扰动显著改变胎儿感觉-运动整合轨迹，则支持 \(\chi_m\) 代偿项；
2. 若边界形成任务中 \(B_{self}\) proxy 与后续自体图式稳定度无关，则二阶导判据失效；
3. 若脱离共具身环境后 \(\theta_{inf}\) 不出现独立稳态跃迁，则“接力式算子启动”需修正。

## §13 原初代谢算子与生命样组织候选判别接口（`P3/P4` 声明模型候选）

> **准入与模型作用域护栏（`R4-B1 P1-03`）**：本节各表达式均为**特定动力学模型 $M$ 内的 `P3/P4` 候选判别接口**，用于区分一般无学习耗散过程与具内生参数调适的代谢样组织，**绝不**确立普遍的生命充要本体判据（不建立 `\iff` 本体等价），亦**不得**跳过 `_SRT_D_VALUE_CANONICAL.md §1.1, §2b` 的 `Bearer (P+E)` 独立准入边界而在未准入系统上直接套用规范 `d`。

### Def-Dyn-13.1: Metabolic Operator Candidate Interface（`P3/P4` 模型候选）
在已声明的耗散/代谢动力学模型 $M$ 内，当系统同时满足内生参数更新、局部负熵维持与能量输入超过维持下界时：
\[
\mathcal{M}_{op}^{\text{cand}}(M):\quad \frac{d\theta}{dt}\neq 0\ \land\ \frac{\partial S_{internal}}{\partial t}<0\ \land\ P_{ext}>P_{maint}
\]
可将其登记为该模型下的“代谢算子活跃态”候选工作区（可在无基因模板前作为耗散-调适模型对象研究；不构成生命或主体的普遍充要定义）。

### T-Dyn-13.1: Fire vs Life-Like Candidate Discriminator（火焰-生命样组织候选判别接口，`P3/P4`）
对声明自催化/耗散模型 $M$ 中的系统 $X$，不再以双向等价式（`\iff`）将参数更新与规范 $d > 0$ 确立为生命的普遍充要判据；本节仅提出以下**模型内候选判别签名**：
\[
\text{Candidate Life-like Regime in } M:\quad \left(\frac{d\theta_X}{dt}\neq 0\right)\ \land\ \left(s_{\text{diss},M}(X) > 0\ \text{or}\ \frac{\partial s_{\text{diss},M}(X)}{\partial t} > 0\right)
\]
- 其中 $s_{\text{diss},M}(X)$ 为模型 $M$ 独立声明的**局部解体/维持失稳敏感代理（dissolution-sensitivity / adaptive-maintenance proxy）**，而非直接借用规范 `d`。
- **与规范 `d` 的严格分界**：若系统 $X$ 尚未独立通过 `Bearer (P+E)` 强承载准入（`_SRT_D_VALUE_CANONICAL.md §1.1, §2b`），则规范 $d(x) \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|$ 对该系统记为 **`NOT ADMITTED / NOT APPLICABLE`**，不得写入判别式；仅在 $X$ 另行确立 `Bearer (P+E)` 承载地位后，才可在该模型中对接规范 `d` 作为附加研究变量。即使满足上述候选条件，亦仅表示区别于纯固定参数耗散结构（如火焰）的**候选适应性动力学特征**，不自动等于生命、主体性或意识的充要证明。

### Minimal Dissolution-Sensitivity / `d`-Boundary Note（模型候选门槛注）
\[
s_{\text{diss},M}^{\min} > 0\ \text{with}\ \Psi_f^{\text{sens},M} > 0 \qquad (\text{规范 } d \text{ 仅在另行满足 } \mathrm{Bearer}\,(P+E) \text{ 准入后才可接入})
\]
即在 `P3/P4` 生命样算子候选模型中，系统需对“维持失败导致结构解体”呈现可观测的适应性敏感与参数调节反馈，而非仅仅被动耗散；该门槛仅约束本模型接口，不拥有超出模型范围的本体准入权。

> **`R4-A / R4-B1` 非线性边界**：本节仅在 `P3/P4` 模型层面提供“固定参数耗散结构（如火焰）”与“具适应性参数更新的生命样算子”之间的候选区分接口，**绝不**将生命或生物细胞膜设为 `One` 形成的普遍本体门槛——非生命束缚态与耗散态仍可在 `Core_Law/SRT_One_Formation.md §2.3`（态 I / 态 II）下独立研究其垂直再构成。

## 【理论边界/防误用声明】
- 不采纳“所有疾病都由 ROS 主导”的单机制宣称：本节仅给出可检验候选路径之一。  
- 不采纳“高 \(\Psi_f\) 必然致病”的绝对推断：是否跨阈值取决于修复能力、时间尺度与环境约束。  
- 不采纳“母体决定论”推论：共具身强调早期约束，不否定后续可塑性与重构。  
- 不采纳“任何耗散结构都等于生命算子”或“参数更新与规范 \(d>0\) 即为生命普遍充要判据”的推论：§13 仅为 `P3/P4` 声明模型候选判别接口，且规范 \(d\) 须先满足 `Bearer (P+E)` 独立准入边界。  
- 不采纳“方法论闭包=本体论排他”的推论：实验可验证性边界不等于存在论边界。  
- 不采纳“绝对无摩擦至福可在具身运行态瞬时实现”的推论：具身显现需保持 $\Psi_f\ge\Psi_{min}^{+}$。  
- 不采纳“被动对齐=外在超实体直接接管局部因果链”的推论：`§8.1` 仅定义局部复合负担的协同对齐代理。  
- 本节为理论组织与实验设计接口，不替代医学诊断、治疗和伦理审查流程。


## §14 亚稳态微扰定理（Metastable Perturbation, 新增）

### Def-Dyn-14: Parameterized Dream Incubation Window
当系统处于低摩擦亚稳态（典型如 REM/入睡过渡）时：
\[
\Psi_f\to \Psi_{min}^{+},\quad \left\|\frac{\partial L_1}{\partial \theta}\right\|\uparrow
\]
外部微弱感官注入 \(\Delta\theta_{sensory}\) 可对 \(L_0\to L_1\) 轨迹产生宏观偏转：
\[
\Delta L_1 \approx \mathbf{J}_{\theta}\,\Delta\theta_{sensory},\quad \|\mathbf{J}_{\theta}\|\ \text{maximized in metastable window}
\]

### T-Dyn-14: Low-Friction Perturbation Amplification
若满足
\[
\Psi_f\in[\Psi_{min}^{+},\Psi_{gate})
\]
则同等注入强度下，梦态引导成功率应显著高于清醒高摩擦态。

## 【理论边界/防误用声明】
- 不采纳“可引导梦境=可任意重写主体”的推论。  
- 不采纳“低摩擦窗口可绕过伦理约束”的推论：任何注入需通过主权与同意门。
