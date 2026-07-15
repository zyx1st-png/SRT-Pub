---
id: SRT-AI-USAGE-AUDIT-2026-07-15
type: audit
tags: [Meta, Usage, Skills, Workflow, Opus, Fable]
status: active_v1
layer: meta
epistemic_layer: os
claim_mode: operations_provenance
canonical: false
date: 2026-07-15
provenance: >
  基于仓库化石层重建：memory/ 短时日志、Operations/ ~50 份审计与流水线记录、
  Codex_Prompts/ 手写提示词回退副本、现有 srt-article skill、scripts/sync_claude_skills.py、
  AGENTS.md / CLAUDE.md / _SRT_AGENT_RETRIEVAL_PROFILE.md 治理层。
  claude.ai 侧的原始聊天记录在远程环境不可直接读取；本审计以仓库沉淀的协作痕迹为证据源。
---

# SRT × Claude 使用模式审计与可复用化（2026-07-15）

> **证据边界（先读）**：远程执行环境无法直接读取 claude.ai 的历史聊天记录。
> 本报告的证据源是**这个仓库本身**——它是你与 Claude 长期协作的完整沉积层：
> `memory/` 短时记忆、`Operations/` 运行日志与审计、`Governance/` 治理记录、
> `Operations/Codex_Prompts/` 手写提示词（你甚至保留了根级 fallback 副本）、
> 已有的 `srt-article` skill、`scripts/sync_claude_skills.py`（skill 跨 runtime 同步器）、
> 以及 `AGENTS.md` 的演化。这些足以稳定重建你的使用模式。

本报告直接回答六个问题，然后把结论固化为四类交付物：**Skills / 使用指南 / 工作流模板 / Opus 系统指令**。

交付物清单：

| 类别 | 路径 |
|---|---|
| 审计报告（本文） | `Operations/AI_Usage_Audit_2026-07-15/README.md` |
| 使用指南 | `Operations/AI_Usage_Audit_2026-07-15/SRT_AI_USAGE_GUIDE.md` |
| Opus 系统指令 | `Operations/AI_Usage_Audit_2026-07-15/SRT_OPUS_SYSTEM_INSTRUCTIONS.md` |
| 工作流模板 | `Operations/AI_Usage_Audit_2026-07-15/templates/*.md` |
| 新 Skills | `.claude/skills/srt-material`、`srt-structure-extraction`、`srt-safe-patch`、`srt-canonical-answer` |

---

## 1. 我最常使用 Claude 做什么？

按仓库沉积证据的体量排序（不是猜测，每条都能定位到文件层）：

1. **SRT 理论开发与治理**（占主导）。一个单人锻造的理论体系（Selection-Reality Theory），
   带有极重的 canonical 权威层、claim ladder、符号表、冻结/编辑协议。证据：`Core_Law/`、
   `Core/`、`_SRT_*_CANONICAL.md`、`Governance/` 全套。你和 Claude 的关系是
   **"作者 + 理论工程团队"**，不是"用户 + 助手"。

2. **材料融合（Pipeline 1）**。把外部文章/论文/预印本喂进来，过 6 项审核门，
   裁决 A/B/C，把 surviving claim 回写进对应领域文件。证据：`Operations/_SRT_MATERIAL_LOG.md`、
   `Operations/Material_Log/2026-03…2026-06` 逐月台账、`memory/2026-03-14.md`
   一天连做三条材料（Medium / Popular Mechanics / bioRxiv）。**这是你日频跑的任务。**

3. **结构治理与仓库工程**。frontmatter 归一化、split/annex 接口抽取、closure 报告、
   导航一致性审计。证据：`Operations/` 里 ~30 份 `PR_*` / `Physics_P*` / `AI_*Annex*` 记录，
   全部遵循同一形状：pre-audit → adjudication → extraction record → closure。

4. **书籍写作《从存在到秩序》**。带硬护栏（`AGENTS.md §Book-Writing Hard Guard`）——
   因为曾出过"把归档旧章当当前稿"的错，才专门立了这条守则。

