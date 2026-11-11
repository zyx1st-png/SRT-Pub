---
id: SRT-SRC-2026-11-11-CN2-RELATIONAL-GEOMETRY-PROTOTYPE-LEARNING-PACKET
type: source_card
status: draft
date: 2026-11-11
layer: materials
epistemic_layer: evidence
claim_mode: source_evidence
canonical: false
ai_do_not_use_for_definition: true
research_mode: U
root_question: How do learned reference and relational structures organize cross-probe predictions, and what could distinguish shared reorganization from capable prototype or latent-state learning?
comparative_claim: none_established; candidate named-model comparison only
named_comparator: "Watters 2026; Sen 2026; Pettine et al. 2023; Love-Medin-Gureckis 2004; capable H1/H2 implementations"
n_mode_triggered: false
source_id: CN2-RELATIONAL-GEOMETRY-PROTOTYPE-LEARNING-PACKET-20261111
title: Relational geometry and prototype learning for CN-2
source_type: mixed_literature_packet_two_preprints_and_two_peer_reviewed_primary_papers_plus_public_code
domain: cognitive_neuroscience_and_category_learning
url: https://www.biorxiv.org/content/10.64898/2026.10.17.759839v1
doi: "10.64898/2026.10.17.759839; 10.64898/2026.10.21.759829; 10.1038/s41562-023-01543-7; 10.1037/0033-295X.111.2.309"
authors: "Nicholas Watters et al.; Rajyashree Sen et al.; Warren Woodrich Pettine et al.; Bradley C. Love et al."
publication: "bioRxiv (two preprints); Nature Human Behaviour (2023); Psychological Review (2004)"
date_published: "2004; 2023; 2026-10-19; 2026-10-22 (Sen v1; later v3 posted 2026-10-28)"
date_added: 2026-11-11
evidence_level: "Publisher abstracts + source-native public code/method comments; no raw neural/participant data inspection or full paper reproduction"
reliability_level: "mixed: primary peer-reviewed models and non-peer-reviewed preprints"
srt_relevance: "CURRENT NEXT neutral pre-object generative orientation / CN-2 E2 shared-geometry fair comparison"
integration_priority: B1
source_log: Operations/Material_Log/2026-11_Part01.md
related_srt_claims:
  - CN-2 E2 candidate shared geometry
  - E3 causal revaluation and E4 recursive recutting as separate future burdens
dependency:
  - Operations/Proposals/SRT_PREOBJECT_GENERATIVE_ORIENTATION_COGNITION_RESEARCH_PROGRAM_2026-09-26.md
  - Operations/Proposals/SRT_L0_FACING_E2_E4_MULTIPROBE_RECUTTING_DESIGN_2026-09-26.md
  - Operations/Audits/SRT_CN2_A_PUBLIC_DATASET_P6_E2_FEASIBILITY_TRIAGE_2026-10-11.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CN2_NAMED_MODEL_FAIR_COMPARISON_2026-10-08.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CN2_P6_CONSEQUENTIAL_INDEPENDENT_ACTION_2026-10-11.md
tags: [SourceCard, Cognition, CN2, E2, RelationalGeometry, ReferenceAnchors, ProDAtt, SUSTAIN, StrongH2, MaterialPacket]
---

# CN-2 材料卡：关系几何、参考锚点与原型学习的机制对照

> **定位：** 记录 2026-10 两篇空间/关系编码预印本与 ProDAtt、SUSTAIN 成熟类别学习机制之间的可复核联系，并保存 2026-11-11 对话提出的 ARRG-2 工作候选及其可识别性压力。**A 源事实 / B 研究侧整理 / C 开放判别**分开陈列。本卡为 Pipeline 1 的 B1 来源资料，不设立 ARRG 新模型 owner，不构成实验协议或 SRT 本体定义。

## 1. One-line summary

关系坐标与地标平方距离为“局部位置由共享参考关系组织”提供两种具体实现；ProDAtt 和 SUSTAIN 已具备动态原型、注意调整或新簇形成的强机制。CN-2 当前有价值的下一问是：具名共享组织模型能否在合法历史、同等资源下，对未参与拟合的多个探测及新组合首次行动作出更好的**前瞻预测**？

