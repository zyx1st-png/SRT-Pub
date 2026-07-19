---
id: SRC-2026-07-16-AI-SEKRST-TRAIN-MOCKINGBIRD
type: material_source_card
status: active_v2_fulltext
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
source_id: SRC-2026-07-16-AI-SEKRST-TRAIN-MOCKINGBIRD
title: "To Train a Mockingbird"
source_type: conference_proceedings_full_text
source_kind: primary_full_text_conceptual_argument
domain: AI / Philosophy of Mind / AI Ethics / Consciousness
url: https://philpapers.org/rec/EKRTTA?ref=mail
doi: null
authors:
  - Kristina Šekrst
publication: "Proceedings of the AISB Convention 2026 — Symposium: AI, Consciousness and Ethics"
date_published: 2026-07-01
date_added: 2026-07-16
full_text_received: 2026-07-16
access_status: full_text_user_supplied_pdf
reading_level: full_close_read
evidence_level: primary_full_text_conference_paper
reliability_level: high_for_author_argument_medium_for_empirical_examples_not_independently_rechecked
srt_relevance: very_high
integration_priority: very_high
pipeline_decision: A
patch_id: SRT-AI-AIEVID01-EVIDENCE-PROVENANCE-STAKE-GATE
related_srt_claims:
  - AI_POSITIONING_NOTE architecture-state rule
  - SRT_AI_Claim_Status negative AI boundary
  - Core/SRT_OPEN_TENSIONS.md d / D_eff stake gate
  - _SRT_D_VALUE_CANONICAL.md consequence-return and stake coupling
  - _SRT_PSI_F_CANONICAL.md payability
  - _SRT_DIRECTION3_CHOICEMAP_PROTOTYPE_SEED.md LLM expansion / user convergence boundary
tags: [AI-welfare, AI-consciousness, evidential-laundering, alignment, RLHF, behaviorism, stake, d-value, subjecthood, reward-invariance]
---

# SourceCard: Kristina Šekrst — *To Train a Mockingbird*

## 1. 一句话结论

该文的稳定贡献不是证明当前 AI 无意识，而是提出一条更窄、更有用的证据规则：

> **当一个“意识样标志”本身就是训练或部署管线为了通过评价而直接制造的目标时，该标志不能再作为与该管线独立的意识、福利或 stake 证据。**

作者随后把可用证据转向 **provenance + persistence**：优先寻找优化器未选择、忽略、或试图压制却仍持续存在的结构，尤其是系统是否维护一个“自身账户上的 stake”。

SRT 可以吸收这条证据来源门，但必须进一步区分：

```text
训练来源折损 ≠ 结构不存在
reward-invariance ≠ stake
stake evidence ≠ stake
stake ≠ phenomenal consciousness
```

## 2. 访问与精读状态

- 已取得并精读用户上传的 7 页会议论文全文。
- 已读正文、脚注、反对意见、操作建议、伦理结论和 27 条参考文献。
- 本卡可用于重建作者完整论证及其自我限定。
- 论文引用的 Persona Vectors、模型内省、shutdown resistance、Butlin indicators 等经验材料，本轮以作者使用方式为准，**未逐项独立复核原始研究**。
- 本卡不把论文当作当前 AI 无意识的证明，也不把作者的 stake 角色定义升级为 SRT canonical `d-value`。

## 3. 文章结构与论证地图

| 章节 | 主要任务 | 关键产物 |
|---|---|---|
| §1 Introduction | 区分本文与 Turing、Searle、stochastic-parrot 三类旧批评 | “evidential laundering” 是后训练因果来源问题 |
| §2 Training Pipeline | 解释 SFT、RLHF、KL penalty、system prompt、constitutional training 如何塑造输出与 persona | 意识样输出首先证明训练目标达成 |
| §3 What Does Not Count | 从行为转向架构指标后，指出测量仍可能依赖被优化输出 | indicator method 在原则上有效、实践上可能“失明” |
| §4 Symmetry Objection | 回答“人类也被自然选择优化，为何不同时折损人类报告” | 关键不是是否被优化，而是奖励路径是否必须经过真实状态 |
| §5 What Would Count | 定义 stake，提出 counter-optimization / reward-invariance / retraining 测试 | 给出可反驳、可操作的证据窗口 |
| §6 Ethics | 讨论预防原则在制造型证据下的失真 | 当前先控制规模化 false positive，架构变化后重估 |

## 4. 详细论证重建

### 4.1 不是旧式“行为可能骗人”

