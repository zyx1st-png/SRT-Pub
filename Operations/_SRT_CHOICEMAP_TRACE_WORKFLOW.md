---
id: SRT-CHOICEMAP-TRACE-WORKFLOW
type: workflow
tags: [ChoiceMap, ChoiceTrace, IntuitionMining, RetroWriteback, Breakout, Convergence, Operations]
status: active_v1
layer: meta
epistemic_layer: os
claim_mode: workflow
canonical: false
ai_do_not_use_for_definition: true
created: 2026-07-09
provenance: 2026-07-09 第一直觉 choice-trace 回写实践复盘。该对话本体是普通 LLM 对话（未走任何管线），仅在结束后用选择地图格式回写成 trace。本文件把这一被验证的用法正式化，并修补该实践暴露的四类缺口。
dependency: [SRT-DIRECTION3-CHOICEMAP-PROTOTYPE-SEED, SRT-CHOICE-TRACE-LOG, SRT-ARTICLE-WORKFLOW]
---

# ChoiceMap 轨迹工作流：模式区分、回写协议与收尾管线

> **性质与边界（先读）**
> 1. 本文件是运行层工作流，**非 canonical，不定义术语**。trace 产出的任何命题都不因走完本流程而获得定义权威。
> 2. 本文件不替代 `_SRT_DIRECTION3_CHOICEMAP_PROTOTYPE_SEED.md`（产品原型规格）与 `Operations/_SRT_CHOICE_TRACE_LOG.md`（文章工作流台账）；它负责三者之间的模式区分，并补齐直觉挖掘与回写记录的协议。
> 3. 第一个真实样本：`01_Source_Intuition/SRT_FIRST_INTUITION_SELECTION_BEFORE_EXISTENCE_CHOICE_TRACE_2026-07-09.md`（回写模式）。

---

## 0. 为什么有这个文件

2026-07-09 的第一直觉 trace 证明了一件事：**ChoiceMap 最自然的真实用法不是全程走管线，而是"自由对话 → 事后用选择地图回写"。**

对话发生时没有任何工作流在场——它就是一次正常的 LLM 引导式对话；选择地图只在结束后作为**回写记录格式**登场。这个模式（下称**回写模式 / retro-writeback**）效果好、摩擦低，但它之前在规格里只是台账的一个边缘字段（`late_entry`），没有自己的协议。结果是：回写出的 trace 数据质量依赖临场判断——那一次做对了大部分（选项全集、未选项、下一话题来源都留了），但也漏了记录模式声明、越界选择的显式分类、委托收敛的隔离和收尾检查。

本文件做四件事：

1. 把**回写模式**正式化为一等记录模式；
2. 把**越界选择（breakout）**升格为一等事件；
3. 定义**委托收敛协议**，防止 assistant 的判断被静默升格为作者直觉；
4. 定义 trace 的**收尾管线**（canonical 碰撞检查 → 术语撞车检查 → 路由 → 落库）。

---

## 1. 模式矩阵：三种用途 × 两种记录方式

ChoiceMap 相关的实践现在有三种用途，各自的发散/收敛边界不同，**不可混用规格**：

| 用途 | 规格文件 | LLM 可以收敛什么 | LLM 绝不收敛什么 |
|---|---|---|---|
| **决策支持**（产品） | `_SRT_DIRECTION3_CHOICEMAP_PROTOTYPE_SEED.md` | 什么都不收敛（第一设计律） | 排序、推荐、结论 |
| **文章工作流** | `Operations/_SRT_ARTICLE_WORKFLOW.md` + `_SRT_CHOICE_TRACE_LOG.md` | 无（只发散；收敛全归作者） | 选题、论点、成文 |
| **直觉挖掘** | 本文件 | **"下一个问题问什么"**（追问收敛是本模式的合法引擎） | **"答案是什么"**（作者的直觉判断） |

直觉挖掘模式的关键区分：assistant 每轮选择"下一个更尖锐的问题"是一种收敛动作，在本模式中**合法且必要**——但它必须被审计：每轮记录**「assistant 下一话题选择来源」**（为什么是这个问题、由作者上一轮的哪个选择触发）。2026-07-09 trace 已经这样做了；本文件把它升格为直觉挖掘 trace 的**必填字段**。

记录方式有两种，trace 文件 frontmatter 必须声明其一（`trace_mode` 字段）：

