---
id: SRT-REVIEW-QUEUE
type: framework
status: active
claim_mode: governance
updated: 2026-08-12
version: v2
layer: meta
epistemic_layer: os
dependency: [SRT-DAILY-REVIEW-PIPELINE, SRT-EQ-HYP-MAP]
---

# SRT 待人工审查队列

> 本文件区分作者裁决、触发式延期、自动扫描待分类和已解决记录。自动扫描不得直接生成作者级结论；Operations 也不得替 canonical owner 宣布废止。

## 优先级

- **High**：需要作者决定，或会影响入口、变量、claim level 与下游引用；
- **Med**：有效研究／工程任务，但不阻塞当前主线；
- **Low**：触碰相关工作线时顺带修复的治理债务。

---

## A. 当前需要作者裁决

| 编号 | 来源 | 决策问题 | 当前护栏 | 优先级 | 状态 |
|---|---|---|---|---|---|
| RQ-2026-08-A01 | `Core_Law/SRT_Core_Text_CN.md` / `SRT_Core_Text_CN_Euclid.md` / `SRT_Selection_Argument.md` | Euclid 是否正式升格为中文入口，还是维持“legacy CN reader entry + Euclid candidate”的现状 | 未裁决前不修改 registry、manifest 或三文件定义权 | High | Awaiting author |
| RQ-2026-08-A02 | `01_Source_Intuition/Conversations/2026-07-25_具身位_d_q_o_收尾审计.md` | `q` 是 stake gate 后的构成深度剖面还是独立轴；`o` 是否操作化、是否设符号 | 形式选择完成前，`d/q/o` 不得进入书稿、公共内容、bridge 或论文 | High | Awaiting author |
| RQ-2026-08-A03 | `Core/SRT_Core_01_Axioms.md` / `Governance/SRT_POSITIONING.md` | `Ax-Core-A10/A11` 的 Part B 实验钩缺口是否仍存在；若存在，是在 Core_01 补、在当前 P2–P4 架构落地并 cross-reference，还是已被现有接口覆盖 | Core_01 仍是 canonical owner；未正式裁决前不得宣布 superseded 或禁止回写 | High | Awaiting re-adjudication |
| RQ-2026-08-A04 | Physics P03/P04/P05 hooks；`Operations/Audits/Hook_Closure_Audit_2026-07-25.md §3.3` | 三张 patch 统一落到新建 `Physics/SRT_Physics_Bridge_v0_2.md`，还是并入现有 `Physics/_SRT_Phys_Bridge.md` | 只裁决 landing；不升级 Physics claim level | High | Awaiting author |

统一裁决包：

`Operations/SRT_AUTHOR_DECISION_PACKET_EUCLID_DQO_PHYSICS_A10A11_2026-08-05.md`

相邻第一性主链的新裁决包：

`Operations/SRT_STABILISATION_AUTHOR_DECISION_PACKET_2026-08-11.md`

---

## B. 触发式延期任务

| 编号 | 原发现日期 | 来源 | 当前裁决 | 复活触发 | 优先级 | 状态 |
|---|---|---|---|---|---|---|
| RQ-DEF-01 | 2026-03-11 | `_SRT_VERTICAL_INTEGRATION.md §4.5` / Eq-Multi-03 | `D_eff(F_collective)` 测量代理仍是有效 P4 问题，但不属于当前材料／投稿收口 | 集体选择实验或 unified formal-core paper 正式重启 | Med | Deferred |
| RQ-DEF-02 | 2026-03-16 | `_SRT_EQ_HYP_MAP.md` / G2 Wikimedia MVP | LDP 数据管线为 Partial 后续；小样本扩展需独立实验计划 | G2 / LDP 工作线点名，且先冻结窗口、映射和判断规则 | Med | Deferred |
| RQ-DEF-03 | 2026-03-02 | `_SRT_EQ_HYP_MAP.md` | 经济学和演化 bridge 未建立，但休眠域不因旧季度计划自动开工 | 论文、书稿或跨域审计明确需要该 bridge | Med | Deferred |
| RQ-DEF-04 | 2026-03-09 | `Operations/_SRT_DAILY_REVIEW_PIPELINE.md` | 占位模式示例可能产生误报 | Pipeline 6 checker 被触碰或误报再次出现 | Low | Touch-based |
| RQ-DEF-05 | 2026-03-09 | 旧扫描中的 26 个 d-value 引用命中 | 旧计数已过期，禁止按“26 文件”盲目批处理 | 新 governance audit 重新生成当前清单 | Low | Re-audit required |

