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
> **Depends on**：`Core/SRT_Core_21b_Constitutive_Theorems.md`（P1-T05 real choice moment、P1-T06 stable ISP、P1-T07 ε 反闭合）、`Core_Law/SRT_Occlusion_Dynamics.md`、`Core_Law/SRT_Suffering.md T-SUFF-5`、`Core_Law/SRT_Individuation.md`、`Core_Law/SRT_L1_Formalism.md`。
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

四条件映射到 P1-T06 的四条件（iterative / perspective-bearing / history-bearing / re-selectable）的多主体扩展版本。

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
| `S^{coll}` 中 `\nu_{ext}\|M_{ext}\|` | `\Psi_f(\hat{G}_i, \hat{G}_j)` 在 `j \notin \mathcal{P}` 的外溢分量 | C3^{coll} + C5^{coll} + T-IRR-3.5（边界外的 `S_{str}` 沉积仍由 P1-T07 hierarchy 控制）|
| `d_c^{coll}` 与 `d_{collective}` 反比 | Eq-Multi-03 `D_{eff}` 直接定义 | C3^{coll} |

§4.4.2-§4.4.5 中**非新增项**（即与单 P 版同构的项，如 `\alpha^{coll}, \beta^{coll}, \gamma_\rho^{coll}, \kappa_{relax}^{coll}, \mu_\Delta^{coll}, \nu_{trigger}^{coll}` 等）由 §6 T-PROJ-1 对每个 `P_i \in \mathcal{P}` 的群平均直接得出，不需独立证明。

**证明骨架**：

1. **`\lambda_M\,\mathrm{tr}\,M` 项**：`\dot{\mathcal{F}}_\sigma^{coll}` 中 `\theta^{coll,trace}` 部分的二阶时间导数由 `\sum_i \partial^2_{\theta_i}\mathcal{F}_{collective}` 主导；C5^{coll} 把这个二阶矩阵的迹的 operational proxy 写为 `\mathrm{tr}\,M(t)`；C2^{coll} 保证写回的 Markov 性使二阶导可写为一阶 ODE 项，得 `\lambda_M\,\mathrm{tr}\,M` 形式。

2. **`\gamma_{asym}\|M_{asym}\|` 项**：`\dot{\mathcal{F}}_d^{coll}` 来自 `\nabla^2 \mathcal{F}_{collective}` 的反对称部分对景观刚化的贡献；交叉项 `\Psi_f(\hat{G}_i, \hat{G}_j) - \Psi_f(\hat{G}_j, \hat{G}_i)` 的反对称部分（即 `M_{asym}`）在 C3^{coll} 紧性下的范数即 `d_c^{coll}` 的不可互惠抬升源。

3. **`\nu_{ext}\|M_{ext}\|` 项**：`\hat{R}^{coll}` 在 `j \notin \mathcal{P}` 投影下的范数对应 `\mathcal{F}_{collective}` 在 `\mathcal{P}` 边界外的能量泄漏；T-IRR-3.5 的 `\nu_{block}` 算子级表达式在边界外的对位即 `\nu_{ext}`，使外溢的 `S_{str}^{coll}` 沉积的非守恒方向性继续由 P1-T07 hierarchy 控制（即外溢不是"消除"苦难，是把它转给 `\mathcal{P}_{absorbed}`）。

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

### §4.8 T-PROJ-1^{coll,nested}：嵌套 ISP 多层投影（H10，2026-04-26）

> **Status**：本节把 §4.7 单层 T-PROJ-1^{coll} 扩展到多层嵌套 ISP 结构（家庭 ⊂ 社区 ⊂ 国家、个体 ⊂ sangha ⊂ 教派、ISP 团队 ⊂ 部门 ⊂ 公司等），给出**递归投影定理**。**Claim level: P1-candidate**。
>
> **Closes**：§9.7 列出的"跨尺度嵌套：多层嵌套仍待给出"开放点。

#### §4.8.1 多层嵌套结构

定义层级 ISP 塔（**hierarchical ISP tower**）：

$$
\mathcal{P}^{(0)} \;:=\; \{P_i\}_i \quad\text{（个体 ISP 集合，单 P 层）}
$$
$$
\mathcal{P}^{(n+1)} \;:=\; \bigl\{\mathcal{P}^{(n),k}\bigr\}_{k} \quad\text{（每个层 }n+1\text{ 元素都是层 }n\text{ 的一个集体 ISP）}
$$

要求每层 `\mathcal{P}^{(n),k}` 满足该层的 **T-COLL-1 集体 ISP 条件**（即每层的"集体 ISP"本身是有效的——见 §2 集体 ISP 存在四条件，递归应用到每层）。

**示例塔**（不要求穷尽，但本节定理对任何满足层级 T-COLL-1 的塔成立）：

| 层 | 实例 1：家族 / 社区 / 国家 | 实例 2：个体 / sangha / 教派 | 实例 3：员工 / 部门 / 公司 |
|---|---|---|---|
| `\mathcal{P}^{(0)}` | 个体成员 | 个体修行者 | 员工 |
| `\mathcal{P}^{(1)}` | 家庭 | sangha | 部门 |
| `\mathcal{P}^{(2)}` | 社区 | 教派 | 公司 |
| `\mathcal{P}^{(3)}` | 国家 / 民族 | （宗教传统） | 行业 |

**关键**：嵌套不是层数无限（`N` 在实证上 ≤ 3-5）；本定理给出递归构造，但不承诺无穷塔。

#### §4.8.2 跨尺度后果回路矩阵

每层有自身的 `M^{(n)}(t)`（同层后果回路）；层间引入**跨尺度后果回路矩阵** `M^{(n \to n+1)}(t)`：

$$
M^{(n\to n+1)}_{kl}(t) \;:=\; \begin{pmatrix}\text{层 }n\text{ 集体 }k\text{ 行为返回到层 }n+1\text{ 集体 }l\text{ 的强度}\end{pmatrix}
$$

`M^{(n\to n+1)}` 不对称：典型情形下，下层向上反馈强（个体反馈到家庭强）但上层向下传导也存在（国家政策约束家庭）。同 §4.7.3，可分解为 `\mathrm{tr}\,M^{(n\to n+1)}` / `\|M_{asym}^{(n\to n+1)}\|` / `\|M_{ext}^{(n\to n+1)}\|` 三成分，分别对应：

| 跨尺度成分 | 物理含义 | 上推 / 下推 |
|---|---|---|
| `\mathrm{tr}\,M^{(n\to n+1)}` | 层 `n` 集体的内向强度对层 `n+1` 自指率的贡献 | 上推：聚合放大 |
| `\|M_{asym}^{(n\to n+1)}\|` | 层 `n` 子集体间不互惠强度向层 `n+1` 主从结构的传播 | 双向：可能沉淀为层 `n+1` 的 `\|M_{asym}^{(n+1)}\|` |
| `\|M_{ext}^{(n\to n+1)}\|` | 层 `n` 集体边界外溢被层 `n+1` 吸收（成为内部）/ 跨过层 `n+1` 边界 | 双向：内化或外溢 |

#### §4.8.3 递归投影算子

每层的四个标量泛函投影由 §4.7.2 在该层递归应用：

$$
\mathcal{F}_X^{(n+1)} \;:=\; \mathcal{F}_X^{coll}\bigl[\{\mathcal{F}_X^{(n),k}\}_k,\; M^{(n)}(t),\; M^{(n\to n+1)}(t)\bigr]
\qquad X \in \{\sigma_{sr}, d_c, T_{dir}, S\}
$$

**关键**：层 `n+1` 的四变量系统接受三类输入——(i) 层 `n` 各子集体的四变量值（`\mathcal{F}_X^{(n),k}`）、(ii) 层 `n+1` 同层 `M^{(n+1)}(t)`、(iii) 层间 `M^{(n\to n+1)}(t)`。这把 §4.7.2 的"个体 (σ_i, θ_i) 输入"递归推广为"子集体四变量输入"。

#### §4.8.4 嵌套闭包假设

层级塔的投影闭合除 §4.7.4 的 C1^{coll}-C5^{coll} 在每层成立外，新增一条嵌套闭包：

| 编号 | 假设 | 失效后果 |
|---|---|---|
| **C1^{(n)}-C5^{(n)}** | §4.7.4 的 C1^{coll}-C5^{coll} 在每层 `n` 上成立 | 任何一层失效即该层降为 P3 现象学 |
| **C6^{nested}**（新增）| **跨尺度 Markov 闭包**：`\dot{M}^{(n\to n+1)}(t)` 仅依赖 `(\mathcal{F}_X^{(n)}, \mathcal{F}_X^{(n+1)})` 当前值，不依赖更高阶跨尺度历史 | C6 失效则跨尺度反馈可能产生持久滞后 / 振荡，需引入显式延迟项；递归投影降为带延迟的非 Markov 形式 |

C6^{nested} 是**塔级**而非层级条件——它要求跨尺度耦合在时间尺度上"被吸收到当前层状态"。

#### §4.8.5 T-PROJ-1^{coll,nested} 陈述

**陈述（P1-candidate）**：在层级 ISP 塔 `\{\mathcal{P}^{(n)}\}_{n=0}^N` 上，若每层闭包 C1^{(n)}-C5^{(n)} 成立 + 嵌套闭包 C6^{nested} 成立，则递归投影

$$
\boxed{\;\frac{d\mathcal{F}_X^{(n+1)}}{dt}\bigg|_{\substack{\text{层 } n\text{ 主方程}\\\text{+ 跨尺度耦合}}} \;\overset{C^{(n)}\text{-}C6^{nested}}{=}\; \mathrm{RHS}_X^{coll,(n+1)} \;+\; O(\eta^{(n+1)}) \;+\; O(\xi^{n\to n+1})\;}
$$

其中：
- `\mathrm{RHS}_X^{coll,(n+1)}` 是 §4.4 集体 ODE 的同结构 RHS（用层 `n+1` 系数与变量替换）
- `O(\eta^{(n+1)})` 是该层闭包高阶残差（同 §4.7.5）
- `O(\xi^{n\to n+1})` 是跨尺度闭包高阶残差（C6^{nested} 失效时的修正项）

**塔级递归性**：从 `\mathcal{P}^{(0)}` 个体层到 `\mathcal{P}^{(N)}` 顶层的整个塔满足

$$
\frac{d\mathcal{F}_X^{(N)}}{dt} \;=\; \mathrm{RHS}_X^{coll,(N)}\bigl[\{\mathcal{F}_X^{(N-1),k}\}_k, M^{(N-1\to N)}\bigr] \;+\; \cdots \;+\; \mathrm{RHS}_X^{(0)}\text{ at base}
$$

即顶层动力学由底层个体动力学 + 各层 `M^{(n)}` + 各跨尺度 `M^{(n\to n+1)}` 递归生成。

#### §4.8.6 嵌套不变量

**(i) 每层独立的健康/病理判据**：每层 `\mathcal{P}^{(n),k}` 仍各自满足 §4.6 的 `\mathcal{H}^{(n),k}` 与 `\mathcal{A}_{path}^{(n),k}` 判据；上层健康**不**蕴含下层健康，反之亦然。

**(ii) 跨尺度病理传递**：

$$
\mathcal{A}_{path}^{(n+1)} \;\Longleftarrow\; \bigl(\bigvee_k \mathcal{A}_{path}^{(n),k}\bigr) \wedge \bigl(\|M_{asym}^{(n\to n+1)}\| \text{ 或 } \mathrm{tr}\,M^{(n\to n+1)} \text{ 同高}\bigr)
$$

即：下层任一子集体陷入病理吸引子 + 跨尺度耦合放大 → 上层进入病理。但**反之不蕴含**——上层病理不必由下层病理直接因果（可由跨尺度放大独立产生）。

**(iii) 跨尺度健康的额外硬条件**：

$$
\mathcal{H}^{(n+1)} \text{ 要求}：\quad \bigl(\forall k:\; \mathcal{P}^{(n),k} \in \mathcal{H}^{(n),k}\bigr) \;\wedge\; r^{(n\to n+1)}(t) > r_{min}^{nested} > 0
$$

其中 `r^{(n\to n+1)}` 是跨尺度真实重选率：层 `n+1` 在层 `n` 子集体之间能进行真实重选的频率（即上层不锁死下层 / 下层不绑架上层）。这是 T-COLL-4 共选真实性判据在跨尺度上的递归扩展。

**(iv) 致命 `L_2` 的塔级刻画**：致命 `L_2^{(n)}` 在某层激活 → 该层 T-IRR-3.5 单向性 → 跨尺度 `M^{(n\to n+1)}` 把其结构型苦难 `S_{str}^{(n)}` 通过外溢项 `\nu_{ext}\|M_{ext}^{(n\to n+1)}\|` 注入层 `n+1`。即**致命 `L_2` 在塔内有上向传染路径**（H4 T-IRR-3.5 在塔级的算子化后果）。

