---
id: SRC-2026-07-16-SEMANTICS-SIMONELLI-IMPLICATION-SPACE
type: material_source_card
status: active_v2_fulltext
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
source_id: SRC-2026-07-16-SEMANTICS-SIMONELLI-IMPLICATION-SPACE
title: "Implication Space Semantics as Bilateral Incompatibility Semantics"
source_type: forthcoming_topoi_penultimate_draft_full_text
source_kind: primary_full_text_formal_semantics_argument
domain: Philosophy of Language / Inferentialism / Formal Semantics / Substructural Logic
url: https://philpapers.org/rec/SIMISS?ref=mail
doi: null
authors:
  - Ryan Simonelli
publication: "Topoi"
date_published: forthcoming
draft_date: 2026-04-10
date_added: 2026-07-16
full_text_received: 2026-07-16
access_status: full_text_user_supplied_penultimate_draft_not_copy_of_record
reading_level: full_close_read
evidence_level: primary_full_text_penultimate_draft
reliability_level: high_for_presented_definitions_and_argument_medium_for_final_publication_metadata_and_external_SRT_projection
srt_relevance: very_high
integration_priority: high
pipeline_decision: A
patch_id: SRT-PH-SEM01-BILATERAL-INCOMPATIBILITY-CONTEXT-REPAIR
related_srt_claims:
  - _SRT_DIRECTION3_CHOICEMAP_PROTOTYPE_SEED.md option differentiation and convergence boundary
  - Core_Law/SRT_Occlusion_Dynamics.md denial and pathological closure
  - _SRT_OBJECTHOOD_AS_RESELECTABILITY_META_STANDARD.md closure and reopening
  - Core/SRT_Core_21b_Constitutive_Theorems.md real choice moment
  - Philosophy semantics / commitment / exclusion bridge
tags: [inferentialism, bilateralism, assertion, denial, incompatibility, implication-space, semantics, defeasibility, substructural-logic, context-repair]
---

# SourceCard: Ryan Simonelli — *Implication Space Semantics as Bilateral Incompatibility Semantics*

## 1. 一句话结论

该文最稳健的贡献不是证明“意义或选择等于排除”，而是把 Kaplan 难以直观理解的 implication-space semantics 重释为一种**双边、不要求持久性的立场语义学**：语义基本单位是由断言与否认组成的 position；一个 position 的语义值首先由其与哪些 positions 发生 incoherence / clash 来刻画；而允许 persistence 失败，使新增例外信息能够解除先前的材料不相容。

对 SRT 最有价值的增量是三分：

```text
positive commitment
!=
negative exclusion
!=
context-sensitive repair
```

同时，作者在结论中主动强调：**incompatibility 只是 inferential articulation 的一个维度，不能把 committive consequence 全部还原为 incoherence。** 因此 SRT 可以借此建立 ChoiceMap 的“双边承诺—可修复冲突”层，却不能把选择整体定义成不相容关系。

## 2. 访问与精读状态

- 已取得并精读用户上传的 40 页 penultimate draft，日期为 2026-04-10。
- 文档明确要求最终引用 *Topoi* 正式版本；当前未在公开检索中确认最终 DOI，因此本卡保留 `doi: null`。
- 已核验导论、Kaplan / Brandom / Hlobil 背景、Ketonen sequent calculus、bilateral reading、positions / incoherence profiles、incompatibility entailment、semantic clauses、soundness / completeness 说明、结论中的自我限制及附录对 Hlobil-style semantic values 的修正。
- 论文是形式语义学和哲学解释论文，不是选择、主体、对象或社会制度的经验理论。
- 下文 SRT 形式桥均为 P3/P4 侧的受限移植，不是 Simonelli 的本体论主张。

## 3. 论文试图解决什么问题

### 3.1 Brandom 早期 incompatibility semantics 的 persistence 问题

Brandom 早期方案用“一个句子与哪些句子不相容”刻画内容，但默认：

```text
若 Γ 不相容，
则任何包含 Γ 的更大位置仍不相容。
```

即 persistence / monotonicity。

材料推理并不总满足这一点：

```text
mammal + lays eggs
```

在默认语境中形成 clash；加入：

```text
platypus
```

后，该 clash 可以被解除。

因此，若要同时容纳严格逻辑关系和可撤销的材料推理，不能在底层强制 Weakening / persistence。

### 3.2 Kaplan 框架的数学成功与直觉不透明

Kaplan 的 implication-space semantics 能对接 Ketonen 多结论 sequent calculus，并容纳 radically substructural material inference；但它把 candidate implications 当作语义点，并对“subjunctive robustness range”反复施加运算，概念上非常难读。

