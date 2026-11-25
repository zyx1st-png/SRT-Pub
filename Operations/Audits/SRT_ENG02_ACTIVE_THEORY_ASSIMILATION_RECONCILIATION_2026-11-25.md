---
id: SRT-ENG02-ACTIVE-THEORY-ASSIMILATION-RECONCILIATION-20261125
type: audit
status: active
canonical: false
layer: operations
epistemic_layer: os
claim_mode: evidence
created: 2026-11-25
updated: 2026-11-25
priority: high
dependency:
  - STATUS.md
  - Operations/Audits/data/srt_active_theory_nodes.json
  - Operations/Audits/SRT_ACTIVE_THEORY_ASSIMILATION_AUDIT_2026-08-06.md
  - Operations/Audits/Hook_Closure_Audit_2026-07-25.md
  - Operations/Proposals/SRT_R3_FULL_SKELETON_CLOSEOUT_GLOBAL_SUBTRACTION_2026-11-25.md
  - _SRT_CONTEXT_ROUTER.md
  - scripts/check_active_theory_assimilation.py
  - scripts/build_srt_context_bundles.py
tags: [ENG02, Audit, Assimilation, EA1-EA5, Reconciliation, ActiveLayer, R4Handoff]
---

# `ENG-02` 活跃理论吸收台账与正文/检索路径对账审计（`2026-11-25`）

> **目标与治理边界（`canonical: false`）：** 本轮 `ENG-02` 从 `main@04dfe961d`（PR `#1155` 合并后）启动，以**理论正文、检索路径与吸收台账的真实一致性**为唯一目标，**不以提高节点完成率为目标**。**内容同步核查**与**台账刷新**严格分开验收；凡涉及实质理论语义修改或 canonical / Freeze-A 文件改写的真实缺口，一律保持诚实阻塞状态并移交 `R4`，本轮不修改任何 canonical 正文或理论桥接正文，不解除任何既有 `HOLD`、`63` 项 `OPEN` 或 `25` 条封存 `validation_holdout`。
>
> **状态时间边界（`P2-02`）**：本报告与台账中的 **`active_complete` 仅表示既有登记增量在当前运行结构中的结构吸收完成，不表示 `R3` 新裁决（`R3-01..R3-08` 与总收口）已完成 `R4` canonical 回写**。凡涉及 `R3` 新骨架重塑的节点（包括 `NODE-T-DIR` 与 `NODE-SUBJECTHOOD`），仍须按 `Wave R4-1..R4-4` 接受重构。

---

## 1. `EA-1..EA-5` 口径统一（JSON 结构轴 vs `2026-08-06` 历史审计初版编号对照）

全仓统一以 [`Operations/Audits/data/srt_active_theory_nodes.json`](data/srt_active_theory_nodes.json) 的三轴模型（Axis A 结构吸收 / Axis B 行为可用性 / Axis C 单 PR 干预效应）为现行口径；历史文件 [`SRT_ACTIVE_THEORY_ASSIMILATION_AUDIT_2026-08-06.md`](SRT_ACTIVE_THEORY_ASSIMILATION_AUDIT_2026-08-06.md) 保留为历史审计快照不覆写，编号差异明文对照如下：

