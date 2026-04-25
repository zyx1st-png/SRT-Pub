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

> **Hardening status (2026-04-24)**: 下列 §9.2 `M(t)` 可测性在 `Core_Law/SRT_L1_Hardening_Notes.md §3` 已给出第一遍 MOC 三判据（exposure / recourse / attentional，合成取 min）；本小节保留原表述直至回写完成。

本 draft_v0 状态下尚未封口：

1. **`\Theta^{coll,trace}` 与 `\Theta^{coll,ext}` 的形式化**：目前按范数集聚给出；真正需要把群体级参数从个体 θ 分布推导出来
2. **`M(t)` 的可测性**：对称/不对称结构在理论上明确，实证提取在大多数社会场景非常困难；本文件不解决此
3. **共选真实性的外部判据**：T-COLL-4 三条件在第三方视角下如何判定？目前仍带相当主观成分，需要进一步降低依赖
4. **制度与集体 ISP 的精确分界**：本文件说制度是器官不是主体，但某些高度自治的制度性实体（法人、社团）是否能在某些条件下**自身**成为集体 ISP？这需要后续硬化
5. **跨尺度嵌套**：家庭是 ISP，社区是 ISP，国家可能是 ISP——嵌套关系下 `M(t)` 与 `σ^{coll}` 如何层级耦合？
6. **历史层面 ε**：集体层面的 ε 反闭合在长时间尺度上如何演化？文明兴衰是否可以读为集体 ε 的长程维持失败？

---

## §10. Cross-References

- P1-T05 real choice moment（集体版的 upstream）→ `Core/SRT_Core_21b_Constitutive_Theorems.md`
- P1-T06 stable ISP（集体 ISP 条件的 upstream）→ 同上
- P1-T07 ε 反闭合必要性（T-COLL-3 的 upstream）→ 同上
- 个体化 / σ → `Core_Law/SRT_Individuation.md`
- 遮蔽动力学 / A/B 分期 / d_c / 结构性恶三判据 → `Core_Law/SRT_Occlusion_Dynamics.md`
- 苦难 / T-SUFF-5 集体外部化 → `Core_Law/SRT_Suffering.md`
- 三变量耦合动力学 → `Core_Law/SRT_L1_Formalism.md`
- 政治哲学 → `Philosophy/SRT_Political_Philosophy.md`
- 社会经济 → `Philosophy/SRT_Social_Economics.md`
- 政治权利 → `Philosophy/SRT_Political_Rights.md`
- 共同体与 sangha → `Spirituality/SRT_Spirituality_Community_and_Sangha.md`
- AI / 平台接口护栏 → `AI/AI_POSITIONING_NOTE.md`

---

## §11. 定位与使用规则

- **本文件做**：固定多 ISP 共享 `L_2` 场、集体 ISP 存在条件（T-COLL-1）、三类退化（T-COLL-2）、集体 ε 反闭合必要性（T-COLL-3）、共选真实性判据（T-COLL-4）
- **本文件不做**：制度设计、政策判断、具体政治/经济案例分析、共同体组织学
- **引用规则**：涉及"集体选择作为结构对象是什么"的**结构层**陈述时，优先回链本文件；涉及具体政治、经济、共同体、制度判断时，回链相应 Philosophy / Spirituality 文件
- **不得**：把本文件读作政治偏好的理论背书；四类退化与三判据完全按结构判据读，不按意识形态读
- **重点**：三类退化（聚合/主从/收编）是**结构性类型**，可以同时存在于任何意识形态立场的群体中——本文件不为任一立场背书
