---
id: SRT-PARKED-INDEX
type: index
status: active
claim_mode: navigation
updated: 2026-08-12
---

# SRT Parked Index — 停驻内容总索引（浮标）

本文件是全仓**停驻内容的唯一总索引**：被下沉、降级、延后的内容在这里留浮标，写明"什么事件发生时它应该浮上来"。

原则（对应治理原则②）：**任何过滤器必须自带回流路径——没有复活触发条件的下沉等于删除。** 触发条件绑定工作线事件，不绑日历；触发发生时，由当时的任务把对应条目捞起并从本索引销账。

## 1. 研究种子 / 候选提案（`90_Backstage/Incubation/`）

| 条目 | 复活触发条件 |
|---|---|
| [方向2：道德谱系种子](90_Backstage/Incubation/_SRT_DIRECTION2_MORAL_GENEALOGY_SEED.md) | 书稿 RC 冻结后重启理论推进线；或 ε-normativity 张力（`_SRT_EPSILON_NORMATIVITY_OPEN_TENSION.md`）被正式处理时 |
| [方向2：相变对决](90_Backstage/Incubation/_SRT_DIRECTION2_PHASE_TRANSITION_DUEL.md) + [Wedge1 模拟](90_Backstage/Incubation/_SRT_DIRECTION2_WEDGE1_SIM_RESULTS.md) / [Wedge2 模拟](90_Backstage/Incubation/_SRT_DIRECTION2_WEDGE2_SIM_RESULTS.md) / [Wedge2 攻击日志](90_Backstage/Incubation/_SRT_DIRECTION2_WEDGE2_ATTACK_LOG_2026-07-01.md) | 方向2 工作线重启；或某篇论文需要 wedge 模拟证据时 |
| [方向3：ChoiceMap 原型种子](90_Backstage/Incubation/_SRT_DIRECTION3_CHOICEMAP_PROTOTYPE_SEED.md) + [校准集](90_Backstage/Incubation/_SRT_DIRECTION3_CHOICEMAP_CALIBRATION_SET.md) / [产品感 memo](90_Backstage/Incubation/_SRT_DIRECTION3_CHOICEMAP_PRODUCTFEEL_MEMO.md) / [运行结果](90_Backstage/Incubation/_SRT_DIRECTION3_CHOICEMAP_RUN_RESULTS.md) | IRP / ChoiceMap 产品线重启（参照 `Product/ChoiceMap/`；IRP 规划 2026-06-17 采纳默认） |
| [方向3：L0 探针研究种子](90_Backstage/Incubation/_SRT_DIRECTION3_L0_PROBE_RESEARCH_SEED.md) | 下一轮 L0 深挖或论文选题轮（Pipeline 2）点名 |
| [方向3：论文停驻注](90_Backstage/Incubation/_SRT_DIRECTION3_PAPER_PARKING_NOTE.md) | 论文候选池下次运行（触发词 `论文候选`） |
| [D3 选项空间读出注](90_Backstage/Incubation/_SRT_D3_OPTION_SPACE_READOUT_NOTE.md) | 方向3 任一条目复活时一并评估 |
| [分配可支付性候选种子](90_Backstage/Incubation/_SRT_DISTRIBUTIONAL_PAYABILITY_CANDIDATE_SEED.md) | Ψ_f / payability 相关 canonical 工作再开时 |
| [审计者独立性候选注](90_Backstage/Incubation/_SRT_AUDITOR_INDEPENDENCE_CANDIDATE_NOTE.md) | 治理审计工作线（GOV-SUB01 残余处理）再开时 |
| [规范性 framing true-up 提案](90_Backstage/Incubation/_SRT_NORMATIVITY_FRAMING_TRUEUP_PROPOSAL.md) | ε normativity 张力升级为正式修订、或 L0 修订获授权时 |
| [对象性=可再选择性元标准](90_Backstage/Incubation/_SRT_OBJECTHOOD_AS_RESELECTABILITY_META_STANDARD.md) | 对象暗线扩展（Q02 试点 PR #593 之后）或 `papers/selective_resynchronization/` 推进时 |

## 2. 材料管线 B 类停驻（`Materials/`）——入口指针

**逐卡复活触发条件的唯一权威源是 `Operations/_SRT_MATERIAL_LOG.md`**（分月记录见 `Operations/Material_Log/`），本索引不逐卡登记、不做第二份台账。恢复任务从台账按域/主题检索 B 卡，读其备注列的触发条件。

- B 类语义自 2026-07-20 起为：**停驻 + 具名触发条件**（写在 Material Log 备注里），不再默认排队等待第二轮审计；规则详见 `Operations/_SRT_MATERIAL_PIPELINE.md §B 类语义修订`。
- 默认策略：对应域的活跃工作线（书稿章节、论文、公共内容）点名该主题时做 close-read；无人点名则作为档案永久停驻，不产生义务。
- 台账中已写明"候选后续落点"的条目，落点文件被实质修订时应顺带评估该卡。

## 3. 分支 / PR 层停驻（不在 main 上的已完成工作）

