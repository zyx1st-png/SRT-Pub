---
id: SRT-PARKED-INDEX
type: index
status: active
claim_mode: navigation
updated: 2026-07-20
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
| P1-T07 证明审计（含 Options A/B/C，推荐 B=降为条件定理） | PR #676（未合并） | 用户授权 P1-T07 修复方案时先合审计，再开受权 amendment PR |
| Costly Selection common-state probe + Adaptive Behavior build | branch `claude/common-state-probe`（9fde3ff0 / e483a5c6） | Adaptive Behavior 重投轮启动时 |

## 4. 计划存档（`90_Backstage/Plans_Archive/`）

| 条目 | 复活触发条件 |
|---|---|
| [实践共同体计划](90_Backstage/Plans_Archive/SRT_PRACTICE_COMMUNITY_PLAN.md) | 社区 / 公开运营线重启时 |
| 2026-04 优化 TODO / Backlog | 无（已被 2026-07-20 治理减负轮取代，仅作史料） |

## 销账规则

- 条目被捞起并完成 → 从本索引删除该行，在触发它的工作线 PR 里说明。
- 条目被判定永久废弃 → 从本索引删除该行，文件留在原archive位置即可，无需另行留痕。
- 新的下沉动作（降级、种子停驻、分支/PR 停驻、计划存档）→ 必须同步在本索引加一行，否则不得下沉。**例外：材料管线 B 卡**——其触发条件唯一登记在 Material Log（见 §2），不在本索引逐卡加行。
