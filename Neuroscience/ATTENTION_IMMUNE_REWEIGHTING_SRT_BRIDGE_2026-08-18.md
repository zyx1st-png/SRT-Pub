---
id: SRT-ATTENTION-IMMUNE-REWEIGHTING-BRIDGE-2026-08-18
type: bridge_audit
tags: [Neuroscience, Attention, Interoception, Inflammation, Immune, Allostasis, HRV, d-value, Psi_f, Qualia, Reselectability]
status: active
layer: L1-L2-bridge
epistemic_layer: bridge-lab
claim_mode: interface
claim_level: P3-P4
canonical: false
date: 2026-08-18
dependency:
  - SRT-INTEROCEPTIVE-PRECISION-BRIDGE-2026-08-08
  - SRT-D-VALUE-CANONICAL
  - SRT-PSIF-CANONICAL
  - PATCH-NEURO-NEURAL23-EMBODIED-RHYTHMIC-ELIGIBILITY
  - PATCH-PHIL-PH-QUAL01-RESELECTIVE-QUALIA-GEOMETRY
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

## 0. 来源与证据边界

来源：Mizrachi N, Rottem M, Rozenkrantz L. *Voluntary attention regulates acute immune responses in humans*. *Nature Human Behaviour* (2026). DOI `10.1038/s41562-026-02541-1`。

本文记录的是用户提供完整版主文中可核对的结果。主文对 Supplementary 的部分分析只给出引用，因此涉及 recovery slope、moderator、预注册细节与次级 autonomic 指标时，应按原文的“主文可见证据”使用，不补写未直接读取的 supplementary 细节。

### 0.1 三个实验的最小事实

- **Exp.1, n = 37, within-subject, counterbalanced**：internal attention 对比 video distraction。20 min wheal 为 `3.5 ± 1.1 mm` 对 `5.0 ± 0.7 mm`，`d = 1.30`；flare 为 `10.6 ± 8.3 mm` 对 `14.0 ± 8.0 mm`，`d = 0.42`。wheal 的条件差异约 3 min 开始出现，并在 20 min 达到最大；AUC 也更小。
- **Exp.2, n = 20, independent sample**：两条件使用同一连续抽象图形序列与匹配任务结构，只改变注意方向。internal attention 再次产生约 `1.6-fold` 更小的 wheal / flare；约 90% 参与者在 distraction 下炎症更大。该实验主要排除了视觉输入、分心来源与主观任务难度的简单替代解释。
- **Exp.3, n = 17**：在 internal attention 下用 topical lidocaine 衰减 sensory signalling。20 min wheal：intact internal attention `3.1 ± 1.0 mm`；internal attention + lidocaine `4.0 ± 0.6 mm`；distraction `4.9 ± 1.0 mm`。lidocaine 削弱但未消除 internal-attention effect，并主要削弱后期 return-towards-baseline / recovery pattern。

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

因为 HRV 只是间接 autonomic proxy，论文没有直接记录、刺激或阻断 vagus，也没有在主文中完成一个足以证明中介因果的 mediation identification。

仍未建立：

```text
phenomenal / subjective experience itself
-> immune regulation
```

Exp.3 反而给出一个重要约束：`INT + lidocaine` 与 distraction 的 sensation rating 无显著差异（`P = 0.290`），但 wheal 仍显著不同。这说明 **felt intensity 不是完整的 causal currency**。

---

## 1. Source-backed increment：attention 不只是改变 report，也能改变 bearer 的后续身体状态

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

在同一个人的同类 histamine challenge 下，注意方向改变后，实际 wheal / flare 轨迹改变。对 SRT 最安全的吸收不是“心灵控制身体”，而是：

> **top-down attentional allocation can causally alter the later state of the same biological bearer through a measurable neuroimmune loop.**

这里的 `same bearer` 只是生理实验单位上的最低限度同体回流，不等于 SRT 已经证明完整的 bearer / subjecthood 条件，更不等于 future-selectability 或 identity-continuity 已被测量。

---

## 2. SRT mapping：这篇主要落在 `selection weight`，不是 `d`、`E_t` 或 `Psi_f`

现有 NEURAL23 已经区分：

```text
selection weight
!= selection opportunity / eligibility
!= selection friction
```

其中 `E_t(x)` 是 embodied timing / state 对 candidate admission window 的 P3 bridge；本文没有操纵 cardiac / respiratory / gastric phase，也没有识别一个瞬时 eligibility window。因此最自然的读法是：

```text
voluntary internal attention
-> W_intero(x) up
-> downstream control / regulation changes
```

而不是：

```text
attention = E_t
attention = d
attention = Psi_f
```

### 2.1 强制保留的四重非同一

```text
signal magnitude
!= subjective intensity
!= attentional / control weight
!= physiological burden
```

并继续保持：

```text
all of the above != canonical d
all of the above != canonical Psi_f
```

