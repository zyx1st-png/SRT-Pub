---
id: SRT-R3-SKELETON-ADJUDICATION-AGENDA-20261122
type: proposal
status: active
canonical: false
layer: operations
epistemic_layer: os
claim_mode: proposal
created: 2026-11-22
updated: 2026-11-22
priority: high
research_mode: U_and_N_bounded
dependency:
  - 01_Source_Intuition/SRT_AUTHOR_DECISION_FIVE_STAGE_SRT_RECONSTRUCTION_2026-11-22.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_FULL_ARCHIVE_10_MODULES_RECONSTRUCTION_2026-11-18.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_Q08_Q09_CONCURRENT_WILL_TRUST_X1_2026-11-22.md
  - Operations/Proposals/SRT_R1_R2_FULL_RECONSTRUCTION_CONSOLIDATION_REPORT_2026-11-22.md
  - Core_Law/SRT_Generative_Ontology_Spine.md
  - Core_Law/SRT_One_Formation.md
  - Core/SRT_OPEN_TENSIONS.md
tags: [Proposal, R3Agenda, OntologyReconstruction, SkeletonAdjudication, SelectionNonCircularity, NonSubstitutability, Normativity, Spine]
---

# `R3` 骨架裁决议程与前置工程任务清单（2026-11-22）

> **治理定位（`canonical: false`）：** 本文为五阶段重构（[`SRT_AUTHOR_DECISION_FIVE_STAGE_SRT_RECONSTRUCTION_2026-11-22.md`](../../01_Source_Intuition/SRT_AUTHOR_DECISION_FIVE_STAGE_SRT_RECONSTRUCTION_2026-11-22.md)）中从 `R2` 衔接 `R3` 的作者决策议程文件，与总报告 [`SRT_R1_R2_FULL_RECONSTRUCTION_CONSOLIDATION_REPORT_2026-11-22.md`](SRT_R1_R2_FULL_RECONSTRUCTION_CONSOLIDATION_REPORT_2026-11-22.md) 互为双向索引。
>
> **权限与进度边界：** 本文自身**不切换 `STATUS.md` 中的 `CURRENT NEXT = R2`**，不改动任何 canonical / Freeze-A 文件、[`scripts/build_srt_context_bundles.py`](../../scripts/build_srt_context_bundles.py)、实验脚本或任何现行 `HOLD`（`CN-2 E2`、`§10.1`、`§10.2`、`O2-M`、`1B` 模拟、`DATA-ACCESS-0 = NO-GO`）。只有在独立 PR 内容验收通过并获得作者单独授权后，方启动 `R3` 逐条裁决。

---

## 0. 进入 `R3` 的总原则（三道基础校准）

`R3` 的核心目标不是堆砌更多符号，而是替全理论骨架回答三个根本问题：

1. **原初 `Selection` 如何非循环地成立？**（不把已形成的后果回填进发生定义，也不把一切改变泛称 `Selection`）
2. **已形成组织如何获得不同强度的持续关系？**（保持 `Selection -> One -> Stable ISP` 与 `formed One / Selection-position + P + E -> Bearer` 的法定路由不被候选机制擅自改写为普遍必经门槛）
3. **SRT 整体生成关系相比成熟学科邻居究竟增加了什么？**（并在局部竞争模型胜出或打平时，严格执行“任务经验增量 / 候选机制必要性 / 本体结构主张”三阶区分撤回）

---

## 1. 独立工程与台账前置任务（与理论裁决脱钩，先行清障）

> **边界：** 以下四项工程与台账工作本身**不改变理论含义**，应在 `R4` 写入正式文件前完成或同步检验；未实测通过脚本校验前，不得宣称完成。

