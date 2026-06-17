---
id: INDEPENDENT-RESEARCHER-PLATFORM-BUSINESS-PLAN-2026-06-17
type: product_business_plan
status: draft_v0_1
canonical: false
scope: public_project_planning
project: Independent Researcher Platform
created: 2026-06-17
updated: 2026-06-17
language: zh-CN
frontstage_positioning: English-first product, multilingual later
srt_role: hidden_operating_system_not_frontstage_doctrine
claim_mode: strategy_planning
privacy_note: "Do not use disclosed third-party email lists as marketing lists. Treat such events only as evidence of a market problem and recruit through opt-in public channels."
---

# Independent Researcher Platform 商业计划书 v0.1

> 核心口号：**Make theories understandable, criticizable, revisable, and discussable.**
>
> 中文压缩：**让理论变得可理解、可批评、可修订、可对话。**
>
> 平台原则：**We do not certify truth. We help theories become public intellectual assets.**

本文件用于整理 Independent Researcher Platform（下称 IRP）的商业计划、产品路线、运营边界、变现结构与早期执行方案。SRT 在该项目中作为隐藏操作系统，不作为前台教义；前台产品面向独立研究者、LLM 辅助研究者、非传统理论建构者，以及后续更广泛的公共空间参与者。

---

## 0. 执行摘要

IRP 是一个面向独立研究者的理论成熟化平台。它不是论文仓库、民科论坛、AI 总结器，也不是学院同行评审的替代品。它要补的是一个现有知识生态中缺失的中间层：**一个理论从私人体系、长文、直觉、痛苦或跨学科冲动，走向公共可理解、可批评、可修订、可对话之前，需要经过的结构化翻译与评审过程。**

第一阶段产品聚焦独立研究者：让用户提交理论、模型、框架、长文或假说，通过多轮 LLM 访谈识别其真正想构建的对象、核心命题、术语系统、选择张力、已有知识关系、失败条件与应用风险，再生成标准化的 **Theory Packet**。之后，Theory Packet 进入社区评审、AI 辅助 red-team、版本修订与成熟度分层。

第二阶段产品扩展为公共对象生成平台：把第一阶段训练出的协议，从理论研究扩展到生活经验、社会问题、教育、医疗沟通、组织困境、价值冲突和公共议题，让更多主体把私人压力和未命名经验转化为公共理性中的可讨论对象。

商业上，IRP 不是靠“认证真理”变现，而是靠工具订阅、深度理论包、评审服务、工作坊、机构空间、出版物与专题报告变现。其核心资产不是代码本身，而是：

1. 理论翻译协议；
2. Theory Packet 数据结构；
3. LLM 多轮访谈 Skill；
4. 宽进严出的成熟度尺度；
5. 高质量理论案例库；
6. 社区评审与出版机制。

---

## 1. 项目使命与基本定位

### 1.1 使命

IRP 的使命是：

> **帮助独立研究者把私人理论体系转化为公共思想资产。**

公共思想资产不等于真理认证。它意味着一个理论至少已经具备以下条件：

- 可理解：别人能知道它想解释什么；
- 可批评：它有可被检验、质疑和反驳的命题；
- 可修订：它不是封闭信仰，而能吸收批评并产生版本变化；
- 可对话：它能与已有知识、相邻理论、生活经验和应用场景建立桥梁。

### 1.2 前台定位

英文前台定位：

> **A platform for independent researchers to turn private frameworks into public, criticizable theory packets.**

中文内部定位：

> 面向独立研究者、LLM 辅助研究者和非传统理论建构者的平台，帮助他们把私人体系转化为公共可理解、可批评、可修订、可对话的理论包。

### 1.3 SRT 的角色

SRT 只作为隐藏操作系统，不作为用户必须接受的世界观。平台前台不要求用户理解 SRT，也不把所有理论翻译成 SRT 术语。

SRT 在产品底层提供三个方法灵感：

1. **对象不是起点，而是生成结果。** 一个理论也不是一开始就是成熟对象，需要经过命名、排除、稳定、批评和修订。
2. **选择张力在对象背后。** 很多理论表面上是概念分歧，底层是价值、压力、痛苦、优化、权威、生活处境之间的选择冲突。
3. **后果需要回流。** 理论不能只被表达，还要记录批评、修订、风险和应用后果。

