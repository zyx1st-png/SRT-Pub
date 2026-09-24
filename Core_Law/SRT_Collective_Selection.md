---
id: SRT-COLLECTIVE-SELECTION
type: theory
tags: [Collective Selection, Multi-ISP, Co-Selection, Shared L2, L1]
status: draft
layer: L1
epistemic_layer: os
claim_mode: canonical
claim_level: P2 / P3
dependency: [SRT-CORE-21-MINIMAL-AXIOMS, SRT-ONE-FORMATION, SRT-CORE-21B-CONSTITUTIVE-THEOREMS, SRT-INDIVIDUATION, SRT-OCCLUSION-DYNAMICS, SRT-SUFFERING, SRT-L1-FORMALISM, SRT-T-DIR-CANONICAL, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL]
---

# SRT Collective Selection: Multi-ISP Co-Selection and Shared L_2 Dynamics

> **Role**: L1 canonical owner for declared multi-process / collective-selection structures, collective Stable-ISP standing candidates, consequence-return models, and conditional collective formal extensions.
> **Claim-level note**：本文默认是 **P2/P3 model-and-bridge surface**。T-COLL-1 是在已声明 group-level candidate unit 上应用 P1-T06 的 P2 structural/admission candidate；集体动力学、投影、诊断类型与 domain mapping 为条件性 P2/P3 模型。canonical ownership 固定词汇与路由，不自动赋予 P1 standing。
> **Does not define**：`One / Selection-position`、`d-value`、`\Psi_f`、`T_dir`、stable ISP、Selection occurrence 或 agency；它们的定义与判定仍以对应 canonical / downstream owner 为准。
> **Depends on**：`Core/SRT_Core_21b_Constitutive_Theorems.md`（P1-T06 stable ISP 与 absorption remainder）、`Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13`（ST-A conditional anti-closure / generative reselectability）、`Core_Law/SRT_Occlusion_Dynamics.md`、`Core_Law/SRT_Suffering.md T-SUFF-5`、`Core_Law/SRT_Individuation.md`、`Core_Law/SRT_L1_Formalism.md`。
> **RC-A boundary (2026-08-18)**：former P1-T05 / Real Choice Moment 不再承担集体 Selection 或 collective-ISP 的定义权。T-COLL-1 的 stable-ISP extension 回链 P1-T06；脚本、制度自动化、投票或共识本身既不能证明更强 agency，也不能反推“没有 Selection”。
> **R1 One-formation boundary (2026-09-11)**：`Core_Law/SRT_One_Formation.md` owns `One / Selection-position`. Relation-level or higher-order One language does **not** establish collective ISP automatically; T-COLL-1 remains the separate collective Stable-ISP standing gate. Shared `L_2`, `M(t)`, or collective `σ_{sr}^{coll}` therefore do not back-define One formation.
> **Standing / interpretation guards (Wave E4, 2026-09-16)**：collective Stable ISP 不等于 collective subject、Bearer、Agency、consciousness / phenomenality 或 generative health。`M(t)` 是 consequence-return / distribution model object，不是 health、morality、legitimacy、evil 或 injustice scalar。`σ_{sr}^{coll}` / `d_c^{coll}` 是 model-local coordinates；`T_{dir}^{coll}` 仅在 direction 独立准入后定义，`S_{sig}^{coll}` / `S_{str}^{coll}` 仅在 suffering 独立准入后定义。formal closure 不将任何分支升为 P1。
> **Relation**: This file does not replace `Philosophy/SRT_Political_Philosophy.md`、`Philosophy/SRT_Social_Economics.md`、`Spirituality/SRT_Spirituality_Community_and_Sangha.md`；它在它们**之前**，固定“多过程 collective-selection 结构如何声明与建模”的 L1 读法。规范性与制度判断仍在上述 domain 文件。
>
> **σ 符号命名空间（governance-canonical, 2026-04-25, `Core_Law/SRT_L1_Hardening_Notes.md §1`）**：本文件中集体自指率符号已在 2026-04-25 L1 Hardening Round 统一改写为 `σ_{sr}^{coll}` 族（含 `σ_{sr,sub}^{coll}, σ_{sr,health}^{coll}` 等历史派生标记），是个体自指率 `σ_{sr}` 的多过程场扩展。与 `Core/SRT_Core_22_Equations.md` 主方程状态场 σ 是**不同对象**。派生标记中的 `health` 只保留旧参数名，不赋予健康语义；少数遗留的 `σ^{coll}` 历史符号在前向引用与跨文件桥接段落中保留，读者按此命名空间转读。
> **σ^{coll} representation / boundary-scope truth-up (2026-08-29, S+R)**：`σ_{sr}^{coll}` 继承单体 `σ_{sr}` 的**规约性、可替换阶参**地位，但它不是单体 provenance 语义的简单复制。§4.4.1 明确把 shared `L_2` 按已声明 collective boundary 重分类为集体内源项，因此这里至少包含 **boundary-relative endogeneity**。当前 bare-norm `σ_{sr}^{coll}` 应读作在已声明集体边界、归属规则、参数表示与 norm/metric 下的 model-local collective historical/endogeneity proxy。不得由同名符号自动推出 `TRACE_individual = TRACE_collective`，也不得把其数值直接读成表示不变的自然量、当前因果控制份额、collective agency 或自然相边界。§4.7 `T-PROJ-1^{coll}` 只登记给定投影下的条件性 ODE 闭包目标；C1^{coll}-C5^{coll} 不证明该闭包，也不提供归属唯一性或 invariant metric。

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
- 集体层面的 d / Ψ_f / σ / S 用法分散，没有结构判据说什么算可作分析的 group-level selection unit；这一问题不等于 collective subjecthood 问题。

本文件填这一空。它**只固定**：

1. 多 ISP 共享 `L_2` 的结构对象；
2. 何时可以对已声明 group-level candidate unit 提出 collective Stable-ISP standing candidate，何时只有聚合；
3. 共选 vs 外部化 vs 退化三类结构性模式；
4. 与 `SRT_L1_Formalism.md` 三变量在多主体场下的扩展。

---

## §1. 基本结构对象

### Def-C-1 多 ISP 共享 L_2 场

给定已声明的 candidate-process 集合 `\mathcal{P} = \{P_1, P_2, \ldots, P_n\}`，若它们共享一个 `L_2` 场 `\mathbf{L_2}`（即：同一路径层痕迹 `ρ(p,t)` 可影响多个 `P_i` 的后续 candidate / selection conditions），则称 `(\mathcal{P}, \mathbf{L_2})` 为一个**多过程共享 L_2 场**。若某个模型要求成员各自是 Stable ISP，必须把这一 domain restriction 显式写出并分别核验 P1-T06；它不是所有 collective-interaction model 的 universal prerequisite。

