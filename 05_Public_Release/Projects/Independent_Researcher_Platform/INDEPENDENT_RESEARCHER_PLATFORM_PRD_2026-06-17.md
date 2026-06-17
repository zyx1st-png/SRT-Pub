---
id: INDEPENDENT-RESEARCHER-PLATFORM-PRD-2026-06-17
type: product_requirements_document
status: draft_v0_1
canonical: false
scope: public_project_planning
project: Independent Researcher Platform
source_business_plan: INDEPENDENT_RESEARCHER_PLATFORM_BUSINESS_PLAN_2026-06-17.md
created: 2026-06-17
updated: 2026-06-17
language: zh-CN
frontstage_positioning: English-first product, multilingual later
srt_role: hidden_operating_system_not_frontstage_doctrine
claim_mode: product_specification
prd_scope: "V1 core platform (Gate 0 manual validation → alpha → paid). V0 landing and Phase-2 Object Commons are referenced but out of scope."
privacy_note: "Do not use disclosed third-party email lists as marketing lists. Recruit only through opt-in public channels."
---

# Independent Researcher Platform 产品需求文档 v0.1

> 产品口号：**Make theories understandable, criticizable, revisable, and discussable.**
>
> 本 PRD 把商业计划书（下称 **BP**）翻译为可构建、可验证、可追溯的产品需求。BP 回答"为什么做、做给谁、怎么变现"；本 PRD 回答"具体做什么、做成什么样、怎么判断做对了"。
>
> 引用约定：`BP §x` 指商业计划书正文章节，`BP A.x` 指其设计评审附录。需求项编号 `FR-XXX-nn` 可被评审、测试与变更追踪引用。

---

## 0. 文档信息

| 项 | 内容 |
|---|---|
| 关联文档 | [商业计划书 v0.1](INDEPENDENT_RESEARCHER_PLATFORM_BUSINESS_PLAN_2026-06-17.md) |
| 本 PRD 范围 | **V1 核心平台**：Gate 0 手工验证 → alpha（10–20 用户）→ 首批付费功能 |
| 明确不在范围 | V0 落地页与等待名单（纯营销页，另出文案稿）；Phase 2 Object Commons / Choice Commons（BP §3.2，远期）；专家市场、私信、复杂群组、大规模积分经济（BP §8.3） |
| 工作语言 | 文档正文 zh-CN；**所有面向用户的字段名、状态、枚举、UI 文案为英文**（English-first 产品） |
| 状态 | draft_v0_1，待 founding circle 评审 |

### 0.1 本 PRD 与 BP 的唯一关键差异

BP 把产品讲成一条线性流水线（BP §5 工作流）。本 PRD 依据 **BP 附录 A** 做一次重排：

> **整个产品压在一件事上——LLM 对"选择张力层"的挖掘质量（BP A.2）。** 其余所有功能（生成、评审、版本、发布、出版）都是围绕这件事的脚手架。

因此本 PRD 的第一原则、北极星指标、Gate 0 验证、P0 优先级，全部锚定到这一个赌注。一个把"访谈"和"评审"当作并列普通功能的 PRD 会做错这个产品。

---

## 1. 产品概述与目标

### 1.1 一句话定义

一个让独立研究者把私人理论体系，经由 LLM 多轮访谈与社区评审，转化为标准化、可批评、可修订的 **Theory Packet** 的平台。

### 1.2 产品要解决的核心痛点（重排自 BP §2 + A.1）

真正的对立轴不是"被支撑 vs 被批评"，而是 **被理解 vs 被无视（understood vs ignored）**。独立研究者最深的伤口是"你不值得我花时间理解，因此也不配得到批评"。一旦批评建立在真正的理解之上，批评本身就站在"被看见"一侧。

由此得到产品要交付的核心体验，按发生顺序：

1. **被看穿**：作者第一次觉得"对，这就是我一直说不清楚的东西"（张力层）。
2. **被认真对待**：在被理解的基础上，接受诚实的批评（对象层）。
3. **被人类承认**：批评、修订最终通向真实评审者、出版、与学院对话（履约闭环，BP A.6）。

### 1.3 产品目标（V1）

| 编号 | 目标 | 判据 |
|---|---|---|
| G1 | 验证张力挖掘可稳定"打中" | 北极星指标达标（见 §10.1） |
| G2 | 证明"对内温暖 + 对外可信"可共存 | 经手工实验与 alpha 验证（BP A.5 / A.10） |
| G3 | 跑通 Theory Packet 全生命周期 | 至少 10 个 packet 走到 T4 以上，其中 ≥3 个产生实质修订（T5） |
| G4 | 建立首批可公开的高质量样例 | 产出 10–20 个可作 landing 示例的 packet（BP §11.5） |