| 记录方式 | `trace_mode` | 含义 | 数据质量含义 |
|---|---|---|---|
| **现场模式** | `live` | 对话按管线推进，逐轮当场记录 | `reason` 是当时的收敛，权重最高 |
| **回写模式** | `retro_writeback` | 对话是自由 LLM 对话，结束后（或事后）整理成 trace | 全部字段是**重构**；须按 §2 协议执行，回看时对 `reason` 类字段降权 |

> 不声明 `trace_mode` 的 trace，回看时一律按 `retro_writeback` 的最低信任等级处理。

---

## 2. 回写模式协议（R1–R6）

回写一次自由对话时，按以下顺序执行。目标：**让重构的边界诚实可见**，而不是让回写件伪装成现场记录。

### R1 · 声明记录模式

frontmatter 写入 `trace_mode: retro_writeback` 与 `late_entry: true`；provenance 一句话说明对话本体形态（"普通 LLM 对话，事后回写"）。

### R2 · 从原始对话逐字回收，不从记忆重写

- 选项全集、作者原话（选择、越界内容、理由短句）**必须从对话原文逐字回收**；找不到原文的轮次，标 `reconstructed: true`。
- assistant 的"下一话题选择来源"允许事后补写（它本来就是对 assistant 行为的解读），但要写成解读而非引文。

### R3 · 逐轮分类选择事件

每轮的作者动作归入且仅归入一类：

| 事件类型 | 判据 | 记录要求 |
|---|---|---|
| `chosen` | 在选项集内选择（含多选） | 选了什么 + 未选项 |
| `breakout` | 越界选择（见 §3） | 按 §3 三要素记录 |
| `delegated` | 作者把收敛交回 assistant | 按 §4 协议处理 |
| `topic_shift` | 作者改换主题而非回答 | 记新主题 + 旧问题是否悬空 |

### R4 · 隔离委托轮次

所有 `delegated` 轮次的产出物按 §4 标记，**不得进入命题簇**，除非已有作者二次确认。

### R5 · 提取命题簇并标注确认状态

每条源头命题挂 `confirmation_status`（见 §4 表）。

### R6 · 执行收尾管线（§5）后才算回写完成

没有走完 §5 的回写件是半成品，不得作为"已留痕"引用。

---

## 3. 越界选择（breakout）：一等事件

2026-07-09 trace 中信息量最大的时刻全部是越界选择（作者给出选项外概念、作者上移一层、作者用自己的句子替代选项）。越界是 revealed-stake 最浓的样本——**选项集装不下作者的时刻，比作者在选项集内的任何选择都更能刻画收敛函数**。

每个 `breakout` 事件必须记录三要素：

1. **越界内容**（作者原话，逐字）；
2. **失配类型**——原选项集为什么装不下它：
   - `dimension_miss`：选项在错误的维度上展开（例：问方向性来源给了 A–E 局部来源，作者给出更底层原则）；
   - `level_miss`：选项在错误的层级上展开（例：问具体判准，作者上移到"这不是本理论关注的问题层"）；
   - `format_miss`：平面选项集应为层级结构（例：作者答"E 是基础，A–D 是它的显化"）；
3. **越界后处理**——assistant 是否在越界后立即做了**防误读追问**（对作者的新概念追问其边界，防止它被按最近的已有概念误读）。现场模式中这是 assistant 的强制动作；回写模式中如实记录做没做。

> 回看时，`breakout` 事件单独成列。积累若干条后，失配类型的分布本身就是对"assistant/LLM 选项生成器在哪个方向上系统性装不下作者"的画像。

---

## 4. 委托收敛协议与确认状态

**问题**：作者说"你帮我分析一下"或"认同你的判断"时，assistant 的判断有被静默升格为作者直觉的风险；且 LLM 的收敛是众数收敛，恰好容易落在仓库已有结论上，形成"看似被作者确认的回声"。

**协议**：作者显式委托收敛时，assistant 只有两种合法动作：

1. **重组交还**：不给结论，把分析重组为供作者选择的结构（产品规格 S5 的兜底规则）；
2. **标记提案**：给出分析，但产出物强制携带 `assistant_proposal` 状态，等待作者二次确认。

命题簇每条命题必须挂 `confirmation_status`：

| 状态 | 含义 | 能否被下游引用为作者直觉 |
|---|---|---|
| `author_breakout` | 来自作者越界选择 | 能（最高等级） |
| `author_chosen` | 来自作者在选项集内的明确选择 | 能 |
| `assistant_proposal_confirmed` | assistant 提案 + 作者事后逐条二次确认 | 能，但标注来源 |
| `assistant_proposal_pending` | assistant 提案，未获二次确认 | **不能**；引用时必须带 pending 标记 |

