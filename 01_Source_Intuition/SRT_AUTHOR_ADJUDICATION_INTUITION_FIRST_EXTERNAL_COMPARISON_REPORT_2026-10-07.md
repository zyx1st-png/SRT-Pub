---
id: SRT-AUTHOR-ADJUDICATION-INTUITION-FIRST-EXTERNAL-COMPARISON-REPORT-20261007
type: author_adjudication
status: active
canonical: false
layer: source_intuition
epistemic_layer: source
claim_mode: author_adjudication
created: 2026-10-07
updated: 2026-10-07
research_mode: U
priority: governance_correction
dependency:
  - AGENTS.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_LOCAL_NO_GAIN_REMOTE_CONVERGENCE_2026-09-29.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CONTINUE_DIRECTIONAL_ACCEPTANCE_2026-09-24.md
related:
  - 01_Source_Intuition/SRT_DIALOGUE_DERIVATION_TRACE_EMPTY_BRAIN_MEMORY_INFORMATION_REPRESENTATION_BEARER_2026-10-07.md
  - Operations/Audits/SRT_EMPTY_BRAIN_MEMORY_INFORMATION_REPRESENTATION_BEARER_CONSISTENCY_PRESSURE_REVIEW_2026-10-07.md
tags: [AuthorAdjudication, Governance, AuthorIntuition, Neighbor, ExternalComparison, OutputFormat]
---

# Author adjudication — intuition-first work with a default three-item external-comparison report

> **Role:** preserve the 2026-10-07 author decision on how AI should present external comparison during SRT theory work, and own the default author-facing output block routed from `AGENTS.md`.
>
> **Boundary:** this is a noncanonical author / governance source. It changes the default **presentation** of external comparison to the author. It does not change any theory definition, does not remove an existing gate, and does not establish that any SRT claim is new, correct or superior.

## A0-Q — direct author wording

> 「我觉得我的理论体系已经相对比较完整，所以不是特别想去接受其他学者的内容。保持原始的直觉。」

> 「你说的3个方法可以写到默认的AI输出内容里吗？」

## A0-S — machine proposal accepted by the second statement

The author's second statement accepted the following machine proposal from the same session as the default AI output:

> 「你继续只做直觉推演，不读文献；对照工作全交给 AI 评审，并且限定它只报告三件事：
> 1. 你的哪句话与已确立的实验事实冲突；
> 2. 你的哪两句话互相矛盾，包括别人的反例揭示出来的矛盾；
> 3. 哪个说法别人已经提出过，只给一行出处，用来判断这是不是新贡献。
>
> 评审不引入对方的术语和框架。」

## 1. Default output rule

**Scope.** SRT theory dialogue, ontology / Constitution / GRG derivation, domain reconstruction, dialogue-trace writeback, and author-facing review of such work. Ordinary Git, tooling, typo, formatting or status-maintenance tasks are out of scope.

**Default.** Each substantive author-facing response in scope ends with this block:

~~~text
外部对照三项
1. 事实冲突：作者的哪句话与已确立的实验 / 观测结果冲突
   —— 引作者原句 + 冲突的结果 + 一行出处
2. 内部矛盾：作者的哪两句话互相矛盾（包括外部反例揭示的矛盾）
   —— 用作者自己的词表述矛盾本身
3. 已有说法：哪个说法他人已提出
   —— 一行出处 + 注明「完全相同」或「部分重合」；只用于判断是否为新贡献
~~~

Write `无` for an item with no finding. Write `未核` for an item the AI could not actually check in this response; do not present an unchecked item as `无`.

**Constraints.**

- **Report, not adoption.** The block does not rewrite the author's wording, import a neighbor's terminology or framework into the author's formulation, or decide keep / drop. The author adjudicates.
- **Item 1 is restricted to established empirical / observational results.** Disagreement with another scholar's theory or interpretation is not a fact conflict. It belongs in item 3 when it is a prior formulation, or in item 2 only when it exposes a contradiction between the author's own statements.
- **Keep it short.** At most a few lines per finding; long neighbor analysis belongs in an audit file, not in the author-facing block.
- **Accuracy over completeness.** Sources named in the block must be ones the AI can actually identify; uncertain metadata is marked as uncertain rather than presented as checked.

## 2. What this does not change

The existing `AGENTS.md §Constitution / Ontology Dialogue Hard Guard` remains in force, including U/N-mode, mature-neighbor adaptation before hardening, internal red-team, the author's second adjudication of substantive meaning changes, the local no-gain rule, the same-target comparison rule, Pipeline 1 source discipline and canonical edit gates.

In particular:

~~~text
three-item block
= default author-facing presentation of external comparison;

three-item block
!= removal of mature-neighbor adaptation;
!= permission to harden a claim that has an open item-1 conflict;
!= author acceptance of any neighbor framework.
~~~

When an audit or workflow requires fuller neighbor analysis, it may still be recorded in the relevant audit file. If that analysis would change, narrow or defeat the author's wording, it is still returned for the author's second adjudication, surfaced through item 1 or item 2 and marked `需作者裁决`.

## 3. Recorded but not decided

The author's preference not to take in other scholars' content and to keep the original intuition is recorded here as a working preference for how the author engages with external material.

Whether to further downgrade or retire the repository's mature-neighbor adaptation rules is **not decided** by this record and requires a separate explicit author decision.
