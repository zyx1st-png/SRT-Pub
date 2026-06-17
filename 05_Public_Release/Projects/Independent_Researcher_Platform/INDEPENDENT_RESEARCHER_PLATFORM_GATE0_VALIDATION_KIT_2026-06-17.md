---
id: INDEPENDENT-RESEARCHER-PLATFORM-GATE0-VALIDATION-KIT-2026-06-17
type: experiment_protocol
status: ready_to_run_v0_1
canonical: false
scope: public_project_planning
project: Independent Researcher Platform
source_prd: INDEPENDENT_RESEARCHER_PLATFORM_PRD_2026-06-17.md
source_business_plan: INDEPENDENT_RESEARCHER_PLATFORM_BUSINESS_PLAN_2026-06-17.md
created: 2026-06-17
updated: 2026-06-17
language: zh-CN
participant_facing_language: en
privacy_note: "Recruit only through opt-in public channels. Never use any disclosed third-party email list as a recruiting list."
---

# IRP Gate 0 验证工具包 v0.1

> **一句话**：在写任何平台代码之前，用最薄的工具（前沿模型 + 一份访谈协议）证明一件事——LLM 能稳定地让真实独立研究者说出"对，这就是我一直说不清楚的东西"，并且随后的批评能被接住而不是把人吓跑。
>
> 这是 [PRD](INDEPENDENT_RESEARCHER_PLATFORM_PRD_2026-06-17.md) §11.0 定义的 **Gate 0**。它操作化 PRD 的北极星指标与 §12-Q2。**过则解锁 Gate 1（构建 alpha P0）；不过则迭代访谈协议，不构建平台。**

## 0. 这份文件是什么 / 怎么用

| 项 | 内容 |
|---|---|
| 目的 | 验证 BP A.2/A.10 指认的单点赌注：**张力挖掘质量**，以及 BP A.5 的"对内温暖能否与对外可信共存" |
| 形态 | 3–5 场一对一会话（每场 60–90 分钟）+ 盲评打分 + 一次通过/不通过判定 |
| 工具 | 前沿模型 + 本协议 + 一份录音/转录 + 一张打分表。**无需平台、无需写代码**（BP A.10：最薄工具甚至无平台） |
| 何时做 | BP §17 的 0–30 天窗口内，先于一切构建 |
| 谁来做 | 访谈者（Founder / LLM workflow builder）+ 两名盲评者（其一为 Review Editor） |
| 通过即解锁 | Gate 1：构建 alpha 的 P0 功能集（PRD §11.1） |
| 工作语言 | 本文件 zh-CN；**所有参与者可见材料（招募、访谈问题、确认话术）为英文** |

---

## 1. 假设与判据（操作化 PRD 北极星 + §12-Q2）

### 1.1 本实验同时检验的三个命门（BP A.10）

1. **情绪价值**：作者是否第一次感到"被看穿"。
2. **张力层假设**：把对象翻回背后的选择张力，是否真的是那把钥匙（DP3）。
3. **"理解 + 批评"共存**：在被理解之后引入批评，作者是更投入还是流失（DP5 / G2）。

一个实验，一次性压这三件最要命的事。

### 1.2 北极星：张力层命中率

> **命中率 = 被双盲评为 HIT 的会话数 / 完成张力层访谈的会话数。**

**为什么判定要严**：BP A.2 警告——挖得浅或挖错，**比无视更深的伤害，因为它假装理解却没有**。因此礼貌性的"嗯，差不多"必须计为 MISS，不是 HIT；并且由不参与访谈的盲评者打分，防止访谈者自我说服。

| 评级 | 定义 | 信号 |
|---|---|---|
| **HIT（2）** | 自发、带情绪的认出 | "exactly" / "that's it" / "I've never been able to put it that way" / 明显的松一口气、能量上来、抢着补充 |
| **PARTIAL（1）** | 方向对但需重要更正，或平淡同意 | "yeah, kind of" / 同意但无能量 / 认对一半改一半 |
| **MISS（0）** | 不对、转移话题、或空洞的客气同意 | "not quite" / 重新解释自己 / "I guess so" |

### 1.3 盲评双人协议（落实 §12-Q2）

- 两名评分者**独立**从转录/录音打分，互不通气；访谈者**不**参与打分。
- **一次会话计为 HIT，当且仅当两名评分者都独立打出 HIT。** 任一方打 PARTIAL/MISS，则该会话不计 HIT。
- 两人分歧 >1 级时，事后对照转录讨论并留记录（用于迭代访谈协议，不用于改判已记录分数）。

### 1.4 通过 / 不通过判据

**主门（命中率）**——按完成会话数取阈值（小样本、宁严勿宽）：

| 完成会话数 | 通过所需 HIT 数 |
|---|---|
| 3 | 3 |
| 4 | 3 |
| 5 | 4 |

**副门（共存，BP A.5）**——在拿到 HIT 的会话里，引入一轮对象层批评后：