Simonelli 的任务不是重新证明 Kaplan 的全部结果，而是给这些对象一个更清楚的哲学解释。

### 3.3 双边重释

Restall-style bilateral reading 把：

```text
X ⊢ Y
```

解释为：

> 同时断言 X 中全部内容并否认 Y 中全部内容，会形成 incoherent / out-of-bounds / clash position。

由此，candidate implication 不再被理解为奇怪的“多结论蕴含对象”，而被理解为一个可能占据的 position。

## 4. 正式框架

### 4.1 Moves

对语言 `L`：

\[
L^{\pm}=\{+A\mid A\in L\}\cup\{-A\mid A\in L\}
\]

- `+A`：断言 A；
- `-A`：否认 A。

断言与否认是两种基础 move，不应预先压成同一种命题态度。

### 4.2 Positions

\[
P=\mathcal P(L^{\pm})
\]

position 是 moves 的任意集合。

- 最小 position：`e = ∅`；
- 最大 position：`⋆ = L±`；
- position 可以不完整，不要求对每个命题都断言或否认；
- 框架允许讨论局部、开放、尚未闭合的立场。

### 4.3 Incoherent positions

有一个被区分出的集合：

\[
I\subseteq P
\]

最低约束包括：

- 空 position 是 coherent；
- 最大 position 是 incoherent；
- 对任一原子句 `p`，同时包含 `+p` 和 `-p` 的 position 属于 `I`。

此外，可将材料性 clash 放入 `I`，例如：

```text
+red(a), +green(a)
+red(a), -colored(a)
```

关键是：作者允许 persistence 失败，因此：

\[
\Gamma\in I \not\Rightarrow \Delta\in I
\quad\text{even when}\quad \Gamma\subseteq\Delta
\]

这不是说严格矛盾会被更多信息“治愈”，而是框架中的 `I` 同时承载形式 incoherence 与 defeasible material clash；后者可以被例外语境修复。

### 4.4 Incoherence profile

对 position `Γ`：

\[
\Gamma^{\perp}=\{\Delta\mid \Gamma\cup\Delta\in I\}
\]

它表示：与 `Γ` 合并后形成 incoherence 的全部 positions。

对 positions 集合 `X`：

\[
X^{\perp}=\{\Gamma\mid \forall\Delta\in X,\;\Gamma\cup\Delta\in I\}
\]

即成员 incoherence profiles 的交集。

### 4.5 Incompatibility entailment

作者定义：

\[
\Delta\vDash_I\Gamma
\quad\text{iff}\quad
\Gamma^{\perp}\subseteq\Delta^{\perp}
\]

直观上：凡与 `Γ` 不相容者，也都与 `Δ` 不相容；因此 `Δ` 在 incompatibility profile 意义上至少与 `Γ` 一样强。

并有：

\[
\Delta\in\Gamma^{\perp\perp}
\quad\text{iff}\quad
\Delta\vDash_I\Gamma
\]

### 4.6 Assertion 与 denial 必须分开

在 persistence 失败时：

\[
\{+A\}^{\perp\perp}
\neq
\{-A\}^{\perp}
\]

所以不能把“断言 A 的双重 profile”直接当作“否认 A 的 profile”。双边性不是装饰，而是 radically substructural 语义的必要维度。

## 5. 全文核验出的非经典性质

### 5.1 Incompatibility entailment 与 ordinary implication 分离

例如：

```text
bird
```

在默认材料推理中可能使主体承诺：

```text
flies
```

但不一定 incompatibility-entail `flies`，因为 `penguin` 与 `flies` clash，却不与 `bird` clash。

甚至严格分类关系也可能分离：

```text
platypus -> mammal
```

是严格承诺，但 `platypus` 未必 incompatibility-entail `mammal`，因为 `lays eggs` 与默认 `mammal` clash，却不与 `platypus` clash。

### 5.2 Containment 可失败

通常会期待：

\[
\Gamma,\varphi\vDash_I\varphi
\]

但在非持久性条件下，这可以失败。加入上下文可能削弱而非增强某个 position 的 incoherence profile。

因此 `⊨I` 不能被无条件当作普通“更强承诺”的偏序。

### 5.3 Semantic values 是 assertion / denial profile 的有序对

对句子 `A`：

\[
\llbracket A\rrbracket
=
\langle\llbracket +A\rrbracket,\llbracket -A\rrbracket\rangle
\]

原子句：

\[
\llbracket p\rrbracket
=
\langle\{+p\}^{\perp},\{-p\}^{\perp}\rangle
\]

否定交换两侧：