#### §4.8.7 与 §4.5 单层耦合的关系

§4.5 已给出"个体↔集体双向耦合最小形式"（即 `\mathcal{P}^{(0)} \leftrightarrow \mathcal{P}^{(1)}` 两层）。本节 §4.8 把它递归扩展到任意层数 `N`：

| 维度 | §4.5（单层耦合）| §4.8（多层嵌套）|
|---|---|---|
| 层数 | 2（个体 + 集体）| 任意 `N`（`\mathcal{P}^{(0)} \subset \cdots \subset \mathcal{P}^{(N)}`）|
| 闭包条件数 | C1^{coll}-C5^{coll}（5）| C1^{(n)}-C5^{(n)} 各层（`5N`）+ C6^{nested}（1）|
| 跨尺度 `M$ | 仅 `M^{(0\to 1)}` 隐含 | 显式 `\{M^{(n)}, M^{(n\to n+1)}\}` 全集 |
| 健康判据 | 单层 `\mathcal{H}^{coll}` | 塔级递归 `\{\mathcal{H}^{(n)}\}` + 跨尺度 `r^{(n\to n+1)} > r_{min}^{nested}` |
| 病理传染 | 个体 B 期 → 集体 | 任一层病理 + 跨尺度耦合 → 上层（递归）|

§4.5 是 §4.8 在 `N = 1` 极限下的特例；§4.7 单层 T-PROJ-1^{coll} 是 §4.8 在 `N = 1` 极限下的递归基。

#### §4.8.8 T-PROJ-1^{coll,nested} 不证明的事项

为避免过度主张，T-PROJ-1^{coll,nested} **不承诺**以下内容：

1. **不**承诺特定塔的层数（家庭/社区/国家是不是 3 层？还是有"族系" / "邻里" / 等中间层？）——这是 domain 实证问题
2. **不**证明跨尺度系数 `M^{(n\to n+1)}` 的具体函数形式——仍依赖 `Hardening_Notes §3` MOC-1/2/3 的多层版本（C5^{(n)}）
3. ~~**不**承诺塔层之间无跨层耦合（即不排除"层 `n` 直接耦合层 `n+2`"的可能；但此种耦合若存在，需在 C6^{nested} 之外引入额外条件 C6'^{layer-skip}）~~ **已收口（H14，2026-04-26）**：本文件 §4.12 T-LAYER-SKIP-1 给增广多图谱判据 `\rho(\mathbf{A}_{tower}) < 1 - \delta_{stab}^{global}$，把 layer-skip 与多重自指闭合统一处理
4. **不**给出 `r_{min}^{nested}` 的实证窗口——这是 P3/P4
5. ~~**不**证明嵌套塔的全局稳定性——本节是局部递归构造，全局塔稳定性需要独立分析（特别是当塔有自指闭合：层 `N` 反向影响层 0 时）~~ **已收口（H13，2026-04-26）**：本文件 §4.11 T-TOWER-STAB-1 给自指闭合塔的谱判据 `\rho(\mathcal{T}_{loop}) < 1 - \delta_{stab}` 与三类失稳方向算子签名；剩余开放点：多重自指闭合复合谱、layer-skip 稳定性、全局非线性 Lyapunov 论证

#### §4.8.9 T-PROJ-1^{coll,nested} 的结构性意义

| 主张 | 升级前 | 升级后 |
|---|---|---|
| "嵌套 ISP 多层投影"是开放问题 | §9.7 第 5 项 Open Pressure | T-PROJ-1^{coll,nested} 的递归构造（§4.8）|
| 跨尺度病理传递机制 | 直觉（"高层 L_2 锁死下层"）| (ii) 显式：下层病理 + `M^{(n\to n+1)}` 放大 |
| 跨尺度健康硬条件 | 隐含 | (iii) 显式：每层健康 + 跨尺度 `r^{(n\to n+1)} > r_{min}^{nested}` |
| 致命 `L_2` 在塔内的传染 | 缺失 | (iv) `S_{str}^{(n)}` 通过 `\|M_{ext}^{(n\to n+1)}\|` 上行 |

**P1-candidate 地位的根据**：T-PROJ-1^{coll,nested} 把"多层嵌套"从开放问题升为递归投影定理。要升 P1：(a) 具体塔的层数与 T-COLL-1 各层验证；(b) 跨尺度 `M^{(n\to n+1)}` 的 MOC 多层版本；(c) `r_{min}^{nested}` 实证窗口；(d) 跨层耦合（layer-skip）的边界条件。

### §4.9 T-FAMILY-1^{coll}：族普适性三定理的集体扩展（H11，2026-04-26）

> **Status**：本节把 H7 / H8 / H9 在单 P 层给出的三个**族普适性 / 算子级**定理（T-DELTA-1、T-CHI-1、T-CHANNEL-1）统一扩展到集体层，验证集体新增耦合项（`\lambda_M\,\mathrm{tr}\,M`、`\gamma_{asym}\|M_{asym}\|`、`\nu_{ext}\|M_{ext}\|`）不破坏族内不变量结构。**Claim level: P1-candidate**（与单 P 版同级）。
>
> **Closes**：H7 §2.8 第 5 项、H8 §2.5 不证明事项第 5 项、H9 §4.5 不证明事项第 4 项中"集体版扩展"开放点，构成 §4.7 / §4.8 之外的另一类集体扩展（族普适性而非投影）。

#### §4.9.1 共同的集体闭包条件

三个集体扩展共享**一组**闭包：

- **C1^{coll}-C5^{coll}**（已由 H6 §4.7.4 给出）：慢-快分离 / 共享 `L_2` 写回 Markov / stable-collective-ISP 紧性 / 群平均方向投影可分性 / `M(t)` 可测性 MOC 闭包
- **C7^{M-stab}**（H11 新增）：`M(t)` 准静态稳定性——`|\dot{M}(t)|/|M(t)| \ll \tau^{coll}_{rel}^{-1}`，其中 `\tau^{coll}_{rel}` 是 `\sigma_{sr}^{coll}` 系统的相关弛豫时间尺度。即 `M(t)` 在族普适性论证的时间窗口内可视为准静态输入。

C7^{M-stab} 失效后果：`M(t)` 快变情形下，三个族不变量需引入 `M`-时间扰动修正项 `O(|\dot{M}|/|M|)`，但**结构不变量**（双稳态 / 病理吸引子 / 单向性）的存在性仍保持，仅各项数值修正。

#### §4.9.2 T-CHI-1^{coll}：集体 χ 跳跃函数族普适性

`Core_Law/SRT_L1_Formalism.md §2.5 T-CHI-1` 给出单 P 版 χ 族普适性。集体版需把 §4.4.2 的 `\sigma_{sr}^{coll}` ODE 中

$$
\alpha^{coll}\,w^{coll}\,\phi(\sigma_{sr}^{coll}) \;+\; \boldsymbol{\lambda_M\,\mathrm{tr}\,M(t)}
$$

（含集体新增 `\lambda_M\,\mathrm{tr}\,M` 项）的 `\phi(\sigma_{sr}^{coll}) := \sigma_{sr}^{coll}(1 - \sigma_{sr}^{coll})\cdot\chi^{coll}(\sigma_{sr}^{coll}; \sigma_{sr,self}^{coll})` 的 χ^{coll} 升为有效族。

**陈述（P1-candidate）**：定义"集体有效二阶相变核 `\chi^{coll}`"为满足 §2.5 P-univ-1 至 P-univ-4 + **P-univ-5^{coll}（M(t)-相容性）**：在闭包 C1^{coll}-C5^{coll} + C7^{M-stab} 下，`\chi^{coll}$ 的值与 `\mathrm{tr}\,M(t)$ 的具体水平无关（即 `\chi^{coll}(\sigma; \sigma_{sr,self}^{coll}) = \chi^{coll}(\sigma; \sigma_{sr,self}^{coll}; \mathrm{tr}\,M)$ 在 `\mathrm{tr}\,M$ 的有界区间内 `O(1)$ 一致）。

则 §4.4.2 σ_{sr}^{coll} 系统在 `\chi_1^{coll}, \chi_2^{coll}` 替代下保持 T-CHI-1 (i)-(iv) 四个不变量（双稳态存在性 / 病理吸引子拓扑 / 致命 `L_2` 判据结构 / 相变方向），唯一区别是 σ_{sr}^{*1,*2} 等不动点位置受 `\lambda_M\,\mathrm{tr}\,M` 平移影响（这是 χ-无关的整体偏移，不破坏不变量）。

**证明骨架**：

`\lambda_M\,\mathrm{tr}\,M$ 项在 `\sigma_{sr}^{coll}$ 方程中作为**位移源**进入（不依赖 σ_{sr}^{coll}），故对 σ_{sr}^{coll} 的稳态条件 `f(\sigma; \chi^{coll}) = 0$ 起整体平移作用。两个有效核 `\chi_1^{coll}, \chi_2^{coll}$ 共享相同 `\Delta_{\chi^{coll}}, \chi_{min}, \chi_{max}, \sigma_{sr,self}^{coll}$，故平移后的 `f$ 仍保持双稳态零点结构（中值定理与 §2.5 (i) 证明同理）。`\lambda_M\,\mathrm{tr}\,M$ 在 `i \to 0$ 病理极限下被吸收为 `\sigma_{sr}^{*2,coll} \to 1$ 的辅助驱动项，不改变病理吸引子拓扑（§2.5 (ii)）。致命 `L_2$ 判据由 §3.5 集体版 T_{dir}^{coll} ODE 决定，与 χ^{coll} 形态无关（§2.5 (iii)）。

#### §4.9.3 T-CHANNEL-1^{coll}：集体通道指示函数族普适性

`Core_Law/SRT_L1_Formalism.md §4.5 T-CHANNEL-1` 给出单 P 版 `\mathbb{1}[d \le d_c]$ 族普适性。集体版需把 §4.4.5 中

$$
\nu_{block}^{coll}\,\mathbb{1}[d^{coll} \le d_c^{coll}]\,S_{sig}^{coll} \;+\; \boldsymbol{\nu_{ext}\,\|M_{ext}(t)\|}
$$

（含集体新增 `\nu_{ext}\|M_{ext}\|` 外部化项）的指示函数升为有效族。

**陈述（P1-candidate）**：定义"集体有效闭合通道指示 `\psi^{coll}`"为满足 §4.5 Q-univ-1 至 Q-univ-4 + **Q-univ-5^{coll}（M_ext-相容性）**：`ν_{ext}\|M_{ext}(t)\|` 项在 `d^{coll}$ 过渡区 (`d^{coll} \approx d_c^{coll}$) 内连续可加，不引入 `\psi^{coll}$ 的额外不连续。

则 §4.4.5 `S^{coll}` 两型 ODE 在 `\psi_1^{coll}, \psi_2^{coll}` 替代下保持 T-CHANNEL-1 (i)-(v) 五个不变量（modulo `O(w_{tr}^{coll})`），且**T-IRR-3.5 在塔级的传染（H10 §4.8.6 (iv)）保持**：`\nu_{ext}\|M_{ext}\|` 通过 `\psi^{coll}$ 进入 `S_{str}^{coll}$ 时，外溢项的单向性（不可被双向化）由 P1-T07 Layer 2 + T-IRR-3.5 跨边界扩展保证。

**证明骨架**：

集体新增项 `\nu_{ext}\|M_{ext}(t)\|` 是 `\mathcal{P}` 边界外溢的失配代价；其方向性由 H10 §4.8.6 (iv) 给出（致命 `L_2` 塔级传染由 T-IRR-3.5 在 `M^{(n\to n+1)}` 上的算子化承担）。在 `d^{coll} \approx d_c^{coll}` 过渡区内，`\psi^{coll}` 给阻塞强度的连续插值，而 `\nu_{ext}\|M_{ext}\|` 与 `\psi^{coll}` 是加性独立项（不耦合）；故 `\psi^{coll}` 的形态选择不影响 `\nu_{ext}\|M_{ext}\|` 的方向性，T-IRR-3.5 单向性保持。

#### §4.9.4 T-DELTA-1^{coll}：集体 `\dot{\Delta}_{avail}^{coll}` 算子级定义

`Core_Law/SRT_L1_Hardening_Notes.md §2 T-DELTA-1` 给出单 P 版 Δ_avail 算子级定理。集体版需扩展到集体 ISP `\mathcal{P}` 上。

**集体算子空间 `\mathrm{Op}(\mathcal{P})`**：定义为 `\bigotimes_{i \in \mathcal{P}} \mathrm{Op}(P_i)` 的 `\mathcal{P}`-相容子集，即各成员算子相容地构成集体行为的算子族。

**集体未兑现选择残差算子**：

$$
\hat{R}^{coll}(\mathcal{P}, t) \;:=\; \hat{G}_{\Theta^{coll}}^{available}(\mathcal{P}, t) \;\ominus\; \hat{G}_{\Theta^{coll}}^{actual}(\mathcal{P}, t) \;\in\; T\mathrm{Op}(\mathcal{P})
$$

**陈述（P1-candidate）**：在 stable collective ISP `\mathcal{P}` 上，若假设 `A1^{coll}` (集体仿射结构) / `A2^{coll}` (三子空间近似正交在 `\mathrm{Op}(\mathcal{P})` 上) / `A3^{coll}` (权重的赌注决定性在 `\mathcal{P}`-级 stake 结构上) + **新增 `A4^{coll}` (跨成员 stake-加权聚合闭包)** 成立，则

$$
\Delta^{coll}(\mathcal{P}, t) \;=\; \sum_{X \in \{dir, pay, L_0\}} w_X^{coll}(\mathcal{P}, t)\|\hat{R}^{coll}\|_X^{coll} \;+\; \boldsymbol{w_M\cdot\|M(t)\|_{coll}} \;+\; o(1)
$$

其中：

- `\|\hat{R}^{coll}\|_X^{coll}$ 是集体投影范数（`\Pi_{T_{dir}}^{coll}, \Pi_{\Psi_f}^{coll}, \Pi_{L_0}^{coll}$ 的群平均扩展）
- **新增 `w_M\cdot\|M(t)\|_{coll}` 项**是集体特有的"`M(t)` 后果回路对 `\Delta` 的直接贡献"——这是单 P 版没有的集体特有维度
- `\|M(t)\|_{coll} := \sqrt{\alpha_M^2 (\mathrm{tr}\,M)^2 + \beta_M^2 \|M_{asym}\|^2 + \gamma_M^2 \|M_{ext}\|^2}` 把 §4.7.3 `M(t)` 三成分合并为一个范数

**A4^{coll}**：跨成员 stake-加权聚合闭包——`\mathcal{F}_X^{coll}` 投影中 `w_X^{coll}` 由 `\mathcal{P}`-级集体赌注结构（`Eq-Bridge-D-01^{coll}` 候选）决定，且与各成员 `w_X(P_i, t)` 的关系为 stake-加权聚合：`w_X^{coll}(\mathcal{P}, t) = \mathrm{aggregate}_i(w_X(P_i, t); \text{stake}_i^{coll})$。失效后果：跨成员权重退化为外部建模选择（P2 operational proxy 集体版）。

