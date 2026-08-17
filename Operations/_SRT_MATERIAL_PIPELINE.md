---
id: SRT-MATERIAL-PIPELINE
type: framework
tags: [Material, Pipeline1, Intake, Writeback, Registry, SourceCard, PatchNote]
status: active_v2
layer: meta
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-OPERATIONS-README, SRT-MATERIAL-LOG, SRT-MATERIAL-ADJUDICATION-WORKFLOW, SRT-GOV-SYN01-ONTOLOGICAL-SYNTHESIS-DISCRIMINATION]
---

# SRT 材料融合流水线（Pipeline 1 / v2 结构化写入版）

> **定位**：Pipeline 1 是外部材料进入 SRT 仓库的权威主流程。  
> **核心原则**：不另起平行流程；`SourceCard / PatchNote / Registry / IntegrationHook` 都是 Pipeline 1 的结构化产物。  
> **贡献纪律**：材料价值按 `GOV-SYN01` 分成 **O-track 本体论整合** 与 **D-track 经验/判别增量**。没有独有经验增量不自动等于低价值；已有成熟理论建立的内容可以作为 SRT 本体论构造材料，但来源证据不能被偷换成“证明 SRT”。  
> **正式状态台账**：所有通过 Pipeline 1 处理的材料，最终状态仍以 `Operations/_SRT_MATERIAL_LOG.md` 为准。

---

## 0. 一句话原则

```text
材料先归档，证据先裁决，贡献分双轨，补丁再解释，正文最后合并。
```

Pipeline 1 不负责把所有新材料立刻升格为 SRT 结论，也不负责为每条材料制造 SRT 独有增量。它负责判断材料是否进入仓库、以什么等级进入、它对 SRT 的价值属于本体论整合还是经验判别、落在哪里、如何被人和机器检索、以及未来是否合并进正文。

必须保持：

```text
source evidence supports source claim
source claim may instantiate / constrain SRT structure
instantiation != proof of SRT ontology
```

---

## 1. 触发方式

### 1.1 标准触发词

```text
材料 <URL / DOI / PDF / 文本 / 摘要 / 截图>
```

触发后执行 Pipeline 1。

### 1.2 辅助裁决触发词

```text
材料裁决 <URL / DOI / PDF / 文本 / 摘要 / 截图>
二轮裁决 <URL / DOI / PDF / 文本 / 摘要 / 截图>
```

触发后执行 `Operations/_SRT_MATERIAL_ADJUDICATION_WORKFLOW.md`，其结果必须回注 Pipeline 1；辅助裁决不替代 Pipeline 1。

### 1.3 陪读转写入

`陪读` 本身是 source-grounded reading，不自动触发仓库写入。若用户在陪读过程中随后要求：

```text
写入
回写
融合
并入仓库
```

则从当前 source-reading 上下文转入 Pipeline 1，并按 `GOV-SYN01` 明确分开：

1. source-derived 内容；
2. SRT ontological synthesis；
3. SRT discriminating claim（如无则明确 none / not claimed）。

---

## 2. 输入类型与读取要求

| 输入类型 | 读取要求 | 风险说明 |
|---|---|---|
| URL | 优先读取原文；若是媒体报道，尽量追踪一手论文/DOI | 媒体解释不得直接当成作者结论 |
| DOI / 论文链接 | 优先读取 abstract、methods、conclusion；必要时读取 PDF | 若无法访问全文，保留证据缺口 |
| PDF | 直接读取正文、图表、参考文献和结论 | 不只读摘要 |
| 用户摘要 | 标记为二手输入；如可检索，应核验一手来源 | 不把用户整理当成原文 |
| 截图 | 只作为线索；需补充可引用来源 | 截图证据等级低 |

---

## 3. 六项审核门

每条材料必须通过以下 6 项审核后，才可给出 A/B/C：