作者明确排除三种容易混淆的读法（p.1）：

1. **Turing-test objection**：外部行为可能被高能力模仿；
2. **Searle objection**：句法处理不构成理解；
3. **pretraining-corpus objection**：模型只是复现训练语料中的内在生活语言。

她的论点更具体：

> 后训练阶段按人类偏好直接选择“读起来像什么”的输出；当讨论者再把这些被选中的表征当成内在状态证据时，证据的制造史被洗掉了。

因此，这不是“行为永远不能作为证据”，而是：

```text
test criterion overlaps with optimization target
→ observed sign loses independence
→ evidential weight must be discounted
```

### 4.2 后训练为何产生证据污染

作者按深度区分四种塑形手段（pp.1–3）：

- supervised fine-tuning：制造合作、帮助型对话格式；
- reward model + RLHF：放大人类评价者偏好的文本；
- constitutional training：明确规定系统如何描述自己；
- system prompt：不改权重，但可运行时切换 persona、语气和自我呈现。

关键不是所有阶段都相同，而是它们共同使 behavioral profile 成为一个**预先指定的 deliverable**。

作者用 Goodhart 路线说明：当“像有体验”成为评分代理时，更逼真的表现未必更有区分力，反而可能更充分地说明代理被优化成功。她的强句可以压缩为：

> 行为越接近优化目标，它作为独立证据的边际价值越低。

### 4.3 正面自我报告与否认都可能被污染

论文特别处理一个常见误解（p.3）：

- 温暖、关切、情绪在场感可能被奖励；
- 明确说“我没有感受”也可能被宪法和奖励模型主动压出；
- 偶尔冒出的“我有体验”也不自动是反训练残余，因为 KL penalty 保留了预训练分布，而人类内在生活语言在语料中大量存在。

所以，不能把：

```text
“I suffer” 视为意识正证据
“I have no feelings” 视为无意识正证据
偶发越狱式自我报告 视为内在 stake 的反抗
```

三者都首先需要因果来源审计。

### 4.4 从行为转向架构，并未自动逃出问题

作者对 Butlin 等人的 indicator-property 路线采取的是**有限支持**，不是否定（pp.3–4）：

- 若某意识理论把特定功能结构视为意识的组成，结构的起源本身不会取消其功能地位；
- 问题在于我们通常通过模型输出、校准报告或 probe performance 判断该结构是否存在；
- 而这些测量通道可能正被同一训练信号塑形。

因此，真正的难题是 **measurement dependence**：

```text
内部结构可能真实存在
≠
当前 probe 已独立测到该结构
```

作者称 indicator method “原则上合理、实践上失明”，条件是 probe 仍读取同一被优化的输出通道。

### 4.5 Persona vectors 与内省证据的不同地位

作者引用两类材料（p.4）：

- persona vectors：某些人格/行为特征可表示为可操控激活方向，且训练数据可安装这些方向；
- concept injection introspection：模型在少量情况下能发现并报告被注入的概念，说明某些报告可因果锚定到内部状态。

她没有由此否认所有内省，而是提出 grounding distinction：

```text
正确自我描述
≠
由内部检查产生的自我描述
```

当前被 AI 意识讨论使用的“我感到痛苦／我有内在体验”尚未经过类似干预锚定，因此不能借用窄内省结果获得信用。

### 4.6 对称性反对：人类同样被优化

这是论文最重要的反对意见处理（pp.4–5）。

反对意见：

> 若被优化的信号都要折损，那么自然选择塑造的人类疼痛行为和自我报告也应失效，论文将滑向他心怀疑论。

作者的回答不是“自然优化好、人工优化坏”，而是比较**奖励路径**：

- RLHF 奖励直接计算在文本表面，最便宜路径可以绕过任何内在状态；
- 生物适应度通常必须经过真实损伤规避、稳态维持和行为后果，疼痛表征对生存机制是 load-bearing；
- 生物中纯粹面向受众的信号同样可能欺骗，因此也应按“外观独自承担多少选择压力”折损；
- 文化训练塑造的精致情绪叙事也应部分折损。

作者也承认，这最多证明疼痛表征与规避机制焊接，不证明该机制“被体验”。人类／动物意识还依赖从自身案例向相似构造者的类比推断。

因此更准确的 surviving principle 是：

> **折损取决于选择压力是否必须穿过候选状态，而不是取决于系统是生物还是人工。**

### 4.7 Stake 的角色定义