平台必须避免把 SRT 变成前台判准。用户看到的是清晰流程，而不是某套理论的推广。

---

## 2. 市场问题

### 2.1 独立研究者缺少“前同行评审层”

现有学术生态通常要求一个思想以论文、preprint、会议投稿、导师网络或机构 affiliation 的形式出现。但很多独立研究者的思想处于更早阶段：它们可能是长文、个人体系、跨学科框架、生活痛点、哲学模型、AI 辅助草稿或尚未对象化的理论冲动。

这些内容常常无法直接进入传统评审，因为：

- 太长、太私人化、太体系化；
- 缺乏术语翻译；
- 没有明确核心命题；
- 不知道与已有文献关系；
- 没有失败条件；
- 直接联系学院学者会造成巨大审阅负担。

因此，市场缺少一个介于“个人长文/社媒表达”和“正式论文/期刊评审”之间的成熟化层。

### 2.2 独立研究者之间也沟通困难

独立研究者之间并不天然容易互相理解。很多人都在自己设计的体系里说话，每个人都有自己的术语、对象、问题顺序和隐含价值。结果是：

- A 说“场”，B 说“能量”，C 说“优化”，D 说“意识”，但彼此指向完全不同；
- 用户常常发出一整套私人体系，而不是公共可评审对象；
- 讨论很快变成互相推销、互相误解或互相否定。

IRP 的核心机会在于建立一个 **Theory Translation Layer / 理论翻译层**：先让理论可理解，再让它可批评。

### 2.3 LLM 同时制造机会与噪音

LLM 让更多人能够写出长文、构造理论、联系专家、组织材料。这会带来大量噪音，也会释放真实的独立思考能力。

现有反应往往把二者混在一起：LLM 辅助、独立身份、非正式联系、低质量自动生成，被归成同一类。这种归类可以保护学术时间，但也可能把认真独立研究与低质量文本一并排除。

IRP 的商业机会是：**不替任何理论背书，但把 LLM 从文本生成器变成理论成熟化工具。**

### 2.4 社交媒体奖励注意力，不奖励修订

传统社交平台容易奖励强情绪、宏大叙事、反权威姿态和人设魅力。它不奖励失败条件、修订记录、有效批评、术语澄清和风险边界。

IRP 需要建立另一套激励：

- 谁能把理论说清楚；
- 谁能提出好批评；
- 谁能帮助理论修订；
- 谁能补充文献、反例、边界和应用风险；
- 谁能让不同私人体系互通。

---

## 3. 产品愿景：两阶段路线

### 3.1 第一阶段：Independent Researcher Platform

第一阶段服务高理论密度用户：独立研究者、LLM 辅助研究者、AI/意识/认知/复杂系统/哲学/价值理论建构者。

目标不是追求大众规模，而是训练协议：

> **让理论变得可理解、可批评、可修订、可对话。**

第一阶段是协议训练场。它要验证：一个混乱或私人化的理论，是否能通过统一 Skill 转化为 Theory Packet，并通过社区批评产生实质改进。

### 3.2 第二阶段：Object Commons / Choice Commons

第二阶段扩展到所有人，面向更广泛的生活经验、社会问题、教育、医疗沟通、组织困境、公共议题和价值冲突。

此时平台不再只问“你的理论是什么”，而是问：

- 你想让什么经验被看见？
- 当前语言把它误切成了什么对象？
- 背后的选择张力是什么？
- 现有世界知识给了哪些选项？
- 有没有更好的对象化方式？

第二阶段的使命是：

> **让隐藏的选择张力可见，把生活压力转化为公共理性中的对象。**

### 3.3 为什么必须先做第一阶段

不能一开始就做全公共空间。公共空间会立即引入心理、医疗、教育、政治、家庭、创伤、宗教、身份冲突等高风险内容。没有成熟协议和治理规则，平台会变成情绪倾倒或 AI 咨询杂货铺。

独立研究者群体更适合作为第一阶段，因为他们愿意接受术语表、命题图、反对意见、版本修订和理论成熟度。这可以训练平台骨架。

---

## 4. 核心产品：Theory Packet

### 4.1 Theory Packet 的定义