| 审核门 | 问题 | 通过标准 |
|---|---|---|
| 1. 相关性 | 是否实质关联 SRT 核心命题？ | 能稳定映射到 L0/L1/L2、Ĝθ、Ψ_f、d-value、硬化、选择、主体性、实验等至少一项 |
| 2. 贡献性 | 是否提供非空理论贡献，而不只重复或换词？ | 至少有稳定 O-track synthesis / correction / constraint，或 D-track prediction / intervention / counterfactual increment，或明确的 guardrail / residual pressure |
| 3. 证据等级 | 证据是 primary / peer-reviewed / preprint / review / secondary / commentary？ | 必须标注，不得混淆 |
| 4. 可对齐性 | 能否转化为 SRT 最小命题或稳定结构位置？ | 至少能压出 1 条 surviving claim / synthesis relation，或明确只作类比 |
| 5. 风险 | 是否存在过拟合、HARKing、偷换、伪背书？ | 必须明确边界声明，尤其防止 `source instantiates SRT -> source proves SRT` |
| 6. 落点清晰 | 应进入哪个文件层？ | 能给出主落点、备选落点、不应落点 |

### 3.1 双轨贡献判定（强制）

每条高价值材料必须在 prose 中标注贡献路线：

```text
O-track        — ontological synthesis
D-track        — discriminating / empirical increment
O + D          — both
source-only    — source evidence / pressure only
```

这些标签是治理阅读标签，**不是新 claim-ladder 级别，也不是新的 frontmatter / registry enum**。

#### O-track 先问

```text
这个外部理论/结果是否能忠实放入 SRT 的共同结构？
是否澄清 layer / bearer / boundary / history / stability / selection relation？
是否把多个原本分散的成熟机制放进一个更少但更清楚的关系语法？
是否反过来约束或修正 SRT？
```

#### D-track 只在实际声称时问

```text
SRT 是否额外预测、区分、干预或解释了 bounded rival 不要求的东西？
```

若答案为 `no`，不要为了 A 类资格强造新变量、机制、scalar、operator 或预测。

### 3.2 三层来源纪律

高价值材料的分析和写入必须能拆成：

```text
Layer A — source-derived
Layer B — SRT ontological synthesis
Layer C — SRT discriminating claim (if any)
```

Layer B 可以很强而 Layer C 为空。

---

## 4. A/B/C 裁决

| 结论 | 含义 | 允许动作 |
|---|---|---|
| A | 可直接融入 | 创建 SourceCard、PatchNote、Material Log、索引、Registry、IntegrationHook；必要时轻量回写正文 |
| B | 延后观察 | 创建 SourceCard + Material Log；可创建 Watchlist 条目；一般不创建 PatchNote 或正文 hook |
| C | 不融入 | 只写 Material Log 的 C 记录，说明拒绝理由；不创建正文补丁 |

### A 的门槛

只有同时满足以下条件时，才建议 A：

1. 材料有稳定贡献，且至少满足以下一条：
   - **O-track**：形成非平凡的本体论整合、跨域结构压缩、层级澄清、SRT 反向约束或共同结构定位；
   - **D-track**：形成真实的预测 / 干预 / 反事实 / 机制判别增量；
   - 两者同时存在；
2. 证据等级足以承受拟写入层级；
3. 主落点明确；
4. 能写出去材料化主句；
5. source / synthesis / discrimination 三层可区分；
6. 风险声明没有打穿正文动作。

特别规则：

```text
“已有理论已经解释这个局部机制”
!= 自动 B / C
```

还必须继续问：该已建立机制是否为 SRT 的本体论整合提供稳定结构材料。

### B 的门槛

出现以下任一情况，优先 B：

1. O-track synthesis 有潜力但 source fidelity / mapping 尚未闭合；
2. D-track increment 疑似存在但证据不足或 bounded rival 未冻结；
3. 一手来源未充分核验；
4. 文件落点仍摇摆；
5. 更像待验证窗口，而不是可写正文窗口。

### B 类内部细分（自 2026-05-23 起优先标注）

为避免 `B` 被误用成安全垃圾桶，B 类材料在备注或观察列表中应尽量补一个子类：

| 子类 | 含义 | 默认动作 |
|---|---|---|
| `B1` | 可转 A 候选：高相关，已有一手锚点或明确技术路线，但需要 close-read / DOI 拆分 / 结果补齐 / 二轮裁决 | 保留高优先重评；必要时启动 `材料裁决`；可预留候选落点，但不正文回写 |
| `B2` | guardrail-only：主要用于边界、降级、防误读、claim-ladder hygiene；理论启发存在，但正文承重弱 | 只留 SourceCard + Material Log；未来仅在 public / governance / claim-status 需要时引用 |
| `B3` | public-prose-only / expression-only：主要是表达素材、公共类比、传播语感；不应进入理论主链 | 只作公共写作素材或拒绝正文使用；不得作为证据或 bridge 支撑 |

