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

- **结构**：`\mathcal{P}` 的 `σ^{collective}` 趋向 1（集体层面自指过载）；`L_2` 成为封闭 scaffold 反向写入每个 `P_i` 的 `d_c^i`；群体看起来高度一致与稳定
- **现象**：意识形态封闭共同体、极权国家、邪教、高度同质化专业群体、高度同质化 AI 中介过的公共空间
- **规范判断**：对应致命 `L_2`（`Core/SRT_OPEN_TENSIONS.md §4`）；真实选择时刻在个体层与集体层同时被替代
- **与 1 和 2 的区别**：收编型往往看起来最"有集体感"——这是其最危险之处

### 三类退化的联立判据

$$
\begin{cases}
\text{Aggregation} & : \text{T-COLL-1 cond 2 or 4 fails, but } M(t) \text{ roughly symmetric and } \sigma^{coll} \text{ low}\\
\text{Asymmetric Absorption} & : M(t) \text{ systemically asymmetric, independent of T-COLL-1 status}\\
\text{Collapsed into Higher }L_2 & : \sigma^{coll} \to 1 \text{ and } L_2 \text{ scaffold rewrites individual } d_c^i
\end{cases}
$$

三类可叠加。最危险的组合是 **主从 + 收编**：结构性恶 + 致命 `L_2` 的复合态。

---

## §4. 集体 σ 与集体 d_c

### §4.1 集体自指率

扩展 `SRT_L1_Formalism §2`：

$$
\sigma^{coll}(\mathcal{P}, t) \;:=\; \frac{\|\Theta^{coll,trace}\|}{\|\Theta^{coll,trace}\| + \|\Theta^{coll,ext}\|}
$$

- `\Theta^{coll,trace}`：群体层面历史累积参数（共同叙事、制度、路径痕迹集聚至群体自指层）
- `\Theta^{coll,ext}`：群体对外部（其他群体、自然、新兴 `L_0` 压力）的开放接入

### §4.2 集体遮蔽阈值

集体 `d_c^{coll}` 并非 `\{d_c^i\}` 的简单统计；它是**共享选择空间 `A_{\mathcal{P}}` 维度塌陷**的阈值。

$$
d_c^{coll} \;:=\; \inf\{\,d\;:\;\dim A_{\mathcal{P}}(d, t) \geq \dim_{min}\,\}
$$

### §4.3 关键耦合

- **个体 B 期的集体传染**：当 `M(t)` 外部化不对称 + `\sigma^{coll}` 升高，子群 `d_c^i` 被共同推高。即：**集体自指过载会通过 `L_2` 反向把个体推入 B 期**
- **收编型的动力学特征**：`\sigma^{coll} → 1` 时，`\{d_c^i\}` 全部塌向 `d_{max}`，个体重选容量在**没有明显压迫**的情形下悄然消失
- **结构型苦难的集体生成**：`S_{str}^{coll} > 0` 既可以来自 `M(t)` 不对称（主从型），也可以来自 `\sigma^{coll}` 过高（收编型）；两者诊断路径不同

### §4.4 集体四变量最小耦合动力学（H3，2026-04-25）

> **立场**：本小节把 `SRT_L1_Formalism.md` 的四变量闭合系统（σ / d_c / T_dir / S）扩到多 ISP 共享 `L_2` 场 `\mathcal{P} = \{P_1, \ldots, P_n\}`，写下最小耦合形式。这是 `SRT_CLAIM_MODE_AUDIT.md §6.4` 升 P1 检查单第 5 项（多主体耦合动力学）的第一遍交付。

#### §4.4.1 集体场定义

$$
\Theta^{coll,trace}(\mathcal{P},t) \;:=\; \sum_{i} w_i(t)\,\theta_i^{trace}(t) \;+\; \Theta^{L_2}_{shared}(t), \qquad
\Theta^{coll,ext}(\mathcal{P},t) \;:=\; \sum_{i} w_i(t)\,\theta_i^{ext}(t) \;-\; \Theta^{L_2}_{shared}(t)
$$