Theory Packet 是 IRP 的核心输出。它不是论文，不是 AI 摘要，也不是平台背书。它是一个理论进入公共讨论之前的标准化档案。

一个完整 Theory Packet 包括：

1. Theory title / 理论名称；
2. One-sentence thesis / 一句话主张；
3. Problem origin / 问题来源；
4. Object proposal / 作者真正想让什么被看见；
5. Choice tension / 对象背后的选择张力；
6. Core concepts / 核心概念；
7. Glossary / 作者术语翻译表；
8. Core claims / 核心命题；
9. Claim map / 命题地图；
10. Evidence types / 证据类型；
11. World knowledge alignment / 与已有知识的关系；
12. Steelman / 最强版本；
13. Red-team critique / 最强反对意见；
14. Failure conditions / 失败条件；
15. Risk flags / 风险标注；
16. Author confirmation / 作者确认；
17. Review ledger / 评审账本；
18. Revision history / 修订历史；
19. Public brief / 大众解释版；
20. Academic brief / 学院对接版。

### 4.2 Theory Packet 的价值

Theory Packet 给用户带来六类资产：

| 平台输出 | 用户获得的资产 |
|---|---|
| Theory Card / Claim Map | 认知资产：知道自己理论到底是什么 |
| Review Ledger | 信誉资产：证明经过批评过程 |
| Public / Academic Brief | 传播资产：别人能读懂 |
| Version History | 成长资产：理论能修订 |
| Reviewer / Collaborator Matching | 社交资产：遇到评审者和合作者 |
| Application Pathway | 实践资产：走向论文、项目、产品或公共影响 |

商业上，用户不是为“AI 帮我总结”付费，而是为“我的私人体系被转化为公共思想资产”付费。

---

## 5. 核心工作流

```text
Create project
↓
Upload text / paste notes / start from interview
↓
LLM multi-round interview
↓
Identify object proposal and choice tension
↓
Generate glossary, claim map, steelman, red-team
↓
World knowledge alignment
↓
Author confirmation / correction
↓
Publish private or public Theory Packet
↓
AI-assisted and community review
↓
Revision roadmap
↓
Version update
↓
Maturity stage upgrade
↓
Public brief / academic brief / publication candidate
```

### 5.1 多轮访谈

第一步不是让用户直接上传一篇理论后自动总结，而是通过多轮访谈帮助作者澄清：

- 你真正不满意的现有解释是什么？
- 你想让什么对象被看见？
- 这个对象现在被误解成了什么？
- 背后冲突的是哪几种选择压力？
- 你的理论最想保护什么价值？
- 如果这个理论被理解，会改变什么选择？

### 5.2 作者确认机制

LLM 不能替作者发明真实意图。每个 Theory Packet 必须区分：

- Original text / 作者原文；
- AI inferred / AI 推断；
- Author confirmed / 作者确认；
- Reviewer challenged / 评审质疑。

只有作者确认过的 Theory Packet，才进入正式社区评审。

### 5.3 世界知识对齐

平台不要求作者一开始熟悉全部文献，但需要帮助他看见：

- 相邻领域已经如何处理类似问题；
- 作者是否重复已有理论；
- 作者真正新的地方在哪里；
- 与既有理论是补充、反对、重命名、重划边界，还是误读。

这不是用权威答案压制作者，而是给主体更多选项。

---

## 6. 宽进严出机制

### 6.1 宽进

平台允许用户提交：

- 理论；
- 假说；
- 模型；
- 哲学框架；
- LLM 辅助作品；
- 跨学科长文；
- 个人研究计划；
- 未成熟但真实的问题意识。

平台不因为作者无 affiliation、非博士、使用 LLM、非英语母语、非传统学科路径而拒绝。

### 6.2 严出

平台不把所有内容都输出为成熟理论。输出必须分层：

| 阶段 | 含义 |
|---|---|
| T0 Impulse | 理论冲动，有问题意识但结构未清 |
| T1 Structured | 已结构化，有理论卡和术语表 |
| T2 Author-confirmed | 作者确认 AI 拆解准确 |
| T3 Criticizable | 已有清晰命题和失败条件，可被批评 |
| T4 Community-reviewed | 已接受社区结构化评审 |
| T5 Revised | 批评后产生实质修订 |
| T6 Expert-readable | 可供学院或领域专家快速判断 |
| T7 Application-restricted / Public-ready | 具备受限应用或公开传播条件 |

