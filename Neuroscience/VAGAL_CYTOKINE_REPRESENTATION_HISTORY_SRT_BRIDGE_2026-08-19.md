---
id: SRT-VAGAL-CYTOKINE-REPRESENTATION-HISTORY-BRIDGE-2026-08-19
patch_id: SRT-VAGAL-CYTOKINE-REPRESENTATION-HISTORY-BRIDGE-2026-08-19
source_ids:
  - SRC-2026-08-19-NEURO-HUERTA-VAGAL-CYTOKINE-REPRESENTATION
type: bridge_audit
domain: neuroscience_neuroimmune_interoception_vagus_representation
tags: [Neuroscience, Vagus, Cytokines, Interoception, Inflammation, Representation, History, CandidateFormation, d-value, Psi_f]
status: active
record_stage: source_bridge
layer: L1-L2-bridge
epistemic_layer: bridge-lab
claim_mode: interface
claim_level: P3-P4
canonical_status: non_canonical
canonical: false
integration_priority: very_high
date: 2026-08-19
dependency:
  - SRC-2026-08-19-NEURO-HUERTA-VAGAL-CYTOKINE-REPRESENTATION
  - SRT-ATTENTION-IMMUNE-REWEIGHTING-BRIDGE-2026-08-18
  - SRT-INTEROCEPTIVE-PRECISION-BRIDGE-2026-08-08
  - SRT-PSIF-CANONICAL
  - SRT-D-VALUE-CANONICAL
target_future_doc:
  - Neuroscience/SRT_Neuro_08_Immune_Dist.md
  - Neuroscience/INTEROCEPTIVE_PRECISION_SRT_BRIDGE.md
  - Neuroscience/SRT_Neuro_Predictions_Table.md
source:
  title: "Neural representation of cytokines by vagal sensory neurons"
  authors: "Tomás S. Huerta et al."
  publication: "Nature Communications"
  year: 2025
  doi: "10.1038/s41467-025-59248-6"
  peer_reviewed: true
  reading_basis: "user-supplied full-text PDF"
---

# Vagal Cytokine Representation × SRT：状态依赖表征、历史接口与判别实验

> **结论先行**：Huerta 等人提供了一个边界清楚的外周神经免疫结果：结状神经节不是把 cytokine 信号原样转送给大脑的简单 relay，而是在进入中枢之前形成可区分的实时响应结构；DSS colitis 又会把这一接口重塑为“baseline 更活跃、特定 evoked response 更弱、类别 separability 更低”的状态。对 SRT 最安全的吸收是 **P3 state-dependent peripheral representation / interface-history bridge**，不是 `immune activity = Selection`、`inflammation = Psi_f`、`nodose = bearer` 或 `history effect = SRT uniquely confirmed`。

## 0. 来源、证据锚点与贡献轨道

来源：Huerta TS et al. *Neural representation of cytokines by vagal sensory neurons*. *Nature Communications* 16, 3840 (2025). DOI `10.1038/s41467-025-59248-6`。

承重 source-level claim 的回查锚点统一由：

```text
Materials/2026/SRC_2026_08_19_Neuro_Huerta_Vagal_Cytokine_Representation.md
```

维护；本 bridge 不重复维护完整页码。

### 0.1 Source-backed minimum

```text
IL-1β / TNF / IL-10
-> distinguishable nodose response dynamics
```

且在 DSS colitis 中：

```text
spontaneously active neurons ↑
while
spontaneous transient amplitude ↓

TNF / IL-10 evoked amplitude ↓
IL-1β amplitude: no comparable significant reduction

cytokine-cluster separability ↓
```

因此最重要的 source-level dissociation 不是“炎症让迷走神经更强或更弱”，而是：

```text
activity amount
!= event-specific discrimination
```

### 0.2 Contribution route

**O-track — retained / primary.** 论文给出一个很好的经验层级：

```text
bodily state
-> state-dependent peripheral representation
-> downstream central access/control
```

这为 SRT 提供的是 relation placement、history/interface 分层和旧单标量 framing 的反向修正。

**D-track — not established by the source.** 论文没有冻结 active inference / predictive-processing / allostatic / ordinary history rival，也没有操纵 bearer-specific future consequence。D-track 只保留为后续 P4 设计。

---

## 1. Source-backed increment：外周感觉站点已经不是“透明传输线”

作者在 Discussion 中明确把结果概括为：vagus body–brain axis 的 cytokine sensing 不是 simple linear relay。部分 nodose neurons 对单个 cytokine 有选择性，另一些响应多个 cytokine，但仍保持不同 activity pattern。

