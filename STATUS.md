---
id: SRT-STATUS
type: dashboard
status: active
layer: meta
epistemic_layer: os
claim_mode: evidence
updated: 2026-08-08
---

# SRT 当前状态仪表盘

> **角色**：当前状态面板（fast bootstrap 直接读 §Fast Status，本文件已兼任原 `STATUS_FAST.md` 职责）。
> **最后更新**：2026-08-08
> **当前排期裁决**：`Operations/SRT_WORKLINE_AUTHOR_PRIORITIES_2026-08-05.md`
> **历史条目**：`Operations/Status_History/`（本面板只保留最近约 30 天）
> **年度变更摘要**：`Governance/_SRT_CHANGELOG_2026.md`

## Fast Status

- 首读顺序唯一权威：`AGENTS.md §Session Start`。
- 当前第一优先工作线：完成此前未融合材料的 Pipeline 1 收口，并保持 Material Log、索引、registry 与 hook 一致。
- 论文线：
  - Frontiers 稿 `1837760` 已接受，但因 APC 过高准备终止原出版路径并转投；在取得原期刊明确终止确认前不得新投，执行卡为 Issue #740；
  - *Costly Selective Closure* / Adaptive Behavior 已投稿，尚未进入外部评审；
  - forcing–CH 的硬性历史书籍与同期记录仍在收集，控制档案 Part II 与控制案例程序暂缓；
  - history-dependent reachability 暂不启动统一优化，等待未融合材料收口。
- 书稿《从存在到秩序》仍以 `Drafts_26Q` 为唯一主线；统一优化等待未融合材料全部处理完毕，不进行逐篇材料触发的局部重写。
- SEA 编码手册已达到 pilot-ready，但独立编码可靠性试验暂缓；PR #738 已按 deferred 关闭。
- 休眠层（AI / Neuroscience / Physics / Spirituality）继续按“带冻结戳的图书馆”治理；材料可进入桥、卡片和索引，但不自动触发 canonical 或正文升级。
- 独立 P4 `Stake–Future Selectability MVP` 已完成 12×6 formal cohort，冻结裁决为 **UNINTERPRETABLE PROTOCOL**：T/S Reach20 逐-cell 有效性门失败 8/48；M4 亦未提升分组样本外预测。旧 selective-resynchronization NO-GO 保持不变，canonical 文件未修改。
- 停驻内容统一看 `_SRT_PARKED_INDEX.md`；最新作者排期以 `Operations/SRT_WORKLINE_AUTHOR_PRIORITIES_2026-08-05.md` 为准。

## 当前仓库状态

- 单一 `main` 分支；根目录治理继续执行 2026-07-20 减负纪律。
- `Core_21` 已拆为 P0/P1/P2-P4；domain、bridge、lab、SourceCard 和 Operations 文件不得反向定义 core。
- Choice-trace 作者门已关闭；T-B、T-D、T-E 首轮 bridge 与五域联合压力测试已经完成，不再列为“待建立”。
- SEA 已形成统一协议、AI 正负校准、生命边界案例、制度配对案例与编码手册；方法贡献仍为 candidate，可靠性 pilot 暂缓。
- forcing–CH 已完成 D05 C5-op、方法个体化协议、控制案例选择协议、多表征方法族审计和 countable-standard-model premise 窄类型说明；控制档案 Part II 仍未签署。
- Pipeline 1 截至本轮材料台账为 208 条：A 131、B 27、C 50；2026-08 Part01 为 10 条。
- 本轮开放材料与证据 PR 已完成收口；后续新增工作应从最新 `main` 重新起分支。

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
- 当前工作线排期 → `Operations/SRT_WORKLINE_AUTHOR_PRIORITIES_2026-08-05.md`

## 最近关键推进

### 2026-08-08 · Stake–Future Selectability MVP 完成

- 新建独立 P4 `PersistentChoiceGrid-v0` 实验，完成 smoke、3-seed A/B-only pilot、formal lock 与 12 master seeds × 6 branches 的 72 条 A→B→C 轨迹。
- 72/72 pre-C 哈希、72/72 identity continuity、24/24 T reset 与 24/24 S persistence 通过；无 replacement、无 C→pre-C 泄漏。
- 冻结 Reach20 有效性门在 T/S 中仅 40/48 通过，故裁决为 **UNINTERPRETABLE PROTOCOL**；不以 Emp5 的正向结果替换预注册 Reach20 门。
- 锁定预测同样不利：M4 相对 M3 的 LOSO CV R² 变化为 −1.0275，NRMSE 恶化 13.04%；`dV_CF_pre` 标准化 β=0.0300，seed-cluster 95% CI [−0.2610, 0.1924]。
- 结果只适用于本架构下的 surrogate-stake → counterfactual-sensitivity → future-selectability 桥；不验证 canonical `d`，不推断意识，不改动 Core 与休眠 owner 文件。

