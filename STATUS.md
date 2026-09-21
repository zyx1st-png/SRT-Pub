---
id: SRT-STATUS
type: dashboard
status: active
layer: meta
epistemic_layer: os
claim_mode: evidence
updated: 2026-09-21
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
NEXT RESEARCH WORK PACKAGE = GRG FRAMEWORK CONSTRUCTION / NONCANONICAL / RELATION LIBRARY + DOMAIN-CIVILIZATION ATLAS + CIVILIZATIONAL LEARNING MAINLINE / HKB ACCESS CONTINUES AS CALIBRATION / CANONICAL HOLD
```

### 0.5 Post-#976 GRG programme routing — 2026-09-20

Author source:
`01_Source_Intuition/SRT_AUTHOR_GRG_FOUNDING_TELOS_GENERATIVE_NORMATIVITY_2026-09-20.md`

Programme architecture:
`Operations/Proposals/SRT_GENERATIVE_RELATIONAL_GRAMMAR_PROGRAMME_V0_1_2026-09-20.md`

GRG Framework v0.1:
`Operations/Proposals/SRT_GRG_RESEARCH_FRAMEWORK_V0_1_2026-09-21.md`

Civilizational Learning Architecture:
`Operations/Proposals/SRT_GRG_CIVILIZATIONAL_LEARNING_ARCHITECTURE_V0_1_2026-09-21.md`

Domain + Civilization Atlas seed:
`Operations/Proposals/SRT_GRG_DOMAIN_CIVILIZATION_ATLAS_SEED_V0_1_2026-09-21.md`

GRG Relation Record template:
`Operations/Templates/SRT_GRG_RELATION_RECORD_TEMPLATE_V0_1.md`

Generative-expectation second adjudication:
`01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GENERATIVE_EXPECTATION_TYPING_2026-09-20.md`

Distributed-neighbor extraction Pass 1:
`Operations/Audits/SRT_GRG_DISTRIBUTED_NEIGHBOR_EXTRACTION_PASS1_2026-09-20.md`

GRG-R1 bounded neuroscience transfer pilot result:
`Operations/Audits/SRT_GRG_R1_NEUROSCIENCE_TRANSFER_PILOT_RESULT_2026-09-20.md`

GRG-R1 O-criterion revision:
`Operations/Audits/SRT_GRG_R1_PRODUCTIVE_ADEQUACY_O_CRITERION_REVISION_PASS1_2026-09-20.md`

GRG-R1 target-blind spectral O1 result:
`Operations/Audits/SRT_GRG_R1_O_FEASIBILITY_SPECTRAL_FORMATION_RESULT_2026-09-20.md`

First RNN O3 causal-mediation result:
`Operations/Audits/SRT_GRG_R1_O3_CAUSAL_MEDIATION_RESULT_2026-09-21.md`

Stricter RNN O3 robustness result:
`Operations/Audits/SRT_GRG_R1_O3_V0_3_CAUSAL_MEDIATION_RESULT_2026-09-21.md`

Parallel O3 reconciliation:
`Operations/Audits/SRT_GRG_R1_O3_PARALLEL_EXECUTION_RECONCILIATION_2026-09-21.md`

HKB feasibility audit:
`Operations/Audits/SRT_GRG_R1_HKB_SOURCE_PROTOCOL_ACCESS_FEASIBILITY_2026-09-21.md`

HKB normalization reanalysis SourceCard:
`Materials/2026/SRC_2026_09_21_HKB_Post2020_Normalization_Reanalysis.md`

Existing-data access request package:
`Operations/Proposals/SRT_GRG_R1_HKB_EXISTING_DATA_ACCESS_REQUEST_PACKAGE_2026-09-21.md`

Public access-route verification:
`Operations/Audits/SRT_GRG_R1_HKB_PUBLIC_ACCESS_ROUTE_VERIFICATION_2026-09-21.md`

Continuation handoff:
`Operations/Handoffs/SRT_GRG_PROGRAMME_NEXT_SESSION_HANDOFF_2026-09-20.md`

Current programme reading:

```text
Selection = non-flat generative change / differentiation at programme level;
objects / symbols / laws = useful finite objectification slices, not final ontology floor;
unification target = generative relational grammar (GRG), not one replacement universal law;
civilizational "big data" = cross-position / cross-domain accumulated experience + extracted regularities;
mature neighbors = distributed contributors / reciprocal constraints by default;
SRT = self-revising grammar-learning architecture;
generative expectation = author-proposed source line of normativity;
full moral ought / universal value weights = OPEN;
canonical edit from this programme = NO.
```

Next sequence:

```text
Phase C internal red-team Pass 1 = COMPLETE:
`Operations/Audits/SRT_GRG_INTERNAL_RED_TEAM_PASS1_2026-09-20.md`

