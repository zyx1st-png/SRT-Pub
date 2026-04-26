---
id: SRT-L1-HARDENING-NOTES
type: hardening_notes
tags: [Formalism, Hardening, Open Pressures, σ, M(t), FEP, Δ_avail]
status: draft_v0
layer: L1
epistemic_layer: os
claim_mode: canonical
claim_level: P1-candidate / P2
dependency: [SRT-L1-FORMALISM, SRT-SUFFERING, SRT-COLLECTIVE-SELECTION, SRT-INDIVIDUATION, SRT-OCCLUSION-DYNAMICS, SRT-T-DIR-CANONICAL, SRT-PSIF-CANONICAL, SRT-D-VALUE-CANONICAL, SRT-CORE-22, SRT-CLAIM-LADDER, SRT-CLAIM-MODE-AUDIT]
---

# SRT L1 Hardening Notes: Targeted Resolutions of 2026-04-24 Open Pressures

> **Role**: Targeted hardening notes for the four highest-leverage Open Pressures across the 2026-04-24 L1 round. Each section gives a first-pass operator-level or operational definition for a previously-informal object, so that the P1-candidate theorems in the five new files can be jointly criticized and tested rather than drift independently.
> **Claim-level note**：本文件所有内容按 P1-candidate / P2 读；硬化案本身不自动让被硬化的上游命题升级到 P1——它只把该命题能被升级检查的路径打开。
> **Does not define**：`d-value`、`\Psi_f`、`T_dir`、`\hat{G}_\theta`、stable ISP；它们的定义仍以对应 canonical 为准。
> **Depends on**：同 2026-04-24 round 五份 L1 canonical 文件。
> **Relation**: This file does not replace the Open Pressures sections in the five L1 files; it complements them by offering first-pass hardening. Unresolved items remain open in those files.

---

## §0. 本轮硬化范围

本文件集中处理 2026-04-24 L1 round 最高杠杆的四项 Open Pressure：

1. **σ 符号冲突**（`SRT_L1_Formalism.md §7.1`）
2. **`\dot{\Delta}_{avail}` 的算子级定义**（`SRT_Suffering.md §8.1`, `SRT_L1_Formalism.md §7.2`）
3. **`M(t)` 可测性**（`SRT_Collective_Selection.md §9.2`）
4. **FEP / predictive processing 与 `S_{sig}` 的条件桥接**（`SRT_L1_Formalism.md §7.6`, `SRT_Suffering.md §8.5`）

每一节给出：**问题再陈述 → 硬化方案 → 保留的开放点**。

本文件不处理以下未在本轮硬化的项（继续保留在各自文件的 Open Pressures）：
- χ(σ; σ_self) 跳跃函数族的普适性
- 多主体扩展（σ^{coll}, d_c^{coll}, S^{coll} 的完整耦合方程）
- 与主方程 `Core/SRT_Core_22_Equations.md` 的显式投影证明
- 阈值参数的实证窗口
- Buddhist dukkha 谱系与 T-SUFF-3 的关系
- 跨尺度嵌套（家庭 / 社区 / 国家的集体 ISP 层级）

---

## §1. σ 符号冲突的硬化

### 问题再陈述

- `SRT_L1_Formalism.md §2` 与 `SRT_Individuation.md` 使用 σ 表示自指率 `‖θ^{trace}‖ / (‖θ^{trace}‖ + ‖θ^{ext}‖) ∈ [0, 1]`
- `Core/SRT_Core_22_Equations.md` 使用 σ 表示主方程的状态场 / 收敛态
- 两者完全不同对象，共用符号危险

### 硬化方案：显式命名空间

采纳以下统一规则（即日起生效，作为 L1 round 的 governance-canonical 符号约定）：