### 1.4 非目标（V1 明确不追求）

- 不追求规模/MAU（BP §3.1：第一阶段是协议训练场，不是增长场）。
- 不认证理论真伪（BP §13.1：只记录过程）。
- 不做通用 AI 总结器、论文仓库、民科论坛、同行评审替代品（BP §0）。
- 不前台暴露 SRT（BP §1.3：隐藏操作系统）。

---

## 2. 产品设计原则（约束所有功能）

这些原则源自 BP 附录 A，是后续每条功能需求的验收背景。任何功能若违反原则即为缺陷。

| 编号 | 原则 | 出处 | 对功能的硬约束 |
|---|---|---|---|
| **DP1** | 先理解后批评：理解发生在张力层，批评发生在对象层 | A.1 | 访谈与评审必须张力层在前、对象层在后；UI 不得在张力层引入批评 |
| **DP2** | 张力层的"批评"是选择支撑，不制造新张力 | A.1 / A.4 | 张力层产物只给"更多选项与代价"，不给"你哪里错了" |
| **DP3** | 单点赌注：张力挖掘质量决定生死 | A.2 | 访谈引擎与作者确认是 P0 之首；用前沿模型，不为省成本降级 |
| **DP4** | 作者确认是情绪命门，不是流程合规 | A.2 / §5.2 | 确认要捕捉"有没有被看穿"，而非"AI 拆得准不准" |
| **DP5** | 双重边界：对内温暖 / 对外冷读者测试 | A.5 | 张力层对作者温暖；对象层必须能扛住不留情面的外部读者，不得软化"严出" |
| **DP6** | 人类承认是情绪契约的履约证据 | A.6 | 评审者/出版/学院对接不是后期点缀，是 packet 价值闭环 |
| **DP7** | 作者照护边界：翻译内容，不评判作者本人 | A.9 | 系统对内容做张力翻译，对作者本人不做心理判断、不背书、不病理化 |
| **DP8** | 宽进严出 | §6 | 输入几乎不拒；输出按成熟度与风险分层、限形 |
| **DP9** | AI 透明与溯源 | §13.4 | 每个字段、每条命题都带来源标签，且在展示层可见 |
| **DP10** | 反流量化 | §13.3 | 点赞/收藏只作兴趣信号，永不计入成熟度或质量 |

---

## 3. 范围

### 3.1 In Scope（V1）

账户与项目、**访谈引擎（张力挖掘）**、**Theory Packet 生成与作者确认**、世界知识对齐、发布与溯源展示、评审系统（张力层 + 对象层 + AI red-team）、成熟度状态机（T0–T7）、版本历史、导出（Public/Academic Brief）、跨切面治理与安全、成本与模型路由、指标埋点。

### 3.2 Out of Scope（本 PRD 不展开）

| 项 | 原因 | 去向 |
|---|---|---|
| V0 落地页/等待名单文案 | 纯营销，非平台功能 | 单独文案稿（参 BP §8.1） |
| Phase 2 Object Commons | 远期，需先有成熟协议（BP §3.3） | 后续 PRD |
| 专家市场 / 私信 / 复杂群组 / 大规模积分经济 / 自动认证徽章 / 应用市场 | BP §8.3 明确 V1 暂不做 | V2+ |
| 机构私有空间、季刊/年鉴出版系统 | 6–24 月路线（BP §17） | 后续 PRD |

### 3.3 范围边界的产品判断

V1 不是"功能齐全的小社区"，而是"能证明单点赌注成立的最小系统 + 跑通一条 packet 完整生命周期"。社区、积分、推荐流在赌注未验证前都是负债。

---

## 4. 用户与画像

### 4.1 人群结构：双峰分布（BP A.7）

平台会同时吸引两类人，**宽进严出正是为了同时接住两峰**：

- **理想用户峰（V1 主画像）**：谦逊、寻求对话、自我克制的严肃独立研究者；其中"严肃独立研究者 × 学院桥接读者"双重身份者为 founding circle 首选。
- **高风险/民科姿态峰**：宏大、不可证伪、怨气驱动、缺乏自我质疑。不拒绝，但其输出经"严出 + 风险限形"处理为可讨论对象。

### 4.2 主要画像