generative-expectation second adjudication = COMPLETE:
B+C / asymmetric-layered;
B = structural generative expectation;
C = formed-locus anticipatory realization with C0 embodied/enacted and C1 model-mediated forms.

distributed-neighbor extraction Pass 1 = COMPLETE.

GRG-R1 bounded neuroscience transfer pilot = COMPLETE / PILOT-NULL:
24/24 preregistered networks eligible;
decoder-defined context subspace failed the full targeted-withdrawal criterion;
decodability != causal retained organization by default;
semantic drift = NO;
canonical consequence = NONE.

productive-adequacy / O-criterion revision Pass 1 = COMPLETE.

target-blind O1 spectral-formation feasibility = COMPLETE / O1-SPECTRAL-PASS:
24/24 fresh-seed networks base-competent;
paired-seed CV history classification = 1.00;
within-pair permutation p = 0.000999;
target data used = NO.

O3 target-blind causal-mediation feasibility = COMPLETE / O3-CAUSAL-NULL:
first execution / one-time spectral transplant:
- 12/12 S donors + 12/12 D donors base competent;
- 12/12 recipient seeds complete;
- median C_SD = 0.001575;
- median C_S0 = 0.002794;
- both bootstrap primary conditions fail;
- target data used = NO.

RNN spectral O3 stricter robustness execution = COMPLETE / O3-CAUSAL-NULL:
- repeated early-learning singular-spectrum resets;
- equal-magnitude D-history spectral-direction control;
- fresh recipients 400..411;
- 12/12 recipient triplets valid;
- median C_SD = -0.002745;
- median C_SI = 0.010806;
- bootstrap 95% CI mean C_SD = [-0.038720, 0.016612];
- bootstrap 95% CI mean C_SI = [-0.017672, 0.051086];
- parameter-distance matching passed to numerical tolerance;
- target data used = NO.

Parallel execution reconciliation = COMPLETE:
- trunk v0.1 is the authoritative first O3 execution;
- stale-branch claim that v0.1 had not executed is superseded;
- #1001 is classified as a stricter independent robustness execution;
- both executions converge on RNN spectral R1c NULL / STOP;
- O4 remains blocked for this RNN spectral family.

cross-realization / source-fidelity audit Pass 1 = COMPLETE.

GRG-R1 programme burden split:

~~~text
R1a retained imprint = diagnostic / insufficient
R1b maintained scaffold = candidate generative organization
R1c causal re-entry = minimum causal core
R1d prospective transfer = stronger downstream burden
~~~

Current interpretation:
- toy decoder family = not R1c;
- toy spectral family = R1a PASS / R1c NULL;
- Bowler = source-native R1b/R1c positive pressure, exact causal object unresolved;
- synergetics = R1b/R1c pressure, source depth still insufficient.

source-fidelity extraction Pass 2 = COMPLETE.

Bowler:
- R1a PASS;
- R1b PASS under exogenous early-training clamp;
- R1c PASS as causal capacity;
- exact downstream dynamical mediator remains open.

Synergetics:
- R1b strong endogenous exemplar;
- R1c strong circular-causality exemplar;
- low-dimensional description alone is insufficient.

New required declaration:
- maintenance provenance;
- component/prior-process -> O evidence;
- O -> component/process evidence.

non-RNN R1c candidate-selection audit = COMPLETE.

selected bounded realization candidate:
HKB / human bimanual coordination dynamics.

Pre-result GRG decomposition:
- component limb state;
- external control parameter (cycling/pacing frequency);
- maintained relative-phase coordination O;
- mechanical perturbation operator;
- relaxation / stability / transition consequence.

maintenance provenance = MIXED / COUPLED.