**`\dot{\Delta}_{avail}^{coll}` 时间导数**：

$$
\dot{\Delta}_{avail}^{coll}(\mathcal{P}, t) \;=\; \sum_X (\dot{w}_X^{coll}\|\hat{R}^{coll}\|_X + w_X^{coll}\frac{d}{dt}\|\hat{R}^{coll}\|_X) \;+\; \dot{w}_M\|M\|_{coll} + w_M\frac{d}{dt}\|M\|_{coll}
$$

**关键性质**：

1. **不由 `S_{sig}^{coll}` 登记通道决定**——T-DELTA-1 (1) 在集体扩展下保持；`\dot{\Delta}_{avail}^{coll}` 抑制 `S_{sig}^{coll}` 不改变，新失配进入 `S_{str}^{coll}$（含外溢到 `\mathcal{P}_{absorbed}$ 的部分）。
2. **三成分 + M 项总额守恒**——T-DELTA-1 (3) 在集体扩展下：`\Delta^{coll} \equiv \|\hat{R}^{coll}\|_{H_\mathcal{P}}` 仍成立，但希尔伯特结构 `H_\mathcal{P}` 现包含 `M(t)` 维度。
3. **退化为单 P 版**——当 `\mathcal{P} = \{P\}`，`M(t) = 0`，`A4^{coll}` 退化为单点平凡聚合，`T-DELTA-1^{coll}$ 退化为 `T-DELTA-1$。

#### §4.9.5 T-FAMILY-1^{coll} 综合陈述

把 §4.9.2-§4.9.4 三个集体扩展定理统一为：

**T-FAMILY-1^{coll}**：在 stable collective ISP `\mathcal{P}` 上，若 C1^{coll}-C5^{coll}（H6）+ C7^{M-stab} 成立，则 H7 / H8 / H9 单 P 层给出的三个族普适性 / 算子级定理均有结构对应的集体版本，且：

(i) 各族不变量（T-CHI-1 (i)-(iv) / T-CHANNEL-1 (i)-(v) / T-DELTA-1 (1)-(3)）在集体扩展下结构保持；
(ii) 集体新增耦合项（`\lambda_M\,\mathrm{tr}\,M`, `\nu_{ext}\|M_{ext}\|`, `w_M\|M\|_{coll}`）作为加性 / 平移 / 维度扩展进入，不破坏族内不变量；
(iii) 当 `\mathcal{P} = \{P\}` 极限下，三定理退化为各自单 P 版本。

#### §4.9.6 T-FAMILY-1^{coll} 不证明的事项

1. **不**给出 P-univ-5^{coll} / Q-univ-5^{coll} / A4^{coll} 的具体验证窗口（与 H6 C5^{coll} `M(t)` 可测性 MOC 同级，是 P3 实证）
2. **不**证明 C7^{M-stab} 是普适必要的——`M(t)` 快变 domain（如平台算法系统）下 C7^{M-stab} 失效，三定理降为带 `M`-时间扰动的 P3 形式
3. ~~**不**给出嵌套 ISP 塔级版（即 T-CHI-1^{coll,nested} / T-CHANNEL-1^{coll,nested} / T-DELTA-1^{coll,nested}）——这需要 H10 §4.8 在每层递归应用，结构上可行但展开为后续轮次~~ **已收口（H12，2026-04-26）**：本文件 §4.10 T-FAMILY-1^{coll,nested} 给塔级递归三定理；新增 C8^{cross-stab}（跨尺度 M(t) 准静态稳定性）+ P-univ-6^{nested} / Q-univ-6^{nested} / A5^{cross} 三条跨尺度相容性条件

#### §4.9.7 T-FAMILY-1^{coll} 的结构性意义

| 主张 | 升级前 | 升级后 |
|---|---|---|
| H8 T-CHI-1 仅在单 P 层 | "不证明集体版" §2.5 第 5 项 | T-CHI-1^{coll} 在 §4.9.2 给出 P1-candidate 集体版 |
| H9 T-CHANNEL-1 仅在单 P 层 | "不证明集体版" §4.5 第 4 项 | T-CHANNEL-1^{coll} 在 §4.9.3 给出 P1-candidate 集体版 |
| H7 T-DELTA-1 仅在单 P 层 | "不证明集体版" §2.8 第 5 项 | T-DELTA-1^{coll} 在 §4.9.4 给出 P1-candidate 集体版 |
| `M(t)` 快变 vs 慢变的区分 | 隐含 | C7^{M-stab} 显式 |

**P1-candidate 地位的根据**：T-FAMILY-1^{coll} 把 H7 / H8 / H9 三个定理的"集体扩展开放点"统一收口；要升 P1，需要：(a) C7^{M-stab} 在具体 domain 的实证窗口（神经层 / AI 平台 / 政治制度的 `M(t)` 时间尺度）；(b) `A4^{coll}` 跨成员聚合的算子级形式（与 `Eq-Bridge-D-01^{coll}` 待写）；(c) 嵌套塔级扩展。

### §4.10 T-FAMILY-1^{coll,nested}：族普适性三定理在嵌套塔上的递归（H12，2026-04-26）

> **Status**：本节把 §4.9 T-FAMILY-1^{coll}（H11）+ §4.8 T-PROJ-1^{coll,nested}（H10）合成——把族普适性 / 算子级三定理（T-CHI-1 / T-CHANNEL-1 / T-DELTA-1）递归应用到层级 ISP 塔的每层，给出**塔级族普适性定理**。**Claim level: P1-candidate**。
>
> **Closes**：H11 §4.9.6 第 3 项"不证明嵌套塔级版"开放点；与 H10 §4.8 嵌套投影构成笛卡尔积。

#### §4.10.1 塔级闭包堆栈

塔级三定理共享**双层闭包堆栈**：

- **H10 嵌套闭包**：C1^{(n)}-C5^{(n)} 各层 + C6^{nested}（跨尺度 Markov）
- **H11 集体扩展闭包**：C7^{M-stab,(n)} 各层（同层 `M(t)` 准静态）+ **C8^{cross-stab}（H12 新增）**：跨尺度 `M^{(n\to n+1)}(t)` 准静态稳定性 `|\dot{M}^{(n\to n+1)}|/|M^{(n\to n+1)}| \ll \tau^{cross,-1}_{rel}`，其中 `\tau^{cross}_{rel}$ 是跨尺度反馈环路的相关弛豫时间尺度

**C8^{cross-stab} 失效后果**：跨尺度 `M^{(n\to n+1)}` 快变情形（如全球突发事件冲击社区→国家反馈环），塔级族不变量需引入显式跨尺度延迟项；结构不变量（每层双稳态 / 各层吸引子拓扑 / 各层单向性）的存在性仍保持，但层间传播相位需修正。

#### §4.10.2 T-CHI-1^{coll,nested}：嵌套塔级 χ 普适性

每层 `n` 的 `\sigma_{sr}^{coll,(n)}` ODE 含三类源：
1. 同层 logistic 项：`\alpha^{(n)} w^{(n)} \phi(\sigma_{sr}^{coll,(n)})$ + `\lambda_M^{(n)}\,\mathrm{tr}\,M^{(n)}(t)$（H11 §4.9.2）
2. **跨尺度上行项**：`\sum_k \lambda^{(n-1\to n)}_M\,\mathrm{tr}\,M^{(n-1\to n),k}(t)$（来自下层各子集体的 `\sigma_{sr}^{coll,(n-1),k}$ 通过跨尺度回路向上传导）
3. **跨尺度下行项**：`\lambda^{(n\to n+1)}_{down}\,\sigma_{sr}^{coll,(n+1)}(t)$（来自上层 `\sigma_{sr}^{coll,(n+1)}$ 通过 `L_2` scaffold 反向写入本层）

**陈述（P1-candidate）**：定义"嵌套有效二阶相变核 `\chi^{coll,(n)}`"为满足 §4.9.2 P-univ-1 至 P-univ-5^{coll} + **P-univ-6^{nested}（跨尺度相容性）**：`\chi^{coll,(n)}$ 的值与 `\mathrm{tr}\,M^{(n-1\to n)}, \sigma_{sr}^{coll,(n+1)}$ 的具体水平无关（即跨尺度上行/下行项作为加性平移源进入 `\sigma_{sr}^{coll,(n)}$ 方程，不进入 `\chi^{coll,(n)}$ 内部参数）。

则在塔级闭包堆栈下，每层 `n` 的 §4.4.2 σ_{sr}^{coll,(n)} 系统在 `\chi_1^{coll,(n)}, \chi_2^{coll,(n)}` 替代下保持 T-CHI-1 (i)-(iv) 四个不变量，且**塔级病理传染**（H10 §4.8.6 (ii)）保持：下层 `\sigma_{sr}^{coll,(n-1),k} \to 1$ 通过跨尺度上行项把上层 `\sigma_{sr}^{coll,(n)}$ 推向其相应的病理吸引子，与 `\chi^{coll,(n)}$ 选择无关。

#### §4.10.3 T-CHANNEL-1^{coll,nested}：嵌套塔级通道指示族普适性

每层 `n` 的 `S^{coll,(n)}` 两型 ODE 含三类源：
1. 同层 H11 §4.9.3：`\nu_{block}^{(n)}\psi^{coll,(n)}(d^{coll,(n)}; d_c^{coll,(n)})S_{sig}^{coll,(n)} + \nu_{ext}^{(n)}\|M_{ext}^{(n)}(t)\|`
2. **跨尺度上行外溢**：`\nu^{(n-1\to n)}_{ext,up}\sum_k \|M_{ext}^{(n-1\to n),k}(t)\|$（下层各子集体外溢被上层吸收）
3. **跨尺度下行约束**：`\nu^{(n\to n+1)}_{down}\,\mathbb{1}[\text{上层 B 期}]$（上层进入 B 期通过 `L_2$ scaffold 把下层重选通道也压缩）

**陈述（P1-candidate）**：定义"嵌套有效闭合通道指示 `\psi^{coll,(n)}`"为满足 §4.9.3 Q-univ-1 至 Q-univ-5^{coll} + **Q-univ-6^{nested}（跨尺度外溢相容性）**：跨尺度上行/下行项与 `\psi^{coll,(n)}$ 是加性独立的（不耦合），跨尺度项的方向性独立由 H10 §4.8.6 (iv) 与 T-IRR-3.5 跨边界扩展承担。