子类不是新的 A/B/C 裁决，只是 B 类内部的操作优先级。若材料同时包含多个层次，应写成 `B1 for X; B2 for Y`，避免把局部可用接口升格为整包可融入。

### B 类语义修订：停驻 + 具名触发条件（自 2026-07-20 起）

治理减负轮起，B 类默认语义从"延后观察、排队等待第二轮审计"改为 **"停驻 + 具名复活触发条件"**。原因：现实是采集速度大于消化速度，"等一次专门二审"的出口对绝大多数 B 卡永远不会到来，等于把分析深度投进一个只沉不浮的填埋场。

新规则：

1. 每张 B 卡在 Material Log 备注里**必须写一条复活触发条件**，绑定工作线事件（如"Q19 章推进碰到该主题时"、"下次 ε_pg 相关 canonical 工作时"），不绑日历。无触发条件的 B 卡不合规。
2. **Material Log 是 B 卡复活触发条件的唯一权威源**。根目录 `_SRT_PARKED_INDEX.md §2` 只保留指向 Material Log 的入口指针与默认策略，不逐卡登记、不要求同步——避免形成第二份需要维护的台账（治理原则③的台账版：一类停驻内容只有一个权威账本）。
3. **SourceCard 深度匹配命运**：默认判 B 的材料按**档案卡**写（来源事实 + 一句边界 + 触发条件即可），不按接口分析写。只有子类判 `B1`（明确可转 A、已有一手锚点）才值得写完整接口分析——因为只有它大概率会被捞起。避免给"大概率永不二审"的卡配"随时要融入"的分析深度。
4. 无人点名的 B 卡作为档案永久停驻，不产生维护义务；这是正常终局，不是欠账。

### C 的门槛

出现以下任一情况，优先 C：

1. 与已有条目高度重复，且不增加 synthesis / correction / constraint / discrimination；
2. 只有漂亮类比或词汇相似，无稳定新结构；
3. 证据等级与正文负担严重不匹配；
4. 需要过度改写来源或 SRT 才能吸收；
5. 既没有 O-track 组织价值，也没有 D-track 增量，也不构成 guardrail / residual pressure。

---

## 5. v2 结构化产物层

Pipeline 1 的 v2 产物分为 6 类：

```text
SourceCard -> PatchNote -> Material Log -> Markdown Index -> JSONL Registry -> IntegrationHook
```

### 5.1 SourceCard：材料事实层

用途：记录材料本身说了什么，尽量不混入 SRT 解释。

建议目录：

```text
Materials/YYYY/SRC_YYYY_MM_DD_<Domain>_<ShortTopic>.md
```

最小字段：

```yaml
source_id:
title:
source_type:
domain:
url:
doi:
authors:
publication:
date_published:
date_added:
evidence_level:
reliability_level:
srt_relevance:
integration_priority:
related_srt_claims:
tags:
```

必写小节：

1. One-line summary
2. Core claims of source
3. Evidence / method
4. Limits
5. SRT relevance
6. Suggested patch target

**证据锚点规则（SourceCard owner）**：当材料是可全文核验的一手 / 学术全文，且 `integration_priority` 为 `high` / `very_high`，或其承重主张将支撑 P3 及以上 bridge / hardening 时，SourceCard 的承重 source-level claim 必须保留可回查定位。优先使用来源原生的 page / section / theorem / figure / table 等 anchor；“已完整阅读 / full close-read”不能替代文本定位。PatchNote 默认引用 SourceCard 相应节位，不要求重复维护全部页码；只有 Patch 本身直接承担新的源事实时才重复锚点。若来源没有稳定页码，应记录可用的 section / heading / paragraph / figure，或明确说明定位限制。

**双轨边界**：SourceCard 的正文事实仍属于 source-derived layer。即使它在 O-track 中非常重要，也不得把 SRT synthesis 写成来源作者的结论。建议在 `SRT relevance` 中明确分开 `source-backed pressure` 与 `SRT-side synthesis`。

### 5.2 PatchNote：SRT 桥接解释层

用途：记录 SRT 如何吸收、降级、约束或反向解释该材料。

建议目录：

```text
<Domain>/patches/SRT_<Domain>_<ClaimID>_<ShortTopic>_v0_1.md
```

若当前仓库尚未迁移到 `patches/` 子目录，可暂时沿用领域目录根层，但必须写入领域索引。

最小字段：