共享并不意味着：
- 同一个 d-value（各 `P_i` 有各自 `d_i`）
- 同一个 Ψ_f（各 `P_i` 有各自可支付性 `\pi_i`）
- 同一个 σ（各 `P_i` 有各自自指率 `σ_i`）

共享只意味着：
- `ρ(p,t)` 作为路径层痕迹对所有 `P_i` 可见并影响其 `d_c^i(t)`

共享 retained structure 可以影响多个 candidate processes，但它本身不建立 higher-order One、collective Stable ISP 或 collective subject。

### Def-C-2 后果回路矩阵

在多 ISP 共享场中，定义**后果回路矩阵** `M(t) \in \mathbb{R}^{n \times n}`：

$$
M_{ij}(t) \;:=\; \text{degree to which consequences of }P_j\text{'s selection return to }P_i\text{'s future selection capacity}
$$

具体形式：`M_{ii}` 是 same-position / same-process consequence-return entry，`M_{ij}` 是 cross-position consequence-return entry。其数值、边界、时窗与 transfer semantics 都由声明模型规定。

`M(t)` 的结构性质可描述为：
- **对称 / 不对称**：cross-position return relation 的结构特征，不自动等于 moral reciprocity 或 injustice。
- **块对角**：子群内外 consequence-return 的相对稀疏性；不自动建立 autonomy 或 legitimacy。
- **行 / 列摘要**：声明模型中的 exposure / return diagnostics；其解释依赖索引定义、边界和测量窗口。

`M(t)` pattern 不自动建立 collective subjecthood、health、legitimacy、suffering、evil、domination 或 injustice。只有在已声明 burden/consequence model 的 boundary 与 transfer semantics 下，才可提出 burden externalization；suffering externalization 还要求受影响位置的 suffering registration 被独立建立。

### Def-C-3 共享选择空间

多 ISP 共享场中的**共享选择空间** `A_{\mathcal{P}}(t)`：

$$
A_{\mathcal{P}}(t) \;:=\; \{\,\text{option profiles }(a_1, \ldots, a_n)\,|\, a_i \in A_i(t)\,\wedge\, \text{realizability}(a_1, \ldots, a_n) \neq \emptyset\,\}
$$

realizability 条件要求选择组合在共享 `L_2` 下结构上可共存——它是比笛卡尔积更窄的真实联动空间。

> **AD-RCA-1 guard**：这里的 option profile 是**已经对象化后的高层 operational candidate space**，用于集体模型的可实现性分析；它不是 Selection 的底层定义。Option picking 只是 Selection 的一种下游特例，不得由本式反向推出 `Selection = choose one item from a pre-given menu`。

`\dim A_{\mathcal P}` 与 non-collapse 只是声明 candidate-space model 的属性，不是 universal value / health measure。

---

## §2. T-COLL-1：collective Stable-ISP standing / admission candidate

### 陈述

在 candidate group/unit/boundary 已被独立声明后，多过程共享场 `(\mathcal{P}, \mathbf{L_2})` 可以在以下四项负担均被建立时，作为在该 group-level candidate unit 上应用 P1-T06 的 **P2 collective Stable-ISP standing/admission candidate**：

1. **group-level iterativity**：在声明区间内，group-level process 重复接收当前有效、非等价的 candidates，而不是只回放封闭脚本。
2. **group-level perspective-bearing organization**：一个结构化 group-level view / state organization 参与后续 Selection。这是 standing language，不是 collective subjecthood 声明。
3. **group-level history-bearing writeback**：既往 group-level outputs / relations 在后续 group-level candidate / selection conditions 中继续具有 materially effective writeback。
4. **group-level continued selectability**：同一 history-bearing group-level process 能继续接收 candidates，且 consequence return 能进入该过程后续的 history / selection conditions。

### 陈述的最小形式

条件 1–4 分别对位 P1-T06 的 iterative / perspective-bearing / history-bearing / continued-selectable 负担。`M(t)` 可以在特定模型中 operationalize 条件 3/4 的 consequence return，但 `M(t)` symmetry、所谓 healthy range 或 non-externalization 都不是 T-COLL-1 的 standing requirement。T-COLL-1 不解决 OPEN 的 exact collective One / unit / scale-attribution problem，也不反向定义 One formation。

### 推论

- **共识、投票、制度自动化不是 standing 的充分条件**；它们的存在或缺席也不决定 primitive Selection 是否发生。
- T-COLL-1 PASS 只建立该声明单元的 collective Stable-ISP standing candidate；它不建立 collective subject、Bearer、Agency、consciousness / phenomenality、moral status、generative health 或 legitimacy。
- 群体级 perspective-bearing / continued-selectable 结构不能由成员结果的简单求和替代；这一 non-reducibility burden 仍不是 subjecthood theorem。

### RC-A absorption result

删除 former P1-T05 / Real Choice Moment 后，T-COLL-1 的对象范围与四条件 extension **不需要新增关系才能保留**：P1-T06 已提供 iterative / perspective-bearing / history-bearing / continued-selectable 的稳定 ISP 骨架；shared `L_2` 与 `M(t)` 已提供集体历史与后果回路结构。原来用“共识剧本 / 制度自动化”对比 real choice 的文字，只能保留为下游 agency / revision guard：脚本或自动化本身不证明更强 collective agency，但也不意味着没有 Selection。

---

## §3. T-COLL-2：三类结构诊断类型

以下是 P2 descriptive/model diagnostic types，不是 normative classes，也不设定自然的健康→病理排序。

### 3.1 聚合型（Aggregation）

- **结构**：`\mathcal{P}` 不满足 T-COLL-1 第 2 或第 4 条；各 `P_i` 独立选择，共享 `L_2`，但没有形成群体级 perspective-bearing / continued-selectable process
- **现象**：市场多数交易、公共广场大多数互动、随机群体
- **读法**：group-level Stable-ISP standing 未建立；这本身不是 pathology。若把聚合修辞为"我们集体决定"，可作为下游 representation / legitimacy audit 的输入。

### 3.2 主从型（Asymmetric Absorption）

- **结构**：`M(t)` 强不对称；一部分 `P_j` 的后果系统性落在另一部分 `P_i` 上，而 `P_j` 本身的未来选择能力不被这些后果影响
- **读法**：在已声明 consequence/burden model 下，`M(t)` 显示不对称 return / externalization pattern。这不自动建立 suffering、evil、domination 或 injustice；相应解释要求各自 owner 与 evidence。

### 3.3 收编型（Collapsed into Higher L_2）

- **结构**：`\mathcal{P}` 的 `σ_{sr}^{coll}` 趋向 1（集体层面自指过载）；`L_2` 成为封闭 scaffold 反向写入每个 `P_i` 的 `d_c^i`；群体看起来高度一致与稳定
- **读法**：已声明 retained-constraint model 中，高位 `σ_{sr}^{coll}` 与 scaffold writeback 可作为 closure / lock-in pattern 的候选特征。`σ_{sr}^{coll}\to1` 只是 model extreme，不是 pathology 或 lethal-`L_2` theorem；底层过程也不因此 selection-free。