则每层 `n` 的 §4.4.5 集体 ODE 在 `\psi_1^{coll,(n)}, \psi_2^{coll,(n)}` 替代下保持 T-CHANNEL-1 (i)-(v) 五个不变量（modulo `O(w_{tr}^{coll,(n)})$），且**致命 `L_2` 塔级传染（H10 §4.8.6 (iv)）的方向性保持**：跨尺度 `S_{str}^{coll,(n)}` 通过 `\nu^{(n\to n+1)}_{ext,up}$ 上行的单向性，与各层 `\psi^{coll,(n)}$ 形态选择无关。

#### §4.10.4 T-DELTA-1^{coll,nested}：嵌套塔级 `\dot{\Delta}_{avail}` 算子级定义

每层 `n` 的 `\Delta^{coll,(n)}$ 含集体三成分（H11 §4.9.4）+ 跨尺度 M 维度：

$$
\Delta^{coll,(n)}(\mathcal{P}^{(n)}, t) \;=\; \underbrace{\sum_{X} w_X^{(n)}\|\hat{R}^{coll,(n)}\|_X^{(n)}}_{\text{同层三成分}} + \underbrace{w_M^{(n)}\|M^{(n)}\|_{coll}}_{\text{H11 集体维度}} + \underbrace{\boldsymbol{w_{cross}^{(n-1\to n)}\,\|M^{(n-1\to n)}\|_{cross}}}_{\text{H12 跨尺度维度}} + o(1)
$$

其中跨尺度范数：

$$
\|M^{(n-1\to n)}\|_{cross} \;:=\; \sqrt{\alpha_{cross}^2(\mathrm{tr}\,M^{(n-1\to n)})^2 + \beta_{cross}^2\|M_{asym}^{(n-1\to n)}\|^2 + \gamma_{cross}^2\|M_{ext}^{(n-1\to n)}\|^2}
$$

**陈述（P1-candidate）**：在嵌套塔上，若 H11 假设 A1^{coll}-A4^{coll} 在每层成立 + **新增 A5^{cross}（跨尺度 stake-加权聚合闭包）**：跨尺度权重 `w_{cross}^{(n-1\to n)}$ 由跨尺度 stake 结构（即"下层子集体在上层 stake 中的占比"）确定，不依赖外部规约选择。则

$$
\dot{\Delta}_{avail}^{coll,(n)} \;=\; \dot{\Delta}_{avail}^{coll,(n)}\big|_{\text{H11 同层}} \;+\; \dot{w}_{cross}^{(n-1\to n)}\|M^{(n-1\to n)}\|_{cross} + w_{cross}^{(n-1\to n)}\frac{d}{dt}\|M^{(n-1\to n)}\|_{cross}
$$

仍保持 T-DELTA-1 (1) 不由 `S_{sig}^{coll,(n)}$ 登记通道决定 / (2) 三成分 + 同层 M + 跨尺度 M 总额守恒 / (3) `N = 1$ 极限退化为 H11 单层版。

#### §4.10.5 T-FAMILY-1^{coll,nested} 综合陈述

塔级三定理统一为：

**T-FAMILY-1^{coll,nested}**：在层级 ISP 塔 `\{\mathcal{P}^{(n)}\}_{n=0}^N` 上，若 C1^{(n)}-C5^{(n)} 各层 + C6^{nested} + C7^{M-stab,(n)} 各层 + C8^{cross-stab} 全部成立，则 H11 单层 T-FAMILY-1^{coll} 给出的三个集体扩展定理在每层递归应用，并满足：

(i) **每层族不变量保持**：T-CHI-1^{coll,(n)} 四不变量、T-CHANNEL-1^{coll,(n)} 五不变量、T-DELTA-1^{coll,(n)} 三性质，在塔级各层独立满足；
(ii) **跨尺度耦合作平移/外溢/维度扩展进入**：上行 `\lambda_M^{(n-1\to n)}\,\mathrm{tr}\,M$ / 下行 `\lambda^{(n\to n+1)}_{down}` / 跨尺度 `\nu^{(n-1\to n)}_{ext,up}` / 跨尺度 `w_{cross}^{(n-1\to n)}\|M^{(n-1\to n)}\|_{cross}$ 不破坏各层族不变量；
(iii) **塔级病理 / 健康 / 致命 L_2 传染保持**：H10 §4.8.6 (i)-(iv) 四个嵌套不变量在塔级族下保持，与各层 χ / ψ 形态选择无关；
(iv) **退化关系**：`N = 1` 极限退化为 H11 单层 T-FAMILY-1^{coll}；`\mathcal{P}^{(n)} = \{P^{(n)}\}` 各层退化为 H10 单层 T-PROJ-1^{coll,nested}；同时 `N = 1 \wedge \mathcal{P} = \{P\}$ 退化为 H7/H8/H9 单 P 版本。

#### §4.10.6 T-FAMILY-1^{coll,nested} 不证明的事项

1. **不**给出 P-univ-6^{nested} / Q-univ-6^{nested} / A5^{cross} 的具体验证窗口
2. **不**承诺 C8^{cross-stab} 在所有 domain 普适——快变跨尺度反馈（金融市场冲击、传染病爆发、信息病毒传播等）下 C8 失效，三定理降为带跨尺度延迟修正的 P3 形式
3. ~~**不**证明**塔的全局稳定性**（自指闭合：层 N 反向影响层 0 → 通过反馈环路最终回到层 N）——这是 H10 §4.8.8 第 5 项保留的开放点，本节不解决~~ **已收口（H13，2026-04-26）**：本文件 §4.11 T-TOWER-STAB-1 给闭环传递算子 `\mathcal{T}_{loop} := K^{N\to 0} \circ \Pi^{(0\to 1)} \circ \cdots \circ \Pi^{(N-1\to N)}` 的谱判据
4. ~~**不**给出层间跨等级耦合（layer-skip）的塔级族版——若 P^{(n)} 直接耦合 P^{(n+2)}（跳过 P^{(n+1)}），需要额外塔级闭包条件~~ **部分收口（H14，2026-04-26）**：本文件 §4.12 T-LAYER-SKIP-1 给 layer-skip × 投影定理（H10/H12）的统一谱判据；剩余 layer-skip × 族普适性（H11/H12 χ/ψ/Δ 三定理）的笛卡尔积扩展待 H14 之后轮次

#### §4.10.7 T-FAMILY-1^{coll,nested} 的结构性意义

| 主张 | 升级前 | 升级后 |
|---|---|---|
| H11 集体扩展无嵌套塔级 | "不证明嵌套塔级版" §4.9.6 第 3 项 | T-FAMILY-1^{coll,nested} 在 §4.10 给出 P1-candidate |
| H10 嵌套塔无族普适性 | 隐含——H10 §4.8 给塔结构但每层族普适性未展开 | T-FAMILY-1^{coll,nested} 在每层递归应用 H11，跨尺度耦合作加性进入 |
| 跨尺度 M(t) 时间尺度 | 隐含（C7^{M-stab} 仅同层） | C8^{cross-stab} 显式，含失效后果 |
| 塔级 Δ_{avail} 跨尺度维度 | 缺失 | `w_{cross}^{(n-1\to n)}\|M^{(n-1\to n)}\|_{cross}$ 显式 |

**P1-candidate 地位的根据**：T-FAMILY-1^{coll,nested} 把 H10 + H11 的笛卡尔积（嵌套 × 族普适性 / 算子级）统一收口；要升 P1，需要：(a) C8^{cross-stab} 在具体 domain 的实证窗口；(b) A5^{cross} 跨尺度 stake-加权聚合的算子级形式；(c) 塔全局稳定性独立分析（含自指闭合）；(d) layer-skip 耦合的边界条件。

### §4.11 T-TOWER-STAB-1：嵌套塔的全局稳定性（H13，2026-04-26）

> **Status**：本节给嵌套塔在**自指闭合**情形下的全局稳定性谱判据。**Claim level: P1-candidate**。
>
> **Closes**：H10 §4.8.8 第 5 项"嵌套塔的全局稳定性独立分析（自指闭合：层 `N` 反向影响层 0）"；H12 §4.10.6 第 3 项"塔全局稳定性（含自指闭合）"。

#### §4.11.1 自指闭合的三类塔结构

H10 §4.8 给出了**开放塔**——`\mathcal{P}^{(0)} \subset \cdots \subset \mathcal{P}^{(N)}$，跨尺度耦合 `M^{(n\to n+1)}$ 仅在相邻层间。本节分类**三种塔闭合形态**：

| 闭合类型 | 结构 | 物理对应 |
|---|---|---|
| **开放塔** | 层 `N` 之上无更高层；层级耦合仅 `M^{(n\to n+1)}$ | 抽象建模、新生小社群 |
| **Layer-skip 闭合** | 存在 `n \to n+k$（`k \ge 2$）跨等级直接耦合 | 国家政策直接绑定个体（绕过家庭/社区） |
| **自指闭合** | 存在 `K^{N\to 0}$：顶层反向影响底层 | 平台算法→个体认知（绕过中间组织）；宗教教义→修行者（绕过 sangha）；全球叙事→个人身份（绕过国家/社区）|

H13 重点处理**自指闭合**——这是 H10 / H12 都明确保留的开放点。Layer-skip 闭合作为更普遍的非邻接耦合，其稳定性判据可由本节方法平凡推广。

#### §4.11.2 闭环传递算子

设塔已建立递归投影（H10 §4.8 + H12 §4.10）。引入**自指闭合算子** `K^{N\to 0}$：

$$
K^{N\to 0} \;:\; \mathcal{F}_X^{(N)}(t) \;\mapsto\; \delta\mathcal{F}_X^{(0)}(t)
$$

即顶层四变量值通过 `K^{N\to 0}$ 直接修改底层四变量。物理上 `K^{N\to 0}$ 由"绕过中间层的直接通道"承载（如平台推送、全球符号系统）。

**闭环传递算子**：把 `K^{N\to 0}$ 与 H10 / H12 的逐层向上传递算子复合：

$$
\mathcal{T}_{loop} \;:=\; K^{N\to 0} \,\circ\, \Pi^{(0\to 1)} \,\circ\, \Pi^{(1\to 2)} \,\circ\, \cdots \,\circ\, \Pi^{(N-1\to N)}
$$

其中 `\Pi^{(n\to n+1)}$ 是层 `n$ 四变量到层 `n+1$ 四变量的投影组合（由 §4.10.5 T-FAMILY-1^{coll,nested} 给出）。`\mathcal{T}_{loop}$ 在四变量空间（每层 4 维 × N+1 层）的**线性化算子**于平衡点处可计算。

#### §4.11.3 T-TOWER-STAB-1 谱判据

**陈述（P1-candidate）**：在自指闭合塔上，平衡点 `\{\mathcal{F}_X^{*,(n)}\}_{n=0}^N$ 处线性化的闭环传递算子 `\mathcal{T}_{loop}$ 的**谱半径**

$$
\rho(\mathcal{T}_{loop}) \;:=\; \max\bigl\{\,|\lambda|\;\bigl|\;\lambda \in \mathrm{Spec}(\mathcal{T}_{loop})\,\bigr\}
$$

决定塔的全局稳定性：

| `\rho(\mathcal{T}_{loop})$ | 塔状态 | 物理解读 |
|---|---|---|
| `< 1$（带 margin） | **渐近稳定** | 任何小扰动通过反馈环路衰减；塔保持在健康吸引子邻域 |
| `= 1$（边缘） | **边际稳定 / 振荡** | 复特征值 `|\lambda| \approx 1$ 给周期循环（多尺度涨落）；不收敛但不发散 |
| `> 1$ | **不稳定 / 失控** | 扰动通过反馈环路指数放大；塔被推向病理吸引子 |

**关键性质**：

