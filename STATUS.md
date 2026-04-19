---
id: SRT-STATUS
type: dashboard
tags: [Status, Dashboard, SessionEntry]
status: active_v2
layer: meta
epistemic_layer: os
claim_mode: evidence
dependency: [SRT-OPERATIONS-SCHEDULE]
---

# SRT 当前状态仪表盘

> **角色**：当前状态面板，不再承担完整历史档案。
> **最后更新**：2026-04-19
> **完整历史**：`Operations/_SRT_STATUS_HISTORY.md`
> **年度变更摘要**：`Governance/_SRT_CHANGELOG_2026.md`

## 当前仓库状态

- 根目录已在 `2026-04-15` 完成平铺，当前 `main` 直接对应 SRT 主树内容。
- 远端已收口为单一 `main` 分支。
- 仓库正在执行一轮入口层与 harness 收口，目标是降低 AI 首读成本、明确权威关系、降低运行噪声权重。

## 当前建议首读顺序

AI / agent 最短读法：

1. `AGENTS.md`
2. `SRT_AI_START.md`
3. `STATUS.md`
4. `_SRT_INDEX.md`
5. `_SRT_SYMBOL_TABLE.md`

进入具体 pipeline / 治理工作时，再补读：

- `Operations/README.md`
- `Governance/README.md`
- `memory/YYYY-MM-DD.md`（today + yesterday）

## 当前权威锚点

- L0 唯一锚点 → `Core_Law/SRT_L0_Metaphysics.md`
- d-value canonical → `_SRT_D_VALUE_CANONICAL.md`
- `Ψ_f` canonical → `_SRT_PSI_F_CANONICAL.md`
- `T_dir` canonical → `_SRT_T_DIR_CANONICAL.md`
- 符号规范 → `_SRT_SYMBOL_TABLE.md`
- formal axioms → `Core/SRT_Core_21_Formal_Axioms.md`
- master equations → `Core/SRT_Core_22_Equations.md`

## 最近关键推进

- `2026-04-19`：已将 `Philosophy/SRT_Philosophy_Ethics_Integration_2026_04_19.md`（主体位、d 增厚、新预期形成）回写并入 `Philosophy/SRT_Philosophy_Ethics.md`，源文件降权为 `archival_index`，`SRT_Merged_Provenance_Index.md` 已更新留痕。
- `2026-04-18`：已新增 `README.md`、`CLAUDE.md`、`Governance/SRT_CANONICAL_FREEZE.md`、`Governance/SRT_EDIT_PROTOCOL.md`、`Governance/SRT_HARNESS_TESTS.md`，并开始收口入口层、manifest 与运行层边界。
- `2026-04-16`：已收紧 `relative existence / L2 convergence` 相关口径，并回写主文与哲学接口。
- `2026-04-15`：已把 `d-value` 的治理层 canonical 锚点收口到 `_SRT_D_VALUE_CANONICAL.md`。
- `2026-04-14`：已完成多批材料审查与若干神经/节律相关机制窗口的回写。

## 当前高优先事项

- 完成入口层去重：`README / AGENTS / CLAUDE / STATUS / _SRT_INDEX / Navigation / manifest`
- 保持 canonical 主链不被入口优化反向污染
- 继续把运行留痕与理论检索层分开

## Pipeline 快照

- `Pipeline 1`：材料融合主流程继续有效；二轮结构裁决走 `Operations/_SRT_MATERIAL_ADJUDICATION_WORKFLOW.md`
- `Pipeline 3`：信号采集按 `Operations/_SRT_OPERATIONS_SCHEDULE.md` 执行
- `Pipeline 6`：内审按 `Operations/_SRT_OPERATIONS_SCHEDULE.md` 执行

## 当前工作边界

- 本轮先做入口、索引、协议、归档与运行层降权
- 暂不大规模改正文主链
- 理论文件编辑先看 `Governance/SRT_CANONICAL_FREEZE.md` 与 `Governance/SRT_EDIT_PROTOCOL.md`
