---
id: CODEX-PROMPT-UPDATE-REGISTRY-FOR-PH-SS-FILES-2026-04-27
type: codex_prompt
tags:
  - Codex
  - Claude-Code
  - Registry
  - README
  - Index
  - PH-SS
  - Discovery
  - Safe-Patching
status: ready_for_codex
layer: operations
epistemic_layer: workflow
claim_mode: prompt
claim_level: P5
canonical: false
date: 2026-04-27
dependency:
  - SRT_NEXT_OPTIMIZATION_TODO.md
  - CANONICAL_REGISTRY.md
  - README.md
  - Philosophy/README.md
  - Philosophy/_PHILOSOPHY_MACHINE_INDEX.md
  - Philosophy/SRT_Philosophy_Hardening_TODO.md
  - Philosophy/PH_SS_Hardening_Audit_2026-04-27.md
machine_summary: >
  Root-level Claude Code / Codex prompt for safely checking and updating repository discovery surfaces
  after the PH-SS philosophy hardening pass. It asks the agent to audit CANONICAL_REGISTRY, root README,
  Philosophy README, machine index, TODO, audit file, and related indexes so new PH-SS files are discoverable
  without promoting bridge files to canonical status or rewriting long files.
---

# Codex / Claude Code Prompt — Update Registry for PH-SS Files

> **Use this from repository root**: `zyx1st-png/SRT-Pub`  
> **Purpose**: Ensure all newly created PH-SS hardening files are discoverable from registry / README / index surfaces.  
> **Critical rule**: Do not promote bridge / companion / public files into canonical primitive sources. Do not rewrite whole files.

---

## Prompt to Claude Code / Codex

You are working in the `zyx1st-png/SRT-Pub` repository.

Your task is to perform a **safe discovery-surface update** after the PH-SS philosophy hardening pass.

The goal is not to change theory content. The goal is to ensure newly created or upgraded PH-SS files can be found by humans and machines from appropriate index / registry / README files.

---

## 0. Verify repository state

Before editing, report:

```bash
git remote -v
git branch --show-current
git rev-parse HEAD
git status --short
```

If not on `zyx1st-png/SRT-Pub` and branch `main`, stop and report the mismatch.

---

## 1. Read these context files first

Read all visible files from this list before editing:

```text
SRT_NEXT_OPTIMIZATION_TODO.md
CANONICAL_REGISTRY.md
README.md
Philosophy/README.md
Philosophy/_PHILOSOPHY_MACHINE_INDEX.md
Philosophy/SRT_Philosophy_Hardening_TODO.md
Philosophy/PH_SS_Hardening_Audit_2026-04-27.md
Core/SRT_Core_24_Floor_Normativity_Verification.md
AI/SRT_AI_03_Consciousness_Framework_CompactCore.md
Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md
```

If any file is missing, report it and continue with visible files. Do not create replacement files unless explicitly required.

---

## 2. Files that should be discoverable

Check that the following files are discoverable from at least one suitable index / README / registry surface.

### PH-SS philosophy hardening files

```text
Philosophy/00_READ_FIRST_Philosophy_Hardening_Soft_Spots.md
Philosophy/01_PH_SS_Objection_Crosswalk.md
Philosophy/02_PH_SS_Hardening_Execution_Plan.md
Philosophy/03_Selection_Realism_Layered_Realism_CompactPatch.md
Philosophy/_SRT_Phil_Axioms_PH_SS_Guardrails.md
Philosophy/SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md
Philosophy/SRT_Ethics_PH_SS_Guardrails.md
Philosophy/SRT_Social_Political_PH_SS_Guardrails.md
Philosophy/SRT_Philosophy_Tradition_Comparison_PH_SS.md
Philosophy/SRT_Subjecthood_Threshold_Interface.md
Philosophy/SRT_Philosophy_Public_OnePager.md
Philosophy/PH_SS_Hardening_Audit_2026-04-27.md
```

### Cross-domain linked files

```text
AI/SRT_AI_03_Consciousness_Framework_CompactCore.md
Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md
Core/SRT_Core_24_Floor_Normativity_Verification.md
```

### Operational prompts / TODOs

```text
SRT_NEXT_OPTIMIZATION_TODO.md
CODEX_PROMPT_Philosophy_Long_File_PH_SS_Direct_Pointers.md
CODEX_PROMPT_Philosophy_Long_Foundations_Axioms_Refactor.md
CODEX_PROMPT_Update_Registry_For_PH_SS_Files.md
Operations/Codex_Prompts/2026-04-27_Philosophy_Long_File_PH_SS_Direct_Pointers.md
```

---

## 3. Target files to patch if needed

Patch only when the target file exists and only if the relevant discovery path is missing or outdated.

Primary targets:

```text
README.md
CANONICAL_REGISTRY.md
Philosophy/README.md
Philosophy/_PHILOSOPHY_MACHINE_INDEX.md
Philosophy/SRT_Philosophy_Hardening_TODO.md
Philosophy/PH_SS_Hardening_Audit_2026-04-27.md
SRT_NEXT_OPTIMIZATION_TODO.md
```

Secondary targets if they exist and clearly serve as indexes:

```text
AI/README.md
Neuroscience/README.md
Core/README.md
Operations/README.md
```

Do not create new README files unless the repository convention clearly expects them.

---

## 4. Patch policy

### 4.1 Do minimal patches only

Allowed edits:

- add a short list item;
- add a short table row;
- add a short “PH-SS hardening files” subsection;
- add a short routing note;
- update a status line from outdated to current;
- add a cross-reference to an existing index.

Forbidden edits:

- broad rewrite;
- deleting old registry entries;
- changing canonical definitions;
- promoting bridge / companion / audit / public files to canonical primitive status;
- reordering whole documents;
- adding long theoretical prose to index files.

### 4.2 Canonical status guardrail

Most new PH-SS files are **not canonical primitive sources**. They should be marked as one of:

```text
bridge hardening
companion guardrail
objection extension
audit
public bridge
workflow / codex prompt
index / route
```

Do not list them as P0/P1 canonical primitives unless their frontmatter explicitly says so and the repository already treats them that way.

### 4.3 Registry entry style

If adding to `CANONICAL_REGISTRY.md`, prefer a section like:

```md
### PH-SS Philosophy Hardening / Guardrail Files

These are not P0/P1 canonical primitive sources. They are routing, bridge hardening, audit, or companion files that protect interpretation of the Philosophy domain.

| File | Role | Status |
|---|---|---|
| `Philosophy/SRT_Philosophy_Foundations_CompactCore.md` | current compact philosophy entry | active_v4 |
| `Philosophy/_SRT_Phil_Axioms_PH_SS_Guardrails.md` | axiom guardrail companion | active bridge guardrail |
| ... | ... | ... |
```

Do not insert them into a core canonical primitives table unless there is a clearly designated non-canonical section.

---

## 5. Suggested minimal additions

### 5.1 Root README

If `README.md` has an overview / navigation section, add a short pointer:

```md
### Philosophy PH-SS hardening route

For the current hardened philosophy route, start with:

- `Philosophy/_PHILOSOPHY_MACHINE_INDEX.md`
- `Philosophy/SRT_Philosophy_Foundations_CompactCore.md`
- `Philosophy/PH_SS_Hardening_Audit_2026-04-27.md`

Public / comparison / subjecthood entries:

- `Philosophy/SRT_Philosophy_Public_OnePager.md`
- `Philosophy/SRT_Philosophy_Tradition_Comparison_PH_SS.md`
- `Philosophy/SRT_Subjecthood_Threshold_Interface.md`
```

### 5.2 Philosophy README

If missing, add or update a PH-SS section:

```md
## PH-SS hardening route

Start here for current hardened philosophy:

1. `_PHILOSOPHY_MACHINE_INDEX.md`
2. `00_READ_FIRST_Philosophy_Hardening_Soft_Spots.md`
3. `01_PH_SS_Objection_Crosswalk.md`
4. `02_PH_SS_Hardening_Execution_Plan.md`
5. `SRT_Philosophy_Foundations_CompactCore.md`
6. `PH_SS_Hardening_Audit_2026-04-27.md`

Key companion files:

- `_SRT_Phil_Axioms_PH_SS_Guardrails.md`
- `SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md`
- `SRT_Ethics_PH_SS_Guardrails.md`
- `SRT_Social_Political_PH_SS_Guardrails.md`
- `SRT_Philosophy_Tradition_Comparison_PH_SS.md`
- `SRT_Subjecthood_Threshold_Interface.md`
- `SRT_Philosophy_Public_OnePager.md`
```

### 5.3 AI / Neuroscience / Core README files

If these README files exist, add one-line cross-links only:

```md
- PH-SS subjecthood guardrail: `../Philosophy/SRT_Subjecthood_Threshold_Interface.md`
```

For Core:

```md
- PH-SS non-reductive validation guardrail: `SRT_Core_24_Floor_Normativity_Verification.md`
```

---

## 6. Audit before editing

Before patching, produce a short checklist in your working notes:

```text
Root README has PH-SS route: yes/no
CANONICAL_REGISTRY has non-canonical PH-SS section: yes/no
Philosophy README has PH-SS route: yes/no
Machine index includes tradition comparison, subjecthood interface, public one-pager: yes/no
TODO active status reflects latest: yes/no
Audit active status reflects latest: yes/no
AI/Neuro/Core README cross-links needed: yes/no/not present
```

Patch only the `no` items.

---

## 7. Diff and safety review

After editing, run:

```bash
git diff -- README.md CANONICAL_REGISTRY.md Philosophy/README.md Philosophy/_PHILOSOPHY_MACHINE_INDEX.md Philosophy/SRT_Philosophy_Hardening_TODO.md Philosophy/PH_SS_Hardening_Audit_2026-04-27.md SRT_NEXT_OPTIMIZATION_TODO.md AI/README.md Neuroscience/README.md Core/README.md Operations/README.md
```

Confirm:

```text
No full-file rewrites.
No deletions of existing registry entries.
No canonical status promotion.
Only index / routing / discovery changes.
All new PH-SS files discoverable from at least one index.
```

---

## 8. Commit message

Use:

```text
Update registry and README discovery for PH-SS files
```

---

## 9. Final report format

Report:

```text
Repository / branch verified:
- ...

Discovery audit:
- Root README PH-SS route: yes/no/updated
- CANONICAL_REGISTRY PH-SS non-canonical section: yes/no/updated
- Philosophy README PH-SS route: yes/no/updated
- Machine index current: yes/no/updated
- TODO current: yes/no/updated
- Audit current: yes/no/updated
- AI/Neuro/Core README links: yes/no/not present/updated

Patched files:
- ...

Skipped files:
- ... and why

Safety checks:
- Full-file rewrites performed: no
- Deletions: none / list
- Canonical claims promoted: no
- Theory content changed: no

Remaining follow-up:
- ...
```

---

## 10. Completion standard

This task is complete when:

```text
A human or agent starting from root README, CANONICAL_REGISTRY, or Philosophy README can find:
- current philosophy compact entry;
- PH-SS hardening route;
- objection extension;
- ethics and social-political guardrails;
- tradition comparison;
- subjecthood interface;
- public one-pager;
- audit / TODO status.
```