平台不认证理论真伪，只记录其经过了哪些澄清、批评、修订和风险标注过程。

### 6.3 高风险内容边界

高风险领域不禁止进入，但限制输出。

涉及医疗、心理、儿童教育、金融、法律、政治动员、神经干预等内容时，平台只允许输出为：

- hypothesis / 假说；
- reflection framework / 反思框架；
- research proposal / 研究提案；
- observation protocol / 观察方案；
- non-clinical educational material / 非临床教育材料。

不得输出为：

- diagnosis / 诊断；
- treatment / 治疗；
- intervention / 干预；
- financial/legal advice / 金融或法律建议；
- protocol for others / 面向他人的执行方案。

这体现“宽进严出”：平台可以接住内容，但不能放大其未经验证的应用风险。

---

## 7. 社区与评审机制

### 7.1 评论与评审分离

平台可以保留点赞、收藏、评论、关注等社区互动，但这些只代表兴趣，不代表理论成熟度。

真正计入声誉的是结构化评审：

- 概念澄清；
- 命题批评；
- 反例补充；
- 文献对齐；
- 失败条件强化；
- 应用风险检查；
- 帮助作者重写最强版本。

### 7.2 评审表结构

有效评审需要回答：

1. 我理解该理论想构建的对象是 X，对吗？
2. 该理论最清楚的命题是什么？
3. 最弱的命题是什么？
4. 哪个核心术语仍然模糊？
5. 它与已有理论的关系是否清楚？
6. 它的失败条件是否足够强？
7. 它的应用风险在哪里？
8. 下一版最应该修哪里？

### 7.3 积分与声誉

不强制提交者评审别人，但通过积分和声誉鼓励参与：

- 写出有效批评获得积分；
- 作者采纳评审获得积分；
- 帮助理论修订获得贡献记录；
- 点赞只作为兴趣信号，不作为质量信号；
- 平台奖励“让理论变清楚的人”，而不是奖励最大声的人。

---

## 8. 产品功能路线

### 8.1 V0：独立网站与等待名单

目的：先传播口号、理想与定位，吸引自愿参与者。

页面包括：

- 首页主标语；
- Mission；
- Manifesto；
- How it works；
- Theory Packet 示例；
- Join waitlist；
- Submit your theory；
- Founding circle call；
- Founder note；
- Privacy and AI-use statement。

V0 首页文案草稿：

> **Independent Researcher Platform**
>
> Make your theory understandable, criticizable, revisable, and discussable.
>
> For independent thinkers, LLM-assisted researchers, and builders of unconventional frameworks who want their ideas to become clear enough to be reviewed, challenged, improved, and shared.

### 8.2 V1：核心平台

第一版平台功能：

1. 用户注册；
2. 创建 theory project；
3. 上传文本 / 粘贴长文 / 进入访谈；
4. LLM 多轮理论访谈；
5. 生成 Theory Packet；
6. 作者确认和修改；
7. 公开 / 私密发布；
8. AI-assisted review；
9. 社区评审；
10. 版本历史；
11. 导出 Public Brief / Academic Brief。

### 8.3 V1 暂不做

第一版暂不做：

- 完整推荐流；
- 私信系统；
- 专家市场；
- 复杂群组；
- 大规模积分经济；
- 自动认证徽章；
- 对外应用市场。

先把 Theory Packet 和 Review Flow 做好。

---

## 9. 商业模式

### 9.1 免费层

目标：让用户快速感到“我被理解了”。

功能：

- 1 个公开 theory project；
- 基础 Theory Card；
- 一句话摘要；
- 普通人解释版；
- 基础公开页面；
- 社区评论。

### 9.2 Builder 订阅

目标用户：认真打磨个人理论的独立研究者。

价格建议：15–30 美元/月。

功能：

- 多个 theory project；
- 多轮 LLM 访谈；
- 完整 Theory Packet；
- Glossary；
- Core Claims Map；
- 基础 red-team；
- 版本历史；
- 多语言输出；
- PDF / webpage 导出。

### 9.3 Researcher 订阅

目标用户：需要深度理论打磨与对接材料的研究者。

价格建议：50–100 美元/月。

