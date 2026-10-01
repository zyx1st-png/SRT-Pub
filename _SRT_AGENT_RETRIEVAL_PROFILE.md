---
id: SRT-AGENT-RETRIEVAL-PROFILE
type: retrieval_profile
tags: [AI, Agent, Retrieval, Context, Codex, ChatGPT, ClaudeCode, BookWriting]
status: active
layer: meta
epistemic_layer: meta
claim_mode: navigation
canonical: false
dependency: [SRT-AI-START, SRT-INDEX, SRT-CONTEXT-ROUTER, SRT-LONGFORM-SPLITS]
ai_role: context_expansion_contract
ai_priority: 2
updated: 2026-09-29
---

# SRT Agent Retrieval Profile

> Purpose: prevent two opposite retrieval failures when this repository is used by Codex, ChatGPT, Claude Code, or another agent:
>
> 1. valuable non-canonical material being ignored merely because it lacks definition authority;
> 2. archived or historical material being mistaken for the current construction source merely because it ranks highly in keyword search.
>
> This file does not define SRT. It tells agents how to retrieve enough context while keeping authority, currentness, and historical value separate.

---

## 0. Three Distinct Axes

SRT retrieval must distinguish three questions:

| Axis | Question | Examples |
|---|---|---|
| Authority | Can this file define or override SRT terms? | canonical anchors, claim ladder, symbol table |
| Retrieval value | Should this file be read for the current task? | source intuition, bridge files, evidence cards, book notes |
| Currentness | Is this the active construction source for the task? | current `Drafts_26Q/` chapter vs `Archive_52Chapter/` historical draft |

`canonical: false` means **not a definition authority**. It does not mean low value, irrelevant, or safe to ignore.

`status: archived` or an archive path means **not current construction authority**. It may still have high historical or comparative value, but it must not displace the active source.

Search rank, keyword density, file version suffixes, and old chapter numbering do not establish authority or currentness.

### 0.1 Author-accepted / boundedly continued machine analysis

Detailed author semantics and exceptions are owned by:

`01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CONTINUE_DIRECTIONAL_ACCEPTANCE_2026-09-24.md`.

Retrieval rule:

~~~text
accepted or boundedly continued
+
non-superseded machine analysis
-> must remain routeable
-> must be consulted when the relevant topic enters task scope
-> authority may remain M
~~~

This is **not** a universal preload rule. Fresh sessions still obey bounded retrieval and STATUS routing. A historical accepted-analysis package is loaded when its burden becomes relevant, not merely because it exists.

The labels `parked`, `downstream`, `companion`, `support`, and `canonical: false` do **not** by themselves lower retrieval value or justify skipping accepted / relevant reasoning. Current retrieval priority may be demoted only by an explicit narrowing such as `EXPLORATORY`, `LOCAL_ONLY`, `SUPERSEDED`, `REJECTED`, `RETIRED`, or a later controlling adjudication.

Implementation status: bounded re-entry mapping is routed through `_SRT_CONTEXT_ROUTER.md §20`. `Operations/Audits/SRT_ACCEPTED_CONTINUED_PRE0728_REENTRY_AUDIT_2026-09-24.md` covers the recorded 2026-07-09 -> 2026-07-27 ChoiceMap / Concern / Ghost upstream segment; `Operations/Audits/SRT_ACCEPTED_CONTINUED_MACHINE_ANALYSIS_REENTRY_AUDIT_2026-09-24.md` covers the reviewed 2026-07-28 -> 2026-08-10 ChoiceMap segment plus selected later pre-GRG re-entry work; the 2026-09-20 -> 2026-09-23 GRG period is delegated to `Operations/Audits/SRT_GRG_ACCEPTED_MACHINE_ANALYSIS_CONTINUITY_AUDIT_2026-09-23.md`. Material before 2026-07-09, the 2026-07-12 cross-scale sibling branch, and other lower-priority chains remain not exhaustively audited. Absence from these maps must not be read as evidence of low retrieval value.

### 0.2 Level-preserving comparison / fresh-session subtraction guard

