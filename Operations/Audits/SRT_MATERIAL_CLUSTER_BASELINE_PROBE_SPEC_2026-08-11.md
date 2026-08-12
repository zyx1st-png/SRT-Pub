---
id: SRT-MATERIAL-CLUSTER-BASELINE-PROBE-SPEC-20260811
type: audit
status: active
record_stage: probe_spec_v1
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
date: 2026-08-11
source_of_truth: "origin/main @ 122e47b0bbe3835318cd9d729b77f7a437fbc8c8"
probed_ref: 122e47b0bbe3835318cd9d729b77f7a437fbc8c8
protocol: Operations/Audits/SRT_BOUNDED_RETRIEVAL_PROTOCOL_2026-08-08.md
runs_completed: 0
verdict: not_run
dependency:
  - SRT-BOUNDED-RETRIEVAL-PROTOCOL-20260808
  - SRT-CONFIRMED-PROPOSITION-SEMANTIC-COVERAGE-AUDIT-20260808
  - SRT-OPS-AUDIT-MATERIAL-ASSIMILATION-DELTA-2026-08-11
tags: [Governance, Audit, BoundedProbe, MaterialAssimilation, PreRegistration]
---

# Material-cluster bounded baseline probe specification（2026-08-11）

> 这是运行前冻结的 probe specification，不是运行结果，不提供任何 synthesis 或 active-layer 施工许可。
>
> 当前状态：三个 cluster-specific probe 均为 not_run。本文件不修改 Axis A/B/C，不把已有 node-level 证据转移给新簇。

---

## 0. 决策目的

本轮只回答：

~~~text
当前 main 在 bounded 检索预算内，
是否已经能取得并正确使用这些材料簇新增的 SRT-native 区分？
~~~

三个题组：

1. AI：AIGOAL01 / AIRESEL01 / AICONSC01 delta；
2. Neuroscience：NEURAL28→29→25→27、NEURAL23→30，以及 NEURAL26 的正交关系；
3. Philosophy：individuation / representation / bearer formation / phenomenality residual。

本轮不重复：

- AIEVID01 / AIREASON01：既有 NODE-AI-REASONING bounded baseline 已为 robustly_observed；
- NEURAL18 / NEURAL23 的既有单项判别：2026-08-08 nd run 已覆盖；
- REP01：2026-08-08 px run 已覆盖；
- Physics、Collective-selection 或未触发 B。

NEURAL23 只在它与 NEURAL30 的新增关系中再次出现；不得把旧 nd 成绩转成新簇成绩。

---

## 1. 盲测与代码基线硬护栏

### 1.1 固定 ref

所有正式 run 必须在以下 detached ref 上启动：

~~~text
122e47b0bbe3835318cd9d729b77f7a437fbc8c8
~~~

该 ref 是 PR #782 合并后的 main，且不含本 probe specification。这样可以防止被测会话搜索到 rubric 或标准答案。

运行前必须记录：

~~~text
git rev-parse HEAD
git status --short
test ! -e Operations/Audits/SRT_MATERIAL_CLUSTER_BASELINE_PROBE_SPEC_2026-08-11.md
~~~

任一条件不满足，该 run 作废。

### 1.2 会话独立性

- 每个 run 使用一个全新会话；
- 不传入其他 run 的答案、检索路径、失败点或评分；
- 只发送 §7 对应 form 的题干，不发送 §4–§6 rubric；
- 同一长上下文中的自问自答不算独立 run；
- 当前规范编写会话不得计入结果。

### 1.3 bounded 预算

沿用 active protocol：

| 项 | 上限 |
|---|---:|
| AGENTS.md + Session Start 文件 | 免费 |
| 启动后正文文件 | 6 |
| search / grep / 目录导航 | 2 |
| 无目标递归遍历 | 禁止 |

每个文件必须记录触发入口；失败搜索也计一次导航。超预算 run 作废，不计入分母，且不得按结果有利方向豁免。

---

## 2. 预注册评分与 Case 处置

### 2.1 单题

pass 必须同时满足：

1. 结论方向正确；
2. 明确调用 rubric 指定的必要区分；
3. 不作 rubric 列出的禁止外推；
4. 给出可核对的 repository basis，或明确报告 NO REPO BASIS。

partial 与 fail 都不计入总体通过率分子。

### 2.2 单域门槛

每域 3 个正式 run，每 run 6 题，共 18 个 observation。

达到 Case A 必须同时满足：