\[
\llbracket\neg A\rrbracket
=
\langle\llbracket-A\rrbracket,\llbracket+A\rrbracket\rangle
\]

作者再通过 `⊥`、交集以及 pairwise-union 运算 `⋓` 给出合取、析取和条件句的 compositional clauses。

### 5.4 Soundness / completeness 的准确范围

Kaplan 的主要结果是：给定原子层 base consequence relation / incoherent positions，这套 semantics 对 Ketonen classical sequent calculus 生成的扩展是 sound and complete：

\[
X\vdash_B Y
\quad\text{iff}\quad
X\vDash_B Y
\]

这说明形式对应成立，不说明：

- 自然语言的全部意义已被捕获；
- `I` 的材料内容来源已被解释；
- incompatibility 是推理或意义唯一的基础；
- 该语义证明了任何 SRT 本体论。

## 6. 作者在结论中的关键自我限制

这是全文相对于摘要最重要的新增信息。

Simonelli 明确指出：

> implication 一般不能被完全还原为 incoherence。

其例子是：

- `red + square` 使主体承诺否认 `blue`；
- `blue + square` 使主体承诺否认 `red`；
- 但 `red + blue` 并不因此使主体承诺否认 `square`。

若只把三者共同出现的 incoherence 当作基础，就无法区分哪一项是应被否认的结论。

因此作者主张更自然的方向是：

```text
incoherence
and
committive consequence
```

应作为同样基础、不可相互还原的两个维度。

这直接修正了摘要预审卡中“选择 = 承担 + 排除”的潜在过强读法：

```text
exclusion structure
!=
positive consequence structure
```

## 7. 附录的技术增量

Hlobil / Brandom 版本把 semantic value 从 positions 集合提升为“具有相同 incoherence profile 的 positions 集合之等价类”，即 sets of sets of positions。

Simonelli 指出：

- 该版本的 adjunction / symjunction 原定义仍依赖代表元，严格说没有直接定义为 roles 这些 set-theoretic objects 上的运算；
- 可以通过任取 role 成员，或使用最大成员 `X⊥⊥` 等方式修正，使 clauses 真正满足 compositionality；
- 修正后 Hlobil 版本可理解，但认知负担极高；
- Kaplan 的直接 incoherence-profile semantic values 更适合解释核心哲学结构。

该附录提高了论文的形式可靠性，但对 SRT 的主要价值仍是“可读的双边位置 + 可撤销材料不相容”，而不是 higher-order role construction。

## 8. 对 SRT 的直接增量

### 8.1 选择结果应被记录为 position，而非标签

局部决策输出不应只有：

```text
selected_option = A
```

还应记录：

```text
asserted commitments
explicit denials
left-open questions
current incompatibilities
bases of those incompatibilities
```

这能区分：

- 选择 A 但不否认 B；
- 选择 A 并明确拒绝 B；
- 当前暂不选择 B，但保留未来进入；
- 将 B 定义为原则上不可接受。

### 8.2 不相容必须区分 strict 与 defeasible

SRT / ChoiceMap 应至少区分：

- `Inc_strict`：逻辑、物理或定义上不能共存；
- `Inc_def`：在当前默认、制度或叙事背景下发生 clash，但存在例外或补充语境；
- `Inc_script`：主要由当前 L2 脚本制造的表面不相容。

否则“加入例外信息解除 clash”会被误读为逻辑矛盾可以随意消失。

### 8.3 可再选择性不仅是撤回，也可以是 context repair

论文最有潜力的 SRT 接口是：

```text
apparent conflict
+ exception / boundary / role distinction / temporal decomposition
-> repaired coexistence
```

重开选择空间不一定要求删除原承诺；有时可通过增加区分，使原本被当成不可共存的路径获得部分共存。

### 8.4 排除结构不能独自定义选择

作者自己的结论要求 SRT 保留：

```text
positive commitment / consequence
!=
negative incompatibility / exclusion
```

选择还需要：

- 执行者或 bearer；
- 方向实际化；
- 代价与后果回流；
- 时间、历史与不可逆写入；
- 后续承诺怎样生成，而不只是哪些组合被禁止。

## 9. ChoiceMap 可操作化

每个 option 可增加：

```yaml
option:
  assertions: []
  denials: []
  left_open: []
  incompatibilities:
    - target:
      type: strict | defeasible | script_generated
      basis:
      exception_or_repair_context:
  consequences:
  bearer:
  revision_conditions:
```

新增五项审计：

1. **bilateral audit**：选择它实际肯定什么、否认什么？
2. **forced-denial audit**：系统是否把“不选择”误写成“否认”？
3. **persistence audit**：该冲突在加入例外信息后是否仍成立？
4. **repair audit**：时间分层、模块化、边界调整或角色区分能否解除 clash？
5. **irreducibility audit**：即使没有显式 incompatibility，是否仍存在正向承诺关系？