### 三类结构诊断的联立模式

$$
\begin{cases}
\text{Aggregation} & : \text{T-COLL-1 cond 2 or 4 fails, but } M(t) \text{ roughly symmetric and } \sigma_{sr}^{coll} \text{ low}\\
\text{Asymmetric Absorption} & : M(t) \text{ systemically asymmetric, independent of T-COLL-1 status}\\
\text{Collapsed into Higher }L_2 & : \sigma_{sr}^{coll} \to 1 \text{ and } L_2 \text{ scaffold rewrites individual } d_c^i
\end{cases}
$$

三类可叠加。联立 pattern 只提供模型诊断输入；任何 pathology、lethality、evil 或 injustice verdict 均需独立 criterion 与 downstream owner。

---

## §4. 集体 σ 与集体 d_c

### §4.1 集体自指率

扩展 `SRT_L1_Formalism §2`：

$$
\sigma_{sr}^{coll}(\mathcal{P}, t) \;:=\; \frac{\|\Theta^{coll,trace}\|}{\|\Theta^{coll,trace}\| + \|\Theta^{coll,ext}\|}
$$

- `\Theta^{coll,trace}`：群体层面历史累积参数（共同叙事、制度、路径痕迹集聚至群体自指层）
- `\Theta^{coll,ext}`：群体对外部（其他群体、自然、新兴 `L_0` 压力）的开放接入

**Scope**：这里的 `trace/ext` 是相对于已声明集体单元 `\mathcal P` 的边界归属。它可以把个体层具有 external provenance 的 shared scaffold 在集体层重新计入 `trace`；因此本式首先是**边界相对的集体历史/内生性追踪器**，不能自动继承单体 `θ^{trace}=P` 自身 prior-output writeback 的严格 authorship 语义。

### §4.2 集体遮蔽阈值

集体 `d_c^{coll}` 并非 `\{d_c^i\}` 的简单统计；它是在给定 candidate-space 表示、尺度和阈值约定下，描述共享选择空间 `A_{\mathcal{P}}` access / correction / dimension-collapse 的 model-local coordinate。

$$
d_c^{coll} \;:=\; \inf\{\,d\;:\;\dim A_{\mathcal{P}}(d, t) \geq \dim_{min}\,\}
$$

### §4.3 关键耦合

在声明 group boundary、component admissions、scale / horizon、measurement map、coefficient meanings、domain criterion 与 failure conditions 后，可检验以下 candidate couplings：

- `M(t)` asymmetry 与 high `\sigma_{sr}^{coll}` 可作为 `d_c^i` / `d_c^{coll}` 的候选 coupling terms；它们不 universal 地推高 threshold，也不自动建立 B phase。
- `\sigma_{sr}^{coll}\to1` 是选定表示中的 model extreme / lock-in candidate，不推出成员 `d_c^i` 全部塌陷的 universal law。
- burden / consequence externalization 可以在不预设 suffering 或 collective subjecthood 的情况下建模。`S_{str}^{coll}` 只在相关 affected positions 的 suffering registration 已独立准入后才可作为条件模型坐标。

### §4.4 集体四变量最小耦合动力学（H3，2026-04-25）

> **立场**：本小节把 `SRT_L1_Formalism.md` 的条件性四变量系统（σ / d_c / T_dir / S）扩到多过程共享 `L_2` 场 `\mathcal{P} = \{P_1, \ldots, P_n\}`。它默认是 P2/P3 conditional multi-process model candidate；各分支只投影已独立准入的 component，formal closure 不建立 P1 standing。

#### §4.4.1 集体场定义

$$
\Theta^{coll,trace}(\mathcal{P},t) \;:=\; \sum_{i} w_i(t)\,\theta_i^{trace}(t) \;+\; \Theta^{L_2}_{shared}(t), \qquad
\Theta^{coll,ext}(\mathcal{P},t) \;:=\; \sum_{i} w_i(t)\,\theta_i^{ext}(t) \;-\; \Theta^{L_2}_{shared}(t)
$$

- `w_i(t)`：声明的 model / measurement participation weights。`M(t)` 列摘要可在特定模型中约束或实例化它们，但 `M(t)` 或 stake 不唯一决定权重。
- `\Theta^{L_2}_{shared}(t)`：共享 `L_2` 沉积（制度 / 叙事 / 路径痕迹）作为集体内源的独立项。它**既**从 `\Theta^{coll,ext}` 中扣除（因为对集体外不再是新接入）**又**累加到 `\Theta^{coll,trace}`

把共享 `L_2` 同时从 `\Theta^{coll,ext}` 扣除并加入 `\Theta^{coll,trace}`，是声明 collective boundary 下的 attribution convention / model choice。它允许研究共享 scaffold 如何改变 `\sigma_{sr}^{coll}`，但不证明 shared `L_2` 是 universal self-reference amplifier。

#### §4.4.2 集体 σ 动力学

$$
\frac{d\sigma_{sr}^{coll}}{dt} \;=\; \frac{1}{T^{coll}}\Big[(1-\sigma_{sr}^{coll})\bigl(\alpha^{coll} w^{coll}\phi(\sigma_{sr}^{coll}) + \boldsymbol{\lambda_M\, \mathrm{tr}\,M(t)} - \lambda_{trace}T^{coll}\sigma_{sr}^{coll}\bigr) - \sigma_{sr}^{coll}\bigl(\beta^{coll} i^{ext} - \lambda_{ext}T^{coll}(1-\sigma_{sr}^{coll})\bigr)\Big]
$$

`\lambda_M\,\mathrm{tr}\,M(t)` 是声明模型中的 candidate coupling term：它检验某个 `M(t)` 对角摘要是否与 `\sigma_{sr}^{coll}` 漂移同变。该项不是由 `M(t)` 定义或 T-COLL-1 唯一推出的因果身份，也不把"内向" pattern 同一化为集体自指膨胀。

#### §4.4.3 集体 d_c 动力学

$$
\frac{dd_c^{coll}}{dt} \;=\; \gamma_\rho^{coll}\rho^{coll}_{local} + \boldsymbol{\gamma_\sigma_{sr}^{coll} \max(0,\,\sigma_{sr}^{coll} - \sigma_{sr,sub}^{coll})} + \boldsymbol{\gamma_{asym}\,\|M_{asym}(t)\|} - \gamma_\pi^{coll}\pi^{coll} - \gamma_I^{coll}I_{window}^{coll}
$$

`\gamma_{asym}\,\|M_{asym}(t)\|` 是另一个 candidate coupling term：它允许在特定模型中测试 `M(t)` 反对称 summary 与 `d_c^{coll}` 漂移的关系。不对称本身不 universal 地推高 `d_c^{coll}`，也不自动建立 pathology、suffering 或 domination。