最安全的结构是：

```text
immune difference
-> peripheral neural transformation / representation
-> brain-facing signal
```

这比：

```text
immune variable
-> brain receives same variable
```

多出一个具有独立状态依赖的接口层。

这并不要求把神经 response pattern 升格为语义内容，也不要求把 nodose ganglion 称为一个完整 SRT selector。

---

## 2. Representation geometry：不是新增 SRT 几何 primitive

本 bridge 使用 `response geometry` / `representational geometry` 只描述实验上的多维 response space：amplitude、duration、rise/decay slope、integral 等特征共同决定 cytokine cluster 的可分性。

可以安全地写：

```text
G_response(healthy)
!=
G_response(DSS)
```

但这里的 `G_response` **只是说明性符号，不进入 symbol table，不是 canonical geometry**。

最重要的经验结构是：

```text
same cytokine type
+ different organismal state
-> different effective neural representation
```

这对 SRT 的价值在于反对“固定对象输入 + 后端才解释”的过早对象化模型，而不是把论文写成 `L0` 的经验观测。

### 2.1 强制非同一

```text
neural activity magnitude
!= representational separability

cytokine identity
!= fixed neural label

state-dependent representation
!= L0

nodose representation
!= SRT Selection
```

---

## 3. 历史写回：论文给出的是 persistence pressure，不是 pure-history proof

DSS colitis 不只改变当前 cytokine level，也伴随 vagal-ganglia transcriptomic change 与后续 response profile change。day 14 时症状型 DAI 已接近正常，而 nodose spontaneous-transient amplitude 仍降低；但 colon length 仍缩短。

因此来源支持：

```text
overt symptom recovery
!= sensory-interface recovery
```

以及一个谨慎的 source-informed inference：

```text
past inflammatory course
may leave a persisting interface state
```

但不能升级为：

```text
matched present state
+ different history
-> different representation
```

因为当前 tissue/end-organ state 并未完全匹配。

这与仓库现有 NEURAL25 / history-conditioned control 路线的正确连接方式是：把 Huerta 作为 **matched-present-state experiment 的生理实现动机**，而不是把它登记成已通过 HEF-3 的历史因果证据。

---

## 4. 对旧 `SRT_Neuro_08` 的反向修正压力

`Neuroscience/SRT_Neuro_08_Immune_Dist.md` 仍保留较早的强表达，例如把 inflammation 直接组织成单一 friction / perception-down 方向。这篇来源要求以后 owner realignment 时至少守住：

```text
inflammatory state
!= one global neural gain scalar

more inflammation
!= globally more neural activity
!= globally less neural activity

inflammation
!= canonical Psi_f
```

Huerta 的数据本身就是多方向的：baseline-active cell count 上升、calcium amplitude 下降、TNF/IL-10 与 IL-1β 的改变不同、cluster separability 整体下降。

因此未来更安全的 owner-level 原生句应类似：

> inflammatory state can reshape channel-specific sensory excitability and the separability of body-state representations before central processing; any mapping from such changes to canonical `Psi_f`, perception or selection must be separately typed and tested.

**本 PR 不直接改 `SRT_Neuro_08_Immune_Dist.md`。** 当前 neuroscience synthesis / owner construction 受 `Operations/SRT_SYNTHESIS_TARGET_FREEZE_2026-08-16.md` 约束；这里只登记 bounded realignment pressure，等待具名重开条件。

---

## 5. Huerta × Mizrachi：真正重要的是闭环会改写下一轮闭环

Mizrachi 2026 提供：

```text
voluntary attentional allocation
-> altered later inflammatory trajectory
```

Huerta 2025 提供：

```text
bodily / inflammatory state
-> altered peripheral neural representation
```

两者合并成一个非 canonical 的组织框架：

```text
B_t -> R_t -> C_t -> B_(t+1) -> R_(t+1)
```

其中：

```text
B = bodily / immune state
R = peripheral representation
C = central weighting / control
```

关键不是简单 bidirectionality，而是：

```text
R_(t+1) need not equal R_t
```

因为 bodily history/state 可以改变以后感知身体的接口。

这可以作为：

```text
Operation -> Structure -> Modified Operation
```

的神经免疫 P3 realization candidate，但不证明这些环节都满足 SRT Selection-event gates。

---

## 6. Candidate formation：在菜单之前还有接口塑形

一个过晚的模型会把系统面对的候选写成：

```text
{IL-1β, TNF, IL-10}
-> downstream system chooses interpretation
```