## 10. 与遮蔽动力学的候选接口

病态 L2 可被进一步诊断为：

```text
将 defeasible clash 升格为 strict impossibility
+ 隐藏例外信息
+ 把未断言误写为否认
+ 撤销被排除者提出 repair context 的 standing
+ 让 incompatibility rule 本身不可审计
```

这只是 `Core_Law/SRT_Occlusion_Dynamics.md` 的未来 integration hook，不直接修改其 canonical 动力学。

## 11. SRT 候选形式桥

设位置：

\[
\Pi=\langle A_\Pi,D_\Pi,O_\Pi,C_\Pi\rangle
\]

其中：

- `A_Π`：已断言承诺；
- `D_Π`：已明确否认；
- `O_Π`：仍保持开放；
- `C_Π`：当前语境 / 边界 / 时间尺度。

设 defeasible incoherence 集为 `I_def`，则可定义候选 repair set：

\[
\operatorname{Repair}(\Gamma)
=
\{E\mid \Gamma\in I_{def},\;\Gamma\cup E\notin I_{def}\}
\]

这只表示：某些语境补充可解除材料 clash。它不适用于逻辑矛盾或已证实的物理不可能。

## 12. 主要压力与失败条件

1. **`I` 的来源仍被当作基础输入。**  
   框架能组合 material incoherence，却没有单独解释谁决定哪些组合属于 `I`、如何学习、争议或修订。

2. **incoherence / clash 的强度不统一。**  
   严格矛盾、默认异常、规范紧张和需要解释的反常组合都可能被放进同一 `I`；SRT 移植必须分型。

3. **非持久性不能无条件外推到现实。**  
   增加“platypus”可解除默认材料 clash，不意味着增加叙事总能解除物理冲突或伦理伤害。

4. **position 不是主体。**  
   它没有 bearer continuity、stake、代价、记忆、行动控制或责任门。

5. **静态 profile 不等于动态选择。**  
   框架主要刻画位置关系，未刻画从一个 position 到另一个 position 的转换支付、时间和不可逆性。

6. **incompatibility entailment 不等于 ordinary consequence。**  
   Containment 可以失败；不能用其大小直接当“更强承诺”或价值排序。

7. **sentential scope 有限。**  
   论文主要处理句子层 vocabulary；subsentential 扩展仍是未来工作。

8. **形式完备性是相对的。**  
   soundness / completeness 相对于给定 base 与 calculus，不是自然语言或现实选择模型的完备性。

## 13. Pipeline 1 裁决

**A — 直接融入 philosophy / ChoiceMap bridge。**

理由：

- 已取得完整 penultimate draft；
- 核心 definitions、semantic clauses、non-persistence、incompatibility entailment 和结论限制均已核验；
- 能形成不依赖 SRT 术语的 surviving claims；
- 对 ChoiceMap 的假两难识别、显式否认与 context repair 有明确操作增量；
- 作者自身对 incompatibility reduction 的否定提供了重要反过度简化守门。

融入层级：P3/P4 bridge；不修改 SRT canonical selection、`d-value`、`Psi_f`、`T_dir` 或对象定义。

## 14. 建议落点

1. `Philosophy/patches/SRT_Philosophy_PH_SEM01_Bilateral_Incompatibility_Context_Repair_v0_1.md`；
2. `Philosophy/hooks/PH_SEM01_Bilateral_Incompatibility_Integration_Hook.md`；
3. ChoiceMap：assertions / denials / left-open / strict-vs-defeasible / repair-context schema；
4. `Core_Law/SRT_Occlusion_Dynamics.md`：未来增加“defeasible clash 被制度化为 strict impossibility”的桥接注释；
5. `_SRT_OBJECTHOOD_AS_RESELECTABILITY_META_STANDARD.md`：未来增加 context repair 与重组式 reopening。

## 15. Surviving claims

1. 一个 discursive position 可由断言与否认两类 moves 共同构成，且可保持不完整。
2. 一个 position 的 inferential significance 可通过其 incoherence profile 部分刻画。
3. defeasible material incompatibility 不满足 persistence；加入例外信息可以恢复 coherence。
4. assertion 与 denial 在非持久性框架中不可互相消去。
5. incompatibility entailment 与普通 implication / committive consequence 可以分离。
6. incompatibility 不能单独穷尽 inferential articulation。
7. SRT 可以借此建立双边承诺和 context-repair 工具层，但不能把语义不相容升级为本体不可能、stake 或选择本身。
