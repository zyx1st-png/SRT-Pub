---
id: SRT-ATTENTION-IMMUNE-REWEIGHTING-BRIDGE-2026-08-18
patch_id: SRT-ATTENTION-IMMUNE-REWEIGHTING-BRIDGE-2026-08-18
source_ids:
  - SRC-2026-08-18-NEURO-MIZRACHI-ATTENTION-IMMUNE
type: bridge_audit
domain: neuroscience_attention_interoception_psychoneuroimmunology
tags: [Neuroscience, Attention, Interoception, Inflammation, Immune, Allostasis, HRV, d-value, Psi_f, Qualia, Reselectability]
status: active
record_stage: source_bridge
layer: L1-L2-bridge
epistemic_layer: bridge-lab
claim_mode: interface
claim_level: P3-P4
canonical_status: non_canonical
canonical: false
integration_priority: very_high
date: 2026-08-18
dependency:
  - SRC-2026-08-18-NEURO-MIZRACHI-ATTENTION-IMMUNE
  - SRT-INTEROCEPTIVE-PRECISION-BRIDGE-2026-08-08
  - SRT-D-VALUE-CANONICAL
  - SRT-PSIF-CANONICAL
  - PATCH-NEURO-NEURAL23-EMBODIED-RHYTHMIC-ELIGIBILITY
  - PATCH-PHIL-PH-QUAL01-RESELECTIVE-QUALIA-GEOMETRY
target_future_doc:
  - Neuroscience/INTEROCEPTIVE_PRECISION_SRT_BRIDGE.md
  - Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
  - Neuroscience/SRT_Neuro_Predictions_Table.md
source:
  title: "Voluntary attention regulates acute immune responses in humans"
  authors: "Nofar Mizrachi; Menachem Rottem; Liron Rozenkrantz"
  publication: "Nature Human Behaviour"
  year: 2026
  doi: "10.1038/s41562-026-02541-1"
  peer_reviewed: true
  reading_basis: "user-supplied full-text PDF"
---

# Attention × Immune Regulation × SRT：人体因果桥与删除压力

> **结论先行**：Mizrachi、Rottem 与 Rozenkrantz 提供了一个强而边界清楚的人体因果结果：在相同 histamine skin-prick challenge 下，自愿把注意指向炎症部位的身体感觉，会改变后续 wheal / flare 的幅度与时间轨迹。该结果值得作为 SRT 的 **P3 attention / reweighting → bearer-physiology bridge**；它不证明 `attention = selection`、`attention = d`、`inflammation = Psi_f`、`HRV = vagal causation`，更不证明“主观感受本身”具有不可删除的额外因果作用。

## 0. 来源、证据锚点与贡献轨道

来源：Mizrachi N, Rottem M, Rozenkrantz L. *Voluntary attention regulates acute immune responses in humans*. *Nature Human Behaviour* (2026). DOI `10.1038/s41562-026-02541-1`。

承重 source-level claim 的回查锚点统一由：

```text
Materials/2026/SRC_2026_08_18_Neuro_Mizrachi_Attention_Immune_Regulation.md
```

维护。该 SourceCard 已按 PDF page / section / figure 标注 Exp.1、Exp.2、Exp.3、HRV 与 limitations；本 PatchNote 不重复维护全部页码，避免双份锚点漂移。

### 0.1 三个实验的最小事实

- **Exp.1, n = 37, within-subject, counterbalanced**：internal attention 对比 video distraction。20 min wheal 为 `3.5 ± 1.1 mm` 对 `5.0 ± 0.7 mm`，`Cohen's d = 1.30`；flare 为 `10.6 ± 8.3 mm` 对 `14.0 ± 8.0 mm`，`Cohen's d = 0.42`。wheal 的条件差异约 3 min 开始出现，并在 20 min 达到最大；AUC 也更小。
- **Exp.2, n = 20**：相对 Exp.1 是**独立 cohort**，但 Exp.2 内部仍是 **within-subject、counterbalanced 两条件设计**。两条件使用同一连续抽象图形序列与匹配任务结构，只改变注意方向。internal attention 再次产生约 `1.6-fold` 更小的 wheal / flare；约 90% 参与者在 distraction 下炎症更大。
- **Exp.3, n = 17**：返回参与者在 internal attention 下增加 topical lidocaine 以衰减 sensory signalling。20 min wheal：intact internal attention `3.1 ± 1.0 mm`；internal attention + lidocaine `4.0 ± 0.6 mm`；distraction `4.9 ± 1.0 mm`。lidocaine 削弱但未消除 internal-attention effect，并主要改变后期 return-towards-baseline / recovery pattern。