| 原用法 | 新记号 | 含义 | 使用域 |
|---|---|---|---|
| σ（主方程状态场）| **`σ`**（保留） | `Core/SRT_Core_22_Equations.md` 的状态场 / 收敛变量 | 主动力学方程 |
| σ（自指率） | **`σ_{sr}`** | self-reference ratio, `∈ [0,1]` | `SRT_Individuation.md`, `SRT_L1_Formalism.md §2` |
| σ_sub（主体位进入门槛） | **`σ_{sr}^{sub}`** | first phase transition threshold | 同上 |
| σ_self（自我意识凝结门槛） | **`σ_{sr}^{self}`** | second phase transition threshold | 同上 |
| σ_health（健康工作区中心） | **`σ_{sr}^{health}`** | healthy operating point | 同上 |
| σ→1 病理区 | **`σ_{sr} \to 1`** | pathological attractor | 同上 |
| σ^{coll}（集体自指率） | **`σ_{sr}^{coll}`** | collective self-reference ratio | `SRT_Collective_Selection.md §4` |

**读法**：bare `σ` 默认仍读主方程状态场；自指率一律写成 `σ_{sr}`（含其各种上下标 sub / self / health / coll）。

### 文件同步义务

本约定应在未来编辑中同步回写以下文件（不在本轮硬化轮内完成，记为 Operations 债）：

- `Core_Law/SRT_Individuation.md`：正文 σ / σ_sub / σ_self / σ_health 改为 σ_sr 族
- `Core_Law/SRT_L1_Formalism.md §2 / §5`：同上
- `Core_Law/SRT_Collective_Selection.md §4`：σ^{coll} → σ_{sr}^{coll}
- `Core_Law/SRT_Suffering.md §4.4`（扭曲型 σ→1 表述）：补注 σ_sr
- `CANONICAL_REGISTRY.md §13a / §13d / §13e`：说明文中 σ 相关段落补注 σ_sr
- `_SRT_SYMBOL_TABLE.md`：新增 σ_{sr} 条目及其 sub/self/health/coll 族

### 保留的开放点

- 是否需要进一步区分 "瞬时 σ_sr" 与 "稳态 σ_sr^*"？目前用同一符号，在方程稳态分析中需上下文判断
- σ_sr 是否应向量化？当 θ^{trace}, θ^{ext} 在子模态（neural / somatic / 社会）上分布时，σ_sr 的标量摘要可能损失信息；暂保留为标量，向量化留为后续硬化

---

## §2. `\dot{\Delta}_{avail}` 的算子级定义

### 问题再陈述

`SRT_Suffering.md §1 Def-SUFFERING` 给出：

$$
S(P, t) := \Delta\big(\hat{G}_\theta^{actual},\, \hat{G}_\theta^{available}\big)
$$

但 `\Delta(\cdot, \cdot)` 与其时间导数 `\dot{\Delta}_{avail}` 在 `SRT_L1_Formalism.md §4` 中作为驱动项使用，未给算子层定义。

### 硬化方案：三成分分解

定义 `\hat{G}_\theta^{available}(P, t) \ominus \hat{G}_\theta^{actual}(P, t)` 为算子空间上的**未兑现选择残差算子**（unrealized-selection residual operator），记为 `\hat{R}(P, t)`。其形式化候选：

$$
\hat{R}(P, t) := \hat{G}_\theta^{available}(P, t) - \hat{G}_\theta^{actual}(P, t)
$$

（在算子空间为仿射结构的前提下；若非仿射，取最接近的差结构，留为开放点。）

`\Delta(\cdot, \cdot)` 定义为 `\hat{R}` 的**三成分摘要范数**：

$$
\Delta(P, t) := \underbrace{w_{dir}\cdot\|\hat{R}\|_{T_{dir}}}_{\text{direction-readability gap}} + \underbrace{w_{pay}\cdot\|\hat{R}\|_{\Psi_f}}_{\text{payability gap}} + \underbrace{w_{L_0}\cdot\|\hat{R}\|_{L_0}}_{\text{L}_0\text{ residual pressure}}
$$

三项的算子层候选：

