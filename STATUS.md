---
id: SRT-STATUS
type: dashboard
status: active
layer: meta
epistemic_layer: os
claim_mode: evidence
updated: 2026-08-04
---

# SRT 当前状态仪表盘

> **角色**：当前状态面板（fast bootstrap 直接读 §Fast Status，本文件已兼任原 `STATUS_FAST.md` 职责）。
> **最后更新**：2026-08-04
> **历史条目**：`Operations/Status_History/`（本面板只保留最近约 30 天）
> **年度变更摘要**：`Governance/_SRT_CHANGELOG_2026.md`

## Fast Status

- 首读顺序唯一权威：`AGENTS.md §Session Start`。
- 当前活跃工作线：①书稿《从存在到秩序》（当前以 `Drafts_26Q` 为主线，处于生成哲学战略总装轮；choice-trace 作者门已关闭，后续分项施工）；②论文（Frontiers executive friction 返修、Adaptive Behavior 重投准备、Forcing–CH 证据建设）；③社媒文章线（`Operations/_SRT_ARTICLE_WORKFLOW.md`）。
- 休眠层（AI / Neuroscience / Physics / Spirituality）按“带冻结戳的图书馆”治理，不进例行状态面。
- 停驻内容（种子 / B 类材料 / 未合 PR）统一看 `_SRT_PARKED_INDEX.md`。
- 治理原则与减负记录：`Governance/README.md §Proportionality Principles`、`Governance/Governance_Load_Reduction_2026-07-20.md`。

## 当前仓库状态

- 单一 `main` 分支；根目录 2026-04-15 平铺，2026-07-20 治理减负轮后根目录 md 80 → 54（口径：`find . -maxdepth 1 -type f -name '*.md' | wc -l`）。
- `Core_21` 已拆 P0/P1/P2-P4 分层；持续要求 domain 文件回链 canonical，防 bridge / companion / lab 命题冒充 core。
- 书稿：当前状态以 `01_Source_Intuition/BOOK/BOOK_CURRENT_STATUS.md` 为准；`Drafts_26Q/Q00–Q28` 为主线，外部评审施工与 choice-trace Phase 1 候选章末注已完成。2026-08-04 已关闭 G1/G2/G4/G5/G6 作者门，但尚未执行新一轮 bridge 或正文改写。
- 工程结构：2026-07-07 清理轮（papers 合并 / preflight 接入 / 前台指针覆盖层定案）；2026-07-20 治理减负轮（见下）。

## 当前权威锚点

- L0 唯一锚点 → `Core_Law/SRT_L0_Metaphysics.md`
- claim ladder → `Governance/SRT_CLAIM_LADDER.md`
- d-value canonical → `_SRT_D_VALUE_CANONICAL.md`
- `Ψ_f` canonical → `_SRT_PSI_F_CANONICAL.md`
- `T_dir` canonical → `_SRT_T_DIR_CANONICAL.md`
- 符号规范 → `_SRT_SYMBOL_TABLE.md`（fast guard 已并入 `SRT_AI_START.md`）
- formal axioms → `Core/SRT_Core_21_Formal_Axioms.md`（P0 → `Core/SRT_Core_21_Minimal_Axioms.md`；P1 → `Core/SRT_Core_21b_Constitutive_Theorems.md`；P2-P4 → `Core/SRT_Core_21c_Bridge_Hypotheses.md`）
- master equations → `Core/SRT_Core_22_Equations.md`
- open tensions → `Core/SRT_OPEN_TENSIONS.md`
- choice-trace 作者裁决 → `Operations/SRT_CHOICE_TRACE_AUTHOR_DECISIONS_2026-08-04.md`

## 最近关键推进

