---
id: SRT-AO-POTENTIAL-LANDSCAPE-SAME-TARGET-VALUE-AUDIT-20261010
type: audit
status: draft
record_stage: proposed
date: 2026-10-10
layer: operations
epistemic_layer: analysis
claim_mode: audit
canonical: false
ai_do_not_use_for_definition: true
research_mode: U
root_question: What can Ping Ao's nonequilibrium stochastic potential framework contribute to SRT without confusing a conditioned L2 landscape with primitive Selection, and where can a genuine same-target comparison begin?
comparative_claim: none
named_comparator: Ping Ao stochastic decomposition/potential landscape; Freidlin-Wentzell quasipotential; Wang potential/flux
n_mode_triggered: false
dependency:
  - Materials/2026/SRC_2026_10_10_StatPhys_Ao_Stochastic_Landscape_Corpus.md
  - 01_Source_Intuition/SRT_AUTHOR_TRACE_VERTICAL_SELECTION_PARTICIPATION_UNIFICATION_2026-10-10.md
  - Operations/Audits/SRT_VERTICAL_SELECTION_POSITION_PUBLICNESS_PRESSURE_2026-10-10.md
  - Core_Law/SRT_Generative_Ontology_Spine.md
  - Core_Law/SRT_Reference_Dynamics.md
  - SRT_Fisher_FEP_Landscape_Interface.md
  - Operations/Proposals/SRT_GRG_FOUNDATIONAL_PROTO_GRAMMAR_V0_3_2026-09-21.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CN2_FIRST_E2_TASK_FAMILY_A_2026-10-09.md
tags: [Audit, PingAo, SRT, PotentialLandscape, NonEquilibrium, Objectification, CoarseGraining, OTrack, DTrack, NoNoveltyClaim]
---

# 敖平（Ping Ao）随机势景观研究对 SRT 的整体价值：来源忠实的同目标对照与落地边界

> **定位：** M-level bounded U-mode source-neighbor audit，依附 [敖平论文群一手记录](../../Materials/2026/SRC_2026_10_10_StatPhys_Ao_Stochastic_Landscape_Corpus.md)。**不是**作者二次本体裁决、未宣称 SRT 相对于 Ao 的新颖性、不可约性或胜出；没有另起 deep well、实验线、形式定理或统一法则。只写 O-track / source pressure / conditional D-track test design。凡外部来源未核到的实质主张标为 OPEN。
>
> **本轮为什么做：** 10-10 对话作者曾问：「我认为是后者。好像敖平是考虑的是随机扰动，是吧？」。该问句只是问题，前面的“后者”原始机器二选一未能恢复，现有来源等级 **A0-J1**；不能伪造 A0-S 或替作者断言 Ao 仅研究随机扰动。#1116 已把 Ao 作为初步强邻居，但没有具体论文价值表。本审计完成限定范围内的来源归属、数学争论及双轨价值对照，不改变 #1116 的作者立场。

## 0. 结论优先：分层价值和证据等级