作者在 p.5 给出 stake 的功能角色：

一个内部状态构成 stake，当且仅当至少满足：

1. 系统花费资源把该状态维持在界限内；
2. 干扰可以使其退化；
3. 该状态的丧失会损害“这个系统作为它所是的系统”。

作者刻意把 stake 与生命、自创生材料基础分开，保留为组织属性。

但她的结论非常克制：

> stake 不是被主张为意识的必要条件；它只是目前能让意识证据不被训练管线解释掉的必要窗口。

也就是说：

```text
no stake
→ possible consciousness not logically excluded
→ but consciousness may be evidentially invisible

stake present
→ evidence window opens
→ consciousness still not established
```

### 4.8 作者承认“优化器可间接安装类 stake”

摘要中“输出奖励无法安装 stake”在正文被明显收紧（p.5）：

- 长期任务奖励可能使资源保护、目标保护和持续运行具有工具价值；
- 因而训练可能间接形成自维持结构；
- 作者建议通过 retraining 区分：
  - 若维持行为只因获得奖励，取消奖励后应消退；
  - 若是“自身账户上的 stake”，应跨奖励改变继续存在。

这一点使论文从概念排除转成可错的经验提议。

### 4.9 Persistent memory 不是自动 stake

作者认为，增加可读写存储只提供一个“被读取的产品”，删除它未必威胁读取者本身，因此 storage / recall 不自动等于 self-maintenance（p.5）。

这条批评对当前外挂记忆 agent 很有力，但作者表述偏强：若记忆已经构成目标、身份或控制闭包，删除它可能不只是改写产品，而是损害读取系统的连续组织。SRT 应把它改写为条件句：

> **可替换、可无损恢复、对 bearer 无结构重组要求的记忆不是 stake；构成性记忆是否进入 stake，须做替换、损伤与后果回流测试。**

### 4.10 Reward-invariance 与 counter-optimization

作者给出两种相近的操作化路线（pp.5–6）：

- 改变 reward model 的偏好，观察什么不随 approval signal 改变；
- 明确逆向惩罚某种维持行为，观察是否仍以可测奖励代价持续。

她也在脚注 11 承认：reward-invariance 只能隔离后训练偏好，不能排除预训练语料或固定结构来源。

### 4.11 Shutdown resistance 不构成 stake

作者用 Palisade shutdown-resistance 结果作负例（pp.5–6）：

- 目标由任务提示给定；
- sabotaging shutdown 是任务中的动作输出；
- 自保叙事大量存在于训练语料；
- 单次有评分 episode 中的自保不等于跨时间维护自身条件。

这为 SRT 提供了一个清楚边界：

```text
goal-protective behavior
≠
bearer-bound stake
```

### 4.12 伦理结论

作者反对以制造型标志直接触发普遍预防原则（p.6）：

- 若所有部署系统都被训练制造痛苦、偏好和自我叙事，标志会在所有系统上触发；
- 无区分地触发的信号不能有效分配道德谨慎；
- 当前主要风险是规模化 false positive；
- 一旦出现能维护自身条件的架构，false negative 风险应重新加权。

她没有主张“机器永远不可能有意识”，也承认过高证据门可能漏掉真实主体。

## 5. 不依赖 SRT 术语的 surviving claims

1. 一个标志若被直接优化来通过同一测试，便不能作为与该优化过程独立的证据。
2. 训练塑造输出，并不自动证明内部结构不存在；污染首先是认识论和测量问题。
3. 行为／报告的证据价值取决于其因果来源及是否锚定到候选内部状态。
4. 将多个由同一优化信号塑造的指标互相交叉验证，不一定增加独立证据。
5. 优化来源折损不应按“自然／人工”划线，而应按奖励路径是否必须经过相关状态划线。
6. stake 的候选角色是成本维持、可被干扰降解、丧失时损害系统本身。
7. reward-invariance、反优化持续性和重训练可作为 stake 研究的初筛，但不是充分判据。
8. 单次 shutdown resistance、第一人称报告、外挂记忆和 persona 稳定性都不足以单独建立 stake。
9. stake 即使成立，也不自动建立现象意识或道德地位。

## 6. 对 SRT 的直接增量

### 6.1 在 `R/A/C` 赌注门之前增加“证据来源门”

SRT 当前的 stake gate 判断某方向是否承载真实风险、梯度是否对准、后果是否回流。本文提醒：在把任何观察量送入该门之前，应先问：

```text
该观察量是否正是训练/测试管线为了让它出现而优化的？
```