本文最漂亮的经验例子是：internal attention 下 inflammation-related sensation 更强，但 wheal / flare 更小；而 `INT + lidocaine` 与 distraction 的主观 sensation 又可相近，但实际 wheal 不同。

因此不得用：

```text
more felt -> more d
more felt -> more Psi_f
more inflammation -> more suffering
```

作为单调映射。

---

## 3. 多通道与时间分解：reweighting 不是一个全局“放松标量”

结果并不支持一个简单的：

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
- HRV 在 internal attention 下较高，但效应较小，且仍是 vagal activity 的间接指标；
- wheal 的时间动力学效应比 flare 更明显；
- sensory attenuation 主要削弱后期 recovery，而不是把全部 attentional effect 清零。

因此更好的桥接结构是：

```text
voluntary attention
-> channel-specific reweighting
-> top-down preparatory control
   + sensory-feedback-dependent updating
-> changed physiological trajectory
```

这允许同一个 attention shift 在不同 control channel / timescale 上产生不同方向的后果，而不是把身体压成一个统一 scalar。

---

## 4. SRT-side inference：target-relative optimality，而不是“向内注意更优”

**以下不是论文结论，是 SRT 侧从结果推出的可失败解释框架。**

作者自己提醒：较小炎症并不普遍等于更好。炎症在感染场景中具有适应功能；过度压低也可能损害 host defence。因此：

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
W_body-detail up
-> more variables re-enter high-level control
-> automatic motor policy becomes less stable
-> current performance may fall
```

但如果同一个身体信号可靠预示真实组织损伤，那么提高其权重又可能：

```text
current performance down
while
long-horizon bodily action capacity is preserved
```

这不是本文实验证明的结果，而是一个 SRT-compatible 的 **target-relative / timescale-relative trade-off**。真正要测的不是“internal attention 好还是坏”，而是：

> 什么后果结构使某个身体信号值得获得足以打断当前策略的控制权？

---

## 5. `d` 的正确进入方式：可能调制 reweighting 概率，不等于 weight

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
d up
not necessarily -> W up
but may increase P(reweighting / interruption)
under declared stake-coupled conditions
```

这不是 canonical 推导，只是未来实验接口。

---

## 6. 和现有 `precision x stake` 设计的直接连接

`INTEROCEPTIVE_PRECISION_SRT_BRIDGE.md` 已经要求把以下变量匹配：

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

Mizrachi et al. 让这个方向从 agent simulation 获得了一个更强的人体生理现实性依据：**attention allocation 确实可能进入生理闭环**。但论文仍未完成 stake manipulation。

下一步最有信息量的实验应反过来做：

```text
same bodily signal
same perceived intensity target
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

如果 richer active inference 在相同复杂度 / refit budget 下完整解释 stake、history、hysteresis、recovery 与 future-policy contraction，而 SRT-side bearer / `d` / `Psi_f` 变量没有增量预测或干预价值，则本桥必须缩减为 implementation-substitutable。

---

## 7. Qualia pressure：这篇不改变 PH-QUAL01 的 `Test E = NOT PASSED`

论文 Discussion 倾向于把 subjective sensory experience 描述成 physiological regulation 的 active contributor，但当前实验没有单独操纵 phenomenality。

可以同时保留以下结构解释：

```text
attention
-> sensory representation / precision
-> autonomic + local control
-> inflammation

and
attention
-> reported subjective experience
```

因此一个“所有结构控制都相同、但 phenomenally empty”的删除版本，并未被本文排除。

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
2. 该效应在匹配视觉输入与任务结构后仍复现。
3. sensory signalling 参与后期 resolution，但不足以解释全部 attentional effect。
4. HRV 变化与 parasympathetic / vagal engagement 一致，但不是 vagal mediation proof。
5. subjective sensation intensity 不能完整解释 physiological difference。

### SRT-side, non-canonical

1. 该论文是 `attention / reweighting -> same-bearer physiology` 的强 P3 bridge。
2. 它支持把 attention 看作可改变候选/通道 downstream influence 的实现机制，但不引入新 primitive。
3. `signal / felt intensity / control weight / physiological burden / d / Psi_f` 必须继续分离。
4. “同一 reweighting 在一个目标上有利、另一个目标上不利”是值得测试的 target-relative optimality 假说。
5. 真正可能区分 SRT 与 richer AIF 的问题仍是：在 matched present-state 条件下，bearer-specific future consequence 是否产生额外的 reweighting / hysteresis / future-selectability 预测。
6. 本文没有通过 phenomenality deletion test；PH-QUAL01 的强 constitutive proposal 不升级。

## 9. 当前裁决

```text
Source quality: A
Attention -> acute cutaneous inflammation causal evidence: A
Sensory contribution to late resolution: A-/B+
Vagal mediation claim: B-/open
Phenomenal experience itself as necessary causal contributor: C/open
SRT bridge value: A
Canonical increment: none
New primitive required: no
Best next test: matched signal x different bearer-specific future consequence
```