- `w_i(t)`：个体 `i` 在集体场的参与权重（由 `M(t)` 列和给出，即"`i` 的输出被其他人写回的总强度"）
- `\Theta^{L_2}_{shared}(t)`：共享 `L_2` 沉积（制度 / 叙事 / 路径痕迹）作为集体内源的独立项。它**既**从 `\Theta^{coll,ext}` 中扣除（因为对集体外不再是新接入）**又**累加到 `\Theta^{coll,trace}`

这保证个体对外部 `L_0` 的接入即便正常，只要共享 `L_2` 足够厚，`\sigma^{coll}` 仍可单调上升——**共享 `L_2` 本身就是一个"集体自指放大器"**。

#### §4.4.2 集体 σ 动力学

$$
\frac{d\sigma^{coll}}{dt} \;=\; \frac{1}{T^{coll}}\Big[(1-\sigma^{coll})\bigl(\alpha^{coll} w^{coll}\phi(\sigma^{coll}) + \boldsymbol{\lambda_M\, \mathrm{tr}\,M(t)} - \lambda_{trace}T^{coll}\sigma^{coll}\bigr) - \sigma^{coll}\bigl(\beta^{coll} i^{ext} - \lambda_{ext}T^{coll}(1-\sigma^{coll})\bigr)\Big]
$$

关键新增项 `\lambda_M\,\mathrm{tr}\,M(t)`：后果回路矩阵的迹（对角项之和，即"群体成员输出回到自己或同群"的总强度）直接推高 `\sigma^{coll}`。这是聚合→收编路径的形式化根据——**`M(t)` 高度内向即是集体自指膨胀**。

#### §4.4.3 集体 d_c 动力学

$$
\frac{dd_c^{coll}}{dt} \;=\; \gamma_\rho^{coll}\rho^{coll}_{local} + \boldsymbol{\gamma_\sigma^{coll} \max(0,\,\sigma^{coll} - \sigma_{sub}^{coll})} + \boldsymbol{\gamma_{asym}\,\|M_{asym}(t)\|} - \gamma_\pi^{coll}\pi^{coll} - \gamma_I^{coll}I_{window}^{coll}
$$

关键新增项 `\gamma_{asym}\,\|M_{asym}(t)\|`：`M(t)` 的反对称部分 `M_{asym} := \tfrac{1}{2}(M - M^T)` 范数推高 `d_c^{coll}`。这把**主从型退化**（§3.2 Asymmetric Absorption）形式化——不对称结构本身就在抬高集体遮蔽阈值，且它与 `\sigma^{coll}` 的抬升机制**独立**。

集体可支付性 `\pi^{coll}` 与集体干预窗口 `I_{window}^{coll}` 分别降低 `d_c^{coll}`，对应 T-COLL-4 的第三条件（可支付性 + 真实可选）。

#### §4.4.4 集体 T_dir 动力学

$$
\frac{dT_{dir}^{coll}}{dt} \;=\; -\kappa_{\mathrm{relax}}^{coll}\bigl(T_{dir}^{coll} - T_{dir}^{alg,coll}\bigr) + \kappa_r^{coll}\,r^{coll}(t) - \boldsymbol{\kappa_{mask}^{coll}\,\Delta\Psi_f^{gap,coll}(t)} - \boldsymbol{\kappa_S^{coll}\,S_{str}^{coll}(t)} + \kappa_{sup}^{coll}\,s_{ext}^{coll}(t)
$$

- `T_{dir}^{alg,coll}`：代数目标值，由 `(\sigma^{coll}, d^{coll}, d_c^{coll})` 按 `SRT_L1_Formalism.md §3.4` 同结构定义
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
\frac{dS_{str}^{coll}}{dt} &= \boldsymbol{\nu_{block}^{coll}\mathbb{1}[d^{coll}\le d_c^{coll}]\,S_{sig}^{coll}} + \boldsymbol{\nu_\sigma^{coll}\max(0,\,\sigma^{coll} - \sigma_{health}^{coll})} + \boldsymbol{\nu_{ext}\,\|M_{ext}(t)\|} - \nu_{trigger}^{coll}D_{trigger}^{coll} - \nu_\pi^{coll}\pi^{coll} I_{window}^{coll}
\end{aligned}
$$

