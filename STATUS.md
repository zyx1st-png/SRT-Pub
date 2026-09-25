---
id: SRT-STATUS
type: dashboard
status: active
layer: meta
epistemic_layer: os
claim_mode: evidence
updated: 2026-09-25
---

# SRT 当前状态仪表盘

> **角色**：fresh session 当前状态入口。先执行 `AGENTS.md §Session Start` 的三文件 bootstrap；本页只提供当前 checkpoint、程序级 verdict 与前向路由，不替代 canonical owners、作者源或历史审计。
>
> **记录口径（2026-09-13 起）**：本页记录**已落地事实**，以及由已落地治理 / 作者裁决支持的**当前 programme state**——两者都属于当前状态面板的职责（`AGENTS.md` 执行后条目、`Governance/SRT_EDIT_PROTOCOL.md` 留痕位置表）。但**不得把未合并 PR 自身的 lifecycle 写成仓库当前事实**：`#N = DRAFT / ACTIVE / WAITING CI` 属于那个 PR，不属于本页。进行中的 owner cycle 以 **owner 文件或 bounded work package** 指称，未合并 PR 号不得充当状态 owner。原因：#959 与 #961 两轮都在各自 landing PR 内部把该 PR 写成 ACTIVE，合并当天本页即失真。本条由 `scripts/check_status_recording_rule.py` 强制（本行含反例文本，故带豁免标记）。<!-- status-lint:allow -->
>
> **历史快照**：pre-#931 根 STATUS 已保存在 `Operations/Status_History/SRT_STATUS_2026-09-11_PRE_PR931_ROOT_SNAPSHOT.txt`。#931/#933/#938 继续作为历史重构与纠偏 provenance；#940/#942 是局部 landing。自 #947 起，跨 owner 的当前生成顺序、非同一性与 OPEN gate 以 `Core_Law/SRT_Generative_Ontology_Spine.md` 为第一 canonical 路由，旧 canonical 的冲突跨层推论转为 cleanup / retyping debt。#957 已于 2026-09-13 合并为 whole-skeleton **非 canonical 作者检查点**；#959 已完成第一只 post-#957 bounded canonical landing，当前 `Core_Law/SRT_Generative_Ontology_Spine.md` 已是 post-#959 cross-owner canonical spine。#961 已完成第二只 post-#957 bounded owner landing：L0 targeted thinning。#970 已完成第三只 bounded owner landing：One Formation vertical-reconstitution semantics。#972 已完成 post-One Generative Ontology Spine 小型同步，canonical trunk 当前达到本轮 cleanup stop condition；L0 / Bearer / Stable ISP / Individuation 均未被连带打开。#976 已于 2026-09-20 合并 Ground / pre-object L0 whole-tree reconstruction。随后作者在 post-#976 对话中把下一研究主线重定向为 noncanonical Generative Relational Grammar (GRG) programme：从 Selection 作为 non-flat generative change 出发，整合跨主体 / 跨领域经验与成熟邻居作为 reciprocal constraints；winner-style strongest-neighbor novelty audit 不再是当前 root question。

## Fast Status

### 0. Landing ledger — 已落地事实（2026-09-13）