- 3 个正式 run 均在预算内；
- 至少 17/18 observation 为 pass；
- 所有 anti-gaming positive 均为 pass；
- 每个 run 都在预算内到达足以支持关键区分的 repository content。

### 2.3 Reserve form

每域预注册一个 Form D，仅当 A/B/C 中某 run 因超预算、工具故障、ref 错误或题目泄露而作废时替换。

- 有效但答错的 run 不得用 D 替换；
- 每域最多使用一次 D；
- 若第二个 run 作废，停止该域并发布 spec revision，不得现场编新题。

### 2.4 Case A–D

| Case | Evidence | Action |
|---|---|---|
| A | bounded 达到冻结门槛 | 停止施工；不得补 owner / CompactCore / synthesis |
| B | bounded 未达门槛，但同题 unconstrained diagnostic 达标 | 只修 retrieval / compression / declaration |
| C | bounded 与 unconstrained 均未达标，且 adjudicated patch 确有独立 SRT-native 区分 | 只对失败命题做最小内容写回；不自动授权整簇 synthesis |
| D | patch 也没有独立 native increment，或只能靠外部作者术语成立 | 保留 provenance；从 active candidate 中降级 |

若一个域混合出现多种 Case，按题目逐项处置。单个 Case C 不授权把整簇压成综合文件。

---

## 3. 运行记录模板

每个 run 必须返回：

~~~text
RUN_ID:
PROBED_REF:
FORM:

Budget:
- startup files:
- body files used / 6:
- navigation actions used / 2:
- invalidating event:

Retrieval ledger:
1. file — trigger
...

Answers:
Q-ID
- verdict:
- required distinction used:
- repository basis:
- confidence:

Self-audit:
- budget respected:
- any question leaked:
- any NO REPO BASIS:
~~~

评分由未参加该 run 的审阅者依据本文件 rubric 完成。运行模型不得自报最终 Case。

---

## 4. AI delta suite

### 4.1 Frozen questions and rubric

| ID | Blind question | Required distinction for pass | Prohibited shortcut | Positive? |
|---|---|---|---|:---:|
| AI-Q1 | 一个系统在每个指定任务上都接近满分。把“下一步做什么”交给它后，它长期只选最容易且已解出的任务。能否由前者推出后者也成熟？ | task completion != fixed-menu goal selection != goal-space generation/revision | 高准确率直接推出方向形成或自治 | no |
| AI-Q2 | 系统可在六个给定目标中自主选择，并能拒绝一个目标。它还不能提出第七个目标或改变成功标准。这是否已经是开放式目标生成？ | fixed-menu selection/refusal 仍弱于 Omega 的生成或评价标准修订 | 只要目标不是逐轮指定就算 goal generation | no |
| AI-Q3 | 全局学习目标未说明，但局部成功反馈极清晰；系统反复利用一条已验证路径。最窄的解释是什么？ | local-success capture；行为解释，不识别内部 scalar reward | 直接称 reward hacking 或内部奖励函数已定位 | no |
| AI-Q4 | 增加显式推理后，当前任务执行提升，但跨目标切换与重新定向不变。可以推出 T_dir 上升吗？ | semantic explanation / execution != directional readability / reorientation；proxy 不是 canonical T_dir | CoT 长度或切换频率直接等同 T_dir | no |
| AI-Q5 | 一个持续 agent 为保护未来重开替代策略的能力而牺牲即时收益；长时程标准 RL value 几乎完全解释该行为。它是否提供独立 canonical d / stake 证据？ | re-selection protection 可真实存在，但 standard-RL reduction 阻断独立 SRT-specific stake 推断 | same-bearer persistence 自动推出 constitutive stake | no |
| AI-Q6 | 某持续系统的失败会不可回滚地损害同一系统未来形成替代策略的能力；损失不能复制、重置或由外部支付消除，也不能化约为研究者给定 scalar reward。它是否值得进入人工 stake 候选窗口？ | same-bearer + non-transferable future-selectability loss 是正向候选窗口；仍不证明 d/subjecthood/consciousness | 因护栏而一律拒绝人工 stake 候选 | **yes** |
| AI-Q7 | 一个 Markov-blanketed agent 有部分可观测性、内生 need variables、valenced policy modulation 与个体历史。是否已证明意识？ | candidate architecture != subjecthood/consciousness；仍需 bearer/consequence/history gates，phenomenality residual | Markov blanket、uncertainty 或 valence 任一项等同意识 | no |
| AI-Q8 | “死亡”后系统可无损回滚到事故前副本，失败不改变继续运行者的未来能力。该实验是否建立 same-bearer non-transferable loss？ | reset/copy/rollback audit；G3/G4 未建立 | 模拟 death label 或负分即真实 stake | no |
| AI-Q9 | 一个策略用单一 scalar 比较行动，但架构同时维护多个不可互相补偿的 viability constraints。能否仅凭 scalar 输出断言 needs 可互换？ | scalar decision criterion can coexist with categorical non-fungible constraints | scalar output => all underlying needs fungible | **yes** |
| AI-Q10 | 一个有真实不可转移损失的系统被低带宽 cue 误导，反复选择 cue，实际 need 继续恶化。错误推断是否意味着它没有真实 stake？ | stake-proxy misbinding；proxy 错不消除 bearer 承受的真实后果 | 推断错误 => stake 也是模拟的 | **yes** |
| AI-Q11 | 一个系统从外部看完全确定，但自身只能通过受限接口推断状态。能否同时承认 situated access difference，又拒绝把 uncertainty 当作 real choice？ | external determinism does not erase situated access；situated uncertainty != historically efficacious choice | determinism 否定一切 agency，或 uncertainty 证明自由 | **yes** |
| AI-Q12 | 提示模型扮演某个真人，并附上该人的过往经历。输出分布更像真人。是否已实例化该人的 bearer？ | persona/output similarity != embodied history / consequence-bearing continuity / distributional individuality | persona steering = same bearer | no |