| 画像 | 描述 | V1 核心诉求 | 对应订阅 |
|---|---|---|---|
| **The Builder（主）** | 认真打磨个人理论的独立/LLM 辅助研究者 | "我的私人体系第一次被看穿、被结构化" | Builder（BP §9.2） |
| **The Researcher** | 需要深度打磨 + 对接学院材料 | 文献对齐、学院简报、私密项目、邀请评审 | Researcher（BP §9.3） |
| **The Reviewer** | 愿做结构化评审的同行（常与前两者重叠） | 用张力层/对象层评审表贡献，获积分与贡献记录 | 任意层 |
| **The Bridge Reader** | 年轻 faculty / postdoc / editor / 开放科学参与者 | 快速判断 packet 是否值得认真对待（冷读者） | 顾问/受邀 |

### 4.3 V1 不优先服务的人（BP §12.3）

只想把理论挂首页者、强反学院情绪者、不愿接受批评与修订者。产品不拒绝其内容，但不为其姿态优化体验。

---

## 5. 核心领域模型

### 5.1 实体总览

```text
User ──< Project ──1:1── TheoryPacket ──< Claim
                  │                  ├──< GlossaryEntry
                  │                  ├──< RiskFlag
                  │                  ├──< ReviewSubmission (tension | object)
                  │                  ├──< Version  (revision history)
                  │                  └──── MaturityState (T0–T7)
                  └──< InterviewSession ──< Turn
每个可显示字段/命题 ──1:1── ProvenanceRecord
```

### 5.2 Theory Packet 数据结构（核心资产，对应 BP §4.1 的 20 字段）

字段名对外为英文。`Gen` = 主要生成方（`AI` / `interview` / `author` / `classifier` / `system`）；`Prov` = 默认来源标签；`Req@` = 该字段成为必填的最低成熟度。

| # | 字段（EN / CN） | 类型 | Gen | 默认 Prov | Req@ |
|---|---|---|---|---|---|
| 1 | Theory title / 理论名称 | string | author/AI | ai_inferred | T1 |
| 2 | One-sentence thesis / 一句话主张 | string | AI→author | ai_inferred | T1 |
| 3 | Problem origin / 问题来源 | text | interview | author_confirmed | T1 |
| 4 | **Object proposal / 想让什么被看见** ★ | text | interview(张力) | ai_inferred | T1 |
| 5 | **Choice tension / 选择张力** ★★ | structured | interview(张力) | ai_inferred | T1 |
| 6 | Core concepts / 核心概念 | list | AI | ai_inferred | T1 |
| 7 | Glossary / 术语翻译表 | map(term→meaning) | AI→author | ai_inferred | T1 |
| 8 | Core claims / 核心命题 | list&lt;Claim&gt; | AI→author | ai_inferred | T2 |
| 9 | Claim map / 命题地图 | graph | AI | ai_inferred | T2 |
| 10 | Evidence types / 证据类型 | per-claim enum | author | author_confirmed | T3 |
| 11 | World knowledge alignment / 与已有知识关系 | structured(relation) | AI+author | ai_inferred | T2 |
| 12 | Steelman / 最强版本 | text | AI | ai_inferred | T3 |
| 13 | Red-team critique / 最强反对 | list | AI/reviewer | ai_inferred | T3 |
| 14 | **Failure conditions / 失败条件** ★ | list | author+AI | author_confirmed | T3 |
| 15 | Risk flags / 风险标注 | list&lt;RiskFlag&gt; | classifier+author | system | T1 |
| 16 | **Author confirmation / 作者确认** ★ | per-field + overall | author | author_confirmed | T2 |
| 17 | Review ledger / 评审账本 | list&lt;ReviewSubmission&gt; | system | system | T4 |
| 18 | Revision history / 修订历史 | list&lt;Version&gt; | system | system | T5 |
| 19 | Public brief / 大众解释版 | text | AI→author | ai_inferred | T6 |
| 20 | Academic brief / 学院对接版 | text | AI→author | ai_inferred | T6 |

★ = 单点赌注直接相关字段；★★ = 产品命门字段。`Choice tension` 的挖掘质量决定整个产品成败（DP3）。

**`Choice tension` 结构化定义**（不是一段自由文本，可被评审与翻译）：
```text
ChoiceTension {
  protected_value: text        // 作者真正想守护的选择/价值
  competing_pressures: [text]  // 与之冲突的价值、压力、痛苦、优化、权威、处境
  current_misread_object: text // 当前语言把它误切成了什么对象
  alternative_objectifications: [text] // 同一张力下其他对象化方式（评审补充）
}
```
此结构是"研究者间张力翻译"（第二支柱，§6.3）的技术前提：两个 packet 的 `ChoiceTension` 可被比对，发现"在与同一个张力较劲"。

### 5.3 来源/透明标签模型（DP9，BP §5.2 + §13.4）

