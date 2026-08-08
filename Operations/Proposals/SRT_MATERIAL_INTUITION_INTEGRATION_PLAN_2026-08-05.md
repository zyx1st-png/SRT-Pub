---
id: SRT-OPS-PROPOSAL-MATERIAL-INTUITION-INTEGRATION-2026-08-05
type: proposal
status: draft
record_stage: awaiting_author_decision
layer: meta
epistemic_layer: os
claim_mode: governance
claim_level: P3/P4_governance
canonical: false
date: 2026-08-05
source_of_truth: "worktree @ a07d2a72（main：Reconcile paper workflow, review queue, and author decisions #742）"
dependency:
  - SRT-MATERIAL-PIPELINE
  - SRT-MATERIAL-LOG
  - SRT-WORKLINE-AUTHOR-PRIORITIES-20260805
  - SRT-OPS-AUDIT-HOOK-CLOSURE-2026-07-25
  - SRT-REVIEW-QUEUE
  - SRT-PARKED-INDEX
tags: [Governance, Proposal, Pipeline1, IntegrationHook, SourceIntuition, Book, Papers]
---

# 外部材料与直觉卡片融入方案（提案 / 未执行）

> **性质**：运行层提案备忘。**本文件不执行任何融入动作**，不修改 canonical、公理、方程、符号、claim level、书稿正文或已投稿论文。
>
> **与作者排期的关系**：`Operations/SRT_WORKLINE_AUTHOR_PRIORITIES_2026-08-05.md §9` 已把「完成此前未融合材料的 Pipeline 1 收口」定为当前第一优先。本文件是该条裁决的**盘点与施工分解**，不是另立一条竞争路线。
>
> **审计方法**：所有数字来自对当前 worktree 的实证扫描（文件计数、frontmatter 字段读取、按文件名/关键词交叉比对），不采信文件的自述状态。方法沿用 `Operations/Audits/Hook_Closure_Audit_2026-07-25.md` 的实证原则。

---

## 1. 现状盘点（可核验事实）

### 1.1 结论先行

仓库并**不是**「材料堆着没人处理」。相反：Pipeline 1 已处理约 207 条材料，其中 130 条判 A；书稿已实质吸收多部外部专著（西蒙东出现在 13 章、巴拉德 16 章、迪肯 7 章、达马西奥 5 章、詹姆斯 5 章、Friston 6 章）。

真实问题是另一个形状：

> **进料通道有四条，权威台账只有一条，而台账只覆盖其中一条半。**
>
> 于是「有没有融入」这个问题，在仓库里目前**无法用机器回答**，只能靠人逐个回忆。

### 1.2 四条并行进料通道

| # | 通道 | 产物落点 | 是否进 Material Log | 现状 |
|---|---|---|---|---|
| C1 | Pipeline 1 材料融合 | SourceCard → domain patch → hook → domain owner file | 是（权威） | 主干健康，末段（hook→正文）有 28 个未落地靶点 |
| C2 | 书稿融合轮（SourceCard 内自称 "Pipeline 3 / book fusion / endnote layer"） | External_Theory_Notes 插入地图 → `Drafts_26Q/` 章末注 | **部分/否** | 6 条台账行滞留未并入，4 部专著完全不在台账 |
| C3 | 直觉挖掘（ChoiceMap trace / ghost card / 对话材料） | 03_Bridges T-B/T-D/T-E、作者裁决文件 | 否（另有 `_SRT_CHOICE_TRACE_LOG.md`） | 主干已收口，但 `d/q/o` 支线全部悬空 |
| C4 | 外部趋同证据卡 `04_External_Convergence/` | EC 卡 + 矛盾台账 | 否 | 10 张卡，**accepted = 0**，全部 `draft_v1` |

### 1.3 逐项数字

**材料层**