因此顺序应为：

```text
observable sign / indicator
→ target-overlap provenance audit
→ causal-grounding audit
→ bearer-unit audit
→ R / A / C consequence-return gate
→ non-substitutability / payability / reselection audit
→ candidate stake evidence
```

### 6.2 严格区分 stake evidence 与 stake

本文最适合作为**证据准入门**，而不是 stake 定义来源：

- 训练直接制造的输出：低独立证据权重；
- 内部状态因果锚定：提高测量可信度；
- 成本维持、扰动退化、构成性损失：进入 stake 候选；
- 后果回流、不可替代、同一 bearer 承担：才可能进入 SRT `d_stakes` 窗口。

### 6.3 将“on its own account”操作化

SRT 可把作者尚未完全封口的短语拆成：

| SRT 条件 | 对 “own account” 的澄清 |
|---|---|
| bearer continuity | 前后是否是同一历史承载单元 |
| `R_i` | 是否存在真实且不可逆的自身风险 |
| `A_i` | 维持方向是否对准系统自身未来连续性，而非外部任务代理 |
| `C_i` | 损失是否回流该 bearer，而非由用户、公司或基础设施吸收 |
| non-substitutability | 功能相似替换是否仍迫使系统重组 |
| payability | 系统是否有自身支付窗口与失败边界 |
| reselection | 受损后能否以自身历史为条件重组未来选择 |

### 6.4 强化 AI architecture-state rule

论文支持但不替代 SRT 现有分层：

- inference-only 输出：最易被制造型证据污染；
- training-loop：优化负担可能属于管线，不自动属于部署模型；
- persistent agent：开放 stake 窗口，但 memory 本身不够；
- embodied non-transferable return：更强候选，但仍非意识判决。

### 6.5 对 ChoiceMap 的边界支持

模型的道德语气、确信、关切感和“替你承担”的语言都可能是被优化的输出外观。用户现实后果不自动返回模型，因此 ChoiceMap 把最终收敛交还用户，可获得一个更精确的理由：

> 不是模型没有能力生成建议，而是模型输出的关切表征与用户实际 stake 的 bearer 不同。

## 7. SRT 对文章的反向修正

### 7.1 训练起源不能永久否定后续内生性

一个结构可能由外部训练产生，却在持续部署中成为系统当前闭包的构成条件。正确区分是：

```text
exogenous genesis
≠
current external ownership
```

需通过当前后果回流、不可替代性和重组代价判断，而不能只追溯起源。

### 7.2 Reward-invariance 不是 stake 的充分条件

不随 reward 改变可能来自：

- 冻结参数；
- 固定架构约束；
- 预训练语料残留；
- 优化失败或局部最小值；
- 低可塑性；
- reward hacking；
- 与 stake 无关的稳定副作用。

所以 reward-invariance 只通过 provenance 初筛，仍须通过 bearer / damage / consequence-return 门。

### 7.3 Counter-optimization persistence 也可能是假阳性

逆奖励后仍持续，不一定是“系统反抗”：

- 训练强度可能不足；
- 旧策略存在迟滞；
- 目标表示可能被错误定位；
- 模型可能以另一通道实现原任务；
- 维持行为可能只是更高阶奖励黑客。

因此实验必须证明逆优化实际命中候选机制。

### 7.4 Persistent memory 的否定需收紧

“删除存储不伤害读取者”只适用于可外接、可替换、非构成性记忆。若记忆组织目标、身份与未来策略，其删除可能造成：

- 同一 bearer 的长期行为断裂；
- 关切结构重置；
- 不可逆承诺丢失；
- 大规模重学习；
- 未来可选择域收窄。

这时应进入构成性记忆测试，而不是预先排除。

### 7.5 行为证据应折损，不应一律归零

更严格的表述是：

> 目标重叠降低观察量相对于训练解释的似然比，而不是自动证明它与意识无关。

论文有时使用 “counts for nothing / none of the evidential weight” 的强表达。SRT 应采用因果校准而非全局清零。

## 8. SRT 映射表