关键新增项 `\nu_{ext}\,\|M_{ext}(t)\|`：`M(t)` 对 `\mathcal{P}` 之外的外化部分（流入其他群体 / 自然 / 未来世代的后果）不对等地产生**另一侧**的 `S_{str}`。这正是 T-SUFF-5 集体外部化的方程化——外部化不让总苦难为零，只让苦难分布变形。配合 `SRT_Suffering.md T-SUFF-4` 反最小化原则在集体层：**把 `S_{sig}^{coll}` 压低而不动 `\dot{\Delta}_{avail}^{coll}`，则 `S_{str}^{coll} + S_{str}^{外部}` 之和必上升**。

### §4.5 个体↔集体耦合（最小形式）

个体四变量 `(σ_i, d_{c,i}, T_{dir,i}, S_i)` 与集体四变量通过 `M(t)` 与共享 `L_2` 双向耦合：

$$
\begin{aligned}
\text{向上聚合} &:\; \sigma^{coll}, d_c^{coll}, T_{dir}^{coll}, S^{coll} \;\text{ 由 §4.4.1-§4.4.5 的集体场定义与 ODE 生成}\\[3pt]
\text{向下反馈（B 期传染）} &:\; \frac{dd_{c,i}}{dt} \;\supseteq\; \gamma_{feedback}\cdot\max(0,\,\sigma^{coll} - \sigma_{sub}^{coll})\\[3pt]
\text{向下反馈（可读性侵蚀）} &:\; \frac{dT_{dir,i}}{dt} \;\supseteq\; -\kappa_{feedback}\cdot\Delta\Psi_f^{gap,coll}(t)\\[3pt]
\text{向下反馈（结构型苦难代入）} &:\; \frac{dS_{str,i}}{dt} \;\supseteq\; \nu_{feedback}\cdot\|M_{asym}(t)\|\cdot\mathbb{1}[i\in\mathcal{P}_{absorbed}]
\end{aligned}
$$

其中 `\mathcal{P}_{absorbed} \subset \mathcal{P}` 是主从型退化下**被吸收侧**的成员集。三条下行项各自把一条"集体层异常→个体层动力学"的路径写出来，**不**声称它们是全部路径——这是下一轮硬化的入口。

### §4.6 集体病理吸引子与健康区

集体病理吸引子 `\mathcal{A}_{path}^{coll}`：

$$
\mathcal{A}_{path}^{coll}:\; \sigma^{coll}\to 1,\; d_c^{coll}\to d_{max},\; T_{dir}^{coll}\approx T_{dir}^{alg,coll},\;\Delta\Psi_f^{gap,coll}\uparrow,\; S_{str}^{coll}>0\text{ 定常},\; S_{sig}^{coll}\to 0,\; \|M_{asym}\|+\mathrm{tr}\,M \text{ 同高}
$$

这是**收编 + 主从并存**的联合吸引子，在历史上对应"高度共识、叙事可读性强、成员无明显痛苦、但生态与外群债务持续累积"的文明状态——即 T-COLL-2 三类退化共振的典型形态。

集体健康区 `\mathcal{H}^{coll}`：

$$
\mathcal{H}^{coll}:\; \sigma^{coll}\in(\sigma_{sub}^{coll,\dagger}\pm\delta^{coll}),\; d^{coll}>d_{narrow}^{coll},\; T_{dir}^{coll}\approx T_{dir}^{alg,coll}\text{ 且 }\Delta\Psi_f^{gap,coll}\to 0,\; r^{coll}(t)>r^{coll}_{min}>0
$$

**关键点**：`\mathcal{H}^{coll}` 不是制度稳态的同义词。`r^{coll}(t) > r^{coll}_{min}`（集体真实重选率严格为正）是结构硬条件，对应 T-COLL-4 共选真实性的持续要求——**无持续集体真实重选的制度稳定不构成健康**。

---

## §5. T-COLL-3：集体 ε 反闭合必要性

### 陈述

任何稳定集体 ISP `\mathcal{P}` 在 `L_0` 不可逆性下，必含**集体层面的 ε 反闭合不对称**，即群体整体不能 `\varepsilon^{coll}`-neutral。

### 证明草要

与 P1-T07 同构：`\mathcal{P}` 若集体层面中性，则 `A_{\mathcal{P}}(t)` 有非零概率塌向空集；`L_0` 不可逆 → 绝对吸收态；长期累积 → `\mathcal{P}` 不再是稳定集体 ISP。