When a task compares SRT with a neighboring theory/model, evaluates novelty,
performs subtraction / no-gain analysis, or prepares publication positioning,
classify the target before drawing a replacement conclusion:

~~~text
P0  primitive Selection / O0 burden
P1  cross-level generative-organization burden
P2  formed whole-field / Gate / selectable-organization burden
P3  retained historical efficacy / writeback
P4  event / state / action implementation
~~~

These labels are retrieval-level comparison types, not new canonical ontology
levels.

A rival that preserves only P3/P4 can absorb only the corresponding P3/P4
explanatory job. It cannot by that result alone establish that P0/P1/P2 is
dispensable. Any `NO SRT GAIN`, `SOURCE-OWNED`, `absorbed`, or
`Selection not needed` conclusion must state the exact target and verify
same-target preservation.

Controlling source:
`01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CROSS_LEVEL_SELECTION_FRESH_SESSION_GUARD_2026-10-01.md`.

For the active cognition programme, also retrieve:
`Operations/Audits/SRT_PASS19_VERTICAL_STRUCTURE_ACTIVE_SELECTABLE_SPACE_CORRECTION_2026-09-10.md`.

Guard:

~~~text
history-conditioned selectability
= downstream consequence

history / consequence writeback
= one route or subtype of recursive reconstitution

active construction / cross-level reconstruction
of selectable organization
= broader controlling burden

downstream equivalence
-/> upstream subtraction
~~~



---

## 1. Mandatory Agent Contract

After the minimal bootstrap, an agent must classify the task before deciding context depth.

Fresh-session read order is owned by `AGENTS.md §Session Start`. Do not maintain a competing bootstrap list here. For the STATUS bootstrap step, consume the current-state surface through §0–§2 (landing ledger, programme state / owner pointers, controlling route); later STATUS theory/history sections are conditional context rather than universal fresh-session input.

Select only the applicable profile and its task-relevant references. Ordinary Git, tooling or typo work does not become a theory task merely because this is an SRT repository. Reuse already-read unchanged context; old audits and full-domain maps are conditional, not universal prerequisites.

Compression must not erase execution semantics. If an owning workflow or skill defines an ordered gate, stop condition, failure behavior or edit boundary, follow it explicitly rather than reconstructing a shorter substitute from model capability.

After the minimal guard files are loaded:

1. Identify the task profile below.
2. Load authority anchors needed for definitions.
3. Load current-status or active-construction routing needed for the task.
4. Load retrieval context needed for depth.
5. If the route touches a long file, use `LONGFORM_SPLITS.md` and the relevant split README first.
6. For substantive conceptual or cross-domain SRT questions, use `_SRT_CONTEXT_ROUTER.md`.
7. Check open tensions or claim-status boundaries before making strong claims.
8. State whether each important file is being used as canonical, current manuscript, bridge, support, evidence, backstage context, historical material, or operations provenance.

Do not answer a substantial theory, book, or domain question from only the minimal bootstrap files.

---

## 2. Task Profiles

### 2.1 Quick Orientation

Use when the user asks for a short definition, reminder, or status.

Read:

1. `SRT_AI_START.md`
2. `CANONICAL_REGISTRY.md`
3. `_SRT_SYMBOL_TABLE.md`
4. the relevant canonical anchor if the term is `d`, `Psi_f`, `T_dir`, `L0/L1/L2`, or `G_theta`

Output rule:

- Keep authority clear.
- Do not pull bridge speculation unless requested.

### 2.2 Theory Advancement

Use when the user asks to develop, harden, test, critique, extend, or repair SRT.

Read in this order, stopping when the active task is adequately grounded:

1. current `STATUS.md` §0–§2 for programme state, current owner and route;
2. the latest relevant author adjudication / bounded work package named by current provenance when substantive meaning is in play;
3. `CANONICAL_REGISTRY.md`;
4. `Core_Law/SRT_Generative_Ontology_Spine.md` when the task touches ontology order, formation, position/perspective/Bearer routing, OPEN gates or old-canonical cleanup;
5. the compatible local owner(s) for the target concept;
6. `Governance/SRT_CLAIM_LADDER.md` and `Governance/SRT_CLAIM_MODE_AUDIT.md` when claim hardness matters;
7. `_SRT_CONTEXT_ROUTER.md`, `_SRT_DEEP_THEORY_MAP.md`, route Primary files and route Secondary files only to the depth required by the question;
8. `Core/SRT_OPEN_TENSIONS.md` and the relevant coverage index when unresolved edges or missing support files matter.