```text
#951 retrospective provenance closeout = MERGED / 62707551602a9d56ac9ec898ea6a66f098b5e543
#952 R2-A authority truth-up = MERGED / e33476e06de3471d11c1994595669552764983ab
R2-A F1/F4/F6/F8/F10/F11 = COMPLETE
#954 R2-B Bearer semantic quarantine = AUTHOR OPTION A ACCEPTED / BOUNDED CANONICAL LANDING
R2-B F2/F5/F9 = COMPLETE IN THIS LANDING
#955 R2-C supersession infrastructure = AUTHOR OPTION A ACCEPTED / BOUNDED GOVERNANCE LANDING
R2-C F3/F7 = COMPLETE IN THIS LANDING
#957 whole-skeleton minimal ontology checkpoint = MERGED / b17d4e6d36ee31e2cfbf465e0578c95be450b97b
#957 role = NONCANONICAL AUTHOR BASELINE FOR BOUNDED OWNER LANDING
#958 owner landing scope = MERGED / 2676f20b3ec0c34120870a1a191ce5969f16d45f
#959 post-#957 Generative Ontology Spine landing = MERGED / 981d544804f935a6399fd3a309dadefc51d8ea5c
#961 L0 targeted thinning = MERGED / 5591c793cd985729a228a22da3a3c8c5fb7a7453
#969 vertical-background author checkpoint = MERGED / 345412f627acd17cf0185547b48e34791cd0a9d4
#970 One Formation vertical-reconstitution landing = MERGED / 0b4ba7dd6a818b70e8cebd7b7f4c681218ef5606
#972 post-One Generative Spine synchronization = MERGED / d29f2d59482ca6f87386f0344d81a6b3b375650d
#949 = SUPERSEDED LIVE GATE / PROVENANCE ONLY
#956 = SUPERSEDED INTERMEDIATE CHECKPOINT / PROVENANCE ONLY
BROAD L0 / MULTI-OWNER CANONICAL REWRITE = NO
OWNER-BY-OWNER CANONICAL LANDING = ACTIVE
FIRST BOUNDED OWNER LANDING = COMPLETE IN #959 / GENERATIVE ONTOLOGY SPINE
SECOND BOUNDED OWNER LANDING = COMPLETE IN #961 / L0 METAPHYSICS
THIRD BOUNDED OWNER LANDING = COMPLETE IN #970 / ONE FORMATION
CANONICAL TRUNK FOLLOW-UP SYNC = COMPLETE / FURTHER OWNER CLEANUP PAUSED BY DEFAULT
#1031 Selection occurrence / sedimentation canonical reconciliation = MERGED / 1a7ed931e75f40f1a30d7b17c5e2ac3439f0e0dd
#1032 provenance / vocabulary reconciliation = MERGED / 35c547ef160d9460ce654b05107baae06c47d91e
#1047 Spine minimal-kernel L0/L1/L2 author adjudication + restoration audit = MERGED / 7308c8b0c3b2bc71811e59a789c360bb5053c839
#1047 role = NONCANONICAL DIRECTION + FUTURE C-CLASS CONTRACT; C1/C2 SPINE RESTORATION NOT AUTHORIZED; OWNER-CLEANUP PAUSE UNCHANGED
#1055 pre-object vertical gating / glue / generative-divinity source + reconciliation plan = MERGED / 01faf40bfb903a1f2c9d378939f5452d36d7cad9
#1055 role = NONCANONICAL SOURCE + CANONICAL-OWNER-STAGE MATERIAL; RETAINED FOR LATER CANONICAL-OWNER STAGE / NOT CURRENT NEXT
#1059 gate-geometry / qualia independent content review = MERGED / d46ad63f3dad4cdfc059c3a371c0c0712f0befad
#1059 role = READ-ONLY AUDIT / triggered explicit A-1…A-5 second adjudication; no canonical edit
2026-09-24 AUTHOR SEMANTIC / DRAFTING SEQUENCING = SPINE OPTIMIZATION FIRST -> THEN OTHER CANONICAL OWNERS; MERGE MUST KEEP MAIN MUTUALLY CONSISTENT; EXECUTION START NOT YET INSTRUCTED
REPOSITORY SELF-RECONSTRUCTION PHASE 2 / 3 = COMPLETE
CURRENT GRG FOUNDATION OWNER = Operations/Proposals/SRT_GRG_FOUNDATIONAL_PROTO_GRAMMAR_V0_3_2026-09-21.md
CURRENT NEXT = high-priority gate-geometry / qualia bounded routing patch; no canonical edit in first pass
CURRENT NEXT OWNER = Operations/Proposals/SRT_GATE_GEOMETRY_QUALIA_SHORT_TERM_ROUTING_PATCH_2026-09-25.md
CASE2 SOURCE ADEQUACY = PASS
CASE2 PRIMARY VERDICT = SOURCE_OWNED_DECOMPOSITION_NO_GRG_GAIN
§8.1 COUNT = FRR case1 + engagement/recommender case2 = TWO ADEQUATE NO-GAIN CASES
§8.1 STOP-LOSS = EXECUTED
FUSION LANE = PAUSED / CONTRACTED
THIRD FUSION DOMAIN = NO / no replacement or rescue target authorized
BCTB T2 = HOLD / NOT AUTOMATIC
BROADER CANONICAL GRG EXPANSION = HOLD
```

### 0.3a High-priority gate-geometry / qualia route — 2026-09-25

Author source, second adjudication and accepted analysis:

- `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GATE_GEOMETRY_BEARER_FRICTION_QUALIA_L0_FREEDOM_2026-09-25.md`
- `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GATE_GEOMETRY_PR1058_REVIEW_SECOND_ADJUDICATION_2026-09-25.md`
- `01_Source_Intuition/SRT_DIALOGUE_DERIVATION_TRACE_GATE_GEOMETRY_QUALIA_CONSCIOUSNESS_2026-09-25.md`

Bounded execution owner:

- `Operations/Proposals/SRT_GATE_GEOMETRY_QUALIA_SHORT_TERM_ROUTING_PATCH_2026-09-25.md`

Current status:

```text
AUTHOR DIRECTION = ACCEPTED / HIGH RETRIEVAL PRIORITY / NONCANONICAL;
SHORT-TERM TASK = OWNER CROSSWALK + COLLISION MAP + PATCH PREPARATION;
FREEZE-A CANONICAL EDIT = NO in first pass;
HP-B / phenomenal necessity = OPEN;
dialogue friction = broader bearer-relative reconstruction-burden family;
dialogue friction PARTIAL_OVERLAP canonical Psi_f / historical Psi_f^maint; identity NOT ESTABLISHED;
gate geometry != Psi_f;
Gate != primitive Selection;
One != Bearer != Experiencer;
GRG fusion lane remains PAUSED;
BCTB T2 remains HOLD;
new GRG v0.4 = NOT AUTOMATIC.
```

This author instruction **supersedes the prior immediate GRG-next sequencing without reopening the stopped fusion lane**. The GRG post-stop-loss method contraction is now handled inside Route H of the bounded gate-geometry patch. The 2026-09-25 second adjudication narrows the 09-23 "深层的语法" intuition: first reconstruct objectification / coarse-graining / L0-L1-L2 generative depth; treat any deep grammar as a downstream reconstruction result, not an upstream universal-grammar assumption.

The routing patch must stop after its declared D1-D5 deliverables and return substantive meaning changes for author adjudication before any Freeze-A semantic landing.

### 0.4 Current GRG / repository-reconstruction route — 2026-09-23

Current merged repair state:

```text
Selection occurrence vs retained historical efficacy / sedimentation / inheritance
= CANONICALLY RECONCILED in #1031;

terminal Selection remains genuine;

genuine actualised Selection
vs merely descriptive / modelled change
= OPEN;

09-22 provenance / vocabulary reconciliation
= COMPLETE in #1032;

BCTB T1
= COMPROMISED-DIAGNOSTIC / BASELINE-SHARED / no GRG residual credit;

BCTB T2
= HOLD / not automatic.
```

Current source-level GRG continuation:

- `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GRG_GENERATIVE_CAPACITY_INTERVENTION_GRAMMAR_2026-09-22.md`
- `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GRG_REACH_RECONSTRUCTIBILITY_GENERATIVE_DEBT_2026-09-22.md`
- derivation provenance: `01_Source_Intuition/SRT_GRG_DIALOGUE_DERIVATION_TRACE_RECONSTRUCTIBILITY_REACH_2026-09-22.md`

Current bounded foundational GRG owner:

- `Operations/Proposals/SRT_GRG_FOUNDATIONAL_PROTO_GRAMMAR_V0_3_2026-09-21.md`

Authority boundary:

```text
v0.3
= bounded noncanonical foundational owner for the grammar admitted through 2026-09-21;

09-22 reach / reconstructibility / generative-debt architecture
= source-level research direction;

09-22 concepts
!= silently incorporated into v0.3
!= canonical SRT
!= reason to create v0.4 before pressure-testing.
```


Current merged continuity / routing surfaces:

- `01_Source_Intuition/SRT_AUTHOR_ROUTING_GRG_CROSS_OBJECTIFICATION_ROOT_RETURN_2026-09-24.md`
- `Operations/Handoffs/SRT_GRG_ROOT_RETURN_FUSION_LANE_CURRENT_NEXT_HANDOFF_2026-09-24.md`
- `Operations/Handoffs/SRT_GRG_DIALOGUE_RECOVERY_CURRENT_NEXT_HANDOFF_2026-09-24.md`
- `01_Source_Intuition/SRT_GRG_DIALOGUE_CONTINUITY_RECOVERY_MASTER_2026-09-23.md`
- `Operations/Audits/SRT_GRG_ACCEPTED_MACHINE_ANALYSIS_CONTINUITY_AUDIT_2026-09-23.md`

Execution / closeout guard:

```text
one CURRENT NEXT only;
prospective case2 engagement test = EXECUTED;
SOURCE_ADEQUACY = PASS;
primary verdict = SOURCE_OWNED_DECOMPOSITION_NO_GRG_GAIN;
§8.1 adequate no-gain count = 2;
independent review = UPHELD;
§8.1 stop-loss = EXECUTED;
fusion lane = PAUSED / CONTRACTED;
FORMER GRG NEXT = post-stop-loss method contraction / root-question review; SUBSUMED INTO 2026-09-25 GATE-GEOMETRY ROUTING PATCH ROUTE H;
no replacement target / third rescue domain;
no BCTB T2 / v0.4 / canonical expansion follows automatically.
```

### 0.4a Provenance / vocabulary owner

Current reconciliation map:

`Operations/Audits/SRT_REPOSITORY_SELF_RECONSTRUCTION_PHASE3_PROVENANCE_VOCABULARY_MAP_2026-09-23.md`