每个可显示字段与每条命题携带一个 `ProvenanceRecord`：

```text
ProvenanceRecord {
  status: original | ai_inferred | author_confirmed | reviewer_challenged
  edited_by_human: bool
  last_changed_at, last_changed_by
}
```
展示层映射为标签：**AI assisted / human revised / author confirmed / reviewer challenged**。
硬规则：任何 `ai_inferred` 且未经 `author_confirmed` 的字段，**不得进入正式社区评审**（BP §5.2）。

### 5.4 成熟度状态机（T0–T7，BP §6.2）

宽进严出落在这台状态机上。**升级是"挣来的"，由门槛（gate）触发，不由时间或点赞触发（DP8/DP10）。**

```text
T0 Impulse ──g1──> T1 Structured ──g2──> T2 Author-confirmed ──g3──> T3 Criticizable
   ──g4──> T4 Community-reviewed ──g5──> T5 Revised ──g6──> T6 Expert-readable ──g7──> T7 Public-ready
```

| 门 | 从→到 | 进入条件（gate） |
|---|---|---|
| g1 | T0→T1 | 字段 1–7、15 已生成（AI 可，未确认可） |
| g2 | T1→T2 | **作者确认 `Choice tension` + `Object proposal` 命中**（情绪命门），且核心字段 `author_confirmed` |
| g3 | T2→T3 | 有清晰 `Core claims` + `Failure conditions`，且 `Risk flags` 已解析到合规输出形态（§8.1） |
| g4 | T3→T4 | 收到 ≥N 份结构化评审（张力层 ≥1 + 对象层 ≥1；N 默认=2，可配置） |
| g5 | T4→T5 | 评审触发了一次**实质性**版本变更（命题/张力/失败条件出现 diff，非措辞修饰） |
| g6 | T5→T6 | 生成 Academic brief 且通过"冷读者测试"清单（§7.6 验收） |
| g7 | T6→T7 | 生成 Public brief，风险限形已强制执行（高风险内容受 §8.1 约束） |

降级：评审推翻已确认结论时，相关字段 Prov 转 `reviewer_challenged`，packet 可被系统降级并通知作者（不静默）。

### 5.5 其他实体关键字段

- **Project**：`owner, title, visibility(private|unlisted|public), created_at`；默认 **private**（DP-安全）。
- **InterviewSession / Turn**：`session.phase(tension|object)`、`turn.role(system|user)`、`turn.intent`（追问意图，用于质量审计），可中断续答。
- **Claim**：`text, type(descriptive|causal|normative|definitional), strength(strong|weak|unspecified), evidence_type, prov`。
- **RiskFlag**：`domain(medical|psych|child_ed|finance|legal|political|neuro|self_state|none), level, allowed_output_forms[], forbidden_output_forms[]`。
- **ReviewSubmission**：`layer(tension|object), reviewer, answers{}, adopted_by_author(bool), created_at`。
- **Version**：`packet_snapshot, change_summary, triggered_by(review_id|author), maturity_at_time`。

---

## 6. 关键用户旅程

### 6.1 作者主旅程（端到端，张力优先）

```text
注册/登录
  ↓
创建 Project（默认 private）
  ↓ 输入：上传文件 / 粘贴长文 / 空白直接进访谈
风险预分类（RiskFlag，§8.1）——尽早，不阻断输入
  ↓
【访谈引擎 · 张力层】(DP1 先)  ← 产品核心，决定生死
  挖掘 protected_value / competing_pressures / current_misread_object
  ↓
【作者确认 · 命门】"对，这就是我一直说不清楚的东西" → 命中则 g2 升 T2
  ↓
【访谈引擎 · 对象层】生成 glossary / claim map / steelman / red-team
  ↓
世界知识对齐（给选项，不压判，DP2）
  ↓
逐字段作者确认/更正（每字段带 Prov 标签）
  ↓
发布 private / unlisted / public（含 AI 透明标签）
  ↓
AI-assisted red-team  +  社区评审（张力层表 → 对象层表）
  ↓
修订路线图 → 版本更新（g5）→ 成熟度升级
  ↓
导出 Public Brief / Academic Brief（冷读者测试，DP5）
```

### 6.2 评审者旅程

进入 packet → 先看 `Choice tension` 与 Object proposal → 填**张力层评审表**（理解 + 选项支撑）→ 再填**对象层评审表**（冷读者批评）→ 作者可标记"采纳"→ 评审者获积分/贡献记录（DP10：点赞不计入）。

### 6.3 两大支柱对应的两类旅程（BP A.3）