```yaml
patch_id:
source_ids:
domain:
claim_level: canonical | bridge | analogy | watchlist
canonical_status: canonical | non_canonical
status: patch | integrated | deferred | rejected
target_future_doc:
related_claims:
tags:
```

必写小节：

1. Source anchor
2. Why this matters for SRT
3. Contribution route: O / D / O+D / source-only
4. Main SRT bridge / synthesis claim
5. Mapping table
6. Formal bridge（若需要；O-track 不要求为了形式感新增方程）
7. New discriminating claim cluster（若有；无则明确 none / not claimed）
8. Experimental / operational consequences（D-track 承重时必写）
9. Boundary cautions
10. Integration hook
11. One-paragraph abstract

PatchNote 必须明确：

```text
external theories may supply the local mechanisms / evidence
SRT may supply a candidate ontological organization of their relations
```

不得在没有 D-track comparison 时写成 “SRT explains what the source cannot explain”。

### 5.3 Material Log：正式状态层

所有材料都必须进入：

```text
Operations/_SRT_MATERIAL_LOG.md
```

Material Log 是正式状态台账，优先级高于 patch、index、hook。

备注字段仍采用五问结构：

```text
新增接口：...；反向修正：...；加固内容：...；SRT反哺：...；残余压力：...
```

高价值新记录还应在备注中自然语言写明：

```text
贡献轨道：O / D / O+D / source-only
```

不新增 machine enum。

### 5.4 Markdown Index：人类导航层

至少更新一个领域索引，必要时更新根索引：

```text
_SRT_Recent_Material_Patches_Index.md
Neuroscience/_SRT_Neuroscience_Hardening_Index.md
Physics/_SRT_Physics_Hardening_Index.md
Philosophy/_SRT_Philosophy_Hardening_Index.md
AI/_SRT_AI_Hardening_Index.md
```

若目标领域没有索引，可创建新的领域索引。

### 5.5 JSONL Registry：机器索引层

建议目录：

```text
Registries/material_registry.jsonl
Registries/patch_registry.jsonl
Registries/claim_registry.jsonl
```

若 registry 尚未建立，A 类材料可先写 Markdown index，并在后续 registry migration 中批量补齐。

最小 registry 记录：

```json
{"source_id":"...","patch_id":"...","domain":"...","file":"...","claim_level":"bridge","canonical_status":"non_canonical","integration_priority":"high","related_claims":["..."],"status":"processed"}
```

`O / D` 默认留在 Markdown prose，不为本纪律新增一次性 registry 字段值。

### 5.6 IntegrationHook：正文回写层

用途：记录未来综合正文如何吸收该补丁，避免把 patch 原文硬粘进主文。

建议目录：

```text
<Domain>/hooks/<ClaimID>_<ShortTopic>_Integration_Hook.md
```

若当前仓库尚未迁移到 `hooks/` 子目录，可暂时沿用领域目录根层，但必须写明 target parent。

必写内容：

1. Target document
2. Insert after
3. Suggested paragraph
4. Suggested table
5. Do not include
6. Future synthesis target

### 5.6.1 落地账（landing ledger）——自 2026-07-25 起强制

> **本节是 hook 落地状态的权威契约**，由 `scripts/check_hooks.py` 在 `governance_preflight` 中机器强制（因而进 CI）。脚本负责执行，本节负责定义；两者必须同步——**只在脚本里存在、本节没写的规则属于隐藏契约，正是本机制要消除的失效模式**。

背景：2026-07-25 闭环审计发现，管线前五段都有台账，唯独 hook → 正文这一段无法回答"这张 hook 到底落地没有"。当时 18 张 hook 里，1 张已落地却标 pending，4 张状态写法不可判读，3 张指向从未创建的文档。根因是 `status` 一个字段同时承担了两件不同的事。

**字段职责必须分开：**

| 字段 | 回答什么 | 取值 |
|---|---|---|
| `status` | 这个**文件**是否在用 | frontmatter ratchet enum：`draft` / `active` / `frozen` / `archived` |
| `integration_status` | 这张 **hook** 是否落到正文 | `landed` / `partial` / `pending` / `withdrawn` |

**完整 frontmatter 示例：**