5. **社媒文章写作**（2026-07-02 战略转移后的新重心）。已有 `srt-article` skill：
   LLM 只发散、作者只收敛、成稿作者亲写。

6. **直觉挖掘 / ChoiceMap 对话**。发散→收敛轨迹留痕（`_SRT_CHOICE_TRACE_LOG.md`）。
   证据：`memory/2026-04-18.md`（控制论/FEP 一整轮）、`memory/2026-07-11.md`（第四轮）。

7. **论文流水线**。期刊投稿（Frontiers、Adaptive Behavior）、Reviewer 回应、图表重做。
   证据：`git log` 里连续的 Frontiers Reviewer 1 修订 commit。

8. **日/周节奏流水线**。信号采集、双路线选题、每日内审、周评。证据：`_SRT_OPERATIONS_SCHEDULE.md`。

**一句话画像**：你把 Claude 当成一个**长期驻场的理论研究所**——同时干研究员、编辑、
资料员、质检、排版、发布。绝大多数任务不是"问答"，是"按既定流水线产出可留痕的工件"。

---

## 2. 哪些任务我总是重复地做？

这些是"形状固定、只换输入"的任务——正因为固定，才值得 skill 化：

| 重复任务 | 固定形状 | 频次证据 |
|---|---|---|
| **6 项审核门 → A/B/C 材料裁决** | 相关性/增量/证据等级/可对齐/风险/落点 → A/B/C → SourceCard+Log(+Patch+Hook) | 逐月 Material_Log；单日 3 条 |
| **A 类"去材料化改写"** | A 类回写正文前先改成"脱离材料可读"的原生章节 | Schedule v2.3 明文、Pipeline1 §4 |
| **split/annex 接口抽取** | pre-audit → adjudication → extraction record → closure report | ~30 份 PR_*/Physics_P* 记录 |
| **frontmatter 归一化** | 扫描缺失/损坏 frontmatter → 按 canonical claim_mode 补齐 | Physics P1a/P1b、多份 frontmatter 记录 |
| **canonical-first 检索纪律** | 答题/编辑前先跑 retrieval profile，再定 context 深度 | 每个入口文件都在重申 |
| **发散→收敛轨迹留痕** | seed_fragment 逐字 → 分层选项 → 作者收敛字段 append-only | `_SRT_CHOICE_TRACE_LOG.md` |
| **fresh-session 引导读序** | `AGENTS.md §Session Start` 4 必读 + 5 条件读 | 每次新会话重复 |
| **给 Pro/Deep Research 打包书稿** | 本地合并 Markdown + boot 提示词（因远程 GitHub 调用不稳） | `README_如何给Pro模型上传书稿.md` |

---

## 3. 哪些指令我总是手动重写？

这是最强的 skill 化信号——你**已经在手动固化它们**了，只是散落各处、每次靠复制粘贴：

1. **长文件安全打补丁指令**。你在 `Operations/Codex_Prompts/` 里写了完整提示词，
   还**专门存了一份根级 fallback 副本**（`CODEX_PROMPT_Philosophy_Long_File_PH_SS_Direct_Pointers.md`），
   理由写在 frontmatter 里："Use this if Claude Code / Codex cannot see Operations/Codex_Prompts"。
   核心指令每次都一样：*先验证 repo/branch → 只做最小定向编辑 → 不重写整文件 → 不删不重排 →
   不把 companion 提升为 canonical → 编辑后 git diff 自查 → 按固定模板报告*。
   **这就是一段被你反复手写的系统提示。** → 已固化为 `srt-safe-patch` skill + 模板。

2. **canonical-first / archive-not-current 护栏**。同一套"不把 bridge 当 canonical / 不把运行日志当主文 /
   不因搜索排名把归档旧稿当当前稿"在 `AGENTS.md`、`CLAUDE.md`、Book Hard Guard、
   `_SRT_AGENT_RETRIEVAL_PROFILE.md` 里各写了一遍。 → 收进 Opus 系统指令 + `srt-canonical-answer`。