集体可支付性 `\pi^{coll}` 与集体干预窗口 `I_{window}^{coll}` 分别降低 `d_c^{coll}`。它们是恢复通道，不等价于 Selection 或 collective agency 的定义。

#### §4.4.4 集体 T_dir 动力学

RC-A 局部删除探针后，former P1-T05 派生的 `+\kappa_r^{coll}r^{coll}(t)` 不再进入当前最小式；没有为它指定新的 Selection / `\varepsilon_{pg}` 来源。

**Admission precondition**：只有在 collectively relevant direction 已独立 typed / declared，且 `T_{dir}^{coll}` 已在模型中准入时，本小节的 direction branch 才定义。无 declared direction 时，`T_{dir}^{coll}` / `T_{dir}^{alg,coll}` 为 undefined / not admitted，而不是填零闭合。

$$
\frac{dT_{dir}^{coll}}{dt} \;=\; -\kappa_{\mathrm{relax}}^{coll}\bigl(T_{dir}^{coll} - T_{dir}^{alg,coll}\bigr) - \boldsymbol{\kappa_{mask}^{coll}\,\Delta\Psi_f^{gap,coll}(t)} - \boldsymbol{\kappa_S^{coll}\,S_{str}^{coll}(t)} + \kappa_{sup}^{coll}\,s_{ext}^{coll}(t)
$$

- `T_{dir}^{alg,coll}`：准入 direction 后，可由 `(\sigma_{sr}^{coll}, d^{coll}, d_c^{coll})` 参数化的 model-local access / readability target；它不生成、排序或验证 direction。
- `\Delta\Psi_f^{gap,coll}(t)`：声明 criterion 下的 collective actual-vs-felt model gap；它不是 universal hidden moral/social debt，也不自行建立 pathology。
- `s_{ext}^{coll}(t)`：**真正来自集体外**的支持（其他群体 / 新接入的 `L_0` 压力被吸收为资源，而非被吸收型收编）；这里要求来源必须不在 `\mathcal{P}` 内，否则退化为 `\kappa_{sup}\cdot` 自身的某种递归伪装

**criterion-relative collective lock-in / lethality signature candidate**（历史标签为"集体层致命 `L_2`"）：仅当 direction、lethality / viability criterion、时窗与各项均已独立准入时，可以在声明 P2/P3 模型中研究下列联合 signature：

$$
\mathrm{lethal\;collective\;}L_2 \;\Longleftrightarrow\; \bigl(T_{dir}^{alg,coll} \text{ 持续高}\bigr) \;\wedge\; \bigl(\Delta\Psi_f^{gap,coll} \text{ 持续累积}\bigr) \;\wedge\; \bigl(\kappa_{mask}^{coll} < \kappa_{\mathrm{relax}}^{coll}\bigr)
$$

该式只是声明 criterion 下的 conditional model signature，不是 iff theorem。高或稳定 `T_{dir}^{coll}` / `T_{dir}^{alg,coll}` 不证明 direction 有效、健康、合法或具有道德权威。

#### §4.4.5 集体 S 动力学（两型）

RC-A 局部删除探针同样删除 former P1-T05 派生的 `-\mu_r^{coll}r^{coll}` relief 项；其余通道仍定义良好。

本节只有在 suffering 已由 `SRT_Suffering.md` 的独立前件登记后，才把相应残差写为 `S_{sig}^{coll}/S_{str}^{coll}`。若该前件未满足，下面的 `M_{ext}` 项只能读作**边界外负担 / 后果外化**的候选动力学，不能被命名为苦难，也不能据此推出存在一个承担该苦难的集体主体。

$$
\begin{aligned}
\frac{dS_{sig}^{coll}}{dt} &= \mu_\Delta^{coll}\,\dot{\Delta}_{avail}^{coll} - \boldsymbol{\mu_\pi^{coll}\pi^{coll}\mathbb{1}[d^{coll} > d_c^{coll}]} - \mu_{sup}^{coll} s_{ext}^{coll} \\[3pt]
\frac{dS_{str}^{coll}}{dt} &= \boldsymbol{\nu_{block}^{coll}\mathbb{1}[d^{coll}\le d_c^{coll}]\,S_{sig}^{coll}} + \boldsymbol{\nu_\sigma_{sr}^{coll}\max(0,\,\sigma_{sr}^{coll} - \sigma_{sr,health}^{coll})} + \boldsymbol{\nu_{ext}\,\|M_{ext}(t)\|} - \nu_{trigger}^{coll}D_{trigger}^{coll} - \nu_\pi^{coll}\pi^{coll} I_{window}^{coll}
\end{aligned}
$$

候选项 `\nu_{ext}\,\|M_{ext}(t)\|` 表示 `M(t)` 跨出 `\mathcal{P}` 边界的负担 / 后果外化。只有当边界外存在已独立登记的 suffering bearer 与 T-SUFF 前件时，它才可作为另一侧 `S_{str}` 的输入。该项不表达总苦难守恒，也不证明压低 `S_{sig}^{coll}` 必然使任一 `S_{str}` 或其总和上升；这些关系须由具体 domain 的归属、转化和测量模型另行建立。

### §4.5 个体↔集体耦合（最小形式）

以下各式是通过 `M(t)` 与共享 `L_2` 写出的**候选耦合项**，不是从上游本体推出的完备因果律。每个分量都继承自身的 admission 条件：`T_dir` 只在方向已独立登记时出现，`S` 只在 suffering 已独立登记时出现。

$$
\begin{aligned}
\text{向上聚合} &:\; \sigma_{sr}^{coll}, d_c^{coll}, T_{dir}^{coll}, S^{coll} \;\text{ 由 §4.4.1-§4.4.5 的集体场定义与 ODE 生成}\\[3pt]
\text{向下反馈（B 期传染）} &:\; \frac{dd_{c,i}}{dt} \;\supseteq\; \gamma_{feedback}\cdot\max(0,\,\sigma_{sr}^{coll} - \sigma_{sr,sub}^{coll})\\[3pt]
\text{向下反馈（方向可读性候选）} &:\; \frac{dT_{dir,i}}{dt} \;\supseteq\; -\kappa_{feedback}\cdot\Delta\Psi_f^{gap,coll}(t)\quad[\text{direction admitted}]\\[3pt]
\text{向下反馈（结构型苦难候选）} &:\; \frac{dS_{str,i}}{dt} \;\supseteq\; \nu_{feedback}\cdot\|M_{asym}(t)\|\cdot\mathbb{1}[i\in\mathcal{P}_{absorbed}]\quad[\text{suffering admitted}]
\end{aligned}
$$

其中 `\mathcal{P}_{absorbed} \subset \mathcal{P}` 是所选模型中被归入吸收侧的成员集。三条下行项只写出可检验的候选路径；`M_{asym}` 本身不建立苦难，`\Delta\Psi_f^{gap,coll}` 本身不建立方向损失，且这些路径既非必要条件也非充分条件。