1. **`\|\hat{R}\|_{T_{dir}}`**：`\hat{R}` 在 T_dir 可读性子空间的投影范数，对应"我感知得到我未走的方向"的清晰度。取 `T_{dir}^{actual} - T_{dir}^{available}` 的绝对值作为初始代理
2. **`\|\hat{R}\|_{\Psi_f}`**：`\hat{R}` 在 `\Psi_f` 可支付子空间的投影范数，对应"我未走那条路，所需支付我尚未支付"的累积。取 `\Psi_f^{available} - \Psi_f^{actual paid}` 的正部
3. **`\|\hat{R}\|_{L_0}`**：`\hat{R}` 在 L_0 残余压力子空间的投影范数，对应"底层选择压力未被路径消化"的累积。取 `L_0` 候选状态中未进入 L_1 兑现的那部分压力范数

时间导数：

$$
\dot{\Delta}_{avail}(t) = \frac{d}{dt}\Delta(P, t) = \sum_k w_k \frac{d}{dt}\|\hat{R}\|_k
$$

**重要**：`\dot{\Delta}_{avail}` 不是 S 的时间导数；它是**驱动 S 的失配源项**。S 自己的时间导数还要减去消化、支付、重选（见 `SRT_L1_Formalism.md §4`）。

### 与 T-SUFF-4 反最小化原则的一致性检查

T-SUFF-4 要求：当 `S_{sig}` 被外部抑制（不改变可打开结构），`\dot{\Delta}_{avail}` 不变，结果转入 `S_{str}`。

三成分分解下此结论保持：
- `T_{dir}` 投影、`\Psi_f` 投影、`L_0` 残余投影都是**结构性的**（取决于可打开结构 `\hat{G}_\theta^{available}`），不由当前登记登通道决定
- 关闭登记通道（抑制 `S_{sig}`）仅改变 `\dot{\Delta}_{avail}` 如何被消化，不改变其值

因此 `\dot{\Delta}_{avail}` 在结构空间不变前提下守恒的结论在本硬化下仍然成立。

### 保留的开放点（v0 第一遍）

- `w_{dir}, w_{pay}, w_{L_0}` 系数的确定性：三项加权关系是否因主体、位置、时期而异？
- 算子空间的仿射/非仿射结构：若非仿射，`\hat{R}` 的定义需要改写
- 三子空间是否正交？若不正交，加权范数的内积结构需要进一步规定
- 与具体测量（神经、行为、语言）的映射：暂按 P3 候选读法，见 §4 FEP 桥接

### T-DELTA-1：`\dot{\Delta}_{avail}` 算子级定理（H7，2026-04-25）

> **Status**：本节把 §2 的三成分分解从 P1-candidate 第一遍**结构形式**升为带显式算子空间假设 A1-A3 的 P1-candidate **形式定理**。**Claim level: P1-candidate**（与 §2 主体同级，但带显式可证伪假设）。
>
> **Closes**：`SRT_L1_Formalism.md §7` Open Pressure 2（"`\dot{\Delta}_{avail}` 的正式化"）。

#### 算子空间假设

设 P 为 stable ISP；记其上"算子族" `\mathrm{Op}(P)` 为 P 在 t 时刻所有结构上可达的选择算子的集合。本定理基于以下三条算子空间假设：