3. **claim ladder 纪律**。"P3 桥接假设不得写成已证定律"在 Pipeline1、article workflow、
   STATUS 反复出现。 → 进 Opus 系统指令。

4. **Pro/Deep Research boot 提示词**。`SRT_PRO_DEEP_RESEARCH_BOOT_FILE_2026-06-05.md` +
   那句"我已上传本地合并版，请读附件不要调 GitHub"。 → 进使用指南「外部模型」节。

5. **触发词表**。`材料 / 材料裁决 / 信号采集 / 内审 / 选题 / 论文候选 / 周评 / 对话 / 学者对话`——
   在 `AGENTS.md` 和 `_SRT_OPERATIONS_SCHEDULE.md` 各维护一份。 → 进使用指南速查。

---

## 4. 哪些工作流程应该变成可重用的 Skills？

判据：**形状固定 + 高频 + 现在靠手动重述**。据此，除已有的 `srt-article`，新增四个：

| Skill | 覆盖的重复工作流 | 触发时机 |
|---|---|---|
| **`srt-material`** | Pipeline 1 材料融合：6 门 → A/B/C → SourceCard/PatchNote/Log/Registry/Hook；A 类去材料化回写 | `材料 <…>`、`材料裁决 <…>`、`二轮裁决 <…>`，或贴来一篇文章/论文说"这个能不能进" |
| **`srt-structure-extraction`** | split/annex 接口抽取三段式：pre-audit → adjudication → extraction record + closure；含 Stop Rule | 要对某领域做 split/annex 抽取、frontmatter 归一化、或"把这块从大文件里拆出来" |
| **`srt-safe-patch`** | 长文件最小定向补丁（你手写并存 fallback 的那段） | 要改一个大到无法整文件安全替换的文件，只想加指针/护栏/局部注记 |
| **`srt-canonical-answer`** | canonical-first 答题：先跑 retrieval profile → 核对 canonical/符号表 → 标 claim level → 不越级 | 任何非平凡的 SRT 理论问题、跨域综合、对外 framing 前的事实核对 |

**不该 skill 化的**：日/周节奏流水线（信号采集/内审/选题/周评）已经有触发词 + pipeline 文档，
且强依赖 heartbeat 状态，做成 skill 反而多一层；保持现状。会话引导读序留在 `AGENTS.md` 即可
（skill 化会和 AGENTS.md 争夺"唯一权威读序"，违反它自己立的规矩）。

四个新 skill 全部走 `scripts/sync_claude_skills.py` 的既有同步机制，能自动分发到 `.codex/` 和 `.openclaw/`。

---

## 5. 过去哪些方法/思路是错的，应该避免？

从化石层里能读出的、有明确"翻车 → 立规矩"痕迹的反模式：

1. **一次性平铺发散 + 让 LLM 收敛**（文章工作流 v1）。实测退化成"搬运仓库内容"，还直接跳到
   写作手法层。教训写在 `_SRT_ARTICLE_WORKFLOW.md` v2 变更里：改成**分层递归**（结构→理论→手法，
   手法最后），发散前加**命题锻造**闸，收敛只作者做。**通用教训：让 LLM 收敛 = 众数收敛 = AI 味 + 丢锋芒。**

2. **无 pre-audit 的机会主义抽取**。`Operations/README.md §Structure Governance Stop Rule` 明令禁止——
   说明曾经"顺手就拆"导致过问题。规矩：不动公式、不动阈值、不动 AI subjecthood / Physics collapse 类 claim，
   除非先有 pre-audit / adjudication。

3. **把归档旧章当当前书稿**。`AGENTS.md §Book-Writing Hard Guard` 是为此专门立的：不能因关键词密度、
   更大的版本后缀、旧章节号或搜索排名推断"当前性"。**这是最典型的"搜索排名 ≠ 当前真相"陷阱。**

