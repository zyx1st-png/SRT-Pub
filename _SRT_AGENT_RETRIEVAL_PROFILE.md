---
id: SRT-AGENT-RETRIEVAL-PROFILE
type: retrieval_profile
tags: [AI, Agent, Retrieval, Context, Codex, ChatGPT, ClaudeCode, BookWriting]
status: active_v1
layer: meta
epistemic_layer: meta
claim_mode: navigation
canonical: false
dependency: [SRT-AI-START, SRT-INDEX, SRT-CONTEXT-ROUTER, SRT-LONGFORM-SPLITS]
ai_role: context_expansion_contract
ai_priority: 2
---

# SRT Agent Retrieval Profile

> Purpose: prevent valuable non-canonical material from sleeping when this GitHub repository is used by Codex, ChatGPT, Claude Code, or another agent for theory advancement and book writing.
>
> This file does not define SRT. It tells agents how to retrieve enough context without confusing retrieval value with canonical authority.

---

## 0. Core Distinction

SRT uses two different axes:

| Axis | Question | Examples |
|---|---|---|
| Authority | Can this file define or override SRT terms? | canonical anchors, claim ladder, symbol table |
| Retrieval value | Should this file be read for the current task? | source intuition, bridge files, split shards, book notes, evidence cards |

`canonical: false` means **not a definition authority**.

It does **not** mean:

- low value;
- do not retrieve;
- irrelevant;
- safe to ignore;
- only historical noise.

Many `canonical: false` files are high retrieval value for writing, theory development, bridge comparison, public framing, and context recovery.

---

## 1. Mandatory Agent Contract

After the minimal bootstrap, an agent must classify the task before deciding context depth.

Minimal bootstrap remains:

1. `AGENTS.md`
2. `SRT_AI_START.md`
3. `STATUS.md` or `STATUS_Split/README.md` when connector limits matter
4. `_SRT_INDEX.md`
5. `_SRT_SYMBOL_TABLE.md`
6. this file

Then:

1. Identify the task profile below.
2. Load the authority anchors needed for definitions.
3. Load the retrieval context needed for the actual work.
4. If the route touches a long file, use `LONGFORM_SPLITS.md` and the relevant split README first.
5. If the task is conceptual, cross-domain, or non-trivial, use `_SRT_CONTEXT_ROUTER.md`.
6. If the task is book writing, also use the book writing profile below.

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

Read:

1. `CANONICAL_REGISTRY.md`
2. `Governance/SRT_CLAIM_LADDER.md`
3. `Governance/SRT_CLAIM_MODE_AUDIT.md`
4. `_SRT_CONTEXT_ROUTER.md`
5. `_SRT_DEEP_THEORY_MAP.md`
6. the route's Primary files
7. the route's Secondary files when the question needs domain depth
8. `Core/SRT_OPEN_TENSIONS.md`
9. the relevant coverage index when the route may miss support files

Important:

- Use canonical anchors to prevent overclaiming.
- Use route, bridge, domain, and hardening files to avoid shallow answers.
- If a support file is `canonical: false`, mark it as support rather than skipping it.

### 2.3 Book Writing

Use when the user asks to write, revise, structure, polish, continue, audit, or style the SRT book.

Read:

1. `README.md`
2. `START_HERE.md`
3. `01_Source_Intuition/README.md`
4. `01_Source_Intuition/INDEX.md`
5. `01_Source_Intuition/BOOK/BOOK_CURRENT_STATUS.md` if present
6. `01_Source_Intuition/BOOK/Outline_Parts/README.md` if present
7. `90_Backstage/Restructure_2026/BOOK_PROJECT/repository_material_inclusion_matrix.md`
8. the current chapter or target chapter file
9. the relevant formal anchors only as guardrails, not as prose style
10. the relevant backstage pass notes when the task mentions consistency, style, or chapter sequence

Writing rule:

- Do not turn the book into canonical documentation.
- Use source-intuition files for force.
- Use formal anchors for accuracy.
- Use backstage notes for continuity.
- Use bridge and evidence files as shadow support, not as proof-dumps.

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
| Neuroscience | `Neuroscience/README.md`, `Neuroscience/NEUROSCIENCE_COMPACT_REGISTRY.md` |
| Physics | `Physics/README.md`, `Physics/PHYSICS_COMPACT_REGISTRY.md`, `Physics/SRT_Physics_Claim_Status.md` |
| Philosophy | `Philosophy/README.md`, `Philosophy/_PHILOSOPHY_MACHINE_INDEX.md`, `Philosophy/00_READ_FIRST_Philosophy_Hardening_Soft_Spots.md` |
| Spirituality | `Spirituality/SPIRITUALITY_COMPACT_REGISTRY.md`, `Spirituality/_SRT_Spirit_Axioms.md` |
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
5. `01_Source_Intuition/CORE_REVERSALS.md`
6. `Manifesto/SRT_MANIFESTO.md` when worldview tone is needed
7. formal anchors only as guardrails

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
5. `Operations/Large_File_Audit_2026-05-09.md`
6. `LONGFORM_SPLITS.md`
7. `_SRT_INDEX.md`
8. `_SRT_CONTEXT_ROUTER.md`

Rule:

- Improve retrieval without smuggling new theory.
- Add governance or operations records when the change affects agent behavior.

---

## 3. Connector-Safe Reading Rule

When using GitHub, ChatGPT repo connectors, Claude Code context tools, or any tool that may truncate large files:

1. Check `Operations/Large_File_Audit_2026-05-09.md`.
2. Check `LONGFORM_SPLITS.md`.
3. Prefer the split README for long owner files.
4. Read the owner file only when exact wording or local line context is needed.

Split shards are not independent authorities. They are high-value connector-safe copies.

---

## 4. Future Frontmatter Guidance

When adding or normalizing files, separate authority from retrieval:

```yaml
canonical: false
authority_level: bridge_support        # examples: canonical_anchor, canonical_support, domain_primary, bridge_support, split_copy, operations_record, backstage_writing_asset
retrieval_priority:
  theory_advancement: high
  book_writing: medium
  public_release: low
```

Do not use `canonical: true/false` as a retrieval filter.

For existing files without these fields, infer retrieval priority from indexes, router entries, split registries, and task profile.

---

## 5. High-Value Non-Canonical Areas

Do not ignore these merely because they are not canonical:

- `01_Source_Intuition/` for founding force and book style.
- `01_Source_Intuition/BOOK/` for current manuscript state.
- `90_Backstage/Restructure_2026/BOOK_PROJECT/` for book continuity, style, and inclusion decisions.
- `03_Bridges/` and `Bridge/` for adjacent theory translation.
- `04_External_Convergence/` for evidence, proxy, contradiction, and pressure.
- `LONGFORM_SPLITS.md` and split directories for connector-safe full-text retrieval.
- `_SRT_*_COVERAGE_INDEX.md` files for files that are valuable but easy to miss.
- `Operations/Material_Log/` for material provenance and integration history.
- domain claim-status files for anti-overclaiming boundaries.

---

## 6. Minimal Agent Workflow

For any non-trivial request:

1. Classify the task profile.
2. Load authority anchors.
3. Load retrieval context.
4. Use split routes for large files.
5. Check open tensions or claim status before making strong claims.
6. State whether a file is being used as canonical, bridge, support, evidence, backstage writing context, or operations provenance.

This is the intended fix for the main retrieval failure mode: agents were correctly avoiding non-canonical files as definition sources, but incorrectly letting that caution suppress valuable context.