- Material Log：10 个分月 part；STATUS 口径 207 条（A 130 / B 27 / C 50）。本轮按表格列解析得 211 条（A 132 / B 29 / C 50）——**差值 4 条需对账**，可能来自跨行条目或标题行误计，属低风险但应查清。
- `Materials/2026/`：59 张 `SRC_*.md` + 2 张 packet index。
- **12 张 SourceCard 在任何 Material Log part 中都没有按文件名出现的记录行**：
  - 其中 6 张有写好的独立台账条目，**滞留在 `Operations/material_log_entries/` 从未并入**：Spontaneous Collapse、Pacherie、Cosmological Principle、Quantum Proper Time、FEP Book、Blind Spot；
  - 另 6 张在台账中**完全不可见**：Damasio *Feeling & Knowing*、Deacon *Incomplete Nature*、Simondon *Individuation*、James *Principles of Psychology*、Wentzell preattentive vision、Quanta *Reasoning Right for the Wrong Reasons*。
  - 后者中，Wentzell 已有 `NEURAL19_Preattentive` patch + hook，Quanta 卡自带 `integration_decision: A-bounded` 并已有 `AIREASON01` patch——**产物存在，台账无记录**。

**补丁 / 钩子层**

- patch 31 张，hook 24 张。
- **7 张 patch 没有对应 IntegrationHook**：Physics `P06`、`P07`、`P08`、`REP01`；Neuroscience `NEURAL18`；AI `AIREASON01`、`AIEVID01`。它们只到"补丁"就停了，没有落地账。
- hook 状态（按 frontmatter `integration_status`）：**landed 12 / partial 3 / pending 9**；`landing_ledger` 中 `state: pending` 的靶点合计 **28 个**。

**28 个 pending 靶点的真实构成**（这一步至关重要——它把"28 个欠账"砍成 15 个）：

| 类别 | 数量 | 性质 |
|---|---:|---|
| 普通域内靶点 | **15** | 真正可施工的部分 |
| 靶点文件**不存在** | 4 | P03/P04/P05 → `Physics/SRT_Physics_Bridge_v0_2.md`；NEURAL19_Preattentive → `Neuroscience/SRT_Neuroscience_Hardening_N1_N12_v0_2.md` |
| 靶点是 **Core / canonical** | 5 | `_SRT_T_DIR_CANONICAL.md` ×2、`Core/SRT_Core_14` ×1、`Core/SRT_Core_25` ×1、`Core_Law/SRT_Occlusion_Dynamics` ×1——**须走编辑协议单独授权，不随材料收口一并授权** |
| 靶点在**停驻区** | 4 | `90_Backstage/Incubation/` 下的 ChoiceMap 原型种子 ×3、对象性元标准 ×1。它们的复活触发条件已登记在 `_SRT_PARKED_INDEX.md §1`，**属合规停驻，不是欠账** |

**靶点存在性全量扫描结果**：28 个去重靶点中，实际缺失 2 个文件（上表），另有 1 个靶点根本不是路径而是占位描述（`future subjective-time bridge document`）。

**命名不一致**：hook 写的合成靶是 `N1_N12_v0_2`，`_SRT_Recent_Material_Patches_Index.md` 推荐的是 `N1_N13_v0_2`——**两个名字指的是同一个从未创建的文件**。
- patch 的 ID 命名有两套并存写法（`PATCH-*` 与 `SRT-*`），hook 用 `patch_id: PATCH-*` 回指。**结果是 patch↔hook 闭合目前无法机检**——这正是 2026-07-25 hook 审计对 `status` 字段所修的同一类病，在 `patch_id` 上复发。

**结构性死锁：两个"落点文件不存在"**

| 缺失文件 | 谁在等它 |
|---|---|
| `Physics/SRT_Physics_Bridge_v0_2.md` | P03/P04/P05 三张 hook 的**唯一**落点；`_SRT_Recent_Material_Patches_Index.md` 也把它列为推荐合成靶 |
| `Neuroscience/SRT_Neuroscience_Hardening_N1_N12_v0_2.md`（索引里又写作 `N1_N13_v0_2`） | NEURAL19_Preattentive 的落点；NEURAL22 等多张 neuro patch 的"未来合成"落点 |

这两个文件从未被创建。所以相关 hook 的 `pending` **不是"还没排上工"，是"在等一个不存在的靶子"**。Physics 三张的归属已作为 `RQ-2026-08-A04` 挂在作者裁决队列。

**直觉层**