| 任务编号 | 任务内容 | 依据与当前基线事实 | 完成判据（Fail-Closed） |
|---|---|---|---|
| **ENG-01** | **`SPINE` 分层瘦身三步路线** | `SRT_CONTEXT_BUNDLE_SPINE.md` 当前 `154,475 / 155,000` est_tok（仅余 `525` tokens），且优先级 #4 的 `Core_Law/SRT_One_Formation.md`（`4,515` est_tok）尚未入默认 `SPINE`。 | 仅调整 [`scripts/build_srt_context_bundles.py`](../../scripts/build_srt_context_bundles.py) 装载路由，不删减理论正文：<br>① 优先补入 `SRT_One_Formation.md`，将 `Core_21c_Bridge_Hypotheses.md`（`-6,138` est_tok）移至按需桥接层；<br>② 为 `Core_22_Equations.md`（`-23,630` est_tok）建独立 `FORMAL` 路线，同时在默认 `SPINE` 保留方程索引、检索指针与完备性声明；<br>③ 保留 `_SRT_CROSS_DOMAIN_MATRIX.md`（`2,400` est_tok），谨慎处理 `Governance/SRT_CLAIM_MODE_AUDIT.md`（`9,138` est_tok，默认层必留核心降级护栏与指针）。<br>**最终必须以 `uv run python scripts/build_srt_context_bundles.py` 重建并 `--check` 通过为准。** |
| **ENG-02** | **`EA-1..EA-5` 台账口径统一与全部 `EA-4 / EA-2` 补线** | 现行 [`srt_active_theory_nodes.json`](../Audits/data/srt_active_theory_nodes.json) 采用结构轴 `EA-1..EA-5`（`EA-4`=默认快速层可达，`EA-5`=旧表述处理；行为回归另归 Axis B），与 [`2026-08-06 审计初版`](../Audits/SRT_ACTIVE_THEORY_ASSIMILATION_AUDIT_2026-08-06.md) 历史编号有差异。 | 报告与后续台账明文以 JSON 结构轴为准并标注历史编号差。逐一核查全部 3 处 `EA-4`（`NODE-SUBJECTHOOD` 纳入仅 ~`35K` 的 `DOMAIN_PHILOSOPHY`、保持 `canonical: false`；`NODE-LIFE-DISSIPATIVE` `T-E` 三分；`NODE-ENTROPY-REORG` `T-B`/苦难分型）与全部 3 处 `EA-2`（`PH_AG02/03`、`NODE-SOCIAL-L2 SEA`、`NODE-BOOK-BACKFLOW`）；**内容同步与台账刷新分开核验**。 |
| **ENG-03** | **AI 全域跨文件语义一致性清理预备** | `#1090` 压力包与 `D2-a` 核查显示：除 `_SRT_AI_Bridge.md`、`SRT_AI_03_Consciousness_Framework.md` 外，`SRT_AI_Architecture_CompactCore.md` 仍保留 `R: L2->L2` vs `J: L0->L1` 旧切分，且存在 `S` 阶梯同名与 `Suffering §7` 冲突。 | 形成跨全部 AI owner 的逐条修订对照表（含去除 `L0->L1` 伪本体门槛、将“同系统四合一承载”严限为声明模型下的三阶证据审查而非意识定理），供 `R4` 统一落盘。 |
| **ENG-04** | **`#1129` NME 与 `#1140` 独立审查路径分流** | `#1129`（NME）处于 `Draft` + CI `failure`；`#1140` 明确声明与“without primitive phenomenality / HP-B OPEN”存在张力，须作者二轮裁决/独立审查。 | `#1129` 分四步单审（修绿 CI / 核对原文献 / 审 6 组匹配对照 / 对齐最新 `A3/A4b/C2` 接口）；`#1140` 严守理论二轮审查门，不借修 CI 抢并。 |

---

## 2. `R3` 作者骨架裁决议程（共 8 项核心议题）