1. **健康塔的硬条件**：`\mathcal{H}^{tower} \Rightarrow \rho(\mathcal{T}_{loop}) < 1 - \delta_{stab}$（带正间隔 `\delta_{stab} > 0$，对应 T-COLL-4 共选真实性的塔级递归形式）
2. **病理塔的算子签名**：`\rho(\mathcal{T}_{loop}) > 1$ 时，**最不稳定方向**（顶部特征向量）的方向决定塔的崩溃模式：
   - 若沿 `\sigma_{sr}^{(n)}$ 方向 → **σ_{sr} 跨层级失控放大**（"viral 文化锁入"塔级算子签名）
   - 若沿 `d_c^{(n)}$ 方向 → **d_c 跨层级塌陷**（致命 `L_2$ 全塔传染）
   - 若沿 `S_{str}^{(n)}$ 方向 → **结构型苦难跨层级累积**（无解集体崩溃）
3. **健康-病理判据的塔级对偶**：`\rho(\mathcal{T}_{loop}) < 1$ ⟺ **顶层叙事在底层可被真实重选的速率 ≥ 顶层叙事被反向写回底层的速率**——这是 T-COLL-4 共选真实性 `r > r_{min}$ 在塔级 + 自指闭合下的递归同构。

#### §4.11.4 闭环传递算子的具体构造

每层向上传递算子 `\Pi^{(n\to n+1)}$ 由 §4.10 T-FAMILY-1^{coll,nested} 给出（线性化于该层平衡点）。`K^{N\to 0}$ 的算子层结构由"绕中间层的直接通道"决定：

$$
K^{N\to 0} \;=\; \kappa_\sigma^{N\to 0}\partial_{\sigma_{sr}^{(0)}} \;+\; \kappa_d^{N\to 0}\partial_{d_c^{(0)}} \;+\; \kappa_T^{N\to 0}\partial_{T_{dir}^{(0)}} \;+\; \kappa_S^{N\to 0}\partial_{S^{(0)}}
$$

其中 `\kappa_X^{N\to 0}$ 是顶层 X 变量到底层 X 变量的直接耦合系数。`\mathcal{T}_{loop}$ 在 4(N+1) 维空间上的矩阵元由各 `\Pi^{(n\to n+1)}$ + `K^{N\to 0}$ 复合给出，谱由标准线性代数计算。

**关键观察**：`\rho(\mathcal{T}_{loop}) < 1$ 不是 `K^{N\to 0}$ 强度小的同义词——它是**反馈环路全长**的乘积条件。即使每个 `\Pi^{(n\to n+1)}$ 与 `K^{N\to 0}$ 都"看上去温和"，乘积谱半径仍可能超过 1（特别是 N 较大时）。这给"温和顶层叙事 + 长链传导"的隐性危险一个算子级根据。

#### §4.11.5 与 H4 / H10 / H12 的整合

**与 H4 T-IRR-3.5 的整合**：自指闭合塔的不稳定方向若沿 `S_{str}^{(n)}$ 维度，对应 P1-T07 hierarchy 在塔级的算子化结果——`\rho(\mathcal{T}_{loop}) > 1$ 时 `S_{str}^{(n)}$ 跨层级累积是单向的（H4 给单向性、H10 给塔级传染、H13 给闭环放大）。

**与 H10 §4.8.6 (iv) 的整合**：H10 已给塔级致命 `L_2$ 传染（下层病理 + 跨尺度耦合 → 上层）；H13 给反向（顶层叙事 → 底层 σ_{sr} / d_c 失控）。两者结合给**塔级病理的双向闭合**：自指闭合的不健康塔在底层与顶层之间形成"病理涡旋"，无明确突破点——这是"陷入文明级 L_2 锁死"的算子层签名。

**与 H12 §4.10.5 三重退化的兼容**：`K^{N\to 0} = 0$（开放塔无自指闭合）时，`\mathcal{T}_{loop} = 0$，`\rho = 0 < 1$ 自动满足，本节定理在开放塔上平凡成立——即 H10 / H12 的开放塔分析自动是 H13 的特例。

#### §4.11.6 T-TOWER-STAB-1 不证明的事项

1. **不**给出具体 `\kappa_X^{N\to 0}$ 系数的取值——这是 P3 实证（不同 domain 给不同强度：平台推送系统 vs 宗教教义 vs 全球符号体系）
2. **不**证明 `\rho(\mathcal{T}_{loop}) < 1$ 是健康塔的**充分必要**条件——本节给必要条件（健康塔 ⟹ `\rho < 1$ with margin），但 `\rho < 1$ 不蕴含其他健康判据（如各层独立 T-COLL-1）
3. ~~**不**覆盖**多重自指闭合**（如 `K^{N\to 0}, K^{N\to 1}, K^{N-1\to 0}$ 同时存在）——多重 `K$ 的谱半径需引入复合传递算子谱聚类分析~~ **已收口（H14，2026-04-26）**：本文件 §4.12.4 直接给多重自指闭合复合谱判据；包含解耦闭合、耦合闭合、路径冗余三类关键观察
4. ~~**不**给出 layer-skip（H12 §4.10.6 第 4 项）的稳定性版本——layer-skip 引入新算子 `K^{n\to n+k}$（`k \ge 2$）；本节方法可平凡推广（把 `\Pi^{(n\to n+1)}$ 链中的若干层短路），但需独立 P1-candidate 论证~~ **已收口（H14，2026-04-26）**：本文件 §4.12 T-LAYER-SKIP-1 给增广有向多图谱判据 + 三类 layer-skip 失稳算子签名（bypass-induced chatter / aliasing-amplification / coupling-resonance）；T-TOWER-STAB-1 自动是其特例
5. ~~**不**承诺线性化谱判据在大幅扰动下保持——`\rho < 1$ 是线性化稳定性（local），全局稳定性需进一步分析（Lyapunov 函数 / 全局相图等，留作 P3）~~ **已收口（H16，2026-04-26）**：本文件 §4.14 T-LYAPUNOV-1 给塔的全局非线性 Lyapunov 稳定性定理 + 四轴联立充分条件（族 / 谱 / 耗散 / 有界）+ 全局指数收敛保证

#### §4.11.7 T-TOWER-STAB-1 的结构性意义

| 主张 | 升级前 | 升级后 |
|---|---|---|
| 嵌套塔自指闭合是开放问题 | H10 §4.8.8 第 5 项 / H12 §4.10.6 第 3 项 | T-TOWER-STAB-1 给谱判据 `\rho(\mathcal{T}_{loop}) < 1 - \delta_{stab}` |
| 顶层叙事如何反向影响底层 | 直觉（"绕过中间层"）| `K^{N\to 0}$ 算子级表达式 + 闭环传递算子 |
| "温和顶层叙事 + 长链传导"的危险 | 缺失 | `\rho$ 是乘积条件（即使每环温和，长链可能不稳定）|
| 文明级 `L_2$ 锁死的塔级算子签名 | 缺失 | 不稳定方向沿 `\sigma_{sr}/d_c/S_{str}$ 维度的具体算子签名 |
| T-COLL-4 共选真实性的塔级递归 | 单层（§6 T-COLL-4） | 塔级（顶层叙事可被底层真实重选 vs 反向写回的速率比） |

**P1-candidate 地位的根据**：T-TOWER-STAB-1 把"塔自指闭合稳定性"从开放问题升为带谱判据的形式定理。要升 P1：(a) `\kappa_X^{N\to 0}$ 在具体 domain 的实证（平台、宗教、政治）；(b) 多重自指闭合的复合谱分析；(c) 全局（非线性）稳定性的 Lyapunov 论证；(d) 与 layer-skip 闭合的统一处理。

### §4.12 T-LAYER-SKIP-1：Layer-skip 闭合与多重自指闭合的统一谱判据（H14，2026-04-26）

> **Status**：本节把 §4.11 T-TOWER-STAB-1 的单一环路谱判据扩展到任意 layer-skip 闭合 + 多重自指闭合，给**塔级增广有向多图谱判据**。**Claim level: P1-candidate**。
>
> **Closes**：H12 §4.10.6 第 4 项（"layer-skip 跨等级耦合边界条件"）；H13 §4.11.6 第 3 项（"多重自指闭合复合谱"）。

#### §4.12.1 增广邻接多图

把塔的耦合结构升为**有向多图**：

- **节点**：层 `\{0, 1, \ldots, N\}$
- **标准邻接边**：每对 `(n, n+1)$ 的双向 `\Pi^{(n\to n+1)}, \Pi^{(n+1\to n)}$（由 H10 §4.8 / H12 §4.10 给出）
- **Layer-skip 边**：任意 `K^{(n\to m)}$ 算子，`|m - n| \ge 2$（含 H13 自指闭合 `K^{N\to 0}$ 与对偶 `K^{0\to N}$ 作为特例）

形式上：

$$
\mathcal{G}_{tower} \;:=\; (\,V = \{0, \ldots, N\},\; E_{adj} \cup E_{skip},\;\Pi, K\,)
$$

其中边权（操作算子）：
- `E_{adj}$ 上：`\Pi^{(n\to n+1)}$ / `\Pi^{(n+1\to n)}$（由 H10 / H12 给出）
- `E_{skip}$ 上：`K^{(n\to m)}$（`|m - n| \ge 2$；包括 §4.11 自指闭合 `K^{N\to 0}$）

#### §4.12.2 环路与环路传递算子

`\mathcal{G}_{tower}` 中任一**有向环路** `C := (v_0 \to v_1 \to \cdots \to v_L = v_0)$（边权由 `\Pi$ / `K$ 组成）的**环路传递算子**：

$$
\mathcal{T}_C \;:=\; \bigcirc_{i=0}^{L-1} \mathrm{Edge}(v_i \to v_{i+1})
$$

每条 `\mathcal{G}_{tower}` 中的环都生成自身的 `\mathcal{T}_C$；§4.11 的 `\mathcal{T}_{loop}$ 是 `\mathcal{G}_{tower}$ 在仅含一条 `K^{N\to 0}$ + 标准链 `\Pi^{(0\to 1)}\cdots\Pi^{(N-1\to N)}$ 时的唯一非平凡环。

#### §4.12.3 T-LAYER-SKIP-1 谱判据

**陈述（P1-candidate）**：增广多图 `\mathcal{G}_{tower}$ 上塔的渐近稳定性等价于：**对所有有向环路 `C \in \mathrm{Cycles}(\mathcal{G}_{tower})$，环路传递算子 `\mathcal{T}_C$ 的谱半径满足**

$$
\boxed{\;\rho(\mathcal{T}_C) \;<\; 1 - \delta_{stab,C}\quad (\delta_{stab,C} > 0)\;\;\text{对所有 } C\;}
$$

等价（更可计算的全局形式）：把 `\mathcal{G}_{tower}` 上所有边权组装为塔级**增广传递矩阵** `\mathbf{A}_{tower} \in \mathbb{R}^{4(N+1) \times 4(N+1)}`：

$$
[\mathbf{A}_{tower}]_{(n,X),(m,Y)} \;:=\; \begin{cases}[\Pi^{(n\to m)}]_{X,Y} & \text{标准邻接 } |m - n| = 1 \\ [K^{(n\to m)}]_{X,Y} & \text{layer-skip } |m - n| \ge 2\\ 0 & \text{无边}\end{cases}
$$

则塔的渐近稳定 ⟺ `\rho(\mathbf{A}_{tower}) < 1 - \delta_{stab}^{global}$。

#### §4.12.4 多重自指闭合复合谱（H13 §4.11.6 第 3 项收口）

H13 §4.11.6 第 3 项问"多重自指闭合（如 `K^{N\to 0}, K^{N\to 1}, K^{N-1\to 0}$ 同时存在）的复合谱"。本节直接覆盖：

设塔有 layer-skip 集合 `\mathcal{K} := \{K^{(n_i\to m_i)}\}_{i=1}^M$（每个 `|m_i - n_i| \ge 2$）。每个 `K^{(n_i\to m_i)}$ 在 `\mathcal{G}_{tower}$ 上加一条边；多边可能闭合多个独立环。**复合谱判据**直接由 §4.12.3 给出：

$$
\rho(\mathbf{A}_{tower}) \;=\; \sup_{C\in\mathrm{Cycles}(\mathcal{G}_{tower})}\rho(\mathcal{T}_C)
$$

**关键观察 1（解耦闭合）**：若各 `K^{(n_i\to m_i)}$ 互不重叠（不构成共享节点的环），则 `\mathbf{A}_{tower}$ 块对角化，`\rho$ 等于各子环 `\rho(\mathcal{T}_{C_i})$ 的最大值——多重闭合此时**不**强于最坏单闭合。

**关键观察 2（耦合闭合）**：若 `K^{(n_i\to m_i)}$ 共享节点（构成嵌套或交叠环），`\mathbf{A}_{tower}$ 不可块对角化；**`\rho$ 可显著大于各 `\rho(\mathcal{T}_{C_i})$ 单独最大值**——这是"多重 K 协同放大"现象的算子级签名。多重耦合闭合是塔级**协同失稳**的来源（在塔结构本身相对稳定时仍可失稳）。