- `01_Source_Intuition/`：11 份 choice-trace / ghost card；`Conversations/` 10 份对话材料。
- 主干已收口：T-B / T-D / T-E 首轮 bridge 已建（#712、#713、2026-08-04），五域联合压力测试已完成，choice-trace 作者门已关闭。
- **悬空支线**：`d/q/o` 三轴线（2026-07-23 至 07-25 三份对话材料）。收尾审计的自述结论是「**全部路由为候选，无一落地**」，且有三条明确触雷（`q` 与 canonical `d` 语义重叠、`o` 作为封闭单标量与 `OPEN_TENSIONS §9` 冲突、`d` 取宽度与 `Def-d-canonical` 冲突）。当前护栏：**形式选择完成前 `d/q/o` 不得进入书稿、公共内容、bridge 或论文**（`RQ-2026-08-A02`，Awaiting author）。

**书稿层**

- 13 张 SourceCard 明确点名书稿章号；卡内章号引用频次 Q17 (67) ≫ Q24 (34) > Q28 (25) > Q16 (19) > Q25 (18) > Q14 (16) > Q19 (15) > Q26/Q10 (11)。
- 但**不存在一份按章聚合的材料输入清单**。作者要为 Q17 做一次统一优化，目前只能反向翻 59 张卡。
- 已有的书稿吸收（詹姆斯 5 章章末注等）证明通道本身有效——缺的是索引，不是方法。
- `SRC_..._BlindSpot` 卡 §7 显式列出「后续可开采的开口（未在本轮施工）」：Q12–14、Q16、Q20、Q22/Q23、Q24、Q28。**这类"已识别未施工开口"目前没有任何汇总处。**

**论文层**

- 全 `Papers/` 目录中，引用 SourceCard 或 `04_External_Convergence/` 的文件**只有 1 个**（`Papers/selective_resynchronization/00_source_audit.md`）。
- 换言之：**材料→论文通道实际上不存在**。130 条 A 材料没有一条被结构化地供给到任何一篇论文的 related work / limitations / discussion。

---

## 2. 诊断：这是五种不同的欠账，被压成了一句话

把它们混为一谈会导致错误施工。必须分开：

| 编号 | 欠账类型 | 性质 | 理论风险 | 是否真欠账 |
|---|---|---|---|---|
| **D1** | 台账缺口（12 张卡失联、6 条滞留条目、4 条计数差、patch_id 双写法） | 纯记账 | 无 | **是**，且成本最低、收益最高 |
| **D2** | hook → 域内正文的 28 个未落地靶点 | 施工 | 低（域内 P3/P4，且休眠层不自动升级） | **部分**：其中 4 个被"落点文件不存在"死锁 |
| **D3** | `d/q/o` 直觉支线悬空 | 形式选择 | **高**（与 canonical `d` 冲突） | **否**——这是待裁决，不是待施工 |
| **D4** | 材料→论文通道缺失 | 结构缺口 | 无 | **是**，但当前两篇稿件在审，不宜动 |
| **D5** | B 卡 27 条、EC 卡 accepted=0 | 已被治理定义为正常终局 | 无 | **否**——见下 |

**关于 D5，必须写死，防止本轮把它重新变成欠账：**

- `Operations/_SRT_MATERIAL_PIPELINE.md §B 类语义修订`（2026-07-20 起）已裁定：B 卡是「停驻 + 具名触发条件」，**无人点名的 B 卡作为档案永久停驻，不产生维护义务；这是正常终局，不是欠账**。本方案不清空 B 队列。
- `04_External_Convergence` 的 `accepted = 0` 不是懒惰，是硬度守恒纪律的正确结果（见 memory: 形式化产能远超判决产能）。**不得为了"看起来完成"而批量升格 EC 卡。**

**关于 D3，同样写死：**

`d/q/o` 的问题不是「还没写进去」，而是「写进去会和 canonical `d` 打架」。它不属于本方案的施工范围，只作为**阻塞项**上报（§5.2）。

---

## 3. 融入方案（六档，按依赖排序）

> 施工纪律：每一档独立成 PR；不跨档合并；每档都可单独中止而不留半成品。
> 全程遵守：休眠层（AI / Neuroscience / Physics / Spirituality）**不因材料到来自动升级 canonical 或正文**；A 类正文回写必须先做**去材料化改写**。