## 2. Corpus: source-native claims, evidence and anchors (Layer A)

| ID | 来源 / 类型 | 实际来源主张与可复核锚点 | 本轮检查范围 |
|---|---|---|---|
| W26 | Watters, Gabel, Tenenbaum & Jazayeri, [*A Relational Code for Objects in Primate Frontal Cortex*](https://www.biorxiv.org/content/10.64898/2026.10.17.759839v1), bioRxiv v1 (2026-10-19), DOI 10.64898/2026.10.17.759839；**预印本** | 灵长类额叶眼动相关区域在多对象工作记忆任务中编码单对象位置与对象间空间配置。[作者代码 README](https://github.com/jazlab/relational_coding_2026) 说明两只猴、多对象记忆、DANDI 000620 数据及图 3/4 的模型对照；[models_lib.py — `remap_angle`, `FutureFieldModel`, `RelationalBiasModel`](https://github.com/jazlab/relational_coding_2026/blob/main/figures/figure_4/models_lib.py) 给出实际变换与响应函数；[fit_lib.py](https://github.com/jazlab/relational_coding_2026/blob/main/figures/figure_4/fit_lib.py) 给出 2-object Poisson likelihood / split 方案 | 预印本摘要、公开 README、源码注释与函数；**未**下载 DANDI/OSF 缓存，未复现神经拟合或全部图表 |
| S26 | Sen, Posani, Medoff, Zhang, Abbott, Axel & Fusi, [*A new neural code for position: generalizable spatial maps in mouse medial frontal cortex*](https://www.biorxiv.org/content/10.64898/2026.10.21.759829v1), bioRxiv v1 (2026-10-22), DOI 10.64898/2026.10.21.759829；**预印本** | 利用小鼠 mFC、dCA1、lvOFC 的钙成像，在有地标的方形场地研究位置编码；mFC 的线性位置解码由一个场地区域外推至其他区域；多地标**平方距离编码**能解释其空间表征的若干几何性质。参见 v1 **Abstract**。另有 [v3](https://www.biorxiv.org/content/10.64898/2026.10.21.759829v3)，2026-10-28 posted，页面注明 methods notation homogenization | v1/v3 发布记录与公开摘要；未复核完整方法、额外补充分析或原始数据。**跨解码器训练区域泛化**不等于已证明动物从未经历该空间 |
| P23 | Pettine, Raman, Redish & Murray, [*Human generalization of internal representations through prototype learning with goal-directed attention*](https://doi.org/10.1038/s41562-023-01543-7), *Nature Human Behaviour* 7:442–463 (2023)；**同行评审原始研究** | 三类潜在状态学习任务；多数参与者同时依赖目标相关辨别特征和原型内特征协方差。参见期刊 **Abstract / Data availability / Code availability**；[公开模型源码 `agentState.updateMu/updateCov/updateValue`、`agent.createNewState`、`calcActivation`](https://github.com/murraylab/instrumentalLatentStateLearning/blob/main/simulations/algorithmicmodels.py)；[任务源码](https://github.com/murraylab/alienArtifactsLearningTask) | 期刊摘要与代码级机制读取，未分析 [Zenodo 7186975](https://zenodo.org/records/7186975) 的行为记录，也不对部署版本作同一性断言 |
| L04 | Love, Medin & Gureckis, [*SUSTAIN: A Network Model of Category Learning*](https://doi.org/10.1037/0033-295X.111.2.309), *Psychological Review* 111(2):309–332 (2004)；**同行评审模型研究** | 自简单类别结构起步；遇到现有结构无法解释的事件时可增加类别簇；簇随后可以发展为原型、吸引子或规则。参见原文 **Abstract / Principle 1: Simple First / cluster recruitment**；[PubMed](https://pubmed.ncbi.nlm.nih.gov/15065912/) | 期刊摘要与作者公开机制概述；未复现各仿真实验。SUSTAIN 原始类别学习不应直接当作已实现 CN-2 P6 行动任务 |

**证据层级说明：** W26/S26 属 2026 年预印本；P23/L04 属已发表同行评审研究。论文/源码支持各自的任务和模型，不直接支持本卡下一节的 SRT 工作假设。

## 3. Mathematics worth retaining (derived analysis, not a quoted result from all papers)

### 3.1 Relational coding is a defined transform

W26 公开代码的 `FutureFieldModel` 在两对象神经元放电率模型中，将视网膜坐标驱动与重新映射的相对坐标驱动相加：

```text
rate = baseline
     + a_ret × [f(phi_A) + f(phi_B)]
     + a_rel × [f(remap(A,B)) + f(remap(B,A))]
```

其中 `remap(A,B)` 为 **从 B 看向 A 的方向**，在等半径圆环配置中可通过角差向量计算；当两对象相对处于圆环对跖点时该变换退化，不能把这一特定实现直接推广成普遍多维关系几何。W26 的神经层 readout 也不是 CN-2 的人类行为 P1–P6 readout。

### 3.2 Landmark squared-distance geometry

对固定锚点 `l_i` 和位置 `x`，定义 `d_i²(x)=||x-l_i||²`。两锚点的平方距离差满足：

```text
d_i²(x) − d_j²(x)
= −2(l_i − l_j)^T x + ||l_i||² − ||l_j||²
```

因此，共同参考关系可形成关于 `x` 的线性读出。**这是标准代数推导和 S26 机制的数学解释，不是本轮从论文中抽出的新增定理或新实证结果。** 其概念学习迁移需要另外声明“锚点是什么、如何获得、哪些维度允许迁移”。

### 3.3 Why moving anchors alone is not a distinctive generative mechanism

在**固定对称度量** `M` 下，两个可移动原型 `c_i,c_j` 的二次距离差同样为：

```text
D_i(x) − D_j(x)
= −2(c_i − c_j)^T M x
  + c_i^T M c_i − c_j^T M c_j
```

若读出是“选择距离更近的原型”，两个原型的竞争边界仍为仿射超平面。移动锚点能改变预测，但它可以由成熟原型更新机制实现；**观察到边界移动本身不区分“重新加权、原型移动、簇重组或更一般的组织重构”**。非线性读出、动态度量、不同原型竞争与任务切换需另行比较，不能从上述两原型特例直接排除。

## 4. SRT relevance and mechanism crosswalk (Layer B; M-origin synthesis)

**现有研究问题：** 一个持续生成、归一化、具方向性的认知组织如何形成，并规定后续局部对象化、转移预期和行动的可能结构？相关 owner 是当前 [pre-object generative orientation programme](../../Operations/Proposals/SRT_PREOBJECT_GENERATIVE_ORIENTATION_COGNITION_RESEARCH_PROGRAM_2026-09-26.md)，而 [CN-2 多探测设计](../../Operations/Proposals/SRT_L0_FACING_E2_E4_MULTIPROBE_RECUTTING_DESIGN_2026-09-26.md) 已经提出了共享几何、后果结构变化与递归重切的测量路线。

| 研究机制 | 源头承担的局部解释 | 对 CN-2 的建设性用途 | 不能由该来源直接付清的负担 |
|---|---|---|---|
| W26 相对坐标混合编码 | 对象的自身位置与相互配置共同影响神经响应 | 为“局部表征 + 关系变换”指定具体候选机制 | 共享组织如何**形成/更新**以及人类跨探测行动读出 |
| S26 多地标平方距离 | 基于多个稳定参考点的位置线性外推 | 为“参考结构约束局部位置和远端泛化”提供几何实例 | 学习可变参考结构以及概念/行动迁移 |
| P23 ProDAtt | 原型、协方差、辨别性注意、奖励与动作价值更新；具备状态增加机制 | 给“动态锚点 + 行动后果”提供直接、强的成熟模型对照 | 原任务不是同人完整 P1–P6 的交叉探测测试 |
| L04 SUSTAIN | 任务相关簇生成、注意重配和类别结构学习 | 给“新对象/类别组织形成”提供成熟结构学习对照 | 原任务未直接定义后果承担的首次独立行动 P6 |

**对话工作标签 `ARRG-2`（Adaptive Reference–Relational Geometry）：** 仅指“参考点/原型位置与关系组织可随合法历史修订”的 **M-origin 对照草图**，不是已冻选的独立模型、仓库术语、SRT 机制或 author decision。P23 的 `updateMu`/`updateCov`/`createNewState` 已显著覆盖该草图的局部计算职责。本卡保留 **“ARRG-2 的动态锚点尚不能说明独立预测增量”** 这一确切结论，同时保留多探测共同组织的问题价值。

## 5. Prospective CN-2 identifiability map (Layer C: questions only)

| Probe / stage | 观察目标 | 主要模型能力需求 | 使结果有意义的留出要求 |
|---|---|---|---|
| P1 相似性 | 物体的主观距离 | 度量 / 原型 / 注意权重 | 训练观察与测试刺激分离 |
| P2 分组 | 形成的等价/类别组织 | 簇、潜在情境与组别读出 | 不用测试分组结果反向拟合几何 |
| P4 转移预期 | 事件接续的概率 | 关系及序列/转移模型 | 不向模型泄漏测试未来 |
| P3 边界 | 模糊刺激的边界位置 | 事先定义的几何→边界读出 | 与 P1/P2/P4 跨探测留出 |
| P5 异常 | 人类报告的惊异/异常 | 预测分布 + 人类报告校准 | 人类报告的时间与 P6 后果反馈分开 |
| P6 新行动 | 从未直接训练的组合上，参与者**第一次独立选择的有实际后果的行动** | 原型/潜在状态 + 目标/行动空间/政策读出 | 每参与者×每具体新组合仅计首次遭遇、同组合后果反馈不可提前可见；实际结果只作后果有效性与时序检查 |

在所有竞争臂中，明确合法历史、已学行动类型、可用选择集合、目标及反馈时点；对模型和参与者均防止组合后果泄漏。单独区分 **cross-probe on known stimuli**、**first-encounter novel combination**、**repeat without feedback**、**repeat after feedback**。后两者不能冒充首次迁移，重复后的变化可进入单独的 forward-learning 问题。

**候选具名模型谱系（不是冻结实现列表）：** GCM/MDS、ALCOVE、SUSTAIN、P23 ProDAtt、允许可实现结构修订的潜在状态/生成模型，以及具备同等行动目标与后果学习能力的模型。只有声明 **具体实现、可用训练输入、结构学习权限、参数/资源预算、每探测读出、测试分布和预先锁定的预测分数** 后才是公平 E2 比较。复杂度/压缩可作次级评价，不能替代留出预测增益。

**候选模型层级：** `G_t` 表示推断的共同组织，`R_j(G_t,x,q_j)` 表示各局部探测读出；`G_{t+1}=F(G_t,h_t,o_t)` 表示在合法历史/后果下的组织更新。这些是 **工作性结构占位表达**，并不指定新 SRT 原语，也不假定所有 P1–P6 已被观察。若 `Δy≈JΔg` 形成低维共同变化，也必须与可产生相同结构的成熟 H2 模型比较，不能只把“低维变化”当成胜出证据。

**E2** 先问具名模型的多探测留出预测；**E3** 才问后果重新估值引起的因果重构；**E4** 另问行动/对象化后果是否改变下一轮形成条件与继续可达性。E4 比普通 history writeback 的语义更广。本卡不设立新协议、不运行模型；目前 CN-2 完整跨探测数据仍为 **NOT READY**，参见 [公开数据适用性审计](../../Operations/Audits/SRT_CN2_A_PUBLIC_DATASET_P6_E2_FEASIBILITY_TRIAGE_2026-10-11.md)。

## 6. Owner-side bounded novelty / nonduplication probe

- **Candidate increment:** 两类可复核关系几何与 P23/L04 强结构学习机制的同页对照；从具体距离恒等式确定“锚点移动本身不区分机制”的可识别性压力；面向 CN-2 P1–P6 的读出与留出接口。
- **Likely owners:** 现有 cognition programme；E2–E4 multi-probe design；CN-2 public-dataset feasibility triage；[H1/H2/H3 level audit](../../Operations/Audits/SRT_L0_FACING_FIELD_H1_H2_H3_LEVEL_RECLASSIFICATION_2026-09-26.md)。
- **Bounded probe:** 本卡的 `shared geometry / whole-field / H2`、`future reachability / coordinated recutting`、`Pettine / prototype / latent-state` 与这些 owner 对齐；不是将 ARRG 另立平行 route。
- **Verdict:** **already owned** for the CN-2 cross-probe E2 question and H1/H2/H3 level separation; **reverse constraint** for moving-anchor novelty; **partly owned** for newly collated W26/S26 first-party mathematical mechanisms and their interface comparison.
- **Residual after owner subtraction:** 暂无已确立的独立科学增量；留下源材料与未来具名模型可识别性问题。
- **Inherited premises / constructive use:** 利用邻域成熟模型完善共享组织的机制设计，明确读出、训练历史、first-choice 时序与潜在结构更新能力。
- **Forbidden parallel construct:** 不注册 ARRG 或新 `G_t` 为 canonical theory/empirical owner；不能把 ordinary action choice 同一化为原初 Selection。

## 7. Pipeline 1 decision and suggested target

| 门 | 结论 |
|---|---|
| 相关性 | PASS：直接关联 CURRENT NEXT / CN-2 E2，可作为 E3/E4 方法线索 |
| 贡献 | PASS（来源机制与 reverse constraint）：“动态锚点本身”需被 ProDAtt 吸收；跨探测预测问题保留 |
| 证据等级 | PASS with scope：2 篇 preprint abstract/作者代码 + 2 篇 peer-reviewed 论文摘要/公开机制 |
| 可对齐 | PASS：关系坐标、锚点距离、原型更新、簇生成、行为读出对应不同工作 |
| 风险 | BOUNDED：未核全文/神经/行为原始数据，尚无公平具名模型实跑 |
| 落点 | **B1 SourceCard + Material Log**；未来 CN-2 具名模型可识别性纸面审计可引此卡 |

- **Contribution route:** O-track = 具体关系/参考机制的研究组织与方法反向约束；D-track = prospective only / **not claimed**。
- **Suggested patch target:** 只读回链 cognition programme 与 E2–E4 design；本轮**不**增设 PatchNote / Hook / canonical、STATUS、论文主张。
- **Revival event:** authoritative trigger **仅在 Material Log**：现有 CN-2 task family A 开始具名模型可识别性审计或 P1–P6 可合法预测读出与数据源复核时，先重读 W26/S26 模型与 P23/L04 任务一致性。

## 8. Sources and cross-reading

1. [Watters et al., bioRxiv 2026, v1](https://www.biorxiv.org/content/10.64898/2026.10.17.759839v1)；[research code/figure recipes](https://github.com/jazlab/relational_coding_2026).
2. [Sen et al., bioRxiv 2026, v1](https://www.biorxiv.org/content/10.64898/2026.10.21.759829v1)；[v3 updated methods notation](https://www.biorxiv.org/content/10.64898/2026.10.21.759829v3).
3. [Pettine et al., *Nature Human Behaviour* 2023](https://doi.org/10.1038/s41562-023-01543-7)；[model](https://github.com/murraylab/instrumentalLatentStateLearning)；[task](https://github.com/murraylab/alienArtifactsLearningTask).
4. [Love, Medin & Gureckis, *Psychological Review* 2004](https://doi.org/10.1037/0033-295X.111.2.309).
5. [CN-2 author first-family A decision](../../01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CN2_FIRST_E2_TASK_FAMILY_A_2026-10-09.md)；[P6 independently consequential choice decision](../../01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CN2_P6_CONSEQUENTIAL_INDEPENDENT_ACTION_2026-10-11.md).
6. [CN-2 paper source feasibility](../../Operations/Audits/SRT_CN2_A_PUBLIC_DATASET_P6_E2_FEASIBILITY_TRIAGE_2026-10-11.md) — prior strong-P6 and leakage scrutiny; do not call the published action task a pure category-label task.