### §4.6 criterion-relative 集体模型区间

在明确给定评价 criterion、变量 admission 与动力学闭包后，可把旧标识 `\mathcal{A}_{path}^{coll}` 重读为一个 closure / lock-in regime candidate；下标 `path` 只保留历史索引，不预断 pathology：

$$
\mathcal{A}_{path}^{coll}:\; \sigma_{sr}^{coll}\to 1,\; d_c^{coll}\to d_{max},\; T_{dir}^{coll}\approx T_{dir}^{alg,coll},\;\Delta\Psi_f^{gap,coll}\uparrow,\; S_{str}^{coll}>0\text{ 定常},\; S_{sig}^{coll}\to 0,\; \|M_{asym}\|+\mathrm{tr}\,M \text{ 同高}
$$

该式是把收编与不对称后果回路并置的一种模型签名。只有在具体模型证明吸引性后才可称为数学吸引子；只有在另行给出的规范、健康或 suffering criterion 下才可称为病理。历史或文明案例不能由该式直接读出。

相对于一个已声明的 correction-access / revision-work criterion，旧标识 `\mathcal{H}^{coll}` 可重读为一个 model work regime；`H` 只保留历史索引，不预断 health：

$$
\mathcal{H}^{coll}:\; \sigma_{sr}^{coll}\in(\sigma_{sub}^{coll,\dagger}\pm\delta^{coll}),\; d^{coll}>d_{narrow}^{coll},\; T_{dir}^{coll}\approx T_{dir}^{alg,coll}\text{ 且 }\Delta\Psi_f^{gap,coll}\to 0
$$

**边界**：`\mathcal{H}^{coll}` 不是健康、合法性或制度善的同义词；低信号、高 `T_dir`、稳定状态或某个 `\sigma` 区间都不自动建立健康。P1-T06 的 collective standing 与 21C B13 的 generative-health bridge 必须分开；若要主张 generative health，须另行声明 B13 的后果回返、规则修订和 domain criterion，不得把本节标量偷渡回 P1。

### §4.7 T-PROJ-1^{coll}：集体四变量系统作为多算子主方程的投影（H6，2026-04-25）

> **Status**：本节给出 §4.4-§4.6 与 `Core/SRT_Core_22_Equations.md §0-C` 多算子形式（Eq-Multi-01 / 02 / 03）之间的一种**带条件投影模型**。结构对位 `Core_Law/SRT_L1_Formalism.md §6 T-PROJ-1`，但不由该单体模型自动推出。**Claim level: P2 conditional model / P3 operational bridge**。
>
> **Does not close**：`SRT_L1_Formalism.md §6.6` 的“集体版投影未证明”开放点。本节只登记一套候选映射及其额外假设，不把符号对位提升为本体推导。

#### §4.7.1 多算子主方程作为上游

`Core/SRT_Core_22_Equations.md §0-C`：

$$
\mathcal{F}_{collective}(\{\sigma_i, \theta_i\}_{i\in\mathcal{P}}) \;=\; \sum_i \Psi_f(\hat{G}_i) + \sum_{i<j} \Psi_f(\hat{G}_i, \hat{G}_j)
\qquad
\hat{G}_i[\sigma_i] \;=\; -\frac{\partial \mathcal{F}_{collective}}{\partial \theta_i}
\qquad
d_{collective} \;=\; D_{eff}(\nabla^2 \mathcal{F}_{collective})
$$

在额外指定集合边界、聚合规则、参数化与测量映射后，可尝试把各 `(σ_i, θ_i)` 与 `\mathcal{P}`-级联立项映射到集体变量。本节给出多 ISP 特定项（`λ_M\,\mathrm{tr}\,M, \gamma_{asym}\|M_{asym}\|, \nu_{ext}\|M_{ext}\|`）的一组候选对应；它们不是由式形相似性唯一确定的“来源”。

#### §4.7.2 集体投影算子

以下至多定义四个集体标量泛函 `\mathcal{F}_X^{coll} : (\mathcal{F}_{collective}, \{\sigma_i, \theta_i\}, M(t)) \mapsto \mathbb{R}`。`T` 分量要求 direction admission；`S` 分量要求 suffering admission。未通过相应 admission 时，该分量从投影域中省略，而不是取零。

**`σ_{sr}^{coll}` 投影**

$$
\mathcal{F}_\sigma^{coll} \;:=\; \frac{\|\Theta^{coll,trace}\|}{\|\Theta^{coll,trace}\| + \|\Theta^{coll,ext}\|}
\qquad\text{其中}\quad
\Theta^{coll,trace} \;:=\; \bigl\{\theta_i^{trace}\bigr\}_{i\in\mathcal{P}}
$$

`\theta_i^{trace}` 是所选模型中归于共享 `L_2^{shared}` 写回的部分（§1 Def-C-1）。该归属和范数选择共同定义一个 `\sigma_{sr}^{coll}` 候选投影，不建立表示唯一性或 collective causal control。

**`d_c^{coll}` 投影**

$$
\mathcal{F}_d^{coll} \;:=\; d_{max}^{coll} - \alpha_d^{coll}\cdot \frac{1}{d_{collective}}
\qquad\text{即}\quad
d_c^{coll} \;\propto\; D_{eff}(\nabla^2 \mathcal{F}_{collective})^{-1}
$$

该式把 Eq-Multi-03 的有效维度倒数选作 `d_c^{coll}` 的模型代理；“倒数即重选容量塌陷度”不是跨参数化恒等式，比例、单调性与适用域都需独立标定。

**`T_{dir}^{coll}` 投影**

本 owner 不提供 universal `\mathcal{F}_T^{coll}` 公式。具体模型只有在 direction 已由其 canonical owner 独立准入后，才可声明相应的成员投影、群体聚合与 measurement map；`Order`、`L_0`、叙事一致或算法目标都不能替代该 direction signal。所得群平均至多是 §4.4.4 的 model-local access / alignment proxy。

**`S^{coll}` 投影**

$$
\mathcal{F}_S^{coll} \;:=\; \bigl\|\hat{R}^{coll}(\{\sigma_i, \theta_i\}, M(t))\bigr\|_{H_\mathcal{P}}
$$

其中

$$
\hat{R}^{coll} \;:=\; \sum_i \frac{d\sigma_i}{dt} - \sum_i \bigl[-\partial_{\theta_i}\mathcal{F}_{collective}\bigr] - \mathcal{C}_M(M(t))
$$

`\mathcal{C}_M(M(t))` 是所选模型对后果回路的修正项。只有在 suffering bearer、归属与 T-SUFF 前件已独立登记，并且残差到 suffering 的映射另行声明后，`\hat{R}^{coll}` 才可分裂为 `S_{sig}^{coll}/S_{str}^{coll}`（§4.4.5）。否则 `\hat{R}^{coll}` 只是一项动力学 / 负担残差。