Cross-realization refinement:
R1b/R1c formation may be historical/sedimented OR continuously regenerated; historical storage is not required for the minimum causal core.

HKB source/protocol-access feasibility audit = COMPLETE.

Result:
- full method / measurement reconstruction = PASS;
- GRG component/control/O/perturbation/consequence typing = PASS;
- 2020 normalization reanalysis creates a mandatory objectification guard;
- half-cycle / component-aware normalization = required future primary route;
- performed amplitude / frequency / oscillation-centre shift remain explicit component variables;
- public original 300-Hz raw trajectories = NO-GO / NOT LOCATED;
- participant-level supplementary outcomes = available but insufficient for trajectory-level R1c execution;
- historical author-held data route = evidenced by 2020 reanalysis;
- current authorized raw-data route = NOT ESTABLISHED.

New programme guard:
candidate maintained O must survive its measurement / normalization interface.

mainline next:
GRG Framework Construction
-> relation-library backfill from completed work
-> domain / civilization atlas expansion
-> civilizational case-record schema pressure tests
-> cross-domain relation extraction only after source-native records
-> calibration used to constrain candidates, not as the only queue.

parallel calibration:
HKB existing-data request has been sent to Harjo de Poel
-> wait for external response
-> if access is granted, freeze raw-data analysis charter before opening outcomes
-> no aggregate substitute / no new experiment / no simulation confirmation
-> R1d / O4 blocked.

canonical reassessment = HOLD.
```

Do not reopen a winner-style whole-package strongest-neighbor competition unless a later task makes an explicit comparative claim. Whole-package novelty / superiority / non-substitutability remain NOT ESTABLISHED.

### 1. 当前 programme state 与 owner 指针

```text
merge facts / sha / landing completion = §0 landing ledger above; not restated here.

prior bounded canonical landings:
#942 One / Selection-position formation owner
#940 Stable-ISP standing decoupling

current phase:
OLD-CANONICAL REVERSE AUDIT = RETYPED INTO BOUNDED OWNER-BY-OWNER LANDING
current One landing audit = `Operations/Audits/SRT_ONE_FORMATION_VERTICAL_RECONSTITUTION_CANONICAL_LANDING_SCOPE_2026-09-13.md`
post-One consistency review = `Operations/Audits/SRT_POST970_ONE_LANDING_WHOLE_SPINE_CONSISTENCY_REVIEW_2026-09-13.md`
post-Spine closeout / Selection handoff = `Operations/Audits/SRT_POST972_CANONICAL_TRUNK_CLOSEOUT_SELECTION_HANDOFF_2026-09-13.md`

