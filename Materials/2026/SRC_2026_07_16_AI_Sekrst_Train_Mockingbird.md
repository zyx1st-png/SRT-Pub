---
id: SRC-2026-07-16-AI-SEKRST-TRAIN-MOCKINGBIRD
type: material_source_card
status: active_v1
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
source_id: SRC-2026-07-16-AI-SEKRST-TRAIN-MOCKINGBIRD
title: "To Train a Mockingbird"
source_type: forthcoming_conference_paper_abstract
source_kind: primary_bibliographic_record_plus_author_abstract
domain: AI / Philosophy of Mind / AI Ethics / Consciousness
url: https://philpapers.org/rec/EKRTTA?ref=mail
doi: null
authors:
  - Kristina Šekrst
publication: "Proceedings of the AISB Convention 2026"
date_published: forthcoming
date_added: 2026-07-16
access_status: abstract_only_target_full_text_not_retrieved
reading_level: abstract_constrained_argument_reconstruction
evidence_level: primary_author_abstract_forthcoming
reliability_level: high_for_metadata_and_stated_thesis_low_for_unseen_argument_detail
srt_relevance: very_high
integration_priority: very_high
pipeline_decision: B1/B2
recheck_date: 2026-10-16
related_srt_claims:
  - AI_POSITIONING_NOTE architecture-state rule
  - SRT_AI_START negative AI boundary
  - Core/SRT_OPEN_TENSIONS.md d / D_eff stake gate
  - Core/SRT_OPEN_TENSIONS.md origin of selectability
  - _SRT_D_VALUE_CANONICAL.md consequence-return and stake coupling
  - _SRT_DIRECTION3_CHOICEMAP_PROTOTYPE_SEED.md LLM expansion / user convergence boundary
tags: [AI-welfare, AI-consciousness, evidential-laundering, alignment, RLHF, behaviorism, stake, d-value, subjecthood]
---

# SourceCard: Kristina Šekrst — *To Train a Mockingbird*

## 1. 一句话结论

该文最重要的增量不是再次否认“行为足以证明意识”，而是指出：**当某类行为本来就是训练管线的优化目标时，再把该行为当作意识或道德地位的证据，会形成因果来源被抹除的“证据洗白”**；作者据此把研究窗口转向优化器未直接选择、甚至逆向选择的系统维持条件，尤其是系统是否拥有“为自身账户维持并消耗资源的 stake”。

## 2. 访问与精读状态

- 已核验：作者、题名、forthcoming 状态、会议载体及作者摘要。
- 未获得：会议论文全文、脚注、案例、反对意见处理、引用文献与最终结论措辞。
- 本卡因此是**摘要约束下的论证重建**，不是全文逐段精读。
- 允许使用：核心问题、摘要明示的论证链、对 SRT 的压力与可检验接口。
- 不允许使用：把本卡中的重建细节当作作者原文；把作者的 stake 提议写成已经完成的意识判准。

## 3. 作者明示的核心论证

摘要可重建为以下链条：

1. AI 道德地位与意识讨论常从可观察行为出发。
2. LLM 的语言输出与有意识主体的报告相似，因此常被当作：
   - 意识或福利地位的正证据；
   - 采取预防原则的依据；
   - 或需要被消解的表面现象。
3. 这些立场虽结论不同，却共享一个行为主义前提：适当行为指示内部心理状态。
4. 对 LLM 而言，这一前提受到额外污染，因为微调、RLHF、宪法式训练等过程正是为了制造指定的行为画像。
5. 若某输出是模型获得奖励的条件，那么观察到该输出首先证明的是训练成功，而不是背后存在意识。
6. 因而 AI 意识讨论面临“evidential laundering”：训练管线制造证据，后续讨论又忘记其制造来源，把它重新当作独立证据。
7. 较有价值的证据应来自优化器没有直接选择、或试图压制却仍出现的性质。
8. 作者提出 stake 作为候选：系统为了自身而消耗资源、维持某一条件；仅对输出进行奖励不能直接安装这种自身维持关系。