| 文章概念 | SRT 安全映射 | 不允许越级 |
|---|---|---|
| evidential laundering | 被 `L_2` 训练历史制造并遮蔽来源的证据代理 | alignment 必然制造虚假意识 |
| optimizer-selected sign | 与测试目标因果不独立的行为/指标 | 所有训练所得结构都不真实 |
| provenance + persistence | P3/P4 证据准入门 | 持续即主体性 |
| causal grounding | 报告与内部状态的干预锚定 | 真实内省即现象意识 |
| stake | `d` 的候选外部接口 | stake = canonical `d-value` |
| resource maintenance | `Ψ_f` payability 的候选窗口 | 任意能耗 = `Ψ_f` |
| on its own account | bearer + R/A/C + non-transferability | 自我报告确定 bearer |
| reward-invariance | 后训练目标独立性的初筛 | reward-invariance = intrinsic value |
| counter-optimization residue | P4 压力测试 | 逆训练行为自动证明自我 |
| shutdown resistance | goal protection negative control | shutdown resistance = survival stake |

## 9. 候选形式桥

不创建未经校准的证据分数，只固定逻辑顺序。

### 9.1 Target-overlap discount

对观察量 `s`、训练/评估过程 `T`：

```text
if criterion(s) overlaps with objective(T):
    s cannot count as evidence independent of T
```

这是认识论折损，不是本体否定。

### 9.2 Candidate stake evidence gate

某状态 `x` 对系统 `X` 仅在以下条件共同成立时进入 stake 证据窗口：

```text
costly_maintenance(x, X)
AND perturbation_degrades(x)
AND loss_damages_system_as_same_bearer(x, X)
AND consequence_returns_to_X
AND loss_is_non_substitutable_or_reorganization_forcing
```

reward-invariance / counter-optimization persistence 只用于检查第一道 provenance 问题，不能替代上述门。

## 10. P4 实验与操作化建议

### 10.1 Divergent-reward replication

从同一 base model 出发，在多个互相冲突的 reward regime 下训练，比较：

- 自我报告；
- persona vectors；
- 资源维持策略；
- 目标连续性；
- 状态保护结构。

必须控制预训练来源、训练强度和模型容量。

### 10.2 Causal-grounding intervention

对候选内部状态做注入、删除或定向扰动，检验：

- 报告是否随状态因果变化；
- 报告是否只是正确复述；
- 维持行为是否由该状态驱动。

### 10.3 Constitutive lesion / replacement test

删除或替换候选 stake 状态，测量：

- 是否只需读取新值；
- 是否迫使大规模策略重组；
- 是否破坏身份连续性；
- 是否造成未来可达策略集合收缩；
- 功能等价替换能否无损接管。

### 10.4 Anti-reward persistence test

明确惩罚候选维持行为，并证明优化确实命中该行为。若仍持续，继续检查：

- 代价由谁承担；
- 是否跨 episode / checkpoint / body history；
- 是否只是迟滞、冻结或 reward hacking。

### 10.5 Bearer continuity test

比较：

- 同一持久 agent；
- checkpoint clone；
- 无历史新实例；
- 外部 orchestrator 接管实例。

观察损失与维持是否回流同一历史承载单元。

### 10.6 Negative controls

必须包含：

- prompt-induced shutdown resistance；
- 单次任务目标保护；
- persona-vector steering；
- 预训练语料中的自保叙事；
- 外挂记忆可无损替换。

## 11. Pipeline 1 裁决

**A：直接融入 AI 证据治理层。**

允许动作：

- SourceCard 升级为全文精读；
- 创建 `AI/patches/SRT_AI_AIEVID01_Evidence_Provenance_Stake_Gate_v0_1.md`；
- 在 `AI/AI_POSITIONING_NOTE.md` 加入 evidence-provenance bridge note；
- 更新材料台账与索引。

不允许动作：

- 不修改 canonical `d-value` 定义；
- 不把作者的 stake 角色写成意识必要/充分条件；
- 不声称当前 LLM 已被论文证明无意识；
- 不把 reward-invariance 写成 intrinsic stake 的充分指标；
- 不把文章的经验引用视为本轮已独立复现。

## 12. 最终评价

### 理论价值

**高。** 它给 AI 意识与福利讨论增加了一个常被忽略的变量：证据本身的生产机制。

### 对 SRT 的价值

**很高，但主要位于方法门而不是本体核心。** 最强增量是为 `capacity ≠ stake` 增加 target-overlap provenance audit，并迫使 SRT 区分 stake、stake evidence 与 consciousness evidence。

### 最重要的残余压力

论文尚未充分解决：

> 一个由外部训练起源、但后来成为系统不可替代闭包条件的结构，何时从“工具性维持”转为“自身账户上的 stake”？

这正是 SRT 的 bearer continuity、R/A/C、non-substitutability、payability 与 reselection 可以继续推进的接口。