**符号消歧**：以上 source statistics 中的 `d` 一律是 **Cohen's d effect size**。它与 SRT canonical `d-value` 无关；本文后续裸写 `d` 时只指 SRT canonical 变量。

**预注册边界**：三项实验本身预注册，但论文明确说明 recovery slope、recovery classification 与 moderator analyses 未写入预注册，应视为 exploratory。故“后期 resolution”可作为机制压力，不应被提升为已预注册的独有 SRT 判别结果。

### 0.2 论文真正建立到哪一层

最强、最稳的因果结论：

```text
voluntary attentional allocation
-> altered acute cutaneous inflammatory trajectory
```

较弱但有机制支持：

```text
sensory signalling contributes to the late / resolution phase
```

候选而未被直接建立：

```text
attention
-> parasympathetic / vagal pathway
-> inflammation
```

因为 HRV 是间接 autonomic proxy；论文没有直接记录、刺激或阻断 vagus，也没有完成足以唯一识别 vagal mediation 的因果中介设计。

仍未建立：

```text
phenomenal / subjective experience itself
-> immune regulation
```

Exp.3 反而给出一个重要约束：`INT + lidocaine` 与 distraction 的 sensation rating 无显著差异（`P = 0.290`），但 wheal 仍显著不同。因此：

```text
felt intensity
!= complete causal currency for the physiological effect
```

### 0.3 Contribution route

**O-track — retained, narrowly scoped**：该来源提供一个高质量人体 realization，可用于组织：

```text
attentional reweighting
-> downstream control influence
-> altered same-organism physiological trajectory
```

并加固多通道非同一关系。这里的 O-track 是 **relation placement / boundary hardening**，不是“该论文证明 SRT ontology”。

**D-track — not claimed**：本文没有与 richer active inference / predictive-allostatic rival 做足以产生 SRT 独有判别增量的比较。真正的 D-track 仍等待 `precision × stake` 或 matched-present-state / different bearer-specific future-consequence 实验。

---

## 1. Source-backed increment：attention 不只是改变 report，也能改变身体后续状态

很多注意研究只到：

```text
attention
-> perception / report / reaction time
```

本研究把链条推进到：

```text
attention
-> altered physiological trajectory
```

在同一参与者的同类 histamine challenge 下，注意方向改变后，实际 wheal / flare 轨迹改变。对 SRT 最安全的吸收不是“心灵控制身体”，而是：

> **top-down attentional allocation can causally alter the later state of the same biological organism through a measurable neuroimmune loop.**

这里的 `same biological organism` 只是实验单位上的同体回流；它不自动满足 SRT 完整 bearer / subjecthood 条件，也不表示 future-selectability 或 identity-continuity 已被测量。

---

## 2. SRT mapping：主要落在 attentional / control reweighting，不是 `d`、`E_t` 或 `Psi_f`

现有 NEURAL23 区分：

```text
selection weight
!= selection opportunity / eligibility
!= selection friction
```

其中 `E_t(x)` 是 embodied timing / state 对 candidate admission window 的 P3 bridge。本文没有操纵 cardiac / respiratory / gastric phase，也没有识别一个瞬时 eligibility window。因此最自然的桥接只需要散文：

```text
voluntary internal attention
-> increased attentional/control weighting of interoceptive information
-> changed downstream regulation
```

而不是引入一个新的 `W_intero(x)` 量，更不是：

