---
id: SRC-2026-07-20-AI-ZHANG-LEVIN-LEARNABLE-NOVELTY
type: material_source_card
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
source_id: SRC-2026-07-20-AI-ZHANG-LEVIN-LEARNABLE-NOVELTY
title: "Intelligence from Learnable Novelty"
source_type: arxiv_preprint_full_text
source_kind: primary_full_text_theory_and_experiments
domain: AI / Machine Learning / Complex Systems / Intrinsic Motivation / Information Theory
source_url: https://arxiv.org/abs/2607.18433
pdf_url: https://arxiv.org/pdf/2607.18433
code_url: https://github.com/Zhangyanbo/learnable-novelty
doi: null
authors:
  - Yanbo Zhang
  - Michael Levin
publication: arXiv preprint arXiv:2607.18433v1
date_published: 2026-07-20
date_added: 2026-07-22
access_status: user_supplied_24_page_pdf_full_text_read
reading_level: full_close_read_without_code_replication
evidence_level: primary_preprint_with_reported_multidomain_experiments
reliability_level: high_for_author_claims_and_reported_results_medium_until_code_replication_and_peer_review
srt_relevance: very_high
integration_priority: very_high
pipeline_decision: B1
parking_state: parked_with_named_reactivation_triggers
related_srt_claims:
  - SRT_Quick_Start.md bounded and historically parameterized selection operator
  - _SRT_PSI_F_CANONICAL.md payability burden and noise term boundaries
  - _SRT_D_VALUE_CANONICAL.md capacity proxy versus stake-coupled concern
  - SRT_Fisher_FEP_Landscape_Interface.md observer-relative geometry and FEP placement
  - papers/history_dependent_reachability/manuscript/MANUSCRIPT.md matched-present future reachability and selection-specific write-back
  - papers/selective_resynchronization/ structured novelty versus randomization
  - Core/SRT_OPEN_TENSIONS.md entropy noise and open-ended selection
reactivation_triggers:
  - history-dependent reachability adds a learnable-future or structured-reachability endpoint
  - selective-resynchronization needs an operational discriminator between generative novelty and noise
  - cross-observer or observer-swap replication tests reservoir-specific objective exploitation
  - a peer-reviewed or revised version resolves estimator and FEP-scope concerns
  - code reproduction is completed on ECA NCA MNIST or reinforcement-learning tasks
tags: [learnable-novelty, epiplexity, bounded-observer, reservoir-computing, minimum-description-length, novelty-search, free-energy-principle, intrinsic-motivation, cellular-automata, representation-learning, reinforcement-learning, reachability, observer-relative-complexity, psi-f-guardrail, d-value-guardrail]
---

# SourceCard: Zhang & Levin — *Intelligence from Learnable Novelty*

## 1. 一句话结论

该文把总惊奇拆成“有界观察者能够内化的结构”与“无法压缩的残差噪声”，并用固定随机 reservoir 加闭式 ridge readout 构造可微的 epiplexity 估计量；它为 SRT 提供了一个很强的候选操作量，用来描述**未来轨迹中有多少结构能被特定有界观察者继续提取和复用**，但该量不是 canonical `Ψ_f`、不是 `d-value`、不是 `W_sel`，也没有解释 `L_0 -> L_1` 的本体论实际化。

最安全的定位是：

> **learnable novelty 是 observer-relative learnable-structure yield / future-structure proxy，可作为 reachability、表征形成和探索研究的桥级端点；它不能被升级为 SRT 的选择成本、价值或主体性定义。**

## 2. 来源与精读状态

- 已读取用户上传的 24 页 arXiv v1 PDF，包括正文、主要图表、实验表、讨论、限制与附录入口。
- 来源为作者一手预印本，包含动力系统、无监督表征学习和强化学习三组实验。
- 论文声明提供代码与复现材料；本轮未完成代码下载、运行或数值复现。
- 本卡按作者报告记录结果，不把预印本结果写成已同行评审事实。
- 本卡不把作者对 novelty search、FEP、compression progress 或 universal computation 的统一叙述视为对这些理论全部版本的严格等价证明。

## 3. 论文的核心问题

作者把两个经典失败解释为同一个混淆：