功能：

- 更长文本处理；
- 多模型评审；
- 学院摘要；
- 文献对齐；
- 高风险输出检查；
- 私密项目；
- 邀请评审者；
- 高级导出。

### 9.4 一次性服务包

早期现金流可能更多来自服务包：

| 服务 | 价格方向 | 交付 |
|---|---:|---|
| AI Theory Diagnostic | 49 美元 | 基础诊断、核心问题、下一步建议 |
| Deep Theory Packet | 199 美元 | 完整理解、命题、术语、red-team、修订路线 |
| Community Review Round | 499 美元起 | Theory Packet + 2–3 位评审 + 作者回应摘要 |
| Academy / Public Launch Pack | 999 美元起 | 学院简报、大众页面、传播材料、修订计划 |

### 9.5 机构与社群授权

中后期可面向：

- 独立研究院；
- AI safety 社群；
- 开放科学组织；
- 大学创新中心；
- 基金会；
- 思想社区。

提供私有空间、Theory Packet 流程、AI 预审、评审管理、专题报告。

### 9.6 出版物与报告

后期出版物包括：

- Quarterly Independent Theory Review；
- Annual Independent Researcher Yearbook；
- Thematic Dossiers；
- Theory Casebooks。

出版物展示理论如何被澄清、批评、修订和成熟化，而不是认证其为真理。

付费边界：可为排版、翻译、编辑服务收费，但不能付费买入选。出版物选择基于公开标准和编辑判断。

---

## 10. 市场与竞争定位

市场上已有相邻产品类型：

1. 学术社交和论文展示平台；
2. 开放评审平台；
3. preprint 和开放出版平台；
4. AI 研究助手；
5. 高认知思想社区；
6. 知识管理和出版基础设施。

IRP 的差异不在于“也能发布内容”，而在于：

- 它处理的是 paper 之前的 theory impulse；
- 它先让理论可理解，再让理论被评审；
- 它使用多轮 LLM 访谈，而不是单次总结；
- 它要求作者确认 AI 解释；
- 它把理论拆成对象、选择张力、术语、命题、失败条件、风险和修订历史；
- 它建立宽进严出的成熟度尺度；
- 它把理论转化为公共思想资产，而不是简单发表。

核心竞争壁垒：**Theory Maturation Protocol**。

---

## 11. Go-to-Market 策略

### 11.1 英文为主，多语言扩展

第一版前台以英文为主，因为独立研究者、AI、意识、复杂系统和开放科学社群的国际交流主要使用英文。后续可以加中文、多语言输出，作为功能优势之一。

### 11.2 创始人公开，但 SRT 隐身

创始人可以公开出现，讲清这个项目源于对独立研究者、LLM 时代知识过载、学院边界、公共对象生成的长期关注。但平台前台不以 SRT 命名，也不要求用户接受 SRT。

Founder note 可写：

> The platform is inspired by a broader philosophical concern: many important ideas fail not because they are false, but because they cannot yet be made legible, criticizable, revisable, and discussable.

### 11.3 不使用非自愿邮件名单营销

任何非自愿披露的邮件列表只能作为用户画像线索，不能作为营销名单。招募必须通过 opt-in：公开网站、公开帖子、自愿报名、社群转发、个人关系中的明确邀请。

这一点是平台信誉底线。项目要批判身份筛选和对象化垄断，就不能从不当使用他人邮箱开始。

### 11.4 早期渠道

- X / Substack / Medium；
- LessWrong / AI / consciousness / complex systems 社群；
- Independent researcher 社群；
- Active Inference、哲学、意识研究相关公开社群；
- 中文侧可接触集智俱乐部、复杂系统与 AI 讨论社群；
- Founder call；
- 公开的 Theory Packet 示例。

### 11.5 初期目标

前三个月目标不是规模，而是形成 10–20 个高质量样例，证明平台能把混乱理论变成可理解、可批评、可修订的 Theory Packet。

---

## 12. 团队与合作角色

### 12.1 初始核心团队

建议 3–5 人：