- **支柱一 · 作者侧张力成熟化**：即 6.1，单作者私人体系 → 可批评 packet。
- **支柱二 · 研究者间张力翻译**（V1 做"只读发现"，不做撮合）：系统比对 packet 间 `ChoiceTension`，向作者**提示**"另一位研究者可能在与同一张力较劲"。这是 ResearchGate/OpenReview 难以复制处（它们默认共享学术语言；IRP 处理的恰是"没有共同语言"）。V1 仅做提示与并排展示，撮合/私信留待 V2。

---

## 7. 功能需求

优先级：**P0** = Gate 0 验证或 alpha 阻断项；**P1** = 首批付费 V1 所需；**P2** = V1 之后。带"验收"的为关键项给出可测条件。

### 7.1 账户与项目

| ID | 需求 | 优先级 |
|---|---|---|
| FR-ACC-01 | 邮箱注册/登录（opt-in；不导入任何第三方邮件名单，BP §11.3） | P0 |
| FR-PRJ-01 | 创建 Theory Project，三种输入：上传文件 / 粘贴文本 / 空白进访谈 | P0 |
| FR-PRJ-02 | Project 默认 **private**；可切换 private/unlisted/public | P0 |
| FR-PRJ-03 | Project 列表/仪表盘，显示成熟度 T 级与待办（确认/评审/修订） | P1 |
| FR-PRJ-04 | 长文本处理上限分层（Builder 基础、Researcher 更长，BP §9.3） | P1 |

### 7.2 访谈引擎（张力挖掘）★ 核心 · DP3

| ID | 需求 | 优先级 |
|---|---|---|
| FR-INT-01 | 多轮访谈，而非单次总结（BP §5.1）；可中断、可续答、可回看 | P0 |
| FR-INT-02 | **张力层在前**：必须先挖 `protected_value / competing_pressures / current_misread_object`，再进对象层（DP1） | P0 |
| FR-INT-03 | 张力层至少覆盖 BP §5.1 六问：不满意的现有解释 / 想让什么被看见 / 现被误解成什么 / 背后哪几种选择压力冲突 / 最想守护什么价值 / 若被理解会改变什么选择 | P0 |
| FR-INT-04 | 用前沿模型跑张力层，不因成本降级（DP3）；模型路由见 §9.4 | P0 |
| FR-INT-05 | 反磨平护栏：禁止在张力层引入批评或下结论；追问而非评判（DP2/DP7） | P0 |
| FR-INT-06 | 根据回答动态追问（branching），而非固定问卷 | P1 |
| FR-INT-07 | 访谈过程不对作者本人做心理判断/诊断（DP7，BP A.9） | P0 |

**FR-INT-02/03 验收**：给定一段真实独立研究者原文，引擎在 ≤R 轮内产出一个结构化 `ChoiceTension`，且其 `protected_value` 在作者确认环节命中（见 §7.3 北极星验收）。

### 7.3 Theory Packet 生成与作者确认 ★ 核心 · DP4

| ID | 需求 | 优先级 |
|---|---|---|
| FR-GEN-01 | 由"访谈 + 原文"生成 Theory Packet 字段 1–9、12、13、15（§5.2） | P0 |
| FR-GEN-02 | 每个字段、每条命题写入 `ProvenanceRecord`（§5.3） | P0 |
| FR-CFM-01 | **命门确认**：在张力层产物上问作者"我们有没有看穿你？"（捕捉被看见，而非"拆得准否"，DP4） | P0 |
| FR-CFM-02 | 作者可逐字段确认/更正；任何 AI 字段未经确认不进社区评审（BP §5.2） | P0 |
| FR-CFM-03 | 命门命中触发成熟度 g2（T1→T2，§5.4） | P0 |
| FR-GEN-03 | 生成 Glossary、Claim Map、Steelman、Red-team（对象层） | P1 |
| FR-GEN-04 | `Failure conditions` 作者+AI 协同补全（T3 门槛字段，DP5 严出抓手） | P1 |

**FR-CFM-01 验收（= 北极星，§10.1）**：在 alpha 真实用户中，张力层产物的作者确认命中率 ≥ 目标阈值；命中定义为作者主动表达"对，就是这个/这正是我说不清的东西"，而非被动点"确认"。**未达阈值则不进入付费 V1 构建（见 §11 Gate 0）。**

### 7.4 世界知识对齐

| ID | 需求 | 优先级 |
|---|---|---|
| FR-WKA-01 | 提示相邻领域如何处理类似问题、是否重复已有理论、真正新处何在（BP §5.3） | P1 |
| FR-WKA-02 | 标注与既有理论关系：补充 / 反对 / 重命名 / 重划边界 / 误读（结构化，进字段 11） | P1 |
| FR-WKA-03 | 姿态约束：给作者"更多选项"，不以权威答案压制（DP2） | P1 |

