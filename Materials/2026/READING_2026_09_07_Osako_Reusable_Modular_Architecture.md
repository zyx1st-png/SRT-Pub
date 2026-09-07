---
id: READING-2026-09-07-OSAKO-REUSABLE-MODULAR-ARCHITECTURE
type: reading_notes
status: active
layer: materials
epistemic_layer: evidence
claim_mode: evidence
canonical: false
date: 2026-09-07
source_title: "Reusable modular architecture enables flexible cognitive operations in the mouse brain and artificial recurrent networks"
source_doi: "10.1038/s41593-026-02410-0"
source_type: peer_reviewed_primary_research
tags: [GuidedReading, NeuralReuse, ComputationalReuse, RepresentationalReuse, mPFC, PPC, WorkingMemory, FunctionalModules, NeuralSubspace, RNN, TrainingHistory, OneFormation, Bearer, Objectification]
---

# 陪读笔记：Osako et al. 2026 — reusable modular architecture

> **性质**：面向当前 SRT Neuroscience Reconstruction Framework 与 Author Re-entry Cycle 1/2 的陪读记录。
>
> **Source guard**：Layer A 只使用用户提供的 *Nature Neuroscience* 一手论文。关于 SRT、One、Bearer、Selection-position、Cycle 1/2 的内容属于仓库侧 Layer B / subtraction，不归因于论文作者。
>
> **Theory guard**：本文件不是 definition authority，不打开新的 Neuroscience deep well，不修改 canonical owner，不把神经模块化或 RNN 结果本体化为 SRT 结构。

---

## 1. 为什么这篇值得陪读

这篇文章的价值不在于“又找到一篇支持 SRT 的论文”，而在于它把四个容易混在一起的对象拆得非常清楚：

```text
represented content
computational operation
functional neural subspace / cluster
continuing bearer / One
```

论文真正建立的是前面三层之间的一组经验关系；第四层并没有被论文回答。

因此它最适合作为 SRT 的**高质量邻居与负向压力材料**：

> 如果同一 computation 可以在不同 content 上复用，功能 cluster 可以参与多个时间段，而训练历史又可以通过普通 RNN 学习改变几何结构，那么 SRT 不能再把“稳定功能”“历史效应”“重复调用”“模块化”中的任何一项直接当成 One/Bearer 的证据。

---

## 2. 先读懂论文自己的问题

论文开头把 reuse 分成两层。

### 2.1 representational reuse

同一类信息在不同时间或不同 context 中使用相似 neural representation。

例如：

```text
Stim 1 = high / low tone
Stim 2 = high / low tone

same stimulus-processing subspace
can decode both epochs
```

这里保持相对稳定的是**被表示的信息类型及其 coding geometry**。

### 2.2 computational reuse

更强的问题是：

```text
information content changes
but
same computation is reused
```

论文的关键例子发生在 memory delay：

```text
Delay 1:
maintain past sensory stimulus

Delay 2:
maintain prospective behavioral choice
```

二者 content 不同，但在 mPFC 中可以共享 memory-maintenance subspace。

所以论文真正推进的是：

```text
reuse need not stop at representation
reuse can occur at the level of computation
```

这对 SRT 很重要，因为它马上拆掉一个危险直觉：

```text
same functional role over time
!= same represented object
```

进一步也不能推出：

```text
same functional role over time
= same bearer
```

---

## 3. Fig. 1–3：从 task 到 shared subspace

### 3.1 task 结构

DMS-dr task 要求小鼠：

```text
Stim 1
-> Delay 1
-> Stim 2
-> Delay 2
-> report match / nonmatch
```

这使实验在同一个 trial 中重复出现两类操作：

- stimulus processing；
- memory maintenance。

因此设计本身非常适合问：

> 大脑是为每个时刻重新建一套计算，还是复用同一套功能资源？

### 3.2 stimulus subspace

mPFC 和 PPC 中，用 Stim 1 训练的 classifier 可以跨到 Stim 2，反之亦然；共享 stimulus geometry 甚至进入 passive-listening context。

这是论文的 representational reuse。

SRT-side 最安全的读法：

```text
publicly measured neural representation
can retain a reusable organization across context
```

