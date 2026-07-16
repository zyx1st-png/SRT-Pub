---
id: SRC-2026-07-16-SEMANTICS-SIMONELLI-IMPLICATION-SPACE
type: material_source_card
status: active_v1
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
source_id: SRC-2026-07-16-SEMANTICS-SIMONELLI-IMPLICATION-SPACE
title: "Implication Space Semantics as Bilateral Incompatibility Semantics"
source_type: forthcoming_journal_article_abstract
source_kind: primary_bibliographic_record_plus_author_abstract
domain: Philosophy of Language / Inferentialism / Formal Semantics
url: https://philpapers.org/rec/SIMISS?ref=mail
doi: null
authors:
  - Ryan Simonelli
publication: "Topoi"
date_published: forthcoming
date_added: 2026-07-16
access_status: abstract_only_target_full_text_not_retrieved
reading_level: abstract_constrained_argument_reconstruction
evidence_level: primary_author_abstract_forthcoming
reliability_level: high_for_metadata_and_stated_thesis_low_for_unseen_semantic_clauses
srt_relevance: very_high
integration_priority: high
pipeline_decision: B1
recheck_date: 2026-10-16
related_srt_claims:
  - Core_Law/SRT_L0_Metaphysics.md differentiation and manifestation
  - Core/SRT_Core_21b_Constitutive_Theorems.md real choice moment
  - _SRT_OBJECTHOOD_AS_RESELECTABILITY_META_STANDARD.md closure and reopening
  - Core_Law/SRT_Occlusion_Dynamics.md excluded positions and re-entry
  - _SRT_DIRECTION3_CHOICEMAP_PROTOTYPE_SEED.md option differentiation
tags: [inferentialism, bilateralism, assertion, denial, incompatibility, implication-space, semantics]
---

# SourceCard: Ryan Simonelli — *Implication Space Semantics as Bilateral Incompatibility Semantics*

## 1. 一句话结论

该文把难以直观理解的 implication-space semantics 重释为 Brandom incompatibility semantics 的双边继承者：语义首先赋给由断言与否认构成的“立场”，一个立场的语义值是与其不相容的立场集合；其 SRT 价值在于提供一种“通过承担与排除形成确定位置”的语义模型，而不是把选择理解为从中立菜单中取出项目。

## 2. 访问与精读状态

- 已核验：题名、作者、Topoi forthcoming 状态及作者摘要。
- 未获得：正文、Kaplan dissertation 的具体语义条款、Simonelli 的翻译定理与例子。
- 可利用相关公开研究确认 implication-space semantics 是正在扩展的 inferentialist 形式方案，但本卡不把相关论文内容归给 Simonelli。
- 所有 SRT 映射均为桥接解释，不是作者本体论立场。

## 3. 摘要明示的论证结构

1. implication-space semantics 最初由 Daniel Kaplan 博士论文提出。
2. Brandom 称其为 inferentialist semantics 的 “holy grail”。
3. 该框架的正式语义条款很难获得直观解释。
4. Simonelli 提出新解释：它是 Brandom 早期 incompatibility semantics 的 bilateral successor。
5. 语义值首先赋给 positions，而非孤立句子。
6. position 由 assertions 与 denials 组成。
7. 一个 position 的语义值是与其 incompatible 的 positions 集合。
8. 这一解释使原本晦涩的特征可通过 Brandom 已有概念理解，尤其是 incompatibility entailment。

## 4. 四个关键概念

### 4.1 Position

不是单一命题，而是一组主体已承担的肯定和否定。语义单位因此带有承诺结构。

### 4.2 Bilateralism

断言与否认不是将否定符号附加到同一种行为，而是两类基础规范姿态。一个完整立场同时由“承认什么”和“拒绝什么”刻画。

### 4.3 Incompatibility

两个立场不能被共同维持。它不是纯句法矛盾的同义词，可能由材料推理、规范承诺或内容关系产生。

### 4.4 Incompatibility entailment

若所有与某结论不相容的立场也与给定前提立场不相容，则可由不相容结构定义蕴含。具体条款需等待全文核验。

## 5. 对 SRT 的核心增量

### 5.1 选择形成位置，而不只是取值

SRT 可把局部选择事件重写为：

```text
selection
= adoption of a position
+ acceptance of commitments
+ exclusion of incompatible continuations
```

这有助于说明为何选择会产生现实差异：它改变的不只是当前标签，还改变后续哪些位置仍可共同维持。

### 5.2 对象边界可通过不相容结构稳定

一个对象或主体位置可被部分刻画为：

- 哪些属性/行动与其当前闭包兼容；
- 哪些变化会破坏其同一性；
- 哪些被排除位置仍可通过重组重新进入；
- 哪些排除已成为不可申诉的 L2 规则。