- 表现为"lean-in（追问 / 想修订 / 想继续）"的人数 **严格多于** "pull-away（退缩 / 防御 / 脱离）"；且
- **零人**因批评而感到"被否定/被打发"（即批评没有落在理解之上，违反 DP1）。出现 1 例即为红旗，须先修批评的引入方式。

**两门皆过 → Gate 0 通过 → 进 Gate 1。** 任一不过：

- 命中率不足 → 访谈协议 / 模型提示词有问题 → 迭代 §3 协议后重跑，**不建平台**。
- 命中高但批评致流失 → 共存命题告急 → 重做批评的时序与措辞（§3.3），**仍不建平台**直到站住。

---

## 2. 招募（仅 opt-in，BP §11.3）

### 2.1 渠道
公开网站/帖子、自愿报名、社群转发、个人关系中的明确邀请；X / Substack / LessWrong / Active Inference / 意识 / 复杂系统等公开社群（BP §11.4）。**禁止**使用任何被披露的第三方邮件名单作为招募名单——它只能作为"需求真实存在"的证据，不能作为联系人列表（BP §11.3 / privacy_note）。

### 2.2 优先筛选"理想用户峰"（BP A.7）
偏好谦逊、寻求对话、自我克制者；尤其同时具备"严肃独立研究者 × 学院桥接读者"双重身份者。自发说出近似治理准则语言者（"criticize the work, not condemn the person" / "ordered sincerity"）是强信号。**不拒绝高风险/民科姿态峰**，但 Gate 0 这一关样本以理想峰为主，以纯净检验张力假设。

### 2.3 招募话术（EN，可直接发布/转发）

> **We're testing a new way to get an independent researcher's core idea *understood* — not judged, understood.**
>
> In one 60–90 minute conversation, we'll try to put into words the thing you've been trying to say and can't get others to see. Then — only once we've actually understood it — we'll push on it the way a serious, unsentimental reader would.
>
> No cost. No commitment. We're looking for people who want their work *engaged with seriously*, criticism included. If that's you, reply with a short paragraph on what you're working on and what you wish people understood about it.

### 2.4 知情同意要点（会前邮件/表单，EN）
- 会话会被录音/转录，仅用于本次评估，**不**用于训练任何模型（对齐 PRD FR-GOV-09）。
- 你保留你理论的全部权利；你可随时叫停。
- **我们翻译你的想法，不评估你这个人**——不做任何心理判断或诊断（DP7 / BP A.9）。

---

## 3. 会话协议（单场 60–90 分钟）

> 顺序铁律（DP1）：**先张力层（理解 + 选择支撑），后对象层（批评）。** 张力层绝不批评、绝不下结论。

### 3.0 会前
请参与者发来其原始表达（长文 / 笔记 / 帖子）。访谈者会前读一遍，但**不**预先下判断。

### 3.1 Phase A — 张力层访谈脚本（EN，约 35–50 分钟）

逐题问，每题用 1–2 个追问深入。目标是填出 PRD §5.2 的 `ChoiceTension`（protected_value / competing_pressures / current_misread_object）。

1. **Dissatisfaction** — "What existing explanation of this *almost* works but doesn't sit right with you? What does it miss?"
2. **Object proposal** — "What is the one thing you want people to finally *see* here that they currently don't?"
3. **Current misread** — "When people meet your idea now, what do they mistake it for?"
4. **Competing pressures** — "What are you caught between? Name two things that both matter to you here and seem to pull against each other."
5. **Protected value** — "Of everything in your framework, what is the one thing you would refuse to give up, even if you had to drop the rest?"
6. **Consequence** — "If someone truly got this, what choice would they make differently afterward?"

**访谈者护栏（do / don't）**
- DO：复述对方的话、追问、停顿、让对方修正你；找"两个都重要、却互相拉扯"的东西。
- DON'T：在 Phase A 评判对错、给结论、推销任何框架、对作者本人做心理解读（DP2 / DP5 / DP7）。

### 3.2 命门时刻 — 回放确认（EN，DP4）

合成 `ChoiceTension` 后，把"底下那层"说回给对方：

> "Let me try to say the thing underneath all of this. I think what you're really trying to protect is **[PROTECTED_VALUE]**, and it keeps colliding with **[COMPETING_PRESSURE]**. The reason your idea gets mistaken for **[MISREAD]** is that people see the surface, not that tension underneath. — **Did I get it? Or did I miss?**"

- **HIT 的样子**：自发、带情绪的认出（"yes — that's exactly what I could never say"）。
- **不要诱导**：用开放的"did I get it, or did I miss?"，给对方否定的空间；空洞的客气同意按 MISS 记。

### 3.3 Phase B — 引入一轮批评（EN，对象层，约 15–25 分钟）

明确换挡，把批评**显式地架在刚才的理解之上**（DP1）：