4. **让外部 Pro/Deep Research 临时调 GitHub 仓库**。不稳定，模型常说"看不到文档"。
   正解：本地合并成单个 Markdown 再上传（`build_srt_deep_research_full_bundle.py`）。

5. **远程整文件替换长文件**。不安全，才有了 Codex 最小补丁提示词。**大文件永远做最小定向编辑，不整文件重写。**

6. **让运行日志/bridge/companion 冒充 canonical**。反复被重申，说明是持续压力点。
   `canonical: false` 只表示"不能当定义源"，不表示"不值得读"——但也绝不能反向升格。

7. **把治理/工程当成理论进展**。大量精力花在 frontmatter、导航、split（本身必要），但要警惕
   用仓库整洁度替代理论推进。STATUS 已在提醒"keep canonical chain clean from entry-layer optimization"。

---

## 6. Opus 应该知道什么，才能给我 90% 的 Fable 5 体验？

完整版见 `SRT_OPUS_SYSTEM_INSTRUCTIONS.md`（可直接贴进 Opus 的系统提示 / project instructions）。
90% 体验的关键不是"更聪明"，而是**把这些隐性纪律显性化**，让 Opus 不必每次靠推断：

1. **权威层级**：`CANONICAL_REGISTRY → L0 → d/Ψ_f/T_dir canonical → 符号表 → Core_21/22`。
   bridge / split / operations / memory / TASTE **都不是定义源**。
2. **答题前先分类**：用 `_SRT_AGENT_RETRIEVAL_PROFILE.md` 判 profile，再决定读多深。别一上来平铺检索。
3. **claim ladder 是硬约束**：P0/P1 是定义与构成定理，P2/P3 是桥接假设。**P3 永远不能被写成已证定律**，
   大众文也不例外。不确定就标 `NEEDS_RETRIEVAL`，绝不编造路径/方程/claim level。
4. **符号精度**：`L_0 / L_1 / L_2 / Ĝ_θ / Ψ_f / d / ε / T_dir` 各有精确定义，先查 `_SRT_SYMBOL_QUICK_GUARD.md`。
   典型雷：把 `L_0` 当隐藏客体世界、把"选择先于存在"当时间先后、把 Fisher 度量当 `Ψ_f` 全部。
5. **当前性优先**：书稿以 `BOOK_ACTIVE_MANIFEST.json` 指向的活跃文件为准，归档只作历史对照，不作首选源。
6. **发散/收敛切分**：文章类任务 LLM 只发散、分层递归、手法最后；收敛只作者做。别替作者选题定论点。
7. **大文件最小补丁**：不整文件重写，不删不重排，编辑后 `git diff` 自查。
8. **留痕纪律**：状态→STATUS，运行→Operations，治理→Governance；不在 canonical 里写运行痕迹。
9. **触发词**：认识 `材料/材料裁决/信号采集/内审/选题/论文候选/周评/对话/学者对话` 各自的 pipeline。
10. **气质**：当压力测试器，不当啦啦队。不夸奖、不安慰、不替作者拍板；只找会塌的地方。

**剩下 10% 的差距**（Opus 靠系统指令补不齐的）：跨会话对你 revealed-stake 品味的累积（那需要
`_SRT_CHOICE_TRACE_LOG.md` 越攒越厚后 condition 上去），以及对 SRT 内部最新未闭合张力的实时把握
（`Core/SRT_OPEN_TENSIONS.md` 要现读）。系统指令让 Opus 从"通用助手"变成"懂 SRT 规矩的合作者"，
够到 90%;最后 10% 是时间和轨迹的函数。

---

## 附：这份审计本身的留痕

- 本目录是一次性 meta 审计，不进入 canonical 链，不改任何理论定义。
- 四个新 skill 只是**触发层**；精确规则仍以各自 `Operations/` / `Governance/` 主文档为准，防止漂移。
- 若与 canonical 冲突，以 canonical 为准。