### 2026-08-07 · NEURAL23 具身节律准入桥

- 对 Young, Ericson & Schooler 2026 *Neuroscience of Consciousness* 综述完成全文材料融合，裁决为 **A（bounded non-canonical P3 implementation bridge + P4 experimental window）**。
- 新增 `NEURAL23`：以 `momentary selection eligibility` 描述脑—身体节律对候选进入竞争／门控／稳定过程的时相调制；明确区分 selection weight、selection opportunity 与 friction。
- 建立 selection eligibility 与 N10/BTSP plasticity eligibility 的双门分离：`eligibility to become current reality != eligibility to enter history`。
- 生理 synchrony 继续只按领域可测机制使用，不恢复为跨层级 SRT primitive，也不复活 selective-resynchronization 构念；一般跨层过程仍使用“选择性再组织”。
- 形成 P4 `Phase x Stake` 差异预测，以及 matched-coupling/different-recovery、state-switch accessibility、selection-vs-plasticity eligibility dissociation 三组补充测试。
- SourceCard、patch、landing-ledger hook、Material Log、两级索引与 registries 已同步；canonical `d` / `Psi_f` / `T_dir` / Core axioms 和休眠 owner 正文未修改。

### 2026-08-05 · 工作线排期与仓库收口

- 作者确定：forcing–CH 控制档案和 SEA reliability pilot 暂缓；书稿与 history-dependent reachability 的统一优化等待此前未融合材料全部收口。
- Frontiers 稿 `1837760` 已接受，但因 APC 过高准备终止原出版路径并转投；Issue #740 负责撤回／终止确认、版权与重复投稿合规、目标期刊选择和状态同步。
- *Costly Selective Closure* / Adaptive Behavior 已投稿，当前尚未外审；不再写作“重投准备”。
- 旧书稿路线 Issue #152、#153、#155 已按 superseded / not planned 关闭；#657、#474 保留但延期。

### 2026-08-05 · PR 与材料线收口

- PR #730 合入 forcing ramified / generic-filter / Boolean-valued 多表征方法族审计；整体为 `qualified_same_method_family`，Method Individuation Protocol v0.1 为 qualified、未被证伪。
- PR #739（替代冲突处理中自动关闭的 #733）合入 countable-standard-model premise 窄类型说明；`EVD-D04-0002` 继续 unresolved，D05 verdict 不动。
- PR #735 合入 salience / lateral-inhibition source-intuition genealogy；保持非 canonical 与反还原护栏。
- PR #734 合入 AIGOAL01：区分 goal completion、给定菜单中的 bounded goal selection 与 goal-space generation。
- PR #728 合入五张意识／认知材料卡；只进入 B1/B2/B3 材料路由，不直接改书稿正文。
- PR #710 解决 `NEURAL21` 编号冲突后以 `NEURAL22` 合入 astrocyte hierarchical information-flow bridge；保留 `NEURAL21` 为 REM metabolic-payability bridge。
- PR #738 SEA reliability pilot 按作者排期关闭为 deferred；不解释为方法失败。

### 2026-08-05 · SEA 方法建设

- 新增统一选择事件方法论文策略：当前定位为非补偿式识别与审计方法 candidate，而非新因果机制。
- 完成学术出版终止／接受后 production 的制度配对校准。
- 完成 SEA 案例编码手册 v0.1；五门、事件、边界、时间尺度、降级点和最高类别均可进入未来独立编码试验。
- 当前不启动正式可靠性 pilot。

### 2026-08-04 · Choice-trace 理论桥与压力测试

- T-B“熵—扰动—选择性再组织”、T-D“选择生成条件”、T-E“耗散结构与选择结构”均已建立首轮 bridge。
- 五域联合压力测试结论：T-D 最稳；T-B 有条件成立，必须定位内部非等价登记；T-E 当前主要承担防止耗散／不可逆性被直接等同于选择的负向护栏。
- CG-1 至 CG-4 已分别建立操作化测试，后续又统一进入 SEA 审计协议。
- 这些推进不构成 canonical、经验确认或五门必要充分性证明。