#### §4.7.3 `M(t)` 作为交叉摩擦项的结构投影

Def-C-2 给出 `M(t)` 作为后果回路矩阵。在额外指定识别映射后，可把它的三种结构摘要与 `\mathcal{F}_{collective}` 中若干项作如下候选对应：

| `M(t)` 成分 | 主方程层来源 | L1 集体 ODE 项 |
|---|---|---|
| `\mathrm{tr}\,M(t)` | 可与 `\sum_i \partial^2_{\theta_i}\Psi_f(\hat{G}_i)` 的选定内向部分建立识别关系 | `\lambda_M\,\mathrm{tr}\,M` 作为 `σ_{sr}^{coll}` 的候选耦合项（§4.4.2）|
| `\|M_{asym}\|` | 可与交叉项的选定非互惠摘要建立识别关系 | `\gamma_{asym}\|M_{asym}\|` 作为 `d_c^{coll}` 的候选耦合项（§4.4.3）|
| `\|M_{ext}\|` | 可与跨 `\mathcal{P}` 边界的选定外部分量建立识别关系 | `\nu_{ext}\|M_{ext}\|` 作为负担外化项；仅在 suffering admitted 后进入 `S_{str}`（§4.4.5）|

三项记录了集体模型可能需要的额外结构信息，但不因此成为唯一、独立或完备的算子分解。群平均的单 P 投影不能自行提供这些跨成员 / 跨边界信息；反过来，本表也不从 `M(t)` 反定义 `\Psi_f` 或 Core22 多算子项。

#### §4.7.4 集体闭包假设

四变量集体系统若要在所选投影下闭合，需要五条额外模型假设（C1^{coll}-C4^{coll} 参照 §6 单 P 版 C1-C4 构造，C5^{coll} 是多过程模型新增；没有一条由 standing 自动推出）：

| 编号 | 假设 | 模型动机 / 边界 |
|---|---|---|
| **C1^{coll}** | 慢-快分离：每个 `θ_i` 与其 `σ_i` 在不同时间尺度演化；`M(t)` 在 `\sigma_i` 收敛时间尺度上近似常数 | Eq-Evo-03 / Eq-Multi-02 提供候选建模动机；具体时间尺度分离须独立验证 |
| **C2^{coll}** | 共享 `L_2^{shared}` 写回 Markov 闭包：`\dot{\theta_i^{trace}}` 仅依赖当前 `(σ_{sr}^{coll}, \rho_{local}^{coll})`，不依赖更高阶共享历史 | 参照 Eq-Bridge-L2-01 的模型选择；共享域的 Markov 性不是同构定理 |
| **C3^{coll}** | 局部正则性：所用 `\mathcal{F}_X^{coll}` 在声明的 `\mathcal{P}` 邻域内有界且 Lipschitz | 额外数学假设；T-COLL-1 本身不保证紧性、界或 Lipschitz 性 |
| **C4^{coll}** | 群平均方向投影可分性：在 direction admitted 的分量中，余弦角与 `\sigma_M` 纵向幅度近似可分（群平均后高阶交叉项可忽略） | 需要 domain-local 正交 / 近似检验；Eq-Bridge-IG-01 不自动推出集体可分性 |
| **C5^{coll}**（新增）| `M(t)` 识别闭包：为 `M(t)` 三成分指定有限维测量或估计映射 | `Hardening_Notes §3` 的 MOC-1/2/3 可提供部分 operational evidence，但不与 `M(t)` 或 Hessian 项构成直接恒等式 |

**关键**：C3^{coll}-C5^{coll} 都是额外的模型债务，不由 collective standing 支付。MOC 只能约束如何观察 exposure / recourse / attention，不能单独选择权重、证明矩阵分解或建立精确动力学系数。当 C5^{coll} 在特定 domain 失效时，`M(t)` 三成分项只能保留为定性现象学描述。

#### §4.7.5 T-PROJ-1^{coll}：条件性集体投影命题

**陈述（P2 conditional model）**：对已经独立取得 collective standing 的 `\mathcal{P}`，若投影定义、变量 admission、识别映射及闭包假设 C1^{coll}-C5^{coll} 都在同一 domain 成立，则可把模型目标写为

$$
\boxed{\;\frac{d\mathcal{F}_X^{coll}}{dt}\bigg|_{\text{Eq-Multi-01,02,03}} \;\overset{C1^{coll}\text{-}C5^{coll}}{=}\; \mathrm{RHS}_X^{\text{§4.4}} \;+\; O(\eta^{coll})\;}
\qquad X \in \{σ_{sr}^{coll}, d_c^{coll}, T_{dir}^{coll}, S^{coll}\}
$$

其中该等式只逐项适用于已经 independently admitted 的分量；`\mathrm{RHS}_X^{\text{§4.4}}` 是 §4.4.2-§4.4.5 中被具体模型采用的右端，`O(\eta^{coll})` 是待估计的闭包残差。该式是有待验证的模型等式，不是 P1 theorem；未 admitted 的 `T` 或 `S` 分支必须省略。

**逐项对应（仅集体新增项）**：

| §4.4 集体新增项 | 主方程来源 | 闭包条件 |
|---|---|---|
| `\sigma_{sr}^{coll}` 中 `\lambda_M\,\mathrm{tr}\,M(t)` | 所选内向交叉 / self-loop 摘要的候选识别 | C2^{coll} + C5^{coll} + 系数标定 |
| `d_c^{coll}` 中 `\gamma_{asym}\|M_{asym}\|` | 所选非互惠交叉摘要的候选识别 | C3^{coll} + C5^{coll} + 单调性检验 |
| `S^{coll}` 中 `\nu_{ext}\|M_{ext}\|` | 跨 `\mathcal{P}` 边界的负担摘要；仅在 suffering admitted 后进入本行 | C3^{coll} + C5^{coll} + suffering attribution / T-IRR-3.5 前件 |
| `d_c^{coll}` 与 `d_{collective}` 反比 | 由本节选择的 `\mathcal{F}_d^{coll}` 代理定义 | C3^{coll} + 参数化适用域 |

§4.4.2-§4.4.5 中与单 P 版式形相似的项也不能仅靠群平均直接得出；跨成员协方差、尺度选择和共享 `L_2` 归属仍须检查。former P1-T05 的 `r/r^{coll}` 通道已经由 RC-A subtractive probe 删除，不在候选列表内。

**需要支付的识别步骤**：

1. **`\lambda_M\,\mathrm{tr}\,M` 项**：必须证明所选 `\theta^{coll,trace}` 归属与 `M` 的 trace 摘要在指定参数化下具有稳定识别关系；C2/C5 本身不把 Hessian 的迹等同于 `\mathrm{tr}\,M(t)`。