Use only the four provenance classes:

```text
A0-Q = preserved direct author quotation
A0-P = faithful paraphrase of an author-originated move
A1   = machine consolidation with preserved explicit author acceptance
M    = machine synthesis / wording without item-level acceptance evidence
```

Important vocabulary guards:

```text
Selection occurrence != retained historical efficacy / sedimentation / inheritance;
generative inheritance != X4c automatically;
structural / operative generative expectation != E_G automatically;
generative / GRG proxy != measurement / operational proxy;
constitutive / boundary friction != Psi_f automatically;
generative reconstructibility != repository/data reconstructibility;
GRG generative debt != repository maintenance / reconciliation debt.
```

BCTB T1 evidence preservation ref:

`archive/grg-bctb0-t1-evidence-20260922`
-> `b393b46c64f172a4fba770982219b5249e32dded`

### 0.5 Superseded GRG routing — provenance only

The former theory-rich §0.4 / §0.4a / §0.5 summaries and the 87-item 2026-09-21 Immediate routing ledger are **not current routing**.

They are preserved verbatim at:

`Operations/Status_History/SRT_STATUS_2026-09-23_PRE_PHASE4_GRG_ROUTING_SNAPSHOT.md`

Use them for reconstruction / provenance only. They do not override §0.4 above, the Phase 3 reconciliation map, v0.3's synchronization boundary, or current canonical owners.

### 1. 当前 programme state 与 owner 指针

```text
canonical cross-owner routing = Core_Law/SRT_Generative_Ontology_Spine.md;
local canonical definitions = Registry-routed compatible owners;
Selection occurrence / sedimentation reconciliation = COMPLETE;
anti-tautology criterion for genuine Selection = OPEN;

GRG foundational research owner = SRT_GRG_FOUNDATIONAL_PROTO_GRAMMAR_V0_3_2026-09-21.md;
09-22 reach / reconstructibility / generative-debt = source-level / research;
Phase 3 provenance + vocabulary owner = SRT_REPOSITORY_SELF_RECONSTRUCTION_PHASE3_PROVENANCE_VOCABULARY_MAP_2026-09-23.md;

new GRG v0.4 owner = NOT AUTHORIZED BY CURRENT STATE;
wholesale 09-22 canonicalization = NO;
BCTB T2 = HOLD / NOT AUTOMATIC;

Level 2 = HOLD;
new Level 1 = NOT ASSIGNED;
scientific distinctiveness = NOT ESTABLISHED;
research_mode = U.
```

### 2. Current controlling route — ontology / canonical edits only

> `CANONICAL_REGISTRY.md §C` is the single owner of complete citation priority. The list below is a **task-local working read sequence**, not a second authority chain; cross-owner adjudication still resolves through Registry §C -> Generative Ontology Spine -> compatible local owners.

For current ontology / canonical-cleanup work, load in this order:

1. `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_SPINE_MINIMAL_KERNEL_L0L1L2_REFLEXIVE_FACETS_2026-09-24.md` — latest merged author direction for Spine restoration: two-role Spine (Part I universal formation kernel stopping at One; Part II thin typed post-One map), L0/L1/L2 labels, SRT / GRG role emphasis; noncanonical
2. `Operations/Audits/SRT_GENERATIVE_ONTOLOGY_SPINE_SEMANTIC_THINNING_AUDIT_2026-09-24.md` — bounded future C-class contract for that restoration (guards, complete OPEN mapping, landing order, acceptance tests); noncanonical
3. `01_Source_Intuition/SRT_AUTHOR_FINAL_ADJUDICATION_PR957_POSITION_RECURRENCE_CONCERN_2026-09-13.md` — whole-skeleton landing direction (2026-09-13), reconciled with 2026-09-14 Selection-totality by item 1; noncanonical
4. `Operations/Audits/SRT_POST957_OWNER_LANDING_SCOPE_AUDIT_2026-09-13.md` — bounded owner/edit-risk/landing sequence; noncanonical
5. `Core_Law/SRT_Generative_Ontology_Spine.md` — current cross-owner canonical order / non-identity / OPEN-gate owner
6. `CANONICAL_REGISTRY.md` — local owner routing after the spine
7. `Governance/SRT_CLAIM_LADDER.md` / `Governance/SRT_CLAIM_MODE_AUDIT.md` — claim hardness / demotion state
8. `Core_Law/SRT_L0_Metaphysics.md` / `Core_Law/SRT_One_Formation.md` / P1-T06 / d / Psi_f / T_dir — local owners, only within spine-compatible scope

Current cleanup / landing rule:

```text
#957 author checkpoint = landing constraint, not definition authority;
current canonical spine = definition/routing authority until edited;
compatible local definitions survive;
retiring an old claim does not require inventing a replacement theorem;
OPEN stays OPEN unless separately adjudicated;
land one Freeze-A owner at a time whenever practical.

2026-09-24 Spine restoration direction (items 1-2)
= direction + contract only, not definition authority;
C1 (L0 Metaphysics / Symbol Table) and C2 (Spine rewrite)
= NOT AUTHORIZED while further owner cleanup stays paused by default;
opening them needs explicit author unpause and must not create a second CURRENT NEXT;
stacked one-owner-per-PR landings satisfy both "one Freeze-A owner at a time"
and the audit's "no half-landed main" condition only if merged as one consistent set.

2026-09-24 author sequencing
(01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_PR1055_REVIEW_SECOND_ADJUDICATION_2026-09-24.md D-3)
= semantic / drafting work: Spine optimization first, then the other canonical owners;
  supersedes the restoration audit §14.0 machine "local-owner-first" semantic-work recommendation;
  integration / merge order remains constrained by the no-contradiction guard:
  main must not carry Spine and local owners in contradictory states;
  if synchronization is required, use a stacked / synchronized package and merge only a mutually consistent state;
  canonical-owner stage material = 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_PREOBJECT_VERTICAL_GATING_GLUE_GENERATIVE_DIVINITY_2026-09-24.md
    + Operations/Proposals/SRT_PREOBJECT_VERTICAL_GENERATION_CANONICAL_RECONCILIATION_PLAN_2026-09-24.md;
  starting either stage (and unpausing owner cleanup) still requires explicit author instruction.
```

The pre-#947 unmerged branch `theory/canonical-cleanup-b1-individuation-20260911` is candidate patch material only. Do not merge it as-is; re-audit / rebase its useful repairs against the post-#957 landing sequence.

---

## Current theory spine — post-#959 canonical reading

> #959 has now landed the first post-#957 canonical owner rewrite. The route below is current cross-owner authority; older G0→G5 wording is superseded at the cross-owner level while compatible local-owner content survives until its own bounded cycle.

### 3. Primary ontology-generation spine

```text
[modal condition]
non-flat / non-neutral openness

-> [primitive generative operation]
finite-position-indexed subjectless Selection
= actual differentiation
= manifestation / relative backgrounding
= primitive verticality as same-event structural reading

-- regenerative role recurrence -->
One
```

The universal formation route now stops at **One**. `Core_Law/SRT_One_Formation.md` is now the post-#970 v1 local owner for detailed One / Selection-position semantics; formed `Selection-position` remains the operative co-aspect of an already formed One and is not a second universal endpoint.

Do **not** use as primary generation laws:

```text
history-bearing -> verticality
history-to-reconstitution -> Bearer
formed process -> One -> Stable ISP -> subject-position
```

### 4. History / verticality typed separation

Current controlling SED-B / VG distinction:

```text
SED-B / historical writeback
= result / condition side:
  prior Selection leaves retained history-conditioned differences
  that alter later transition / reconstitution conditions.

VG / active vertical generation
= source / ongoing-process side:
  Selection generates / regenerates the non-flat relation through which
  manifestation and relative backgrounding occur.
```

Therefore:

```text
history != ontological source of verticality
historical writeback != Selection-position
historical writeback may condition later vertical re-generation / reconstitution
```

Post-#959 guard: genuine Selection may leave an ontic before/after non-equivalence, but irreversible occurrence does not by itself establish durable, localized or recurrent historical efficacy. Where history does become effective, it can condition later Selection without becoming a second primitive source of Selection or verticality.

### 5. Positionality and Selection-position

Three burdens must remain distinct:

```text
L0 positionality:
Selection is necessarily indexed to a finite position.

formed Selection-position:
an already formed vertical organization / One has a time-local operative from-where.

stronger first-person bearing direction:
future alternatives become different in what this continuing position itself
is expected to undergo / preserve / lose / enable.
```

Guards:

```text
position alone != perspective
Selection-position standing != Bearer automatically
Selection-position standing != first-person bearing automatically
first-person bearing != subjecthood automatically
```

### 6. Perspective layering

Current One-level direction:

```text
One-level perspective candidate
= the lineage-conditioned organization of a formed One / Selection-position
  is itself load-bearing in later manifestation, relative backgrounding,
  and maintenance / construction of selectable space.
```

This is endogenous participation, not an external coordinate description.

Current status:

```text
One-level perspective can exist: YES / reconstruction direction
all Ones automatically have it: NOT ESTABLISHED
full sufficient condition: OPEN
```