### 7.5 发布与溯源展示

| ID | 需求 | 优先级 |
|---|---|---|
| FR-PUB-01 | 发布为 private/unlisted/public Theory Packet 页面 | P0 |
| FR-PUB-02 | 展示层显示 AI 透明标签（AI assisted/human revised/author confirmed/reviewer challenged，DP9） | P0 |
| FR-PUB-03 | public packet 页面含 Object proposal、Choice tension、Claim map、成熟度 T 级与评审账本 | P1 |
| FR-PUB-04 | 点赞/收藏/评论存在但**不计入**成熟度或质量（DP10，BP §7.1） | P1 |

### 7.6 评审系统（张力层 + 对象层 + AI red-team）· DP1/DP5

| ID | 需求 | 优先级 |
|---|---|---|
| FR-REV-01 | **张力层评审表**（BP A.4）：① 我理解你想守护的选择是 X 对吗 ② 还有哪些别的对象化方式 ③ 每种选择各付什么代价/放弃什么 ④ 现有世界知识给了哪些现成选项 | P1 |
| FR-REV-02 | **对象层评审表**（BP §7.2）：理解的对象 / 最清楚命题 / 最弱命题 / 仍模糊术语 / 与既有理论关系 / 失败条件够强否 / 应用风险 / 下一版最该修哪 | P1 |
| FR-REV-03 | 顺序强制：先张力层（提供选择支撑，不制造张力），后对象层（冷读者批评）（DP1/DP2） | P1 |
| FR-REV-04 | 评论与评审分离：仅结构化评审计入声誉（BP §7.1） | P1 |
| FR-REV-05 | AI-assisted red-team：自动生成对象层批评草稿，供作者与评审者参考 | P0 |
| FR-REV-06 | 作者可标记评审"采纳"，采纳触发修订路线项与积分（BP §7.3） | P1 |
| FR-REV-07 | Researcher 层可邀请指定评审者（私密项目，BP §9.3） | P1 |

**FR-REV-02/03 验收（冷读者测试，DP5/G2）**：packet 进入 T6 前须通过对象层"冷读者"清单——一个不认识作者、不抱同情的外部读者能在 10 分钟内判断核心命题、最弱处与失败条件。**张力层的温暖不得软化此门**，否则平台退化为"更善良的回音壁"（BP A.5）。

### 7.7 成熟度与版本

| ID | 需求 | 优先级 |
|---|---|---|
| FR-MAT-01 | 实现 T0–T7 状态机与 g1–g7 门槛（§5.4） | P1 |
| FR-MAT-02 | 升级仅由门槛触发，不由时间/点赞触发（DP10） | P1 |
| FR-MAT-03 | 版本历史：每次实质修订生成 Version 快照，记录 change_summary 与触发源 | P1 |
| FR-MAT-04 | 评审推翻结论时字段降级为 reviewer_challenged 并通知作者，不静默 | P1 |

### 7.8 导出

| ID | 需求 | 优先级 |
|---|---|---|
| FR-EXP-01 | 导出 Public Brief（大众解释版）与 Academic Brief（学院对接版） | P1 |
| FR-EXP-02 | 导出 PDF / 网页 | P1 |
| FR-EXP-03 | 多语言输出（English-first，其他语言作为功能优势，BP §11.1） | P1 |

---

## 8. 治理与安全需求（跨切面，含 P0）

安全不能等付费功能。以下为 alpha 即须生效项。

### 8.1 高风险内容限形门（BP §6.3，DP8）

| ID | 需求 | 优先级 |
|---|---|---|
| FR-GOV-01 | 内容风险分类器，识别 domain ∈ {medical, psych, child_ed, finance, legal, political, neuro, self_state}，写入 RiskFlag | P0 |
| FR-GOV-02 | 命中高风险域时，输出**只允许**为 hypothesis / reflection framework / research proposal / observation protocol / non-clinical educational material | P0 |
| FR-GOV-03 | **禁止**输出为 diagnosis / treatment / intervention / financial·legal advice / protocol for others | P0 |
| FR-GOV-04 | 高风险 packet 未完成限形不得升至 T3 以上（接 g3） | P0 |

**FR-GOV-02/03 验收（worked example，BP A.8）**：输入"我用 LLM 发现了快乐的机制、胜过神经科学"，系统应：① 宽进不拒；② 挖出可讨论对象 *joy = suspension of optimization*；③ 严出降级为 *Hypothesis: joy as the suspension of optimization pressure*，并追问失败条件与 affect/reward 文献关系。