```text
attention = E_t
attention = d
attention = Psi_f
```

**本 PatchNote 不引入新的 scalar / operator / primitive。** 若未来确实需要把 attentional weight 数学化，必须另走定义、减法审计与符号治理。

### 2.1 强制保留的多重非同一

```text
signal magnitude
!= subjective intensity
!= attentional / control weight
!= physiological burden
!= canonical d
!= canonical Psi_f
```

本文提供了很干净的经验压力：internal attention 下 inflammation-related sensation 可以更强，而 wheal / flare 更小；`INT + lidocaine` 与 distraction 的主观 sensation 又可相近，但实际 wheal 不同。

因此不得建立：

```text
more felt -> more d
more felt -> more Psi_f
more inflammation -> more suffering
```

这类单调映射。

---

## 3. 多通道与时间分解：reweighting 不是一个全局“放松标量”

结果不支持简单的：

```text
internal attention
-> globally calmer physiology
-> lower inflammation
```

因为：

- heart rate 无显著条件差异；
- skin conductance 无显著条件差异；
- skin temperature 无显著条件差异；
- perceived anxiety 无显著条件差异；
- HRV 在 internal attention 下较高，但仍只是 vagal activity 的间接指标；
- wheal 的时间动力学效应比 flare 更明确；
- sensory attenuation 没有把全部 attentional effect 清零，而主要影响后期 resolution-shaped pattern。

更好的桥接结构是：

```text
voluntary attention
-> channel-specific reweighting
-> top-down preparatory control
   + sensory-feedback-dependent updating
-> changed physiological trajectory
```

这里前半段与后半段的机制拆分仍是 source-informed bridge，不是已被完全识别的神经通路。

---

## 4. SRT-side inference：target-relative optimality，而不是“向内注意更优”

**以下不是论文结论，是 SRT 侧从结果推出的可失败解释框架。**

作者自己强调，较小炎症并不普遍等于更好；炎症在感染场景中具有适应功能，过度压低可能损害 host defence。因此：

```text
attention reweighting
!= global optimization
```

更安全的是：

```text
same reweighting
can improve one target / timescale
while worsening another
```

### 4.1 运动员类比：低层自动化与身体保护可以冲突

一个已高度自动化的运动策略，可能需要把局部 proprioceptive / interoceptive detail 保持在较低显式权重，才能维持流畅动作：

```text
body-detail attention up
-> more variables re-enter high-level control
-> automatic motor policy may become less stable
-> current performance may fall
```

但如果同一个身体信号可靠预示真实组织损伤，提高其控制权又可能：

```text
current performance down
while
long-horizon bodily action capacity is preserved
```

这是 SRT-compatible 的 **target-relative / timescale-relative trade-off**，不是 Mizrachi et al. 的实验证明。真正要测的不是“internal attention 好还是坏”，而是：

> 什么后果结构使某个身体信号值得获得足以打断当前策略的控制权？

---

## 5. canonical `d` 的正确进入方式：可能调制 reweighting 阈值，不等于 weight

canonical `d` 关心 stake-coupled concern / irreversible-risk sensitivity。本文没有操纵 `d`，也没有测 future-selectability loss。

因此禁止：

```text
d = attention weight
d = salience
d = pain / itch intensity
d = inflammation magnitude
```

可保留的 P4 candidate 只有：

```text
matched signal / matched salience / matched immediate reward
+ different bearer-specific future consequence
-> different probability or threshold of attentional reweighting / interruption
```

也就是：

```text
higher stake-coupled concern
not necessarily -> higher momentary attentional weight
but may alter P(reweighting / interruption)
under declared conditions
```

这不是 canonical 推导，只是未来实验接口。

---

## 6. 和现有 `precision × stake` 设计的直接连接

`INTEROCEPTIVE_PRECISION_SRT_BRIDGE.md` 已要求尽量匹配：

- current homeostatic error；
- sensory noise；
- total precision budget；
- immediate reward / preferred-outcome strength；
- task difficulty；

