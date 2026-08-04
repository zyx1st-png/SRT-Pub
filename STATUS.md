---
id: SRT-STATUS
type: dashboard
status: active
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
- 当前活跃工作线：①书稿《从存在到秩序》（RC1-candidate 冻结中，choice-trace 回写按豁免裁决推进）；②论文（Frontiers executive friction 返修、Adaptive Behavior 重投准备）；③社媒文章线（`Operations/_SRT_ARTICLE_WORKFLOW.md`）。
- 休眠层（AI / Neuroscience / Physics / Spirituality）按"带冻结戳的图书馆"治理，不进例行状态面。
- 停驻内容（种子 / B 类材料 / 未合 PR）统一看 `_SRT_PARKED_INDEX.md`。
- 治理原则与本轮减负记录：`Governance/README.md §Proportionality Principles`、`Governance/Governance_Load_Reduction_2026-07-20.md`。

## 当前仓库状态

- 单一 `main` 分支；根目录 2026-04-15 平铺，2026-07-20 治理减负轮后根目录 md 80 → 54（口径：`find . -maxdepth 1 -type f -name '*.md' | wc -l`）。
- `Core_21` 已拆 P0/P1/P2-P4 分层；持续要求 domain 文件回链 canonical，防 bridge / companion / lab 命题冒充 core。
- 书稿：2026-06-19 冻结为 RC1-candidate（PR #506，导出校验通过）；2026-07-04 外部评审（知微）开卷过堂完成，品味级条目收编为一轮施工；2026-07-10 choice-trace 回写 Phase 1 按作者冻结豁免完成四章章末注。详见 `01_Source_Intuition/BOOK/BOOK_CURRENT_STATUS.md`。
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

## 最近关键推进