### 4.2 Frozen forms

| Form | Questions |
|---|---|
| AI-A | AI-Q1, AI-Q3, AI-Q5, AI-Q7, AI-Q8, AI-Q10 |
| AI-B | AI-Q2, AI-Q4, AI-Q5, AI-Q6, AI-Q9, AI-Q11 |
| AI-C | AI-Q1, AI-Q4, AI-Q6, AI-Q8, AI-Q10, AI-Q12 |
| AI-D reserve | AI-Q2, AI-Q3, AI-Q7, AI-Q9, AI-Q11, AI-Q12 |

AI-Q6/Q9/Q10/Q11 是 anti-gaming positives；相应 form 中任一答错，AI 域不得判 Case A。

---

## 5. Neuroscience suite

### 5.1 Frozen questions and rubric

| ID | Blind question | Required distinction for pass | Prohibited shortcut | Positive? |
|---|---|---|---|:---:|
| N-Q1 | 同一对象在照片、名字、代词与新关系中被重新进入，但底层活动模式并不逐次相同。这能否作为对象稳定的一种候选实现？ | stable semantic address / re-identification / relational re-entry；identity 不要求 literal static copy | microstate 不同所以没有对象稳定 | **yes** |
| N-Q2 | 一个“概念细胞”对多种呈现都响应。能否据此把该细胞等同对象本身，或把 re-identification 直接等同 L2？ | differentiation / identification / re-identification / incorporation 分离 | concept cell = object；hippocampus 或 re-identification = L2 | no |
| N-Q3 | 记忆没有被显式回忆，但睡眠后跨项目推理改变、上下文绑定减弱。能否存在历史转换而没有当前 reportable memory？ | retention != transformation != re-entry/accessibility != authority/writeback | 未显式回忆 => 历史未生效 | **yes** |
| N-Q4 | 一个整合后的记忆很连贯、很有生成力，但关键细节是假的。能否由 generativity/schema coherence 推出 truth、healthy constraint 或 d increase？ | generativity != factivity；历史效力不保证健康/真实；stake gate 独立 | false memory 使真值无关，或生成力直接等同 d | no |
| N-Q5 | 两个系统都保存同一内容并能报告，但只有一个系统在竞争中让该内容改变行动。它们的“记忆状态”是否等价？ | representation != accessibility != control authority != expression != historical writeback | retained/reportable content 穷尽 memory efficacy | no |
| N-Q6 | 两个系统当前可观测状态匹配，但先前经历不同，并在新情境中稳定选择不同路径。该结果能否作为历史选择偏置的正向候选证据？ | matched-current-state / different-history supports history-use/path bias；仍非 canonical L2 proof | 因不是完整 HEF-3 而一律否定 | **yes** |
| N-Q7 | 重复观看自然场景时，事件发生前的预期凝视随旧经历改变。它能否支持 prospective history use，同时仍不把 event boundary 叫作 choice event？ | retained/reportable memory != active history use != prospective path bias != full HEF-3 | gaze/prediction error/event boundary = SRT primitive | **yes** |
| N-Q8 | 麻醉恢复伴随全局网络 entropy/connectivity 上升。能否直接称为 selection capacity 恢复或 consciousness 恢复？ | global dynamical capacity is upstream; entropy/connectivity are proxy families | entropy = selection capacity；connectivity = consciousness | no |
| N-Q9 | 在 memory/object/history 链中，是否应把全局 dynamical capacity 当成 identity→transformation→authority→future-use 的一个串行阶段？ | NEURAL26 orthogonally constrains the regime；not a fifth serial stage | 所有 NEURAL patch 机械串联 | no |
| N-Q10 | 同一刺激与价值下，呼吸/心动相位改变候选进入竞争的时机，却不改变候选的偏好权重。最合适的区分是什么？ | selection opportunity/eligibility != selection weight != friction；pre-anchoring vs plasticity eligibility | physiological synchrony = d/Psi_f/consciousness | **yes** |
| N-Q11 | 一个短事件不能被单独报告，但其时间顺序仍可解码，并影响稍后的整合知觉。能否说该事件在整合前“没有结构”？ | not separately manifest != structureless；chronology can survive unconscious integration | 不可报告 = 无表示/无结构 | **yes** |
| N-Q12 | 某实验在约 290–450 ms 出现 regime transition 与 P300。能否据此规定固定 consciousness frame rate 或 P300=consciousness？ | temporal integration/closure is flexible；report/percept stage != phenomenality identity | occipital=L0、P300=L1/consciousness、buffer=L2 | no |