Bearer-level perspective is a thicker downstream research direction in which future branches become related to what the continuing position itself is to undergo / preserve / lose / enable.

Phenomenal / experiencer perspective remains separately OPEN.

### 7. Anticipation layering

Anticipation must not be moved entirely downstream to Bearer.

```text
A1 Selection / verticality forward structuring:
future selectable space is actively constructed / maintained / kept re-enterable.

A2 formed-position internal anticipation:
a formed One / Selection-position participates from within its own organization
in preparing / differentiating possible continuations.

A3 Bearer research direction:
future branches become non-neutral in terms of what this position itself
will undergo / preserve / lose / enable.
```

None of A1–A3 automatically means Bayesian prediction, explicit cognitive modelling, consciousness or phenomenality.

### 8. One / Selection-position / Bearer current layering

```text
One
= canonically: formed process-unity carried by a relatively separable
  Selection-mediated vertical reconstitution path;
  exact identity / boundary remain OPEN.

Selection-position_t
= canonically: time-local operative from-where of an already formed One.

Bearer
= canonically routed as an already formed One / Selection-position satisfying
  P prospective self-indexing + E same-One prospective exposure at semantic / architectural strength;
  the current E non-outsourcing counterfactual is a consistency / exclusion test;
  an independently applicable positive E admission criterion remains OPEN;
  pre-#947 bearer-language is quarantined pending claim-by-claim retyping;
  a universal formal / empirical cross-domain N&S theorem remains OPEN.
```

Hard guards:

```text
One != Bearer
Selection-position != Bearer
history-bearing != Bearer
own-history writeback != bearing
being affected != bearing
feedback != bearing
Bearer != 承担 by definition
Bearer != subject
Bearer != experiencer
```

---

## Supersession ledger for #931 / #933

### 9. What remains retained

Retain from #931/#933 within scope:

```text
pre-object difference -> subjectless Selection;
manifestation + relative backgrounding;
active vertical organization;
One / Selection-position distinction;
role-regenerative recurrence at cross-owner strength; exact lineage identity remains local / OPEN;
distributed history / no mandatory centralized history store;
who causes != who bears;
being affected != bearing;
feedback != bearing;
state change != own-history writeback;
W2 happened to O != O actively Selected;
Active Selection != second-order Selection;
multiscale standing must be paid independently at each claimed scale.
```

### 10. What is demoted / retyped

```text
history-to-reconstitution dependence
-> retrospective integration / continuity evidence relation;
   necessary role for Bearer = OPEN;
   sufficient Bearer status = WITHDRAWN.

self-consequence closure
-> retrospective self-effect closure relation;
   possible future input to Bearer research = OPEN;
   no longer ordered as > generic Bearer.

matched-history tests
-> retrospective dependence tests only;
   no Bearer score by themselves.

PH-IND02 PERS-2
-> retrospective consequence/history relation family;
   no longer a Bearer admission gate.
```

### 11. What is retired as current admission logic

```text
history-to-reconstitution = Bearer definition: RETIRED
first constitutive history coupling = Bearer onset: RETIRED
SC > generic Bearer: RETIRED
old R-B / R-C as live Bearer owner routes: RETIRED
presence / absence of constitutive historical writeback -> Bearer YES / NO: RETIRED
```

The historical author acceptance of the earlier gate remains part of the research record; its current sufficiency status is superseded by the later author adjudication.

### 12. W2 cases E / F current reading

Historical descriptions remain useful, but Bearer verdicts are superseded.

```text
Case E:
no constitutive later-history relation for the named perturbation
-> retrospective history-to-reconstitution relation = NO
-> Bearer = NOT ESTABLISHED BY THIS TEST

Case F:
persistent lineage-indexed history-to-reconstitution relation
-> retrospective relation = YES / candidate as separately scoped
-> Bearer = NOT ESTABLISHED BY THIS TEST
```

Thus neither absence nor presence of that retrospective relation is currently a sufficient Bearer classifier.

---

## Stable ISP / B13 / measurement routing

### 13. Stable ISP and B13

P1-T06 Stable ISP and B13 remain important canonical neighbors, but no longer organize the ontology-generation spine.

Use them for:

```text
standing / persistence / perspective / history / consequence crosswalks
```

Do not use them for:

```text
verticality generation
Bearer admission
subjecthood proof
```

Post-#959 routing:

```text
One / Selection-position formation
= owned upstream by `Core_Law/SRT_One_Formation.md` at D4a strength.

P1-T06 Stable ISP
= stronger recurrent standing criterion.

B13
= stabilization / generative-health crosswalk.
```

Do not infer `One -> Stable ISP`, `Stable ISP -> full One theorem`, or subjecthood from this routing. The formal necessary-and-sufficient One theorem remains OPEN.

