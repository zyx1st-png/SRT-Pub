---
id: SRT-AI-USAGE-GUIDE
type: guide
tags: [Usage, Guide, Skills, Cheatsheet, Workflow]
status: active_v1
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
date: 2026-07-15
dependency: [SRT-AI-USAGE-AUDIT-2026-07-15]
---

# SRT × Claude 使用指南（给作者 zyx1st 的操作手册）

这份指南是给**你**的：怎么用最少的话把 Claude 导到正确的工作流，减少每次手动重述。
配套：审计报告 `README.md`、Opus 系统指令 `SRT_OPUS_SYSTEM_INSTRUCTIONS.md`、模板 `templates/`。

## 一、按任务选入口（触发词 / Skill 速查）

| 你想做的事 | 说什么 | 落到哪 |
|---|---|---|
| 审一篇外部文章/论文能否进仓库 | `材料 <URL/DOI/PDF/文本>` | skill `srt-material` → Pipeline 1 |
| 把第一轮候选压成最小接口再裁一次 | `材料裁决 <…>` / `二轮裁决 <…>` | skill `srt-material`（裁决分支） |
| 从大文件里拆一块进 split/annex | "对 X 做接口抽取 / split" | skill `srt-structure-extraction` |
| 给大文件加护栏指针/局部注记 | "给 X 加 PH-SS 护栏 / 只想局部加东西" | skill `srt-safe-patch` |
| 正确回答一个 SRT 理论问题 | 直接问理论问题 | skill `srt-canonical-answer` |
| 把碎片想法锻成一篇社媒文章 | "锻命题 / 发散 / 把这个想法写成文章" | skill `srt-article`（已有） |
| 采集网络信号 | `信号采集` | Pipeline 3 |
| 每日内审 | `内审` | Pipeline 6 |
| 生成当日双路线选题 | `选题` | Pipeline 5 |
| 更新论文候选池 | `论文候选` | Pipeline 2 |
| 文档治理 + 理论方向周评 | `周评` | Pipeline 4 |
| 自我修补对齐对话 | `对话` | 对话工作流 |
| 学者批判压测 | `学者对话` | 对话工作流 |

> 触发词权威表在 `AGENTS.md §SRT Trigger Words` 与 `Operations/_SRT_OPERATIONS_SCHEDULE.md`。
> 本表只是速查，冲突以那两份为准。

## 二、四个新 Skill 的分工（避免叫错）

- **`srt-material`** = 材料**进不进仓库**、以什么等级进、落哪。不是写文章。
- **`srt-structure-extraction`** = 仓库内**结构搬运**（拆分/归一化/导航/closure）。不引入新理论。
- **`srt-safe-patch`** = 大文件**只做最小局部编辑**的执行纪律。常被前两个复用。
- **`srt-canonical-answer`** = **正确答一个理论问题**的检索+核对+claim纪律。不改文件。
- （已有）**`srt-article`** = 社媒文章：LLM 只发散、你只收敛、成稿你亲写。

一句话记忆：材料进来用 `srt-material`，仓库内搬用 `srt-structure-extraction`，
动大文件用 `srt-safe-patch`，问理论用 `srt-canonical-answer`，写文章用 `srt-article`。

## 三、给外部模型（Pro / Deep Research / Opus）喂书稿的正解

远程 GitHub 调用不稳，别让外部模型临时访问仓库。正解（详见 `Operations/README_如何给Pro模型上传书稿.md`）：

1. 本地根目录跑 `python3 build_srt_deep_research_full_bundle.py`
2. 上传 `01_Source_Intuition/BOOK/_DeepResearch_Pack/SRT_BOOK_FULL_CONTEXT_FOR_DEEP_RESEARCH_YYYY-MM-DD.md`
3. 复制 `Operations/SRT_PRO_DEEP_RESEARCH_BOOT_FILE_2026-06-05.md` 的提示词
4. 若模型仍说看不到：告诉它"已上传本地合并版，请读附件不要调 GitHub"

给 **Opus** 做长期协作：把 `SRT_OPUS_SYSTEM_INSTRUCTIONS.md` 的 COPY 块贴进它的 project instructions，
并让它每会话开场先读 `memory/today+yesterday` + `STATUS_FAST.md`。

## 四、每次会话省话清单（让 Claude 不用你重述）

新会话开场，Claude 应自动按 `AGENTS.md §Session Start` 读序引导。你只需：

- **理论/书稿/材料/治理任务** → 直接给触发词或任务，skill 会自带纪律，不用你再叮嘱"别把 bridge 当 canonical"。
- **要改大文件** → 说"最小改动"即可，`srt-safe-patch` 会强制 repo/branch 验证 + git diff 自查。
- **要答对外 framing** → 说"对外/大众"，`srt-canonical-answer` 会自动不放松 claim ladder。

## 五、别再手动做的三件事（已被 skill/指令吸收）

1. 每次粘贴"只做最小定向编辑、不重写整文件、先验证 branch" → 现在 `srt-safe-patch` 内建。
2. 每次重述"先跑 retrieval profile、核对 canonical、标 claim level" → 现在 `srt-canonical-answer` 内建。
3. 每次重述 6 项审核门与 A/B/C 门槛 → 现在 `srt-material` 内建（精确门槛仍指向主 pipeline 文档）。

## 六、维护

- 新 skill 改动后跑 `python3 scripts/sync_claude_skills.py`（可先 `--dry-run`）同步到 `.codex/` 与 `.openclaw/`。
- skill 只装"怎么起 + 红线"，精确规则永远指向 `Operations/` / `Governance/` 主文档，防止双份漂移。