```text
novelty maximization
-> noisy-TV trap
-> high surprise but no reusable structure

surprise minimization
-> dark-room trap
-> low surprise and no new structure
```

其共同原因是把以下两部分相加后当成单一目标：

```text
total surprise
=
learnable structure
+
unlearnable residual
```

作者提出只最大化第一部分，即 **learnable novelty**。

## 4. 概念与数学骨架

### 4.1 Prequential surprise

观察者按顺序预测目标 `Y = (y_1, ..., y_N)`，累积惊奇为：

```text
L = sum_i -log2 p(y_i | y_<i, X)
  = -log2 p(Y | X)
```

作者把该量解释为给定 `X` 时发送 `Y` 的 prequential description length。

### 4.2 有界 MDL 分解

在计算能力受限的模型类 `M_phi` 中：

```text
L^phi(Y | X)
≈
|M_phi*|
+
[-log2 p(Y | X, M_phi*)]
```

其中：

- `|M_phi*|`：观察者实际学到并可复用的模型结构；
- residual：该观察者无法进一步压缩的部分。

作者定义：

```text
S^phi(Y | X) = |M_phi*(Y | X)|
```

并把它与 Finzi et al. 的 epiplexity 对齐，将其作为目标时称为 learnable novelty。

### 4.3 闭式 reservoir 估计器

固定随机非线性特征映射：

```text
H = phi(X)
```

只学习线性 ridge readout：

```text
W_lambda
=
(H_tilde^T H_tilde + lambda I)^(-1) H_tilde^T Y_tilde
```

再用 readout 奇异值的谱描述长度估计结构量：

```text
S_hat^phi
=
1/2 log2 det(I + eta W_lambda W_lambda^T)
=
1/2 sum_i log2(1 + eta s_i(W_lambda)^2)
```

该形式压低重复方向的额外贡献，并奖励多个独立、可解码、非冗余结构方向。

## 5. 三组主要实验

### 5.1 动力系统与元胞自动机

作者评估 88 个局部不等价 elementary cellular automata：

- Rule 110 在其设置下获得最高 `S^phi`；
- 近常量、近平凡周期规则得分低；
- chaotic Rule 30 低于 complex Rule 54；
- 结果被解释为对经典 order / chaos / complexity 排序的无监督恢复。

随后直接对 neural cellular automaton 最大化 `S^phi`，多随机种子中产生移动、碰撞的 soliton-like 结构。

安全结论：

> 在该 observer、采样窗口与模型族下，可学习结构最大化把动力学推向既非平凡有序、也非纯噪声的中间区域。

不安全结论：

```text
max S^phi universally implies Turing completeness
solitons prove universal computation
Rule 110 ranking proves an absolute complexity measure
```

### 5.2 无监督 MNIST 表征

编码器 `E_theta(x)` 不使用标签，只最大化：

```text
S^phi(E_theta(X) | X)
```

作者报告：

- 表征逐渐形成按数字类别分离的区域；
- linear probe 从约 0.53 上升到 0.89；
- 5-NN 从约 0.66 上升到 0.89；
- 标签仅用于训练后的可视化和评估。

边界：该结果同时依赖有限代码维数、单位范数、ridge 强度、随机特征核的平滑偏置，以及 MNIST 中数字身份作为主导可分辨因素。它不证明任意数据上的 learnable novelty 都会恢复人类认为正确的语义类别。

### 5.3 强化学习 intrinsic reward

作者把轨迹未来窗口的 epiplexity 增量作为 PPO intrinsic bonus：

```text
r_t = r_task_t + beta (S^phi_t - S^phi_{t-1})
```

在十个环境中，论文报告：

- task + epiplexity 在九个任务上高于 task-only 平均回报；
- Walker2d 略低于 task baseline；
- state-magnitude 控制在多个任务中崩溃，而 epiplexity bonus 未出现同类严重崩溃；
- epiplexity-only 并非通用任务求解器，在终止任务中甚至可能回避完成目标，以延续结构流。

这一负边界非常重要：

> **可学习新颖性可以提供探索动力，但不自动提供任务目标、价值、stake 或规范方向。**

## 6. 六项审核门