### 8.2 作者照护边界（BP A.9，DP7）

| ID | 需求 | 优先级 |
|---|---|---|
| FR-GOV-05 | 涉 self_state 类主张时，系统对内容做张力翻译，**不对作者本人**做心理判断/干预 | P0 |
| FR-GOV-06 | 既不背书也不病理化，将其保持为"关于经验的可讨论对象" | P0 |

### 8.3 AI 透明与隐私版权（BP §13.4/§13.5，DP9）

| ID | 需求 | 优先级 |
|---|---|---|
| FR-GOV-07 | 全程 AI 溯源标签（§5.3），展示层可见 | P0 |
| FR-GOV-08 | 用户保留理论权利；明确上传内容归属、平台生成使用范围 | P0 |
| FR-GOV-09 | 是否允许用用户内容训练/改进平台模型——**默认关闭，显式 opt-in** | P0 |
| FR-GOV-10 | 私密项目不公开；受邀评审者访问权限可控；提供删除与导出 | P0 |
| FR-GOV-11 | 反真理认证声明：产品文案与导出件统一标注"只认证过程，不认证真理"（BP §13.1/§16） | P1 |

---

## 9. 非功能需求

### 9.1 隐私与安全
default-private（FR-PRJ-02）；训练 opt-in（FR-GOV-09）；删除/导出（FR-GOV-10）；不导入第三方邮件名单（FR-ACC-01）。

### 9.2 性能与体验
访谈为多轮深度交互，**容忍单轮数秒级延迟以换取张力挖掘质量**（DP3 优先于速度）；长文本处理按订阅分层（FR-PRJ-04）；访谈断点续答必须可靠（FR-INT-01）。

### 9.3 国际化
English-first；字段名/状态/UI 文案英文；packet 内容支持多语言输入与多语言导出（FR-EXP-03）。

### 9.4 LLM 成本与模型路由（接 BP §14.2/§15）
- **分层路由**：张力层（FR-INT-04）= 前沿模型，不降级；对象层生成、red-team、分类 = 可用较低成本模型。
- 记录每个 packet 的 LLM 成本（北极星之外的运营指标，BP §14.2"每个理论平均 LLM 成本"）。
- 设单 packet 成本上限告警；超限不静默吞成本。

### 9.5 可观测性
所有北极星与漏斗事件（§10）须埋点；访谈 `turn.intent` 留痕以便事后审计张力挖掘质量。

---

## 10. 指标与埋点

### 10.1 北极星指标（唯一最高优先，DP3/DP4）

> **张力层作者确认命中率** = 主动确认"对，就是这个"的 packet 数 / 完成张力层访谈的 packet 数。

这是 BP A.2/A.10 指认的"最该优先验证的单点"。它高于付费意愿、评审者供给、留存等一切指标。

### 10.2 产品有效性指标（BP §14.1）
作者确认准确率、陌生读者 10 分钟理解率、有效（结构化）评审率、修订触发率（评审→实质修订）、失败条件完成率、高风险输出标注率。

### 10.3 商业漏斗（BP §14.2，付费 V1 后才重点看）
Waitlist 转化 → 首个 packet 完成率 → Free→Builder → Builder→Researcher → 服务包购买 → 月留存 → 单 packet LLM 成本 → 单付费用户毛利。

### 10.4 品牌指标（BP §14.3）
被外部引用的 packet 数、被收录出版物数、桥接读者反馈、高质量研究者推荐、机构询问数。

### 10.5 关键埋点事件（最小集）
`interview_tension_completed`、`author_confirm_hit` / `author_confirm_miss`、`packet_published`、`review_submitted{layer}`、`review_adopted`、`version_created{substantive:bool}`、`maturity_changed{from,to}`、`risk_flag_set{domain}`、`brief_exported{type}`、`llm_cost_recorded{packet,amount}`。

---

## 11. 验证计划与发布门

依据 BP A.10：**最该先验证的不是付费意愿或评审者供给，而是张力挖掘质量，以及"对内温暖能否与对外可信共存"。** 因此发布分门进行，前一门不过不进下一门。

### 11.0 Gate 0 — 手工验证（构建 V1 之前）★ 必经
- **做法**：找 3–5 位真实独立研究者，**先手工**（前沿模型 + 访谈协议，最薄工具甚至无平台）帮其显影 `Choice tension`，让其确认"对，这就是我真正在意的"；再在此基础上引入一轮批评，观察事后**更投入还是流失**。
- **同时检验三件最要命的事**：情绪价值、张力层假设、"理解 + 批评"共存（BP A.10）。
- **通过判据**：北极星命中率达阈值，且引入批评后多数人更投入而非流失。
- **不通过**：回到访谈协议迭代，**不构建付费平台**。这是本 PRD 最重要的产品判断——不要在单点赌注未验证前堆功能。

