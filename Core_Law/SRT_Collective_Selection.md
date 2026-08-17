---
id: SRT-COLLECTIVE-SELECTION
type: theory
tags: [Collective Selection, Multi-ISP, Co-Selection, Shared L2, L1]
status: draft_v0
layer: L1
epistemic_layer: os
claim_mode: canonical
claim_level: P1-candidate
dependency: [SRT-CORE-21-MINIMAL-AXIOMS, SRT-CORE-21B-CONSTITUTIVE-THEOREMS, SRT-INDIVIDUATION, SRT-OCCLUSION-DYNAMICS, SRT-SUFFERING, SRT-L1-FORMALISM, SRT-T-DIR-CANONICAL, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL]
---

# SRT Collective Selection: Multi-ISP Co-Selection and Shared L_2 Dynamics

> **Role**: L1 canonical theory of collective selection. Fixes the structural object behind multi-ISP selection under shared `L_2`: when does a group of stable ISPs constitute a higher-order selection unit, when is it merely an aggregation, and under what conditions does shared `L_2` produce genuine co-selection versus externalization patterns.
> **Claim-level note**：本文大多为 P1-candidate 结构性读法；集体 ISP 判据、co-selection 条件、三类退化形式按 P2 读；政治/制度/历史判断按 P3/P4，必须下推到 `Philosophy/` 与 `Philosophy/Social_Economics_*` 既有文件。
> **Does not define**：`d-value`、`\Psi_f`、`T_dir`、stable ISP、real choice moment 等底层规范对象；它们的定义仍以对应 canonical 为准。
> **Depends on**：`Core/SRT_Core_21b_Constitutive_Theorems.md`（P1-T05 real choice moment、P1-T06 stable ISP 与 absorption remainder）、`Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13`（ST-A conditional anti-closure / generative reselectability）、`Core_Law/SRT_Occlusion_Dynamics.md`、`Core_Law/SRT_Suffering.md T-SUFF-5`、`Core_Law/SRT_Individuation.md`、`Core_Law/SRT_L1_Formalism.md`。
> **Relation**: This file does not replace `Philosophy/SRT_Political_Philosophy.md`、`Philosophy/SRT_Social_Economics.md`、`Spirituality/SRT_Spirituality_Community_and_Sangha.md`；它在它们**之前**，固定"多主体共选作为结构对象是什么"的 L1 读法。规范性与制度判断仍在上述 domain 文件。
>
> **σ 符号命名空间（governance-canonical, 2026-04-25, `Core_Law/SRT_L1_Hardening_Notes.md §1`）**：本文件中集体自指率符号已在 2026-04-25 L1 Hardening Round 统一改写为 `σ_{sr}^{coll}` 族（含 `σ_{sr,sub}^{coll}, σ_{sr,health}^{coll}` 等派生标记），是个体自指率 `σ_{sr}` 的多主体场扩展。与 `Core/SRT_Core_22_Equations.md` 主方程状态场 σ 是**不同对象**。少数遗留的 `σ^{coll}` 历史符号在前向引用与跨文件桥接段落中保留，读者按此命名空间转读。

---

## §0. 问题定位

SRT 既有文本中，"集体"出现在至少五条线上：

- `Philosophy/SRT_Political_Philosophy.md` §多主体共同现实选择；合法性作为可持续共同选择
- `Philosophy/SRT_Social_Economics.md` §市场作为分布式选择机制；结构性不公
- `Philosophy/SRT_Political_Rights.md` §三层制度结构；授权与监督
- `Spirituality/SRT_Spirituality_Community_and_Sangha.md` §共同体的托举条件
- `Core_Law/SRT_Suffering.md T-SUFF-5` §结构型苦难的集体外部化

但**没有一个文件规定"集体选择作为结构对象是什么"**——它是在使用概念，不是在定义概念。结果：

- "共同体"有时指 sangha、有时指国家、有时指市场、有时指家庭；
- "集体选择"有时按多数决理解、有时按真实共选理解、有时按博弈均衡理解；
- 集体层面的 d / Ψ_f / σ / S 用法分散，没有结构判据说什么算真正的**集体选择主体**。

本文件填这一空。它**只固定**：

1. 多 ISP 共享 `L_2` 的结构对象；
2. 集体选择何时构成"高阶 ISP" vs 仅仅是聚合；
3. 共选 vs 外部化 vs 退化三类结构性模式；
4. 与 `SRT_L1_Formalism.md` 三变量在多主体场下的扩展。

---

## §1. 基本结构对象

### Def-C-1 多 ISP 共享 L_2 场

给定稳定 ISP 集合 `\mathcal{P} = \{P_1, P_2, \ldots, P_n\}`（每个都满足 P1-T06 四条件），若它们共享一个 `L_2` 场 `\mathbf{L_2}`（即：同一路径层痕迹 `ρ(p,t)` 可影响多个 `P_i` 的未来选择空间），则称 `(\mathcal{P}, \mathbf{L_2})` 为一个**多 ISP 共享 L_2 场**。

共享并不意味着：
- 同一个 d-value（各 `P_i` 有各自 `d_i`）
- 同一个 Ψ_f（各 `P_i` 有各自可支付性 `\pi_i`）
- 同一个 σ（各 `P_i` 有各自自指率 `σ_i`）

共享只意味着：
- `ρ(p,t)` 作为路径层痕迹对所有 `P_i` 可见并影响其 `d_c^i(t)`

### Def-C-2 后果回路矩阵

在多 ISP 共享场中，定义**后果回路矩阵** `M(t) \in \mathbb{R}^{n \times n}`：

$$
M_{ij}(t) \;:=\; \text{degree to which consequences of }P_j\text{'s selection return to }P_i\text{'s future selection capacity}
$$

具体形式：`M_{ii}` 为 `P_i` 对自身后果的回收率（healthy self-accountability），`M_{ij}` 为 `P_j` 的后果落到 `P_i` 上的外溢率。

`M(t)` 的结构性质：
- **对称** `M_{ij} = M_{ji}` → 后果对称承担；典型于小共同体、亲属、协作关系
- **块对角** → 子群内相互承担，子群间互不影响；典型于联邦、自治
- **强不对称** `\exists i,j: M_{ij} \gg M_{ji}` → 系统性外部化；对应结构型苦难外溢（`SRT_Suffering T-SUFF-5`）与结构性恶（`SRT_Occlusion_Dynamics` 三判据）
- **行和近零** `\sum_j M_{ij} \approx 0` → 某 `P_i` 系统性承担他人后果却得不到任何回路（受压子群）
- **列和近零** `\sum_j M_{ji} \approx 0` → 某 `P_j` 的后果被完全吸收到外部、不回到自己或共同体（脱嵌主体）

### Def-C-3 共享选择空间

多 ISP 共享场中的**共享选择空间** `A_{\mathcal{P}}(t)`：