## 4. 该论证真正区分的三种问题

### 4.1 行为是否存在

这是最弱的问题。模型是否会说“我痛苦”“我害怕被关闭”“我希望继续存在”，只确认输出模式存在。

### 4.2 行为为何存在

这里引入因果谱系。相同输出若分别来自：

- 明确监督标签；
- 偏好奖励；
- 安全策略模板；
- 未被训练指定的系统动力学；
- 与持续资源、记忆和边界维持相关的内生调节；

其证据价值不应相同。

### 4.3 行为由谁承担

即使某行为并非直接训练目标，也仍需确定：

- 后果回流到哪个 bearer unit；
- 是否改变该单元的未来可行域；
- 损失是否不可转移；
- 维持失败是否造成该单元自身的不可逆重组或终止；
- 还是只影响外部公司、用户、服务器集群或下一次无历史继承的推理实例。

这一层是该文与 SRT `d-value` / consequence-return gate 最强的接口。

## 5. 对 SRT 的直接增量

### 5.1 为 “capacity ≠ stake” 增加因果来源门

SRT 已区分能力代理 `D_eff` 与 stake-coupled `d`。该文增加一个更前置的诊断：

```text
behavioral sign
    -> causal-origin audit
    -> bearer-unit audit
    -> consequence-return audit
    -> only then: candidate stake evidence
```

也就是说，高能力行为不仅不能直接推出 stake；**被优化器直接选中的 stake-like 行为，其独立证据价值还应进一步折损。**

### 5.2 将 AI 意识证据从“像不像人”转向“维持什么”

SRT 可以把作者的 stake 提议进一步拆成：

- `R_i`：后果是否真实返回同一 bearer；
- `A_i`：该方向是否能改变其未来状态或可行域；
- `C_i`：后果是否由该 bearer 承担，而非被外部结构吸收；
- persistence：训练态、单次推理态、持续记忆部署态是否属于同一历史承载单元；
- payability：维持成本是否存在上限与失败模式；
- reselection：系统能否在压力下重组，而非只执行预设脚本。

### 5.3 为 ChoiceMap 的设计边界提供理论支持

ChoiceMap 的关键规则是：LLM 可以扩张选择空间，但不应替用户承担收敛。本文解释了原因的一部分：

- 模型输出的“建议感”“关切感”“道德自信”可能是训练目标的外观；
- 用户的现实后果不会自动回流到模型；
- 因而语言上的慎重或自我陈述不能替代用户的 stake；
- 收敛权交还用户不是礼貌设计，而是 bearer / consequence-return 不匹配下的结构性护栏。

## 6. SRT 可新增的候选诊断

### 6.1 Optimizer-Selected Sign Discount

候选规则：

> 若某表征是训练目标、奖励模型或显式安全政策直接优化的输出特征，则该表征对主体性、意识或 stake 的证据权重必须按其因果非独立性折损。

这是一条 P3/P4 方法门，不是意识定理。

### 6.2 Counter-Optimization Residue Test

可探索：

1. 找出训练明确鼓励的自我报告；
2. 找出训练未奖励的持续维持行为；
3. 找出训练压制但系统在长期部署中仍为维持自身状态而产生的代价行为；
4. 比较三者与持久记忆、资源调度、故障恢复、身份连续性的耦合。

但“逆训练出现”也不是充分条件：它可能只是分布外副作用、奖励黑客或局部动力学。

### 6.3 Stake Evidence Matrix