2. **`\gamma_{asym}\|M_{asym}\|` 项**：必须验证后果回路的不对称摘要怎样影响所选 `d_c^{coll}` 代理；矩阵不对称、交叉摩擦与 Hessian 结构不是同一对象，C3 也不提供等同关系。

3. **`\nu_{ext}\|M_{ext}\|` 项**：必须先固定边界与 bearer，再证明负担外化如何进入残差；若进一步写成 `S_{str}`，还须独立满足 suffering admission 与 T-IRR-3.5 的适用前件。外溢不自动等于苦难转移或沉积。

4. **`d_c^{coll} \propto 1/d_{collective}`**：这是 `\mathcal{F}_d^{coll}` 的代理选择；需检验尺度、零点、参数化与反例，不能作为 Core22 的直接语义后果。

#### §4.7.6 T-PROJ-1^{coll} 不证明的事项

为避免过度主张，T-PROJ-1^{coll} **不承诺**以下内容：

1. **不**证明集体系数（`\lambda_M, \gamma_{asym}, \nu_{ext}` 等）与单个体系数的具体函数关系——这仍是 P3 实证 / domain 标定问题
2. **不**证明 MOC-1/2/3 三判据是 `M(t)` 可测性的 minimal complete 集——`Hardening_Notes §3` 仍标 P2 operational proxy
3. **不**证明嵌套 ISP（家庭 ⊂ 社区 ⊂ 国家）的多层投影——§9 的跨尺度嵌套问题不被本节解决
4. **不**证明 `M(t)` 的非线性时间演化（H6 假设 C1^{coll} 下 `M(t)` 慢于 `σ_i`；快变 `M(t)` 域外）
5. **不**证明 T-COLL-2 三类结构诊断（聚合 / 不对称后果回路 / 闭合或锁定）与 `M(t)` 三成分（`\mathrm{tr}\,M / \|M_{asym}\| / \|M_{ext}\|`）一一对应——§4.4-§4.6 只给候选耦合，不给双射
6. **不**证明 `\mathcal F_\sigma^{coll}` 的 trace/ext 归属唯一、bare norm 在等价集体参数化下表示不变、或其 trace 语义与单体 `P`-own-output provenance 完全同一；也不把 `σ_{sr}^{coll}` 的数值直接等同于 collective causal control / agency 或自然相边界。
7. **不**反向定义 Core22 多算子、`\Psi_f`、direction 或 suffering，也不从 collective standing 推出任何一个投影闭包条件。

#### §4.7.7 与 §6 单 P 版投影的关系

| 维度 | §6 T-PROJ-1（单 P）| §4.7 T-PROJ-1^{coll}（多 ISP）|
|---|---|---|
| 上游主方程 | Eq-Evo-01 / Eq-Evo-02（单算子） | Eq-Multi-01 / 02 / 03（多算子） |
| 投影输入 | `(\sigma_M, \theta)` | `(\mathcal{F}_{collective}, \{\sigma_i, \theta_i\}, M(t))` |
| 闭包条件数 | 4（C1-C4） | 5（C1^{coll}-C5^{coll}，新增 `M(t)` 可测性） |
| 新增结构项 | — | `\lambda_M\,\mathrm{tr}\,M, \gamma_{asym}\|M_{asym}\|, \nu_{ext}\|M_{ext}\|` |
| `S` 边界 | P 内部 `\hat{R}` | `\mathcal{P}` 内部 + 边界外溢（`\mathcal{P}_{absorbed}` via T-IRR-3.5）|

T-PROJ-1^{coll} 是参照 T-PROJ-1 构造的多 ISP 候选模型，不是其逻辑推论。只有在聚合、边界、trace/ext 归属和参数化都与单体定义兼容时，`\mathcal{P} = \{P\}` 极限才应接受单 P 一致性检验；该极限不是本文已证明的恒等式。

### §4.8 Late-stage tower/nested hardening pointer

The tower/nested material previously drafted as H10-H16 has been moved to
`Core_Law/SRT_Collective_Tower_Hardening_Notes.md`.

It is not part of the minimal canonical definition of collective selection.
It should be read as late-stage P2/P3 conditional hardening material. Strong
closure assumptions do not promote it to P1.

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
`M(t)`, boundary maintenance, memory, collective continued-selectability, and
any stronger downstream agency/revision standing claimed.

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

## §6. T-COLL-4：集体 agency / revision guard（former “真实共选”判据降级）

### 陈述

> **Claim level: P2/P3 downstream guard.** 本节不定义 Selection occurrence，也不是 T-COLL-1 collective-ISP standing 的附加必要条件。

在已经满足 T-COLL-1 的 collective ISP 中，若要进一步主张**较强的 collective agency / consequence-sensitive revision standing**，至少需要独立检查以下结构，而不能仅凭投票、共识或制度程序成立：

$$
\text{结果改变后续有效候选关系}\,\wedge\, \text{后果经 }M(t)\text{ 返回 }\mathcal{P}\,\wedge\,\text{行为不被既有集体 }L_2\text{ 脚本穷尽解释}
$$

该合取是 bounded downstream guard，不是 Selection 的本体定义。它失败时只表示**更强 collective agency / revision standing 未建立**；不得推出 `no Selection`、不得撤销已经独立满足的 P1-T06/T-COLL-1 standing，也不得由通过该 guard 推出 consciousness、freedom 或 moral responsibility。

### 推论

- **投票不自动证明较强 collective agency**：既定选项、既定程序、既定后果路径可能只是高层 option-picking；这不等于 selection-free，也不定义 Selection
- **共识不自动证明较强 collective agency**：若 `M(t)` 强不对称，少数子群不实际承担任何后果回路，则一致意见不足以建立 consequence-sensitive collective revision
- **专家决定不自动证明较强 collective agency**：即便专业正确，仍需独立检查 collective consequence return 与 revision standing
- **通过本 guard 仍不证明主体性或意识**：它只是 collective agency / revision 的 P2/P3 审计输入

---

## §7. 接口：政治、经济、共同体

本文件**不替代**以下 domain 文件，它为它们提供结构基石：

- `Philosophy/SRT_Political_Philosophy.md`：合法性与可持续共同选择的关系只能作 P2/P3 规范桥；T-COLL-1、条件性 T-COLL-3 与降级后的 T-COLL-4 可提供结构审计输入，但不自动等价于合法性
- `Philosophy/SRT_Social_Economics.md`：分布式聚合、后果回路不对称和闭合风险可把本文件的结构诊断作为输入；结构性不公、制度病理等结论须由该 domain 的额外判据建立
- `Philosophy/SRT_Political_Rights.md`：投票相关判断只能把降级后的 T-COLL-4 作为 downstream agency/revision audit input；公检法、监督、授权等制度可被检验为改变 `M(t)` 或闭合风险的机制，但本文不预先判定其效果或合法性
- `Spirituality/SRT_Spirituality_Community_and_Sangha.md`：`M(t)` 的互惠程度与 `\sigma_{sr}^{coll}` 轨迹可作为共同体审计输入；它们不单独定义健康、托举或“新地板”
- `Core_Law/SRT_Suffering.md T-SUFF-5`：集体外部化只在 suffering bearer 与归属已独立登记后，才可进入结构型苦难分析