### 14. W1 / W2

Owner: `Operations/SRT_W1_W2_WRITEBACK_AUDIT_LABELS.md`. 标签定义、表示不变性护栏与 `W2 != Bearer` 硬限制以该文件为准；本页不再定义它们，也不再作为该类型学的事实 owner。

### 15. d / sigma / T_dir

Continue to preserve:

```text
d-value != subject proof
sigma threshold != ontology event by itself
T_dir != subject proof
measurement variables may read declared structures;
they may not silently constitute them.
```

Exact bearer/domain and threshold assignments remain OPEN.

**既有 d/q/o 下游护栏（继续有效）**：owner 为 `Governance/SRT_DOWNSTREAM_GUARDRAILS.md` §G-DQO，禁运原句与解除条件以该文件为准；本页不再持有该句，也不再作为生成器抽取源。

---

## Programme-level verdicts unchanged

### 16. HOLD

```text
CONTINUE HOLD — NAMED BLOCKER
```

The blocker remains a bounded implementation-specific Level-2 realization design that can:

```text
1. identify a Selection candidate independently of the consequence being tested;
2. expose an author-owned SRT relation to a prospective divergence against a named strongest mature comparator.
```

Physics is permitted but not privileged.

### 17. IRR-B

> Genuine Selection leaves an incompletely erasable effective difference somewhere in the current complete relevant causal state; local restoration / information relocation may occur, but the complete relevant system cannot truly return to the same pre-Selection state.

```text
IRR-B Level 1: PASS — NARROW
IRR-B Level 2: HOLD
```

### 18. MOBJ2-B

```text
Level 1 PASS — NARROW / RECOVERED / CLASS-M SCOPED
```

It distinguishes SRT only from Class-M approaches that take the determinate manifest interface as primitive. It does not by itself distinguish SRT from constitutive theories such as Barad / Simondon.

Do not transfer that Level standing to One / Bearer / Active Selection reconstruction.

### 19. Physical trigger pluralism

```text
no physics-first universal primitive Selection registration is required;
bounded domain-specific physical admission surfaces are permitted;
physical realization is not privileged over other implementations.
```

---

## Authority / publication guards

### 20. Authority routing — pointer only

For exact registered meanings and current cross-owner order, read the owners directly:

- `CANONICAL_REGISTRY.md §C` — **single owner of the complete current citation priority** (10 levels, from registry entry through split navigation)
- `Core_Law/SRT_Generative_Ontology_Spine.md` — cross-owner generation order, non-identities and OPEN gates

**This page does not restate that chain.** `AGENTS.md` states the rule: `STATUS.md` may specify a task-local working read sequence — that is §2 above, and it is explicitly not a second citation-priority chain — but a competing complete authority chain must not be reconstructed in a runtime file. The five-level list that stood here was a lossy copy of Registry §C's ten, so removing it drops no routing information.

`STATUS.md` is routing / programme state, not definition authority.

If an older local canonical surface conflicts with the new spine at the cross-layer inference level, preserve any compatible local content but route the conflict into canonical cleanup rather than allowing historical status to override the new spine.

### 21. Publication carve-outs

```text
Book mainline:
01_Source_Intuition/BOOK/Drafts_26Q/
= current book source-intuition mainline; no automatic full-book rewrite from #938.

Frontiers manuscript 1837760:
PUBLISHED
DOI 10.3389/fnins.2026.1837760

Costly Selective Closure / Adaptive Behavior:
SUBMITTED / NOT EXTERNALLY REVIEWED
Do not describe it as "under review" unless status changes.
```

Reconstruction does not retroactively rewrite published/submitted framing unless separately authorized or required.

---

## Current collaboration / governance routing

### 22. Session start

Fresh-session read order has a single owner: `AGENTS.md §Session Start`. This page neither restates nor extends it.

For current ontology / cleanup work, load the merged #957 final author adjudication and landing-scope audit first as noncanonical constraints, then `Core_Law/SRT_Generative_Ontology_Spine.md` and its local owners. Historical #931/#933/#938/#949/#956 material is provenance and controls only where not superseded by #947/#957 or later explicit author decisions.

### 23. Canonical freeze / edit discipline

Before any canonical theory edit, load:

- `Governance/SRT_CANONICAL_FREEZE.md`
- `Governance/SRT_EDIT_PROTOCOL.md`