### 2026-08-04 至 2026-08-05 · Forcing–CH

- D05 `EVD-D05-0001` 保持 **qualified**：有界 C5-op failure 获得支持，无界主张仍受阶段级操作库存缺口阻塞。
- `EVD-D04-0002` 保持 **unresolved**。
- `METHOD_INDIVIDUATION_PROTOCOL_v0_1`、`CONTROL_CASE_SELECTION_PROTOCOL_v0_1` 与档案边界已冻结。
- `CONTROL_ARCHIVE_ADEQUACY_CERTIFICATE_v0_1` Part I 已固定，Part II 未签署；在硬性历史书籍和同期记录未收齐前，不枚举、评分、排名或选择 Control A/B。

### 更早的重要状态

- 2026-07-25：P1-T07 证明审计、IntegrationHook 闭环审计与 CI 检查完成；两份具身位／`d-q-o` 对话补走 trace 收尾管线。**全部路由为候选，无一落地**；已加下游护栏：符号重命名与 `q` / `o` 的形式选择做出前，`d/q/o` 不得进入书稿、公共内容、bridge 或论文。仍待作者另行裁决：Physics 三张 patch 最终落点；`q` 是否独立于／正交于 `d`；`o` 是否设符号。
- 2026-07-20：治理减负轮完成，boot 必读缩至 3 文件，状态入口与 router 收口。
- 2026-07-10：choice-trace Phase 1 完成，Q06/Q19/Q22/Q28 只加入候选性质章末注。

（更早条目见 `Operations/Status_History/2026-04_to_2026-07_Dashboard_Part.md`）

## 当前高优先事项

1. **材料收口**：继续处理此前未融合材料；每条材料按 Pipeline 1 完成 SourceCard / Patch / Hook / Material Log / Index / Registry 所需闭环，不因单篇材料立即改写全书或论文。
2. **Frontiers 转投合规**：按 Issue #740 核验 accepted / production / proof / DOI 状态，取得原期刊明确终止确认，再选择并提交新期刊。
3. **Adaptive Behavior 稿件维护**：当前已投稿、未外审；等待编辑处理，除非期刊提出明确要求，不增加实验或扩张 framing。
4. **Forcing 历史材料收集**：继续收集硬性历史书籍、原始论文和同期评论；只做 corpus 与 coverage 记录，不提前形成控制候选判断。
5. **延后统一优化**：材料收口后，再分别启动《从存在到秩序》和 history-dependent reachability 的统一 pass。
6. **SEA reliability**：待上述工作减压后重新评估独立编码 pilot。
7. 保持 canonical 主链不被入口优化、source intuition、材料卡或暂时排期反向污染。

## Pipeline 快照

- `Pipeline 1`：继续有效；B 类为“停驻 + 具名触发条件”，不是默认排队。
- 当前理论术语以 2026-08-04 作者裁决为准：一般过程使用“选择性再组织”，不再用“再同步”作为跨层级定义；具体神经或群体同步仍按领域可测含义使用。
- `Pipeline 3` / `Pipeline 6`：按 `Operations/_SRT_OPERATIONS_SCHEDULE.md` 执行。
- Pipeline 5 主模式：`Operations/_SRT_ARTICLE_WORKFLOW.md`。
- 书稿统一优化、HDR 统一优化、forcing 控制档案 Part II、SEA reliability pilot 均受 2026-08-05 排期裁决约束。

## 当前工作边界

- 书稿当前状态与施工许可先看 `01_Source_Intuition/BOOK/BOOK_CURRENT_STATUS.md`；当前只允许材料融合和必要治理修复，不启动统一正文优化。
- history-dependent reachability 的已有实验、数字、图表和 assembly 记录保持稳定；新材料先停在材料层，待统一 pass 再裁决是否进入正文。
- Frontiers 原出版路径未明确终止前不得重复投稿；已接受但准备转投不等于 published、in press 或 rejected。
- Adaptive Behavior “已投稿、未外审”不得写成 under review。
- forcing 书籍收集不等于控制案例枚举；Part II 未签署前继续执行既有阻塞。
- SEA pilot 暂缓不等于 SEA 被验证或被否定。
- 理论文件（canonical）编辑先看 `Governance/SRT_CANONICAL_FREEZE.md` 与 `Governance/SRT_EDIT_PROTOCOL.md`。
- 休眠层只做 touch-based repair，不开专项治理轮。
