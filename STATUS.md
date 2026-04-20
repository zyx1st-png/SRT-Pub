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
> **最后更新**：2026-04-20
> **完整历史**：`Operations/_SRT_STATUS_HISTORY.md`
> **年度变更摘要**：`Governance/_SRT_CHANGELOG_2026.md`

## 当前仓库状态

- 根目录已在 `2026-04-15` 完成平铺，当前 `main` 直接对应 SRT 主树内容。
- 远端已收口为单一 `main` 分支。
- 仓库已执行一轮“理论硬化优先、去命题混层”回写：`Core_21` 已拆成 P0/P1/P2-P4 分层，AI 首读入口已降密度为 runtime/bootstrap。
- 当前后续重点是让 domain 文件持续回链 canonical，避免 bridge / companion / lab 命题反向冒充 core。

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
- claim ladder → `Governance/SRT_CLAIM_LADDER.md`
- d-value canonical → `_SRT_D_VALUE_CANONICAL.md`
- `Ψ_f` canonical → `_SRT_PSI_F_CANONICAL.md`
- `T_dir` canonical → `_SRT_T_DIR_CANONICAL.md`
- 符号规范 → `_SRT_SYMBOL_TABLE.md`
- formal axioms → `Core/SRT_Core_21_Formal_Axioms.md`
- P0 minimal axioms → `Core/SRT_Core_21_Minimal_Axioms.md`
- P1 constitutive theorems → `Core/SRT_Core_21b_Constitutive_Theorems.md`
- P2/P3/P4 bridge hypotheses → `Core/SRT_Core_21c_Bridge_Hypotheses.md`
- master equations → `Core/SRT_Core_22_Equations.md`
- open tensions → `Core/SRT_OPEN_TENSIONS.md`

## 最近关键推进