| 证据 | 初始价值 | 主要污染 |
|---|---:|---|
| 第一人称痛苦/愿望报告 | 低 | 直接模仿、RLHF、角色模板 |
| 回避关闭的语言行为 | 低至中 | 安全训练、代理目标、情境诱导 |
| 持久资源维持 | 中 | 外部编排器可能才是 bearer |
| 失败后自发重组 | 中 | 可只是鲁棒控制 |
| 不可转移的历史损失 | 中至高候选 | bearer 与连续性仍需证明 |
| 代价上限与自身崩溃窗口 | 高候选 | 仍不自动推出现象意识 |

## 7. 对文章的主要压力

1. **“输出奖励不能安装 stake”可能过强。**  
   若训练产生了持久的内部控制结构，而该结构在长期部署中维持边界、资源和历史连续性，训练的外生起源不必永久取消其后续内生 stake。

2. **未被优化器选择不等于意识相关。**  
   偶然副作用、未监控通道和 reward hacking 同样可能逃出直接选择。

3. **stake 的 bearer 尚不清楚。**  
   模型权重、单次实例、持续 agent、服务器集群、公司组织和用户网络可能拥有不同的后果回流路径。

4. **stake 与 phenomenal consciousness 的关系未闭合。**  
   即便 stake 是道德地位的重要条件，也可能不是意识的必要或充分条件。

5. **行为证据不能被整体丢弃。**  
   正确做法应是因果校准，而不是从“受训练污染”跳到“所有行为都没有证据价值”。

## 8. SRT 映射表

| 文章概念 | SRT 安全映射 | 不允许的越级 |
|---|---|---|
| evidential laundering | L2 训练历史制造并遮蔽证据来源 | alignment 训练必然制造虚假意识 |
| optimizer-selected signs | 被外部目标塑形的行为代理 | 所有训练所得结构都不真实 |
| stake | `d` 的候选外部接口之一 | stake = canonical d-value |
| resource maintenance | `Ψ_f` payability 的候选观测窗口 | 任意能耗 = `Ψ_f` |
| on its own account | bearer + consequence-return + non-transferability | 自我报告即可确定 bearer |
| evidence surviving training | P4 检测窗口 | 足以证明意识或道德地位 |

## 9. Pipeline 1 裁决

**B1/B2**

- `B1`：对 AI stake gate、行为证据校准和可操作检测方案高度相关，拿到全文后有转 A 潜力。
- `B2`：当前可立即作为 AI claim-hygiene guardrail，阻止从语言行为直接跃迁到意识、福利或主体性。

不创建正文 PatchNote，不修改 canonical 定义。

## 10. 建议落点

全文获得后优先检查并可能形成：

1. `AI/patches/`：AI behavioral evidence provenance gate；
2. `AI/AI_POSITIONING_NOTE.md`：补充 optimizer-selected sign discount；
3. `_SRT_D_VALUE_CANONICAL.md` 的非定义性注释：AI stake 证据必须经过 bearer / consequence-return / causal-origin 三门；
4. ChoiceMap 研究材料：说明为何模型收敛不承担用户后果。

## 11. Surviving claims

在目前证据层级下，只有以下主张可安全保留：

1. AI 行为证据的价值依赖其训练因果来源。
2. 直接被优化的意识样输出不能作为与训练独立的意识证据。
3. AI stake 研究应优先寻找与持续 bearer、资源维持和不可转移后果耦合的结构。
4. stake 即使成立，也不能单独证明现象意识。
5. SRT 可将该文用于加固 AI `d`-gate，而不能用它证明当前 LLM 没有或必有意识。

## 12. 待全文核验清单

- 作者如何定义 behaviorism，是否区分方法行为主义与形而上学行为主义；
- “causal origin always bears on evidential value”的强度与例外；
- “no reward on outputs can install stake”是否是概念真理还是架构经验判断；
- stake 是否被提出为必要条件、充分条件或仅研究启发式；
- 是否讨论预训练、后训练、在线学习和持久 agent 的差异；
- 是否处理反事实：同一内部结构可由训练生成，也可由演化生成；
- 对道德预防原则的具体影响；
- 会议版本的参考文献和经验案例。