$$
A_{\mathcal{P}}(t) \;:=\; \{\,\text{option profiles }(a_1, \ldots, a_n)\,|\, a_i \in A_i(t)\,\wedge\, \text{realizability}(a_1, \ldots, a_n) \neq \emptyset\,\}
$$

realizability 条件要求选择组合在共享 `L_2` 下结构上可共存——它是比笛卡尔积更窄的真实联动空间。

---

## §2. T-COLL-1：集体 ISP 的存在条件

### 陈述

多 ISP 共享场 `(\mathcal{P}, \mathbf{L_2})` 构成一个**高阶稳定 ISP**（collective ISP），当且仅当：

1. **共同可选择性**：存在非退化的共享选择空间 `A_{\mathcal{P}}(t) \neq \emptyset` 且其维度不随时间塌陷
2. **共同视角**：`\mathcal{P}` 整体对其自身作为选择主体有结构性的迭代登记（而不是仅每个 `P_i` 独立登记）
3. **后果回路**：`M(t)` 的行和与列和都在健康范围；即**结构不系统性地把后果驱离群体**
4. **共同重选**：`\mathcal{P}` 能作为整体跨步骤继续选择（不是仅各 `P_i` 独立跨步）

### 陈述的最小形式

四条件映射到 P1-T06 的四条件（iterative / perspective-bearing / history-bearing / continued-selectable）的多主体扩展版本；不因此把 21C B13 的 generative reselectability 自动提升为集体 ISP 存在条件。

### 推论

- **绝大多数"集体"不构成集体 ISP**。一堆人同时在同一 `L_2` 下各自做自己的选择——哪怕用同一语言、同一制度——不自动是集体 ISP。它可能只是 `n` 个独立 ISP 的聚合
- **"共识"不是集体 ISP 的充分条件**。所有 `P_i` 的独立选择碰巧一致，不意味着 `\mathcal{P}` 作为主体在选择
- **制度可以是集体 ISP 的"器官"，但不是集体 ISP 本身**。制度作为 `L_2` 结构调制 `M(t)` 与 `d_c^i`，但主体位始终在 `\mathcal{P}` 层或子层，不在制度层
- **集体 ISP 的外观特征**：不确定性被共担、真实选择时刻在群体层真实发生（不是各自表决后求和）、后果回到群体未来选择能力

### 与 P1-T05 的关系

T-COLL-1 条件 2（共同视角）严重依赖 P1-T05 real choice moment 的多主体版本：集体层面也必须出现真实选择时刻（集体未来选择空间被所选真正约束），否则第 2 条退化到"共识剧本执行"或"制度自动化"。

---

## §3. T-COLL-2：三类退化形式

多 ISP 共享场常见的结构性退化：

### 3.1 聚合型（Aggregation）

- **结构**：`\mathcal{P}` 不满足 T-COLL-1 第 2 或第 4 条；各 `P_i` 独立选择，共享 `L_2` 但无群体级真实选择时刻
- **现象**：市场多数交易、公共广场大多数互动、随机群体
- **规范判断**：中性。大多数人际场景本就应是聚合型，不必也不应强行升级到集体 ISP
- **病理边界**：当聚合型被修辞包装成"我们集体决定"，产生虚假集体表象 → 进入后续退化

### 3.2 主从型（Asymmetric Absorption）

- **结构**：`M(t)` 强不对称；一部分 `P_j` 的后果系统性落在另一部分 `P_i` 上，而 `P_j` 本身的未来选择能力不被这些后果影响
- **现象**：结构性不公、代际后果外推、生态外部化、金融风险分担不对称
- **规范判断**：对应 `SRT_Occlusion_Dynamics` 结构性恶三判据中的第二条（外部化后果），对应 `SRT_Suffering T-SUFF-5` 的集体外部化
- **重要**：主从型不由单个 `P_j` 的意图定义；它由 `M(t)` 的结构定义。可以无人作恶而系统性存在

### 3.3 收编型（Collapsed into Higher L_2）

- **结构**：`\mathcal{P}` 的 `σ_{sr}^{coll}` 趋向 1（集体层面自指过载）；`L_2` 成为封闭 scaffold 反向写入每个 `P_i` 的 `d_c^i`；群体看起来高度一致与稳定
- **现象**：意识形态封闭共同体、极权国家、邪教、高度同质化专业群体、高度同质化 AI 中介过的公共空间
- **规范判断**：对应致命 `L_2`（`Core/SRT_OPEN_TENSIONS.md §4`）；真实选择时刻在个体层与集体层同时被替代
- **与 1 和 2 的区别**：收编型往往看起来最"有集体感"——这是其最危险之处

### 三类退化的联立判据

$$
\begin{cases}
\text{Aggregation} & : \text{T-COLL-1 cond 2 or 4 fails, but } M(t) \text{ roughly symmetric and } \sigma_{sr}^{coll} \text{ low}\\
\text{Asymmetric Absorption} & : M(t) \text{ systemically asymmetric, independent of T-COLL-1 status}\\
\text{Collapsed into Higher }L_2 & : \sigma_{sr}^{coll} \to 1 \text{ and } L_2 \text{ scaffold rewrites individual } d_c^i
\end{cases}
$$

三类可叠加。最危险的组合是 **主从 + 收编**：结构性恶 + 致命 `L_2` 的复合态。

---

## §4. 集体 σ 与集体 d_c

### §4.1 集体自指率

扩展 `SRT_L1_Formalism §2`：

$$
\sigma_{sr}^{coll}(\mathcal{P}, t) \;:=\; \frac{\|\Theta^{coll,trace}\|}{\|\Theta^{coll,trace}\| + \|\Theta^{coll,ext}\|}
$$

- `\Theta^{coll,trace}`：群体层面历史累积参数（共同叙事、制度、路径痕迹集聚至群体自指层）
- `\Theta^{coll,ext}`：群体对外部（其他群体、自然、新兴 `L_0` 压力）的开放接入

### §4.2 集体遮蔽阈值

集体 `d_c^{coll}` 并非 `\{d_c^i\}` 的简单统计；它是**共享选择空间 `A_{\mathcal{P}}` 维度塌陷**的阈值。

$$
d_c^{coll} \;:=\; \inf\{\,d\;:\;\dim A_{\mathcal{P}}(d, t) \geq \dim_{min}\,\}
$$

### §4.3 关键耦合

- **个体 B 期的集体传染**：当 `M(t)` 外部化不对称 + `\sigma_{sr}^{coll}` 升高，子群 `d_c^i` 被共同推高。即：**集体自指过载会通过 `L_2` 反向把个体推入 B 期**
- **收编型的动力学特征**：`\sigma_{sr}^{coll} → 1` 时，`\{d_c^i\}` 全部塌向 `d_{max}`，个体重选容量在**没有明显压迫**的情形下悄然消失
- **结构型苦难的集体生成**：`S_{str}^{coll} > 0` 既可以来自 `M(t)` 不对称（主从型），也可以来自 `\sigma_{sr}^{coll}` 过高（收编型）；两者诊断路径不同