1. **Founder / Protocol Architect**：负责愿景、产品原则、Theory Packet 结构、选择张力显影协议。
2. **LLM Workflow Builder**：负责多轮访谈、claim extraction、red-team、作者确认、输出评估。
3. **Full-stack / No-code Builder**：负责网站、用户系统、LLM 接入、订阅支付、评审页面。
4. **Review Editor**：负责评审表、成熟度尺度、出版标准、质量边界。
5. **Community Moderator**：负责早期社区、用户访谈、争议处理、积分体系。

### 12.2 顾问圈

可找：

- 学院桥接读者：年轻 faculty、postdoc、editor、开放科学参与者；
- 严肃独立研究者：愿意接受批评，不只是推广自己体系；
- 出版 / 编辑顾问；
- 隐私 / 法务 / 高风险内容顾问。

### 12.3 不适合早期作为核心的人

- 只想把自己理论放上首页的人；
- 强反学院情绪者；
- 只会做增长、无法维护质量的人；
- 不愿接受批评与修订的人。

---

## 13. 运营与治理原则

### 13.1 平台不认证真理

平台只记录过程：

- 是否经过 LLM 拆解；
- 是否作者确认；
- 是否接受评审；
- 是否回应批评；
- 是否修订；
- 是否标注风险；
- 是否具备专家可读性。

### 13.2 反宗派化

每个理论必须有：

- 最强反对意见；
- 失败条件；
- 非适用范围；
- 与相邻理论的区别；
- 修订历史。

不鼓励“解释一切”的理论直接升级。

### 13.3 反流量化

可以有点赞，但不能把点赞等同于质量。质量要由结构化评审、修订、失败条件、风险标注和可理解性测试来衡量。

### 13.4 AI 透明

每个输出必须标明：

- AI assisted；
- human revised；
- author confirmed；
- reviewer challenged。

### 13.5 隐私与版权

用户保留自己理论的权利。平台需要明确：

- 用户上传内容归属；
- 平台可用于生成输出的范围；
- 是否允许训练或改进平台内部模型；
- 私密项目不公开；
- 被邀请评审者的访问权限；
- 删除和导出机制。

---

## 14. 成功指标

### 14.1 产品有效性指标

- 作者确认准确率：作者是否认为 Theory Packet 抓住了真实意图；
- 陌生读者理解率：10 分钟内能否理解理论核心；
- 有效评审率：评论中有多少是结构化有效批评；
- 修订触发率：评审是否导致理论实质修改；
- 失败条件完成率；
- 高风险输出标注率。

### 14.2 商业指标

- Waitlist 转化率；
- 首次 Theory Packet 完成率；
- Free → Builder 转化率；
- Builder → Researcher 转化率；
- 一次性服务包购买率；
- 月留存；
- 每个理论平均 LLM 成本；
- 每个付费用户平均毛利。

### 14.3 品牌指标

- 被外部引用的 Theory Packet 数；
- 被收录出版物的理论数；
- 学院桥接读者反馈；
- 高质量独立研究者推荐；
- 合作者和机构询问数量。

---

## 15. 成本结构

技术成本初期不高，核心成本在治理、评审、质量控制和早期样例打磨。

### 15.1 初期成本项

- 网站和前端；
- 数据库和文件存储；
- LLM API；
- 用户认证；
- 支付系统；
- 邮件服务；
- 域名和基础运维；
- 设计和品牌；
- 法务 / 隐私咨询；
- 社区运营时间；
- 手工样例制作时间。

### 15.2 成本判断

早期可用 LLM 辅助开发，先做轻量平台。最大风险不是开发费用，而是平台质量控制不足导致品牌一开始就被定义为低质量民科场。

---

## 16. 出版物战略

出版物是后期品牌资产。

### 16.1 Quarterly Review

每季度选 5–10 个 Theory Packet，展示其核心命题、选择张力、批评记录、作者回应和修订路径。

### 16.2 Annual Yearbook

年度总结：

- 今年出现了哪些新理论方向；
- 哪些理论从 T0 成长到 T4/T5；
- 哪些对象和选择张力反复出现；
- 哪些失败理论仍然有价值；
- 哪些方向值得学院关注。

### 16.3 Thematic Dossiers

专题报告可聚焦：

- New Theories of Consciousness；
- Independent Research on AI Agency；
- Theories of Value and Meaning；
- Alternative Models of Mental Health；
- Independent Systems Thinking；
- Human Flourishing after Optimization。

### 16.4 Theory Casebooks