Huerta 的结果提醒我们：对 organism 来说，进入 downstream control 的并不是带标签的 cytokine object，而是被当前 sensory apparatus 转换后的 activity structure。

更安全的 SRT-side bridge 是：

```text
bodily difference
x current interface state/history
-> effective distinction available downstream
```

因此这篇材料适合作为：

```text
pre-selection representational shaping / candidate-forming substrate
```

的 bounded example，而不是：

```text
nodose ganglion performs full SRT Selection
```

---

## 7. P4 discriminating program

### P4-VAGAL-H1 — matched present / different history

建立两组：never-inflamed control 与 recovered-from-colitis。尽可能匹配当前：

- serum / colon cytokines；
- colon histology / length；
- body weight / disease score；
- autonomic / metabolic baseline。

然后给予相同 cytokine probe，比较：

- baseline activity；
- evoked amplitude / duration / slopes；
- cluster separability；
- downstream NTS response；
- transcriptomic / receptor state。

候选问题：

```text
matched current state
+ different history
-> persistent difference in sensory response geometry ?
```

这只是 **history-sensitive discriminator**，不是 SRT 独有结果；`M_AIF-history` 等 rival 必须允许正常的 temporal depth / transition learning。

### P4-VAGAL-H2 — matched exposure / different bearer consequence

匹配 acute signal magnitude、duration、immediate physiological burden 与主要感知强度，但让历史 episode 对同一 organism 的未来能力后果不同：

```text
resettable low-stake consequence
vs
same-bearer future-capacity-reducing consequence
```

恢复后比较：

- reweighting / response threshold；
- cytokine separability；
- hysteresis；
- recovery cost；
- future control recruitment。

真正的 D-track 问题不是“history matters”，而是：

> bearer-specific future consequence structure 是否在 ordinary history/precision/preference variables 匹配后仍有独立预测或干预价值？

### P4-VAGAL-H3 — consequence relocation

在信号与即时损失匹配时，改变后果是否真正回到同一 organism，或是否被外部机制吸收/替代。测试未来 sensory/control interface 是否随 consequence-return structure 改变。

此设计目前只是 SRT-side candidate。没有实验结果，不得写成 bearer theorem。

---

## 8. Frozen comparator rule

后续 D-track 至少比较：

```text
M_AIF-base
M_AIF-history
M_SRT-bridge
```

并在数据前冻结：

- information budget；
- temporal horizon；
- refit budget；
- current-state covariates；
- evaluation vector；
- symmetric failure criteria。

### 对 SRT 不利、必须接受

如果 richer ordinary history / active-inference model 在同等复杂度与拟合预算下能解释：

- history effect；
- separability change；
- hysteresis；
- recovery；
- future capacity contraction；

且加入 bearer-specific consequence return / future-selectability term 没有产生新的 prospective prediction、intervention 或 counterfactual gain，则该接口对该目标应判 implementation-substitutable / target-relative dispensable。

### 对 SRT 有利但仍不升级 canonical

只有当匹配并冻结后的 rivals 稳定遗漏 bearer relocation、future-capacity consequence 或 matched-endpoint history差异，而显式加入这些结构后带来 out-of-sample / intervention gain，才可记录一个 P4 `N1 current target-relative indispensable candidate`。这仍不是 `d` / `Psi_f` 的 canonical proof。

---

## 9. 不得写入的等式与强命题

```text
immune system = SRT selection operator
nodose ganglion = bearer
nodose ganglion = subject
cytokine code = L0 -> L1 mapping
state-dependent response = L0 evidence
inflammation = Psi_f
more neural activity = more information
less neural activity = less information
colitis persistence = historical efficacy proved
history effect = SRT unique prediction
this paper proves SRT
```

也不从该来源新增 scalar、operator、threshold 或 NEURAL claim number。

---

## 10. 最小保留结论

1. **值得吸收**：外周 nodose ganglion 已形成 cytokine-specific dynamic representation，不是透明 relay。
2. **最重要的 correction**：inflammatory state 改变的是多维 response/separability 结构，不是一个全局 activity/perception scalar。
3. **最重要的 history pressure**：symptom recovery 与 sensory-interface recovery 可以解离，但 pure-history effect 尚未建立。
4. **最有信息量的下一步**：matched-present/different-history，随后才是 matched-exposure/different bearer consequence；后者必须冻结 richer rivals。
5. **canonical edits**：none。
6. **owner realignment**：pending synthesis-freeze reactivation；先通过 hook 留痕。