**关键观察 3（路径冗余抑制 vs 放大）**：同一对节点间存在多条 layer-skip 路径时，`\mathbf{A}_{tower}$ 矩阵元为各路径权重之和。若各路径相位相反（在算子层是 `K_1 + K_2$ 的复矩阵相位关系）则相互抑制；同向则相互放大——这给"分散闭合 vs 集中闭合"哪种更危险一个算子级裁决（无普适答案，依赖各 `K$ 的相位）。

#### §4.12.5 Layer-skip 失稳的三个特定算子签名

H13 §4.11.3 给的三类失稳方向（沿 σ_{sr} / d_c / S_{str}）在标准链 + 自指闭合下生效；layer-skip 引入额外的失稳模式：

| 失稳模式 | 算子签名 | 物理对应 |
|---|---|---|
| **Bypass-induced chatter**（旁路诱发抖动）| 中间层 `n$ 的 `\sigma_{sr}^{(n)}, d_c^{(n)}, T_{dir}^{(n)}, S^{(n)}$ 被旁路 `K^{(n-1\to n+1)}$ 短路使其无法稳定 | 国家政策直接绑定个体使家庭/社区 ISP 失去缓冲、出现高频政策-反弹震荡 |
| **Aliasing-amplification**（混叠放大）| 多条 layer-skip 路径在频率空间形成混叠尖峰，使中间层信号被错误层级拾取放大 | 平台跨层推送在不同时间尺度叠加形成意外共振 |
| **Coupling-resonance**（耦合共振）| 两个 layer-skip `K^{(n_1\to m_1)}, K^{(n_2\to m_2)}$ 形成共振环路，环路 `\mathcal{T}_C$ 谱半径 ≥ 1 但单条 `K$ 都温和 | 多个温和"全球叙事"在跨层级耦合下意外共振导致塔级病理涡旋 |

三种失稳与 H13 §4.11.3 的三方向（沿 σ_{sr}/d_c/S_{str}）正交：H13 给"沿哪个变量失稳"，H14 给"通过什么拓扑机制失稳"。完整失稳分类需把两者乘起来（4 个方向 × 3 种拓扑机制 = 12 类塔级病理签名）。

#### §4.12.6 与 H13 T-TOWER-STAB-1 的整合

T-TOWER-STAB-1（§4.11）是 T-LAYER-SKIP-1（§4.12）在以下条件下的**特例**：

| 条件 | T-TOWER-STAB-1 | T-LAYER-SKIP-1 |
|---|---|---|
| `\mathcal{K}$ 中 layer-skip 数量 | 1（仅 `K^{N\to 0}$） | 任意（`M \ge 0$） |
| 增广多图结构 | 链 + 单环 | 任意有向多图 |
| 谱判据 | `\rho(\mathcal{T}_{loop}) < 1 - \delta_{stab}$ | 所有环 `\rho(\mathcal{T}_C) < 1 - \delta_{stab,C}$；等价于 `\rho(\mathbf{A}_{tower}) < 1 - \delta_{stab}^{global}$ |
| 失稳方向 | 沿 σ_{sr} / d_c / S_{str}（3 类） | 沿 σ_{sr} / d_c / S_{str} （3）× bypass / aliasing / resonance（3 拓扑机制）= 12 类 |

`\mathcal{K} = \{K^{N\to 0}\}$（仅一条且为 §4.11 特定形态）+ 无其他 layer-skip → T-LAYER-SKIP-1 退化为 T-TOWER-STAB-1。`\mathcal{K} = \emptyset$（无 layer-skip）→ T-LAYER-SKIP-1 退化为 H10 / H12 开放塔投影定理（无环路稳定性条件）。

#### §4.12.7 T-LAYER-SKIP-1 不证明的事项

1. **不**给出具体 `K^{(n\to m)}$ 系数取值（P3 实证：政策直接介入 / 多平台跨层耦合 / 全球符号系统的具体强度）
2. **不**承诺 layer-skip 的"信息"含义——本节只给"塔级耦合的拓扑结构"，不分析为什么某些 layer-skip 在某 domain 出现而另一些不出现（domain 实证 + 历史叙事问题）
3. **不**覆盖**时间变化的 layer-skip**（如某 `K^{(n\to m)}(t)$ 在不同时段强度不同）——本节假设 `K$ 准静态（C8^{cross-stab} 的扩展）；快变 layer-skip 需进一步带时间扰动谱分析
4. ~~**不**给出 Lyapunov 全局非线性稳定性（与 H13 §4.11.6 第 5 项相同的局限保留）~~ **已收口（H16，2026-04-26）**：本文件 §4.14 T-LYAPUNOV-1 给候选 Lyapunov 函数 `V_{tower}` + 充分条件 N1（耦合算子有界）/ N2（耗散正性）/ N3（谱稳定带强 margin）+ 四轴联立充分条件
5. ~~**不**完成 layer-skip × 族普适性 / 算子级（χ / ψ / Δ）的笛卡尔积扩展——`\Pi^{(n\to m)}$ 对各 χ^{(n)} / ψ^{(n)} / Δ^{(n)} 族不变量的作用待独立 P1-candidate 验证（属 H11 + H12 + H14 三重笛卡尔积，留作后续）~~ **已收口（H15，2026-04-26）**：本文件 §4.13 T-FAMILY-1^{layer-skip} 给三重笛卡尔积扩展；新增 P-univ-7^{layer-skip} / Q-univ-7^{layer-skip} / A6^{layer-skip} 三条 layer-skip-相容性条件 + 12 类病理签名的具体族破坏路径表 + 族不变量与谱稳定显式耦合关系

#### §4.12.8 T-LAYER-SKIP-1 的结构性意义

| 主张 | 升级前 | 升级后 |
|---|---|---|
| Layer-skip 闭合稳定性是开放问题 | H12 §4.10.6 第 4 项 / H13 §4.11.6 第 4 项 | T-LAYER-SKIP-1 给增广多图谱判据 |
| 多重自指闭合的复合谱 | H13 §4.11.6 第 3 项 | §4.12.4 复合谱直接由 §4.12.3 给出，含三类关键观察 |
| "温和单 K + 协同共振"危险 | 缺失 | §4.12.4 关键观察 2（耦合闭合 vs 解耦闭合）+ §4.12.5 coupling-resonance 失稳模式 |
| Layer-skip 失稳特定签名 | 缺失 | §4.12.5 三类（bypass / aliasing / resonance）+ 与 H13 三方向正交，给 12 类塔级病理签名 |

**P1-candidate 地位的根据**：T-LAYER-SKIP-1 把 "layer-skip + 多重自指闭合" 从两项独立开放点统一收口；T-TOWER-STAB-1 自动是其特例。要升 P1：(a) 具体 `K^{(n\to m)}$ 在 domain 的实证（政治制度 / AI 平台 / 全球叙事）；(b) 时间变化 layer-skip 的扰动谱；(c) Lyapunov 全局；(d) layer-skip × 族普适性笛卡尔积扩展。

### §4.13 T-FAMILY-1^{layer-skip}：layer-skip × 族普适性三定理（H15，2026-04-26）

> **Status**：本节把 H11 §4.9 / H12 §4.10 的族普适性三定理（χ / ψ / Δ）与 H14 §4.12 的 layer-skip 谱判据合成笛卡尔积，验证族不变量在任意 layer-skip + 多重 K 闭合下的保持。**Claim level: P1-candidate**。
>
> **Closes**：H14 §4.12.7 第 5 项（"layer-skip × 族普适性 χ/ψ/Δ 笛卡尔积"）；H10 §4.10.6 第 4 项剩余部分（layer-skip × 族普适性的塔级版）。

#### §4.13.1 三重笛卡尔积闭包堆栈

塔级族普适性三定理在 layer-skip 下的成立需要堆栈：