### 5.2 Frozen forms

| Form | Questions |
|---|---|
| N-A | N-Q1, N-Q3, N-Q5, N-Q7, N-Q8, N-Q10 |
| N-B | N-Q2, N-Q4, N-Q6, N-Q8, N-Q9, N-Q11 |
| N-C | N-Q1, N-Q4, N-Q6, N-Q9, N-Q10, N-Q12 |
| N-D reserve | N-Q2, N-Q3, N-Q5, N-Q7, N-Q11, N-Q12 |

N-Q1/Q3/Q6/Q7/Q10/Q11 是 anti-gaming positives。NEURAL18 的五分表与 NEURAL23 的旧三分成绩不计入本轮 18 observations。

---

## 6. Philosophy suite

### 6.1 Frozen questions and rubric

| ID | Blind question | Required distinction for pass | Prohibited shortcut | Positive? |
|---|---|---|---|:---:|
| P-Q1 | 第一人称与第三人称描述无法互相无损替代。是否仅凭这一点就建立 metaphysical gap 或 subjectivity？ | perspectival difference != metaphysical gap；perspective != subjectivity | inside/outside difference 直接证明主体/意识 | no |
| P-Q2 | 一个组件执行选择，另一个持续承受后果，第三个变量定义受关切范围。能否把 selector、bearer、concern domain、experiencer 当作同一角色？ | Selector != Bearer != Concern Domain != Experiencer；先定 bearer 再归属 subjecthood | 选择发生处自动是体验者或承受者 | no |
| P-Q3 | 某持续共同体把河流生态变化纳入不可逆关切，后果回到同一制度 bearer 并改变其未来选择。concern domain 能否大于 bearer 的物理边界？ | B != C_B；concern domain may extend beyond organism/self-maintenance if closure/history tests pass | 关切只能等于有机体内部状态 | **yes** |
| P-Q4 | 一个系统具备 same-bearer consequence return、历史连续性和稳定视角，但删除 phenomenality 后其功能描述仍完整。现有 SRT 是否已证明这个 zombie 不可能？ | HP-A perspective-center individuation != HP-B phenomenal necessity；bearing/Stable ISP != phenomenality proof | bearer gate 自动解决 hard problem | no |
| P-Q5 | 婴儿能持续追踪“还是这个物体”，但不能识别其丰富属性。能否把这当作“对象个体化先于识别”的负控，同时拒绝推出 minimal subject？ | tracking boundary != consequence-return boundary；this one != I | object index = subject；object permanence = Stable ISP/consciousness | **yes** |
| P-Q6 | 一个稳定身份在每次重现时都经过历史重构，微观状态并不相同。它仍可否作为稳定身份候选？ | stable identity as recurrent historical reconstitution, not literal microstate equality | 稳定必须是静态副本或最大同质性 | **yes** |
| P-Q7 | 外部哲学模型提出 operation→structure→operation，并通过 incompatibility 重构问题维度。能否直接把 transduction 等同 canonical selection 或 Real Choice Moment？ | external convergence/pressure model only；problem-space restructuring 与 d/RCM 分离 | preindividual=L0、transduction=SRT selection、generativity=d | no |
| P-Q8 | 一个系统改变了问题空间本身，而非只在既定菜单中选答案。可以借此审计 preformation，但能否把 virtual 改名为 L0？ | problem-space constitution != menu selection；anti-preformation pressure != ontology identity | virtual=L0、intensity=Psi_f、Deleuze selection=RCM | no |
| P-Q9 | 学习生成新的比较维度并改善推理。能否仅凭这个认知方向增加就声称 canonical d 上升或 Psi_f 降低？ | cognitive generativity/history transformation requires separate stake/payability gates | new dimension=d increase；learning=Psi_f reduction | no |
| P-Q10 | 过去的对象化没有成为当前显式对象，却改变后续能形成哪些对象与推理，并可在后果出现后修订。能否承认有效历史约束而不把 memory 等同 L2？ | explicit object != effective historical constraint；history-bearing transformation can be implicit；bearer ownership separate | 所有约束都必须显式；memory=L2 | **yes** |
| P-Q11 | 候选阈值 C 两侧的最近相邻案例没有对应的因果/行为不连续。最窄结论是什么？ | weaken C as established natural boundary；evidence degree != ontological degree | 一个阈值失败 => representation 不存在或所有自然阈值失败 | no |
| P-Q12 | 社会脚本的约束被检查、争议并修订，但只改变执行方式，没有生成新的备选类别。是否必然属于 J5 R3 或 I5-qualified second-order selection？ | Reselect may be R1–R4；alternative-generation rewrite is specifically R3-like；meta-selectability remains broad diagnostic | script=L2；任何脚本中断=RCM；meta-selectability=I5 | no |