### 第 0 档 · 台账收口（无理论风险，先做）

**目标**：让「这条材料融没融」变成一个**机器可回答**的问题。

| 动作 | 说明 |
|---|---|
| 0.1 | 把 `Operations/material_log_entries/` 的 6 条滞留条目并入对应分月 part，然后**删除该目录**（消灭第二本账，符合治理原则③） |
| 0.2 | 为 4 部完全失联的专著（Simondon / Deacon / Damasio / James）**补写台账行**。它们均已在书稿落地，故补的是 `A` 行 + 实际落点 + 「经 C2 书稿融合轮」的通道说明，**不是重新裁决** |
| 0.3 | 为 Wentzell、Quanta *Wrong Reasons* 补台账行（产物已存在：`NEURAL19_Preattentive` patch+hook；`AIREASON01` patch） |
| 0.4 | 对账 207 vs 211，修正 `_SRT_MATERIAL_LOG.md` 索引表的 Rows 列与 STATUS 口径 |
| 0.5 | **统一 `patch_id` 命名**为 `PATCH-<DOMAIN>-<ID>-<SLUG>` 单一写法，7 张 `SRT-*` 写法的 patch 改齐 |
| 0.6 | 新增 `scripts/check_material_closure.py`，进 preflight CI。三条检查：<br>① 每张 `Materials/2026/SRC_*.md` 在 Material Log 有且仅有一行；<br>② 每张 patch 有 `patch_id`，且能被某张 hook 回指，或在白名单里注明「有意无 hook」；<br>③ 每张 hook 的每个 `landing_ledger.target` 是**合法路径且文件存在**（不检查内容，只检查靶子在不在）——当前会报出 2 个缺失文件 + 1 个非路径占位串 `future subjective-time bridge document` |

**验收**：checker 全绿；`Operations/material_log_entries/` 不再存在；台账行数与 STATUS 口径一致。

**为什么先做这个**：第 0 档做完之后，后面每一档的"还剩多少"都由 checker 自动报数，作者不必再靠记忆判断收口进度。

---

### 第 1 档 · 解死锁（4 项作者裁决 + 2 个缺失落点）

**这一档不是施工，是拍板。** 在这四项之前，第 2 档的 12 个靶点无法动工。

| 项 | 问题 | 已挂在 |
|---|---|---|
| 1.1 | Physics P03/P04/P05 落到**新建** `SRT_Physics_Bridge_v0_2.md`，还是并入现有 `Physics/_SRT_Phys_Bridge.md` | `RQ-2026-08-A04` |
| 1.2 | `Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md` 是否创建；若不创建，NEURAL18/21/22 改落 `SRT_Neural_Mechanisms_CompactCore.md` 还是继续停驻 | 本方案新增，建议并入 `RQ` A 区 |
| 1.3 | 7 张无 hook 的 patch：补 hook、判定"有意无 hook"（如 REP01 自述"未来仅在 synthesis 时吸收"），还是降级停驻 | 本方案新增 |
| 1.4 | `d/q/o` 形式地位 | `RQ-2026-08-A02`（已在队列，**本方案不催办**） |

**建议默认（保守，非结论）**：1.1 取「并入现有 `_SRT_Phys_Bridge.md`」——避免再造一个 `v0_2` 空壳继续制造死锁；1.2 同理，不新建 `N1_N13_v0_2`，改把靶点指向已存在的 compact core；1.3 对 REP01 与 P06/P07/P08 判「有意无 hook + 写明触发条件」，只给 NEURAL18、AIREASON01、AIEVID01 补 hook。

---

### 第 2 档 · hook → 域内正文落地（28 个靶点）

依赖第 1 档。按**已解阻塞**的顺序做，不按材料日期。