| 条目 | 位置 | 复活触发条件 |
|---|---|---|
| Costly Selection common-state probe + Adaptive Behavior build | branch `claude/common-state-probe`（9fde3ff0 / e483a5c6） | Adaptive Behavior 重投轮启动时 |

> P1-T07 证明审计已于 2026-07-25 随 PR #676 合入 main。2026-08-11 作者选择 ST-A 后，本项作者门已销账：无条件 P1 身份撤销，absorption remainder 留在 21B，neutral-kernel anti-closure 转入 21C B13 的 P2/P3 条件候选。Options A/B/C 仅保留为历史；未来若尝试条件 theorem，仍须选定稳定语义、独立定义 neutral kernel，并证明吸收或比较性 closure-risk bound。

> `Operations/Proposals/SRT_CONSISTENCY_DECISION_PACKET_2026-08-11.md` Gate A 已由 EX-A 销账：manifest actuality、anchoring persistence 与 stable ISP 分层，旧 `E = 1-H(L_1)/H(L_0)` 仅在 21C B14 保留为历史启发式。量化 anchoring readout 不再构成 canonical 待办；只有具名 P3 测量工作线同时给出相对域、分割／sigma-algebra、概率测度、有限性条件与事件／时间窗时，才可复活为模型级候选。Gate B 后由 B-A 关闭，Gate C 后由 C-A 关闭。

> 位置无关、宇宙尺度、带语义／评价内容的 `global optimum` 已由 C-A 停驻，不是当前 canonical 待办。只有作者明确重开 C-B，且同一工作线补齐承载对象、跨主体／尺度／时间的聚合或偏序、闭包边界、可支付／可协调／不外包／可再选择冲突规则、存在性／唯一性、有限算子的 epistemic bridge 与失败条件时，才可复活为 L₁+ 作者级承诺；技术性 model-global optimum 不受此停驻影响。CΨ 的 `Ψ_f→0` 价态是独立开放作者门，不以此条替代。

> C-A 同步停驻的具名旧载体包括 `Core_Law/SRT_Reference_Axioms.md A12` 的“同一原初全局算子分化”、`Core_Law/SRT_Reference_Ontology.md O14 / Hyp-O8 / O15` 的全局算子与 L₀ 真善美最优流形、`Core_Law/SRT_Reference_Dynamics.md §8.4` 的 $B_{L_0}$ 至福牵引项，以及 `Core_Law/SRT_Reference_Scaling.md Def-Scale-TEL-1` 把评价性 $d_{pull}$ 加进 canonical `d` 的旧式。它们共享上一条 C-B 复活门；不得以历史编号、glossary 旧别名或 split 镜像绕过。

> `Physics/SRT_Physics_Cosmology.md Ax-Cosmo-2 / §5.1` 的“Big Bang = $\arg\min_{\sigma\in L_0}K(\sigma)$”亦已停驻。只有具名 cosmology workline 给出可观测关联的状态空间、复杂度量、可行域／闭包、存在与唯一性条件、竞争模型和失败测试时，才可作为 P3/P4 技术模型复活；不得恢复为 $L_0^{abs}$ 的无条件定义。

> `Core_14` 的旧跨尺度熵证明与无条件 strict conjugacy 已于 2026-08-12 停驻。它们只有在具名 P3 跨尺度工作线同时声明两侧状态空间、尺度映射、可逆性或近似交换误差界、保留观测量、比较范数、熵变量／测度以及可区分于普通路径依赖／吸引子／粗粒化描述的失败测试时才可复活。否则只使用 P3-B06／T-Scale-02C1 的条件接口。

> 神经除法归一化的“本体必然／能量—信息唯一交点／直接产生行为选择”强式已于 2026-08-12 停驻。具名工作线 `NB1-MOFC-Lottery-v0` 已在 `Neuroscience/SRT_NB1_MOFC_LOTTERY_EXECUTION_CARD_v0_1.md` 定义，但只到 P4 card-defined 黄灯，尚未通过 formal lock、预注册或执行门。只有该类实验同时冻结候选身份映射、神经读出、阈值／累积或采样规则、执行门、held-out 分割、误差容差与 rival 集合，并提供神经参数独立估计及干预跟踪时，才可复活为任务局部机制主张；任何局部成功都不复活“所有选择系统必然归一化”或机制同一主张。

## 4. 计划存档（`90_Backstage/Plans_Archive/`）

| 条目 | 复活触发条件 |
|---|---|
| [实践共同体计划](90_Backstage/Plans_Archive/SRT_PRACTICE_COMMUNITY_PLAN.md) | 社区 / 公开运营线重启时 |
| 2026-04 优化 TODO / Backlog | 无（已被 2026-07-20 治理减负轮取代，仅作史料） |

## 销账规则

- 条目被捞起并完成 → 从本索引删除该行，在触发它的工作线 PR 里说明。
- 条目被判定永久废弃 → 从本索引删除该行，文件留在原archive位置即可，无需另行留痕。
- 新的下沉动作（降级、种子停驻、分支/PR 停驻、计划存档）→ 必须同步在本索引加一行，否则不得下沉。**例外：材料管线 B 卡**——其触发条件唯一登记在 Material Log（见 §2），不在本索引逐卡加行。