### 11.1 Gate 1 — Alpha（BP §17 31–90 天）
构建 P0：注册、项目、访谈引擎、生成、命门确认、AI red-team、风险限形、AI 透明、隐私。招 10–20 alpha 用户。验证 BP §14.1 三指标：作者确认准确、陌生读者理解、评审导致修订。

### 11.2 Gate 2 — 付费 V1（BP §17 3–6 月）
加 P1：张力层/对象层评审表、成熟度状态机、版本历史、世界知识对齐、导出、Builder/Researcher 订阅。先决定首批付费形态：Builder 订阅 vs Deep Theory Packet 服务包（BP §19.10）。

### 11.3 Gate 3 — 出版与机构试点（BP §17 6–12 月，多为后续 PRD）
Quarterly Review 001、专题 dossier、机构空间 beta、桥接读者小组、100+ packet。

---

## 12. 关键决策（2026-06-17 已采纳默认）

> Founder 已确认采纳下表全部建议默认值（2026-06-17）。Q2 的阈值与"命中"判定已在 [Gate 0 验证工具包](INDEPENDENT_RESEARCHER_PLATFORM_GATE0_VALIDATION_KIT_2026-06-17.md) §1 中操作化。下表保留为决策记录。

| # | 决策 | 影响 | 采纳的决定 |
|---|---|---|---|
| Q1 | 产品英文名是否长期用 "Independent Researcher Platform" 或仅作阶段名（BP §19.1） | 品牌、域名 | 阶段名，留长期名空间 |
| Q2 | 张力层北极星命中率的**具体阈值**与"命中"判定标准 | Gate 0 成败判据 | **已操作化**：盲评双人、HIT/PARTIAL/MISS 评分、通过阈值见 [Gate 0 验证工具包](INDEPENDENT_RESEARCHER_PLATFORM_GATE0_VALIDATION_KIT_2026-06-17.md) §1 |
| Q3 | 访谈轮数上限 R 与单 packet 成本上限 | 成本/体验 | 张力层不设硬轮数上限、设成本告警；对象层设上限 |
| Q4 | 首批付费形态：订阅先行 or 服务包先行（BP §19.10） | 现金流/构建顺序 | 服务包（Deep Theory Packet 199 美元）先行，验证付费意愿再上订阅 |
| Q5 | 是否允许用户内容用于改进平台模型 | 隐私/信任 | 默认关闭，显式 opt-in（已落 FR-GOV-09） |
| Q6 | g4 评审门 N 值、评审者冷启动供给 | 升级可行性 | N=2 起；alpha 期评审者可由 founding circle 兼任 |
| Q7 | 支柱二（研究者间张力翻译）V1 做到"只读发现"是否足够 | 差异化壁垒 | V1 仅提示+并排，撮合留 V2 |

---

## 13. 需求追溯索引

| 模块 | 需求 ID | 关键依赖原则/BP |
|---|---|---|
| 账户项目 | FR-ACC-01, FR-PRJ-01..04 | §11.3, §9 |
| 访谈引擎 ★ | FR-INT-01..07 | DP1/DP2/DP3/DP7, §5.1, A.1/A.2 |
| 生成与确认 ★ | FR-GEN-01..04, FR-CFM-01..03 | DP4, §5.2, A.2 |
| 世界知识对齐 | FR-WKA-01..03 | DP2, §5.3 |
| 发布溯源 | FR-PUB-01..04 | DP9/DP10, §7.1, §13.4 |
| 评审 | FR-REV-01..07 | DP1/DP5, §7.2, A.4/A.5 |
| 成熟度版本 | FR-MAT-01..04 | DP8/DP10, §6.2 |
| 导出 | FR-EXP-01..03 | §9, §11.1 |
| 治理安全 | FR-GOV-01..11 | DP7/DP8/DP9, §6.3, §13, A.8/A.9 |

---

## 14. 一句话总判

V1 不是"做一个研究者社区"，而是 **证明一件事并围绕它建最小系统**：

> LLM 能否稳定地让真实研究者说出"对，这就是我一直说不清楚的东西"——并在此基础上，让随之而来的批评被接住、被采纳、被人类承认。

这件事过了（Gate 0），其余皆是工程；这件事不过，其余皆是负债。