cross-owner generative routing owner = `Core_Law/SRT_Generative_Ontology_Spine.md`
local One / Selection-position owner = `Core_Law/SRT_One_Formation.md` / post-#970 v1 landed
One Formation freeze class = A / EDIT-SAFETY ONLY / `draft`, `P1-candidate` UNCHANGED
Individuation freeze class = B / downstream hybrid / subject-entry and sigma reconstruction remain OPEN
freeze class != epistemic truth / P-level / theorem status / programme Level standing
canonical retype ledger = `Operations/Audits/SRT_CANONICAL_RETYPE_LEDGER.md` / noncanonical per-claim working surface
Stable ISP standing owner = P1-T06, stronger and separate
Bearer semantic route = formed One + P prospective self-indexing + E same-One prospective exposure -> Bearer
current E non-outsourcing counterfactual = consistency / exclusion test
independently applicable positive E admission / establishment criterion = OPEN
pre-#947 bearer / same-bearer mapping = LEGACY QUARANTINE / CLAIM-BY-CLAIM ONLY
P+E canonical routing strength != universal theorem / validated cross-domain classifier strength
formal cross-domain P+E N&S theorem = OPEN
Bearer -> actual 承担 / concern / agency / subject / cognition / phenomenality = separately OPEN
#957 author direction: Bearer => Concern NOT ESTABLISHED / Concern => Bearer NOT ESTABLISHED
#957 author direction: `Selection_O` = same primitive Selection under formed constraints, NOT second primitive
new Level 1 = NOT ASSIGNED
Level 2 = HOLD
HOLD EXIT REVIEW 2 = NOT TRIGGERED
scientific distinctiveness = NOT ESTABLISHED
whole-architecture non-substitutability = NOT ESTABLISHED
research_mode = U
```

### 2. Current controlling route

> `CANONICAL_REGISTRY.md §C` is the single owner of complete citation priority. The list below is a **task-local working read sequence**, not a second authority chain; cross-owner adjudication still resolves through Registry §C -> Generative Ontology Spine -> compatible local owners.

For current ontology / canonical-cleanup work, load in this order:

1. `01_Source_Intuition/SRT_AUTHOR_FINAL_ADJUDICATION_PR957_POSITION_RECURRENCE_CONCERN_2026-09-13.md` — latest merged author adjudication for the whole-skeleton landing direction; noncanonical
2. `Operations/Audits/SRT_POST957_OWNER_LANDING_SCOPE_AUDIT_2026-09-13.md` — bounded owner/edit-risk/landing sequence; noncanonical
3. `Core_Law/SRT_Generative_Ontology_Spine.md` — post-#959 cross-owner canonical order / non-identity / OPEN-gate owner
4. `CANONICAL_REGISTRY.md` — local owner routing after the spine
5. `Governance/SRT_CLAIM_LADDER.md` / `Governance/SRT_CLAIM_MODE_AUDIT.md` — claim hardness / demotion state
6. `Core_Law/SRT_L0_Metaphysics.md` / `Core_Law/SRT_One_Formation.md` / P1-T06 / d / Psi_f / T_dir — local owners, only within spine-compatible scope

Current cleanup / landing rule:

```text
#957 author checkpoint = landing constraint, not definition authority;
current canonical spine = definition/routing authority until edited;
compatible local definitions survive;
retiring an old claim does not require inventing a replacement theorem;
OPEN stays OPEN unless separately adjudicated;
land one Freeze-A owner at a time whenever practical.
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
cross-owner ontology OPEN gates      -> `Core_Law/SRT_Generative_Ontology_Spine.md` §9
One / Selection-position local OPEN  -> `Core_Law/SRT_One_Formation.md` §7
symbol / formalism hardening ledger  -> `Core/SRT_OPEN_TENSIONS.md`
collective higher-order realization  -> `Core_Law/SRT_Collective_Selection.md` §9
W1 / W2 audit labels                 -> `Operations/SRT_W1_W2_WRITEBACK_AUDIT_LABELS.md`
```

Two facts about the move that a reader of the owners alone would not see:

```text
former S04 + S12 = ONE record, now Spine §9 `Bearer <-> Concern / 关切`;
merging two records did not close the question — it stays OPEN.