但不能写成：

```text
same decoded subspace
-> same ontological object
```

因为 subspace 本身就是由记录边界、变量定义、classifier、时间窗和分析方法构造出来的 measurement object。

### 3.3 memory subspace

mPFC 的关键结果更强：

```text
Delay 1 stimulus memory
and
Delay 2 upcoming-choice memory
```

尽管内容不同，classifier 仍能 cross-generalize。

更重要的是，mPFC 中 memory subspace 越共享，行为表现越好。

这意味着 reusable computation 不是纯粹几何巧合，而与 task performance 有关系。

但即便如此，它仍然只支付：

```text
shared computation
+ behavioral relevance
```

没有支付：

```text
same bearer
same consequence owner
same numerical individual
same subject
```

---

## 4. Fig. 4–6：从 subspace 到 functional cluster，再到 RNN perturbation

这部分是最容易被 SRT 过度吸收的地方。

### 4.1 functional clustering

作者先问：这些 reusable subspace 是“所有 neuron 混合贡献”的 population effect，还是存在功能上比较明确的 neuronal subpopulation？

结果显示 mPFC 与 PPC 的 response profile 都不是简单随机均匀分布，并能用 GMM 得到 functional clusters。

mPFC 的 cluster differentiation 最清楚：

```text
putative stimulus-processing cluster
putative memory-maintenance cluster
```

但 PPC 更 multiplexed。

这个区域差异很重要：

```text
functional specialization
need not imply
one universal clean modular architecture
```

### 4.2 module 不是固定盒子

论文的结果反而支持一个比较谨慎的理解：

```text
computation can have a reusable functional locus
while
implementation can remain distributed / multiplexed / context-dependent
```

因此 SRT 如果以后讨论 Selection-position / One，不应预设：

```text
One = one anatomically fixed cluster
```

更可行的开放问题反而是：

> 一个持续的功能位置，是否可以在成员贡献、具体内容和瞬时几何不断变化时仍被重新实现？

注意：这是由论文触发的 SRT 问题，不是论文给出的答案。

### 4.3 RNN perturbation 的证据边界

作者训练 data-constrained RNN 去重现 mPFC neural dynamics，然后做 cluster-specific in-silico silencing。

结果呈现很漂亮的 epoch specificity：

```text
silence stimulus cluster during stimulus epoch
-> performance impairment

silence memory cluster during delay epoch
-> performance impairment
```

连接层面：

```text
silence stimulus-cluster -> memory-cluster connection
in stimulus epoch
-> impaired performance
```

所以最强安全结论是：

> RNN 中存在与 empirical population structure 一致的候选 modular mechanism，并且 module interaction 对 network dynamics 有功能作用。

这里必须挡住一个跳跃：

```text
RNN cluster-specific lesion
!=
direct cluster-specific causal lesion in the mouse brain
```

作者自己也把更精细的 time-specific animal perturbation 留给 future work。

---

## 5. training history：本篇对 Cycle 1 最重要的负向结果

论文观察到 memory-maintenance subspace 中 stimulus / choice coding direction 的 alignment 与训练顺序有关。

作者随后在 RNN 中改变 pre-training history，并重现这种 geometry bias。

因此得到：

```text
training history
-> sculpts current coding geometry
```

对一般神经科学，这是一个正结果。

对当前 SRT Cycle 1，它首先是一个**generic-baseline strengthening**。

Cycle 1 已经经历过：

```text
past history
-> current causal state
-> later selection / repair / output
```

只要这条链能被普通 recurrent learning / stored-state / credit assignment 完整吸收，就不能作为 SRT-specific Bearer-genesis discriminator。

Osako 进一步说明：

```text
history-shaped present geometry
+
functional reuse
+
behavioral relevance
```

仍然可以在普通 RNN 学习中出现。

所以本篇不应拿来“救回” Cycle-1 history-localization；它恰恰把 Level-0 generic baseline 拉得更高。

---

## 6. 对 Cycle 1 的正式 subtraction

### 6.1 被论文加强、但不能归 SRT 独有的部分

```text
history matters
history modifies later computation
history changes representational geometry
history-dependent organization can persist across time
recurrent networks can preserve and reuse learned functional structure
```