### §4.4 集体四变量最小耦合动力学（H3，2026-04-25）

> **立场**：本小节把 `SRT_L1_Formalism.md` 的四变量闭合系统（σ / d_c / T_dir / S）扩到多 ISP 共享 `L_2` 场 `\mathcal{P} = \{P_1, \ldots, P_n\}`，写下最小耦合形式。这是 `SRT_CLAIM_MODE_AUDIT.md §6.4` 升 P1 检查单第 5 项（多主体耦合动力学）的第一遍交付。

#### §4.4.1 集体场定义

$$
\Theta^{coll,trace}(\mathcal{P},t) \;:=\; \sum_{i} w_i(t)\,\theta_i^{trace}(t) \;+\; \Theta^{L_2}_{shared}(t), \qquad
\Theta^{coll,ext}(\mathcal{P},t) \;:=\; \sum_{i} w_i(t)\,\theta_i^{ext}(t) \;-\; \Theta^{L_2}_{shared}(t)
$$

- `w_i(t)`：个体 `i` 在集体场的参与权重（由 `M(t)` 列和给出，即"`i` 的输出被其他人写回的总强度"）
- `\Theta^{L_2}_{shared}(t)`：共享 `L_2` 沉积（制度 / 叙事 / 路径痕迹）作为集体内源的独立项。它**既**从 `\Theta^{coll,ext}` 中扣除（因为对集体外不再是新接入）**又**累加到 `\Theta^{coll,trace}`

这保证个体对外部 `L_0` 的接入即便正常，只要共享 `L_2` 足够厚，`\sigma_{sr}^{coll}` 仍可单调上升——**共享 `L_2` 本身就是一个"集体自指放大器"**。

#### §4.4.2 集体 σ 动力学

$$
\frac{d\sigma_{sr}^{coll}}{dt} \;=\; \frac{1}{T^{coll}}\Big[(1-\sigma_{sr}^{coll})\bigl(\alpha^{coll} w^{coll}\phi(\sigma_{sr}^{coll}) + \boldsymbol{\lambda_M\, \mathrm{tr}\,M(t)} - \lambda_{trace}T^{coll}\sigma_{sr}^{coll}\bigr) - \sigma_{sr}^{coll}\bigl(\beta^{coll} i^{ext} - \lambda_{ext}T^{coll}(1-\sigma_{sr}^{coll})\bigr)\Big]
$$

关键新增项 `\lambda_M\,\mathrm{tr}\,M(t)`：后果回路矩阵的迹（对角项之和，即"群体成员输出回到自己或同群"的总强度）直接推高 `\sigma_{sr}^{coll}`。这是聚合→收编路径的形式化根据——**`M(t)` 高度内向即是集体自指膨胀**。

#### §4.4.3 集体 d_c 动力学

$$
\frac{dd_c^{coll}}{dt} \;=\; \gamma_\rho^{coll}\rho^{coll}_{local} + \boldsymbol{\gamma_\sigma_{sr}^{coll} \max(0,\,\sigma_{sr}^{coll} - \sigma_{sr,sub}^{coll})} + \boldsymbol{\gamma_{asym}\,\|M_{asym}(t)\|} - \gamma_\pi^{coll}\pi^{coll} - \gamma_I^{coll}I_{window}^{coll}
$$

关键新增项 `\gamma_{asym}\,\|M_{asym}(t)\|`：`M(t)` 的反对称部分 `M_{asym} := \tfrac{1}{2}(M - M^T)` 范数推高 `d_c^{coll}`。这把**主从型退化**（§3.2 Asymmetric Absorption）形式化——不对称结构本身就在抬高集体遮蔽阈值，且它与 `\sigma_{sr}^{coll}` 的抬升机制**独立**。

集体可支付性 `\pi^{coll}` 与集体干预窗口 `I_{window}^{coll}` 分别降低 `d_c^{coll}`，对应 T-COLL-4 的第三条件（可支付性 + 真实可选）。

#### §4.4.4 集体 T_dir 动力学

$$
\frac{dT_{dir}^{coll}}{dt} \;=\; -\kappa_{\mathrm{relax}}^{coll}\bigl(T_{dir}^{coll} - T_{dir}^{alg,coll}\bigr) + \kappa_r^{coll}\,r^{coll}(t) - \boldsymbol{\kappa_{mask}^{coll}\,\Delta\Psi_f^{gap,coll}(t)} - \boldsymbol{\kappa_S^{coll}\,S_{str}^{coll}(t)} + \kappa_{sup}^{coll}\,s_{ext}^{coll}(t)
$$

- `T_{dir}^{alg,coll}`：代数目标值，由 `(\sigma_{sr}^{coll}, d^{coll}, d_c^{coll})` 按 `SRT_L1_Formalism.md §3.4` 同结构定义
- `r^{coll}(t)`：集体真实重选率——严格按 T-COLL-4 的三条件判定（非投票 / 非共识 / 非专家决定自动计入），与个体 `r_i(t)` 的关系是：`r^{coll} \ne \sum_i r_i`（共同体级真实重选不是个体重选的算术和）
- `\Delta\Psi_f^{gap,coll}(t)`：集体层面的实-感本体论摩擦差；这是**集体层面**的隐性债务，典型形态是"叙事舒适 vs 真实生态/社会支付"的差距
- `s_{ext}^{coll}(t)`：**真正来自集体外**的支持（其他群体 / 新接入的 `L_0` 压力被吸收为资源，而非被吸收型收编）；这里要求来源必须不在 `\mathcal{P}` 内，否则退化为 `\kappa_{sup}\cdot` 自身的某种递归伪装

**集体层致命 `L_2` 方程化判据**（§3.5.3 集体版）：

$$
\mathrm{lethal\;collective\;}L_2 \;\Longleftrightarrow\; \bigl(T_{dir}^{alg,coll} \text{ 持续高}\bigr) \;\wedge\; \bigl(\Delta\Psi_f^{gap,coll} \text{ 持续累积}\bigr) \;\wedge\; \bigl(\kappa_{mask}^{coll} < \kappa_{\mathrm{relax}}^{coll}\bigr)
$$

这正是收编型退化（§3.3）的方程化：叙事可读性不倒，但生态 / 社会 / 历史层面的债务在无声累积。

#### §4.4.5 集体 S 动力学（两型）