```yaml
---
id: HOOK-<DOMAIN>-<CLAIMID>-<SHORT-TOPIC>
patch_id: PATCH-<DOMAIN>-<CLAIMID>-<SHORT-TOPIC>
type: integration_hook
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
domain: <domain_topic>
status: active
integration_status: partial
landing_ledger:
  - target: "Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md"
    state: landed
    anchor: "## 3. Triggering causes and structuring biases"
  - target: "_SRT_T_DIR_CANONICAL.md"
    state: pending
    blocked_by: "canonical freeze：改 `T_dir` 主定义属 C 类高风险编辑，需作者授权"
  - target: "Physics/SRT_Physics_Bridge_v0_2.md"
    state: pending
    target_status: planned
    blocked_by: "计划中的综合文，从未创建；落点属作者裁决"
  - target: "future subjective-time bridge document"
    state: withdrawn
    withdrawn_reason: "从未是真实文件路径；不再作为待办追踪"
closure_audit: Operations/Audits/Hook_Closure_Audit_2026-07-25.md
---
```

**聚合规则**（`integration_status` 必须与 ledger 自洽，否则 CI 失败）：

| ledger 情况 | `integration_status` |
|---|---|
| 非 withdrawn 条目全部 `landed` | `landed` |
| 非 withdrawn 条目无一 `landed` | `pending` |
| 非 withdrawn 条目部分 `landed` | `partial` |
| 全部条目 `withdrawn` | `withdrawn` |

`withdrawn` 条目不参与聚合——它是被移出待办的历史记录，不应把一张已全部落地的 hook 拖成 `partial`。

**target 规则：**

- 必须是**仓库相对路径**的 Markdown 文件；禁止绝对路径、禁止 `..` 越界；
- 必须存在。只有两个逃逸口，且**都要求把"不存在"这件事写出来**：
  - `state: withdrawn` + `withdrawn_reason`——该落点已被移出待办；
  - `state: pending` + `target_status: planned` + `blocked_by`——目标是**计划中但从未创建**的文档（例如一份尚未动工的领域综合文）。这不是笔误的挡箭牌：只有当多份 patch / SourceCard / 索引一致把它当作 `target_future_doc` 引用时才成立，且必须写明落点二选一由谁裁决。
- `target_status: planned` 的目标一旦真的创建，CI 会报错，强制把该条目改为 landed 或 pending。

**anchor 规则（`landed` 专用）：**

- 必须是在 target 文件中**恰好出现一次**的字面串；
- 应优先取**稳定且可诊断**的东西：完整章节标题（`## 3. Triggering causes...`）、claim ID（`T-Cog-6`、`P3-B12`、`### §4.8a ...`）、或指向该 hook 文件本身的 source-trail 链接（`PH_AG04_..._Integration_Hook.md`）；
- **不得**使用普通关键词或通用短语（`many-many`、`authorial`、`CMRO`）。它们会在无关段落误命中，从而让一条陈旧的 `landed` 声明蒙混过关——唯一命中要求正是为堵这个口。

**边界**：`landed` 只断言"该锚串出现在该文件中"。它**不断言**回写质量、去材料化程度或 claim-level 正确性——那属于内容评审，不属于闭环检查。

---

## 6. 正文回写规则

### 6.1 默认不直接改 canonical 正文

A 类材料也不自动进入核心正文。默认动作是：

```text
SourceCard + PatchNote + Log + Index + Registry + Hook
```

只有当材料已通过 A 且目标正文明确时，才允许轻量回写。

### 6.2 去材料化主句

任何正文回写必须有一句可脱离材料阅读的原生主句。

错误写法：

```text
这篇 Nature 文章说明了 SRT 是对的。
```

正确写法：

```text
L2 不应只被理解为突触或记忆结构，它还包括支持未来选择可达性的非神经元拓扑。
```

### 6.3 Patch 不等于正文

PatchNote 是分析层，正文是理论层。未来综合正文应压缩 patch，而不是粘贴 patch。

建议压缩比例：

```text
一个 patch -> 2-4 段 + 1 张映射表 + 1 条边界声明
```

### 6.4 O-track 正文纪律

当材料主要承担 O-track 时，正文允许把成熟外部机制纳入 SRT 的共同本体论结构，但必须写成：

```text
外部理论/实验提供局部机制与证据；
SRT 提供这些机制之间的候选本体论组织。
```

不能写成：

```text
因为这些外部机制存在，所以 SRT 被证明；
因为 SRT 可以重述这些机制，所以它优于原理论。
```

O-track 正文可以有高理论价值，即使 D-track 明确为 `none / not claimed`。