- `2026-08-04`：**Forcing–CH Cohen event 技术证据基线完成首轮裁决**。新增 `Philosophy/Papers/Forcing_CH_Evidence/D03_Cohen_Event_Baseline.md`：`EVD-D03-0009`（原始 ground model—ramified terms—conditions—complete sequence—`N`—`¬CH` 输出）与 `EVD-D03-0013`（CTM / generic / external metatheory / finite-fragment discharge 假设审计）判为 supported；`EVD-D03-0010`（原始 forcing、偏序/generic-filter、Boolean-valued 表述关系）判为 qualified。严格分离 Cohen event 与 institutionalized forcing；不作 C5-op、H/N/S、C2、CH 局部制度或全局 set-theoretic update-regime 裁决；`strategy_note_v0_7` 与分阶段正文未改。
- `2026-08-03`：**Forcing–CH 论文转入证据建设**。PR #701 已合并 evidence-gated 分阶段稿；当前活跃任务为 Gödel 阶段 D03 基线档案（`EVD-D03-0006`–`0008`，并仅准备 `EVD-D04-0002`）；`strategy_note_v0_7` 继续冻结，不在本轮升级正文主张。
- `2026-07-25`：**第 0 档闭账轮完成（三项）**。①**P1-T07 证明审计合入 main**（PR #676，纯审计三文件 `Operations/Audits/SRT_P1_T07_PROOF_HARDENING_AUDIT.md`、`Operations/Audits/Maps/SRT_P1_T07_ASSUMPTION_MAP.md`、`Operations/Proposals/SRT_P1_T07_HARDENING_OPTIONS.md`，不改任何 canonical）；Options A/B/C 仍为 proposal-only，Option B 是最小编辑候选但须先清三项前置（选定 S1/S2/S3 稳定性语义、把 "ε-neutral" 定义在独立转移核上、证明该中性基线 a.s. 吸收）；`_SRT_PARKED_INDEX.md §3` 已销账。②**IntegrationHook 闭环审计**（`Operations/Audits/Hook_Closure_Audit_2026-07-25.md`）：18 张 hook 用字面锚串实证体检 = 12 landed / 3 partial / 3 pending；发现 PH-AG01 被低报（实际已落地）、4 张状态不可判读、Physics 三张指向从未创建的计划文档 `Physics/SRT_Physics_Bridge_v0_2.md`、3 张的停驻目标路径在 2026-07-20 下沉后未更新；新增 `scripts/check_hooks.py` + `scripts/test_check_hooks.py`（15 条 fixture 覆盖四态与错误路径）并接入 CI preflight，ledger 契约同步回写 `Operations/_SRT_MATERIAL_PIPELINE.md §5.6.1`，`landed` 必须带**在 target 中唯一命中**的锚串（章节标题 / claim ID / source-trail 链接，禁用通用关键词），`status`（文件在用）与 `integration_status`（是否落地）拆开；顺带修复 main 上已红的四条 frontmatter ratchet 违规，基线净减 21 行、零新增。**待作者裁决**：Physics 三张 patch 的最终落点（新建综合文 vs 并入 `Physics/_SRT_Phys_Bridge.md`）。③**两份对话材料补走 trace 收尾管线**（`01_Source_Intuition/Conversations/2026-07-25_具身位_d_q_o_收尾审计.md`）：2026-07-23 具身位/三层关切与 2026-07-24 客体性/`d-q-o` 三轴此前是管线外影子路径；补做符号撞车（九个候选记号中三个重命名了既有对象、三个违反记号或命名空间约定、一个有撞车风险；`ρ`/`Ω`/`τ_self`/`g` 已被 canonical 占用，`w_i`、`D_stake`、`d_canonical` 各被重新发明一次）、canonical 碰撞三分类、张力表与路由。**候选增量**四条（d/q 解耦最值得优先审计，但均未确认成立）；触雷三条（`q` 五成分中两项落在 `Def-w_i` 的 `C_i` 定义文字内、一项在价值桥、两项门内无对应——有实质重叠与 GOV-SUB01 refit-budget 风险，但**准入条件成分重叠不蕴含非正交，是否独立轴未决**；`o` 若写成**封闭单标量**会与 `Core/SRT_OPEN_TENSIONS.md §9` 的 closure-boundary 冲突，但 §9 Direction 2 反而要求继续 operationalize，故分解式读数 / fallibilist proxy **未决**；`d` 取参与率与 `Def-d-canonical` 范数定义冲突）。**全部路由为候选，无一落地**；已加下游护栏：符号重命名与 `q` / `o` 的形式选择做出前，`d/q/o` 不得进入书稿、公共内容、bridge 或论文。**待作者裁决**：`q` 是否与 `d` 正交、`o` 是否设符号。
- `2026-07-22`：**Learnable Novelty 材料卡完成并按高优先级 B1 停驻**。新增 `Materials/2026/SRC_2026_07_20_AI_Zhang_Levin_Learnable_Novelty.md`，完成 Zhang–Levin arXiv `2607.18433v1` 24 页全文精读；代码已声明但本轮未复现。稳定增量：observer-relative learnable-structure yield、`W_sel x S^phi_future` 二维分解、future learnability endpoint、structured novelty 与 residual noise 分离，以及 observer-ensemble / observer-swap 防目标利用门。关键边界：`S^phi != Ψ_f != d != W_sel`；可学习结构不等于价值、stake 或主体性；Rule 110、soliton、MNIST 聚类和 RL exploration 不构成统一智能证明；论文对 FEP 和 universal computation 的强叙述需降级。`Operations/Material_Log/2026-07_Part01.md` 与 `Operations/_SRT_MATERIAL_LOG.md` 已同步；未修改 canonical、HDR/selective-resynchronization 正文或正式 PatchNote。复活触发：HDR 增 future-structure endpoint、selective-resynchronization 需要区分噪声与结构重组、完成代码复现或 cross-observer / observer-swap 测试、论文新版本或同行评审回应 fixed-observer exploitation 与外推风险。
- `2026-07-21`：**热力学计算材料卡完成并按高优先级 B1/B2 停驻**。新增 `Materials/2026/SRC_2026_07_15_Computing_Ball_Thermodynamic_Computers_Quanta.md`，完成 Quanta 全文与 Melanson et al. 2025 SPU 硬件、Whitelam–Casert 2026 非平衡计算、Whitelam 2026 生成式计算、Jelinčič et al. 2026 概率硬件架构的分层交叉读取。稳定增量：`N-C-R-W-B` 审计（noise / constraint / readout / write-back / bearer）、trajectory computation、trained stochastic scaffold，以及“随机可被约束组织但噪声本身不选择”。关键边界：`N + C + R` 可实现真实计算，但不推出 `W_sel + bearer`；外部训练能量地形不是系统拥有的选择史；低热耗散不等于低 canonical `Ψ_f`；概率生成不证明 stake 或意识。`Operations/Material_Log/2026-07_Part01.md` 与 `Operations/_SRT_MATERIAL_LOG.md` 已同步；未修改 canonical、Physics/AI 正文、source trace 或论文正文。复活触发：selective-resynchronization related work、熵—随机—再同步 bridge 获作者成文确认、HDR external-programming/stochastic negative control、AI 点名 thermodynamic/probabilistic hardware、`Ψ_f` 完整能耗账本或公共文章点名该案例。
- `2026-07-21`：**水结冰材料卡完成并按 B1/B2 停驻**。新增 `Materials/2026/SRC_2024_06_17_Physics_Cutts_Water_Freezing_Quanta.md`，完成 Quanta 全文与 Dhabal–Kumar–Molinero PNAS `10.1073/pnas.2322853121` 全文交叉读取。稳定增量：`stability != reachability`、`manifestation != anchoring`、scaffold 作为成本重排器、晶格形成后的 inherited pre-trimming；关键边界：过冷水不是 `L_0`，成核势垒不是 canonical `Ψ_f`，物理路径依赖与一般写回不构成 `W_sel`、主体性或 consequence-return。`Operations/Material_Log/2026-07_Part01.md` 与 `Operations/_SRT_MATERIAL_LOG.md` 已同步；未修改 canonical、Physics 正文或 history-dependent reachability 论文正文。复活触发：HDR natural comparison / negative-boundary、`Ψ_f` physical-proxy taxonomy、Physics nucleation/metastability 任务或公共文章点名该案例。
- `2026-07-20`：**治理减负轮完成**。①Operations 51 个一次性记录归档入 `Operations/Archive_Records/`；②根目录 22 个停驻文件迁入 `90_Backstage/Incubation|Plans_Archive/` 等层，新建 `_SRT_PARKED_INDEX.md` 停机坪索引（下沉必须带复活触发条件）；③7 个 coverage index 冻结为快照，5 个休眠域入口加冻结戳（canonical 漂移免同步声明 + touch-based repair）；④状态面收口为本文件单面（`STATUS_FAST.md`、`STATUS_Split/` 删除）；⑤boot 读单 4→3（symbol quick guard 并入 `SRT_AI_START.md`）；⑥router 三个扩展并回主文件；⑦人类入口四合一进 `SRT_Navigation_Map.md`；⑧frontmatter 最小 schema 棘轮 + B 类裁决语义改停驻 + 治理四原则入 `Governance/README.md`。记录：`Governance/Governance_Load_Reduction_2026-07-20.md`。
- `2026-07-10`：**Choice-trace 回写计划 Phase 1 执行完成（2026-07-10 PR 复审后修正）**。理论侧三项：`Core/SRT_OPEN_TENSIONS.md` 新增 §12（熵去选择化读法，标注 ontological absence / theoretical abstraction 校准未完）+ §7 追加两条 P0-04 直觉证词；`04_External_Convergence/FIRST_EVIDENCE_CANDIDATES.md` 新增 Candidate 8（脆弱性—选择空间收窄候选方向，按 `FIRST_EVIDENCE_CANDIDATES.md` 自身纪律未编造/未核实任何具体引用——**注意这只是候选登记级，回写计划原定的正式证据卡【`EVIDENCE_CARD_TEMPLATE.md` + `EVIDENCE_INDEX.md`】尚未开始，需先完成一手文献 close-read**）；`Philosophy/SRT_Political_Philosophy.md` §6.2 新增显现权/分配权词汇对表注防平行术语。书稿侧四章（按作者 2026-07-10 冻结豁免裁决，不受 RC1 冻结约束，直接改章）：`Q06`→v22（章末注九：边界作为存在成分候选，交 Q07 检验；三分——成功选择/失败选择/未完成选择——已恢复，不再把失败与未完成并成一类）、`Q19`→v18（新增章末注：四分层与五步病理学为不同海拔的候选对照）、`Q22`→v29（章末注七："1432 循环"去遮蔽→解笼→重建尺度→重分配操作顺序候选，标注"重建尺度"锚点最弱）、`Q28`→v19（章末注七：熵的位置——两种未决读法并列，不替 `Core/SRT_OPEN_TENSIONS.md §12` 选边，"选择耗尽↔熵增终态"等同已弱化为"可能存在结构类比"——+ "没有选择→退化→脆弱性提升"负向链，一并承接原定位于 Q18/幕前·五的熵素材）。全部新增均为候选性质章末注，不改写任何既有正文段落，不补术语表词条（未达正文核心概念密度）。`BOOK_VERSION_LOG.md` 已记录冻结豁免授权与范围。**Phase 2/3 未执行**：门 G1/G2/G4/G5/G6 是作者裁决项，不可由执行者代为拍板，待下一轮对话清点；T-C 边界 bridge 例外——本身无门，回写计划执行顺序表此前误将其挂在 G4/G6 下，已订正为可独立推进。
- `2026-07-10`：**Choice-trace 回写计划立项**。新建 `Operations/_SRT_CHOICE_TRACE_WRITEBACK_PLAN_2026-07-10.md`：基于两份 2026-07-09 trace 的收尾审计，整理理论层七条轨道（T-A OPEN_TENSIONS 登记【熵去选择化张力 + P0-04 两条直觉证词】、T-B 熵—随机—再同步合并 bridge、T-C 边界作为存在成分 bridge、T-D 跨域选择条件文件【"选择地基"改名后】、T-E 耗散结构 vs 选择结构 bridge、T-F 脆弱性证据卡、T-G 政治哲学词汇对表）与书稿层两条轨道（B-A **直接改章**清单八项【Q06 边界收口、Q19 四分层、Q20/Q22 1432 循环、Q28+幕前·五负向链、Q18 熵章末注、Q21、Q15、术语表随动】、B-B 素材池）。**书稿冻结豁免（2026-07-10 作者裁决）**：本计划书稿轨道不受 RC1-candidate 冻结约束，直接改章执行；首次动章时在 `BOOK_VERSION_LOG.md` 记录解冻授权与范围，术语指南/定梁页验收/frontmatter 同步等其余书稿治理纪律不豁免。七个门（G1–G7）组成作者裁决包阻塞相应轨道；trace2 升级轮（§0a）已消解 G3（T1 分层改写已应用）与 G7（选项全集已补收），剩 G1/G2/G4/G5/G6 待裁决；执行分四阶段，Phase 1（OPEN_TENSIONS/证据卡/对表/notes 骨架）无门可立即动工。边界：计划非执行，各项动工须走冻结/编辑/书稿治理既有协议；pending 命题确认前禁止进入任何回写正文。
- `2026-07-09`：**ChoiceMap 轨迹工作流 v2：一致性压测（反服从性）+ 第二份 trace 收尾补全**。`Operations/_SRT_CHOICEMAP_TRACE_WORKFLOW.md` 升 v2：新增 §4a 一致性压测协议（承诺台账、张力即报、每轮挑战项、张力轮节奏；原则=揭示张力是发散义务、解决张力只归作者；处置四类 revised_old/revised_new/layered/retained_as_tension，禁止"不了了之"）、§2a 暂停/恢复协议（暂停点冻结候选选项全文、恢复先清二次确认队列）、第五确认状态 `author_accepts_contextual_selection`、收尾管线 §5.0 张力审计（张力表为 trace 固定组成，空表须解释）、§7 粘贴即用对话提示词（把反服从性烧进自由对话开场）。台账指针模板增补 tension 字段并登记 CT2-20260709。第二份 trace（`SRT_CHOICEMAP_RANDOM_RESYNCHRONIZATION_TRACE_2026-07-09.md`）补 §7 回写审计：张力表 4 条（T1 痛苦最原始 vs 去同步化先行【intra，建议 layered】、T2 选择过程定义 vs 第一 trace 操作定义【inter】、T3 痛苦用法 vs `Core_Law/SRT_Suffering.md` 类型学【vs_canonical】、T4 幸运开放 vs P0-04【retained】）；canonical 碰撞三态（P2-14 与 L0 随机性论证兼容应挂锚、显现权/分配权与 `Philosophy/SRT_Political_Philosophy.md` 近亲需交叉链接、机制链/1432 循环/分配先于显现为真实增量）；数据质量缺陷登记（选项全集未逐字回收，待原对话补收，有时效）；已登记 INDEX 与台账。另记正向收敛：trace1 P13（熵=去选择化画像）与 trace2 P2-14（选择=对随机再同步）构成对偶，建议合并立 bridge。边界：全部非 canonical；张力表不判定谁对，解决权在作者。
- `2026-07-09`：**ChoiceMap 轨迹工作流落地 + 第一直觉 trace 收尾补全**。新建 `Operations/_SRT_CHOICEMAP_TRACE_WORKFLOW.md`：区分三用途（决策支持/文章/直觉挖掘）×两记录模式（live/retro_writeback），把"自由对话→事后回写"正式化为一等记录模式，新增越界选择（breakout）一等事件、委托收敛协议（assistant_proposal 不得未经二次确认进入命题簇）与收尾管线（canonical 碰撞检查→术语撞车检查→路由→落库）。`Operations/_SRT_CHOICE_TRACE_LOG.md` 增补 `trace_type` 字段与指针条目模板，并登记首条轨迹。`SRT_FIRST_INTUITION_SELECTION_BEFORE_EXISTENCE_CHOICE_TRACE_2026-07-09.md` 补 `trace_mode: retro_writeback` 声明与 §6 回写审计：P8「选对」侧与 P14 耗散结构排序标为 `assistant_proposal_pending` 待作者二次确认；新候选命题 P6/P10/P12/P13 完成路由建议（P13 熵定位建议进 OPEN_TENSIONS + bridge；P2 挂 P0-04 护栏）；发现「选择地基」与书稿 Q17 术语撞车（进入书稿/理论/产品线前须改名或分义）。已登记入 `01_Source_Intuition/INDEX.md`。边界：工作流为运行层，非 canonical；trace 命题一律不因走完流程获得定义权威。

