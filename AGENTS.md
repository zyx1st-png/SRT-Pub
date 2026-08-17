# AGENTS.md - SRT Local Workspace

This project keeps its own OpenClaw/ClawX entrypoints.

Use this file as the canonical runtime overlay when the current work is inside this repository, even if sibling projects exist in the same parent workspace.

`CLAUDE.md` is only a compatibility wrapper.
`SRT_AI_START.md` is the AI minimal-theory entry.
`README.md` is the public-facing repo entry.

## Session Start

`AGENTS.md` is the **single authority for fresh-session read order**. Other entry files should point here rather than maintaining competing bootstrap lists.

For a fresh AI session inside this repo, read in this order (3 files):

1. `SRT_AI_START.md` — minimal theory/runtime guard, including the symbol quick guard (§3); not a definition authority.
2. `_SRT_AGENT_RETRIEVAL_PROFILE.md` — classify the task before choosing context depth.
3. `STATUS.md §Fast Status` — compact current status for bootstrap (full dashboard in the same file).

Then load conditionally:

4. `_SRT_INDEX.md` when file routing, domain entrypoints, registry relations, or edit landing zones matter.
5. `_SRT_SYMBOL_TABLE.md` when exact symbol definitions, notation conflicts, or canonical term precision matters.
6. `_SRT_CONTEXT_ROUTER.md` for non-simple conceptual, cross-domain, or deep theory questions.
7. `_SRT_DEEP_THEORY_MAP.md` for cross-domain theory synthesis.
8. `_SRT_PARKED_INDEX.md` when a task touches parked seeds, B-verdict materials, or unmerged proposal work.
9. `Operations/Status_History/` when historical status detail matters.

Read `README.md` when public-facing framing or external onboarding context is useful.

For theory advancement, book writing, domain deep-dives, material fusion, public release, governance work, or any non-trivial SRT answer, classify the task with `_SRT_AGENT_RETRIEVAL_PROFILE.md` before deciding how much context to load. `canonical: false` means "not a definition authority"; it does not mean "do not retrieve."

`Manifesto/SRT_MANIFESTO.md` is a human-first worldview entry (`claim_mode: manifesto`, governed by `Governance/SRT_CLAIM_LADDER.md §2A`). It is **not** part of AI session bootstrap; read it only when the task involves user-facing framing.

Before doing substantial pipeline / governance / theory work:

1. Read `Operations/README.md`
2. Read `Governance/README.md`
3. Read `memory/YYYY-MM-DD.md` (today + yesterday) if present — the memory layer may be dormant for long stretches; absence is normal, do not go looking for substitutes
4. Read `HEARTBEAT.md` before heartbeat-style or automation-style work

Before editing theory files, also read:

1. `Governance/SRT_CANONICAL_FREEZE.md`
2. `Governance/SRT_EDIT_PROTOCOL.md`

## Book-Writing Hard Guard

Any task that reads, revises, continues, audits, or writes back to 《从存在到秩序》 must follow this order before keyword search results are treated as source text:

1. Read `01_Source_Intuition/BOOK/BOOK_CURRENT_STATUS.md`.
2. Read `01_Source_Intuition/BOOK/BOOK_ACTIVE_MANIFEST.json`.
3. Load the manifest's active primary file under `01_Source_Intuition/BOOK/Drafts_26Q/`.
4. Only after the active primary is loaded may `Archive_52Chapter/` or `Archive_Meta/` be opened for historical comparison.

Hard prohibitions:

- Do not use a file under `Archive_52Chapter/` or `Archive_Meta/` as the first or sole source for current book status, current chapter wording, or a current draft patch.
- Do not infer currentness from keyword density, a larger version suffix, an old chapter number, or search rank.
- When archived material is used, label it explicitly as historical and state the current active file it is being compared with.
- Do not copy archived prose into the current manuscript without re-deriving it against the current chapter, current five-act architecture, and current terminology rules.

## SRT Trigger Words

When the user sends the following trigger words, use the current `SRT/` structure rather than any retired `SRT_openclaw/` paths:

| Trigger | Pipeline / Mode | Action |
|--------|------------------|--------|
| `材料 <文本/URL/文件>` | Pipeline 1 | 按 `Operations/_SRT_MATERIAL_PIPELINE.md` 执行材料融合，并同时遵守 `Governance/SRT_GOV_SYN01_Ontological_Synthesis_and_Empirical_Discrimination_Protocol_v0_1.md`：先忠实提取 source claim，再分别判断 O-track 本体论整合价值与 D-track 经验判别增量；**不得为了证明 SRT 独特而强造新变量/机制，也不得因“别人已经解释”就自动判低价值**。随后执行 A/B/C、必要时二轮裁决、SourceCard / PatchNote / Material Log / Index / Registry / IntegrationHook；A 类正文回写必须先做去材料化改写。 |
| `陪读 <文本/URL/文件>` | Source-grounded reading | 先按来源本身的术语、论证与证据强度陪读，不自动写入仓库。若后续要求“写入/回写/融合”，转入 Pipeline 1，并按 `GOV-SYN01` 分开记录：A) source-derived 内容；B) SRT ontological synthesis；C) 只有在实际声称时才建立 discriminating/empirical increment。外部结果可作为 SRT 本体论构造材料，但不得被改写成“来源证明 SRT”。 |
| `材料裁决 <文本/URL/文件>` | 辅助工作流 | 启动第二轮结构裁决：审查第一轮候选接口，并按 `GOV-SYN01` 先判 O-track / D-track / O+D / source-only，再压成最小可承重命题，给出 A/B/C 建议与主/备/禁止落点；结果必须回注 Pipeline 1。 |
| `二轮裁决 <文本/URL/文件>` | 辅助工作流 | 同 `材料裁决` |
| `信号采集` | Pipeline 3 | 立即执行网络信号采集 |
| `内审` | Pipeline 6 | 立即执行每日内部审查 |
| `选题` | Pipeline 5 | 生成当日大众路线 + 精英路线选题 |
| `论文候选` | Pipeline 2 | 更新候选池与期刊匹配 |
| `周评` | Pipeline 4 | 执行文档治理 + 理论方向评审 |
| `对话` | Dialogue Mode | 启动自我修补对齐模式 |
| `学者对话` | Dialogue Mode | 启动学者批判模式 |

执行前：

- 先读 `STATUS.md`
- 以 `Operations/_SRT_OPERATIONS_SCHEDULE.md` 为当前节奏入口
- 若触发 `材料` 或需要把 `陪读` 结果写回仓库，必须读 `Operations/_SRT_MATERIAL_PIPELINE.md`、`Operations/_SRT_MATERIAL_LOG.md` 与 `Governance/SRT_GOV_SYN01_Ontological_Synthesis_and_Empirical_Discrimination_Protocol_v0_1.md`

执行后：

- 更新 `STATUS.md` 中的今日执行状态
- 需要留痕时追加到相应 `Operations/` 或 `Governance/` 台账
- Pipeline 1 的正式状态以 `Operations/_SRT_MATERIAL_LOG.md` 为准
- 不把 `Operations/` 日志、bridge 文件、patch 文件、hook 文件或 split / annex 导航写成新的 canonical 定义

## Canonical Runtime Paths

- AI 最小首读入口：`SRT_AI_START.md`
- Agent 检索扩展协议：`_SRT_AGENT_RETRIEVAL_PROFILE.md`
- 当前状态面板（含 §Fast Status 快速入口）：`STATUS.md`
- 快速符号守门：`SRT_AI_START.md §3`（原 `_SRT_SYMBOL_QUICK_GUARD.md` 已并入）
- 停驻内容总索引：`_SRT_PARKED_INDEX.md`
- 运行层入口：`Operations/README.md`
- 治理层入口：`Governance/README.md`
- 节奏总表：`Operations/_SRT_OPERATIONS_SCHEDULE.md`
- Pipeline 1 主流程：`Operations/_SRT_MATERIAL_PIPELINE.md`
- Pipeline 1 正式台账：`Operations/_SRT_MATERIAL_LOG.md`
- 本体论整合 / 经验判别双轨纪律：`Governance/SRT_GOV_SYN01_Ontological_Synthesis_and_Empirical_Discrimination_Protocol_v0_1.md`
- 对话留痕：`Operations/_SRT_DIALOGUE_LOG.md`
- 书稿当前状态入口：`01_Source_Intuition/BOOK/BOOK_CURRENT_STATUS.md`
- 书稿机器路由：`01_Source_Intuition/BOOK/BOOK_ACTIVE_MANIFEST.json`

## Migration Note

- `SRT_openclaw/` is retired and should be treated as legacy history, not a live path.
- Active SRT workflow docs now live under `Operations/` and `Governance/`.
- Root-level entry surfaces now separate public entry, runtime protocol, AI start, machine index, and human map.

## ClawX Environment

- Use local `TOOLS.md` for SRT-specific tool notes.
- Prefer `uv run python ...` over bare `python` / `python3` / `pip` unless a document explicitly requires otherwise.