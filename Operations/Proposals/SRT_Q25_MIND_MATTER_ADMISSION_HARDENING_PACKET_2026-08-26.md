---
id: SRT-OPS-PROPOSAL-Q25-MIND-MATTER-ADMISSION-HARDENING-2026-08-26
type: proposal
status: active
date: 2026-08-26
layer: meta
epistemic_layer: os
claim_mode: governance
claim_level: P3/P4_governance
canonical: false
dependency:
  - 01_Source_Intuition/BOOK/Drafts_26Q/Q25_选择广于意识.md
  - Core_Law/SRT_L0_Metaphysics.md
  - Core/SRT_Core_12b_Ontology_L2.md
  - Philosophy/patches/SRT_Philosophy_PH_IND02_Selective_Closure_Perspective_Bearer_Formation_v0_1.md
  - Philosophy/patches/SRT_Philosophy_PH_IND04_Object_Bearer_Selector_Subject_Experiencer_NonJump_Ladder_v0_1.md
  - Philosophy/hooks/PH_IND05_Occurrence_Trace_L2_Bearer_Experiencer_Integration_Hook.md
  - Philosophy/patches/SRT_Philosophy_PH_IND06_Bearer_Concern_Selectability_Relational_Decomposition_v0_1.md
tags: [Governance, Q25, MindMatter, Objectification, Bearer, Individuation, NonJump, Admission, BookHardening]
---

# Q25 Mind–Matter Admission Hardening — Decision Packet (2026-08-26)

