---
id: SRT-GENERATIVE-MAINTENANCE-DESIGN-REVIEW-IMPLEMENTATION-HANDOFF-20261028
type: audit
status: draft
canonical: false
layer: operations
epistemic_layer: machine_analysis
claim_mode: internal_adversarial_review_and_conditional_implementation_contract
created: 2026-10-28
updated: 2026-10-28
research_mode: U
root_question: Are proposed causal contrasts well defined, non-tautological, implementation-ready, and fairly tested against mature models?
comparative_claim: none; the review attempts to defeat premature inference
named_comparator: organizational closure; homeostatic RL; full-capacity latent world-model learning
n_mode_triggered: false
dependency:
  - Operations/Proposals/SRT_GENERATIVE_MAINTENANCE_FULL_EXPERIMENT_DESIGN_V0_1_2026-10-28.md
  - STATUS.md
tags: [Audit, ExperimentProtocol, Simulation, FairBaselines, RedTeam, Handoff, PaperOnly]
---

# 方法学红队与未来实现验收契约 — 生成性自维系实验设计 v0.1

> **本文件属于同一 PR 的 AI 内部红队，不是独立同行评审、真实运行验收或结果报告。** 不负责更改 SRT/GRG 定义、当前 CURRENT NEXT、HOLD 或作者意向。只有设计层面的检查与未来审查要求；“测试应通过”不等于它已经通过。

## 1. 本次 paper-only 设计究竟解决了什么

前置讨论把两种机制混为一谈的风险很大：

- “外部差异对身体 A/B 的后果不同 → 模型学习不同关注点”，完全可能由成熟 HRL、条件化策略或 world model 解释。
- “组织本身被修复和重构 → 未来感知、维修和动作能否成功的条件发生变化”，需要实际转移因果、结构干预和未来效果；但这也可以由具身状态下的成熟 RL 实现。

主设计改为**先辨识世界中的组织关系，后测学习器如何使用该关系**。这是方法学增量，不是声称已有生命研究无人提出。G0 成立也不要求 G1 的特制模型胜出；成熟基线能成功是可接受结局。

## 2. 内部红队已识别的高风险点与最低修正标准