| 审核门 | 结论 | 理由 |
|---|---|---|
| 相关性 | 通过，极高 | 直接涉及有界观察者、可学习结构、噪声区分、复杂性、表征、未来行为与探索 |
| 增量性 | 通过 | 为 SRT 增加 observer-relative structured-future proxy，并可与 `W_sel` / reachability 正交组合 |
| 证据等级 | 有条件通过 | 一手完整预印本，有多域实验与代码声明；尚未同行评审或独立复现 |
| 可对齐性 | 通过 | 可压成“有界观察者可提取未来结构量”，且能明确禁止与 `Ψ_f`、`d`、`W_sel` 混同 |
| 风险 | 中高、可管控 | observer exploitation、超参数依赖、FEP 简化、Rule 110 过度外推、MNIST 语义偶然性、任务终止偏置 |
| 落点清晰 | 通过 | 主落点为 HDR / selective resynchronization 的实验候选端点；备选为 AI/ML observer-relative complexity bridge；不进入 canonical 定义 |

## 7. 与 SRT 的安全映射

| 论文概念 | SRT 安全映射 | 不允许越级 |
|---|---|---|
| bounded observer `phi` | 对 `L_1` 数据进行有限解码和模型沉积的观察位置 | `phi = G_hat_theta` 的完整等同 |
| data-generating system `theta` | `L_1` 中可被优化的动力学、编码器或策略 | 论文参数空间等于 canonical `L_0` |
| `S^phi` / epiplexity | observer-relative learnable-structure yield；未来结构容量 proxy | `S^phi = Psi_f`、`S^phi = d`、`S^phi = intelligence` 的裸等号 |
| residual surprise | `S_noise` 的局部操作近邻 | 一切不可预测量都等于 canonical 噪声项 |
| maximize future `S^phi` | 保持结构化未来、探索与可继续学习能力的候选驱动 | 价值、关切、目标或主体性 |
| learned readout spectrum | 可独立解码方向的容量 proxy | stake-coupled `d-value` |
| observer-system relation | 复杂性是系统与有限观察者的关系属性 | 现实完全由观察者主观创造 |
| observer-observed coevolution | 移动的 learnability boundary；`L_1 <-> L_2` 共适应候选 | 已建立开放式智能或意识机制 |

## 8. 与 `Psi_f`、`d-value`、`W_sel` 的硬边界

### 8.1 `S^phi` 不等于 `Psi_f`

二者分别回答不同问题：

```text
S^phi:
what reusable structure did this bounded observer extract?

Psi_f:
what burden must be paid to actualize and maintain a selected reality?
```

因此：

```text
high S^phi with low measured cost is possible
high Psi_f with little learnable structure is possible
noise can raise total surprise without raising S^phi
```

允许研究二者的收益—成本关系，但禁止直接同一化。

### 8.2 `S^phi` 不等于 canonical `d`

谱方向数量描述可分辨或可解码容量；canonical `d` 需要这些方向与真实不可逆赌注、后果回流、bearer continuity 和未来选择能力耦合。

```text
learnable directions
!=
stake-coupled directions
```

MNIST 聚类、Rule 110 排名或探索回报都不证明系统“在乎”这些方向。

### 8.3 `S^phi` 不等于 `W_sel`

`W_sel` 识别过去是否由系统自身的选择—后果耦合形成内容特异的慢写回；`S^phi` 识别给定轨迹对观察者有多少可学习结构。

可出现四种组合：

| `W_sel` | future `S^phi` | 解释 |
|---:|---:|---|
| low | low | 无特异写回，未来也贫乏 |
| low | high | 外部设计或一般动力学产生丰富结构，但不是自身选择史写回 |
| high | low | 自身历史确实写回，却造成僵化、重复或结构贫化 |
| high | high | 自身选择史写回，并扩大或重组可继续学习的未来结构 |

该二维分解是本材料对 SRT 最稳定的增量。

## 9. 对 history-dependent reachability 的直接价值

现有 HDR 问题是：

```text
matched present
+
only slow history carrier differs
->
different future arrival distributions?
```

该文允许新增一个正交端点：

```text
matched present
+
selection-specific memory differs
->
different future learnable structure S^phi?
```