这与 reselectability 的关系是：

> 健康对象并非没有排除，而是其排除结构仍保留可审计的重组、申诉和重新开放路径。

### 5.3 为 pathological closure 提供语义接口

致命 L2 可表现为：

- 只允许断言，不允许实质否认；
- 某些位置在进入讨论前就被定义为不相容；
- incompatibility 规则本身不可修订；
- 被排除者无 standing 触发重新评估；
- 制度把局部矛盾扩散成身份层排除。

## 6. 与 ChoiceMap 的接口

ChoiceMap 的选项不能只是名称列表。每个选项应显示：

- 它要求用户承担哪些承诺；
- 它否认或排除哪些其他路径；
- 哪些不相容是真实约束；
- 哪些只是当前叙事制造的伪不相容；
- 能否通过模块化、时间分层或边界调整，使原本冲突的选项部分共存。

可增加输出字段：

```text
Option:
  assertions:
  denials:
  incompatible_with:
  incompatibility_basis:
  reversible_by:
```

这可能显著提高 ChoiceMap 对假两难的识别能力。

## 7. SRT 候选形式桥

设一个位置为：

\[
p = \langle A_p, D_p \rangle
\]

其中 `A_p` 为断言集，`D_p` 为否认集。

设：

\[
\mathsf{Inc}(p)=\{q\mid q \text{ 与 }p\text{ 不相容}\}
\]

SRT 侧可进一步区分：

- `Inc_phys`：物理/资源不相容；
- `Inc_log`：逻辑不相容；
- `Inc_norm`：规则或制度不相容；
- `Inc_id`：身份闭包不相容；
- `Inc_script`：仅由当前 L2 脚本制造的表面不相容。

这不是 Simonelli 的分类，而是 SRT 可操作化建议。

## 8. 该桥接的边界

1. **语义排除不等于本体排除。** 不能从某立场无法共同断言，推出世界中的状态无法共存。
2. **不相容结构不等于选择行为。** 它刻画位置空间，但没有说明谁执行、承担或支付转换。
3. **承诺不等于 stake。** 语言承诺可能没有不可转移后果。
4. **bilateral positions 仍然预设规范实践。** 它不能解释最初的 selectability 或非语言对象如何形成。
5. **集合外延可能隐藏强度与代价。** 两个位置都“不相容”，但转换代价、可恢复性和受影响者可能完全不同。

## 9. SRT 映射表

| 文章概念 | SRT 安全映射 | 禁止越级 |
|---|---|---|
| position | 已承担断言/否认的局部选择位置 | position = 完整主体 |
| bilateral assertion/denial | 选择的正向承诺与排除面 | 所有选择都是语言行为 |
| incompatibility set | 选择后被关闭的共存路径 | 语义不相容 = 物理不可能 |
| incompatibility entailment | 由排除结构定义推理约束 | 推理蕴含 = 因果生成 |
| semantic value | 位置在推理网络中的差异角色 | 语义值 = d-value |
| framework reinterpretation | 形式直觉澄清 | 证明 SRT selection-first ontology |

## 10. Pipeline 1 裁决

**B1**

高潜力形式/语义桥，但需要全文核验后才可：

- 使用具体语义条款；
- 对接 Brandom/Kaplan；
- 创建 ChoiceMap incompatibility layer PatchNote；
- 判断是否有非单调、非传递推理的实质增量。

## 11. 建议落点

1. `Philosophy/patches/`：bilateral position and exclusion structure；
2. ChoiceMap：选项承诺/否认/不相容字段；
3. `Core_Law/SRT_Occlusion_Dynamics.md`：制度化不相容规则的候选诊断；
4. `_SRT_OBJECTHOOD_AS_RESELECTABILITY_META_STANDARD.md`：排除规则可重开性，但仅作研究注释。

## 12. Surviving claims

1. 一个语义位置可由断言和否认共同刻画。
2. 内容可通过它与哪些位置不相容来获得推理角色。
3. 选择研究应记录正向承诺和负向排除，而非只记录结果标签。
4. SRT 可借此审计假两难和不可修订的排除规则。
5. 语义不相容不能直接升级为本体论排除或 stake。

## 13. 待全文核验清单

- Kaplan 原框架的语义对象与条款；
- Simonelli 的 bilateral translation 是否等价；
- position 是否允许不完备或不一致；
- incompatibility 是否对称；
- entailment 的精确定义；
- 非单调和非传递推理如何处理；
- 逻辑联结词的解释；
- 与 Brandom 早期 incompatibility semantics 的差异；
- 是否给出可计算或模型论性质。