| 评价维度 | 判断 | 可承重程度 |
| --- | --- | --- |
| 强邻居 / 外部纠错 | **高**：Ao 已尝试从非平衡随机动力学构造势景观、讨论稳定性与通量／非梯度成分 | Publisher abstracts + AO17E full HTML；无需以此断言普遍定理 |
| 局部 L2 数学脚手架 | **高（有条件）**：稳态概率、势垒、跃迁、噪声扰动和不同随机积分解释，为有状态／可观察的模型提供候选工具 | 必须验证 \`x,f,D\`、随机积分解释、边界条件及 identifiability |
| SRT 的 O-track 研究组织 | **中**：帮助把“给定变量上的稳定/跃迁”与“变量/边界/前景—背景切分的生成”区分为不同解释任务 | M 映射，非 Ao 或 SRT 的共同已证定理 |
| 对 SRT 主张的逆向约束 | **高**：拒绝“成熟势景观方法只有固定景观 + 随机重排”的稻草人；也反对“凡观察到景观重塑就是原初 Selection” | Source-backed pressure；由多篇来源直接支持 |
| SRT 的独有经验增量 | **NOT ESTABLISHED** | 无冻结模型／数据、同目标 held-out 比较 |
| L0 primitive Selection 的实证或数学证明 | **NONE** | Ao 的 SDE 不涉及并未验证 SRT 原初本体 |
| 是否值得立即开新实验 / GRG 跨域综合 | **NO** | CN-2 family A paper-only；GRG broad synthesis HOLD |

**价值排序是此处 M 层研究判断，不是通用量表或学术影响力排名。**

## 1. 先在 Ao 自身术语里忠实说明对象

### 1.1 来源处理的对象和起点

Ao 和共同作者把系统的状态量、漂移、扩散／随机驱动、稳定性及非详细平衡动力学作为数学起点。2004 倾向于**构造** potential；2005 把 ascendancy、transverse、Wright potential 与随机驱动并列，提供一个含层级问题的形式框架；2007 探讨这个构造与更常见随机积分规则的差别；2009 说明生物网络景观的稳健／稳定应用；2017 年综述强调耗散 + detailed-balance-breaking 及 A-type；2017 年开放应用论文展示对高维强噪声系统的具体数值方法。

**关键修正：** Ao 的 landscape 不是只能预设为一幅不会变的地形，更不只是“变异在山谷间弹跳”。动力系统参数、噪声形式、稳定性结构及模型解释的变化都进入其研究范围。SRT 如仅描述“可随历史或环境变动的景观”，不能据此认领独特机制。

### 1.2 非梯度运动与稳态结构不是同一维度

在非详细平衡系统中，系统动力学并非必然是纯粹对某个势函数作梯度下降。Ao17R 明示 detailed-balance-breaking 成分；Ao17E 明示非详细平衡可以造成**有方向的、非互易的转换作用**和路径差异。不能用一维固定 fitness 函数把这些全部重写为“随机选高峰”，也不能把 Ao 的 transverse component 当成某种 SRT 前对象 Selection 的数学等价物。

### 1.3 “生成的景观”与“生成切分”要分开

- **Ao/source-native job:** 在**已经声明**的变量、SDE/ODE、随机积分解释及实验建模条件内，构造势与相对稳定性／转移描述，即使该势不是一开始已知。
- **SRT/current author question:** 为什么某些区别／关系／边界在一个参与位置的实际 Selection 中成为前景/相对背景？在何种条件下形成新关系或重切分？
- **非同一性：** 从方程重构势函数是**模型层的 construction**；不能把“construction”这个英语动词自动读成 SRT L0 的 difference actualisation。两者可能在特定域通过操作化桥接，但该桥接尚未建立。
- **反向压力：** Ao/其他成熟 adaptive / latent-state / moving-boundary models 也可以建模维度、状态空间及约束改变；因此“切分生成”本身未证明是成熟理论的盲区。

## 2. 精确的对照工作表（source-owned vs SRT burden）

| Same-target 问题 | Ao 已有来源工作（A） | SRT 能保留的研究问题（作者源 / M） | 不能主张 |
| --- | --- | --- | --- |
| 势／稳定性如何量化 | 构造 stochastic potential；非平衡系统稳定态与相对概率；有相应推算方法 | 将符合条件的潜在景观作为 formed/L2 的域内读出；声明精度、尺度、噪声解释 | “势=原初 Selection”、\`Ψ_f=Ao potential\` |
| 非梯度方向及环流 | dissipative + transverse / detailed-balance-breaking，转移路径可非对称 | Gate/历史约束对可达性和转移的作用可用域模型尝试量化 | “Ao 只建模无方向随机游走” |
| 噪声变化会怎样 | AO17E 的 noise-strength 调制稳定态比例、转换 | 把 noise perturbation 作为模型内操控，不是自动引发全新 Selection-position | “加噪声就生成 SRT One” |
| 景观是否可改变 | f、D、参数、解释与模型构造影响 landscape；并非不可变图 | 区分已有状态坐标内的模型修订，与被研究参与中边界/等价关系本身的重切分 | “唯有 SRT 能重构 landscape” |
| 新对象/新关系如何出现 | SDE 模型可表示多稳态、分叉及参数相关组织 | 问一组不同观测／任务的切分更新是否共享前瞻解释约束 | “潜在类/吸引子新增=已测 SRT primitive Selection” |
| 历史/位置的地位 | 按来源所指定的状态变量、参数及动力学跟踪过程；不是关于位置本体的定理 | 检查位置参与是否对因果效果构成必要条件；先与历史敏感对手公平比较 | “加 observer/θ 已重建真实 Selection-position” |
| 数学能否穷尽本体 | 论文主张在声明条件下构造可用函数，不针对 SRT 形上学作裁决 | 作者明确“数学化是 L2 脚手架，不是本体” | “敖平数学证明 SRT”、或“SRT 已证明数学化不可能完整” |
| 证据增量 | AO17E 对其数值和疾病网络模型展示应用 | 若未来提出可区分预测，须 prospectively beat strong baseline on identical task | “SRT 科学独特性已成立” |

## 3. 概念之间的错配：避开两种反向本体化

### 3.1 SRT 的三层位置（不是把 Ao 分配到 L0/L1/L2 三个实体）

- **Primitive Selection / O0-S0**：SRT 当前本体源（Spine）说原初 actualising Selection 不需要预设选项菜单、先验 chooser 或形成后的 Ghost Operator。
- **Formed organization / Gate / history**：具体有持久、记忆、前瞻或可达性效果的组织，需要额外的形成和保留证据，不能用一个模型参数冒充。
- **L2 effective objectification/formalization**：经过单位、边界、坐标、分辨率及测量策略约束的 Ao 式 \`x, f, D, potential, action, barrier\` 可以是**非常有用**的近似工具，非新的 primitive ontology。

**注意:** “L2 脚手架”表述的是在 SRT 研究中的**认识论/使用层级**，不是声称 Ao 论文自身在 SRT 三层理论中自认属于 L2，亦不等于整套 FEP/Fisher/Ao 势都是同一个标量。

### 3.2 粗粒化术语的三义不被敖平替代

当前仓库 #1116 已区分：
1. 作者 10-10 的 Selection-generative “粗粒化”；
2. 09-25 formed Gate 的“粗粒化几何”；
3. 数学尺度投影 \`π_λ\`（可损失表征区分）。

Ao 构造势函数并**不**在概念上将三者合一。作者对“Gate 粗粒化几何是否为生成过程留下的稳定组织”明确说**不太确定**，保持 AUTHOR-OPEN；敖平的方程不会替这个问题作裁决。

### 3.3 位置参与的“非公共”主张不能豁免证伪

即使 SRT 位置参与对某些域可能重要，研究仍应区分客观的操作可重复条件／轨迹、参与者实际作用、局部因果响应和更强的本体解释。Ao 的群体／生物网络景观与位置参与任务也未必属于同一个 explanandum。它们不能因为领域不同自动互相否定或相互证明。

## 4. 2016 独立数学争论：明确保留不确定性

**强邻居不可绕过：** Zhou & Li, *J. Chem. Phys.* 144:094109 (2016), 讨论 steady-state potential、Freidlin–Wentzell quasi-potential 和 Ao A-type 路线的关系，提出一般 SDE decomposition **nonunique** 的论点。Yuan, Tang & Ao, *J. Chem. Phys.* 145:147104 (2016), 反驳并论述某些 OU 类及边界条件；Zhou & Li, *J. Chem. Phys.* 145:147105 (2016), 回应其定义和边界条件不足。2017 Ao 共同作者综述仍主张唯一性。

**本次审计不裁定哪方的完整数学论证赢得最终证明。** 用于 SRT 时，任何泛化都要完成：状态空间/变量定义、SDE 随机积分约定、扩散矩阵类别、适用域、边界条件、广义存在／唯一性、数据 identifiability 与 numerical validation。**“势函数唯一可得”不能是未经检验的 SRT 理论前提。**

这项争议不是 SRT 反驳 Ao 的直接证据，也不证明 SRT 因不要求数学化而“超越”数学争议。

## 5. Ao 与其他强邻居也不能合称一个 “Ao model”

| 方法族 | 最强来源侧已做之事 | SRT 对照时的必要控制 |
| --- | --- | --- |
| Ao SDE decomposition + A-type | 非平衡势构造、耗散/横向分解、与噪声解释相关的数学结构 | 明确 A-type 约定、边界及是否唯一；source-specific 预测 |
| Freidlin–Wentzell quasipotential | 大偏差／小噪声极限中的逃逸与最可能路径；不是任意噪声通用式 | 不能用 FW 小噪声条件内的失败虚构所有随机方法失败 |
| Wang–Xu–Wang potential-and-flux | 景观与 flux 对非平衡循环、稳健性和耗散的建模 | **另一作者体系**，不可混为 Ao 原创 |
| Zhou–Li mathematical comparison | 明确讨论 steady-state, quasi-potential, Ao 及其非唯一性条件 | 任何数学“普遍唯一”都须审议反例和边界 |
| Dynamical coarse-graining / active learning / latent cause | 模型可学习状态划分、特征权重、类别结构和参数漂移 | “原来背景成为前景”不自动比这些模型新；在 cognition 域还需 ALCOVE/SUSTAIN/latent-cause 对比 |

**模型公平性：** 不把一个 *fixed-potential toy implementation* 当成 Ao 整个文献群；要比较可表达的机制、允许的条件、参数预算、可获取的历史／行动／反馈、held-out readouts 与外部可识别性。

## 6. 正向技术价值：三个 L2 候选用例（不授权执行）

1. **局部稳定和跃迁解释：** 当 domain 数据已提供可声明的 \`x(t)\`、漂移与噪声机制，研究 \`U(x)\` / quasi-potential / action / barrier 是否能描述稳定态占据、跨越概率、方向非对称和噪声响应；先比较 Ao、FW、Wang 及普通 SDE，不从这些结果推出 SRT 原初 Selection。
2. **景观模型更新诊断：** 给定参数扰动、外部条件变化或主动干预，区分 \`U(x;\theta,t)\` 变化、稳定态／盆地变化、因历史记忆改变可达性，与**分析者重新定义状态变量/等价类**；标明哪个是模型内部动力学，哪个是换对象化协议。以上符号仅候选模型语言，不是 SRT 理论方程。
3. **跨位置参与式模型契约：** 记录谁/何种操作生成观测，干预是否改变以后的生成条件，跨场景模型重建如何执行；可让局部 Ao 动力学服务于不同角色的协作，但不能将单一 public \`U\` 视为所有位置共享的真实景观。这延续 Beacon/ChoiceMap 的 **meta-level validation contract** 方向，而非要求共同拥有完全一样的内部语义。

**优先级建议（M）：** 作为 SRT 独有证据，以上三个目前均 **NOT YET**；作为 L2 方法补充与反向压力，首先做来源公平性与任务匹配，而不是优先寻找新符号。

## 7. 在既有 CN-2 内能做什么（paper-only，且不是 Ao 实验选择）

CN-2 当前作者选择的 first E2 family A = **后果结构化多属性概念学习 + P1–P6 多探针可识别性 paper survey**。Ao 的数学动力学**不是**该 family A 的直接 baseline，因为论文主要处理非平衡随机连续系统／生物网络，而非已实现的人类后果驱动概念重切分任务。

*仅纸面可提出的筛选问题：*

- 有没有经过源方法忠实实例化、可处理反馈与后果改变的动态势景观／状态空间模型，而非一个固定峰值图？
- 它是否用同一套声明好的输入/参数／条件前瞻预测 P1 相似性、P2 分组、P3 边界、P4 事件预期、P5 异常评估、P6 行动/affordance 迁移，而不是分别对每个 probe 事后拟合？
- 它与强注意学习、SUSTAIN 聚类、latent-cause 和动态表征模型的公平比较，能否区分模型层新切分与真正新增的一组联合预测约束？
- 是否有同被试、同后果条件、独立 held-out、泄漏控制和先验注册的对照数据？如果没有，则结果为 **NOT READY / UNDERDETERMINED**。

**停止条件：** 不能因“需要新位置和新关系”就创造新实验臂、数据下载／复现、或将 Ao 直接插入 CN-2 竞争模型。它首先是一条**M-level comparator relevance question**，如 #1112 survey 后续明确要求，再提出单独评审，并获得作者另行授权。

## 8. GRG 若未来参与，应承认双向压力

现行 GRG v0.3 的 **GTS**（Generative Transformation Signature）要求 source-native mechanism、stabilized objectification、strong horizontal baseline、what is given/reopened、history input、output reconstruction、negative controls、failure conditions。

**假设的 bounded case（此刻不启动新 GRG case）**：
- input: 已有随机动态／SDE 给出的变量和噪声描述。
- transformation: 在外部干预或反馈下重设漂移/扩散/参数，或重设变量等价关系。
- output: potential/attractor/transition/readout 条件变化。
- crucial separation: **model-level** structural transition ≠ empirical claim that primitive Selection or an SRT One was identified.
- reverse constraint: 若 Ao/Wang/FW/source-native 方法已完整支付所选解释工作，只记 **SOURCE-OWNED AT THIS EXPLANATORY JOB / NO LOCAL COMPARATIVE INCREMENT**，不从 SRT 全体系减去原初问题，也不硬凑 GRG 新语法。

当前 GRG fusion/broad-synthesis §10.2 仍 **HOLD**。不得将 Ao 作为新的已获准跨域验证案例或独立深井；本节只是未来审批时可检索的方法地图。

## 9. Owner-side bounded novelty probe / subtraction

| Proposed new item? | Existing owner(s) | Bounded probe + result |
| --- | --- | --- |
| 势景观作为 SRT 新本体 operator | \`SRT_Fisher_FEP_Landscape_Interface.md\`, \`Core_Law/SRT_Reference_Dynamics.md\`, \`Core_Law/SRT_Generative_Ontology_Spine.md\` | **ALREADY OWNED AS L2/HYBRID INTERFACE, NOT NEW ONTOLOGY** |
| “Selection 可生成前景与相对背景” | Spine §3；10-10 author trace A0-Q2/A0-S9 | **ALREADY OWNED / AUTHOR-SOURCE**, 不得从 Ao 倒灌为新 primitive |
| 非详细平衡、非梯度动力学、势垒 | Ao + FW/Wang 成熟源；仓库 Reference Dynamics formed-side 方程 | **INHERITED SOURCE MECHANISM**；不可标记 SRT 独创 |
| 泛化的 “Ao 景观重塑 → SRT Gate 几何” | 09-25 Gate author trace、#1116 OPEN map | **UNRESOLVED OVERLAP**；作者明确不确定，不从数学构造推导历史留存 |
| 位置参与与重切分有新可检验增量 | CN-2 E2 family A / 2026-10-10 author source | **NOT ESTABLISHED**；现有最强邻居能处理部分任务 |
| 本 PR 的新增价值 | 上述各 owner | **SOURCE-FIDELITY + REVERSE CONSTRAINT + BOUNDED RESEARCH ROUTING ONLY**；不新建平行 schema、level、primitive、equation 或 standalone lane |

**Subtraction verdict:** \`reverse constraint\` + \`partly owned\`（仅来源比较精度、Ao 争论及方法细节的空缺得到补齐）；没有创造需要 canonical 所有权的 residual。**Inherited premises / constructive use:** 有效非平衡 L2 景观构造、限域稳定性与转移机制，SRT 可将其作为有约束的公开研究工具。**Forbidden parallel construct:** \`SRT-Ao-Potential-Primitive\`、\`Selection = Ao SDE\`、\`Gate = transverse matrix\`、\`Ψ_f = Ao U\`、\`Ao proves SRT uniqueness\`。

## 10. Falsifiers and negative/failure rights

- **无局部新颖性**：在同目标、同历史预算下，Ao/动态潜变量/主动注意模型做出同样好的预注册 held-out 联合预测 → **NO LOCAL COMPARATIVE INCREMENT**（仅该任务，不全局否定 SRT）。
- **方法不可识别**：相同数据在多个噪声积分约定或边界条件下给出不同势 → 返回 **UNDERDETERMINED**；不把模型选择强度提升为本体强度。
- **只能复述稳定态**：模型只能解释已拟合的状态占据，不能对外部扰动/转换/未来行动做独立预测 → 只作为描述性 proxy。
- **位置增益消失**：匹配 action-conditioned observables 与 history 后，位置变量不增加解释力 → 该局部位置模型减弱；这本身不证明所有位置本体主张错误。
- **模型结构更新即可解释重切分**：若强动态/主动学习 rival 完整支付本目标，停止认领“生成切分”是 SRT 独有。
- **数学论文争论未闭合**：不存在与当前任务匹配的唯一性证据 → 不可用“理论已保证唯一”叙述。
- **Ao17E 类推到临床被否**：癌症 38 维网络演示不等于患者治疗有效；不得生成健康干预建议或临床因果肯定句。

## 11. 有限外部对照三项

1. **事实冲突：** 若作者 Q1 被扩张为「Ao 只研究在固定 landscape 中的随机扰动」，则与 AO04/AO05/AO17E/AO17R 来源冲突；但作者原话只是疑问，不登记为作者已犯事实错误。**核定结论：作者事实冲突无（仅在已核直接原话范围内）。**
2. **内部矛盾：** 10-10 作者关于“粗粒化是 Selection 的生成性表现”与“数学化是 L2 脚手架”在本卡所核范围不冲突；09-25 Gate 粗粒化几何的因果谱系仍 **AUTHOR-OPEN**，而非自动矛盾。
3. **已有说法：** AO04/AO05/AO17E 的非平衡势构造／噪声变化——**部分重合**（SRT formed/L2 动态）；ZL16/FW 的准势和跃迁路径——**部分重合**（形成后的稳定/路径）；Jin Wang potential/flux——**部分重合**（非梯度循环）；均不能无损转换成 SRT primitive ontology，也不由这种 scope 差异自动产生 SRT 科学增量。

## 12. Result, scope and traceability

**本轮值不值得入库？ YES，作为 source evidence + O-track comparison discipline / reverse constraint，非 canonical。**

- [一手论文群来源卡](../../Materials/2026/SRC_2026_10_10_StatPhys_Ao_Stochastic_Landscape_Corpus.md)
- [10-10 作者原话与 Gate OPEN](../../01_Source_Intuition/SRT_AUTHOR_TRACE_VERTICAL_SELECTION_PARTICIPATION_UNIFICATION_2026-10-10.md)
- [原 #1116 初步敖平比较](SRT_VERTICAL_SELECTION_POSITION_PUBLICNESS_PRESSURE_2026-10-10.md)
- [已有 landscape interface](../../SRT_Fisher_FEP_Landscape_Interface.md)
- [形成后动力学 Reference](../../Core_Law/SRT_Reference_Dynamics.md)
- [现行 GRG GTS owner](../Proposals/SRT_GRG_FOUNDATIONAL_PROTO_GRAMMAR_V0_3_2026-09-21.md)
- [CN-2 family A paper-only 作者裁决](../../01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CN2_FIRST_E2_TASK_FAMILY_A_2026-10-09.md)
- [Pipeline 1 official log](../Material_Log/2026-10_Part01.md)

**当前状态：** paper-level source comparison complete within declared accessible subset; full mathematical uniqueness proof review, reproducibility, and any same-target prospective SRT model comparison remain **OPEN**. No Core_Law, canonical symbol, STATUS/CURRENT NEXT, existing PR, draft paper, experiment, or new GRG fusion work modified.