$$
\begin{aligned}
\frac{dS_{sig}^{coll}}{dt} &= \mu_\Delta^{coll}\,\dot{\Delta}_{avail}^{coll} - \boldsymbol{\mu_\pi^{coll}\pi^{coll}\mathbb{1}[d^{coll} > d_c^{coll}]} - \mu_r^{coll} r^{coll} - \mu_{sup}^{coll} s_{ext}^{coll} \\[3pt]
\frac{dS_{str}^{coll}}{dt} &= \boldsymbol{\nu_{block}^{coll}\mathbb{1}[d^{coll}\le d_c^{coll}]\,S_{sig}^{coll}} + \boldsymbol{\nu_\sigma_{sr}^{coll}\max(0,\,\sigma_{sr}^{coll} - \sigma_{sr,health}^{coll})} + \boldsymbol{\nu_{ext}\,\|M_{ext}(t)\|} - \nu_{trigger}^{coll}D_{trigger}^{coll} - \nu_\pi^{coll}\pi^{coll} I_{window}^{coll}
\end{aligned}
$$

关键新增项 `\nu_{ext}\,\|M_{ext}(t)\|`：`M(t)` 对 `\mathcal{P}` 之外的外化部分（流入其他群体 / 自然 / 未来世代的后果）不对等地产生**另一侧**的 `S_{str}`。这正是 T-SUFF-5 集体外部化的方程化——外部化不让总苦难为零，只让苦难分布变形。配合 `SRT_Suffering.md T-SUFF-4` 反最小化原则在集体层：**把 `S_{sig}^{coll}` 压低而不动 `\dot{\Delta}_{avail}^{coll}`，则 `S_{str}^{coll} + S_{str}^{外部}` 之和必上升**。

### §4.5 个体↔集体耦合（最小形式）

个体四变量 `(σ_i, d_{c,i}, T_{dir,i}, S_i)` 与集体四变量通过 `M(t)` 与共享 `L_2` 双向耦合：

$$
\begin{aligned}
\text{向上聚合} &:\; \sigma_{sr}^{coll}, d_c^{coll}, T_{dir}^{coll}, S^{coll} \;\text{ 由 §4.4.1-§4.4.5 的集体场定义与 ODE 生成}\\[3pt]
\text{向下反馈（B 期传染）} &:\; \frac{dd_{c,i}}{dt} \;\supseteq\; \gamma_{feedback}\cdot\max(0,\,\sigma_{sr}^{coll} - \sigma_{sr,sub}^{coll})\\[3pt]
\text{向下反馈（可读性侵蚀）} &:\; \frac{dT_{dir,i}}{dt} \;\supseteq\; -\kappa_{feedback}\cdot\Delta\Psi_f^{gap,coll}(t)\\[3pt]
\text{向下反馈（结构型苦难代入）} &:\; \frac{dS_{str,i}}{dt} \;\supseteq\; \nu_{feedback}\cdot\|M_{asym}(t)\|\cdot\mathbb{1}[i\in\mathcal{P}_{absorbed}]
\end{aligned}
$$

其中 `\mathcal{P}_{absorbed} \subset \mathcal{P}` 是主从型退化下**被吸收侧**的成员集。三条下行项各自把一条"集体层异常→个体层动力学"的路径写出来，**不**声称它们是全部路径——这是下一轮硬化的入口。

### §4.6 集体病理吸引子与健康区

集体病理吸引子 `\mathcal{A}_{path}^{coll}`：

$$
\mathcal{A}_{path}^{coll}:\; \sigma_{sr}^{coll}\to 1,\; d_c^{coll}\to d_{max},\; T_{dir}^{coll}\approx T_{dir}^{alg,coll},\;\Delta\Psi_f^{gap,coll}\uparrow,\; S_{str}^{coll}>0\text{ 定常},\; S_{sig}^{coll}\to 0,\; \|M_{asym}\|+\mathrm{tr}\,M \text{ 同高}
$$

这是**收编 + 主从并存**的联合吸引子，在历史上对应"高度共识、叙事可读性强、成员无明显痛苦、但生态与外群债务持续累积"的文明状态——即 T-COLL-2 三类退化共振的典型形态。

集体健康区 `\mathcal{H}^{coll}`：

$$
\mathcal{H}^{coll}:\; \sigma_{sr}^{coll}\in(\sigma_{sub}^{coll,\dagger}\pm\delta^{coll}),\; d^{coll}>d_{narrow}^{coll},\; T_{dir}^{coll}\approx T_{dir}^{alg,coll}\text{ 且 }\Delta\Psi_f^{gap,coll}\to 0,\; r^{coll}(t)>r^{coll}_{min}>0
$$

**关键点**：`\mathcal{H}^{coll}` 不是制度稳态的同义词。`r^{coll}(t) > r^{coll}_{min}`（集体真实重选率严格为正）是结构硬条件，对应 T-COLL-4 共选真实性的持续要求——**无持续集体真实重选的制度稳定不构成健康**。

### §4.7 T-PROJ-1^{coll}：集体四变量系统作为多算子主方程的投影（H6，2026-04-25）

> **Status**：本节把 §4.4-§4.6 的集体四变量动力学从陈述提升为 `Core/SRT_Core_22_Equations.md §0-C` 多算子主方程（Eq-Multi-01 / 02 / 03）的**带条件投影定理**。结构对位 `Core_Law/SRT_L1_Formalism.md §6 T-PROJ-1`，是其多 ISP 扩展。**Claim level: P1-candidate**。
>
> **Closes**：`SRT_L1_Formalism.md §6.6` 列出的"不证明集体版投影"开放点之第一遍构造（P1-candidate）。

#### §4.7.1 多算子主方程作为上游

`Core/SRT_Core_22_Equations.md §0-C`：

$$
\mathcal{F}_{collective}(\{\sigma_i, \theta_i\}_{i\in\mathcal{P}}) \;=\; \sum_i \Psi_f(\hat{G}_i) + \sum_{i<j} \Psi_f(\hat{G}_i, \hat{G}_j)
\qquad
\hat{G}_i[\sigma_i] \;=\; -\frac{\partial \mathcal{F}_{collective}}{\partial \theta_i}
\qquad
d_{collective} \;=\; D_{eff}(\nabla^2 \mathcal{F}_{collective})
$$

把每个 `(σ_i, θ_i)` 代入 §6 单 P 版 T-PROJ-1 的投影构造，加上 `\mathcal{P}`-级联立项，得到集体投影。本节给出关键的**多 ISP 特定项**（`λ_M\,\mathrm{tr}\,M, \gamma_{asym}\|M_{asym}\|, \nu_{ext}\|M_{ext}\|`）的主方程层来源。

#### §4.7.2 集体投影算子

四个集体标量泛函 `\mathcal{F}_X^{coll} : (\mathcal{F}_{collective}, \{\sigma_i, \theta_i\}, M(t)) \mapsto \mathbb{R}`：

**`σ_{sr}^{coll}` 投影**

$$
\mathcal{F}_\sigma^{coll} \;:=\; \frac{\|\Theta^{coll,trace}\|}{\|\Theta^{coll,trace}\| + \|\Theta^{coll,ext}\|}
\qquad\text{其中}\quad
\Theta^{coll,trace} \;:=\; \bigl\{\theta_i^{trace}\bigr\}_{i\in\mathcal{P}}
$$