- `2026-08-04`：**Forcing–CH D05 首轮 C5-op 比较完成裁决**。新增 `Philosophy/Papers/Forcing_CH_Evidence/D05_C5op_Goedel_to_Cohen_Audit.md`：Gödel 阶段与 Cohen event 两份 D03 基线均已在各自记录的裁决层级完成，D05 的 C5-op 比较现为当前活跃证据任务。`EVD-D05-0001` 判为 **qualified**——对五个已登记的保守重建候选（`D05-T01`–`D05-T05`）逐一做对抗性检验后，有界的 C5-op 失败获得支持，失败见证为 Cohen 明示不可在基模型中定义的外部完全序列；无界主张因缺少 1938–1963 阶段级操作库存而不成立，据此新登记 `EVD-D05-0003`、`EVD-D05-0004`。`EVD-D04-0002` 维持 unresolved。**尚未作出任何 institutionalization（H/N/S）、CH 局部制度、全局 update-regime、C2 或 SRT 裁决**；`strategy_note_v0_7` 维持 frozen，冻结战略与分阶段正文未改，三项欠规定项仅记录为 freeze-exception 候选。
- `2026-08-04`：**Choice-trace 作者裁决包全部关闭**。作者逐项完成 G1/G2/G4/G5/G6 裁决；G3 已分层消解，G7 已完成选项回收。新建 `Operations/SRT_CHOICE_TRACE_AUTHOR_DECISIONS_2026-08-04.md`，并将 `Operations/_SRT_CHOICE_TRACE_WRITEBACK_PLAN_2026-07-10.md` 升为 `plan_v2_author_gates_closed_2026-08-04`。核心治理结果：可再选择性只属于生成健康评价层；耗散结构不等于选择结构；选择分过程层／事件层／评价层；痛苦定位为“具身位上的结构性损失压力”；理论词形统一为“选择生成条件”“选择性再组织”“最低非中立性”。本轮只完成治理闭环，不修改 canonical、bridge 或书稿正文。由此解锁 T-B“熵—扰动—选择性再组织”、T-D“选择生成条件”、T-E“耗散结构与选择结构”以及 Q15/Q21/耗散书稿接口的独立施工。
- `2026-08-04`：**Forcing–CH Cohen event 技术证据基线完成首轮裁决并经 PR #708 合入**。新增 `Philosophy/Papers/Forcing_CH_Evidence/D03_Cohen_Event_Baseline.md`：`EVD-D03-0009` 与 `EVD-D03-0013` 判为 supported，`EVD-D03-0010` 判为 qualified；严格分离 Cohen event 与 institutionalized forcing，不作 C5-op、H/N/S、C2 或全局 update-regime 裁决；冻结战略与分阶段正文未改。
- `2026-08-03`：**Forcing–CH 论文转入证据建设**。PR #701 已合并 evidence-gated 分阶段稿；Gödel 与 Cohen 的 D03 技术基线现均已建立，下一步进入受证据门约束的比较与后续阶段。
- `2026-07-25`：**第 0 档闭账轮完成**。P1-T07 证明审计合入 main；IntegrationHook 闭环审计与 CI 检查落地；两份具身位／`d-q-o` 对话补走 trace 收尾管线。**全部路由为候选，无一落地**；已加下游护栏：符号重命名与 `q` / `o` 的形式选择做出前，`d/q/o` 不得进入书稿、公共内容、bridge 或论文。仍待作者另行裁决：Physics 三张 patch 最终落点；`q` 是否独立于／正交于 `d`；`o` 是否设符号。
- `2026-07-22`：**Learnable Novelty 材料卡完成并按高优先级 B1 停驻**。稳定增量包括 observer-relative learnable-structure yield、future learnability endpoint 与 structured novelty／residual noise 分离；继续保留 `S^phi != Ψ_f != d != W_sel` 护栏。
- `2026-07-21`：**热力学计算与水结冰两张材料卡完成并停驻**。前者承担 `noise + constraint + readout` 不推出 `W_sel + bearer` 的边界；后者承担 `stability != reachability`、物理路径依赖不自动构成选择写回的自然边界。
- `2026-07-20`：**治理减负轮完成**。Operations 一次性记录归档、根目录停驻文件下沉、coverage index 冻结、状态面收口、boot 读单缩减、router 合并、人类入口整合、frontmatter 最小 schema 棘轮与治理四原则落地。
- `2026-07-10`：**Choice-trace 回写计划 Phase 1 完成**。理论侧完成 T-A、T-F 候选登记、T-G；书稿 Q06/Q19/Q22/Q28 落候选性质章末注。T-F 正式证据卡尚未开始；T-C 边界 bridge 无门但尚未施工。
- `2026-07-09`：**ChoiceMap 轨迹工作流 v2 与两份 source trace 收尾完成**。建立暂停／恢复、一致性压测、张力审计、委托收敛与 canonical 碰撞检查；原 pending 作者项现已由 2026-08-04 裁决记录覆盖。

（更早条目见 `Operations/Status_History/2026-04_to_2026-07_Dashboard_Part.md`）

## 当前高优先事项

1. **Choice-trace 下游施工**：优先建立 T-B“熵—扰动—选择性再组织”bridge；随后拆建 T-D“选择生成条件”和 T-E“耗散结构与选择结构”。三项必须分别提交，不在治理闭环 PR 中混改。
2. **书稿接口**：待 T-B/T-D/T-E 稳定措辞后，分别处理 Q15 关切、Q21 苦难与耗散接口；不得把可再选择性写成选择事件定义，也不得把痛苦写成一切主体动力的唯一来源。
3. **论文线**：完成 Frontiers 稿 1837760 major revision 的门户提交；推进 Adaptive Behavior 重投；Forcing–CH 继续按 evidence gate 建设。
4. 保持 canonical 主链不被入口优化或 source intuition 反向污染。
5. 治理可观测指标：boot 必读 3 文件 / 根目录 md ≤ 60 / navigation 占比下降 / 状态镜像唯一（详见 `_SRT_QUALITY_METRICS.md`）。

## Pipeline 快照

- `Pipeline 1`：材料融合继续有效；B 类语义自 2026-07-20 起为“停驻 + 具名触发条件”（见 `Operations/_SRT_MATERIAL_PIPELINE.md`）。
- 当前理论术语以 2026-08-04 作者裁决为准：一般过程使用“选择性再组织”，不再用“再同步”作为跨层级定义；具体神经或群体同步仍按领域可测含义使用。
- `Pipeline 3` / `Pipeline 6`：按 `Operations/_SRT_OPERATIONS_SCHEDULE.md` 执行。
- Pipeline 5 主模式：`Operations/_SRT_ARTICLE_WORKFLOW.md`。

## 当前工作边界

- 书稿当前状态与施工许可先看 `01_Source_Intuition/BOOK/BOOK_CURRENT_STATUS.md`；choice-trace 轨道沿用 2026-07-10 作者豁免，其余书稿治理纪律不豁免。
- 理论文件（canonical）编辑先看 `Governance/SRT_CANONICAL_FREEZE.md` 与 `Governance/SRT_EDIT_PROTOCOL.md`；本轮作者裁决不构成 canonical 修改授权。
- `Operations/SRT_CHOICE_TRACE_AUTHOR_DECISIONS_2026-08-04.md` 是治理裁决来源，不得独立用作经验或形式证明。
- 休眠层只做 touch-based repair，不开专项治理轮。