> **Status / boundary**: non-canonical governance packet. It records owner subtraction and a minimal hardening route for Q25 plus two narrow P3 additions to existing individuation owners. It does **not** create a new bridge, symbol, primitive, ontology, mind–matter duality, or canonical bearer criterion. It must not be cited as a theorem that bearerhood entails mind or phenomenality.
>
> **Execution state (PR #857):** the Q25 exposition hardening, Q25 professional-note sync, PH-IND05 branching clarification, PH-IND02 writeback test, and owner-side duplicate terminology sweep have all been executed in this PR. This packet remains as the governance/decision record, not as an unexecuted future plan.

## 0. Executive result

The current Q25 core direction survives:

```text
matter / consciousness are not two primordial substances
binary categories are downstream of one selection-generation history
object-side stabilization may occur earlier than reflective subjecthood
```

The wording that should be hardened is narrower:

```text
low complexity -> matter
high complexity -> consciousness
matter / consciousness = two phases
```

This wording is too strong because `complexity` is not an SRT admission criterion and because matter-as-object and consciousness are not mutually exclusive states. A conscious person remains physically objectifiable and re-identifiable; therefore the intended relation is non-exclusive structural differentiation, not phase replacement.

Recommended compression:

> **Complexity is not the gate. Physical objectification does not require bearer admission; mind-side organization requires additional bearer / selector / subject-side structure, while bearerhood still does not by itself establish phenomenality. The resulting categories may overlap in one continuing process.**

No canonical owner is modified by this packet.

---

## 1. Owner subtraction

### 1.1 Q25 already owns the core anti-dualist insight

Q25 §3 already states that:

- matter and consciousness are not primordial ingredients;
- their distinction is generated downstream rather than given at the start;
- the pre-object field is a condition of differentiation, not a neutral substrate;
- object-side organization can precede reflective subjecthood without becoming the explanatory substance from which subjecthood is manufactured;
- object and subject are logically co-originating categories even when their historical emergence is asymmetric.

Therefore the present work must **not** create a parallel `mind–matter interface`, `dual identity`, `cross closure`, or neutral-process ontology.

### 1.2 EX-A already blocks occurrence / persistence collapse

`Core_Law/SRT_L0_Metaphysics.md` already distinguishes:

```text
primitive actualisation
!= anchored persistence
!= Stable ISP
```

and explicitly notes that a table's persistent objecthood belongs downstream of first actuality. This packet does not reopen that distinction.

### 1.3 PH-IND04 already owns the non-jump ladder

Retain:

```text
Object !-> Bearer !-> Selector !-> Subject !-> Experiencer
```

The ladder is a role/admission discipline, not a `matter -> mind` evolutionary sequence. `Object` is wider than physical matter-as-object: institutions, concepts, and emergent structures can be re-identifiable objects without thereby becoming ordinary physical objects.

### 1.4 T-L2-Scaffold already owns foreground/background hardening

Do not redescribe the present increment as a new `L1 foreground / L2 background` theory. `Core/SRT_Core_12b_Ontology_L2.md` already distinguishes trace floor, minimal closure, L2-grade closure, and scaffold threshold. No new writeback symbol is introduced here.

---

## 2. Main Q25 hardening decision

### Q25-H1 — replace the one-axis complexity reading

Do not use `complexity` as if it were the criterion separating matter and consciousness.

Preserve only the weak explanatory use:

```text
later subject / consciousness organization may require more structural conditions
than bare physical object stabilization
```

Do not infer:

```text
higher complexity -> consciousness
lower complexity -> matter
```

Counterexamples include highly complex non-subject systems and highly complex physical objects that remain matter-as-object even when they are also subjects.

### Q25-H2 — replace phase opposition with overlapping structural conditions

The ice/steam analogy should be removed because it suggests:

```text
one token occupies phase A or phase B
```

whereas the SRT-compatible relation permits:

```text
Matter_as_object(X) AND Consciousness_candidate(X)
```

A conscious human does not cease to be physically objectifiable when subject/phenomenal conditions are satisfied.

Therefore prefer:

```text
same generation history
-> different structural thresholds / conditions
-> resulting categories may overlap
```

rather than:

```text
same substrate
-> phase A / phase B
```

### Q25-H3 — physical object admission and bearer admission do different work

For book-level exposition, keep the distinction thin:

```text
physical-object side:
stabilized / physically constrained / re-identifiable organization

bearer side:
same-unit consequence return
+ history-bearing writeback
+ future-condition change
+ continuity / non-outsourcing pressure
```

Do not say matter is produced by deleting an already existing bearer index. The safer statement is:

> **Physical objectification can be admitted without bearerhood ever being established.**

### Q25-H4 — mind and phenomenal consciousness must not be collapsed

The original discussion started from `mind`, while Q25 centrally discusses `consciousness`. Preserve:

```text
functional / historical mind organization
!= phenomenal consciousness
```

A bearer/selector architecture can support functional mind-like organization without closing the `Subject -> Experiencer` burden.

---

## 3. Landed Q25 §3 wording

The book-level revision landed in PR #857 as:

> 回到三层剃刀，你会看到一个完全不同的宇宙生成史。冰川切出河谷、雪花结出六角晶体时，世界并不需要先替它们贴上“物质”标签：河谷会承重，晶体会折射，形态能在不同遭遇中被反复认出。孩子走向沙坑、感受失望并调整行为，也不是另一种“精神原料”突然介入。这里真正多出来的是另一组门槛——后果回到同一具身位，写进它自己的历史，并改变下一次还能怎样选择。物质与意识的区分，因此不能压成一条“复杂度越高就越接近意识”的刻度。
>
> 所以，“物质”和“意识”不是两种预先存在的原料，也不是冰和蒸汽那样彼此替换的两个状态。更准确地说，它们是同一生成过程在不同门槛上形成的范畴，而且可以重叠：一个有意识的人并不会因为获得了承重、主体和感受性，就不再是一个可测量、可重复识别的物理对象。客体侧的稳定化可以远早于主体侧出现；但“更早出现”不等于“作为原料制造后者”。二分不是起点，而是生成过程中逐渐出现的区分。

Retained Q25 commitments immediately after the replacement:

- pre-object field is a prior condition, not common stuff;
- `simultaneous` means logical co-origin, not temporal simultaneity;
- earlier object-side stabilization does not make matter the primitive explanatory ground of subjecthood;
- later subject-side conditions do not cancel physical object conditions.

---

## 4. Q25 professional-note hardening

The chapter note now avoids treating matter/consciousness as products of different `complexity thresholds` or as a `phase transition` pair. It uses existing book vocabulary—`门槛 / 条件 / 范畴`—and keeps the explicit non-exclusivity guard:

> **一个有意识的人仍然可以同时作为物理对象被测量和重识别。**

The Q26-facing failure conditions are split into independently assessable burdens:

1. consciousness-layer independence;
2. selection-structure threshold validity;
3. separability of physical-object re-identification from embodiment/subject/consciousness conditions;
4. the stronger generative claim that no extra primordial property must be posited outside the generation chain.

---

## 5. P3 increment A — branching defeats the equivalence-class shortcut

**Target owner**: `Philosophy/hooks/PH_IND05_Occurrence_Trace_L2_Bearer_Experiencer_Integration_Hook.md`.

### Increment

Directionality already blocks a naive symmetry assumption, but branching is the stronger defeater. If:

```text
B0 -> B1
B0 -> B2
```

and `B1` / `B2` thereafter carry independently closing consequences, then the ordinary symmetric-transitive closure of continuation would pull both successors into one equivalence class through `B0`. That erases the post-fission distinction the bearer analysis is supposed to preserve.

Compact P3 form:

```text
shared predecessor
+ symmetric/transitive closure
!-> one post-branch bearer

continuation(B_t, B_t+1)
!= bearer-identity equivalence by default
```

### Boundary

This does not solve fission, define numerical identity, forbid branching, or introduce a universal bearer metric. It only records why an equivalence-class shortcut is structurally inadequate.

---

## 6. P3 increment B — prospective history-writeback ablation test

**Target owner**: `Philosophy/patches/SRT_Philosophy_PH_IND02_Selective_Closure_Perspective_Bearer_Formation_v0_1.md` under the existing `future-selectability change` admission question.

### Increment

The primary intervention is prospective: block the candidate same-unit history-writeback channel **before** the consequence has been incorporated into the candidate bearer's continuing state, while matching the pre-writeback condition and relevant external inputs as closely as the domain permits. Then ask whether later reachability, transition bias, boundary maintenance, correction burden, or another declared future-selectability proxy diverges.

Critical mediation guard:

> **Do not condition on or match away state variables that are themselves downstream effects of writeback.** Otherwise the test removes the very path whose historical efficacy it is meant to measure.

A current-state-matched / history-divergent design is secondary only. It is informative when the matching is independently justified and explicitly coarse-grained; a null result under a fully matched causal state does not by itself weaken bearer history, because history may act precisely by being incorporated into that state.

### Guardrails

Do not introduce a new canonical `W_B` variable or a universal `do()` equation in this pass.

Do not infer:

```text
any counterfactual effect -> bearer
any material damage -> subject
future-state difference -> phenomenality
```

This is an operationalization of an existing P3 admission burden, not a new definition.

---

## 7. Explicit rejection of the abandoned cross architecture

Do not land the following constructs from the exploratory dialogue:

```text
bearer index as a new primitive
L1^B / L1^pos as new canonical layers
W_B as a new canonical writeback operator
C_parallel / C_perp / C_ret
Dual Identity Interface
Mind-Matter Identity Cross
pi_B / pi_O as co-primary ontological projections
```

Reason:

1. owner subtraction shows substantial overlap with existing `J_B(X)`, consequence-return, objectification, and L2 hardening machinery;
2. a co-primary projection picture risks presupposing an already individuated neutral process and conflicts with Q25's generated-category ordering;
3. the useful residue is narrower and can be absorbed by existing owners without namespace inflation.

---

## 8. Acceptance tests

The landed integration should pass all of the following:

```text
T1  A conscious human can remain matter-as-object; no phase replacement is implied.
T2  A highly complex physical/non-subject system does not become conscious by complexity alone.
T3  A stable physical object can be admitted without bearerhood.
T4  An institution may be a bearer candidate without becoming an ordinary matter-as-object category token.
T5  Object !-> Bearer !-> Selector !-> Subject !-> Experiencer remains intact.
T6  Branching continuation is not collapsed by a symmetric/transitive equivalence-class shortcut.
T7  Prospective writeback ablation tests historical efficacy without conditioning away writeback-mediated state change; it does not define bearerhood by itself.
T8  No new canonical symbol or bridge is required.
T9  EX-A occurrence / anchoring / Stable ISP distinctions remain untouched.
T10 Q25 still rejects materialism, idealism, panpsychism, and neutral-substrate monism without claiming that matter and consciousness are mutually exclusive phases.
```

---

## 9. Execution record — PR #857

Completed in this PR:

```text
1. Q25 §3
   -> removed low/high-complexity criterion
   -> removed ice/steam phase analogy
   -> retained overlap guard with book-native vocabulary

2. Q25 professional note
   -> removed complexity-differentiation framing
   -> split Q26-facing failure burdens
   -> replaced bare `bearer` in book prose with existing `具身位`

3. PH-IND05
   -> made branching the decisive counterexample to quotient/equivalence shortcut

4. PH-IND02
   -> changed state-conditioned ablation into prospective writeback-channel ablation
   -> added mediation guard against matching away writeback effects

5. Owner-side duplicate search / hygiene
   -> synchronized `附录_跨域难题_重述而非解决.md`
   -> removed newly coined book-level `下游资格 / 结构资格` vocabulary
   -> restored trailing newlines on touched P3 files and this packet
```

No new bridge was created from this workline.