建议候选分析：

1. 对 active / yoked / sham / prediction-error memory 条件生成匹配未来轨迹；
2. 用冻结 observer 计算 `S^phi(Y_future | present)`；
3. 同时报告 arrival-distribution divergence 与 learnable-structure difference；
4. 加 observer ensemble、不同 reservoir 宽度与 observer-swap；
5. 检查高 `W_sel` 是否既可能带来 aligned advantage，也可能带来 blocked-path structural impoverishment；
6. 区分 raw surprise、state magnitude、predictive information、`W_sel` 与 `S^phi`。

候选联合量只可作为实验工作量，不升级 canonical：

```text
Delta N_phi_future
=
S^phi(future | history_plus)
-
S^phi(future | matched_history_minus)
```

以及成本约束下的研究性比值：

```text
structured-future yield per payable burden
=
Delta N_phi_future / (epsilon + Delta Phi)
```

该比值不得被命名为智能、价值或适应度的通用定义。

## 10. 对 selective resynchronization 的价值

learnable novelty 为“随机化之后什么算真正形成了新结构”提供一个候选读数：

```text
randomization
-> total surprise may rise

selective reorganization
-> observer-extractable independent structure may rise
```

因此可用于区分：

- 纯噪声增大；
- 简单周期锁定；
- 产生可传播、可组合结构的重组；
- 对一个 observer 有效、对另一个 observer 无效的局部适配。

但完整 selective resynchronization 仍需额外证明：

- 选择内容特异性；
- 写回；
- 后果回流；
- 新结构对环境变化的可迁移性；
- 不只是优化器利用固定 observer 的漏洞。

## 11. 关键风险与压力

### 11.1 Observer dependence 既是优点也是弱点

作者明确把复杂性定义为系统—观察者关系，这是与 SRT 的强接口。但固定 reservoir 同时意味着：

- observer architecture 决定什么结构可见；
- `lambda`、`eta`、feature width、normalization、target scale 与 horizon 改变可学习边界；
- 被优化系统可能生产“对该 observer 容易读、对其他 observer 无意义”的结构。

必须增加：

```text
observer ensemble
cross-architecture agreement
observer swap
held-out observer evaluation
adversarial anti-exploitation tests
```

### 11.2 从 Rule 110 到 universal computation 的推论过强

Rule 110 在 ECA 排名中最高是重要结果，但仍不足以推出：

```text
universal computation is the unique maximum of learnable novelty
all edge-of-chaos systems maximize S^phi
soliton presence certifies universality
```

需要更广系统族、不同观察者和真正 computation readout。

### 11.3 FEP 被压缩成 surprise minimization

文章用 dark-room 与 noisy-TV 构造统一叙述有启发性，但完整 active inference / expected free energy 通常还区分 prior preferences、epistemic value、policy selection 与 action。SRT 引用时应写成：

> 该文批评的是把总惊奇直接作为单一优化目标的简化版本，不是对所有 FEP / active-inference 形式的充分反驳。

### 11.4 MNIST 的类别涌现不是无偏语义发现

类别形成可能来自：

- 数据流形；
- random-feature kernel 的平滑偏置；
- 较强 ridge；
- 单位球约束；
- 有限代码维数；
- 数字类别是数据中最明显的低复杂度主因子。

应在多因素数据、背景冲突、风格—语义竞争和 out-of-distribution 数据上测试。

### 11.5 Intrinsic drive 的终止规避

纯 `S^phi` agent 可能把死亡、任务完成或 episode 终止视为结构流中断，因此：

```text
preserve novelty flow
!=
solve assigned task
!=
serve value
!=
protect the right bearer
```

这反而为 SRT 的 capability / persistence / stake / value 分离提供负例。

## 12. 双向增益

### 12.1 新增接口

- `observer-relative learnable-structure yield`：为可学习未来增加候选标量；
- `W_sel x S^phi_future` 二维分解：写回来源与未来结构质量分开；
- `structured novelty vs residual noise`：为 randomization / resynchronization 增加操作边界；
- `observer-ensemble gate`：防止单一解码器成为目标漏洞；
- `future learnability endpoint`：为 HDR 增加 arrival distribution 之外的端点。