The 2026-09-05 author-reentry correction and reconstruction amendment remain important programme/governance context, but they are **conditional rather than automatic prefaces to every current owner edit**. Load them when scope/pace, collaboration, U/N-mode, Domain Reconstruction, deep-well/HOLD gates or programme interpretation is actually at issue. Current bounded owner work should not be forced to traverse the full older programme corpus before reading its live adjudication and owner.

Important:

### 2026-09-27 cognition CURRENT NEXT retrieval note

When STATUS routes the active task to the pre-object generative orientation of cognition programme, load these first:

1. `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_PRIMITIVE_SELECTION_ANTI_TAUTOLOGY_STOP_AND_NEXT_ROUTING_2026-09-27.md` — current author closeout + next routing;
2. `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_PREOBJECT_GENERATIVE_ORIENTATION_COGNITION_2026-09-26.md` — root author target;
3. `Operations/Proposals/SRT_PREOBJECT_GENERATIVE_ORIENTATION_COGNITION_RESEARCH_PROGRAM_2026-09-26.md` — active neutral-science execution owner;
4. `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CROSS_LEVEL_SELECTION_FRESH_SESSION_GUARD_2026-10-01.md` + `Operations/Audits/SRT_PASS19_VERTICAL_STRUCTURE_ACTIVE_SELECTABLE_SPACE_CORRECTION_2026-09-10.md` — controlling level-preservation / active-selectable-space guard; history/writeback is downstream and must not be promoted into the programme's whole target;
5. `Operations/Proposals/SRT_FACING_HUMAN_IN_LOOP_GENERATIVE_CONFRONTATION_METHOD_V0_3_2026-09-27.md` + `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_FACING_V03_POST_REVIEW_CORRECTIVE_2026-09-27.md` — mandatory only when neutral results are promoted into SRT / GRG recut or cross-domain Facing claims;
6. `Operations/Audits/SRT_L0_FACING_FIELD_H1_H2_H3_LEVEL_RECLASSIFICATION_2026-09-26.md` — H1/H2/H3 level discipline + E1-E4 evidence ladder;
7. when music / temporal phenomenology / completion / unfinishedness / `foreground_phen` enters scope: `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_MUSIC_CHANGE_PHENOMENAL_VERTICAL_GENERATION_2026-09-29.md` + `Operations/Proposals/SRT_MUSIC_PHENOMENAL_VERTICAL_GENERATION_BOUNDED_RESEARCH_ROUTE_2026-09-29.md` — bounded companion only, no second CURRENT NEXT;
8. preformal-coherence source/programme only as a downstream behavioral assay;
9. strong local-update / latent-state / representation-learning baselines before any SRT interpretation.

Retrieval guard:

~~~text
neutral cognition science first;
SRT interpretation downstream / optional;
toy simulation is not the first move;
whole-field language must earn predictive / causal / recursive value;
positive cognition result != primitive Selection / O0 proof;
history/writeback = one downstream route of recursive reconstitution, not its definition;
downstream implementation equivalence -/> upstream / primitive subtraction;
rival/no-gain conclusions must preserve and name the same comparison target;
neutral empirical work may proceed before author Facing confrontation;
SRT / GRG recut promotion -> v0.3 blind-first FR-AUTH + FR-ADV;
new experiment / preregistration or formal domain-reconstruction promotion
-> independent FR-ADV required;
HP-B remains frozen / read-only;
canonical edit = NO.
~~~

### Facing reconstruction retrieval note — v0.2 historical pass / v0.3 future reconstruction guard


When STATUS routes the active task to the 2026-09-26 Facing reconstruction / simplification pass, load these before broad historical or neighbor material:

1. `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_PR1069_FACING_METHOD_CORRECTIVE_2026-09-26.md` — controlling author corrective for the historical bounded pass;
2. `Operations/Proposals/SRT_FACING_RECONSTRUCTION_SIMPLIFICATION_METHOD_V0_1_2026-09-26.md` — historical v0.2 execution owner for #1071;
3. `Operations/Audits/SRT_FACING_COMPLETION_SCOPE_AUDIT_2026-09-27.md` — prevents 8/8 + 7/7 from being read as full historical / cross-domain reconstruction;
4. for any **new stronger cross-domain / domain-recut work**, switch to `Operations/Proposals/SRT_FACING_HUMAN_IN_LOOP_GENERATIVE_CONFRONTATION_METHOD_V0_3_2026-09-27.md` and `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_FACING_V03_POST_REVIEW_CORRECTIVE_2026-09-27.md`;
5. `Operations/Audits/SRT_PR1068_FACING_RECONSTRUCTION_METHOD_INDEPENDENT_CONTENT_REVIEW_2026-09-26.md` — historical independent review provenance;
6. `_SRT_SYMBOL_TABLE.md` aspect boundary + `Core_Law/SRT_L0_Metaphysics.md` + `Core_Law/SRT_Generative_Ontology_Spine.md` — canonical controls;
7. only then the target-specific owner / source-native neighbor files needed by the declared scope.

Retrieval guard:

~~~text
Facing = execution alias for the canonical analytic-aspect rule;
do not harden it as a new layer taxonomy;
v0.2 / #1071 = bounded historical cleanup, not full reconstruction;
new FACE-REC work = v0.3 blind-first FR-AUTH -> FR-ADV;
author intuition may remain PREFORMAL at generation, but claim promotion needs a differentiating consequence;
future FACE-REC does not automatically reopen the #1074 anti-tautology STOP;
HP-B Bearer / Psi_f / consciousness were read-only in the #1071 pass.
~~~

- Use canonical anchors to prevent overclaiming.
- Use route, bridge, domain, and hardening files to avoid shallow answers.
- If a support file is `canonical: false`, mark it as support rather than skipping it.
- If a new intuition may alter canonical content, first route it through source-intuition / bridge / open-tension hardening, then apply `Governance/SRT_EDIT_PROTOCOL.md` before a C-class edit.

### 2.3 Book Writing

Use when the user asks to read, write, revise, structure, polish, continue, compare, audit, or write back to 《从存在到秩序》.

#### Mandatory currentness route

Follow `AGENTS.md §Book-Writing Hard Guard`: book status → active manifest → selected active primary, before archive comparison. Writing/revision/translation and literary or structural review also load `01_Source_Intuition/BOOK/TASTE.md`.

After resolving the active primary, add only context required by the task:

- Orientation: `README.md`, `START_HERE.md`, `01_Source_Intuition/README.md`, `01_Source_Intuition/INDEX.md`.
- Architecture: `01_Source_Intuition/BOOK/BOOK_ARCHITECTURE_MAP_5ACT_2026-06-24.md`.
- Wording: `01_Source_Intuition/BOOK/BOOK_TERMINOLOGY_SIMPLIFICATION_GUIDE_2026-06-03.md`.
- Historical sequence: `01_Source_Intuition/BOOK/BOOK_ARCHITECTURE_MAP_2026-06-03.md` (retained content cards only), `BOOK_PROBLEM_CHAIN_REWRITE_2026-05-21.md` and `BOOK_CHAPTER_CARDS_2026-05-22.md` under the book directory.
- Omission/continuity audits: `90_Backstage/Restructure_2026/BOOK_PROJECT/repository_material_inclusion_matrix.md` and relevant backstage notes.
- Accuracy: relevant formal anchors, never as prose-style authority.

#### Archive hard guard

`01_Source_Intuition/BOOK/Archive_52Chapter/` and `Archive_Meta/` are historical routes.

An agent must not:

- open an archived file before loading the active primary when the task concerns current book content;
- use an archived file as the first or sole source for a current chapter answer;
- infer currentness from search rank, terminology density, old version suffixes, or old chapter numbers;
- copy archived prose directly into a current draft patch.

An archived file may be used only after the current primary is loaded, and only for:

- historical comparison;
- provenance tracing;
- controlled recovery of examples or formulations;
- omission audits against the current chapter.

When archive material is used, label it explicitly as historical and name the current file it is being compared with.

Writing rules:

- Do not turn the book into canonical documentation.
- Use source-intuition files for force.
- Use formal anchors for accuracy.
- Use backstage notes for continuity.
- Use bridge and evidence files as shadow support, not proof-dumps.
- Current book prose must be re-derived against the current five-act architecture rather than restored wholesale from the old 52-chapter route.

### 2.4 Source-Intuition / Philosophical Prose

Use when the task asks for founding intuition, worldview framing, philosophical explanation, or non-technical exposition.

Read:

1. `01_Source_Intuition/README.md`
2. `01_Source_Intuition/CORE_REVERSALS.md`
3. `Core_Law/SRT_L0_Metaphysics.md`
4. `Core_Law/SRT_Selection_Argument.md`
5. `Core_Law/SRT_Core_Text_CN_Euclid.md` when Chinese source style matters
6. `Manifesto/SRT_MANIFESTO.md` only when the task is public-facing or worldview-facing

Boundary:

- Source force is allowed.
- Definition replacement is not allowed.

### 2.5 Domain Deep Dive

Use when the task asks about AI, neuroscience, physics, philosophy, spirituality, social theory, ethics, politics, experiments, or adjacent theories.

Read:

1. `_SRT_CONTEXT_ROUTER.md`
2. `_SRT_DEEP_THEORY_MAP.md`
3. the relevant domain README or compact registry
4. the route Primary files
5. the route Secondary files if needed
6. the relevant split README when the owner file is long
7. the relevant claim-status file when the domain has one

Domain starter map:

| Domain | Start |
|---|---|
| AI | `AI/README.md`, `AI/AI_POSITIONING_NOTE.md`, `AI/SRT_AI_Claim_Status.md` |
| Neuroscience | `Neuroscience/README.md`, `Neuroscience/SRT_Neuroscience_Claim_Status.md`, `Neuroscience/NEUROSCIENCE_COMPACT_REGISTRY.md` |
| Physics | `Physics/README.md`, `Physics/PHYSICS_COMPACT_REGISTRY.md`, `Physics/SRT_Physics_Claim_Status.md` |
| Philosophy | `Philosophy/README.md`, `Philosophy/SRT_Philosophy_Claim_Status.md`, `Philosophy/_PHILOSOPHY_MACHINE_INDEX.md`, `Philosophy/00_READ_FIRST_Philosophy_Hardening_Soft_Spots.md` |
| Spirituality | `Spirituality/SPIRITUALITY_COMPACT_REGISTRY.md`, `Spirituality/SRT_Spirituality_Claim_Status.md`, `Spirituality/_SRT_Spirit_Axioms.md` |
| External convergence | `04_External_Convergence/README.md`, `04_External_Convergence/EVIDENCE_INDEX.md`, `04_External_Convergence/EVIDENCE_GRADING.md` |

### 2.6 Material Fusion

Use when the user triggers `材料`, `材料裁决`, or asks to integrate an external paper, article, dataset, or claim.

Read:

1. `Operations/_SRT_MATERIAL_PIPELINE.md`
2. `Operations/_SRT_MATERIAL_LOG.md` or `Operations/Material_Log/README.md`
3. `Operations/_SRT_MATERIAL_ADJUDICATION_WORKFLOW.md` when second-round adjudication is needed
4. `_SRT_CONTEXT_ROUTER.md`
5. the target domain canonical and bridge files
6. the relevant registry or index files

Rule:

- A-class body writeback must be de-materialized into native SRT prose.
- SourceCard, PatchNote, Hook, and Operations records are retrieval support, not canonical definitions.

### 2.7 Public Release / External Onboarding

Use when the user asks for one-pagers, essays, talks, public explanations, summaries, or external-facing framing.

Read:

1. `README.md`
2. `05_Public_Release/README.md`
3. `05_Public_Release/PUBLIC_INDEX.md`
4. `05_Public_Release/PUBLIC_GUARDRAILS.md`
5. `SRT_Navigation_Map.md`（人类阅读总入口；原 `SRT_Public_Reading_Guide.md` 的分轨阅读已并入，2026-07-20）
6. `video/SRT_Video_Claim_Status.md` when scripts, talks, or cinematic drafts are involved
7. `01_Source_Intuition/CORE_REVERSALS.md`
8. `Manifesto/SRT_MANIFESTO.md` when worldview tone is needed
9. formal anchors only as guardrails

Rule:

- Public force is welcome.
- Public phrasing does not become canonical.

### 2.8 Governance / Repository Engineering

Use when the user asks to improve structure, indexes, agent behavior, split files, frontmatter, status, or workflow.

Read:

1. `Operations/README.md`
2. `Governance/README.md`
3. `Governance/SRT_CANONICAL_FREEZE.md`
4. `Governance/SRT_EDIT_PROTOCOL.md`
5. `LONGFORM_SPLITS.md` and `Operations/Archive_Records/Large_File_Audit_2026-05-09.md` when long-file routing or historical size debt is relevant
6. `_SRT_INDEX.md` when entrypoint/registry relations change
7. `_SRT_CONTEXT_ROUTER.md` only when conceptual routing changes

Rule:

- Improve retrieval without smuggling new theory.
- Add governance or operations records when the change affects agent behavior.
- Prefer machine-checkable routing and CI checks over another prose-only policy layer.

---

## 3. Connector-Safe Reading Rules

When using GitHub, ChatGPT repo connectors, Claude Code context tools, or any tool that may truncate or rank files:

1. Detect truncated results; fetch missing portions before relying on their contents.
2. For long files, check `LONGFORM_SPLITS.md`; the historical large-file audit is optional context for routing gaps.
3. Prefer the split README for long owner files.
4. Read the owner file when exact wording or local line context is needed.
5. Treat search as discovery, not authority resolution.
6. For book tasks, resolve each search hit through `BOOK_ACTIVE_MANIFEST.json` before treating it as current.
7. If a book search hit is under `Archive_52Chapter/` or `Archive_Meta/`, load the active primary first and use the hit only as historical comparison.

Split shards are not independent authorities. They are high-value connector-safe copies.

---

## 4. Future Frontmatter Guidance

When adding or normalizing files, separate authority, retrieval value, and currentness:

```yaml
canonical: false
authority_level: bridge_support
retrieval_priority:
  theory_advancement: high
  book_writing: medium
active_construction: false
superseded_by:
  - path/to/current/file.md
```

Do not use `canonical: true/false` as a retrieval filter.

For existing files without these fields, infer retrieval priority from indexes, router entries, split registries, task profile, current-status files, and active manifests.

---

## 5. High-Value Non-Canonical Areas

Do not ignore these merely because they are not canonical:

- `01_Source_Intuition/` for founding force and book style.
- `01_Source_Intuition/BOOK/Drafts_26Q/` for current manuscript prose.
- `01_Source_Intuition/BOOK/Archive_52Chapter/` for explicitly labelled historical comparison only.
- `90_Backstage/Restructure_2026/BOOK_PROJECT/` for book continuity, style, and inclusion decisions.
- `Bridge/` for adjacent theory translation.
- `03_Bridges/` for **SRT's own cross-domain frameworks**, not only adjacent-theory translation. Several files there (T-B entropy/disturbance, T-D choice generation conditions, T-E dissipative structures, MSD selection dynamics) carry P2-P3 machinery that changes concrete judgments and has no equivalent in the canonical layer. Consult it for any "does this count as a selection / a real choice / an ordering event?" question, not just when comparing SRT to a neighboring theory. Entry: `03_Bridges/BRIDGE_INDEX.md`; for selection-event judgments start at `03_Bridges/SRT_Selection_Event_CompactCore.md`.
- `04_External_Convergence/` for evidence, proxy, contradiction, and pressure.
- `LONGFORM_SPLITS.md` and split directories for connector-safe full-text retrieval.
- `_SRT_*_COVERAGE_INDEX.md` files for valuable but easy-to-miss files.
- `Operations/Material_Log/` for material provenance and integration history.
- domain claim-status files for anti-overclaiming boundaries.