这些都属于普通 learning / recurrent dynamics 可支付的 territory。

### 6.2 Cycle 1 仍剩下什么问题

Cycle 1 当前真正保留的不是：

```text
history exists
```

而是较窄的 genetic ordering：

```text
repeated consequences increasingly close on / reconfigure
one continuing organization
-> same-unit bearing relation may participate in Bearer formation
```

Osako 没有测试：

- consequence 到底归属于哪个 continuing unit；
- functional cluster 的 membership 变化时是否仍是“同一个”历史 bearer；
- reset / copy / outsourcing 后 consequence history 是否仍回到同一 unit；
- Bearer 是 measurement object、functional module 还是 organism-level process。

因此：

```text
Cycle-1 Level-2 route: not reopened
Cycle-1 genetic question: still conceptually pressureable
```

---

## 7. 对 Cycle 2 的正式 subtraction

Cycle 2 当前 author-confirmed dependency 是：

```text
subjectless Selection before a completed One
-> foregrounding + relative backgrounding
-> historical mutual support / relative inhibition
-> continuing Selection-position / One formation
```

Osako 可以提供几个很诱人的 analogy：

```text
functional specialization
competitive / selective population geometry
reusable modules
history-shaped organization
```

但这些 analogy 全部必须停在 Layer B。

原因是：

1. 论文开始时已经有 mouse、brain、mPFC/PPC、task epochs、neuronal population 这些 Given Ones；
2. 它研究的是一个已经存在的 nervous system 如何组织 computation；
3. functional clusters 是 task-related network organization，不是“completed One 出现以前的 primitive Selection”；
4. RNN 的 unit / network boundary 也是建模时给定的；
5. history bias 是 learning history，不是 One/Bearer genesis theorem。

所以：

```text
Osako modular reuse
!= Cycle-2 primitive bearerless Selection
!= One formation
```

本篇对 Cycle 2 的最大价值是逼出一个更干净的问题：

> 如果一个 functional locus 可以跨内容复用、跨时间重新调用、成员贡献又不是固定不变，那么 SRT 所说的 continuing Selection-position 究竟比“可复用 computation”多了什么？

如果回答只是：

```text
它能重复做同一功能
```

那已经被 Osako / ordinary recurrent computation 支付。

---

## 8. 与 Posani / NEURAL18 的关系：不是谁推翻谁

仓库中的 Posani material 强调：

```text
within-region neuronal selectivity often remains diverse
high separability does not require clean categorical clustering
```

Osako 在 mPFC 看到更明显的 functional clustering。

两者表面有张力，但 Osako 自己提出一个关键限定：task demand 可能影响 modular organization；需要 flexible input-output mapping 的任务更容易出现 subcluster organization。

因此最安全的联合读法不是：

```text
brain is modular
```

也不是：

```text
brain is nonmodular
```

而是：

```text
population organization
is task-, scale-, region- and analysis-dependent
```

对 SRT 的反向纠偏：

```text
categorical cluster != anchoring
non-clustered distributed code != absence of functional organization
shared subspace != bearer
stable function != fixed implementation membership
```

这正好强化 Neuroscience Framework 的 objectification discipline。

---

## 9. N1 / N2 / N3 / N5 / N6 路由

| Framework family | 本篇提供什么 | SRT 需要继续问什么 | 禁止跳跃 |
|---|---|---|---|
| N1 object/state/representation identity | same stimulus representation across epochs; same memory computation across changing content | same subspace / computation under what transformation is still counted as same? | shared geometry = natural ontological identity |
| N2 historical ownership / efficacy | training history biases later coding geometry | history is merely present-state information, or belongs to / reconstitutes one continuing unit? | history effect = history ownership |
| N3 relational/distributed organization | mPFC modularity versus PPC multiplexing; inter-module connection matters | functional locus can remain continuous despite distributed changing realization? | functional cluster = fixed One |
| N5 measurement objectification | classifier, subspace, GMM cluster, pseudopopulation, task epoch construct public neural objects | which analyst cut corresponds to causal / historical unit, if any? | decoder / cluster boundary = natural bearer boundary |
| N6 bearer/consequence attribution | task performance depends on neural architecture | whose consequence changed: cluster, network, organism, behavioral system? | local causal contribution = consequence ownership |