| 风险 | 为什么会摧毁推论 | 设计必须怎样做 | 目前状态 |
|---|---|---|---|
| R1 **把即时 J 开关当“生成”** | \`J=U\` 成功率 0.9，本来就是硬编码条件 | 把 J 对即时通行成功率的效果单列为 manipulation check；把组织修复/再组织在未见扰动下的跨时效应作为独立科学量 | 已写入主设计；未运行 |
| R2 **闭环组天生资源更多** | 模型差距是供给差，不是反馈结构 | healthy-state 校准边际保护流量、维修物料、信息、动作代价；切边采用预先定时外生同预算替代，并列 sham | 设计待校准 |
| R3 **状态不全／“神秘历史差异”** | 同一完整 Markov 状态、转移、未来策略下不应有额外魔法作用 | 检查滞后队列、组织状态、random tape、policy 内存，说明任何差异经过哪些当前因果状态 | 纸面 guard |
| R4 **把 cue 干预等同于 hazard 干预** | 改变传感器并非改变外界事件 | 分别写 \`do(q)\` 和 \`do(U,V)\` 的转移 API 与日志 | 纸面 guard |
| R5 **用弱固定编码器打全能模型** | 学习重切可能只是模型容量差 | 完整 B0/B1/B2 自适应表示和同等信息权、预算，固定 1-bit 只用于消融 | 纸面 guard |
| R6 **终止样本量混杂（CSC E1）** | 长寿组得到更多真实经验与更新 | 共同外部步数、记录有效 decision/update、冻结策略 common-bank、matched-update sensitivity；明确 episode token ≠ controller lineage | 纸面 guard |
| R7 **有限 J 原语冒充开放演化** | 只是先造后用预置按钮 | 报告 \`A_1\` 与 \`Reach_{H,p}\`；无界新规则、自生个体另立题，G1 不宣称 | 纸面 guard |
| R8 **human P6 与 synthetic outcome 混淆** | CN-2 是预测人的第一后果性行动，不是模拟世界的转移 | 此协议单独合成行为/Y_H，不宣称完成 CN-2 E2/E3/E4 | 纸面 guard |
| R9 **后果预测头 test leakage** | 用环境真值或同组合反馈训练了预测头 | 行为与实际后果日志分开，冻结 train-only 校准和 test cutoffs，防止 world-model privileged transition | 纸面 guard |
| R10 **开放循环校准不可能** | closed 与 open 在 healthy 分布也有显著差异 | 若匹配失败，撤回“机制隔离成功”主张，返回重新设计 g 或限制可识别目标 | 尚未验证 |
| R11 **过度认为反馈必然有益** | 某些反馈增加脆弱性、稳定性和适应性并非同一量 | 全报正/负/零效应、短/长 H、稳态/扰动、maintenance-only dead-end | 纸面 guard |
| R12 **人为奖励指定“生命”** | 新奖励标签可能直接驱动行为 | 不把 novelty/life/viability 作为候选专属目标；HRL intrinsic shaping 单独标注并对所有模型做相应敏感性组 | 纸面 guard |

**当前真实性：以上均属设计层检查，未有任何经验事实、独立 reviewer、CI pass 或计算确认。**

## 3. 未来实现的最小 config 记录（参数全部 PROPOSED，非 frozen）

本表是**参数 registry 初稿**；主设计允许校准之后经审阅修订。为避免“全写好了却无法复现”，任何实施版本必须填入最终 hash 与 freeze_date，再触碰确认数据。

| key | v0.1 建议初值 | 实现前必须澄清 |
|---|---|---|
| \`episode_horizon\` | 64 steps | 按回合还是跨回合评价？后者必须显式 controller lineage |
| \`E_cap,B_cap\` | 8, 4 | 与采集能量/每步耗能的安全边界 |
| \`module_cap\` | \`M=C=R=2\` | 初始 M/C/R 建议各 2，需另含单/双受损初态 |
| \`J\` | none / U / V | 制造成本 2 材料，替换是否消耗旧物并记录 |
| \`p_U,p_V\` | 0.20 each | 独立发现版与关联/非平稳评估版严格分离 |
| \`hazard_delay\` | 2 steps | cue_visible < event_effect 的时序无泄漏 |
| \`cue_accuracy\` | C≥1:0.85, C=0:0.50 | full-state ceiling 与等噪级 placebo |
| \`damage_p_no_J,damage_p_with_J\` | 0.75, 0.15 | 检查两个 hazard 的对称维修负担 |
| \`reward_for_successful_traverse\` | +1 external | 失败损失通过组织转移体现，无“life bonus” |
| \`return_to_safe\` | macro traverse ending safe | 必须核算一次往返的时间/扰动，不能得到免费瞬移 |
| \`G0_H\` | 4,8,16 | 对 DP 的状态规模、误差和 finite horizon sensitivity |
| \`G0_reach_p\` | 0.5,0.8 | 仅纸面敏感性建议，非经验阈值 |
| \`G1_debug_seeds,steps\` | 8, 50k/arm | 仅调通、调可辨识性，不能用于 confirmatory |
| \`G1_confirm_seeds,steps\` | 48, 100k/arm | 须经独立 review/power/systems budget，禁止 optional stop |
| \`G1_frozen_eval_tapes\` | 200/arm/seed | 独立新 tape，嵌套 seed，勿当独立样本 |
| \`G1_main_models\` | PPO-RNN, HRL-RNN, learned world model | 运行前填写版本、来源、观察/动作能力、搜索预算 |
| \`holdouts\` | unseen joint combo + time-forward perturbation | 两套独立 hash、每个 combo 首遇遮断反馈 |
| \`preregistration\` | none | 现阶段为 candidate design，作者未批准真实预注册 |

未来若发现这些建议值使所有臂全死或全部存活，需用**独立 debug** 修参数并在 confirmatory 之前加新版本锁定；不得对 confirmatory data 边看边调。

## 4. 动态系统的未来实现接口（并非代码）

\`\`\`text
reset(world_mechanism, state_initial, exogenous_tape, lineage_semantics)
  -> observation_t0, metadata

transition(world_mechanism, state_full, action, exogenous[t])
  -> state_next, observed_event, truth_event, reward_task, disabled_flag

clone_counterfactual(state_full, action_plan, exogenous_tape, intervention)
  -> time-locked paired trajectories

dp_viability(transition_kernel, K, horizon)
  -> state_to_probability_of_staying_in_K

dp_reachability(transition_kernel, target_event, horizon, reliability_cut)
  -> state_to_reachable_flag_and_optimal_policy

train(model_spec, legal_observation_contract, arm_spec, training_seed, split_spec)
  -> frozen_policy, training_trace, lineage_trace

evaluate(frozen_policy, first_encounter_holdout, paired_test_tapes)
  -> nested_episode_log, scored_predictions, action_and_effect_log
\`\`\`

**主设计中需事先封口的四项未决低层机制：**

1. \`return_to_safe\`：建议正式方案采用“traverse 一次动作完成往返”，并且 hazard、能耗每个 world step 只计一次；不能物理意义上往返需要两步，计算上只消耗一步却不声明。另一种方案是明确 2-step action，形成宏动作成本并让所有算法等权。**直到这点固定，世界转移仍是 proposal 而不是可运行规格**。
2. \`G_open\` 稳态流量匹配：需要具名 \`f(M,\xi)\` / \`g(t,\xi)\`；没有具体校准完成之前，不能把结果声称已隔离“闭合因果”。
3. \`H\` 连续失能计数：例如 C=0,R=0 两步计数，不得在 reset/介入时丢掉是否已连续失能一步的历史状态。
4. 确认性预测头：是否允许 B0/B1/B2 同权一个专用 probabilistic readout；若某模型本身没有环境预测头，则用相同 train-only probe calibration 过程；不可把原始 reward value 当某个 Y_H 的合法概率。

## 5. 设计检查清单与可供正式审查的分工问题

### A. 环境与因果

- [ ] 在 main 的控制门槛下，本协议是否仍只是纸面候选？
- [ ] 每一个状态字段实际影响哪条转移、在哪一步更新？能否用手算轨迹重建？
- [ ] 维修闭合的每条依赖是否由真实效应而非命名实现？
- [ ] open-loop 输入能否保持稳态资源/信息/成本，又不偷读未来与当前 M？
- [ ] 结构切断的正负效应是否均可出现？最弱反例是否保留？
- [ ] 把可达集定义成当前/有限时窗条件，能否避免 “新绝对可能性” 强宣称？

### B. 机器学习与统计

- [ ] 强 B0/B1/B2 是否拥有同等合法体态、结构学习、规划原语与历史观测？
- [ ] HRL intrinsic reward/drive 对照是否清楚？
- [ ] train/dev/held-out 与 first encounter 后果时钟是否全锁？
- [ ] 固定同策略 vs 允许再训练的系统效应是否明确区分？
- [ ] seed、world tape、测试 episode 的嵌套关系是否被正确建模？
- [ ] 失败、零效应、sham 等效、强 baseline 胜出是否作为有效结果，而非“失败需继续调参”？

### C. 理论 / 仓库与边界

- [ ] 个体显著性与 learned coarse-graining 是否均仅是局部科学代理，而非 d、Ψ_f、Selection、Bearer 定义？
- [ ] 组织闭合/内稳态 RL/既有状态抽象是否获得公平解释空间？
- [ ] 是否仅靠 G0/G1 toy 结果推断了完全无个体的生成世界？若是，判定 overclaim。
- [ ] 当前 CN-2 A P1–P6 人类行为任务是否原样保留？合成 Y_H 不得冒充人类选择预测。
- [ ] 是否需要运行/预注册/招募/下载或创建另一主线？若是，必须停止并另行授权；本 PR 不予批准。
- [ ] 是否将本文虚构为独立审查通过？如是则不可 merge。

**在没有真实独立审阅之前，以上全部是待检项目，而非已完成验收；本轮唯一已做的验证是文档引用/内容完整性回读。**

## 6. 后续实现验收与 Stop/Go 决策表

| 关口 | 必需交付 | PASS 条件 | FAIL 之后 |
|---|---|---|---|
| R0 文件审阅 | 版本化方案与内部红队 | 无明显非法授权或权威偷换；可供作者逐项讨论 | 修本文，不执行 |
| R1 独立审阅 | 方法学、动力学、强模型能力、来源对照 | 方法目标可识别、基线公平、参数可收敛；作者作明确授权决策 | HOLD |
| R2 小世界 G0 | 可手算转移 + DP + 干预 + 单测 | 有非平凡因果对照，open-loop 校准成立或承认局限 | NO GO，禁止 G1 |
| R3 G1 debug | 模型合法接口与少量种子 | 状态可学习、无泄漏、算量可承受、无明显算法 bug | 改 v0.2，仍不读 confirm |
| R4 confirm | 封存配置、独立 seed/tape、统计计划 | 完整包括零/负结果、所有评价可复现 | 结果 INVALID/HOLD 或有界报告 |
| R5 理论回读 | 成熟邻居 same-target 映射 | 作者与独立 reviewer 裁决，不从 toy 偷升本体论 | 维持 mature-source / no gain |

**无任何关口在此次 PR 中被实际执行或判定通过。** 下一次用户请求「开始运行」「合并」「冻结实验」时必须重新读取 merged main、当前 STATUS 与新审阅；本 PR 不能代替相应 author experiment authorization。

## 7. 参考与来源身份

- 作者本轮问题：维系的是持续生成的结构，自维系不是终点；暂不预设终极目的，尝试生成/粗粒化解释；请求完整实验设计。
- Draft PR #1136：2026-10-28 探索性来源备忘，**不是已合并 main 或 canonical owner**。
- 已合并 main 的 STATUS / neutral cognition CN-2 A owner 为唯一当前执行来源。
- Montévil & Mossio (2015), https://doi.org/10.1016/j.jtbi.2015.02.029；Keramati & Gutkin (2014), https://doi.org/10.7554/eLife.04811：成熟机制优先，对比不宣称新颖性。