展示理论成长过程：

```text
原始表达
↓
LLM 访谈识别对象
↓
选择张力
↓
第一版命题地图
↓
最强批评
↓
作者修订
↓
成熟版本
↓
应用路径
```

出版物前言必须写清：

> Inclusion does not mean certification of truth. It means the theory has been made legible, criticized, revised, and judged worthy of further discussion.

---

## 17. 路线图

### 0–30 天：定位与网站

- 锁定名称和域名；
- 完成 landing page；
- 写 Mission / Manifesto / How it works；
- 发布等待名单；
- 制作 1–3 个 Theory Packet 样例；
- 招募 founding circle。

### 31–90 天：V1 原型

- 用户注册；
- theory project 创建；
- 上传与访谈；
- Theory Packet 生成；
- 作者确认；
- 基础发布页；
- 基础 AI red-team；
- 早期评审表；
- 10–20 个 alpha 用户。

### 3–6 个月：社区评审与订阅

- Builder 订阅；
- Researcher 订阅；
- 社区评审；
- 版本历史；
- 积分机制；
- 导出 Public Brief / Academic Brief；
- 第一批高质量案例。

### 6–12 个月：出版物与机构试点

- Quarterly Review Issue 001；
- 专题 dossier 试验；
- 机构空间 beta；
- 学院桥接读者小组；
- 100+ Theory Packet；
- 10+ 高质量成熟化案例。

### 12–24 个月：公共空间扩展

- 从 Independent Researcher Platform 扩展到 Object Commons / Choice Commons；
- 支持生活问题、教育、组织、公共议题；
- 强化高风险输出限制；
- 发布年度年鉴；
- 开始更大规模机构合作。

---

## 18. 关键风险与应对

| 风险 | 表现 | 应对 |
|---|---|---|
| 噪音过载 | 大量低质量理论上传 | 强制 Theory Packet、成熟度分层、严出机制 |
| AI 篡改作者 | LLM 把作者理论磨平或误解 | 原文 / AI 推断 / 作者确认分层 |
| 民科互捧 | 用户互相吹捧或推销 | 结构化评审、质量积分、评论与评审分离 |
| 反学院情绪化 | 平台变成怨气社区 | 前台强调标准、批评、修订，不做反学院运动 |
| 高风险应用 | 医疗/心理/教育理论被当建议 | 宽进严出，限制输出形态和风险标注 |
| 伪权威化 | 平台被看成认证真理 | 明确只认证过程，不认证真理 |
| 商业薄弱 | 用户觉得 ChatGPT 也能总结 | 卖 Theory Packet + 评审 + 版本 + 连接 + 出版，而非总结 |
| 冷启动失败 | 第一批内容质量低 | 少而精，先做 10–20 个高质量样例 |

---

## 19. 当前最小行动清单

1. 决定产品英文名：Independent Researcher Platform 是否为长期名，或作为阶段名。
2. 注册域名或准备临时 landing page。
3. 写首页文案，突出四个价值：understandable, criticizable, revisable, discussable。
4. 制作 Theory Packet v0 模板。
5. 制作 1–3 个示例 Theory Packet。
6. 招募 founding circle：LLM workflow、builder、review editor、community moderator。
7. 开放 waitlist。
8. 启动 10–20 人 alpha。
9. 验证三个指标：作者确认准确、陌生读者理解、评审导致修订。
10. 决定第一批付费功能：Builder 订阅还是 Deep Theory Packet 服务包先行。

---

## 20. 最终战略判断

IRP 的商业价值不在“发表更多理论”，而在于建立一个新的理论成熟化基础设施。它把私人体系转化为公共思想资产，把 LLM 从文本生产器转化为理论翻译与评审工具，把独立研究者从孤立表达带入可理解、可批评、可修订、可对话的公共过程。

短期，它是一个独立研究者平台。

中期，它是一个 Theory Packet 和开放评审工具。

长期，它可以成为公共对象生成平台，让更多人把尚未命名的经验、痛苦、价值和选择张力带入公共理性空间。

项目的最强一句话：

> **We make theories understandable before judging them.**

更完整一句话：

> **We help independent researchers turn private frameworks into public intellectual assets: legible, criticizable, revisable, discussable, and ready for serious engagement.**