Secondary N4 pressure：reusable computation shows a form of currently available processing capacity, but capacity remains distinct from Selection, authority and consequence ownership.

---

## 10. 本篇最有价值的 One-formation 反问

### Q1. operation identity 与 bearer identity 是否可以分离？

论文几乎肯定要求答案是：可以。

```text
same operation
can act on different contents
```

但 SRT 还要额外回答：

```text
what makes later operation belong to the same continuing One?
```

### Q2. stable functional locus 是否要求 stable membership？

论文不支持这种强要求。

PPC 的 multiplexing 尤其提醒：

```text
functional continuity
may coexist with distributed implementation
```

因此未来 One-formation 如果继续发展，最好避免“固定成员集合”作为未经论证的前提。

### Q3. history-shaped reusable module 与 SRT history-bearing One 有何差别？

目前最重要的回答是：

```text
Osako-side:
history sculpts the state / geometry of a computational network

SRT unresolved stronger burden:
which continuing unit owns / bears consequences such that
those consequences participate in reconstituting that same unit's
future Selection-position?
```

前者已有普通神经网络解释；后者仍需要独立 discriminator 才能进入 Level 2。

### Q4. 如果 members / content / state 都变化，什么是 STILL-THIS？

这是本篇最值得保留给未来作者重构的问题。

可能的候选不能直接从论文推出，但至少应该能区分：

```text
same represented content
same computation
same functional locus
same causal unit
same historical bearer
same organism
```

这六种“same”不应再被混写。

---

## 11. Layer B 当前可保留的 SRT gain

经过 subtraction，本篇只建议保留以下 bounded gains：

1. **content / computation / implementation / bearer 四分**；
2. reusable computation 作为 One/Bearer 推理的 negative control；
3. training-history geometry 作为 Cycle-1 ordinary-learning baseline strengthening；
4. mPFC/PPC 差异作为“functional locus 不必等于固定 modular box”的压力；
5. Posani + Osako 联合形成 task/scale-sensitive objectification guard；
6. `same function over time != same bearer` 作为 N1/N6 交叉 guard。

不保留为新增量：

```text
history matters
modularity exists
recurrent dynamics can maintain memory
functional specialization
learning shapes geometry
```

这些全部已有成熟科学 owner。

---

## 12. Layer C — discriminating / empirical increment

**None claimed in this pass.**

本篇没有给出：

```text
SRT One/Bearer vs ordinary reusable module matched test
consequence-ownership intervention
same-state / different-bearer prospective divergence
primitive Selection test
Selection-position genesis manipulation
subjecthood / consciousness discriminator
```

因此当前 disposition：

```text
Layer A: HIGH-VALUE PRIMARY EVIDENCE
Layer B: HIGH-VALUE SUBTRACTION / OBJECTIFICATION PRESSURE
Layer C: NONE
new neuroscience deep well: NO
canonical writeback: NO
```

---

## 13. Future-use rule

如果未来重新使用这篇，不要问：

> “它是不是支持 SRT？”

优先问：

> “普通 reusable computation 已经能解释到哪里？SRT 声称的 One / Bearer / Selection-position 到底在哪一步开始多出一个不能被普通 recurrent modular dynamics 吸收的 burden？”

只有后一个问题有机会产生真正的 Level-2 路径。

---

## 14. Hard guards

Do not write:

```text
reusable module = One
memory subspace = Bearer
functional cluster = historical bearer
training history = Selection sedimentation
history-shaped geometry proves OWN-HISTORY
mPFC modularity proves center-surround One formation
RNN lesion proves animal cluster-specific causal architecture
shared computation proves numerical identity
stable function proves stable membership
neural reuse proves SRT
```

Primary SourceCard:

`Materials/2026/SRC_2026_09_07_Neuro_Osako_Reusable_Modular_Architecture.md`

Routing / subtraction audit:

`Operations/Audits/SRT_OSAKO_REUSABLE_MODULAR_ARCHITECTURE_ROUTING_SUBTRACTION_2026-09-07.md`