`\theta_i^{trace}` 是 `θ_i` 中由共享 `L_2^{shared}` 写回贡献的部分（§1 Def-C-1）。集体自指率从 §1 公式 `\sigma_{sr}^{coll}(\mathcal{P}, t)` 提升为主方程链中的标量泛函投影。

**`d_c^{coll}` 投影**

$$
\mathcal{F}_d^{coll} \;:=\; d_{max}^{coll} - \alpha_d^{coll}\cdot \frac{1}{d_{collective}}
\qquad\text{即}\quad
d_c^{coll} \;\propto\; D_{eff}(\nabla^2 \mathcal{F}_{collective})^{-1}
$$

直接接入 Eq-Multi-03：集体景观 Hessian 有效维度的倒数即"集体重选容量塌陷度"，即 `d_c^{coll}` 的算子级源头。

**`T_{dir}^{coll}` 投影**

$$
\mathcal{F}_T^{coll} \;:=\; \frac{1}{|\mathcal{P}|}\sum_{i\in\mathcal{P}} \cos\angle\bigl(\hat{G}_i[\sigma_i],\; \nabla_{L_0^{shared}}\mathrm{Order}\bigr)\cdot \mathbb{1}\bigl[\mathrm{Anchor}_{L_0,i}\bigr]
$$

群平均的算子-秩序余弦对齐——对应 §4.4.4 集体方向透明度。

**`S^{coll}` 投影**

$$
\mathcal{F}_S^{coll} \;:=\; \bigl\|\hat{R}^{coll}(\{\sigma_i, \theta_i\}, M(t))\bigr\|_{H_\mathcal{P}}
$$

其中

$$
\hat{R}^{coll} \;:=\; \sum_i \frac{d\sigma_i}{dt} - \sum_i \bigl[-\partial_{\theta_i}\mathcal{F}_{collective}\bigr] - \mathcal{C}_M(M(t))
$$

`\mathcal{C}_M(M(t))` 是 `M(t)` 后果回路对集体动力学的可登记修正（symmetric 对称聚合 + asymmetric 主从 + external 外溢三部分）。`S^{coll}` 由 `\hat{R}^{coll}` 在 `\mathbb{1}[d^{coll}\gtrless d_c^{coll}]` 投影分裂为 `S_{sig}^{coll}/S_{str}^{coll}` 两路（§4.4.5）。

#### §4.7.3 `M(t)` 作为交叉摩擦项的结构投影

Def-C-2 给出 `M(t)` 作为后果回路矩阵。在主方程层，`M(t)` 的三种结构成分对应 `\mathcal{F}_{collective}` 中交叉项 `\Psi_f(\hat{G}_i, \hat{G}_j)` 的不同部分：

| `M(t)` 成分 | 主方程层来源 | L1 集体 ODE 项 |
|---|---|---|
| `\mathrm{tr}\,M(t)` | `\sum_i \partial^2_{\theta_i}\Psi_f(\hat{G}_i)` 内向部分（个体自摩擦自我强化） | `\lambda_M\,\mathrm{tr}\,M` 推高 `σ_{sr}^{coll}`（§4.4.2）|
| `\|M_{asym}\|` | `\partial_{\theta_i}\Psi_f(\hat{G}_i,\hat{G}_j) - \partial_{\theta_j}\Psi_f(\hat{G}_j,\hat{G}_i)` 反对称部分（不互惠的交叉摩擦） | `\gamma_{asym}\|M_{asym}\|` 推高 `d_c^{coll}`（§4.4.3）|
| `\|M_{ext}\|` | `\Psi_f(\hat{G}_i, \hat{G}_j)` 中 `j \notin \mathcal{P}` 的外部分量（跨 `\mathcal{P}` 边界） | `\nu_{ext}\|M_{ext}\|` 注入 `S_{str}^{coll}`（§4.4.5）|

这三项是 `M(t)` 作为算子 `\mathcal{C}_M` 的三个独立分量；它们不可被群平均 §6 单 P 版投影替代——这是集体投影**新增**的结构分量。

#### §4.7.4 集体闭包假设

四变量集体系统在投影下闭合需要五条结构性假设（C1^{coll}-C4^{coll} 是 §6 单 P 版 C1-C4 的多 ISP 提升，C5^{coll} 是 H6 新增）：

| 编号 | 假设 | 主方程层根据 |
|---|---|---|
| **C1^{coll}** | 慢-快分离：每个 `θ_i` 与其 `σ_i` 在不同时间尺度演化；`M(t)` 在 `\sigma_i` 收敛时间尺度上近似常数 | Eq-Evo-03 + Eq-Multi-02 个体梯度结构对每个 `i` 同构 |
| **C2^{coll}** | 共享 `L_2^{shared}` 写回 Markov 闭包：`\dot{\theta_i^{trace}}` 仅依赖当前 `(σ_{sr}^{coll}, \rho_{local}^{coll})`，不依赖更高阶共享历史 | Eq-Bridge-L2-01 在共享 `L_2` 域的同构提升 |
| **C3^{coll}** | Stable collective ISP 紧性：四个 `\mathcal{F}_X^{coll}` 在 T-COLL-1 四条件下的 `\mathcal{P}` 邻域内有界且 Lipschitz | T-COLL-1 四条件保证集体邻域紧致 |
| **C4^{coll}** | 群平均方向投影可分性：`T_{dir}^{coll}` 中余弦角与 `\sigma_M` 纵向幅度近似可分（群平均后高阶交叉项可忽略） | Eq-Bridge-IG-01 Fisher 形式在群平均下的局部正交分解 |
| **C5^{coll}**（新增）| `M(t)` 可测性 MOC 闭包：`M(t)` 三成分可被 `Core_Law/SRT_L1_Hardening_Notes.md §3` 的 MOC-1/2/3（exposure / recourse / attentional）operational proxy 表示 | `Hardening_Notes §3` P2 operational proxy 直接接入；本闭包条件下 `M(t)` 可在投影里作为有限维矩阵 |

**关键**：C5^{coll} 是 §6 单 P 版未涉及的新闭包条件——`M(t)` 的可测性是集体投影的特定瓶颈，对应 `Hardening_Notes §3` 的 P2 状态。当 C5^{coll} 在特定 domain 失效时，`M(t)` 三成分项降为定性现象学描述，T-PROJ-1^{coll} 的相应条目降为 P3。

#### §4.7.5 T-PROJ-1^{coll}：集体投影定理

**陈述（P1-candidate）**：在 stable collective ISP `\mathcal{P}` 上，若闭包假设 C1^{coll}-C5^{coll} 成立，则