Bearer admission threshold + Bearer <-> position stability
= PROVISIONAL routing in Spine §9 while Bearer canonical ownership is itself OPEN.
```

---

## Immediate routing

> **2026-09-21 GRG framework turn:** the programme mainline is now framework construction across domains and civilization. RNN/HKB remain calibration workstreams. No single pending dataset blocks the framework mainline. Canonical owners remain closed by default.

~~~text
1. GRG mainline = framework construction, relation library, domain/civilization atlas, generative-expectation/normativity architecture;
2. existing Domain Reconstruction Framework remains the source-native entry surface for mature disciplines;
3. GRG compares independently grounded generative burdens rather than replacing domain mechanisms;
4. Relation Record template = active schema for source-native claim -> evidence -> objectification -> GRG burden -> expectation -> failure -> transfer;
5. Civilizational Learning Architecture = active research layer for science, technology, institutions, markets, law, culture and historical experience;
6. civilizational inputs are evidence-typed; they are not treated as one homogeneous "big dataset";
7. first Atlas seed = D-PHY/D-LIFE/D-NEUR/D-COG/D-AI/D-TECH/D-ECON/D-SOC/D-LAW/D-ETH/D-EPI/D-CULT/D-HIST + HKB calibration;
8. first backfill records = RR-001 RNN adverse calibration, RR-002 HKB candidate, RR-003 Bowler source-native scaffold;
9. RNN spectral family = R1a PASS / R1c NULL / STOP; no tuning and no O4;
10. HKB = calibration workstream; source/protocol PASS, raw-data access pending;
11. first HKB data request has been sent to Harjo de Poel; any received raw outcomes remain unopened until a new charter;
12. HKB waiting state does NOT block GRG framework work;
13. first civilizational schema pass = COMPLETE: CIV-001 Internet standards, CIV-002 AMR, CIV-003 Montreal Protocol;
14. false-convergence Pass 1 = COMPLETE: one-relation compression rejected;
15. mature-source pressure Pass 1 = COMPLETE using Ostrom institutional analysis + niche-construction/ecological-inheritance literature;
16. X3 split = X3a articulated expectation / X3b operative expectation regime; written rule != operative institution;
17. X4 split = X4a reconstructed condition / X4b recursive feedback / X4c inherited reconstructed condition; long-term effect != feedback/inheritance;
18. CIV-004 Nepal irrigation = X3b positive source pressure; CIV-005 beaver ecosystem engineering = X4a positive but X4b not automatically paid;
19. historical mature-source checkpoint: X3a/X3b/X4a/X4b were M2 and X4c M1/M2 before later transfer / infrastructure passes; live M-status is superseded below;
20. live Relation Library owner = ESTABLISHED at Operations/GRG/SRT_GRG_RELATION_LIBRARY_V0_1.md;
21. negative-control discipline = PAID: formal-decoupling rejects X3b automatic admission; ecosystem-engineering-only evidence rejects X4b automatic admission;
22. M3/M4 distinction = EXPLICIT: M3 independent source-native relation match != M4 prospective transfer gain != scientific distinctiveness;
23. X3b -> Kubernetes NetworkPolicy = semantic/source match PASS; X3b promoted to M3; target-domain distinction already explicit, so M4 = NO / ABSORBED;
24. X4b -> Performative Prediction = non-biological semantic/source match PASS; X4b promoted to M3 and DOMAIN-LIMITED lifted; M4 = NO / ABSORBED;
25. X4b generic programme label = recursive reconstructed-field feedback; biological selective/viability feedback remains a specialization;
26. M4 relations = NONE; M5 relations = NONE; scientific distinctiveness = NOT ESTABLISHED;
27. M4-01 = COMPLETE / ABSORBED: X3b -> tool-using AI-agent authorization; no duplicate execution;
28. M4-02 = COMPLETE / ABSORBED: X4b -> road-capacity induced-demand feedback; charter frozen before transport source audit;
29. transport target-domain pre-ownership = STRONG: fixed vs variable demand modelling, generalized-cost response, induced demand, land-use/trip feedback and appraisal already standard;
30. M4-02 duplicate transport simulation = STOP; M4 remains NONE;
31. M4-E0 absorption-before-execution rule = REPLICATED across two distinct relations / target domains;
32. framework-adequacy audit after repeated absorption = COMPLETE: M4 remains strict target-domain transfer criterion but is not the sole GRG framework adequacy axis;
33. Cross-Domain Burden Matrix v0.1 = ACTIVE at Operations/GRG/SRT_GRG_CROSS_DOMAIN_BURDEN_MATRIX_V0_1.md;
34. Generative Expectation Ledger v0.1 = ACTIVE at Operations/GRG/SRT_GRG_GENERATIVE_EXPECTATION_LEDGER_V0_1.md;
35. Position / Horizon Conflict Ledger v0.1 = ACTIVE at Operations/GRG/SRT_GRG_POSITION_HORIZON_CONFLICT_LEDGER_V0_1.md;
36. X6 multi-position consequence divergence = RETYPED / REMOVED FROM RELATION QUEUE; PH is a cross-cutting analysis burden with NO M-status;
37. PH guard = position/horizon sensitivity != evidenced directional conflict; conflict must be source-paid case by case;
38. CIV-006 combined-sewer long-duration infrastructure pass = COMPLETE; freeze preceded dedicated source inspection;
39. CIV-006 source-native topology = historical reconstruction -> persistent/maintained material carrier -> successor cohort inherits field -> later operation/compliance/retrofit possibilities are conditioned;
40. X4c inherited reconstructed condition = M3 PASS; ecological P-ECO + infrastructure P-MAT cross-domain semantic invariance;
41. X4c carrier-explicit admission = ACTIVE: inheritance requires carrier + successor cohort + changed later possibility structure; persistence/age/sunk cost alone do not pay it;
42. inheritance provenance metadata = P-MAT / P-ECO / P-INST / P-INFO; historical P-MIXED inheritance kind is retired; provenance metadata != relation identity;
43. IPv4 -> IPv6 installed-base stress = COMPLETE; X4c PASS / remains M3;
44. precedent / stare-decisis carrier stress = COMPLETE; X4c PASS / remains M3;
45. Inheritance Carrier Architecture v0.1 = ACTIVE at Operations/GRG/SRT_GRG_INHERITANCE_CARRIER_ARCHITECTURE_V0_1.md;
46. Carrier Architecture Adequacy Pass 1 = COMPLETE / PRODUCTIVE;
47. adequacy verdict = CARRIER ARCHITECTURE RETAIN; PROVENANCE-KIND-FIRST NARROW; CAUSAL-ROLE-FIRST ACTIVE;
48. historical P-MIXED provenance kind = RETIRED; multi-component architecture is represented directly;
49. bounded Carrier Role Census Pass 1 = COMPLETE at Operations/Audits/SRT_GRG_INHERITANCE_CARRIER_ROLE_CENSUS_PASS1_2026-09-21.md;
50. minimal Inheritance Carrier Role Library v0.1 = EARNED / ACTIVE at Operations/GRG/SRT_GRG_INHERITANCE_CARRIER_ROLE_LIBRARY_V0_1.md;
51. CORE reusable roles = SUBSTRATE [3 paid records], PAYLOAD [2], INTERFACE [2];
52. SPECIALIZED reusable role = AUTHORITY [1 paid precedent record + strong binding/persuasive and first-impression near-controls]; broad recurrence OPEN;
53. ENACTMENT = CASE-LOCAL / NARROW; not admitted to Role Library v0.1;
54. REPRODUCTION = OPEN / NOT PAID; not admitted to Role Library v0.1;
55. MAINTENANCE = RETYPED from component role to architecture persistence process;
56. persistence process values = PASSIVE-PERSISTENCE / ACTIVE-MAINTENANCE / RECURRENT-REPRODUCTION / MIXED / OPEN;
57. provenance metadata = P-ECO / P-MAT / P-INFO / P-INST; metadata do not receive M-status;
58. carrier record = component + provenance metadata + reusable/source-local causal role + role evidence/near-control + component status + persistence process + architecture sufficiency;
59. CIV-006 paid component roles = P-MAT/SUBSTRATE+INTERFACE; persistence process = ACTIVE-MAINTENANCE / MIXED; modern regulation remains S-LEGAL/S-ORG expectation source, not carrier;
60. IPv4/IPv6 paid roles = P-INFO/PAYLOAD + P-MAT/SUBSTRATE+INTERFACE; P-INST proposed coordination role = PRESENT / ROLE-OPEN; source-local ENACTMENT = NARROW;
61. precedent carrier = MULTI-COMPONENT with P-INFO/PAYLOAD + P-INST/AUTHORITY both COMPONENT-ROLE-PASS;
62. reusable near-controls = greenfield vs installed-base; binding vs persuasive; controlling precedent vs case of first impression;
63. component-role PASS != architecture sufficiency automatically; unsupported components cannot strengthen X4c admission;
64. X3b current operative rule/compatibility != X4c inherited successor field;
65. expectation provenance, carrier architecture and PH remain separate analysis surfaces;
66. CIV-005 Role Library negative / borderline test = COMPLETE / NEGATIVE PRODUCTIVITY PASS at Operations/Audits/SRT_GRG_CIV005_CARRIER_ROLE_LIBRARY_NEGATIVE_PASS1_2026-09-21.md;
67. CIV-005 X4c = NOT ADMITTED BY CURRENT CASE EVIDENCE; this does not deny real-world beaver ecological inheritance;
68. CIV-005 P-ECO modified environment / SUBSTRATE = ROLE-CANDIDATE / PRE-ADMISSION, not COMPONENT-ROLE-PASS;
69. CIV-005 missing X4c burden = declared successor boundary + field transmission across that boundary + successor enters under F + inherited successor possibility change;
70. general ecological-inheritance evidence cannot retroactively pay beaver-specific admission by analogy;
71. new admission-order guard = carrier-role plausibility != X4c admission; relation-level successor/transmission burden must be paid before COMPONENT-ROLE-PASS;
72. positive-record X4c admission-order consistency audit = COMPLETE / PASS at Operations/Audits/SRT_GRG_X4C_POSITIVE_ADMISSION_ORDER_CONSISTENCY_PASS1_2026-09-21.md;
73. positive admission-order results = ecological inheritance PASS; CIV-006 STRONG PASS; IPv4/IPv6 PASS; precedent PASS / CO-EVIDENCED BUT NON-CIRCULAR;
74. positive X4c downgrades = NONE; carrier-role circular bootstrap detected = NONE;
75. admission order = LOGICAL / EPISTEMIC, not mandatory artifact chronology; same-source relation+role evidence is allowed if relation-level successor/transmission evidence is independently articulable without the role label;
76. IPv4 and precedent SourceCard carrier summaries were synchronized to current role-census schema; source-native evidence unchanged;
77. X4c carrier-subprogramme local-closure audit = COMPLETE at Operations/Audits/SRT_GRG_X4C_CARRIER_SUBPROGRAMME_LOCAL_CLOSURE_PASS1_2026-09-21.md;
78. X4c carrier-subprogramme verdict = LOCAL CLOSE;
79. carrier vocabulary for current evidence = FROZEN; new carrier-case / provenance-category / reusable-role hunt = STOP BY DEFAULT;
80. reopen triggers = internal contradiction / source-native new-role pressure / role collapse / carrier-expectation conflation / material X4c relation revision;
81. broader-GRG next-burden selection = COMPLETE; selected Generative Expectation provenance / locus / normative-comparison adequacy;
82. Generative Expectation adequacy charter v0.1 = FROZEN at Operations/Proposals/SRT_GRG_GENERATIVE_EXPECTATION_ADEQUACY_CHARTER_V0_1_2026-09-21.md;
83. Generative Expectation adequacy Pass 1 = PRODUCTIVE SPLIT at Operations/Audits/SRT_GRG_GENERATIVE_EXPECTATION_ADEQUACY_PASS1_2026-09-21.md;
84. live expectation source/provenance = S-MAT / S-TECH / S-LEGAL / S-ORG / S-NORM / S-BIO;
85. live expectation locus/mode = B-STRUCTURAL / C0-ENACTED / C1-MODEL / OBS-MODEL;
86. historical E-MODEL as provenance = RETIRED; external analyst / evaluator model routes to OBS-MODEL unless formed-locus C1 is separately paid;
87. historical E-MIXED as provenance = RETIRED; explicit source-layer lists required;
88. indexed G-stronger / G-weaker requires explicit relation/objective + position/locus + scale/grain + horizon + comparison dimension;
89. Generative Expectation negative productivity Pass 1 = PASS at Operations/Audits/SRT_GRG_GENERATIVE_EXPECTATION_NEGATIVE_PRODUCTIVITY_PASS1_2026-09-21.md;
90. RNN negative control = O1 prediction/classification can coexist with R1c O3 NULL; OBS-MODEL != B/C1 and no indexed normativity follows;
91. precedent negative control = S-LEGAL+S-ORG B PASS and indexed legal force PASS, but binding != morally correct / just / legitimate;
92. expectation-schema consistency census = ACTIVE; migrate live GRG routing only, preserve historical audit notation where appropriate;
93. periodic M4 only when target ownership is genuinely uncertain;
94. M4 relations = NONE; M5 = NONE; scientific distinctiveness = NOT ESTABLISHED;
95. author generative expectation = B+C asymmetric/layered; indexed normativity remains distinct from full moral legitimacy;
96. do not automatically open canonical L0/One/Bearer/d/Concern/Agency/phenomenality/normativity owners;
97. preserve Level 2 HOLD, no new Level 1, no scientific-distinctiveness promotion;
98. do not restart winner-style strongest-neighbor novelty audit;

~~~

## Historical navigation

Pre-#931 snapshot:

`Operations/Status_History/SRT_STATUS_2026-09-11_PRE_PR931_ROOT_SNAPSHOT.md`

Byte-preserving raw snapshot:

`Operations/Status_History/SRT_STATUS_2026-09-11_PRE_PR931_ROOT_SNAPSHOT.txt`

Other historical handoffs remain under `Operations/Status_History/`.

When historical files conflict, do not resolve by date alone: separate current canonical K, explicit author A, historical B, machine C and open D; apply explicit supersession records within their declared scope.