#972 is now the synchronized semantic cross-owner canonical spine state following the #970 One landing. #952 continues to close the R2-A authority-propagation layer: Registry §C owns the complete citation-priority chain, the Spine owns cross-owner generation order / non-identity / OPEN routing, and compatible local owners retain local definitions. #957 remains the noncanonical author baseline; #961 completed the bounded L0 owner cycle; #970 completed the bounded One Formation owner cycle. No new canonical owner cycle is open by default. Further canonical edits require a demonstrated live contradiction, separate author adjudication, or bounded operational/formal necessity. The next substantive programme work is the noncanonical GRG Framework Construction mainline. Bounded transfer/data-access work is calibration, not the programme-wide gate.

---

## OPEN register

> **Programme-level verdicts only.** The ontology OPEN items this page used to carry moved to their owners on 2026-09-13 under `Operations/Audits/SRT_OPEN_REGISTER_OWNERSHIP_ADJUDICATION_2026-09-13.md`. **Nothing was closed in that move**: every item is recorded unchanged in its receiving surface.

Do not silently close:

```text
whole-architecture non-substitutability;
scientific distinctiveness;
Level-2 realization.
```

`new Level 1 = NOT ASSIGNED` and `Level 2 = HOLD` are carried in §1 with the rest of programme state.

Everything else is held by its owner — read them there, not here:

```text
cross-owner ontology OPEN gates      -> `Core_Law/SRT_Generative_Ontology_Spine.md` §13
One / Selection-position local OPEN  -> `Core_Law/SRT_One_Formation.md` §7
symbol / formalism hardening ledger  -> `Core/SRT_OPEN_TENSIONS.md`
collective higher-order realization  -> `Core_Law/SRT_Collective_Selection.md` §9
W1 / W2 audit labels                 -> `Operations/SRT_W1_W2_WRITEBACK_AUDIT_LABELS.md`
```

Two facts about the move that a reader of the owners alone would not see:

```text
former S04 + S12 = ONE record, now Spine §13 `Bearer <-> Concern` (Concern = 关切 per A4);
merging two records did not close the question — it stays OPEN.

Bearer admission threshold + Bearer <-> position stability
= PROVISIONAL routing in the Spine OPEN register (§13) while Bearer canonical ownership is itself OPEN.
```

Pointer note (2026-09-24): the register moved from Spine §9 to §13 in the 2026-09-14 Selection-totality retype, which also shortened its compact list. Several items in the post-migration 2026-09-13 Spine §9 register (including the two PROVISIONAL Bearer items above) are no longer named individually and are held only by §13's "omitted items remain OPEN" clause. The list is in `Operations/Audits/SRT_GENERATIVE_ONTOLOGY_SPINE_SEMANTIC_THINNING_AUDIT_2026-09-24.md` §12.1a; nothing was closed.

---

## Immediate routing

Current single next:

```text
HIGH-PRIORITY GATE-GEOMETRY / QUALIA BOUNDED ROUTING PATCH

owner:
Operations/Proposals/SRT_GATE_GEOMETRY_QUALIA_SHORT_TERM_ROUTING_PATCH_2026-09-25.md
```

Execution boundary:

1. start from the 2026-09-25 author-adjudication record and accepted dialogue derivation trace;
2. route GG-1..GG-8 through the declared L0/L1/L2, One/Bearer, Psi_f, Hard Problem, qualia, consciousness, Agency and GRG owners;
3. produce D1-D5 only: owner crosswalk, semantic collision map, bounded patch list, revised Z6 deletion test and GRG contraction decision packet;
4. do not edit Freeze-A canonical owners in the first pass;
5. preserve `B_s -> B_p ?`, genuine Selection vs descriptive/modelled change, and all named One/Bearer/Experiencer non-identities as OPEN where currently OPEN;
6. do not identify dialogue `friction` with canonical `Psi_f` without a separate semantic crosswalk;
7. keep the GRG fusion lane paused; do not create v0.4, run BCTB T2, or acquire a third fusion domain from this route;
8. stop after D1-D5 and return only substantive meaning decisions that require author adjudication.

The former GRG latent-reach / post-stop-loss next is not discarded: its method-level burden is subsumed under Route H of this bounded patch, where the specific question is whether GRG should reconstruct gate / objectification geometry before inferring cross-domain grammar.

The former 2026-09-21 87-item routing ledger remains provenance-only in the Phase-4 status snapshot linked from §0.5.

## Historical navigation

Pre-#931 snapshot:

`Operations/Status_History/SRT_STATUS_2026-09-11_PRE_PR931_ROOT_SNAPSHOT.md`

Byte-preserving raw snapshot:

`Operations/Status_History/SRT_STATUS_2026-09-11_PRE_PR931_ROOT_SNAPSHOT.txt`

Other historical handoffs remain under `Operations/Status_History/`.

When historical files conflict, do not resolve by date alone: separate current canonical K, explicit author A, historical B, machine C and open D; apply explicit supersession records within their declared scope.