$$
\boxed{\;\frac{d\mathcal{F}_X^{coll}}{dt}\bigg|_{\text{Eq-Multi-01,02,03}} \;\overset{C1^{coll}\text{-}C5^{coll}}{=}\; \mathrm{RHS}_X^{\text{§4.4}} \;+\; O(\eta^{coll})\;}
\qquad X \in \{σ_{sr}^{coll}, d_c^{coll}, T_{dir}^{coll}, S^{coll}\}
$$

其中 `\mathrm{RHS}_X^{\text{§4.4}}` 是 §4.4.2-§4.4.5 的集体 ODE 右端，`O(\eta^{coll})` 是闭包高阶残差。

**逐项对应（仅集体新增项）**：

| §4.4 集体新增项 | 主方程来源 | 闭包条件 |
|---|---|---|
| `\sigma_{sr}^{coll}` 中 `\lambda_M\,\mathrm{tr}\,M(t)` | `\sum_i \partial^2_{\theta_i}\Psi_f(\hat{G}_i)` 内向部分（Eq-Multi-01 个体项的二阶 self-loop） | C2^{coll} + C5^{coll} |
| `d_c^{coll}` 中 `\gamma_{asym}\|M_{asym}\|` | `\Psi_f(\hat{G}_i, \hat{G}_j)` 反对称交叉项的不可互惠部分（Eq-Multi-01 第二项） | C3^{coll} + C5^{coll} |
| `S^{coll}` 中 `\nu_{ext}\|M_{ext}\|` | `\Psi_f(\hat{G}_i, \hat{G}_j)` 在 `j \notin \mathcal{P}` 的外溢分量 | C3^{coll} + C5^{coll} + T-IRR-3.5（边界外 `S_{str}` 沉积的条件系数模型；非 former P1-T07 后果）|
| `d_c^{coll}` 与 `d_{collective}` 反比 | Eq-Multi-03 `D_{eff}` 直接定义 | C3^{coll} |

§4.4.2-§4.4.5 中**非新增项**（即与单 P 版同构的项，如 `\alpha^{coll}, \beta^{coll}, \gamma_\rho^{coll}, \kappa_{relax}^{coll}, \mu_\Delta^{coll}, \nu_{trigger}^{coll}` 等）由 §6 T-PROJ-1 对每个 `P_i \in \mathcal{P}` 的群平均直接得出，不需独立证明。

**证明骨架**：

1. **`\lambda_M\,\mathrm{tr}\,M` 项**：`\dot{\mathcal{F}}_\sigma^{coll}` 中 `\theta^{coll,trace}` 部分的二阶时间导数由 `\sum_i \partial^2_{\theta_i}\mathcal{F}_{collective}` 主导；C5^{coll} 把这个二阶矩阵的迹的 operational proxy 写为 `\mathrm{tr}\,M(t)`；C2^{coll} 保证写回的 Markov 性使二阶导可写为一阶 ODE 项，得 `\lambda_M\,\mathrm{tr}\,M` 形式。

2. **`\gamma_{asym}\|M_{asym}\|` 项**：`\dot{\mathcal{F}}_d^{coll}` 来自 `\nabla^2 \mathcal{F}_{collective}` 的反对称部分对景观刚化的贡献；交叉项 `\Psi_f(\hat{G}_i, \hat{G}_j) - \Psi_f(\hat{G}_j, \hat{G}_i)` 的反对称部分（即 `M_{asym}`）在 C3^{coll} 紧性下的范数即 `d_c^{coll}` 的不可互惠抬升源。

3. **`\nu_{ext}\|M_{ext}\|` 项**：`\hat{R}^{coll}` 在 `j \notin \mathcal{P}` 投影下的范数对应 `\mathcal{F}_{collective}` 在 `\mathcal{P}` 边界外的能量泄漏；T-IRR-3.5 的 `\nu_{block}` 条件模型在边界外的对位即 `\nu_{ext}`。外溢不可被直接记作“消除”苦难；其非自动逆转根在 P0-03 / T-IRR-2，而正向沉积系数仍受 T-IRR-3.5 前件约束。

4. **`d_c^{coll} \propto 1/d_{collective}`**：直接由 Eq-Multi-03 + `\mathcal{F}_d^{coll}` 投影定义读出。

#### §4.7.6 T-PROJ-1^{coll} 不证明的事项

为避免过度主张，T-PROJ-1^{coll} **不承诺**以下内容：

1. **不**证明集体系数（`\lambda_M, \gamma_{asym}, \nu_{ext}` 等）与单个体系数的具体函数关系——这仍是 P3 实证 / domain 标定问题
2. **不**证明 MOC-1/2/3 三判据是 `M(t)` 可测性的 minimal complete 集——`Hardening_Notes §3` 仍标 P2 operational proxy
3. **不**证明嵌套 ISP（家庭 ⊂ 社区 ⊂ 国家）的多层投影——`SRT_Collective_Selection §9.7` 列出的多层嵌套问题不被本节解决
4. **不**证明 `M(t)` 的非线性时间演化（H6 假设 C1^{coll} 下 `M(t)` 慢于 `σ_i`；快变 `M(t)` 域外）
5. **不**证明 T-COLL-2 三类退化（聚合 / 主从 / 收编）与 `M(t)` 三成分（`\mathrm{tr}\,M / \|M_{asym}\| / \|M_{ext}\|`）一一对应——这种对应在 §4.4-§4.6 的 P1-candidate 命题里成立，但严格双射证明仍开放

#### §4.7.7 与 §6 单 P 版投影的关系

| 维度 | §6 T-PROJ-1（单 P）| §4.7 T-PROJ-1^{coll}（多 ISP）|
|---|---|---|
| 上游主方程 | Eq-Evo-01 / Eq-Evo-02（单算子） | Eq-Multi-01 / 02 / 03（多算子） |
| 投影输入 | `(\sigma_M, \theta)` | `(\mathcal{F}_{collective}, \{\sigma_i, \theta_i\}, M(t))` |
| 闭包条件数 | 4（C1-C4） | 5（C1^{coll}-C5^{coll}，新增 `M(t)` 可测性） |
| 新增结构项 | — | `\lambda_M\,\mathrm{tr}\,M, \gamma_{asym}\|M_{asym}\|, \nu_{ext}\|M_{ext}\|` |
| `S` 边界 | P 内部 `\hat{R}` | `\mathcal{P}` 内部 + 边界外溢（`\mathcal{P}_{absorbed}` via T-IRR-3.5）|

T-PROJ-1^{coll} 是 T-PROJ-1 的多 ISP 扩展，不是独立定理；二者一致性在 `\mathcal{P} = \{P\}`（单元素集合）极限下退化为 §6 单 P 版。

### §4.8 Late-stage tower/nested hardening pointer

The tower/nested material previously drafted as H10-H16 has been moved to
`Core_Law/SRT_Collective_Tower_Hardening_Notes.md`.