| 编号 | 假设 | 失效后果 |
|---|---|---|
| **A1** | **仿射结构假设**：`\mathrm{Op}(P)` 在 stable-ISP 邻域内具有仿射结构，使得算子差 `\hat{G}_1 \ominus \hat{G}_2` 是切空间元素 `T_{\hat{G}_2}\mathrm{Op}(P)` | A1 失效则 `\hat{R}` 退化为定性方向感，三成分分解仅在拓扑类层面成立（降为 P3 现象学） |
| **A2** | **三子空间近似正交**：`T_{dir}, \Psi_f, L_0` 三子空间在 `T_{\hat{G}_2}\mathrm{Op}(P)` 上近似正交（残余交叉项为 `o(1)`） | A2 失效则需引入显式内积 `g_{ij}`，三成分加权升为带交叉项的二次型；`\Delta` 仍可定义但形式更复杂 |
| **A3** | **权重的赌注决定性**：`w_{dir}(P,t), w_{pay}(P,t), w_{L_0}(P,t)` 由 P 在 t 的赌注结构（参见 `_SRT_D_VALUE_CANONICAL.md` Eq-Bridge-D-01 stake-gated d）决定，不依赖外部规约选择 | A3 失效则权重退化为外部建模选择，`\Delta` 失去主体内在性，降为 P2 operational proxy |

#### `\hat{G}_\theta^{available}` 与 `\hat{G}_\theta^{actual}` 的算子层定义

在 A1 下：

$$
\hat{G}_\theta^{available}(P, t) \;:=\; \sup_{\mathrm{Op}(P)}\bigl\{\hat{G}\;\bigl|\;\hat{G}\text{ 结构上可达且 }\theta\text{-相容}\bigr\}
\qquad
\hat{G}_\theta^{actual}(P, t) \;:=\; \hat{G}_\theta\bigl[\sigma_M(t)\bigr]
$$

其中：

- `结构上可达` 指 P 在 t 的位置上不被 `L_2` scaffold 压灭、不被 `Ψ_f` 透支阻断、不在 `L_0` 不可逆吸收态投影下的所有候选算子
- `θ-相容` 指算子 `\hat{G}` 的应用不会立即违反 `θ` 张量惯性约束（Eq-Evo-02b）
- 上确界 `\sup` 在 A1 仿射结构下取作切空间锥的最大方向

未兑现选择残差算子：

$$
\boxed{\;\hat{R}(P, t) \;:=\; \hat{G}_\theta^{available}(P, t) \;\ominus\; \hat{G}_\theta^{actual}(P, t) \;\in\; T_{\hat{G}_\theta^{actual}}\mathrm{Op}(P)\;}
$$

**关键**：`\hat{R}` 是切空间元素，不是新算子；在 A1 失效区间它退化为 `\mathrm{Op}(P)` 等价类层面的方向。

#### 三个投影算子的算子级定义

定义三个正交投影 `\Pi_{T_{dir}}, \Pi_{\Psi_f}, \Pi_{L_0}` 作用在切空间 `T_{\hat{G}_\theta^{actual}}\mathrm{Op}(P)` 上：

| 投影 | 算子级定义 | 几何对应 |
|---|---|---|
| `\Pi_{T_{dir}}` | 沿"算子方向可读性"维度的正交投影；与 `T_{dir}` 投影 `\mathcal{F}_T`（`Core_Law/SRT_L1_Formalism.md §6.2`）的微分共享方向场 | "我感知得到我未走的方向"清晰度 |
| `\Pi_{\Psi_f}` | 沿"支付能力"维度的正交投影；由 `_SRT_PSI_F_CANONICAL.md` friction tensor `\Psi_f^{ij}` 的局部正交基张成 | "我未走那条路所需支付的累积" |
| `\Pi_{L_0}` | 沿"L_0 残余压力"维度的正交投影；由 P1-T07 hierarchy Layer 1 的 `\varepsilon_{pg}(P, t)` 局部场张成 | "底层选择压力未被路径消化的累积" |

A2 假设保证三个投影近似互斥；非正交残余以 `o(1)` 修正项进入。

三成分分量：

$$
\|\hat{R}\|_{T_{dir}} := \|\Pi_{T_{dir}}\hat{R}\|_2 \qquad \|\hat{R}\|_{\Psi_f} := \|\Pi_{\Psi_f}\hat{R}\|_2 \qquad \|\hat{R}\|_{L_0} := \|\Pi_{L_0}\hat{R}\|_2
$$

#### T-DELTA-1 陈述