（更早条目见 `Operations/Status_History/2026-04_to_2026-07_Dashboard_Part.md`）

## 当前高优先事项

- 书稿 RC1-candidate：choice-trace 回写 Phase 2/3 待作者裁决包（G1/G2/G4/G5/G6）
- 论文线：Frontiers 稿 1837760 major revision 施工；Adaptive Behavior 重投（common-state probe 分支停驻，见 `_SRT_PARKED_INDEX.md §3`）
- 保持 canonical 主链不被入口优化反向污染
- 治理可观测指标看板：boot 必读 3 文件 / 根目录 md ≤ 60 / navigation 占比下降 / 状态镜像唯一（详见 `_SRT_QUALITY_METRICS.md`）

## Pipeline 快照

- `Pipeline 1`：材料融合继续有效；B 类语义自 2026-07-20 起为"停驻 + 具名触发条件"（见 `Operations/_SRT_MATERIAL_PIPELINE.md`）。最新高优先级 B1 卡为 Learnable Novelty：可作为 observer-relative future-structure proxy，但严格保留 `S^phi != Ψ_f != d != W_sel`，待代码复现和 cross-observer 防利用测试；热力学计算卡继续承担 `noise + constraint + readout` 不推出 `W_sel + bearer` 的边界；水结冰卡继续承担 `P / W_global` 不推出 `W_sel` 的自然边界。
- `Pipeline 3` / `Pipeline 6`：按 `Operations/_SRT_OPERATIONS_SCHEDULE.md` 执行
- Pipeline 5 主模式：`Operations/_SRT_ARTICLE_WORKFLOW.md`

## 当前工作边界

- 书稿正文默认冻结（RC1-candidate，2026-06-19；choice-trace 轨道按 2026-07-10 作者豁免裁决直接改章，其余纪律不豁免），走 `Governance/SRT_EDIT_PROTOCOL.md`
- 理论文件（canonical）编辑先看 `Governance/SRT_CANONICAL_FREEZE.md` 与 `Governance/SRT_EDIT_PROTOCOL.md`——理论冻结不受书稿豁免影响
- 休眠层只做 touch-based repair，不开专项治理轮