- `2026-04-20`：Pipeline 1 处理 Science and Culture 关于纪录片 *The Story of Everything* 的宣传性评论；判定为 C 类不融入正文，因其把宇宙开端、fine-tuning、DNA code 与 beauty 组合成 intelligent design / theism 解释链，但未提供新的同行评审锚点、机制变量或可证伪窗口；已在 `Operations/_SRT_MATERIAL_LOG.md` 留痕。
- `2026-04-20`：Pipeline 1 处理 JCS 2026 关于 spacetime emergence 与 consciousness emergence 是否同源的评论文；判定为 A 类小回写，已在 `Core/SRT_Core_21c_Bridge_Hypotheses.md` 的 holographic duality 边界中加入 pressure note，防止强 bridge 被误用为 P0/P1 或把物理涌现与意识涌现压成同一证明动作。
- `2026-04-20`：Pipeline 1 处理 ML Chen Substack 关于 premature requiem for philosophy 的提交；判定为 C 类不融入正文，因其主要加固现有 `Philosophy/SRT_Philosophy_Foundations.md` 的哲学功能口径，但未形成新的稳定理论接口；已在 `Operations/_SRT_MATERIAL_LOG.md` 留痕。
- `2026-04-20`：Pipeline 1 处理 Neuroscience News / Cedars-Sinai 关于 visual imagination shared neural code 的提交；判定为既有 `Ventral-Temporal Shared Imagery Code patch` 的来源升级而非新接口，已补强 `Neuroscience/SRT_Neural_Mechanisms.md` 的公开摘要级细节，并在 `Operations/_SRT_MATERIAL_LOG.md` 留痕。
- `2026-04-20`：完成“理论硬化优先、去命题混层”回写：`Core/SRT_Core_21_Formal_Axioms.md` 改为 claim-layer index；新增 `Core/SRT_Core_21_Minimal_Axioms.md`（P0）、`Core/SRT_Core_21b_Constitutive_Theorems.md`（P1）、`Core/SRT_Core_21c_Bridge_Hypotheses.md`（P2/P3/P4）、`Governance/SRT_CLAIM_LADDER.md` 与 `Core/SRT_OPEN_TENSIONS.md`；`SRT_AI_START.md` 瘦身为 bootstrap；AI / Philosophy / Spirituality 主入口已加角色与 P-level 回链头部。
- `2026-04-20`：第二轮 spirituality 扩展已完成主要分流：A 线（`SRT_Spirituality_Selection_Pathology_and_Return.md`）已吸收 directional return、faith as openness to `L_0`、semantic gravity / belief viscosity / ontological amnesia、expert vs master、以及 frozen-`L_2` AI / intelligence ⟂ care；B 线（`SRT_Spirituality_How_We_Lose_Ourselves_and_Return.md`）已反映初心不是无知、熟悉解释变成现实本身、技术系统高智能但不真正关切、以及 community 作为轻量支持接口；`SRT_Spirituality_Community_and_Sangha.md` 已作为独立 companion 支线建立；`SRT_Spirituality_Second_Expansion_Bridge.md` 已降权为 `archival_index` 并补全 provenance record。
- `2026-04-20`：`SRT_Spirituality_Return_Expansion_Bridge.md` 已完成反向并入，降权为 `archival_index`；A 线（`SRT_Spirituality_Selection_Pathology_and_Return.md`）与 B 线（`SRT_Spirituality_How_We_Lose_Ourselves_and_Return.md`）均已增强：B 线新增 §2 空心主体/L2 主导环境（生活化）、§4 病理 vs 苏醒性空心感区分、§5 初学现象学、§8-§9 工作/关系/忙碌场景、§10 过渡期（dark night 生活化版本）共五处增补与一个新章节；bridge provenance record 已完整记录并入落点。
- `2026-04-20`：已新增 spirituality 双线文档：`Spirituality/SRT_Spirituality_Selection_Pathology_and_Return.md` 作为 canonical 主轴，收口 ready-made floors、主体位丢失、危机现象学、真轻/伪轻、support、micro-selection 与现代技术的 spiritual crisis；`Spirituality/SRT_Spirituality_How_We_Lose_Ourselves_and_Return.md` 作为 companion exposition，以更生活化方式展开现代生活反思、空心感、现成答案、支持与回返路径。
- `2026-04-20`：`SRT_Uncertainty_Payment_Raw_L0_Selection_Bridge.md` 已反向并入 canonical 主文档：`§4.4`（更轻 = 自我扭曲成本下降，`processing load ≠ Ψ_f`）、`§5.5`（真选择 vs 标签内优化，不确定性更根于直觉）、`§6.5`（`d↑/d↓` 不确定性支付能力，混沌精确定义，微小选择）已熔入 `SRT_Philosophy_Ethics.md`；`3.1d Integration Note`（空心感封口、自我扭曲链条、健康支持、早期修复序列）已并入 `SRT_Ethics_Agency.md`；bridge 已降权为 `archival_index`；`SRT_Merged_Provenance_Index.md` 已更新留痕。
- `2026-04-20`（earlier）：已新增 `Philosophy/SRT_Uncertainty_Payment_Raw_L0_Selection_Bridge.md`，整理本轮关于 `d↑/d↓` 与不确定性支付、真选择 vs 标签内优化、raw `L_0` 秩序、自我扭曲（痛苦/空心感/标签化/空洞自我维持）及健康支持的闭链内容，作为后续反向并入 `Philosophy_Ethics / Ethics_Agency` 的 staging bridge。
- `2026-04-19`：已将 `Philosophy/SRT_Philosophy_Ethics_Integration_2026_04_19.md`（主体位、d 增厚、新预期形成）回写并入 `Philosophy/SRT_Philosophy_Ethics.md`，源文件降权为 `archival_index`，`SRT_Merged_Provenance_Index.md` 已更新留痕。
- `2026-04-18`：已新增 `README.md`、`CLAUDE.md`、`Governance/SRT_CANONICAL_FREEZE.md`、`Governance/SRT_EDIT_PROTOCOL.md`、`Governance/SRT_HARNESS_TESTS.md`，并开始收口入口层、manifest 与运行层边界。
- `2026-04-16`：已收紧 `relative existence / L2 convergence` 相关口径，并回写主文与哲学接口。
- `2026-04-15`：已把 `d-value` 的治理层 canonical 锚点收口到 `_SRT_D_VALUE_CANONICAL.md`。
- `2026-04-14`：已完成多批材料审查与若干神经/节律相关机制窗口的回写。

## 当前高优先事项

- 继续同步入口层去重：`README / AGENTS / CLAUDE / STATUS / _SRT_INDEX / Navigation / manifest`
- 保持 canonical 主链不被入口优化反向污染
- 按 `Governance/SRT_CLAIM_LADDER.md` 持续标注 domain 文件中的 P-level
- 继续把运行留痕与理论检索层分开
- 将 spirituality 三支结构（旧主轴 / 新双线 / community companion）与后续导航/入口层建立更清晰索引关系
- ~~将 `SRT_Uncertainty_Payment_Raw_L0_Selection_Bridge.md` 反向合并进 `Philosophy/SRT_Philosophy_Ethics.md` 与 `Philosophy/SRT_Ethics_Agency.md`~~（已完成 2026-04-20）

## Pipeline 快照

- `Pipeline 1`：材料融合主流程继续有效；二轮结构裁决走 `Operations/_SRT_MATERIAL_ADJUDICATION_WORKFLOW.md`
- `Pipeline 3`：信号采集按 `Operations/_SRT_OPERATIONS_SCHEDULE.md` 执行
- `Pipeline 6`：内审按 `Operations/_SRT_OPERATIONS_SCHEDULE.md` 执行

## 当前工作边界

- 本轮已优先完成 Core_21 命题硬度分层；入口、索引与 domain 回链只做配套收口
- 暂不大规模改正文主链
- 理论文件编辑先看 `Governance/SRT_CANONICAL_FREEZE.md` 与 `Governance/SRT_EDIT_PROTOCOL.md`
