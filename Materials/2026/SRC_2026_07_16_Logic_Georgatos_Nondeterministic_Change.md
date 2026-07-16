---
id: SRC-2026-07-16-LOGIC-GEORGATOS-NONDETERMINISTIC-CHANGE
type: material_source_card
status: active_v1
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
source_id: SRC-2026-07-16-LOGIC-GEORGATOS-NONDETERMINISTIC-CHANGE
title: "Conditional Logics of Nondeterministic Change"
source_type: peer_reviewed_conference_chapter_abstract
source_kind: primary_bibliographic_record_plus_author_abstract
domain: Formal Logic / Reasoning Under Uncertainty / Dynamic Semantics
url: https://philpapers.org/rec/GEOCLO?ref=mail
doi: null
authors:
  - Konstantinos Georgatos
publication: "In Kai Sauerwald & Matthias Thimm (eds.), Symbolic and Quantitative Approaches to Reasoning with Uncertainty, ECSQARU 2025. Springer, Lecture Notes in Computer Science, pp. 316–330"
date_published: 2025
date_added: 2026-07-16
access_status: abstract_and_bibliographic_metadata_only_target_full_text_not_retrieved
reading_level: abstract_constrained_formal_reconstruction
evidence_level: peer_reviewed_conference_chapter_abstract
reliability_level: high_for_metadata_and_stated_results_medium_low_for_unseen_formal_details
srt_relevance: very_high
integration_priority: very_high
pipeline_decision: B1
recheck_date: 2026-10-16
related_srt_claims:
  - Core_Law/SRT_L0_Metaphysics.md accessible possibility and manifestation
  - Core/SRT_Core_21b_Constitutive_Theorems.md real choice moment
  - Core/SRT_Core_22_Equations.md transition and update interfaces
  - Core_Law/SRT_Irreversibility.md write / history asymmetry
  - _SRT_OBJECTHOOD_AS_RESELECTABILITY_META_STANDARD.md future path preservation
tags: [conditional-logic, nondeterminism, branching-time, update, completeness, axiomatization, change]
---

# SourceCard: Konstantinos Georgatos — *Conditional Logics of Nondeterministic Change*

## 1. 一句话结论

该文把条件句从静态世界间真假关系改写为非确定变化的描述符，并在“过去线性、未来分叉”的树序上分别构造前向、前后向及其对偶更新算子，同时给出公理化与完备性结果；对 SRT 的最大价值是提供一种可审计的形式语言，用来区分未来可达分支、实际变化、反向路径条件与当前状态的生成历史。

## 2. 访问与精读状态

- 已核验：完整书目信息、页码、会议/丛书载体和作者摘要。
- 未获得：14 页正文、符号定义、语义条款、具体公理、模型类与完备性证明。
- 本卡只重建摘要明确承诺的形式架构，不复原未见公式。
- 在取得全文前，不得把本卡中的 SRT 形式桥写入 Core equations。

## 3. 摘要明示的形式贡献

1. 条件陈述被理解为 change descriptors。
2. 基础模型是标准的 nondeterministic framework。
3. 时间/状态结构采用树序：过去线性，未来本质上不确定并分叉。
4. 第一类系统包含纯前向条件算子。
5. 第二类系统组合后向与前向条件算子。
6. 两类系统均给出公理化并证明完备性。
7. 还为这些条件算子的对偶构造类似结果。
8. 对偶算子自然地表示 update operators，因为它们描述导致当前状态的变换。

## 4. 需要严格区分的四个形式对象

### 4.1 状态树

一个节点代表状态或时刻，偏序表示历史可达性。线性过去意味着每个当前节点有单一实际祖先链；分叉未来意味着存在多个尚未被排除的延续。

### 4.2 前向条件

大意是描述：从当前状态出发，在满足某条件的后续变化中，什么结果成立。具体量化方式必须等待正文，不可预设是全称、存在、最小变化或选择函数语义。

### 4.3 后向条件

描述当前状态相对于此前变化的条件结构，使逻辑能够表达“当前是如何由某类变化来到的”。

### 4.4 对偶更新算子

摘要称其自然表示 update operators，并通过导致当前状态的 transformations 来细化。需要全文核验：

- 对偶是经典否定下的 modal dual，还是另有定义；
- update 是前向改变信息状态，还是反向刻画生成路径；
- 是否允许多条不同历史导向同一状态。

## 5. 对 SRT 的核心形式价值

### 5.1 将“选择”拆为三个不同操作

SRT 不应把以下三者压成一个 `Select()`：

1. **branch availability**：哪些未来仍可达；
2. **transition realization**：哪条变化实际发生；
3. **history inscription**：当前状态携带怎样的生成路径。

该文的前向、后向与 update 结构可帮助建立三层语法。

### 5.2 形式化“不可逆不是未来无分支”

线性过去与分叉未来提示：