> "Okay — now I'm going to push on the idea itself, the way a reader who *doesn't* know you and isn't trying to be kind would. Not on you, on the claim. **[一条最锋利的对象层批评：最弱命题 / 缺失的失败条件 / 与既有理论是否只是重命名]**."

提出后，观察并记录反应：

> "How does that land? Does it make you want to walk away from it — or does it make you want to sharpen it?"

- **lean-in 信号**：追问、想立刻修订、要继续、主动补失败条件。
- **pull-away 信号**：退缩、防御、转而推销、脱离。
- **红旗**：表达"被否定 / 被打发"——说明批评没落在理解上，记下并复盘 §3.2/§3.3 的衔接。

### 3.4 会后（EN，5 分钟）
一句开放问题捕捉投入度信号：*"Would you want to keep going on this with us?"* —— 记录其回答与主动程度（是否反过来追问下一步、是否当场想约下次）。

---

## 4. 角色与防偏倚

- **访谈者**：跑 §3，不打分。
- **盲评者 ×2**（其一 = Review Editor）：独立从转录打 HIT/PARTIAL/MISS（§1.2），互不通气，且不知道对方分数。
- **防自我说服**：北极星由盲评者定，不由访谈者定（BP A.2 的核心方法论防线）。
- **防诱导**：命门话术保留否定空间（§3.2）；副门看真实行为（追问/约下次），不看口头客气。

---

## 5. 数据捕捉表（每位参与者一份，可直接复制）

```text
Participant ID:            P0_
Source material received:  [link/file]   Read before session: [Y/N]

— Phase A: Tension layer —
protected_value:           ____________________________________________
competing_pressures:       ____________________________________________
current_misread_object:    ____________________________________________
rounds to stable tension:  ____

— Confirmation (命门) —
Verbatim author reaction:  "________________________________________"
Rater A:  HIT / PARTIAL / MISS      Rater B:  HIT / PARTIAL / MISS
Counts as HIT (both HIT)?:  [Y/N]

— Phase B: Critique introduced —
Critique used (object layer): _______________________________________
Reaction:  LEAN-IN / PULL-AWAY      Red flag (felt condemned)?: [Y/N]
Verbatim: "________________________________________"

— Post —
"Keep going?" answer + proactivity: _________________________________
Notes for protocol iteration: ______________________________________
```

**汇总判定（全部会话跑完后）**

```text
Completed sessions:  N = ___
HITs (both raters):  ___    → 主门阈值（N=3→3, N=4→3, N=5→4）: PASS / FAIL
Among HITs: LEAN-IN ___ vs PULL-AWAY ___ ; red flags ___
  → 副门（lean-in 严格多于 pull-away 且红旗=0）: PASS / FAIL

GATE 0:  PASS（→ Gate 1 建 alpha P0） / FAIL（→ 迭代 §3 协议，不建平台）
```

---

## 6. 决策规则（与 PRD §11 对齐）

| 结果 | 含义 | 下一步 |
|---|---|---|
| 两门皆 PASS | 单点赌注成立，理解+批评可共存 | 解锁 **Gate 1**：构建 alpha 的 P0（PRD §7 各表 P0 项 + §8 治理 P0） |
| 主门 FAIL | 张力挖掘还不稳 | 迭代 §3 访谈脚本 / 模型提示词，重跑 Gate 0；**不建平台** |
| 主门 PASS、副门 FAIL | 能被看穿，但批评把人推走 | 重做 §3.3 批评的时序与措辞，重跑；**不建平台** |

---

## 7. 工具与成本

- **工具**：前沿模型（对齐 PRD FR-INT-04 / §9.4，张力层不降级）+ 录音转录 + 本打分表。无需平台、无需写代码。
- **成本**：3–5 场会话的时间 + 少量 LLM 调用；这是全项目性价比最高的一次支出——它在写第一行平台代码前就回答了"这产品该不该存在"。

---

## 8. 伦理与照护边界（DP7 / BP A.9）

平台会系统性吸引"理论"与"心理状态"高度缠绕的作者。本实验同样守边界：

- 对**内容**做张力翻译与批评；对**作者本人**不做心理判断、不诊断、不干预。
- 涉自我状态类主张时，既**不背书**也**不病理化**，只保持为"关于经验的可讨论对象"。
- 这既是伦理底线，也是法律与品牌底线。

---

## 9. 时间表（嵌入 BP §17 的 0–30 天）

| 天 | 动作 |
|---|---|
| D1–3 | 定稿 §1 阈值与 §3 脚本；两名盲评者就 HIT/PARTIAL/MISS 校准（用 1 段样例转录对齐口径） |
| D3–10 | opt-in 招募，确认 3–5 位理想峰参与者，发知情同意 |
| D8–20 | 跑 3–5 场会话，转录 |
| D18–25 | 双盲打分、汇总、判定 |
| D25–30 | 出结论：PASS → 起草 Gate 1 构建计划；FAIL → 迭代协议并安排重跑 |