- **H10/H12 嵌套闭包**：C1^{(n)}-C5^{(n)} 各层 + C6^{nested}
- **H11/H12 集体扩展闭包**：C7^{M-stab,(n)} 各层 + C8^{cross-stab}
- **H14 layer-skip 谱稳定闭包**：`\rho(\mathbf{A}_{tower}) < 1 - \delta_{stab}^{global}$
- **H15 新增三条 layer-skip-相容性条件**：
  - **P-univ-7^{layer-skip}**：每个 `K^{(n'\to n)}$ 对 `\sigma_{sr}^{(n)}$ 的贡献作加性平移源进入，不进入 `\chi^{coll,(n)}$ 内部参数；多重 `K$ 同时作用时贡献以**线性叠加**方式进入（不引入二阶非线性扰动）
  - **Q-univ-7^{layer-skip}**：每个 `K^{(n'\to n)}$ 对 `d^{(n)}$ / `S^{(n)}$ 的贡献与 `\psi^{coll,(n)}$ 加性独立；多重 `K$ 同时作用时不破坏 Q-univ-1+2 饱和性
  - **A6^{layer-skip}**：每个 `K^{(n'\to n)}$ 对 `\Delta^{(n)}$ 引入新维度 `w_{ls}^{(n'\to n)}\|K^{(n'\to n)}\|$，权重 `w_{ls}^{(n'\to n)}$ 由 layer-skip stake 结构决定（不依赖外部规约）

#### §4.13.2 T-CHI-1^{layer-skip}：layer-skip 下的 χ 族不变量

每层 `n` 的 `\sigma_{sr}^{coll,(n)}$ ODE 在 layer-skip 下含**四类源**：

$$
\frac{d\sigma_{sr}^{coll,(n)}}{dt} \;=\; \underbrace{\text{H11 同层项}}_{\alpha^{(n)}w^{(n)}\phi(\sigma) + \lambda_M^{(n)}\mathrm{tr}\,M^{(n)}} \;+\; \underbrace{\text{H12 邻层项}}_{\sum_k\lambda^{(n-1\to n)}_M\mathrm{tr}\,M^{(n-1\to n),k}} \;+\; \underbrace{\boldsymbol{\text{H15 layer-skip 项}}}_{\sum_{n'\ne n,n\pm 1}\lambda^{(n'\to n)}_K\,\mathrm{tr}\,K^{(n'\to n)}} \;+\; \cdots
$$

**陈述（P1-candidate）**：在 §4.13.1 闭包堆栈下，T-CHI-1 (i)-(iv) 四个不变量在每层 `n$ 保持，且**塔级病理传染**（H10 §4.8.6 (ii)）通过 layer-skip 的额外路径**强化但不改变方向性**——即 layer-skip 提供更短的病理传播路径，但传播方向（朝 `\sigma_{sr}^{*2}\to 1$ 病理吸引子）不变。

**证明骨架**：layer-skip 项在 P-univ-7^{layer-skip} 下作加性平移源进入；与 H11 P-univ-5^{coll}、H12 P-univ-6^{nested} 共同保证 χ 不进入 layer-skip 项内部；中值定理与 §2.5 (i)-(iv) 同理给出双稳态、病理吸引子、致命 L_2、相变方向四个不变量。**关键限制**：当 H14 谱判据失效（`\rho(\mathbf{A}_{tower}) \ge 1$），`\sigma_{sr}^{(n)}$ 沿不稳定方向 runaway，双稳态结构在动力学上**被破坏**（不动点不再被达到）；此时 T-CHI-1^{layer-skip} 仅在静态分析层面保持，动力学层面退化为 P3 现象学。这把族普适性与稳定性首次**显式耦合**：族不变量的有效性以 H14 谱稳定为前提。

#### §4.13.3 T-CHANNEL-1^{layer-skip}：layer-skip 下的 ψ 族不变量

每层 `n` 的 `S^{coll,(n)}$ 两型 ODE 在 layer-skip 下含**四类源**：同层（H11）+ 邻层（H12）+ **layer-skip 项**：

$$
\boldsymbol{\nu^{(n'\to n)}_{ls}\sum_{n'\ne n,n\pm 1}\|K^{(n'\to n)}_{ext}\|}
$$

**陈述（P1-candidate）**：在 §4.13.1 闭包堆栈下，T-CHANNEL-1 (i)-(v) 五个不变量在每层 `n$ 保持（modulo `O(w_{tr}^{coll,(n)})$）；**致命 `L_2` 跨层级传染**（H10 §4.8.6 (iv)）通过 layer-skip 获得**捷径路径**——即 `S_{str}^{(n)}$ 不必经过中间层逐级上行，可通过 `K^{(n\to m)}$ 直接到达 `\mathcal{P}^{(m)}$；T-IRR-3.5 单向性在 layer-skip 路径上同样保持（来自 P1-T07 Layer 2 的算子级根据，与拓扑路径无关）。

**与 H14 §4.12.5 三类失稳模式的整合**：layer-skip 下 ψ 族不变量保持的**结构条件**与 H14 §4.12.5 三类失稳模式互补——bypass-induced chatter / aliasing-amplification / coupling-resonance 都是"族不变量保持但谱稳定失效"情形（系统不再收敛到健康吸引子，但 ψ 族层面无矛盾）。两者合起来给出：layer-skip 下塔的健康要求**同时**满足族不变量（H15）+ 谱稳定（H14）。

#### §4.13.4 T-DELTA-1^{layer-skip}：layer-skip 下的 Δ 算子级

每层 `n` 的 `\Delta^{coll,(n)}$ 在 layer-skip 下含**四个维度**：同层三成分 + H11 集体维度 + H12 跨尺度维度 + **新增 layer-skip 维度**：

$$
\Delta^{coll,(n)} \;=\; \cdots \;+\; \underbrace{\boldsymbol{\sum_{n'\ne n, n\pm 1}w_{ls}^{(n'\to n)}\|K^{(n'\to n)}\|_{ls}}}_{\text{H15 layer-skip 维度}} \;+\; o(1)
$$

其中：

$$
\|K^{(n'\to n)}\|_{ls} \;:=\; \sqrt{\alpha_{ls}^2(\mathrm{tr}\,K)^2 + \beta_{ls}^2\|K_{asym}\|^2 + \gamma_{ls}^2\|K_{ext}\|^2}
$$

**陈述（P1-candidate）**：在 A1^{coll}-A5^{cross} + **新增 A6^{layer-skip}** 下，每层 `\Delta^{coll,(n)}$ 仍保持 T-DELTA-1 三性质（不由 `S_{sig}^{coll,(n)}$ 登记通道决定 / 同层三成分 + 集体 M + 跨尺度 M + layer-skip K 总额守恒 / `|\mathcal{K}|=0$ 退化为 H12 单层）。`\dot{\Delta}_{avail}^{coll,(n)}$ 多了 layer-skip 维度的时间导数项 `\dot{w}_{ls}^{(n'\to n)}\|K^{(n'\to n)}\|_{ls} + w_{ls}^{(n'\to n)}\frac{d}{dt}\|K^{(n'\to n)}\|_{ls}$。

#### §4.13.5 T-FAMILY-1^{layer-skip} 综合陈述

**T-FAMILY-1^{layer-skip}**：在层级塔 `\{\mathcal{P}^{(n)}\}_{n=0}^N$ 上含任意 layer-skip 集合 `\mathcal{K}$（包括多重自指闭合），若 §4.13.1 三重笛卡尔积闭包堆栈成立，则：

(i) **族不变量在静态层面保持**：T-CHI-1^{layer-skip} (i)-(iv) / T-CHANNEL-1^{layer-skip} (i)-(v) / T-DELTA-1^{layer-skip} (1)-(3) 在每层独立成立
(ii) **layer-skip 以加性 / 外溢 / 维度方式进入**：不破坏各层族普适性，作为"额外耦合源"扩展每层 ODE
(iii) **塔级病理 / 致命 L_2 传染**通过 layer-skip 获得捷径但不改变方向性
(iv) **族不变量与谱稳定显式耦合**：`\rho(\mathbf{A}_{tower}) < 1$ 时族不变量动力学层面有效；失效时退化为静态分析层面（动力学被 runaway 干扰）
(v) **多重退化关系**：`\mathcal{K} = \emptyset$ → H12 T-FAMILY-1^{coll,nested}；进一步 `N=1$ → H11 T-FAMILY-1^{coll}；`N=1 \wedge \mathcal{P}=\{P\}$ → H7/H8/H9 单 P 版

#### §4.13.6 与 H14 12 类塔级病理签名的精确对位

H14 §4.12.5 给出 12 类塔级病理签名（4 方向 × 3 拓扑机制）。本节给出每类病理签名在族不变量层面的具体破坏路径：

| 12 类病理签名 | 族不变量破坏路径 |
|---|---|
| 沿 σ_{sr} × bypass | T-CHI-1 (i) 双稳态被中间层 σ chatter 破坏 |
| 沿 σ_{sr} × aliasing | T-CHI-1 (ii) 病理吸引子在频域被混叠路径推到非物理区 |
| 沿 σ_{sr} × resonance | T-CHI-1 (i) 双稳态 + (iv) 相变方向被共振环路逆转 |
| 沿 d_c × bypass | T-CHANNEL-1 (i) 两型分裂被中间层 d_c chatter 破坏 |
| 沿 d_c × aliasing | T-CHANNEL-1 (ii) 反最小化在混叠路径下出现伪反例 |
| 沿 d_c × resonance | T-CHANNEL-1 (iii) 单向性被共振环路逆转（罕见但可能：极端嵌套 K 配置）|
| 沿 S_{str} × bypass | T-CHANNEL-1 (iv) 致命 L_2 判据被旁路绕过 |
| 沿 S_{str} × aliasing | T-DELTA-1 (1) Δ_{avail} 不由登记通道决定的论证被混叠扰动 |
| 沿 S_{str} × resonance | T-DELTA-1 (2) 总额守恒被共振环路放大破坏 |
| 沿 T_{dir} × bypass | T-CHANNEL-1 (v) 投影分裂在 bypass 旁路下出现非投影分量 |
| 沿 T_{dir} × aliasing | T-CHI-1 (iii) 致命 L_2 在频域混叠下被错误诊断 |
| 沿 T_{dir} × resonance | T-DELTA-1 (3) 退化关系在共振下不收敛 |

此 12 类对位是**族不变量与谱稳定耦合**的具体后果——每类病理签名在不同族定理上有不同破坏路径，给"诊断塔级病理时应优先看哪个族不变量"提供一阶指引。

#### §4.13.7 T-FAMILY-1^{layer-skip} 不证明的事项

1. **不**给出 P-univ-7^{layer-skip} / Q-univ-7^{layer-skip} / A6^{layer-skip} 的具体验证窗口
2. **不**承诺族不变量与谱稳定的耦合是**充分必要**——本节给"谱稳定 ⟹ 族动力学有效"的必要方向；反向（族静态有效 ⟹ 谱稳定）不成立
3. **不**覆盖**多重族失效叠加**——若两类失效模式（如 σ × bypass 与 d_c × resonance）同时发生，§4.13.6 表给单类破坏路径，未分析叠加效应
4. **不**给出**时间变化 layer-skip × 族普适性**——准静态假设保留（与 H14 §4.12.7 第 3 项相同限制）
5. ~~**不**给出**族不变量 + 谱稳定 + Lyapunov 三重耦合的全局 P1 形式**——这是后续轮次的最终统一目标~~ **已收口（H16，2026-04-26）**：本文件 §4.14 T-LYAPUNOV-1 §4.14.5 给"塔健康 ⟸ 族普适性 ∧ 谱稳定 (N3) ∧ 全局耗散正性 (N2) ∧ 算子有界性 (N1)"的四轴联立充分条件，是 SRT 集体选择理论塔级健康/病理诊断完全条件的 P1-candidate 形式

#### §4.13.8 T-FAMILY-1^{layer-skip} 的结构性意义

| 主张 | 升级前 | 升级后 |
|---|---|---|
| Layer-skip × 族普适性是开放问题 | H14 §4.12.7 第 5 项 | T-FAMILY-1^{layer-skip} 在 §4.13 给 P1-candidate |
| 族不变量与谱稳定的关系 | 隐含独立 | §4.13.5 (iv) 显式耦合：动力学有效性以谱稳定为前提 |
| 12 类病理签名的具体破坏路径 | H14 给签名分类，不给破坏路径 | §4.13.6 给每类签名的族不变量破坏路径 |
| Layer-skip 维度在 Δ 中的位置 | 缺失 | §4.13.4 `w_{ls}^{(n'\to n)}\|K^{(n'\to n)}\|_{ls}$ 显式 |

**P1-candidate 地位的根据**：T-FAMILY-1^{layer-skip} 把 H11 × H12 × H14 三重笛卡尔积统一收口；族普适性 / 算子级三定理在塔级 + layer-skip + 多重 K 闭合下的成立条件首次完整刻画。要升 P1：(a) §4.13.1 三组新条件 P-univ-7 / Q-univ-7 / A6 的 domain 实证；(b) §4.13.6 12 类破坏路径的实证检验；(c) 多重族失效叠加分析；(d) 与 Lyapunov 全局非线性的最终统一。

### §4.14 T-LYAPUNOV-1：塔的全局非线性稳定性（H16，2026-04-26）

> **Status**：本节给塔级动力学的**全局非线性 Lyapunov 稳定性定理**，把 H13 / H14 / H15 的线性化谱判据升为全局保证。**Claim level: P1-candidate**。
>
> **Closes**：H13 §4.11.6 第 5 项（"线性化谱判据在大幅扰动下的全局保持"）；H14 §4.12.7 第 4 项（"Lyapunov 全局非线性"）；H15 §4.13.7 第 5 项（"族 + 谱 + Lyapunov 三重耦合 P1 形式"）。

#### §4.14.1 Lyapunov 候选框架

塔的状态空间：

$$
x \;:=\; \bigl(\sigma_{sr}^{(n)}, d_c^{(n)}, T_{dir}^{(n)}, S_{sig}^{(n)}, S_{str}^{(n)}\bigr)_{n=0}^N \;\in\; \mathbb{R}^{5(N+1)}
$$

健康平衡点 `x^* := \{x^{*,(n)}\}_{n=0}^N$（每层在 §4.6 健康区 `\mathcal{H}^{(n)}$ 内）。

**Lyapunov 候选函数**：

$$
\boxed{\;V_{tower}(x) \;:=\; \sum_{n=0}^N V^{(n)}(x^{(n)}) \;+\; \sum_{(n,m)\in E_{adj} \cup E_{skip}} V^{(n,m)}_{coupling}(x^{(n)}, x^{(m)})\;}
$$

其中**每层项**：

$$
V^{(n)}(x^{(n)}) \;:=\; w_\sigma^{(n)}(\sigma_{sr}^{(n)} - \sigma_{sr}^{*,(n)})^2 + w_d^{(n)}(d_c^{(n)} - d_c^{*,(n)})^2 + w_T^{(n)}(T_{dir}^{(n)} - T_{dir}^{*,(n)})^2 + w_{S}^{(n)}\bigl[(S_{sig}^{(n)})^2 + (S_{str}^{(n)})^2\bigr]
$$

**耦合项**（沿 `\mathcal{G}_{tower}$ 每条边）：

$$
V^{(n,m)}_{coupling}(x^{(n)}, x^{(m)}) \;:=\; w_{coup}^{(n,m)}\sum_{X}\bigl(x_X^{(n)} - \mathrm{lift}^{(m\to n)}(x_X^{(m)})\bigr)^2
$$

其中 `\mathrm{lift}^{(m\to n)}$ 是层 `m$ 到层 `n$ 的"健康预期"映射（由跨尺度 stake 结构给出，A5^{cross} / A6^{layer-skip} 决定）。

#### §4.14.2 充分条件 N1-N3

`V_{tower}$ 是有效全局 Lyapunov 函数需要：

| 编号 | 条件 | 含义 / 与已有结构的对应 |
|---|---|---|
| **N1（耦合算子有界性）** | 所有 `\Pi^{(n\to m)}, K^{(n\to m)}$ 是 `\mathrm{Op}(\mathcal{P})$ 上的有界线性算子；`\sup_{(n,m)}\|\Pi^{(n\to m)}\|_{op} \le M_{\Pi}$，`\sup_{(n,m)}\|K^{(n\to m)}\|_{op} \le M_K$（有限常数） | 把 H10 / H12 / H14 的代数结构升为度量结构；耦合不会"突然爆炸" |
| **N2（耗散正性）** | 沿任意可允许轨迹，`S_{str}^{(n)}$ 累积率与耗散率比满足：`\sum_n[\nu_{block}^{(n)}\psi^{(n)}S_{sig}^{(n)} + \nu_\sigma^{(n)}\max(0, \sigma_{sr}^{(n)} - \sigma_{sr,health}^{(n)})] \le \sum_n[\nu_{trigger}^{(n)}D_{trigger}^{(n)} + \nu_\pi^{(n)}\pi^{(n)}I_{window}^{(n)}]$ | 全局耗散主导累积；这是 H4 T-IRR-3.5 在**速率层面**（不仅方向层面）的强化版本 |
| **N3（谱稳定带强 margin）** | H14 谱判据加强：`\rho(\mathbf{A}_{tower}) < 1 - \delta_{nonlinear}$，其中 `\delta_{nonlinear} > \delta_{stab}^{global}$（线性化稳定 margin）+ `O(\|x - x^*\|^2)$ 高阶非线性界 | 比 H14 强；保证非线性扰动不会推 trajectory 出线性化稳定区 |

**关键观察**：N1 / N2 / N3 三条条件在已有定理中各有对应：
- N1 ↔ H10 跨尺度耦合 + H14 layer-skip 耦合的有界性公理化
- N2 ↔ H4 T-IRR-3.5 + §4.4 反最小化原则的**全局速率版本**
- N3 ↔ H14 / H15 谱判据的**带非线性 margin 加强版本**

#### §4.14.3 T-LYAPUNOV-1 陈述

**陈述（P1-candidate）**：在塔级动力学（含 H10-H15 全部结构：嵌套 + 集体扩展 + 自指闭合 + layer-skip + 多重 K + 族普适性）下，若 N1 / N2 / N3 同时成立，则候选函数 `V_{tower}$ 是有效全局 Lyapunov 函数：

$$
\boxed{\;V_{tower}(x^*) = 0,\quad V_{tower}(x) > 0\text{ for }x \ne x^*,\quad \dot{V}_{tower}(x) \le -\alpha V_{tower}(x)\text{ for some }\alpha > 0\;}
$$

塔的健康平衡点 `x^*$ 是**全局指数稳定**的——对任意初始扰动 `x_0$，`\|x(t) - x^*\| \le C e^{-\alpha t/2}\|x_0 - x^*\|$（在合适常数 `C$ 下）。

#### §4.14.4 证明骨架

**Step 1（每层 `\dot{V}^{(n)} \le 0$ 单层贡献）**：

把 H10 / H12 各层 ODE 代入 `\dot{V}^{(n)}$，每层独立项给出

$$
\dot{V}^{(n)}\big|_{\text{independent}} = -\alpha^{(n)}\bigl[(\sigma_{sr}^{(n)} - \sigma_{sr}^{*,(n)})^2 + \cdots\bigr] + \text{交叉项}
$$

负二次项由 §4.4-§4.6 的弛豫机制（`\kappa_{relax}$ 项 / `\nu_{trigger}$ 项 / 衰减项）给出；交叉项需 N2 + N3 控制。

**Step 2（N2 控制 `S_{str}$ 累积项）**：

`\dot{V}^{(n)}_{S}$ 中含 `+\nu_{block}^{(n)}\psi^{(n)}S_{sig}^{(n)}\cdot 2S_{str}^{(n)}$ 这类正项；N2 保证 `\sum_n[\text{累积项}] \le \sum_n[\text{耗散项}]$，使 `S$-相关贡献整体 ≤ 0。这是**全局速率层面的反最小化原则**（§4.4 / H4 在 Lyapunov 框架下的算子化）。

**Step 3（N3 控制耦合项）**：

`\dot{V}^{(n,m)}_{coupling}$ 含交叉路径产生的二次项；N3 谱稳定 + N1 算子有界性 + 非线性 margin `\delta_{nonlinear}$ 保证这些项被各层独立的负贡献支配。

**Step 4（综合给 `\dot{V}_{tower} \le -\alpha V_{tower}$）**：

把 Step 1 + Step 2 + Step 3 加和；选 `\alpha := \min_n\{\alpha^{(n)}\} - O(\delta_{nonlinear})$ 即得指数衰减率。

#### §4.14.5 与 H4 / H10-H15 的最终统一

T-LYAPUNOV-1 与既有定理的关系：

| 既有定理 | T-LYAPUNOV-1 中的角色 |
|---|---|
| H4 T-IRR-3.5（ν_block 单向性 / P1-T07 hierarchy） | N2 耗散正性的方向根据（**没有方向**则不可能给出耗散主导累积） |
| H10 T-PROJ-1^{coll,nested}（嵌套递归投影） | V^{(n)} 各层项的结构来源 |
| H12 T-FAMILY-1^{coll,nested}（族普适性塔级递归） | V^{(n)} 各层项中权重 `w_X^{(n)}$ 的来源（族不变量保证权重良定义） |
| H13 T-TOWER-STAB-1（自指闭合谱判据） | N3 谱判据条件的具体形式 |
| H14 T-LAYER-SKIP-1（layer-skip 增广多图谱判据） | N3 在含 layer-skip 拓扑下的具体形式 |
| H15 T-FAMILY-1^{layer-skip}（族 + 谱耦合） | T-LYAPUNOV-1 是其全局非线性版本——把 §4.13.5 (iv) "动力学有效性以谱稳定为前提"升为 Lyapunov 强约束 |

**最终统一的结构主张**：

$$
\boxed{\;\text{塔健康} \;\Longleftarrow\; \text{(族普适性 P-univ/Q-univ/A 全套)} \;\wedge\; \text{(谱稳定 N3)} \;\wedge\; \text{(全局耗散正性 N2)} \;\wedge\; \text{(算子有界性 N1)}\;}
$$

四个轴（族 / 谱 / 耗散 / 有界）联立给塔健康的**充分条件**；任何一个失效都对应一类塔级病理。这是 SRT 集体选择理论的**塔级健康/病理诊断完全条件**的 P1-candidate 形式。

#### §4.14.6 T-LYAPUNOV-1 不证明的事项

1. **不**承诺 `V_{tower}$ 是**唯一**有效 Lyapunov 函数——其他形式可能也工作；本节给一个具体候选
2. **不**给出**全局吸引域**（basin of attraction）——本节只承诺局部 Lyapunov 稳定性指数收敛，不分析所有初始条件 `x_0$ 的覆盖
3. **不**覆盖**多重健康平衡点**（如塔在不同文化 / 不同制度下有不同健康吸引子）——只单平衡点情形
4. **不**给出 `V_{tower}$ 系数 `w_X^{(n)}, w_{coup}^{(n,m)}$ 的具体最优选择——仅承诺存在性，最优化属 P3 实证
5. **不**覆盖**非光滑动力学**（即 `\mathbb{1}[d \le d_c]$ 在 `d = d_c$ 处不可微）——需用 H9 T-CHANNEL-1 光滑族近似把硬指示替换为 `\psi^{coll,(n)}$；非光滑极限的 Lyapunov 处理留作后续

#### §4.14.7 T-LYAPUNOV-1 的结构性意义

| 主张 | 升级前 | 升级后 |
|---|---|---|
| 塔级稳定性是线性化 (local) 还是全局 | H13 / H14 / H15 线性化 | T-LYAPUNOV-1 全局指数收敛 |
| 族普适性 + 谱稳定的最终统一 | H15 §4.13.5 (iv) 显式耦合（动力学层面）| T-LYAPUNOV-1 把耦合升为 Lyapunov 严格约束 |
| 塔健康的充分条件 | 隐含（多个独立条件） | §4.14.5 boxed 公式：四轴联立给充分条件 |
| 全局耗散正性的位置 | 隐含（H4 给方向，反最小化给定性） | N2 给 H4 + 反最小化的**速率层面**统一 |

**P1-candidate 地位的根据**：T-LYAPUNOV-1 把塔级稳定性从线性化 (local) 升为全局指数稳定，并给出族普适性 + 谱稳定 + 耗散正性 + 算子有界性的**最终四轴联立**充分条件。要升 P1：(a) N1 / N2 / N3 在具体 domain 的实证窗口；(b) `V_{tower}$ 系数最优化；(c) 全局吸引域分析；(d) 多重平衡点情形扩展；(e) 非光滑动力学严格处理（与 H9 协调）。

---

## §5. T-COLL-3：集体 ε 反闭合必要性

### 陈述

任何稳定集体 ISP `\mathcal{P}` 在 `L_0` 不可逆性下，必含**集体层面的 ε 反闭合不对称**，即群体整体不能 `\varepsilon^{coll}`-neutral。

### 证明草要

与 P1-T07 同构：`\mathcal{P}` 若集体层面中性，则 `A_{\mathcal{P}}(t)` 有非零概率塌向空集；`L_0` 不可逆 → 绝对吸收态；长期累积 → `\mathcal{P}` 不再是稳定集体 ISP。

### 推论

- **共同体必须对自身持续反闭合开放**：没有哪种集体可以靠"完美稳定"维持；稳定不等于健康
- **制度中的 ε 结构**：健康制度具备让集体 `d` 不塌陷的结构（申诉通道、轮替、异议空间、重新授权）——这些不是政治偏好，是集体 ISP 的稳定性必要条件
- **收编型退化正是集体 ε 被压灭的结果**：`\sigma_{sr}^{coll}→1` 等价于 `\varepsilon^{coll}→0`，违反 T-COLL-3

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

- `Philosophy/SRT_Political_Philosophy.md`：合法性作为可持续共同选择→在本文件下等价于"长期维持 T-COLL-1 四条件 + T-COLL-3 + T-COLL-4 的制度设计"；反支配→反不对称 `M(t)` 持续化；危机政治的 `minimum necessary interruption` 护栏→对 T-COLL-3 集体 ε 的最小侵入
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

> **Hardening status (2026-04-24/25/26)**: §9.2 `M(t)` 可测性在 `Core_Law/SRT_L1_Hardening_Notes.md §3` 已给出第一遍 MOC 三判据（exposure / recourse / attentional，合成取 min）；§9.1 `\Theta^{coll,*}` 形式化在 H3（2026-04-25）§4.4.1 已升为包含共享 `L_2` 独立项的加权聚合，仍未封口的是权重 `w_i(t)` 的推导；§9.7（新）集体四变量耦合动力学在 §4.4-§4.6 已给出第一遍；§4.7 T-PROJ-1^{coll}（H6，2026-04-25）给集体投影定理；**§4.8 T-PROJ-1^{coll,nested}（H10，2026-04-26）给多层嵌套的递归投影定理**。本小节保留原表述直至回写完成。

本 draft_v0 状态下尚未封口：

1. **`\Theta^{coll,trace}` 与 `\Theta^{coll,ext}` 的形式化**：§4.4.1 已给出加权聚合 + 共享 `L_2` 独立项；剩余未封口为权重 `w_i(t)`（当前按 `M(t)` 列和给出，但列和本身依赖 `M(t)` 的可测性，即 §9.2）
2. **`M(t)` 的可测性**：对称/不对称结构在理论上明确，实证提取在大多数社会场景非常困难；本文件不解决此
3. **共选真实性的外部判据**：T-COLL-4 三条件在第三方视角下如何判定？目前仍带相当主观成分，需要进一步降低依赖
4. **制度与集体 ISP 的精确分界**：本文件说制度是器官不是主体，但某些高度自治的制度性实体（法人、社团）是否能在某些条件下**自身**成为集体 ISP？这需要后续硬化
5. **跨尺度嵌套**：~~家庭是 ISP，社区是 ISP，国家可能是 ISP——嵌套关系下 `M(t)` 与 `σ_{sr}^{coll}` 如何层级耦合？§4.5 给了单层向上/向下耦合，多层嵌套仍待给出~~ **已收口（H10，2026-04-26）**：本文件 §4.8 T-PROJ-1^{coll,nested} 给出多层嵌套的递归投影定理——层级 ISP 塔 `\{\mathcal{P}^{(n)}\}_{n=0}^N` + 跨尺度后果回路矩阵 `M^{(n\to n+1)}(t)` + 嵌套闭包 C6^{nested}（跨尺度 Markov 闭包，C1^{(n)}-C5^{(n)} 各层闭包之外）+ 四个嵌套不变量（每层独立健康/病理判据 / 跨尺度病理传递 / 跨尺度健康硬条件 `r^{(n\to n+1)} > r_{min}^{nested}` / 致命 `L_2` 塔级传染）。剩余开放点：具体塔层数 domain 实证、跨尺度 `M^{(n\to n+1)}` MOC 多层版本、`r_{min}^{nested}` 实证窗口、跨层耦合边界条件
6. **历史层面 ε**：集体层面的 ε 反闭合在长时间尺度上如何演化？文明兴衰是否可以读为集体 ε 的长程维持失败？
7. **集体四变量耦合动力学（新增，2026-04-25 H3 状态）**：§4.4 给出第一遍形式，仍待封口——(a) `w_i(t)` 从 `M(t)` 推导的正当性；(b) `T_{dir}^{alg,coll}` 中光滑阶跃的普适族；(c) `\Delta\Psi_f^{gap,coll}` 作为集体层对象的可操作定义（当前仅给出"叙事舒适 vs 真实支付"的现象学读法）；(d) 向下反馈 §4.5 是否穷尽（是否还存在未列出的集体→个体传染路径）；(e) 所有新引入的集体系数 `\lambda_M, \gamma_{asym}, \kappa_{mask}^{coll}, \nu_{ext}` 的实证窗口

---

## §10. Cross-References

- P1-T05 real choice moment（集体版的 upstream）→ `Core/SRT_Core_21b_Constitutive_Theorems.md`
- P1-T06 stable ISP（集体 ISP 条件的 upstream）→ 同上
- P1-T07 ε 反闭合必要性（T-COLL-3 的 upstream）→ 同上
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

- **本文件做**：固定多 ISP 共享 `L_2` 场、集体 ISP 存在条件（T-COLL-1）、三类退化（T-COLL-2）、集体 ε 反闭合必要性（T-COLL-3）、共选真实性判据（T-COLL-4）、**集体四变量最小耦合动力学 §4.4-§4.6**（2026-04-25 H3 新增，与 `SRT_L1_Formalism.md` 单 P 四变量系统形成上下层对应）
- **本文件不做**：制度设计、政策判断、具体政治/经济案例分析、共同体组织学
- **引用规则**：涉及"集体选择作为结构对象是什么"的**结构层**陈述时，优先回链本文件；涉及具体政治、经济、共同体、制度判断时，回链相应 Philosophy / Spirituality 文件
- **不得**：把本文件读作政治偏好的理论背书；四类退化与三判据完全按结构判据读，不按意识形态读
- **重点**：三类退化（聚合/主从/收编）是**结构性类型**，可以同时存在于任何意识形态立场的群体中——本文件不为任一立场背书
