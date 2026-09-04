# AGENTS.md - SRT Local Workspace

This project keeps its own OpenClaw/ClawX entrypoints.

Use this file as the canonical runtime overlay when the current work is inside this repository, even if sibling projects exist in the same parent workspace.

`CLAUDE.md` is only a compatibility wrapper.
`SRT_AI_START.md` is the AI minimal-theory entry.
`README.md` is the public-facing repo entry.

## Session Start

`AGENTS.md` is the **single authority for fresh-session read order**. Other entry files should point here rather than maintaining competing bootstrap lists.

For a fresh AI session inside this repo, read in this order (3 files):

1. `SRT_AI_START.md` — minimal theory/runtime guard; not a definition authority.
2. `_SRT_AGENT_RETRIEVAL_PROFILE.md` — classify the task before choosing context depth.
3. `STATUS.md §Fast Status` — compact current status and current programme identity.

### Current programme expansion — Constitution + Domain Reconstruction

For **theory advancement, source-intuition recovery, Constitution work, Core/Core_Law role questions, or a new domain deep-dive**, after the 3-file bootstrap above read:

4. `Operations/Proposals/SRT_CONSTITUTION_DOMAIN_ARCHITECTURE_V2_2026-09-04.md` — active post-Constitution architecture.
5. `Operations/Proposals/SRT_CONSTITUTION_DOMAIN_RECONSTRUCTION_BLUEPRINT_2026-08-29.md` — compact historical/identity blueprint.
6. `Operations/Proposals/SRT_CONSTITUTION_DOMAIN_EXECUTION_PLAN_2026-08-29.md` — execution plan as amended by Architecture v2.
7. `Operations/Templates/SRT_DOMAIN_RECONSTRUCTION_FRAMEWORK_TEMPLATE.md` for new/backfilled domain work.
8. `Governance/SRT_GOV_CONSTITUTION_DOMAIN_RECONSTRUCTION_2026-08-29.md`.
9. `Operations/Proposals/SRT_CONSTITUTION_SOURCE_RECOVERY_MAP_2026-08-29.md` when recovering existing SRT intuition rather than answering a narrow factual question.

Current identity guard:

```text
SRT Constitution
= bearer-involved perspective framework

Domain Reconstruction Framework
= Constitution × domain starting picture × inherited SRT assets × materials
  -> problem-space / objectification / bearer-position / problem families / deep-well queue

Domain Theory / Hypothesis / Model
= mechanisms / formalisms / proxies / candidate explanations

Deep Well / Evidence
= bounded test / strongest baseline / Case A-B-C / data / proof / archive
```

Do not restart the older `unified ontology -> local formalization -> D2` sequence as the active programme merely because older proposal files contain it. Do not redesign SRT's identity again before the current identity-freeze reopen conditions are met.

Then load conditionally:

8. `_SRT_INDEX.md` when file routing, domain entrypoints, registry relations, or edit landing zones matter.
9. `_SRT_SYMBOL_TABLE.md` when exact symbol definitions, notation conflicts, or canonical term precision matters.
10. `_SRT_CONTEXT_ROUTER.md` for non-simple conceptual, cross-domain, or deep theory questions.
11. `_SRT_DEEP_THEORY_MAP.md` for cross-domain theory synthesis.
12. `_SRT_PARKED_INDEX.md` when a task touches parked seeds, B-verdict materials, or unmerged proposal work.
13. `Operations/Status_History/` when historical status detail matters.

Read `README.md` when public-facing framing or external onboarding context is useful.

For theory advancement, book writing, domain deep-dives, material fusion, public release, governance work, or any non-trivial SRT answer, classify the task with `_SRT_AGENT_RETRIEVAL_PROFILE.md` before deciding how much context to load. `canonical: false` means "not a definition authority"; it does not mean "do not retrieve."

`Manifesto/SRT_MANIFESTO.md` is a human-first worldview entry (`claim_mode: manifesto`). It is not part of AI session bootstrap; read it only when the task involves user-facing framing or source recovery.

Before doing substantial pipeline / governance / theory work:

1. Read `Operations/README.md`
2. Read `Governance/README.md`
3. Read `memory/YYYY-MM-DD.md` (today + yesterday) if present — absence is normal
4. Read `HEARTBEAT.md` before heartbeat-style or automation-style work

Before editing theory files, also read:

1. `Governance/SRT_CANONICAL_FREEZE.md`
2. `Governance/SRT_EDIT_PROTOCOL.md`

### Frontmatter write ratchet

For any **new or substantially edited ordinary Markdown file**, use one of the repository ratchet status values:

```text
draft | active | frozen | archived
```

Do not invent versioned status strings such as `active_v2` or `superseded_input`; put finer lifecycle meaning in a separate field such as `record_stage`. Explicit noncanonical transcript/source-record exceptions are governed by `scripts/check_frontmatter.py`; do not generalize those exceptions to ordinary theory/governance files.

## Constitution Dialogue Hard Guard

For Constitution work, the default workflow is:

```text
existing source recovery
-> AI divergence
-> Light Neighbor Awareness (read-only; no gate; no repo artifact by default)
-> author convergence
-> repository write
-> internal reflexivity/circularity red-team
-> Full Neighbor Map
-> author second adjudication
-> Constitution freeze
```

Hard rules:

- **No theory write before author convergence.** AI may retrieve and present options, but should not create a Constitution artifact for every live branch.
- AI-generated alternatives are not author decisions.
- Two models agreeing is corroboration, not proof and not author convergence.
- **When mature-domain overlap, neighbor comparison, or cross-domain mapping is in play, use cross-domain ontological unification (U-mode) rather than domain-local novelty maximization; tasks that raise no such question remain in their native task mode and must not be widened merely to manufacture cross-domain mappings. Switch to novelty/increment subtraction (N-mode) only when the active task explicitly requires it.**
- Do not use novelty/prior-art as a permission gate before the author knows what they mean.
- **Light Neighbor Awareness** occurs before convergence only to reduce avoidable rediscovery and improve terminology/problem precision; it is read-only, bounded, does not score novelty, does not recommend keep/drop, and creates no repository artifact by default.
- **Full Neighbor Map** occurs only after convergence and internal red-team; it uses `resonance / contrast / pressure / translation / realization` for comparative positioning and external legibility, not permission to think.
- Constitution substantive items should have a `reader-entry operation`; pure worldview propositions without an executable perspective move belong in commentary unless the author decides otherwise.
- Constitution must not use equations/scalars/thresholds/state-space formalisms as constitutional authority.
- Domain formalization is allowed and encouraged when the domain declares its objectification assumptions.

Use `Operations/_SRT_CHOICE_TRACE_LOG.md` / ChoiceMap discipline for author convergence when practical. AI may record option sets; author choice, skipped mode, reason and closure boundary must not be invented by AI.

## Book-Writing Hard Guard

Any task that reads, revises, continues, audits, or writes back to 《从存在到秩序》 must follow this order before keyword search results are treated as source text:

1. Read `01_Source_Intuition/BOOK/BOOK_CURRENT_STATUS.md`.
2. Read `01_Source_Intuition/BOOK/BOOK_ACTIVE_MANIFEST.json`.
3. Load the manifest's active primary file under `01_Source_Intuition/BOOK/Drafts_26Q/`.
4. Only after the active primary is loaded may `Archive_52Chapter/` or `Archive_Meta/` be opened for historical comparison.

Hard prohibitions:

- Do not use archived book material as the first or sole source for current wording.
- Do not infer currentness from keyword density, version suffix, chapter number, or search rank.
- When archived material is used, label it historical and name the current active file.
- Do not copy archived prose into the current manuscript without re-deriving it against the current architecture and terminology.

For Constitution source recovery, the current 26Q book is a **source-intuition reservoir**, not automatic canonical authority. Extract perspective operations and author intuitions; do not promote vivid prose directly into Constitution.

## SRT Trigger Words

When the user sends the following trigger words, use the current `SRT/` structure rather than retired `SRT_openclaw/` paths:

| Trigger | Pipeline / Mode | Action |
|--------|------------------|--------|
| `材料 <文本/URL/文件>` | Pipeline 1 | 按 `Operations/_SRT_MATERIAL_PIPELINE.md` 执行材料融合，并遵守 `Governance/SRT_GOV_SYN01_Ontological_Synthesis_and_Empirical_Discrimination_Protocol_v0_1.md`。先忠实提取 source claim，再区分 Constitution resonance/contrast/pressure、domain mechanism/constraint 与真正 D-track increment。不得把来源写成“证明 Constitution”。 |
| `陪读 <文本/URL/文件>` | Source-grounded reading | 先按来源本身术语、论证与证据强度陪读，不自动写仓库。若后续要求写回，再转 Pipeline 1。 |
| `材料裁决 <文本/URL/文件>` | 辅助工作流 | 审查第一轮候选接口，区分 source-native fact / Constitution relevance / domain relevance / D-track increment；结果回注 Pipeline 1。 |
| `二轮裁决 <文本/URL/文件>` | 辅助工作流 | 同 `材料裁决`。 |
| `推演回流 <对话/片段>` | 辅助工作流 | 外部模型理论推演回流。当前 Constitution programme 下，优先恢复 author choice / unresolved branch / pressure point；对话本身不建 SourceCard，其中真正承担证据的外部论文需拆出进 Pipeline 1。 |
| `信号采集` | Pipeline 3 | 立即执行网络信号采集 |
| `内审` | Pipeline 6 | 立即执行每日内部审查 |
| `选题` | Pipeline 5 | 生成当日大众路线 + 精英路线选题 |
| `论文候选` | Pipeline 2 | 更新候选池与期刊匹配 |
| `周评` | Pipeline 4 | 执行文档治理 + 理论方向评审 |
| `对话` | Dialogue Mode | 启动作者发散/收敛对齐模式；若触及 Constitution，遵守 Constitution Dialogue Hard Guard |
| `学者对话` | Dialogue Mode | 启动学者批判 / red-team 模式 |

执行前：

- 先读 `STATUS.md`
- 以当前 Constitution execution plan 作为 theory-development programme；日常节奏继续参考 `Operations/_SRT_OPERATIONS_SCHEDULE.md`
- 材料写回必须读 Material Pipeline、Material Log 与 GOV-SYN01

执行后：

- 更新 `STATUS.md` 中的当前执行状态（需要时）
- 需要留痕时追加到相应 Operations/Governance 台账
- Pipeline 1 正式状态以 `Operations/_SRT_MATERIAL_LOG.md` 为准
- 不把 Operations 日志、bridge、patch、hook、split/annex 导航写成新的 Constitution 或 canonical definition

## Canonical Runtime Paths

- AI 最小首读入口：`SRT_AI_START.md`
- Agent 检索扩展协议：`_SRT_AGENT_RETRIEVAL_PROFILE.md`
- 当前状态面板：`STATUS.md`
- 当前 programme blueprint：`Operations/Proposals/SRT_CONSTITUTION_DOMAIN_RECONSTRUCTION_BLUEPRINT_2026-08-29.md`
- 当前 programme plan：`Operations/Proposals/SRT_CONSTITUTION_DOMAIN_EXECUTION_PLAN_2026-08-29.md`
- 当前 programme governance：`Governance/SRT_GOV_CONSTITUTION_DOMAIN_RECONSTRUCTION_2026-08-29.md`
- Constitution source recovery：`Operations/Proposals/SRT_CONSTITUTION_SOURCE_RECOVERY_MAP_2026-08-29.md`
- 作者身份源记录：`01_Source_Intuition/SRT_CONSTITUTION_IDENTITY_AUTHOR_TRACE_2026-08-29.md`
- 停驻内容总索引：`_SRT_PARKED_INDEX.md`
- 运行层入口：`Operations/README.md`
- 治理层入口：`Governance/README.md`
- 节奏总表：`Operations/_SRT_OPERATIONS_SCHEDULE.md`
- Pipeline 1：`Operations/_SRT_MATERIAL_PIPELINE.md`
- Material Log：`Operations/_SRT_MATERIAL_LOG.md`
- Choice trace：`Operations/_SRT_CHOICE_TRACE_LOG.md`
- 书稿当前状态：`01_Source_Intuition/BOOK/BOOK_CURRENT_STATUS.md`
- 书稿机器路由：`01_Source_Intuition/BOOK/BOOK_ACTIVE_MANIFEST.json`

## Migration Note

- `SRT_openclaw/` is retired and should be treated as legacy history.
- Active workflow docs live under `Operations/` and `Governance/`.
- The 2026-08-29 Constitution reconstruction is prospective: it does not silently rewrite published/submitted manuscripts or frozen canonical owners.

## ClawX Environment

- Use local `TOOLS.md` for SRT-specific tool notes.
- Prefer `uv run python ...` over bare `python` / `python3` / `pip` unless a document explicitly requires otherwise.