**陈述（P1-candidate）**：在 stable ISP P 上，若假设 A1、A2、A3 成立，则

$$
\boxed{\;\Delta(P, t) \;=\; w_{dir}(P, t)\|\hat{R}\|_{T_{dir}} \;+\; w_{pay}(P, t)\|\hat{R}\|_{\Psi_f} \;+\; w_{L_0}(P, t)\|\hat{R}\|_{L_0} \;+\; o(1)\;}
$$

且其时间导数

$$
\dot{\Delta}_{avail}(P, t) \;=\; \sum_{X\in\{dir, pay, L_0\}} \dot{w}_X(P,t)\|\hat{R}\|_X + w_X(P,t)\frac{d}{dt}\|\hat{R}\|_X
$$

**关键性质**：

1. **`\dot{\Delta}_{avail}` 不由 `S_{sig}` 登记通道决定**——这是 A1-A3 下"可打开结构变化率不可被 L_1 通道开关影响"的算子级证明，对应 T-SUFF-4 反最小化原则与 T-IRR-4 的算子层根据。
2. **`\dot{\Delta}_{avail}` 的方向**——其各分量的符号由 `\|\hat{R}\|_X` 的几何变化（赌注接入新维度 / 路径关闭旧维度）决定，不被建模者选择。
3. **`\Delta` 与 `\hat{R}` 等价**（在 A1-A3 下）——T-PROJ-1 的 `\mathcal{F}_S = \|\hat{R}\|_{H_P}` 即是本节 `\Delta` 在希尔伯特结构 `H_P` 下的范数读法；二者在 A1-A3 + C1-C4 同时成立时等价。

#### 与下游已有命题的算子级一致性