- 不可逆性首先意味着实际历史不能被重写为另一条已发生历史；
- 它不意味着未来只剩一条路；
- 选择可能关闭部分未来，但健康闭包仍保留可再选择分支；
- pathological closure 可被描述为未来可达子树持续收缩，而非仅仅当前状态变差。

### 5.3 为 reselectability 提供可达性接口

可再选择性不应简化为选项数量。形式上至少需要：

- 可达分支是否真实；
- 进入分支的转换成本；
- 被关闭路径是否可在可支付代价下重开；
- 不同分支是否只是标签不同而状态同构；
- 当前行动是否改变未来树本身。

## 6. SRT 候选形式桥

仅作 P3 研究草图：

设 `(W, \preceq)` 是树序，`w \preceq v` 表示 `v` 是 `w` 的可能延续。

\[
\mathsf{Avail}(w)=\{v\mid w\preceq v\}
\]

\[
\mathsf{Realize}(w,a)=w'
\]

\[
\mathsf{Hist}(w')=\langle w_0,\ldots,w'\rangle
\]

SRT 的选择事件至少应同时报告：

```text
pre-choice reachable set
actual transition
post-choice reachable set
history writeback
reopening cost
```

该草图不是 Georgatos 的原始系统，也不能在未读正文时声称其公理满足 SRT 的非自我抹除条件。

## 7. 对 `L0 / L1 / L2` 的安全映射

| 逻辑结构 | SRT 候选接口 | 限制 |
|---|---|---|
| 分叉未来 | 局部可访问 `L0` | 不等于总 L0，本体层不可由树模型穷尽 |
| 实际节点迁移 | `L1` transition / manifestation | 逻辑可达不等于现实锚定 |
| 线性实际过去 | `L2` 历史记录接口 | L2 还含共享脚手架、制度与模型约束 |
| 后向算子 | 当前状态的生成条件 | 不保证唯一因果解释 |
| update 对偶 | 状态变化/历史重建接口 | 不自动包含 `Ψ_f` 或 stake |
| 完备性 | 形式系统相对模型类的充分性 | 不等于 SRT 本体论完备 |

## 8. 可形成的研究任务

### 8.1 Branch Restriction Audit

对每次选择记录：

- 被排除分支；
- 暂时不可达分支；
- 永久不可达分支；
- 通过何种代价可重开；
- 哪些受影响者拥有不同的未来树。

### 8.2 Forward / Backward Consistency Test

在 ChoiceMap 或模拟中检查：

- 前向预测的后果是否与事后可重建路径一致；
- 是否存在“事后叙事”把未曾可达的路径伪装成当时可选；
- 当前解释是否遗漏关键转换。

### 8.3 Occlusion Dynamics

把 pathological L2 表述为：

```text
apparent local stability increases
while effective reachable subtree shrinks
and reopening cost grows
```

这可与现有 `reselection capacity loss` 连接，但需另行定义权重、成本和 bearer。

## 9. 对文章的主要压力

1. **树结构是否过强。** 现实系统可能有合并历史、循环、并发、部分序和不可区分路径，不一定拥有单一线性过去。
2. **逻辑 update 不等于物理变化。** 条件语义可能描述信息更新，而非现实生成。
3. **完备性只相对于给定模型类。** 不能从形式完备性推出世界具有该结构。
4. **条件句与选择仍有距离。** 描述变化不等于执行或承担变化。
5. **没有 stake、cost 和 bearer。** 形式分支本身无法区分高代价选择与无关状态变化。

## 10. Pipeline 1 裁决

**B1**

这是七项中最有希望转化为 SRT 形式补丁的材料，但必须先取得全文并核验：

- 语法和语义；
- 树序条件；
- 前向/后向算子；
- 对偶定义；
- 公理系统；
- 完备性证明的模型假设。

未完成前不进入 `Core/SRT_Core_22_Equations.md`。

## 11. 建议落点

1. `Core_Law/patches/` 或 `Philosophy/patches/`：branch/update/history formal interface；
2. `Core/SRT_OPEN_TENSIONS.md`：可再选择性与动态闭包的形式候选；
3. ChoiceMap 实验：记录 pre/post reachable option graph；
4. `Core_Law/SRT_Irreversibility.md`：仅在全文核验后讨论线性过去与写入不对称。

## 12. Surviving claims

1. 条件逻辑可以把条件句解释为非确定变化描述，而非仅静态真假关系。
2. 前向、后向和更新算子可分别描述未来分支、生成条件和状态转换。
3. SRT 应区分可达分支、实际转换和历史写入。
4. 线性过去/分叉未来是有用模型，但不是 SRT 世界结构的既定事实。
5. 形式完备性不能被写成对 SRT 的经验或本体论验证。

## 13. 待全文核验清单

- 模型 frame 的精确定义；
- 过去线性的公理条件；
- 是否允许 future reconvergence；
- 条件算子的真值条款；
- 前向和后向系统的公理；
- 对偶 update 的定义；
- soundness / completeness 证明范围；
- 示例是否涉及因果、行动或仅信息变化；
- 与 dynamic logic、branching-time logic、belief update 的差异。