### 12.2 反向修正

该文要求 SRT 收紧以下潜在误读：

- 丰富性不等于 stake；
- 可学习性不等于价值；
- complexity 不应轻易写成系统绝对属性；
- 噪声增加不等于选择空间增加；
- 结构产出不等于已经支付 canonical `Psi_f`；
- 观察者相关不等于主观任意性。

### 12.3 加固内容

它加固 SRT 已有区分：

```text
capacity != stake
surprise != selection-specific information
randomness != selection
future diversity != learnable future structure
persistence != task alignment
```

### 12.4 SRT 反哺

SRT 可以把作者的统一智能目标进一步分层：

```text
learnable structure yield
+
selection-specific writeback
+
payability
+
stake coupling
+
bearer continuity
+
directional readability
```

由此解释为什么同样高 `S^phi` 的系统可能分别是：有用表征、外部设计的复杂装置、自我维持代理、僵化探索者，或真正承担后果的主体候选。

### 12.5 残余压力

- observer-relative complexity 是否存在跨架构稳定不变量；
- 系统与 observer 共演化时如何避免彼此合谋式编码；
- learnable novelty 如何处理新结构的长期可迁移性；
- 如何把 `S^phi` 与真实资源成本、写回成本和环境代价放进同一账本；
- open-ended growth 是否需要不断扩张 observer，还是需要 observer population；
- “可学习结构”是否会系统性偏爱易压缩但规范上无价值的模式。

## 13. Pipeline 1 裁决

**B1：高优先级停驻，可转 A 的实验桥候选。**

理由：

- 一手完整预印本，稳定增量很强；
- 与 HDR、selective resynchronization、observer-relative complexity 高度对齐；
- 但核心估计器和多域结果尚未独立复现；
- 固定 observer 的目标利用风险未被充分排除；
- 文章对 FEP 与 universal computation 的强叙述需要降级；
- 当前最合适动作是保存完整 SourceCard 与实验接口，而不是修改 canonical 或建立正式 PatchNote。

允许动作：

- 作为 HDR future-structure endpoint 的候选方法；
- 在 selective-resynchronization 需要区分噪声与可学习重组时复活；
- 进行 reservoir ensemble、observer-swap 与代码复现；
- 未来 peer-reviewed / revised version 出现时重评 A。

不允许动作：

- 不修改 `Psi_f`、`d-value`、`G_hat_theta`、`L_0/L_1/L_2` canonical；
- 不写 `S^phi = Psi_f`、`S^phi = d` 或 `S^phi = W_sel`；
- 不声称论文证明智能的统一定义；
- 不声称 Rule 110 结果证明 universal computation 必然最大化 learnable novelty；
- 不声称无监督 MNIST 聚类证明语义客观涌现；
- 不声称 epiplexity-only agent 具有价值、关切或意识。

## 14. 具名复活触发条件

本卡只在以下工作线事件发生时复活：

1. `papers/history_dependent_reachability/` 决定加入 future structural richness / learnability endpoint；
2. `papers/selective_resynchronization/` 需要区分 pure randomization 与 structured reorganization；
3. 完成作者代码复现，至少覆盖 ECA ranking、NCA、MNIST、RL 中的一项，并记录 observer sensitivity；
4. 设计 cross-observer、held-out observer 或 observer-swap 实验；
5. arXiv 新版本或同行评审版本实质回应 estimator validity、observer exploitation、FEP scope 或 universality 外推；
6. SRT 正式建立“结构收益—可支付成本—selection-specific writeback”联合实验账本。

## 15. 最终评价

### 理论价值

**很高。** 它把 noisy-TV 与 dark-room 统一到“可学习结构 / 不可学习残差”的拆分，并把有界观察者放进复杂性定义中心。

### 对 SRT 的价值

**很高，但目前主要是实验与桥接价值。** 最重要的增量不是为 SRT 提供外部背书，而是提供 `W_sel` 之后的第二个问题：历史改变未来以后，新的未来究竟包含多少可被继续学习和复用的结构。

### 当前最稳的去材料化主句

> **选择史是否被写回，与写回后的未来是否仍包含可学习、可迁移和可支付的结构，是两个必须分别测量的问题。**