| 现行 JSON 口径（Axis A 结构吸收） | 含义 | `2026-08-06` 历史初版编号 | 本轮代码/台账清理动作 |
|---|---|---|---|
| **`EA-1`** | 形成 SRT 原生命题、护栏或已登记张力（不可机检） | `EA-1` | 无编号冲突 |
| **`EA-2`** | 进入适当活跃理论 owner（不仅停留在 SourceCard/patch/hook/Operations） | `EA-2` | 无编号冲突 |
| **`EA-3`** | 存在可解析并点名该节点文件的声明式检索路径（router / deep map） | `EA-3`（合并 bundle） | 无编号冲突 |
| **`EA-4`** | 进入快速层或默认装载路径（context bundle） | 曾并入 `EA-3` | 修正 [`scripts/check_active_theory_assimilation.py`](../../scripts/check_active_theory_assimilation.py#L276-L286) 过时分段注释 |
| **`EA-5`** | 已处理被取代的旧表述（非 `n/a`） | 曾记为 `EA-4` | 同步清理 `NODE-SELECTION-ONTOLOGY` 中过时的 `"missing EA-5"` 旧注记 |
| **Axis B（非 `EA-5`）** | 新会话独立有界实跑行为验证（`untested / observed / robustly_observed (bounded)`） | 曾记为 `EA-5` | 严守 CI 不得设置 Axis B；本轮不声称任何新增 Axis B 通过 |

---

## 2. 逐节点「正文核查 vs 检索核查 vs 台账处置」分账验收表

### 2.1 重点核查的 7 处非 `active_complete` 节点（含 `EA-1 / EA-2 / EA-4` 全部点名项）

| 节点 ID | 独立正文/检索实证核查结论 | 缺口性质判定 | `ENG-02` 执行动作（内容与台账分账） | Axis A 变更（Axis B 均不变） | 移交 `R4` 事项 |
|---|---|---|---|---|---|
| **`NODE-T-DIR`** | 实查 [`_SRT_T_DIR_CANONICAL.md`](../../_SRT_T_DIR_CANONICAL.md#L129-L132) 及 [`PH_AG02`](../../Philosophy/hooks/PH_AG02_Reasoning_Bias_Integration_Hook.md) / [`PH_AG03`](../../Philosophy/hooks/PH_AG03_Constitutive_Commitment_Integration_Hook.md) hook：`directional efficacy / behavioral bias` 与 `commitment strength / decisiveness` 负面判据补注已于 **`2026-08-11`** 实装落地且两张 hook 对 `_SRT_T_DIR_CANONICAL.md` 均记 `state: landed`（仅停驻的 ChoiceMap 孵化目标保持 `pending`）。 | **正文早已同步，仅台账与 `G3` 陈旧**（`2026-07-25` 审计与 `2026-08-07` JSON 均早于 `08-11` 落地） | ① **不改 `_SRT_T_DIR_CANONICAL.md`**；② 仅刷新 JSON 台账反映 `08-11` 已落地与 `EA-5`；③ 在 `build_srt_context_bundles.py` `G3` 补注 `2026-07-25` 快照与实时 `landing_ledger` 分界（不改历史审计表）。 | `partially_active` → **`active_complete`**（真实对账） | `Wave R4-2`：Part II 过宽桥接清理与广义关切方向分离（`R3-06`） |
| **`NODE-SUBJECTHOOD`** | 实查 [`Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md`](../../Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md)（`canonical: false`）：已吸收 `PH_AG01..04` 与 `PH_SEM01` 并在 §1 显式降格旧线性阶梯，但此前未入任何上下文包（`0/9`），且 `_SRT_CONTEXT_ROUTER.md#23` 仅指向停驻孵化区。 | **真实 `EA-3 / EA-4` 工程检索缺口**（不涉及理论正文修改） | ① 在 [`scripts/build_srt_context_bundles.py`](../../scripts/build_srt_context_bundles.py) 通过 `DOMAINS["Philosophy"]["bridges"]` 纳入 `DOMAIN_PHILOSOPHY`（保持 `canonical: false`，不混入 `COMPACTCORE`）；② 在 [`_SRT_CONTEXT_ROUTER.md §8a`](../../_SRT_CONTEXT_ROUTER.md#L269-L284) 补入该文件（`§23` 加互链）；③ 重建上下文包后刷新 JSON。 | `partially_active` → **`active_complete`**（工程补线） | `Wave R4-3/R4-4`：`R3-04` `Bearer ↔ Agency` 必要性、`R3-07` `O2-A` 归责、`PH_SEM01 → Occlusion_Dynamics` 回写 |
| **`NODE-LIFE-DISSIPATIVE`** | 实查 [`03_Bridges/SRT_Selection_Event_CompactCore.md`](../../03_Bridges/SRT_Selection_Event_CompactCore.md#L142) 与 [`T-E` 桥](../../03_Bridges/SRT_Dissipative_Structures_and_Selection_Structures_Bridge_2026-08-04.md#L103-L153)：快速层确只含 `G2` 一句分层裁决，**确实缺失** `T-E §2` 物理底座 / 组织机制 / 解释充分性三分。 | **真实 `EA-4` 快速层理论压缩缺口** | **不改理论/桥接正文、不强行升格**；保持 `partially_active` 与原 `EA-4` blocker，在台账标明实证复核日期与 `R4` 移交落点。 | **保持 `partially_active`** | `Wave R4-4`：物理域快速层补齐 `T-E` 三分并对接一手物理证据卡 |
| **`NODE-ENTROPY-REORG`** | 实查 [`03_Bridges/SRT_Selection_Event_CompactCore.md`](../../03_Bridges/SRT_Selection_Event_CompactCore.md#L117-L141) 与 [`T-B` 桥](../../03_Bridges/SRT_Entropy_Disturbance_Selective_Reorganization_Bridge_2026-08-04.md#L85-L190)：快速层**确实缺失** `T-B §2` 最小过程链与 `§5` 痛苦接口四分（结构性损失压力 / `pain` / `distress` / `suffering`）。 | **真实 `EA-4` 快速层理论压缩缺口** | **不改理论/桥接正文、不强行升格**；保持 `partially_active` 与原 `EA-4` blocker，在台账标明 `R4` 移交落点。 | **保持 `partially_active`** | `Wave R4-3`：`Core_Law/SRT_Suffering.md` 与快速层入口同步 |
| **`NODE-SOCIAL-L2`** | 实查 `Philosophy/SRT_Soc_03_Institutions.md` 与 `Core_Law/SRT_Collective_Selection.md`：`SEA` 协议与编码手册 **0 命中**，仍仅在 `Operations/`。 | **真实 `EA-2` 缺口（涉 canonical owner）** | **不提前改写 canonical**；保持 `partially_active` 与 `EA-2` blocker，在台账明确移交 `Wave R4-3`。 | **保持 `partially_active`** | `Wave R4-3`：`SRT_Collective_Selection.md` 与 `SRT_Soc_03_Institutions.md` 同步 `SEA` 接口 |
| **`NODE-BOOK-BACKFLOW`** | ① 实查 `Core_Law/`、`Core/`、`Philosophy/`：第三态能动性 / 被排开者去向三分 / 自检三问 **0 命中**（仅存书稿与 [`Sync Bridge`](../../03_Bridges/SRT_Book_Vocabulary_Theory_Sync_Bridge_2026-07-05.md)）；② `check_active_theory_assimilation.py` 报 `_SRT_CONTEXT_ROUTER.md#19` 未点名该桥。 | **真实 `EA-2` 理论缺口 + 真实 `EA-3` 导航遗漏** | ① 仅在 [`_SRT_CONTEXT_ROUTER.md §19`](../../_SRT_CONTEXT_ROUTER.md#L629-L660) Secondary 补入 `SRT_Book_Vocabulary_Theory_Sync_Bridge_2026-07-05.md`（消除检查器唯一 `WARN`，不改理论正文）；② 保持 `engineered_not_active`、`bundle: false` 与 `EA-2` blocker。 | **保持 `engineered_not_active`**（消除 `EA-3` WARN） | `Wave R4-2 / R4-4`：按 `R3-05/08` 新口径落盘 `B3-a` 五去向、第三态能动性与自反三问 |
| **`NODE-GHOST-OPERATOR`** | 实查 `Core/SRT_Core_21_Minimal_Axioms.md` 与 `_SRT_SYMBOL_TABLE.md`：三张 Ghost 源卡命题化 **0 命中**；[`Core_Law/SRT_Reference_Dynamics.md §1`](../../Core_Law/SRT_Reference_Dynamics.md#L26-L56) 仅完成 `\hat G_\theta != primitive Selection` 隔离。 | **真实 `EA-1 / EA-2` 缺口（涉多 canonical owner）** | **不提前改写 canonical**；保持 `partially_active` 与 `EA-1` blocker，明确移交 `R4`（`R3-08`）与后续 `Axis B` 实测。 | **保持 `partially_active`** | `Wave R4-1..R4-3`：Ghost 五位分流、`U5 ≠ U6` 落地与新会话 `Axis B` 行为验收 |

### 2.2 其余 9 个节点核查摘要（无状态异动）
- **`NODE-D-VALUE`**：保持 `author_gate`（`RQ-2026-08-A02` 与 `07-23/24` 符号禁运仍在 `R4` 前持续生效）。
- **既有 8 个 `active_complete` 节点**（`NODE-CHOICE-GENERATION`、`NODE-SELECTION-ONTOLOGY`、`NODE-L0-L1-L2`、`NODE-PSI-F`、`NODE-CONSCIOUSNESS`、`NODE-AI-REASONING`、`NODE-NEURAL-DECODABILITY`、`NODE-PHYSICS-MEASUREMENT`）：全部保持 `active_complete` 与原 `Axis B` 观察状态不变（仅清理 `NODE-SELECTION-ONTOLOGY` 一处过时 `missing EA-5` 备注）。

---

## 3. 对账后全仓统计快照（不宣称新增 Axis B 行为验证）

| 指标 | `ENG-02` 前（`04dfe961d`） | `ENG-02` 后 | 变化说明 |
|---|---:|---:|---|
| 节点总数 | 16 | 16 | 不增删节点 |
| Axis A: `active_complete` | 8 | **10** | +1 真实台账纠偏（`NODE-T-DIR` 2026-08-11 已落地）+1 工程补线（`NODE-SUBJECTHOOD` 入 `DOMAIN_PHILOSOPHY` 与 `§8a`） |
| Axis A: `partially_active` | 6 | **4** | 其余 4 处真实理论/快速层缺口全部诚实保留并移交 `R4` |
| Axis A: `engineered_not_active` | 1 | **1** | `NODE-BOOK-BACKFLOW` 诚实保持，仅消除 `EA-3` 路由 `WARN` |
| Axis A: `author_gate` | 1 | **1** | `NODE-D-VALUE` 禁运不变 |
| Axis B: `robustly_observed (bounded)` / `effectively_assimilated` | 3 / 3 | **3 / 3** | **零虚增**；本轮不开展或宣称任何新 Axis B 运行 |
| `check_active_theory_assimilation.py` 报告问题数 | 1 WARN | **0 WARN** | 收紧 `EA-3 / EA-4` 校验后，一并补齐 `NODE-BOOK-BACKFLOW` 与 3 处暴露的 `_SRT_DEEP_THEORY_MAP.md` 导航遗漏 |

---

## 4. `EA-3 / EA-4` 检查器收紧与暴露的历史假阳性处置（`P1-01 / P1-02 / P2-01`）

1. **`G3` 历史快照与现行规则一致性修复（`P1-01`）**：[`scripts/build_srt_context_bundles.py`](../../scripts/build_srt_context_bundles.py) `guard_hooks()` 保留 `2026-07-25` 历史审计表与分组，但同步修订标题、`affected`、解释段与 `USAGE POLICY`，明确历史表不自动等同于当前仍未落地，现行状态以各 hook 实时 `landing_ledger` 与目标 owner 正文为准，彻底消除与 `NODE-T-DIR`（`2026-08-11` 已落地）的口径矛盾。
2. **`EA-3 / EA-4` 检查器假阳性修复与全量复核（`P1-02`）**：
   - [`scripts/check_active_theory_assimilation.py`](../../scripts/check_active_theory_assimilation.py) 收紧 `EA-3` 为**仅在指定路由章节及其下属子节内检查目标文件名**（不再全文件搜索），收紧 `EA-4` 为**仅扫描真实上下文包 `SRT_CONTEXT_BUNDLE_*.md`（排除 `README.md`）并要求命中 `## FILE: \`<path>\`` 正文块**（防止未收录清单、索引或 `G5` 提及被误判为已装载）；并在 [`scripts/test_check_active_theory_assimilation.py`](../../scripts/test_check_active_theory_assimilation.py) 补入 4 项反例回归测试。
   - 收紧后对全部 16 个节点重跑实查：**全部 `16/16` `EA-4` 与全部 `14/14` `_SRT_CONTEXT_ROUTER.md` 锚点均无假阳性**；但在 [`_SRT_DEEP_THEORY_MAP.md`](../../_SRT_DEEP_THEORY_MAP.md) 暴露出 **3 处真实历史 `EA-3` 导航遗漏**：
     - `NODE-NEURAL-DECODABILITY`（`_SRT_DEEP_THEORY_MAP.md#8`）：原只列 `SRT_Neural_Mechanisms.md`，未列 `SRT_Neural_Mechanisms_CompactCore.md`、`_SRT_Neuroscience_Hardening_Index.md` 与 `SRT_Neuroscience_Claim_Status.md` → 本轮已在 `§8 Support files` 补齐（纯导航，不改理论正文）；
     - `NODE-PHYSICS-MEASUREMENT`（`_SRT_DEEP_THEORY_MAP.md#11`）：原只列长文 `SRT_Quant_01_Selection.md`，未列 `SRT_Quant_01_Selection_CompactCore.md`、`SRT_Physics_Claim_Status.md` 与 `REP01` 补丁 → 本轮已在 `§11 Primary / Support files` 补齐；
     - `NODE-SOCIAL-L2`（`_SRT_DEEP_THEORY_MAP.md#12`）：原未列 `SRT_Soc_03_Institutions.md`、`Core_Law/SRT_Collective_Selection.md` 与 `SRT_Political_Philosophy_CompactCore.md` → 本轮已在 `§12 Primary files` 补齐。
3. **`§8a` 查询条件分流（`P2-01`）**：在 [`_SRT_CONTEXT_ROUTER.md §8a`](../../_SRT_CONTEXT_ROUTER.md#L269-L288) 顶部增补物体个体化负对照 vs Agency / Subjecthood / S5–S6 门槛的条件分流，并将 `SRT_Philosophy_Agency_Subjecthood_v0_2.md` 与 `SRT_Subjecthood_Threshold_Interface.md` 升入 `§8a Primary`（注明 `canonical: false`）。