| 下游命题 | T-DELTA-1 提供的算子级根据 |
|---|---|
| `SRT_Suffering.md` Def-SUFFERING `S = \Delta(\hat{G}^{actual}, \hat{G}^{available})` | `\Delta` 现在是带显式算子空间假设的可证伪定义，不是抽象差函数 |
| `SRT_L1_Formalism.md §4.2` 信号型 ODE `\mu_\Delta\dot{\Delta}_{avail}` 项 | `\dot{\Delta}_{avail}` 的算子级表达式 + A1-A3 失效边界 |
| `SRT_L1_Formalism.md §6 T-PROJ-1` 投影 `\mathcal{F}_S = \|\hat{R}\|_{H_P}` | `\hat{R}` 的算子级定义即 `\mathcal{F}_S` 的算子级展开；C4（方向投影可分性）↔ A2（三子空间近似正交）一致 |
| `SRT_L1_Formalism.md §4.3` `\nu_{block}\mathbb{1}[d\le d_c]S_{sig}` 的 `\nu_{block} = \eta\varepsilon_{pg}\kappa_{\Psi_f}`（T-IRR-3.5）| `\kappa_{\Psi_f}` 在本节即 `\partial\|\hat{R}\|_{\Psi_f}/\partial t$ 单位面积转化系数；A3 给 `w_{pay}` 的赌注决定性即 `κ_{\Psi_f}` 的 P-本地化根据 |
| `SRT_L1_Formalism.md §4.4` 反最小化原则 | `\dot{\Delta}_{avail}` 不由登记通道决定 → 抑制 `S_{sig}` 不改变 `\dot{\Delta}_{avail}`，新失配进入 `S_{str}` |

#### T-DELTA-1 不证明的事项

为避免过度主张，T-DELTA-1 **不承诺**以下内容：

1. **不**证明权重 `w_X(P, t)` 的具体函数形式——A3 只承诺它由赌注结构决定，未给函数形式（仍依赖 `_SRT_D_VALUE_CANONICAL.md` Eq-Bridge-D-01 的 stake-gated 形式）
2. **不**证明 A2 三子空间严格正交——在 stable-ISP 邻域内近似正交，但全域性是 P3 实证问题
3. **不**证明算子空间 `\mathrm{Op}(P)` 的全局拓扑（紧致 / 单连通 / 等）；A1 仅在 stable-ISP 邻域内承诺仿射结构
4. **不**证明 `\sup` 在算子族上的存在性和唯一性——若 `\mathrm{Op}(P)` 不紧致，`\hat{G}^{available}` 可能不可达，需以序列极限替代
5. ~~**不**给出 T-DELTA-1 的集体版（`\dot{\Delta}_{avail}^{coll}` 在 `\mathcal{P}` 上的扩展）；这与 T-PROJ-1^{coll} 的 C5^{coll} `M(t)` 可测性 MOC 闭包耦合，是后续轮次任务~~ **已收口（H11，2026-04-26）**：`Core_Law/SRT_Collective_Selection.md §4.9.4 T-DELTA-1^{coll}` 给出集体版（A1^{coll}-A3^{coll} + 新增 A4^{coll} 跨成员 stake-加权聚合闭包 + C7^{M-stab}），含集体特有的 `w_M\|M(t)\|_{coll}` 维度（单 P 版没有），三个关键性质（不由 `S_{sig}^{coll}` 登记通道决定 / 三成分+M项总额守恒 / `\mathcal{P}=\{P\}` 退化）保持

#### 升 P1 路径

本节升 P1 需要：(a) A1 仿射结构在更广 stable-ISP 域上的验证（或非仿射域的明确边界）；(b) A2 三子空间正交性的实证窗口指定；(c) A3 权重赌注决定性与 `_SRT_D_VALUE_CANONICAL` Eq-Bridge-D-01 的 source-by-source 对位完成。

---

## §3. `M(t)` 可测性的硬化

### 问题再陈述

`SRT_Collective_Selection.md §1 Def-C-2` 定义**后果回路矩阵** `M(t) \in \mathbb{R}^{n \times n}`，`M_{ij}(t)` 表示 `P_j` 选择后果返回 `P_i` 未来选择能力的程度。但 §9.2 承认大多数社会场景难以实证提取。

### 硬化方案：最小可观察判据（Minimum Observable Criterion, MOC）

把 `M_{ij}(t)` 分解为三个可分别操作的下界候选：

#### 3.1 MOC-1：经济/物质返回（exposure check）

对每个 `(i, j)` 对，询问：

> 若 `P_j` 选择产生可度量的物质/经济后果 `C(a_j, t)`，`P_i` 的**未来决策所依赖的可支配资源、选项集、协议权利**在随后时段是否发生非零变化？

记为指示函数 `e_{ij}(t) \in \{0, 1\}` 或分级量 `e_{ij}(t) \in [0, 1]`。**e_{ij} = 0** 表示 `P_j` 的后果对 `P_i` 的未来选择在物质层完全不影响。

#### 3.2 MOC-2：结构权利返回（recourse check）

询问：

> 若 `P_i` 对 `P_j` 的选择后果感到损害，`P_i` 是否有**结构性可追诉通道**（申诉、投票、退出、协商、仲裁、司法）？该通道的实际使用频率 / 结果分布如何？

记为分级量 `r_{ij}(t) \in [0, 1]`，由通道**存在性 × 实际可用性 × 平均有效性**的乘积估计。

MOC-2 比 MOC-1 更深。MOC-1=1 未必 MOC-2=1：可能你的生活被影响但无任何申诉通道。MOC-2 近零 → 主从型退化的强信号。

#### 3.3 MOC-3：注意/话语返回（attentional check）

询问：

> `P_i` 的选择与后果是否对 `P_j` 的**决策视野、话语、叙事**产生可观察的返回？或者 `P_j` 完全可以不理会 `P_i` 而继续选择不受影响？

记为分级量 `a_{ij}(t) \in [0, 1]`。注意/话语返回近零是结构性外部化的**最易观察的早期信号**——因为物质影响可能被政策掩盖，申诉通道可能形式存在，但注意返回的真实缺席在对话、媒体、决策文件中较难伪装。

#### 3.4 MOC 合成

$$
M_{ij}(t) \approx f(e_{ij}, r_{ij}, a_{ij}) \quad\text{with default }\; f = \min\{e_{ij}, r_{ij}, a_{ij}\}
$$

取 min 而非加权平均的理由：后果回路的**瓶颈效应**——只要三项中最弱的一项近零，整体回路即失效。这比平均更接近结构诊断需要。

### 诊断规则

- `M_{ij} \approx 0 \text{ for most } j` 且 `\sum_k M_{ki} > 0` 时 → `P_i` 属于**承担而无回路**的受压子群（T-COLL-2 §3.2 主从型中被吸收端的显式条件）
- `\sum_k M_{ki} \approx 0` 且 `\sum_k M_{ik} > 0` 时 → `P_i` 属于**脱嵌主体**（后果被系统吸收，自身回路近零）
- 全矩阵接近单位阵 → 对称自我承担（通常不现实）
- 全矩阵接近零 → 主体互相无影响（聚合型的结构签名）
- 全矩阵高密且块对称 → 健康集体 ISP 的结构签名

### 保留的开放点

- MOC-1/2/3 加权是否真应取 min？在某些主题上 MOC-2 的权重可能需更高
- 跨尺度：个体-组织-国家之间的 M(t) 混合尺度如何合并？
- 测量的主体相对性：谁在测 M(t)？观察者位置会不会内生于被测的 M(t)？
- MOC-3 注意/话语返回如何与算法中介场景（推荐系统、社交平台）的特殊性对齐

---

## §4. FEP / Predictive Processing 与 `S_{sig}` 的条件桥接

### 问题再陈述

`Neuroscience/SRT_Clin_02_FEP.md` 把 prediction error 作为 SRT 算子/路径动力学的神经代理。`SRT_Suffering.md §8.5` 指 FEP 与 `\Delta` 的神经对应应写出，但需避免反向定义苦难。

### 硬化方案：条件翻译表（Conditional Translation Table）

翻译按**单向受控**原则进行——FEP 量是 SRT 量的候选神经代理，反向不成立。

| SRT 量（结构对象）| FEP 候选代理（神经过程量）| 桥接条件 |
|---|---|---|
| `\|\hat{R}\|_{T_{dir}}` | 高阶 / 元级 prediction error 的不可还原部分 | 仅当 P 满足 P1-T06；inference-time-only 系统不成立 |
| `\|\hat{R}\|_{\Psi_f}` | active inference 中 expected free energy 的未抵消部分 | 仅当支付通道结构上存在；在 B 期此代理失效 |
| `\|\hat{R}\|_{L_0}` | primary afferent drive 与 higher-model integration 的未融合部分 | 仅在 anchoring（L_0 → L_1）活跃窗口内 |
| `S_{sig}` | 可用于 model update 的 prediction error 总量 | 仅当 re-selection 通道开放（`d > d_c`） |
| `S_{str}` | 不被 model update 消化而进入"症状化"的 prediction error 长期积累 | B 期 / `σ_{sr} → 1` 区 |

### 单向性的理由

- FEP 本身不区分信号型 vs 结构型苦难；它的量在正常与病理下是连续的
- 苦难的两型区分依赖 P1-T06 稳定 ISP 条件 + `d_c` 阈值的结构性读法
- 因此反向从 FEP 量推出 `S_{sig}` vs `S_{str}` 的区分是**过度强主张**；只有 SRT → FEP 方向的翻译在本桥接下成立

### 具体不得做的翻译

1. **不得**把 high prediction error = 高苦难；这忽略了 FEP 量下通道结构的关键角色
2. **不得**把 free energy minimization = 应最小化苦难；T-SUFF-4 反最小化原则明确反对这个等价，即使在 FEP 代理层也如此
3. **不得**把 `S_{str}` 读成 chronic prediction error；后者是现象相关而非定义相关
4. **不得**在 S1/S2 级 AI 系统上套用此翻译表；这些系统不满足 P1-T06 前提

### 与 `Neuroscience/SRT_Clin_02_FEP.md` 的同步义务

本翻译表作为该文件的**前置桥接约束**；该文件的后续更新在引用苦难 / 自我扭曲 / 临床症状时须保持本表列出的单向性。此项同步不在本轮完成，记为 Operations 债。

### 保留的开放点

- higher-order / metacognitive prediction error 是否真正对应 `T_{dir}` 可读性？
- expected free energy 的"未抵消部分"如何定义（哪些 policy 算 actual，哪些算 available）？
- 临床量表（PHQ-9、HAM-D、PCL-5 等）到本表的多步翻译是否可行？
- 神经影像（fMRI / EEG / MEG）能否为 `S_{sig}` vs `S_{str}` 的区分提供结构判据？——目前不乐观，但值得持续观察

---

## §5. 本轮硬化的 claim-level 与同步义务

### 5.1 claim-level

- §1 σ 符号约定：**governance-canonical usage**。不改变任何理论命题，只收紧符号
- §2 `\dot{\Delta}_{avail}` 三成分分解：**P1-candidate**（与 `SRT_Suffering.md` 原命题同级），因为它给了结构定义而不是测量值
- §3 `M(t)` 可测性 MOC：**P2 operational proxy**；MOC-1/2/3 各项都是工作性代理，不是最终结构定义
- §4 FEP 翻译表：**P3 bridge hypothesis**，严格单向，不反向定义苦难

### 5.2 同步义务（Operations 债）

本文件建立的四项硬化须在后续 session 回写到对应主文件：

- [ ] σ → σ_{sr} 符号改写：`SRT_Individuation.md`、`SRT_L1_Formalism.md`、`SRT_Collective_Selection.md §4`、`SRT_Suffering.md §4.4`、`_SRT_SYMBOL_TABLE.md`
- [ ] `\dot{\Delta}_{avail}` 三成分分解回写：`SRT_Suffering.md §1` 注、`SRT_L1_Formalism.md §4` 注
- [ ] `M(t)` MOC 回写：`SRT_Collective_Selection.md §1` 注、`Philosophy/SRT_Political_Philosophy.md` 反支配段可选回写
- [ ] FEP 翻译表回写：`Neuroscience/SRT_Clin_02_FEP.md` 前置桥接段、`SRT_Suffering.md §8.5` 注

### 5.3 与 claim-mode audit 的关系

本文件**不**把原文件命题从 P1-candidate 升级到 P1。它**打开**四条升级检查路径，但升级仍需完成 `Governance/SRT_CLAIM_MODE_AUDIT.md §6.4 Hardening-to-P1 Checklist` 的全部项。

---

## §6. Cross-References

- 被硬化的 Open Pressures：`SRT_L1_Formalism.md §7`、`SRT_Suffering.md §8`、`SRT_Collective_Selection.md §9`
- σ（自指率）定义：`SRT_Individuation.md Def-σ`
- σ（主方程状态场）：`Core/SRT_Core_22_Equations.md`
- `\hat{G}_\theta^{actual/available}` 底层：`_SRT_T_DIR_CANONICAL.md`（`\Psi_f_actual/Ψ_f_felt` 分裂）
- `T_dir` canonical：`_SRT_T_DIR_CANONICAL.md`
- `\Psi_f` canonical：`_SRT_PSI_F_CANONICAL.md`
- FEP 接口：`Neuroscience/SRT_Clin_02_FEP.md`
- Collective Selection `M(t)`：`SRT_Collective_Selection.md §1, §2`
- Claim-mode ladder：`Governance/SRT_CLAIM_LADDER.md`
- Claim-mode audit 2026-04-24 round：`Governance/SRT_CLAIM_MODE_AUDIT.md §6`