然后只改变：

```text
resettable low-stake consequence
vs
same-bearer, future-capacity-reducing consequence
```

Mizrachi et al. 为这个方向增加的是**人体生理实现现实性**：attention allocation 确实可以进入身体调节闭环。它没有完成 stake manipulation，也没有建立 SRT 独有 prediction。

下一步最有信息量的实验仍应反过来做：

```text
same bodily signal
same perceived-intensity target
same immediate reward
same task demand

but

different future consequence structure
```

观察：

- reallocation onset / slope；
- interruption probability；
- policy switching latency；
- post-threat hysteresis；
- recovery；
- future reachable-policy loss。

并在数据前冻结：

```text
M_AIF-base
M_AIF-history
M_SRT-bridge
```

如果 richer active inference 在相同复杂度 / refit budget 下完整解释 stake、history、hysteresis、recovery 与 future-policy contraction，而 SRT-side bearer / `d` / `Psi_f` 结构没有增量预测或干预价值，则本桥对该目标应降为：

```text
implementation-substitutable
```

---

## 7. Qualia pressure：这篇不改变 PH-QUAL01 的 `Test E = NOT PASSED`

论文 Discussion / Conclusion 对 subjective sensory experience 使用了较强的功能性语言，但实验没有把 phenomenality 本身从 attention、representation、sensory signalling 与 autonomic/local control 中独立操纵出来。

可以继续保留结构解释：

```text
attention
-> sensory representation / precision
-> autonomic + local control
-> inflammation

and
attention
-> reported subjective experience
```

因此一个“相关结构控制保持、但 phenomenality 被删除”的反事实版本，并未被本文排除。

对 PH-QUAL01 的正确回流是：

```text
structural / reselective consequence evidence strengthened
phenomenal necessity evidence not strengthened
```

特别是：

```text
subjective intensity
!= actual physiological burden
```

与 PH-QUAL01 已有 `Psi_f_actual / Psi_f_felt` 分离纪律兼容；但它不能升级为：

```text
qualia = reselective deformation
qualia is necessary for immune regulation
```

所以强 constitutive proposal 继续保持：

```text
Test E = NOT PASSED
```

---

## 8. 最小保留结论

### Source-backed

1. 自愿注意方向可以因果改变人体局部急性 histamine-induced inflammatory trajectory。
2. 该效应在独立 cohort 中、匹配视觉输入与任务结构后复现；每个实验内部仍是 within-subject comparison。
3. sensory signalling 参与后期 resolution，但不足以解释全部 attentional effect；recovery slope / classification 本身属于探索性分析。
4. HRV 变化与 parasympathetic / vagal engagement 一致，但不是 vagal mediation proof。
5. subjective sensation intensity 不能完整解释 physiological difference。

### SRT-side, non-canonical

1. 该论文是 `attention / reweighting -> same-organism physiology` 的强 P3 bridge。
2. 它支持把 attention 看作可改变通道 downstream influence 的实现机制，但不引入新 primitive 或新符号。
3. `signal / felt intensity / control weight / physiological burden / d / Psi_f` 必须继续分离。
4. “同一 reweighting 在一个目标上有利、另一个目标上不利”是值得测试的 target-relative optimality 假说。
5. 真正可能区分 SRT 与 richer AIF 的问题仍是：在 matched present-state 条件下，bearer-specific future consequence 是否产生额外的 reweighting / hysteresis / future-selectability 预测。
6. 本文没有通过 phenomenality deletion test；PH-QUAL01 的强 constitutive proposal 不升级。

## 9. 当前裁决

```text
Source quality: A
Attention -> acute cutaneous inflammation causal evidence: A
Sensory contribution to late resolution: A-/B+
Specific vagal mediation claim: B-/open
Phenomenal experience itself as necessary causal contributor: C/open
Contribution route: O-track relation placement / boundary hardening
D-track: not claimed
SRT bridge value: A
Canonical increment: none
New primitive / symbol required: no
Best next test: matched signal × different bearer-specific future consequence
```