---

## 7. 与第二轮裁决的关系

`Operations/_SRT_MATERIAL_ADJUDICATION_WORKFLOW.md` 只在高风险或不确定材料上启动。

启动条件：

1. 材料很像 SRT，但可能只是漂亮类比；
2. 材料跨域，主落点不清楚；
3. 证据等级不稳；
4. 第一轮候选接口过多；
5. 是否 A/B/C 不确定；
6. “已有理论已解释”正在被当成自动否决理由，但 O-track 尚未审计；
7. O-track 与 D-track 被混写，可能把 synthesis 冒充 empirical support。

第二轮裁决完成后，回注 Pipeline 1，只保留：

```text
A/B/C
贡献轨道：O / D / O+D / source-only
surviving claims
主落点 / 备选 / 不应落点
五问终裁
写作动作
去材料化主句
三层边界：source / synthesis / discrimination
风险声明
```

---

## 8. 机器与人类索引规范

### 8.1 文件命名

推荐格式：

```text
SRC_YYYY_MM_DD_<Domain>_<ShortTopic>.md
SRT_<Domain>_<ClaimID>_<ShortTopic>_v0_1.md
<ClaimID>_<ShortTopic>_Integration_Hook.md
```

示例：

```text
SRC_2026_04_24_Neuro_BTSP_Quanta.md
SRT_Neuro_N10_BTSP_Hardening_v0_1.md
N10_BTSP_Integration_Hook.md
```

### 8.2 使用强度标签

必须给每个 patch 标注：

| 标签 | 含义 |
|---|---|
| canonical | 已成为 SRT 正式定义或核心表达 |
| bridge | 高价值桥接材料，可进入正文 |
| analogy | 类比材料，只能辅助说明 |
| watchlist | 暂存，暂不进入正文 |

O-track bridge 可以是高价值 `bridge`，不因为没有 D-track unique prediction 自动降为 `analogy`。

### 8.3 证据等级标签

建议固定为：

```text
primary / peer_reviewed / preprint / review / secondary / commentary / user_summary / screenshot
```

---

## 9. 输出模板

Pipeline 1 处理材料后，回复用户时至少包含：

```md
## Pipeline 1 裁决
- 结论：A / B / C
- 证据等级：
- 贡献轨道：O / D / O+D / source-only
- 主落点：
- 融入状态：

## 三层边界
- Source-derived：
- SRT ontological synthesis：
- SRT discriminating claim（无则写 none / not claimed）：

## 五问
- 新增接口：
- 反向修正：
- 加固内容：
- SRT反哺：
- 残余压力：

## 写入文件
- SourceCard：
- PatchNote：
- Material Log：
- Index：
- Registry：
- IntegrationHook：

## 边界声明
- ...
```

---

## 10. 当前迁移说明

此前已有一批 recent material patches 直接写入领域目录，并补充了根索引、领域索引和 integration hooks。这些文件视为 Pipeline 1 v2 的早期产物，后续不废弃，但需要逐步补齐：

```text
SourceCard
Material Log 新条目
Registry JSONL
```

当前允许过渡期存在两种目录风格：

```text
<Domain>/SRT_..._v0_1.md
<Domain>/patches/SRT_..._v0_1.md
```

但新材料优先使用 `patches/` 与 `hooks/` 子目录。

旧材料不要求批量回填 O/D 标签；只有在重新陪读、重开 bridge、二轮裁决或正文整合时按 `GOV-SYN01` 重新判定。

---

## 11. 守门原则

```text
Pipeline 1 管“是否进入 SRT”；
SourceCard 管“材料本身说了什么”；
GOV-SYN01 管“它贡献的是本体论整合、经验判别，还是两者都没有”；
PatchNote 管“SRT 如何吸收”；
Registry 管“机器如何索引”；
IntegrationHook 管“未来如何并入正文”；
Material Log 管“正式状态与责任留痕”。
```

任何工具或代理执行 Pipeline 1 时，必须遵守这个分层，不得把外部材料直接升格为 canonical SRT 结论。

最后一条方法纪律：

> **不要为了最大化 SRT 的独特性而发明理论。优先忠实吸收已经建立的知识，检验它们能否共同构成一个更完整、更少混淆的 SRT 本体论框架；只有当 SRT 真正声称额外预测、干预或不可替代解释时，再要求 D-track 增量并承担可失败风险。**