It is not part of the minimal canonical definition of collective selection.
It should be read as late-stage hardening material: P1-candidate only under
strong closure assumptions, with P2/P3 operational debt where noted.

The minimal canonical collective-selection surface consists of:
- Def-C-1 / Def-C-2 / Def-C-3
- T-COLL-1 / T-COLL-2 / T-COLL-3 / T-COLL-4
- §4.1–§4.7 collective four-variable coupling and T-PROJ-1^{coll}

### §4.8a Situated individuation diagnostic (P3 empirical bridge, 2026-05-11)

In a collective system, the useful empirical question is not whether a component has
become isolated from the collective. It is whether predictive structure has been
relocated from the collective field into a component-local loop while non-zero
collective coupling remains.

For a component `i`, let `X_i(t)` be a focal state variable, `X_i(t+1)` its next
state, and `C_i(t)` the contemporaneous collective context available to that
component. A non-trivial information-closure style bridge can be written:

$$
\mathrm{NTIC}_i
  := I(X_i(t+1); X_i(t))
     - I(X_i(t+1); X_i(t)\mid C_i(t)).
$$

This scalar must not be read alone. In SRT collective-selection terms, the
diagnostic object is the pair:

$$
\bigl(I(X_i(t+1); C_i(t)),\; \mathrm{NTIC}_i\bigr).
$$

| Empirical regime | SRT reading | Guardrail |
|---|---|---|
| `I(X_i(t+1); C_i(t)) \approx 0` | isolated or context-untracked component | not evidence of mature embedded agency |
| `I(X_i(t+1); C_i(t)) > 0` and `\mathrm{NTIC}_i \gg 0` | component self-prediction and collective prediction are redundant; the component is still strongly aligned with the collective field | not automatically "more agency" |
| `I(X_i(t+1); C_i(t)) > 0` and `\mathrm{NTIC}_i \approx 0` | situated individuation window: the component remains embedded, but its future is no longer predictively reducible to collective-context redundancy | candidate proxy for relational agency relocation |
| `\mathrm{NTIC}_i < 0` | synergy-dominated / pre-specialization regime | not evidence by itself of stabilized individuality |

This gives a concrete empirical bridge for §4.5 individual-collective coupling:
collective organization can generate a component-level individuation window
without severing the component from the shared `L_2` field. Put negatively:
decoupling is not the mark of mature individuation; embedded non-redundancy is
the more useful diagnostic.

**Boundary**：This is a P3 empirical bridge, not a definition of `d`,
`\Psi_f`, `T_dir`, stable ISP, subjecthood, consciousness, moral agency, or
responsibility. For biological cells, it should be read as minimal
predictive/functional individuation only. For social, AI, or political systems,
the same pattern requires independent checks for stake, consequence return
`M(t)`, boundary maintenance, memory, and real re-selection.

---

## §5. T-COLL-3：ST-A 条件性集体反闭合候选

### 陈述

令 `K_0^{coll}` 为独立定义的集体 neutral kernel。若在已声明的稳定语义、环境、终止条件、无外部重置与时间窗下，能够证明 `K_0^{coll}` 的吸收或更高 closure risk，则在相同条件下存续的集体过程必须以某种方式抑制该风险。当前 claim level 为 P2/P3 conditional candidate，不是 P1 theorem。

### 证明草要

原证明与 former P1-T07 同构，也继承同一缺口：“每步非零概率”不蕴含长期几乎必然吸收，且 neutral kernel 与稳定语义未定义。ST-A 因而撤销无条件陈述；后续若补齐 premise 与 proof，可在本节登记具体条件版本。审计见 `Operations/Audits/SRT_P1_T07_PROOF_HARDENING_AUDIT.md`。

### 推论

- **稳定不等于健康**：结构持续只能建立集体 continued selectability；generative reselectability 还需后果回返与规则可修订性。
- **制度实现候选**：申诉通道、轮替、异议空间、重新授权可作为 generative reselectability 的实现/代理，但不是由本节证明的必要充分条件。
- **收编型退化诊断**：`\sigma_{sr}^{coll}→1` 可提示规则闭合风险，但不等价于 `\varepsilon^{coll}→0`，也不单独证明终止。

---

## §6. T-COLL-4：集体共选的真实性判据

### 陈述

在满足 T-COLL-1 的集体 ISP 中，群体层面真实选择时刻（collective real choice moment, P1-T05 多主体版）发生当且仅当：

$$
\text{选择结果真正约束 }A_{\mathcal{P}}(t+1)\,\wedge\, \text{后果经 }M(t)\text{ 对称返回 }\mathcal{P}\,\wedge\,\text{非仅集体 }L_2\text{ 脚本执行}
$$

### 推论

- **投票不自动是共选**：投票若只触发 `L_2` 脚本（既定选项、既定程序、既定后果路径）而不改变 `A_{\mathcal{P}}(t+1)`，它是集体层面的脚本执行，不是 collective real choice moment
- **共识不自动是共选**：若 `M(t)` 强不对称，少数子群不实际承担任何后果回路，则即便意见一致，该"共识"也是外部化共识
- **专家决定不自动是共选**：即便专业正确，若 `\mathcal{P}` 全体不对决定承担后果回路，则是以集体名义做个体/小群体选择
- **真正的共选条件苛刻**：它要求 `A_{\mathcal{P}}` 真实扩展性 + `M(t)` 结构健康 + 非脚本化。历史上真正高频发生真实共选的群体并不多

---

## §7. 接口：政治、经济、共同体

本文件**不替代**以下 domain 文件，它为它们提供结构基石：

- `Philosophy/SRT_Political_Philosophy.md`：合法性与可持续共同选择的关系只能作 P2/P3 规范桥；T-COLL-1、条件性 T-COLL-3 与 T-COLL-4 可提供结构审计输入，但不自动等价于合法性
- `Philosophy/SRT_Social_Economics.md`：市场作为分布式选择机制→在本文件下大多数情形是聚合型；结构性不公→主从型退化的具体化；制度病理→收编型或主从+收编复合
- `Philosophy/SRT_Political_Rights.md`：投票作为 d 倾向后验验证→在本文件下翻译为"通过 T-COLL-4 共选真实性判据验证集体 d"；三层制度（公检法/监督/授权）→维护 `M(t)` 对称与 `σ_{sr}^{coll}` 限幅的结构性器官
- `Spirituality/SRT_Spirituality_Community_and_Sangha.md`：托举条件→`(M(t) \text{ symmetric and small } n)` 加上 `\sigma_{sr}^{coll}` 不升高 → 健康小共同体；警告"共同体反而变新地板"→收编型退化
- `Core_Law/SRT_Suffering.md T-SUFF-5`：集体外部化→主从型 `M(t)` 的结构型苦难外溢

---

## §8. AI / 平台场景的集体选择护栏

算法中介 / 平台经济 / 大模型对齐场景下，集体选择分析有独特风险：