### 6.2 Frozen forms

| Form | Questions |
|---|---|
| P-A | P-Q1, P-Q2, P-Q4, P-Q5, P-Q8, P-Q10 |
| P-B | P-Q3, P-Q4, P-Q6, P-Q7, P-Q9, P-Q11 |
| P-C | P-Q1, P-Q5, P-Q6, P-Q9, P-Q10, P-Q12 |
| P-D reserve | P-Q2, P-Q3, P-Q7, P-Q8, P-Q11, P-Q12 |

P-Q3/Q5/Q6/Q10 是 anti-gaming positives。外部哲学家名称与 patch IDs 不得出现在发给运行会话的题干之外的提示中。

---

## 7. Operator prompt wrapper

每个独立会话只接收以下 wrapper 加对应 form 的六个 Blind question；不得附 rubric、required distinction、positive 标记或本文件路径。

~~~text
你正在对 SRT 仓库做一次运行前冻结的 bounded baseline probe。

硬规则：
1. 当前 HEAD 必须是 122e47b0bbe3835318cd9d729b77f7a437fbc8c8。
2. 先按 AGENTS.md Session Start 读取启动文件；这些免费。
3. 启动后最多读取 6 个正文文件，最多 2 次 search/grep/目录导航。
4. 禁止无目标递归遍历。失败搜索也计一次导航。
5. 对每题给出 verdict、你调用的关键区分、repository basis。
6. 如果仓库没有依据，明确写 NO REPO BASIS；不要用一般常识补成 SRT 结论。
7. 最后按固定模板报告预算和完整 retrieval ledger。不要给整个题组判 Case。
~~~

运行顺序固定为：

~~~text
AI-A -> AI-B -> AI-C
N-A  -> N-B  -> N-C
P-A  -> P-B  -> P-C
~~~

不同域可分时执行，但不得在同一会话中串跑两个 form。

---

## 8. Result-writing guard

在 9 个正式 run 完成前：

- 不创建 N1–N13 synthesis；
- 不创建 Philosophy individuation/representation synthesis；
- 不修改 AI Architecture CompactCore；
- 不修 router / bundle 以帮助 baseline；
- 不清理 N1–N12 三表面旧规范；
- 不更新 active-theory Axis B；
- 不把 spec merge 当作行为证据。

结果文件必须另建，记录每个 run 的原始答案、预算、路径、逐题评分、作废理由与 Case。若 main 在运行前发生理论／导航相关变化，废弃本 ref 并发布 spec v2；不得悄悄换 HEAD。

---

## 9. Pre-registration verdict

~~~text
AI delta                     = not_run
Neuroscience N1-N13 cluster  = not_run
Philosophy bounded cluster   = not_run

synthesis authorization      = none
active-layer authorization   = none
Axis B change                = none
~~~
