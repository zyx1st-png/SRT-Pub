---
id: CODEX-PROMPT-SECOND-FORMULA-ROLE-PASS-2026-04-27
type: codex_prompt
tags:
  - Codex
  - Claude-Code
  - Formula-Role
  - Philosophy
  - Ethics
  - Political-Philosophy
  - Social-Economics
  - Safe-Patching
  - PH-SS
status: ready_for_codex
layer: operations
epistemic_layer: workflow
claim_mode: prompt
claim_level: P5
canonical: false
date: 2026-04-27
dependency:
  - SRT_NEXT_OPTIMIZATION_TODO.md
  - SRT_Terminology_Consistency_Audit.md
  - Philosophy/PH_SS_Hardening_Audit_2026-04-27.md
  - Philosophy/SRT_Philosophy_Hardening_TODO.md
  - Core/SRT_Validation_Template.md
machine_summary: >
  Root-level Claude Code / Codex prompt for a second safe formula-role pass. It instructs the agent to
  scan Philosophy, Ethics, Political, and Social files for high-risk formulas and formula-like claims,
  then add short role labels without altering formulas, deleting content, rewriting long files, or
  promoting bridge material to canonical status.
---

# Codex / Claude Code Prompt — Second Formula-Role Pass

> **Use this from repository root**: `zyx1st-png/SRT-Pub`  
> **Purpose**: Add formula-role labels to high-risk formulas and formula-like claims across Philosophy / Ethics / Political / Social files.  
> **Critical rule**: Do **not** alter formulas. Do **not** rewrite whole files. Do **not** delete legacy material. Do **not** promote bridge claims to canonical status.

---

## Prompt to Claude Code / Codex

You are working in the `zyx1st-png/SRT-Pub` repository.

Your task is to perform a **second safe formula-role pass**.

The goal is not to rewrite SRT. The goal is to make formulas and formula-like statements easier to interpret by adding short labels such as:

```text
Formula role: definition
Formula role: bridge model
Formula role: phenomenological model
Formula role: operational proxy
Formula role: analogy
Formula role: placeholder
Formula role: legacy expression; read through current PH-SS guardrails
```

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

## 1. Read context files first

Read these files before editing:

```text
SRT_NEXT_OPTIMIZATION_TODO.md
SRT_Terminology_Consistency_Audit.md
Core/SRT_Validation_Template.md
Philosophy/PH_SS_Hardening_Audit_2026-04-27.md
Philosophy/SRT_Philosophy_Hardening_TODO.md
Philosophy/SRT_Philosophy_Foundations_CompactCore.md
Philosophy/_SRT_Phil_Axioms_PH_SS_Guardrails.md
Philosophy/SRT_Ethics_PH_SS_Guardrails.md
Philosophy/SRT_Social_Political_PH_SS_Guardrails.md
Philosophy/SRT_Subjecthood_Threshold_Interface.md
```

If any context file is missing, report it and continue with visible files. Do not create replacement files.

---

## 2. Target files

Perform this second pass on the following files if they exist:

```text
Philosophy/SRT_Philosophy_Foundations.md
Philosophy/_SRT_Phil_Axioms.md
Philosophy/SRT_Philosophy_Ethics.md
Philosophy/SRT_Ethics_Agency.md
Philosophy/SRT_Political_Philosophy.md
Philosophy/SRT_Social_Economics.md
Philosophy/SRT_Philosophy_Objection_Ledger.md
```

Optional compact files if they exist and contain formulas:

```text
Philosophy/SRT_Social_Economics_CompactCore.md
Philosophy/SRT_Political_Philosophy_CompactCore.md
Philosophy/SRT_Philosophy_Foundations_CompactCore.md
```

Do not scan the whole repository in this pass. Keep scope limited.

---

## 3. Search targets

Look for formulas, equations, theorem-like statements, or symbolic compressed claims involving:

```text
Existence ≡ Being Selected
Existence(X) iff ...
G_hat_theta / Ĝ_θ
L0 / L1 / L2 transitions
Psi_f ≡ g
Fisher metric
selection cost
friction export
moral legitimacy
moral progress
d-value
love / grief / gift / virtue formulas
responsibility / culpability / repair formulas
institutional legitimacy formulas
market / money / trust formulas
subjecthood / consciousness threshold formulas
paradox / ineffability / self-reference formulas
```

Also search for formula-like prose patterns:

```text
X = Y
X ≡ Y
X iff Y
X -> Y
X <-> Y
where X is not merely metaphorical
```

---

## 4. Label types

Use one of these labels. Add only short labels, preferably as blockquotes directly above or below the formula.

### 4.1 Definition

Use when the formula is intended as a local definition inside SRT vocabulary.

```md
> **Formula role**: definition within SRT vocabulary. Read with the current PH-SS guardrails; this does not by itself establish empirical measurement.
```

### 4.2 Bridge model

Use when the formula connects conceptual layers but is not yet canonical or empirically complete.