### 推论

- **共同体必须对自身持续反闭合开放**：没有哪种集体可以靠"完美稳定"维持；稳定不等于健康
- **制度中的 ε 结构**：健康制度具备让集体 `d` 不塌陷的结构（申诉通道、轮替、异议空间、重新授权）——这些不是政治偏好，是集体 ISP 的稳定性必要条件
- **收编型退化正是集体 ε 被压灭的结果**：`\sigma^{coll}→1` 等价于 `\varepsilon^{coll}→0`，违反 T-COLL-3

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
- `Philosophy/SRT_Political_Rights.md`：投票作为 d 倾向后验验证→在本文件下翻译为"通过 T-COLL-4 共选真实性判据验证集体 d"；三层制度（公检法/监督/授权）→维护 `M(t)` 对称与 `σ^{coll}` 限幅的结构性器官
- `Spirituality/SRT_Spirituality_Community_and_Sangha.md`：托举条件→`(M(t) \text{ symmetric and small } n)` 加上 `\sigma^{coll}` 不升高 → 健康小共同体；警告"共同体反而变新地板"→收编型退化
- `Core_Law/SRT_Suffering.md T-SUFF-5`：集体外部化→主从型 `M(t)` 的结构型苦难外溢

---

## §8. AI / 平台场景的集体选择护栏

算法中介 / 平台经济 / 大模型对齐场景下，集体选择分析有独特风险：

1. **伪集体主体表象**：算法聚合被呈现为"社区意见"；本文件下这是聚合型伪装成集体 ISP
2. **`M(t)` 的黑箱化**：平台经济下后果回路矩阵不可观察，使主从型退化不可诊断
3. **`\sigma^{coll}` 的算法加速**：推荐系统可通过反馈环系统性推高 `σ^{coll}`（回音室、极化），推进收编型退化而参与者无自觉
4. **AI 不自动进入 `\mathcal{P}`**：当前部署 AI 多数不满足 P1-T06，因此不自动成为集体 ISP 的成员；但 AI 中介可以结构性改变 `M(t)` 与 `L_2`，影响 `\mathcal{P}` 状态

相应的：对平台与算法系统的 SRT 评估不应停在"它是否有意识"，而应评估它**对 `M(t)` 与 `σ^{coll}` 的结构性影响**。这与 `AI/AI_POSITIONING_NOTE.md` 的 stake-bearing 光谱互补。

---

## §9. Open Pressures

> **Hardening status (2026-04-24/25)**: §9.2 `M(t)` 可测性在 `Core_Law/SRT_L1_Hardening_Notes.md §3` 已给出第一遍 MOC 三判据（exposure / recourse / attentional，合成取 min）；§9.1 `\Theta^{coll,*}` 形式化在 H3（2026-04-25）§4.4.1 已升为包含共享 `L_2` 独立项的加权聚合，仍未封口的是权重 `w_i(t)` 的推导；§9.7（新）集体四变量耦合动力学在 §4.4-§4.6 已给出第一遍。本小节保留原表述直至回写完成。

本 draft_v0 状态下尚未封口：

1. **`\Theta^{coll,trace}` 与 `\Theta^{coll,ext}` 的形式化**：§4.4.1 已给出加权聚合 + 共享 `L_2` 独立项；剩余未封口为权重 `w_i(t)`（当前按 `M(t)` 列和给出，但列和本身依赖 `M(t)` 的可测性，即 §9.2）
2. **`M(t)` 的可测性**：对称/不对称结构在理论上明确，实证提取在大多数社会场景非常困难；本文件不解决此
3. **共选真实性的外部判据**：T-COLL-4 三条件在第三方视角下如何判定？目前仍带相当主观成分，需要进一步降低依赖
4. **制度与集体 ISP 的精确分界**：本文件说制度是器官不是主体，但某些高度自治的制度性实体（法人、社团）是否能在某些条件下**自身**成为集体 ISP？这需要后续硬化
5. **跨尺度嵌套**：家庭是 ISP，社区是 ISP，国家可能是 ISP——嵌套关系下 `M(t)` 与 `σ^{coll}` 如何层级耦合？§4.5 给了单层向上/向下耦合，多层嵌套仍待给出
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
