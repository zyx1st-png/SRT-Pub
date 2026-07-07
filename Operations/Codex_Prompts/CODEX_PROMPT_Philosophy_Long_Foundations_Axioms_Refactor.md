---
id: CODEX-PROMPT-PHIL-LONG-FOUNDATIONS-AXIOMS-REFACTOR-2026-04-27
type: codex_prompt
tags:
  - Codex
  - Claude-Code
  - Philosophy
  - Long-Files
  - Foundations
  - Axioms
  - Refactor
  - Formula-Role
  - Legacy-Cleanup
  - Safe-Patching
status: ready_for_codex
layer: operations
epistemic_layer: workflow
claim_mode: prompt
claim_level: P5
canonical: false
date: 2026-04-27
dependency:
  - Philosophy/SRT_Philosophy_Foundations.md
  - Philosophy/_SRT_Phil_Axioms.md
  - Philosophy/SRT_Philosophy_Foundations_CompactCore.md
  - Philosophy/_SRT_Phil_Axioms_PH_SS_Guardrails.md
  - Philosophy/SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md
  - Philosophy/PH_SS_Hardening_Audit_2026-04-27.md
machine_summary: >
  Root-level Claude Code / Codex prompt for safely refactoring long Philosophy Foundations and
  Axioms files. It instructs the agent to audit first, avoid full-file rewrites, add formula-role
  labels, mark legacy duplicates, add canonical links, and propose companion merges without deleting
  historical content.
---

# Codex / Claude Code Prompt — Long Foundations + Axioms Safe Refactor

> **Use this from repository root**: `zyx1st-png/SRT-Pub`  
> **Purpose**: Safely refactor long philosophy files that are too large for remote full-file replacement.  
> **Critical rule**: Do **not** rewrite whole files. Do **not** delete historical content. Do **not** canonicalize bridge companion files.

---

## Prompt to Claude Code / Codex

You are working in the `zyx1st-png/SRT-Pub` repository.

Your task is to perform a **safe, minimal, reviewable refactor** of two long Philosophy files:

1. `Philosophy/SRT_Philosophy_Foundations.md`
2. `Philosophy/_SRT_Phil_Axioms.md`

The goal is not to rewrite SRT philosophy. The goal is to make existing long files easier for humans and machines to read by adding structure, formula-role labels, legacy markers, and canonical / companion links.

---

## 0. First verify repository state

Before editing, report:

```bash
git remote -v
git branch --show-current
git rev-parse HEAD
git status --short
```

If not on the intended repository `zyx1st-png/SRT-Pub` and branch `main`, stop and report the mismatch.

---

## 1. Read context files first

Read these before editing:

```text
Philosophy/_PHILOSOPHY_MACHINE_INDEX.md
Philosophy/SRT_Philosophy_Hardening_TODO.md
Philosophy/PH_SS_Hardening_Audit_2026-04-27.md
Philosophy/SRT_Philosophy_Foundations_CompactCore.md
Philosophy/_SRT_Phil_Axioms_PH_SS_Guardrails.md
Philosophy/SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md
Philosophy/SRT_Philosophy_Tradition_Comparison_PH_SS.md
Philosophy/SRT_Subjecthood_Threshold_Interface.md
Philosophy/SRT_Philosophy_Public_OnePager.md
```

If any context file is missing, report it and continue with the visible files. Do not create replacements unless explicitly asked.

---

## 2. Work in four passes, but keep edits minimal

Perform these passes in order:

```text
Pass A: audit map only
Pass B: formula-role labels
Pass C: legacy / duplicate markers
Pass D: canonical / companion links
```

Do not do broad prose rewriting. Prefer short inserted notes, headings, and markers.

---

# Pass A — Audit map only

For each target file, create or update a short section near the top after frontmatter and existing pointer sections:

```md
## Current Reading Map

This long file contains multiple historical layers. For current hardened reading, start with:

- `SRT_Philosophy_Foundations_CompactCore.md`
- `_SRT_Phil_Axioms_PH_SS_Guardrails.md`
- `SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md`
- `PH_SS_Hardening_Audit_2026-04-27.md`

Reader rule:

- Treat Compact Core v4 as the current short entry point.
- Treat this long file as expanded / historical / argumentative material.
- Where old slogans appear stronger than current guardrails, read them through the PH-SS guardrails.
```

If a similar section already exists, merge without duplication.

---

# Pass B — Formula-role labels

Find formulas or theorem-like statements in both target files. Do not alter the math unless there is a clear typo. Add short labels directly above or below high-risk formulas.

Use one of these labels:

```text
Formula role: definition
Formula role: bridge model
Formula role: phenomenological model
Formula role: analogy
Formula role: operational proxy
Formula role: placeholder
Formula role: legacy expression; read through current PH-SS guardrails
```

Priority formulas to label:

```text
Existence ≡ Being Selected
Existence(X) iff ... G_hat_theta ...
L0 as all possibilities / potentiality / Meinong / Sunyata
Psi_f ≡ g
Fisher metric / information geometry claims
paradox formulas involving L1/L2 or self-reference
ineffability formulas
love / grief / gift / virtue formulas if present
moral progress / d-value formulas if present
subjecthood / consciousness formulas if present
social or political legitimacy formulas if present
```

Examples of safe insertions:

```md
> **Formula role**: bridge definition inside SRT vocabulary; read with PH-SS guardrails. This does not imply chronological creation or subjective idealism.
```

```md
> **Formula role**: operational proxy / information-geometric slice. This does not exhaust `Psi_f` across ontological, embodied, or normative layers.
```

```md
> **Formula role**: phenomenological model. Do not read poetic infinity or divergence language as literal unless an operational proxy and failure condition are stated.
```

---

# Pass C — Legacy / duplicate markers

Identify sections that appear older, duplicated, or stronger than the current PH-SS-hardened reading. Do not delete them. Add compact markers:

```md
> **Legacy / expanded note**: This passage is preserved as historical or argumentative expansion. For current guardrails, read with `SRT_Philosophy_Foundations_CompactCore.md` and `_SRT_Phil_Axioms_PH_SS_Guardrails.md`.
```

Use this especially when old passages imply:

```text
L0 as hidden object-world;
selection-before-existence as temporal priority;
Psi_f as one single cost;
L2 stabilization as moral legitimacy;
micro-selection as subjecthood;
truth as whatever is selected;
formula-as-proof where current status is only bridge model.
```

Do not mark every paragraph. Mark only high-risk sections.

---

# Pass D — Canonical / companion links

Add or improve links to current routing files. Keep this short.

In `SRT_Philosophy_Foundations.md`, add a section if missing:

```md
## Current Companion Links

- Compact current entry: `SRT_Philosophy_Foundations_CompactCore.md`
- Axiom guardrails: `_SRT_Phil_Axioms_PH_SS_Guardrails.md`
- Objection extension: `SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md`
- Tradition comparison: `SRT_Philosophy_Tradition_Comparison_PH_SS.md`
- Subjecthood interface: `SRT_Subjecthood_Threshold_Interface.md`
- Public one-pager: `SRT_Philosophy_Public_OnePager.md`
```

In `_SRT_Phil_Axioms.md`, add a section if missing:

```md
## Current Guardrail Links

- Axiom guardrail companion: `_SRT_Phil_Axioms_PH_SS_Guardrails.md`
- Compact current entry: `SRT_Philosophy_Foundations_CompactCore.md`
- Objection extension: `SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md`
- Subjecthood interface: `SRT_Subjecthood_Threshold_Interface.md`
```

---

## 3. Update TODO only after successful edits

If edits are made, update `Philosophy/SRT_Philosophy_Hardening_TODO.md` minimally:

- bump status from `active_v9` to `active_v10`;
- add one line under integration status:

```text
SRT_Philosophy_Foundations.md and _SRT_Phil_Axioms.md -> safe refactor pass started: reading map, formula-role labels, legacy markers, companion links
```

- in pending tasks, change:

```text
Long Foundations / Axioms full refactor
```

to:

```text
Long Foundations / Axioms full refactor -> started; only safe marking / linking pass completed
```

Do not claim full refactor is complete unless it truly is.

---

## 4. Produce a diff and review before commit

After edits, run:

```bash
git diff -- Philosophy/SRT_Philosophy_Foundations.md Philosophy/_SRT_Phil_Axioms.md Philosophy/SRT_Philosophy_Hardening_TODO.md
```

Check:

- no large deletions;
- no mass rewrite;
- no frontmatter corruption;
- no accidental canonical promotion;
- formula-role labels are short;
- legacy markers are sparse and targeted;
- companion links are correct.

---

## 5. Commit message

Use a message like:

```text
Safely mark Philosophy Foundations and Axioms for PH-SS refactor
```

---

## 6. Final report format

Report:

```text
Repository / branch verified:
- ...

Patched files:
- Philosophy/SRT_Philosophy_Foundations.md
- Philosophy/_SRT_Phil_Axioms.md
- Philosophy/SRT_Philosophy_Hardening_TODO.md

Passes completed:
- Pass A reading map: yes/no
- Pass B formula-role labels: yes/no, count
- Pass C legacy markers: yes/no, count
- Pass D companion links: yes/no

Safety checks:
- Full-file rewrites performed: no
- Deletions: none / list
- Canonical claims changed: no
- Math altered: no / list

Remaining follow-up:
- optional deeper section reorganization
- optional companion-to-owner merge after review
```

---

## 7. Absolute prohibitions

Do not:

- replace entire long files;
- delete legacy material;
- rewrite philosophical arguments wholesale;
- alter formulas except typo fixes;
- change claim levels from bridge to canonical;
- promote companion files into canonical definitions;
- claim the refactor is complete if only markers were added.

The goal is to make the long files safer and more navigable, not to finalize them.