这些条目不是按时间自动排队的当前欠账。

---

## C. 自动扫描待分类

Pipeline 6 只能把原始发现追加到本区，不得直接写入 A/B，也不得自动判定 canonical 废止、作者选择或理论优先级。

| 扫描日期 | 来源文件 | 原始发现 | 检查类别 | 建议严重度 | 分类状态 |
|---|---|---|---|---|---|
| — | — | 当前无待分类扫描项 | — | — | Empty |

人工分类后：

- 需要作者决定 → 移入 A；
- 有具名触发条件但不阻塞 → 移入 B；
- 已修复、误报或已被覆盖 → 移入 D；
- 信息不足 → 保留本区并补核验任务。

---

## D. 已解决、误报或被覆盖

| 原发现日期 | 处理日期 | 来源 | 原问题 | 处理方式 | 状态 |
|---|---|---|---|---|---|
| 2026-08-11 | 2026-08-12 | `Operations/SRT_CROSS_SCALE_ENTROPY_FLOOR_AUDIT_2026-08-12.md` | `Core_14` 以未定义 `H(L_0)`、无条件粗粒化熵式、普遍最小作用与通常不可逆的 `Λ^{-1}` 支撑跨尺度共轭 | 旧证明撤回；P3-Scale-01／B07 降回条件性桥，通用接口采用 B06／T-Scale-02C1 近似交换；T-Scale-Rhythm-5 标为 P3/P4 条件模型 | Resolved at claim-mode / proof-load level |
| 2026-08-12 | 2026-08-12 | `Operations/SRT_NEURAL_NORMALIZATION_BEHAVIORAL_SELECTION_FLOOR_AUDIT_2026-08-12.md` | 神经入口把除法归一化写成所有受限选择的本体必然／唯一极值解，并从相对响应跳到行为选择与跨尺度同构 | 广义连接判红；Core14 登记 P3-Scale-NB1 有界合同，Core13a 与神经 owner／CompactCore／claim-status 降级并补冻结读出、held-out、rival、干预与事件门 | Resolved at claim-mode; empirical P3 execution open |
| 2026-08-11 | 2026-08-11 | `Operations/SRT_STABILISATION_AUTHOR_DECISION_PACKET_2026-08-11.md` | structural stability、continued selectability、generative reselectability 与 metastability 混层；P1-T07 无条件概率证明未闭合 | 作者选择 ST-A；P1-T06 保留 continued selectability，generative reselectability 降到 P2/P3；former P1-T07 撤销无条件 P1 身份，保留 absorption remainder 与 21C B13 条件候选 | Resolved by author; landed |
| 2026-08-11 | 2026-08-11 | `Operations/SRT_ACTUALISATION_AUTHOR_DECISION_PACKET_2026-08-11.md` | P0-01/P0-04 的 primitive/open 口径与 Ax-L0-Bootstrap 的 fixed-point “正式消解”互相冲突 | 作者选择 AM-A；actualisation 明确为既有 selection primitive 的最小内核；删除 fixed-point / 最陡下降的 universal derivation，保留 plural domain implementations | Resolved by author; landed |
| 2026-08-11 | 2026-08-11 | `Operations/SRT_POSSIBILIA_CONSERVATION_AUTHOR_DECISION_PACKET_2026-08-11.md` | `Conservation of Possibilia` 的内容／基数守恒与创新即发现读法，和上位 L0 的真实新颖性、历史雕刻与 anti-preformation 护栏冲突 | 作者选择 PC-A；Ax-L0-02 / A13 改为潜在不可穷尽，T-L0-01 改为非预成的新颖性；actualisation mechanism 继续开放 | Resolved by author; landed |
| 2026-08-11 | 2026-08-11 | `Operations/SRT_PHYSICAL_REALISATION_AUTHOR_DECISION_PACKET_2026-08-11.md` | AM-A 在物理域采用 interpretation-plural audit、collapse-family 优先，还是只保留 operational registration | 作者选择 PHR-A；Physics 采用共同 P3/P4 事件审计核并显式区分 collapse-family、Everett／branch-relative 与 operational／instrument 口径；不建立解释中立的普遍物理机制 | Resolved by author; landed |
| 2026-08-11 | 2026-08-11 | `Operations/SRT_EXISTENCE_AUTHOR_DECISION_PACKET_2026-08-11.md` | P0-01 event actuality、P0-02 anchoring persistence 与 P1-T06 stable ISP 被“existence”一词压成一层；旧 `E` 式与 `H(L_0)=∞` 冲突 | 作者选择 EX-A；三层分离，旧 `E` 式降至 21C B14 历史启发式；未采用全局熵、归一化或量化 existence index | Resolved by author; landed |
| 2026-03-16 | 2026-03-16 | `_SRT_EQ_HYP_MAP.md` | Eq-LDP-01 / Eq-LDP-02 为 Gap | 已推进为 Partial；后续数据执行转入 RQ-DEF-02 | Resolved at mapping level |
| 2026-03-05 | 2026-03-16 | `_SRT_EQ_HYP_MAP.md` | Eq-Select-Thermo / Eq-LDP-01 / Eq-LDP-02 三条 Gap | Eq-Select-Thermo 已推进为 Partial；不得继续写作“三条 Gap 未补” | Resolved at mapping level |
| 2026-03-02 | 2026-03-11 | `_SRT_VERTICAL_INTEGRATION.md §4` | d_collective 聚合方案未形式化 | 框架层已形成 collective landscape 与 Eq-Multi-01/02/03；实证代理另列 RQ-DEF-01 | Resolved at framework level |
| 2026-03-02 | 2026-03-02 | 多文件 | d-value 定义分裂 | `_SRT_D_VALUE_CANONICAL.md` 已统一定义 | Resolved |
| 2026-03-02 | 2026-03-02 | `Neuroscience/SRT_Neuro_10_Advanced_Models.md` | 感受—摩擦循环 | 已加入单向因果链声明 | Resolved |
| 2026-03-02 | 2026-03-02 | `Core/_SRT_Core_Bridge.md` | L2 语义漂移 | 已增加热力学封闭条件 | Resolved |
| 2026-03-02 | 2026-03-02 | `AI/_SRT_AI_Bridge.md` | AI 屏障永久／可突破歧义 | 已加入工程性／原则性区分 | Resolved |
| 2026-03-02 | 2026-03-02 | `Spirituality/_SRT_Spirit_Axioms.md` | Omega 拓扑极限与具身公理冲突 | 已加入边界声明 | Resolved |

---

## E. 入队规则

人工裁决项必须写明：当前 owner、作者决策问题、不处理阻塞、当前护栏和完成定义。

自动扫描项只需写明：日期、来源、原始发现、检查类别和建议严重度；不得伪装成人工裁决结果。

禁止：

- 用旧扫描计数代替当前审计；
- 把 open tension 自动转成开发 TODO；
- 把 trigger-based parked item 当作按时间排队的欠账；
- 由 Operations 宣布 canonical owner superseded；
- 在未经过作者门时自动修改符号、入口或 canonical claim level。