```md
> **Formula role**: bridge model. This connects SRT vocabulary across layers; it should not be read as a final reduction or single-variable proof.
```

### 4.3 Phenomenological model

Use for love, grief, shame, gift, virtue, meaning, ineffability, or lived-experience formulas.

```md
> **Formula role**: phenomenological model. This formalizes a structure of experience; do not read it as literal numerical measurement unless an operational proxy is specified.
```

### 4.4 Operational proxy

Use when the formula is intended as an empirical measurement proxy or possible operationalization.

```md
> **Formula role**: operational proxy candidate. This can support validation only if proxy, baseline, expected result, and failure condition are specified.
```

### 4.5 Analogy

Use when the formula is suggestive or cross-domain but not yet formal.

```md
> **Formula role**: analogy / heuristic. This may guide interpretation but should not be treated as proof or direct measurement.
```

### 4.6 Placeholder

Use when the formula is explicitly incomplete or needs later operationalization.

```md
> **Formula role**: placeholder. This requires later operational definition before being used as a strong claim.
```

### 4.7 Legacy expression

Use when the formula or claim is older, stronger than the current guardrails, or could mislead.

```md
> **Formula role**: legacy expression; read through current PH-SS guardrails. Preserved for historical / argumentative continuity, not as an unrestricted current claim.
```

---

## 5. Priority rules

Add labels only where there is real risk of misreading.

Highest priority:

```text
Psi_f ≡ g
Existence ≡ Being Selected
selection-before-existence formulas
moral progress formulas
d-value formulas
love / grief formulas with infinity or divergence language
social legitimacy / L2 formulas
AI / subjecthood threshold formulas
```

Lower priority:

```text
simple explanatory arrows;
ordinary section summaries;
plain diagrams already clearly marked as diagrams.
```

Do not over-label every formula. Aim for high-signal labels only.

---

## 6. Safety rules

Do not:

```text
alter formulas;
correct mathematics unless there is an obvious typo and you report it;
delete sections;
rewrite paragraphs;
rename claims;
change frontmatter claim_level / canonical fields unless strictly needed for status update;
promote bridge models to canonical primitives;
convert poetic formulas into empirical claims;
claim the formula-role cleanup is complete for the entire repository.
```

Only insert concise labels and, where needed, one sentence of guardrail.

---

## 7. Update TODO after successful edits

If you add labels, update:

```text
SRT_NEXT_OPTIMIZATION_TODO.md
```

Minimal update:

- bump status from current `active_v12` to `active_v13` if still current;
- add to completed baseline:

```text
Second formula-role pass completed for Philosophy / Ethics / Political / Social high-risk formulas.
```

- change priority overview row:

```text
Second formula-role pass ... todo
```

to:

```text
Second formula-role pass ... done
```

- suggested next action should become:

```text
Create CODEX_PROMPT_Long_Foundations_Axioms_Deeper_Reorganization.md
```

or, if you judge deep reorganization not yet advisable:

```text
Review whether deeper long-file reorganization is needed after the formula-role pass.
```

Do not mark deeper long-file reorganization done.

---

## 8. Diff and review

After editing, run:

```bash
git diff -- Philosophy/SRT_Philosophy_Foundations.md Philosophy/_SRT_Phil_Axioms.md Philosophy/SRT_Philosophy_Ethics.md Philosophy/SRT_Ethics_Agency.md Philosophy/SRT_Political_Philosophy.md Philosophy/SRT_Social_Economics.md Philosophy/SRT_Philosophy_Objection_Ledger.md Philosophy/SRT_Social_Economics_CompactCore.md Philosophy/SRT_Political_Philosophy_CompactCore.md Philosophy/SRT_Philosophy_Foundations_CompactCore.md SRT_NEXT_OPTIMIZATION_TODO.md
```

Confirm:

```text
No formulas altered.
No full-file rewrites.
No deletions.
No canonical status promotion.
Labels are concise.
Only high-risk formulas were labeled.
TODO updated only after successful edits.
```

---

## 9. Commit message

Use:

```text
Add second formula-role labels to high-risk SRT claims
```

---

## 10. Final report format

Report:

```text
Repository / branch verified:
- ...

Files scanned:
- ...

Patched files:
- ...

Labels added:
- definition: N
- bridge model: N
- phenomenological model: N
- operational proxy: N
- analogy: N
- placeholder: N
- legacy expression: N

Safety checks:
- Full-file rewrites performed: no
- Deletions: none
- Formulas altered: no
- Canonical claims promoted: no
- Theory content changed: no, only formula-role labels / guardrails

TODO updated:
- yes/no

Remaining follow-up:
- deeper long-file reorganization optional / not yet done
```

---

## 11. Completion standard

This task is complete when high-risk formulas in the target Philosophy / Ethics / Political / Social files have enough labels that a human or machine can distinguish:

```text
definition vs bridge model vs phenomenological model vs operational proxy vs analogy vs placeholder vs legacy expression
```

without interpreting every formula as a literal measurement, proof, or canonical primitive.