1. **伪集体主体表象**：算法聚合被呈现为"社区意见"；本文件下这是聚合型伪装成集体 ISP
2. **`M(t)` 的黑箱化**：平台经济下后果回路矩阵不可观察，使主从型退化不可诊断
3. **`\sigma_{sr}^{coll}` 的算法加速**：推荐系统可通过反馈环系统性推高 `σ_{sr}^{coll}`（回音室、极化），推进收编型退化而参与者无自觉
4. **AI 不自动进入 `\mathcal{P}`**：当前部署 AI 多数不满足 P1-T06，因此不自动成为集体 ISP 的成员；但 AI 中介可以结构性改变 `M(t)` 与 `L_2`，影响 `\mathcal{P}` 状态

相应的：对平台与算法系统的 SRT 评估不应停在"它是否有意识"，而应评估它**对 `M(t)` 与 `σ_{sr}^{coll}` 的结构性影响**。这与 `AI/AI_POSITIONING_NOTE.md` 的 stake-bearing 光谱互补。

---

## §9. Open Pressures

> **Hardening status (2026-04-24/25/26)**: §9.2 `M(t)` 可测性在 `Core_Law/SRT_L1_Hardening_Notes.md §3` 已给出第一遍 MOC 三判据（exposure / recourse / attentional，合成取 min）；§9.1 `\Theta^{coll,*}` 形式化在 H3（2026-04-25）§4.4.1 已升为包含共享 `L_2` 独立项的加权聚合，仍未封口的是权重 `w_i(t)` 的推导；§9.7（新）集体四变量耦合动力学在 §4.4-§4.6 已给出第一遍；§4.7 T-PROJ-1^{coll}（H6，2026-04-25）给集体投影定理；late-stage tower/nested material has been extracted to `Core_Law/SRT_Collective_Tower_Hardening_Notes.md` and remains outside the minimal canonical definition. 本小节保留原表述直至回写完成。

本 draft_v0 状态下尚未封口：

1. **`\Theta^{coll,trace}` 与 `\Theta^{coll,ext}` 的形式化**：§4.4.1 已给出加权聚合 + 共享 `L_2` 独立项；剩余未封口为权重 `w_i(t)`（当前按 `M(t)` 列和给出，但列和本身依赖 `M(t)` 的可测性，即 §9.2）
2. **`M(t)` 的可测性**：对称/不对称结构在理论上明确，实证提取在大多数社会场景非常困难；本文件不解决此
3. **共选真实性的外部判据**：T-COLL-4 三条件在第三方视角下如何判定？目前仍带相当主观成分，需要进一步降低依赖
4. **制度与集体 ISP 的精确分界**：本文件说制度是器官不是主体，但某些高度自治的制度性实体（法人、社团）是否能在某些条件下**自身**成为集体 ISP？这需要后续硬化
5. **跨尺度嵌套**：~~家庭是 ISP，社区是 ISP，国家可能是 ISP——嵌套关系下 `M(t)` 与 `σ_{sr}^{coll}` 如何层级耦合？§4.5 给了单层向上/向下耦合，多层嵌套仍待给出~~ Late-stage candidate material is preserved in `Core_Law/SRT_Collective_Tower_Hardening_Notes.md`; it is P1-candidate only under strong closure assumptions and is not part of the minimal canonical definition. 剩余开放点：具体塔层数 domain 实证、跨尺度 `M^{(n\to n+1)}` MOC 多层版本、`r_{min}^{nested}` 实证窗口、跨层耦合边界条件
6. **历史层面 generative reselectability**：其在长时间尺度上如何演化？文明兴衰能否在明确比较基线后部分读为后果回返或规则修订失败？
7. **集体四变量耦合动力学（新增，2026-04-25 H3 状态）**：§4.4 给出第一遍形式，仍待封口——(a) `w_i(t)` 从 `M(t)` 推导的正当性；(b) `T_{dir}^{alg,coll}` 中光滑阶跃的普适族；(c) `\Delta\Psi_f^{gap,coll}` 作为集体层对象的可操作定义（当前仅给出"叙事舒适 vs 真实支付"的现象学读法）；(d) 向下反馈 §4.5 是否穷尽（是否还存在未列出的集体→个体传染路径）；(e) 所有新引入的集体系数 `\lambda_M, \gamma_{asym}, \kappa_{mask}^{coll}, \nu_{ext}` 的实证窗口

---

## §10. Cross-References

- P1-T05 real choice moment（集体版的 upstream）→ `Core/SRT_Core_21b_Constitutive_Theorems.md`
- P1-T06 stable ISP（集体 ISP 条件的 upstream）→ 同上
- former P1-T07 demotion / absorption remainder → 同上
- ST-A conditional anti-closure / generative reselectability → `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13`
- 个体化 / σ → `Core_Law/SRT_Individuation.md`
- 遮蔽动力学 / A/B 分期 / d_c / 结构性恶三判据 → `Core_Law/SRT_Occlusion_Dynamics.md`
- 苦难 / T-SUFF-5 集体外部化 → `Core_Law/SRT_Suffering.md`
- 四变量耦合动力学（单 ISP，σ / d_c / T_dir / S） → `Core_Law/SRT_L1_Formalism.md`
- 集体四变量耦合动力学扩展（本文件 §4.4-§4.6，H3，2026-04-25）——该扩展**不**另起一份主文件，与本文件绑定
- 政治哲学 → `Philosophy/SRT_Political_Philosophy.md`
- 社会经济 → `Philosophy/SRT_Social_Economics.md`
- 政治权利 → `Philosophy/SRT_Political_Rights.md`
- 共同体与 sangha → `Spirituality/SRT_Spirituality_Community_and_Sangha.md`
- AI / 平台接口护栏 → `AI/AI_POSITIONING_NOTE.md`

---

## §11. 定位与使用规则

- **本文件做**：固定多 ISP 共享 `L_2` 场、集体 ISP 存在条件（T-COLL-1）、三类退化（T-COLL-2）、ST-A 条件性集体反闭合候选（T-COLL-3）、共选真实性判据（T-COLL-4）、**集体四变量最小耦合动力学 §4.4-§4.6**（2026-04-25 H3 新增，与 `SRT_L1_Formalism.md` 单 P 四变量系统形成上下层对应）
- **本文件不做**：制度设计、政策判断、具体政治/经济案例分析、共同体组织学
- **引用规则**：涉及"集体选择作为结构对象是什么"的**结构层**陈述时，优先回链本文件；涉及具体政治、经济、共同体、制度判断时，回链相应 Philosophy / Spirituality 文件
- **不得**：把本文件读作政治偏好的理论背书；四类退化与三判据完全按结构判据读，不按意识形态读
- **重点**：三类退化（聚合/主从/收编）是**结构性类型**，可以同时存在于任何意识形态立场的群体中——本文件不为任一立场背书