> 特别警惕："作者认同 assistant 判断"不等于二次确认。一句"认同"覆盖的是当轮语境，不构成对提炼后命题措辞的确认。二次确认必须针对**成文后的命题原文**逐条进行。

---

## 5. 收尾管线（每份 trace 成文时必做）

### 5.1 Canonical 碰撞检查

对命题簇逐条标注三态（对照 `CANONICAL_REGISTRY.md`、相关 canonical 锚点与 `Core/SRT_OPEN_TENSIONS.md`）：

- **已覆盖**：canonical 已有承接（注明锚点）。此类命题的价值是**直觉复认**，不是新增；
- **新候选**：仓库无落点。此类命题是 trace 的真实增量，进入路由（§5.3）；
- **冲突/触雷**：与 canonical 定义相抵，或触及 OPEN_TENSIONS 未解决点。此类命题引用时必须挂对应张力编号，不得表述为已解决。

### 5.2 术语撞车检查

trace 中每个**新造或再定义的词**，grep 一遍 `_SRT_SYMBOL_TABLE.md`、`SRT_Glossary.md` 与书稿术语指南（`01_Source_Intuition/BOOK/BOOK_TERMINOLOGY_SIMPLIFICATION_GUIDE_*.md`）。撞车时当场二选一：改名，或在 trace 内显式分义（"本 trace 的 X 不是 QNN 章的 X"）。

### 5.3 下游路由

每条**新候选**命题标注建议去向（可多选）：

- `OPEN_TENSIONS 登记`（触及未解决核心张力的）；
- `bridge 硬化候选`（可形式化、需跨域对照的）；
- `书稿轻补丁 notes`（走 `BOOK_*_REVISION_NOTES` 形式，**不直接动冻结正文**）；
- `ChoiceMap 产品指标`（可转产品线的）；
- `搁置`（暂无去向，注明原因）。

路由是建议，不是执行；执行各走各的既有协议（编辑协议、冻结协议、书稿治理）。

### 5.4 落库 checklist（缺一条即未完成）

- [ ] trace 文件 frontmatter 完整（`trace_mode`、`late_entry`、provenance、dependency）；
- [ ] 在 `Operations/_SRT_CHOICE_TRACE_LOG.md` §4 登记（非文章类 trace 用指针条目，`trace_type` 注明）；
- [ ] 在所属目录索引登记（源头直觉类 → `01_Source_Intuition/INDEX.md`）；
- [ ] `STATUS.md` 最近关键推进留痕一条（或 memory 层，若当日 memory 活跃）。

> 不落库等于这条轨迹没发生——台账的存在理由是"轨迹可积累、可回看、可作条件"，孤儿 trace 三者皆无。

---

## 6. 现场模式的提问形制（直觉挖掘）

现场跑直觉挖掘时，assistant 的选项设计遵守：

1. **互斥优先**：选项应是真分岔（强迫取舍），不是同一命题的不同侧面。作者一轮选四五项说明选项集失败——那一轮的判别信息约等于零；
2. **层级归置题**是本体论问题的首选题型：不问"A–E 选哪个"，问"哪个是基础，哪些是它的显化"（2026-07-09 trace CT-12 的作者自发答法，效果好于平面单选）；
3. **反众数扰动**沿用产品规格 S1：每轮至少一个低频/跨域选项，与显然选项并列——它的作用是测出作者的越界是被激发的还是纯内生的；
4. **越界后必须防误读追问**（§3 第三要素）；
5. 每轮记录**「下一话题选择来源」**。

回写模式对既成对话无法补做 1–4，只能如实记录；这正是回写件降权的原因之一。

---

## 7. 本文件不是什么（防误用）

- 不是 canonical，不定义任何 SRT 术语；
- 不把"走完本流程"当作命题被验证——收尾管线只判定命题的**登记位置**，不判定真伪；
- 不替代文章工作流：文章类 trace 仍按 `_SRT_CHOICE_TRACE_LOG.md` 的字段与纪律执行，本文件只补 `trace_type` / 回写 / 越界 / 委托四块公共协议；
- 不主张回写模式与现场模式数据等价——回写是重构，永远降权，这是诚实成本，不是缺陷。