| 批次 | 内容 | 靶点数 | 说明 |
|---|---|---:|---|
| **2A** | AI `AIGOAL01` 全部 4 靶 | 4 | 无阻塞，风险最低，**建议第一批** |
| **2B** | Neuroscience 普通靶点（compact core / predictions table / N12 astrocyte） | 11 | 休眠层：只做 bounded 吸收，**不动 canonical、不动意识定义** |
| **2C** | Physics P03/P04/P05 | 3 | 依赖 1.1 |
| **2D** | NEURAL19_Preattentive 的合成靶 | 1 | 依赖 1.2 |
| — | **停驻区靶点 ×4** | 4 | **不做**。已有具名触发条件（IRP / ChoiceMap 产品线重启、对象暗线扩展），把 hook 对应行改标为「parked + 触发条件」即可，不算欠账 |
| — | **Core / canonical 靶点 ×5** | 5 | **不做**。`_SRT_T_DIR_CANONICAL` ×2、`Core_14`、`Core_25`、`Occlusion_Dynamics`——触碰 canonical 须走 `Governance/SRT_EDIT_PROTOCOL.md` **单独授权**，不在材料收口范围内 |

**净可施工量 = 19 个靶点**（2A–2D），不是 28。剩下 9 个中，4 个合规停驻、5 个需另行授权。

**每个靶点的完工定义**：目标文件里存在一段**去材料化**的原生段落（读者不需要读 SourceCard 就能懂），且 hook 的 `landing_ledger` 对应行改为 `state: landed`，`integration_status` 相应更新。**由第 0 档的 checker 复核靶子存在性，由人工复核内容落地**——沿用 2026-07-25 审计的"字面锚串 grep"方法。

---

### 第 3 档 · 书稿统一优化的材料输入包（**只做输入包，不改正文**）

作者排期已裁定：书稿统一优化**等待材料收口后**再启动，且**不得因单篇材料到来触发局部重写**。本档严格遵守——**产出的是给未来那一轮用的弹药，不是改书**。

**动作**：新建 `Materials/2026/INDEX_BOOK_CHAPTER_MATERIAL_ROUTING.md`（按章聚合，而非按材料聚合）：

```text
每章一节，内容为：
- 已落地：本章已吸收哪些外部材料（章末注编号 → SourceCard）
- 待评估：哪些 SourceCard 点名本章但未施工（含各卡自述的"未施工开口"）
- 禁区：该章不得写入的表述（各卡"反向修正"栏的汇总）
- 饱和警告：该章是否已被某类材料饱和（如 Q16 已被 4E/Thompson 饱和，再加须防稀释）
```

**优先级由材料密度给出**（这是数据，不是判断）：Q17(67) → Q24(34) → Q28(25) → Q16(19) → Q25(18) → Q14(16) → Q19(15)。

**边界**：本档**不写一个字的正文**。它的全部价值是：让未来那一轮统一优化，能一次性看到某一章的全部材料压力、全部禁区和饱和状态，而不是逐张翻卡。

---

### 第 4 档 · 建立材料→论文通道（当前只建管道，不动稿件）

当前两篇稿件在审 / 在转投，**不得改动**。本档只做两件不碰稿件的事：

| 动作 | 说明 |
|---|---|
| 4.1 | 在 `Operations/_SRT_PAPER_PIPELINE.md` 增加一节「材料供给接口」：规定新论文立项时**必须**先跑一次 SourceCard/EC 卡检索，产出 related-work 候选清单 |
| 4.2 | 建 `Papers/_MATERIAL_ROUTING.md`：把 A 类材料按论文线（selective_resynchronization / history_dependent_reachability / ontological_friction / markov_blanket / SEA 方法论文）分组，标注可用作 related work、可用作 limitations、可用作 negative control 三类 |

**已识别的高价值候选**（来自台账备注栏，仅供 4.2 落位，不构成引用承诺）：
- Bradley 熵-operad → `Psi_f` 组合律形式化 / Fisher 论文 related work；
- Zhang & Levin *Learnable Novelty* → HDR 的 future-structure endpoint；
- 热力学计算机组 → selective-resynchronization 的 related work 与 HDR external-programming 负控制；
- 水结冰 / nucleation → HDR 的**自然负边界对照**（"稳定不等于可达"）。

**边界**：不因本档改动任何已投稿论文的科学内容。

---

### 第 5 档 · 直觉线（**阻塞中，本方案不施工**）