---

## §8. AI / 平台场景的集体选择护栏

算法中介 / 平台经济 / 大模型对齐场景下，集体选择分析有独特风险：

1. **集体主体归属风险**：算法聚合被呈现为“社区意见”时，聚合结果本身不建立 collective standing、subjecthood 或 agency
2. **`M(t)` 的黑箱化**：平台经济下后果回路矩阵不可观察，使主从型退化不可诊断
3. **`\sigma_{sr}^{coll}` 的算法加速**：推荐系统可通过反馈环系统性推高 `σ_{sr}^{coll}`（回音室、极化），推进收编型退化而参与者无自觉
4. **AI 不按类别自动纳入或排除 `\mathcal{P}`**：是否把某个 AI 过程列为候选成员，须按其具体边界、迭代、历史写回与 continued-selectability 独立检查；无论 standing 是否成立，AI 中介都可能改变 `M(t)` 与 `L_2`

相应的：对平台与算法系统的 SRT 评估不应停在"它是否有意识"，而应评估它**对 `M(t)` 与 `σ_{sr}^{coll}` 的结构性影响**。这与 `AI/AI_POSITIONING_NOTE.md` 的 stake-bearing 光谱互补。

---

## §9. Open Pressures

> **Hardening status (2026-04-24/25/26; RC-A sync 2026-08-18; semantic truth-up 2026-09-16)**: §9.2 `M(t)` 可测性在 `Core_Law/SRT_L1_Hardening_Notes.md §3` 已给出第一遍 MOC 三判据（exposure / recourse / attentional）；它们提供 P2 operational evidence，不与 `M(t)` 构成恒等式。§4.4.1 的加权聚合仍欠权重选择与 trace/ext 归属；§4.7 T-PROJ-1^{coll} 是 P2 conditional model / P3 operational bridge，不关闭集体投影证明债务。Late-stage tower/nested material remains outside the minimal canonical definition. Former P1-T05 / `r^{coll}` dependency has been removed; T-COLL-4 remains only as downstream agency/revision guard.

本 draft 状态下尚未封口：

1. **`\Theta^{coll,trace}` 与 `\Theta^{coll,ext}` 的形式化**：§4.4.1 给出候选加权聚合 + 共享 `L_2` 项；权重 `w_i(t)`、trace/ext 归属及表示不变性均未封口，不能说权重由 `M(t)` 推导
2. **`M(t)` 的可测性**：对称/不对称结构在理论上明确，实证提取在大多数社会场景非常困难；本文件不解决此
3. **collective agency / revision guard 的外部判据**：降级后的 T-COLL-4 如何由第三方稳定审计？当前仍是 P2/P3 downstream operational debt，不回升为 Selection criterion
4. **制度与集体 ISP 的精确分界**：本文件说制度是器官不是主体，但某些高度自治的制度性实体（法人、社团）是否能在某些条件下**自身**成为集体 ISP？这需要后续硬化
5. **跨尺度嵌套**：Late-stage candidate material is preserved in `Core_Law/SRT_Collective_Tower_Hardening_Notes.md`; it remains P2/P3 conditional under strong closure assumptions and is not part of the minimal canonical definition. 剩余开放点：具体塔层数 domain 实证、跨尺度 `M^{(n\to n+1)}` MOC 多层版本、跨层耦合边界条件
6. **历史层面 generative reselectability**：其在长时间尺度上如何演化？文明兴衰能否在明确比较基线后部分读为后果回返或规则修订失败？
7. **集体四变量耦合动力学**：§4.4 给出第一遍形式，仍待封口——(a) `w_i(t)` 的选择规则以及 `M(t)` 摘要能否约束它；(b) `T_{dir}^{alg,coll}` 中光滑阶跃的适用族；(c) `\Delta\Psi_f^{gap,coll}` 作为集体层对象的可操作定义；(d) 向下反馈 §4.5 的遗漏路径与 failure conditions；(e) 仍保留的新集体系数 `\lambda_M, \gamma_{asym}, \kappa_{mask}^{coll}, \nu_{ext}` 的实证窗口
8. **紧耦合嵌套 One 的 scale attribution —— higher-order realization 部分**：在多个 One 紧耦合嵌套时，后果与 standing 应归到哪一层？本条由 `STATUS.md §OPEN register` 依 `Operations/Audits/SRT_OPEN_REGISTER_OWNERSHIP_ADJUDICATION_2026-09-13.md` 迁入，原样保留、**未关闭**。只有 higher-order realization 一半落在本文件；local formation / unit 问题归 `Core_Law/SRT_One_Formation.md §7`，cross-layer non-identity gate 归 `Core_Law/SRT_Generative_Ontology_Spine.md §13`（OPEN register）——本文件不定义 `One / Selection-position`（见开头 R1 One-formation boundary），因此不得据本条反推 One 的形成或单位划分。与第 5 条跨尺度嵌套相邻但不同：第 5 条问塔层形式化，本条问归属。

---

## §10. Cross-References

- P1-T06 stable ISP（集体 ISP 条件的 upstream）→ `Core/SRT_Core_21b_Constitutive_Theorems.md`
- former P1-T07 demotion / absorption remainder → 同上
- ST-A conditional anti-closure / generative reselectability → `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13`
- RC-A agency / automation guard → `03_Bridges/SRT_Agency_Automation_Guard_2026-08-17.md`
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

- **本文件做**：给出声明式多过程 / collective candidate、共享 `L_2` 与后果回路的 P2/P3 模型；T-COLL-1 仅作为 P1-T06 的集体应用；T-COLL-2/3/4 与 §4.4-§4.7 都保留各自的条件和 claim level
- **本文件不做**：制度设计、政策判断、具体政治/经济案例分析、共同体组织学；不定义 One、Selection occurrence、subject、Bearer、Agency、consciousness、moral standing、health 或 legitimacy
- **引用规则**：涉及"集体选择作为结构对象是什么"的**结构层**陈述时，优先回链本文件；涉及具体政治、经济、共同体、制度判断时，回链相应 Philosophy / Spirituality 文件
- **不得**：把本文件读作政治偏好的理论背书；不得把描述性 `M(t)`、`\sigma_{sr}^{coll}`、`d_c^{coll}`、谱量或投影闭包直接升级为 suffering、pathology、health、legitimacy 或 moral verdict；不得把 T-COLL-4 反向提升为 Selection criterion
- **重点**：聚合、不对称后果回路、闭合 / 锁定是可并存的结构诊断；它们不按意识形态归类，也不单独给出规范结论