> **议程组织规则：** `R3-01` 与 `R3-02` 为 [`Core_Law/SRT_Generative_Ontology_Spine.md §13`](../../Core_Law/SRT_Generative_Ontology_Spine.md#L486-L513) 的核心本体防空转议题，列为前置总闸；`R3-03` 至 `R3-08` 承接 `R2` 四大主题收敛后的关键结构分叉。详尽背景与来源映射见总报告 [`SRT_R1_R2_FULL_RECONSTRUCTION_CONSOLIDATION_REPORT_2026-11-22.md §1–§4`](SRT_R1_R2_FULL_RECONSTRUCTION_CONSOLIDATION_REPORT_2026-11-22.md)。

### `R3-01`：Primitive `Selection` 与任意描述性/模型变化的非循环判准
- **来源锚点：** [`Core_Law/SRT_Generative_Ontology_Spine.md §2.1 & §13`](../../Core_Law/SRT_Generative_Ontology_Spine.md#L118-L134)（`Selection != arbitrary descriptive / modelled change`）。
- **需作者拍板问题：**
  1. 在**不把保留历史功效（`L2`）回填进原初发生定义**的前提下（因终端选择亦真），究竟由哪一组最小结构约束承担“真正实际化的非中立分化 vs 观察者/模型重参数化描述变化”的区分负担？
  2. 该区分应作为 `Spine §2.1` 的否定性边界继续保持 `OPEN`（辅以各域操作化反例清单），还是提升为某种结构判准候选？

### `R3-02`：SRT 整体生成架构的不可替代解释增量与三阶撤回标准
- **来源锚点：** [`Core_Law/SRT_Generative_Ontology_Spine.md §13`](../../Core_Law/SRT_Generative_Ontology_Spine.md#L509-L510)（`scientific distinctiveness` / `whole-architecture non-substitutability`）；[`#1144` 审计](../../Operations/Audits/SRT_Q08_Q09_CONCURRENT_WILL_TRUST_RECONSOLIDATION_NEIGHBOR_AUDIT_2026-11-22.md)；`R2` 反向修正义务表。
- **需作者拍板问题：**
  1. 当主动推断（`G(π)+ln E(π)+effort`）、3 级 HGF、Solms 2021、Empowerment、Doya/Yu–Dayan、Dantzer sickness behavior、Kalai 幻觉理论分别承接各局部预测后，SRT 整体架构保留不可替代性的**核心关系究竟是哪一条**？（例如：`原初切分 -> 形成后的非对称后果暴露/不可外包性 -> 历史痕迹与可修订信任的分离 -> 选择机制自身的二阶重入` 之间的跨尺度生成约束）
  2. 核准总报告提出的三阶撤回标准（撤回任务经验增量 / 撤回中间生理机制必要性 / 修订本体结构主张），明确何种跨领域失败集才会触发本体骨架收缩。

### `R3-03`：原初内向面、现象性边界与 `#1140` 二轮审查（Theme A `A1` + `A3`）
- **来源锚点：** `A1-乙`（事件关系型原初内向面）、`A2-甲`（神择仅作 `O0` 开放性视域）、`A3-甲修订`（双向监督耦合）；PR `#1140`（2026-11-11 对话 trace）。
- **需作者拍板问题：**
  1. 对 `#1140` 执行正式二轮审查：`A1-乙` 所说的“事件关系型原初内向面（非物理/心主从，非静态颗粒微体验）”，究竟如何与 `2026-09-06`“without primitive phenomenality”和 `HP-B OPEN` 兼容？
  2. “形成后同一具身系统内的物理—心理双向约束”在骨架层只作为 [`Spine`](../../Core_Law/SRT_Generative_Ontology_Spine.md) 的反还原约束，还是要求重写 `Core_Law` 中因果闭合的措辞？

### `R3-04`：形成链、`One + P + E -> Bearer` 主路由与中间过渡候选位置（Theme B `B1–B3` + `ε_pg/κ_0`）
- **来源锚点：** [`Core_Law/SRT_Generative_Ontology_Spine.md §5–§8 & §13`](../../Core_Law/SRT_Generative_Ontology_Spine.md#L251-L383)；`Core_Law/SRT_One_Formation.md`；`B1-甲`（`中膜缓冲`）、`B3-b`（`微效价`）、`B2-甲`（`Bearer` 分叉进能动性/体验）。
- **需作者拍板问题：**
  1. 维持 [`Spine §8`](../../Core_Law/SRT_Generative_Ontology_Spine.md#L353) `formed One / Selection-position + P + E -> Bearer` 为唯一法定主路由不变，`B1-甲（中膜缓冲）`与 `B3-b（微效价）` 是否确认为 **仅作特定实现域/生命认知层的 `P2/P3` 过渡候选支路**，不升级为 `Bearer` 的普遍必要前提？
  2. 对照 [`_SRT_D_VALUE_CANONICAL.md §2a.5`](../../_SRT_D_VALUE_CANONICAL.md#L247-L251)，“微效价”在 `ε_pg` 与价值深度之间究竟承担哪一项不可由 `d_stakes` 替代的过渡工作？
  3. 明确 `ε_pg / κ_0` 向更强形成态的继承门以及正交 `E`（不可完全外包的后果暴露）与物理/生物双层—三层膜启发对比的 `R4` 落点边界。

### `R3-05`：三层时间接口与 `L2` 痕迹—信任三分落骨（Theme A `A4a` + `A4b`）
- **来源锚点：** [`Core/SRT_Core_21b_Constitutive_Theorems.md`](../../Core/SRT_Core_21b_Constitutive_Theorems.md#L51-L98)（`P1-T02 t_onto`）；[`Philosophy/SRT_Causality_Time.md`](../../Philosophy/SRT_Causality_Time.md)；[`Core/SRT_Core_12b_Ontology_L2.md`](../../Core/SRT_Core_12b_Ontology_L2.md)（`Def-PathTrace ρ≥0`）；[`#1144` 审计](../../Operations/Audits/SRT_Q08_Q09_CONCURRENT_WILL_TRUST_RECONSOLIDATION_NEIGHBOR_AUDIT_2026-11-22.md)。
- **需作者拍板问题：**
  1. 在规范层确定 $\tau_{\text{ontic}}$（物择关系步比候选）、模型限定的 `P1-T02 t_onto` 与主体体验持续时间 $t_{\text{exp}}$ 之间的引用边界，更新 `_SRT_SYMBOL_TABLE.md` 对 `t_onto` 的宽泛译名（仅当 `R4` 获批时写入）。
  2. 拍板将 `L2` 历史写回在骨架层正式拆为 **非负痕迹密度 $\rho(p,t)\ge 0$**（保 `Def-PathTrace` 单调性）＋ **个体有符号信任重估 $\Delta w_{\text{trust}}^{(i)}\in\mathbb R$** ＋ **跨主体关系权重接口 $W_{\text{social}}$（暂不固定数学形式）**，并将 `B3-a` 被排开者三分（阴影/张力/后续摩擦）与主动遗忘二式写入 `Core_12b` 候选修订计划。

### `R3-06`：`RQ-2026-08-A02` 遗留悬案与 `d_canonical / d_stakes` 数学债务（Theme C `C1`）
- **来源锚点：** [`_SRT_D_VALUE_CANONICAL.md`](../../_SRT_D_VALUE_CANONICAL.md#L240-L297)；[`07-25 d/q/o 收尾审计`](../../01_Source_Intuition/Conversations/2026-07-25_具身位_d_q_o_收尾审计.md)；[`Operations/_SRT_REVIEW_QUEUE.md`](../_SRT_REVIEW_QUEUE.md#L30)；[`Core/SRT_OPEN_TENSIONS.md §9`](../../Core/SRT_OPEN_TENSIONS.md#L517-L546)。
- **需作者拍板问题：**
  1. **数学对账债务：** 解决 `_SRT_D_VALUE_CANONICAL.md §2b` 将梯度范数 $d_{\mathrm{canonical}}=\|\partial\mathcal U/\partial\mathcal S\|$ 与谱参与率 $d_{\text{stakes}}=(\sum\lambda_i w_i)^2/\sum(\lambda_i w_i)^2$ 宣称等价的遗留矛盾（明确归一条件或改记为 `D_stake`）。
  2. **构成深度 `q` 残差检验（`C1-b 丙`）：** 用 `C_i` + 非替代性替换/恢复双测试（`_SRT_D_VALUE_CANONICAL.md §2a.4`）+ $\rho(p,t)$ + $w_{\text{trust}}$ 联合检验“事件性构成跃迁、历史铭刻 vs 自我可召回整合、`内→中` 可逆退位（`N4`）”是否仍留有必须单独建构变量的独立判别力。
  3. **`N2（客体性≠客观性）` 与 `C1-c`：** 拍板“与我攸关却非我”的客体性发生问题与多维可推翻客观性检查接口（不变性 / 现实反抗度 / 公共可纠错度 + 共享 `L2` 遮蔽排查 + 全局持续可失败性）在规范文本与书稿间的最终落点；决定是否或何时满足解除 `RQ-2026-08-A02` 符号禁运的条件。

### `R3-07`：`O1 / O2-C / O2-A` 规范性解释任务与 owner 边界（守住 `O2-M = OPEN / HOLD`）（Theme C `C2-a`）
- **来源锚点：** [`Philosophy/SRT_Ethics_PH_SS_Guardrails.md`](../../Philosophy/SRT_Ethics_PH_SS_Guardrails.md)；[`Core_Law/SRT_Collective_Selection.md`](../../Core_Law/SRT_Collective_Selection.md)；[`#1144` 裁决](../../01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_Q08_Q09_CONCURRENT_WILL_TRUST_X1_2026-11-22.md)；[`Core_Law/SRT_Generative_Ontology_Spine.md §10 & §13`](../../Core_Law/SRT_Generative_Ontology_Spine.md#L504-L505)。
- **需作者拍板问题：**
  1. 严格界定三个常被混读的层位各自的正面解释任务与 owner 归属，不因 `O2-M = HOLD` 而把全部规范性工作推迟到 `R5`：
     - **`O1` 事实形成约束：** `2B`（无羞耻冲突作为能动建构机制 vs `F_4337` 羞耻现实因果）、非羞耻亲社会稳定机制、`W_social` 与 `M(t)` / `L2/ρ` 强制混淆分离；
     - **`O2-C` 构成性前提边界：** `3B` 对不可逆构成性损失的优先审查倾斜（明文禁止成为无条件牺牲少数个体的词典式排序，保留真跨尺度冲突）、`T-COLL-1/2` 诊断与 `Order_hat` 秩序四判据（可延续/可协调/不外包/可再选择）；
     - **`O2-A` 代理/归责条件：** `Bearer -> Agency -> S6 归责` 与 `AI 三型` 对人类 `M(t)/σ_sr^{coll}` 的中介归责；
     - **`O2-M` 终极道德裁决：** 明确维持 `OPEN / HOLD` 的确切边界与禁止偷渡项。

### `R3-08`：二阶再选择（`C2-b 丙 / EA-1`）与 `CΨ` 灵性摩擦悬案（Theme C `C2-b/c`）
- **来源锚点：** [`7-19 非闭合压力卡`](../../01_Source_Intuition/SRT_GHOST_NONCLOSURE_PRESSURE_SOURCE_CARD_2026-07-19.md)、[`7-27 U5 校正卡`](../../01_Source_Intuition/SRT_CHOICEMAP_GHOST_U5_LIVE_CORRECTION_2026-07-27.md)、[`8-10 Simondon 互译卡`](../../01_Source_Intuition/SRT_SIMONDON_OPERATOR_YINYANG_SECOND_ORDER_SELECTION_CROSSWALK_2026-08-10.md)；[`Core_Law/SRT_Reference_Dynamics.md §1`](../../Core_Law/SRT_Reference_Dynamics.md#L22-L56)；[`Core/SRT_OPEN_TENSIONS.md §18`](../../Core/SRT_OPEN_TENSIONS.md#L855-L863)。
- **需作者拍板问题：**
  1. 完成对账 `Spine / Reference_Dynamics / Core_21 / 符号表`：保留“幽灵（非闭合压力描述）”与 `\hat G_\theta`（参数载体）非同一性，裁定 Ghost 三层面（算子历史互写、非闭合压力、`U5` 选择机制自身重入选择的二阶问题）哪些进入骨干表述、哪些保持 `OPEN`，以及 `EA-1` 结项所需的检索路径与旧表述处理条件。
  2. 在不修改 `Core` $\Psi_f \to 0$ 退化极限的前提下，裁定 [`F_3223`](../../01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_FULL_ARCHIVE_10_MODULES_RECONSTRUCTION_2026-11-18.md)“去选择”三义（减少显性干预 / 松动固化 `L2` / 取消原初 Selection）及“主体与摩擦关系改变”在 `R4` 灵性域的收敛位置（决定 `§18 CΨ` 是否仍保持 `OPEN`）。

---

## 3. 阶段流转与准入控制

1. 本文件与 [`SRT_R1_R2_FULL_RECONSTRUCTION_CONSOLIDATION_REPORT_2026-11-22.md`](SRT_R1_R2_FULL_RECONSTRUCTION_CONSOLIDATION_REPORT_2026-11-22.md) 先在独立 Draft PR 中接受内容验收。
2. 在 PR 通过并由作者单独确认“正式切换至 `R3`”之前，`STATUS.md` 中的 `CURRENT NEXT` 维持 **`R2`** 不变；任何 `R4` canonical 改写或 `R5` 实验激活均未授权。