- `d/q/o`：等 `RQ-2026-08-A02`。裁决前，护栏「不得进入书稿、公共内容、bridge 或论文」**继续有效且本方案不申请豁免**。
- T-B/T-D/T-E 三桥：首轮已合入，状态为「待跨域压力测试」。本方案**不启动**压力测试——它属于理论推进线，不属于材料收口。
- ghost / 阴阳 / 代理对象 / 协调身份 四张 continuation card：均自述"暂停在某个未决问题"。**建议维持暂停**，在第 3 档的按章输入包里为它们各留一行"来源直觉指针"即可，不强行形式化。

---

## 4. 排序、工作量与验收

| 档 | 前置 | 性质 | 理论风险 | 建议 |
|---|---|---|---|---|
| 0 | 无 | 记账 + CI | 无 | **立即可做，一个 PR** |
| 1 | 无 | 作者拍板 | 无（拍板本身无风险） | **本方案唯一真正需要作者的部分** |
| 2 | 第 1 档 | 域内施工（19 靶点） | 低（canonical 与停驻靶点已剔除） | 分 4 个 PR |
| 3 | 第 0 档 | 索引 | 无（不动正文） | 一个 PR |
| 4 | 无 | 管道 | 无（不动稿件） | 一个 PR |
| 5 | `RQ-2026-08-A02` | — | 高 | **不做** |

**全局验收（"材料收口完成"的定义）**：

1. `check_material_closure.py` 三项全绿；
2. `Operations/material_log_entries/` 已消灭；
3. 每张 hook 的 `integration_status` ∈ {landed, 有具名触发条件的 pending}——**不存在无理由的 pending**；
4. 按章材料输入包存在；
5. 论文材料路由文件存在。

满足以上五条，作者排期 §9 第 1 项即可判定完成，书稿与 HDR 的统一优化解锁。

---

## 5. 防误用

### 5.1 本方案不做什么

- 不改 canonical、公理、方程、符号表、claim level；
- 不清空 B 队列，不批量升格 EC 卡（`accepted = 0` 是正确状态，不是欠账）；
- 不启动书稿正文重写（第 3 档只产索引）；
- 不改动任何已投稿论文；
- 不让休眠域因材料到来自动升级；
- 不把 `d/q/o` 写进任何地方。

### 5.2 需要上报的阻塞（非本方案可解）

1. `RQ-2026-08-A02`（`d/q/o` 形式地位）——挡住全部直觉支线；
2. `RQ-2026-08-A04`（Physics 三 patch 落点）——挡住 3 个靶点；
3. 新增：Neuroscience 合成文件是否创建——挡住 NEURAL18/21/22 的最终落点；
4. 新增：5 个 pending 靶点落在 Core / canonical（`_SRT_T_DIR_CANONICAL` ×2、`Core_14`、`Core_25`、`Occlusion_Dynamics`），需 `SRT_EDIT_PROTOCOL` 单独授权，**不随材料收口一并授权**。

### 5.3 语义纪律

- 「材料已融入」= 目标文件里有可脱离材料独立阅读的原生段落，**不等于** SourceCard 已写、patch 已建或 hook 已挂；
- 「台账补行」**不等于**重新裁决——第 0 档补的是既成事实的记录，不改 A/B/C；
- 「收口完成」**不等于**所有材料都进了正文——B 卡永久停驻是合规终局。

---

## 6. 需要作者拍板的四项（本方案的唯一提问）

1. **Physics 落点**：新建 `SRT_Physics_Bridge_v0_2.md` / 并入现有 `_SRT_Phys_Bridge.md`（建议后者）/ 继续停驻？
2. **Neuroscience 落点**：创建 `N1_N13_v0_2` 合成文件 / 改指 compact core（建议后者）/ 继续停驻？
3. **7 张无 hook 的 patch**：全补 hook / 只补 NEURAL18+AIREASON01+AIEVID01，其余判"有意无 hook"（建议后者）/ 全部降级停驻？
4. **第 3 档按章输入包**：现在建（材料收口的一部分）/ 推迟到书稿统一优化启动时再建？

拍板后，第 0 档即可开工；第 0 档与第 4 档不依赖上述任何一项，可并行。
