---
id: CODEX-PROMPT-PHIL-LONG-FILE-PH-SS-DIRECT-POINTERS-2026-04-27
type: codex_prompt
tags:
  - Codex
  - Philosophy
  - PH-SS
  - Long-Files
  - Direct-Pointers
  - Safe-Patching
status: ready_for_codex
layer: operations
epistemic_layer: workflow
claim_mode: prompt
claim_level: P5
canonical: false
date: 2026-04-27
dependency:
  - Philosophy/00_READ_FIRST_Philosophy_Hardening_Soft_Spots.md
  - Philosophy/01_PH_SS_Objection_Crosswalk.md
  - Philosophy/02_PH_SS_Hardening_Execution_Plan.md
  - Philosophy/SRT_Philosophy_Foundations_CompactCore.md
  - Philosophy/_SRT_Phil_Axioms_PH_SS_Guardrails.md
  - Philosophy/SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md
  - Philosophy/SRT_Ethics_PH_SS_Guardrails.md
  - Philosophy/SRT_Social_Political_PH_SS_Guardrails.md
machine_summary: >
  Prompt for Codex to safely patch long SRT Philosophy files using full local file access.
  The goal is to add direct PH-SS guardrail pointers and minimal formula-role / warning notes
  without rewriting, truncating, or canonicalizing companion files.
---

# Codex Prompt — Philosophy Long-File PH-SS Direct Pointers

Copy the prompt below into Codex from the repository root of `zyx1st-png/SRT-Pub`.

---

## Prompt to Codex

You are working in the `zyx1st-png/SRT-Pub` repository.

Goal: safely add direct PH-SS guardrail pointers into long Philosophy owner files that were too large to safely replace through remote full-file updates. Do **minimal targeted edits only**. Do not rewrite full files. Do not delete or reorder existing long sections. Do not promote companion files to canonical definitions.

### Context files to read first

Read these files before editing:

1. `Philosophy/_PHILOSOPHY_MACHINE_INDEX.md`
2. `Philosophy/00_READ_FIRST_Philosophy_Hardening_Soft_Spots.md`
3. `Philosophy/01_PH_SS_Objection_Crosswalk.md`
4. `Philosophy/02_PH_SS_Hardening_Execution_Plan.md`
5. `Philosophy/SRT_Philosophy_Foundations_CompactCore.md`
6. `Philosophy/_SRT_Phil_Axioms_PH_SS_Guardrails.md`
7. `Philosophy/SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md`
8. `Philosophy/SRT_Ethics_PH_SS_Guardrails.md`
9. `Philosophy/SRT_Social_Political_PH_SS_Guardrails.md`
10. `Philosophy/SRT_Philosophy_Hardening_TODO.md`

### Target files

Patch these files if they exist:

1. `Philosophy/SRT_Philosophy_Ethics.md`
2. `Philosophy/SRT_Ethics_Agency.md`
3. `Philosophy/SRT_Philosophy_Foundations.md`
4. `Philosophy/_SRT_Phil_Axioms.md`
5. `Philosophy/SRT_Philosophy_Objection_Ledger.md`
6. `Philosophy/SRT_Political_Philosophy.md`
7. `Philosophy/SRT_Social_Economics.md`

If any file is missing, skip it and report that it was missing. Do not create replacement files for missing targets.

---

## Required edits

### 1. Add a PH-SS guardrail pointer near the top of long ethics files

For:

- `Philosophy/SRT_Philosophy_Ethics.md`
- `Philosophy/SRT_Ethics_Agency.md`

Add a short section after the frontmatter and existing terminology / canonical cross-link block, without disrupting existing text:

```md
## PH-SS Guardrail Pointer

Read this file with `SRT_Ethics_PH_SS_Guardrails.md`.

Core guardrails:

- `d-value` expansion is not automatically moral progress.
- `L_2` stabilization is not automatically moral legitimacy.
- Moral intensity, moral reality, and moral legitimacy must remain distinct.
- Responsibility requires selectable agency, not merely high harm or high concern.
- Love / grief / gift / virtue formulas should be read with explicit formula-role labels unless operationalized.
- Ethics claims involving social norms should check friction export, future selectability, reversibility, and correction channels.
```

### 2. Add local warning notes near risky ethics claims

In `SRT_Philosophy_Ethics.md`, find sections resembling:

- `T-Eth-1: Moral Gradient Theorem`
- `Ax-Eth-7: The Ontological Weight of Love`
- any `Gift`, `Grief`, `Virtue`, or infinite-friction formula sections

Add short notes directly under the heading or formula, not replacing the original claim.

For `T-Eth-1`, add:

```md
> **PH-SS guardrail**: This theorem should be read as a directional / phenomenological model, not as a sufficient condition for moral legitimacy. `d-value` expansion may signal moral widening, but moral legitimacy also requires non-exported friction, future-selectability, cross-subject bandwidth, and correction channels. See `SRT_Ethics_PH_SS_Guardrails.md`.
```

For love / grief / gift / virtue formulas, add:

```md
> **Formula role guardrail**: This formula is a phenomenological / existential-weight model unless explicitly operationalized. Do not read poetic infinity, gift-phase, or grief-weight language as literal mathematical divergence without a stated proxy and failure condition. See `SRT_Ethics_PH_SS_Guardrails.md`.
```

### 3. Add a PH-SS guardrail pointer near the top of long foundations / axiom files

For:

- `Philosophy/SRT_Philosophy_Foundations.md`
- `Philosophy/_SRT_Phil_Axioms.md`

Add:

```md
## PH-SS Guardrail Pointer

Read this file with:

- `SRT_Philosophy_Foundations_CompactCore.md` — current active short entry, active_v4.
- `_SRT_Phil_Axioms_PH_SS_Guardrails.md` — safe readings for `L_0`, selection-before-existence, reality strength, `Psi_f` layers, normativity, and subjecthood.
- `SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md` — `O-Phil-11..20` objections.

Core guardrails:

```text
L0 is not a hidden object-world;
selection-before-existence is manifestational, not temporal;
theta is not subjective will;
Psi_f is not a single cost;
stabilization is not moral justification;
selected reality is not relativism;
not all selection is consciousness.
```
```

If the file already contains similar guardrails, merge the wording without duplication.

### 4. Add local notes near risky axiom / foundations claims

In `_SRT_Phil_Axioms.md` and `SRT_Philosophy_Foundations.md`, where relevant, add brief notes near:

- `Existence ≡ Being Selected`
- `L_0` as all possibilities / potentiality / Meinong / Sunyata
- `Psi_f ≡ g` or Fisher metric statements
- statements implying all selection is consciousness
- statements implying stable norms are morally good

Use these notes as appropriate:

```md
> **PH-SS guardrail**: `L_0` should be read here as a modal field of selectability / condition of possible manifestation, not an object-like hidden world.
```

```md
> **PH-SS guardrail**: Selection-before-existence is manifestational priority, not chronological priority.
```

```md
> **PH-SS guardrail**: Fisher information metric may express `Psi_f` on an information-geometric slice; it does not exhaust the full meaning of ontological / embodied / normative friction.
```

```md
> **PH-SS guardrail**: Micro-selection does not entail subjecthood. Consciousness requires threshold conditions such as structured `d-value`, integration, memory / `L_2` closure, boundary maintenance, and counterfactual access.
```

### 5. Add PH-SS pointer to main objection ledger

In `Philosophy/SRT_Philosophy_Objection_Ledger.md`, add a short top-level pointer:

```md
## PH-SS Extension Pointer

For the current PH-SS objection extension, also read `SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md`, which adds:

- `O-Phil-11` L0 hidden-world objection
- `O-Phil-12` temporal priority objection
- `O-Phil-13` reality-strength flattening objection
- `O-Phil-14` `Psi_f` equivocation objection
- `O-Phil-15` mystical teleology objection
- `O-Phil-16` `d-value` preference-reduction objection
- `O-Phil-17` social construction / institutional reification objection
- `O-Phil-18` consciousness over-attribution objection
- `O-Phil-19` non-reductive verification objection
- `O-Phil-20` selected-reality relativism objection
```

### 6. Add social-political guardrail pointers to long social / political files

For:

- `Philosophy/SRT_Political_Philosophy.md`
- `Philosophy/SRT_Social_Economics.md`

Add a top-level pointer:

```md
## PH-SS Social / Political Guardrail Pointer

Read this file with `SRT_Social_Political_PH_SS_Guardrails.md`.

Core guardrails:

- Social `L_2` reality is not social legitimacy.
- Institutional persistence is not political justification.
- Market selection is not moral truth.
- Money / price is an `L_2` metric, not final value.
- Low friction is not justice unless hidden `Psi_f` is not exported.
- Legitimacy requires reselection capacity, consequence-return symmetry, non-exported friction, exit/correction channels, and future-selectability.
```

### 7. Update TODO status only after edits

After the above edits, update `Philosophy/SRT_Philosophy_Hardening_TODO.md`:

- Keep `status: active_v5` unless you have a reason to bump to `active_v6`.
- Mark direct pointer additions as completed for:
  - long ethics files if patched;
  - long foundations / axiom files if patched;
  - main objection ledger if patched;
  - long social / political files if patched.
- Do not claim direct merge is complete unless you actually inserted into the target file.

---

## Safety rules

1. Do not rewrite whole files.
2. Do not delete existing content.
3. Do not canonicalize companion files.
4. Do not change P0/P1 definitions.
5. Do not convert bridge claims into canonical claims.
6. Do not alter math except by adding formula-role / guardrail notes.
7. Keep all additions short, visible, and easy to grep.
8. After editing, run:

```bash
git diff -- Philosophy
```

Review the diff and ensure only targeted pointer / note additions were made.

---

## Final response expected from Codex

Report:

```text
Patched files:
- ...

Skipped files:
- ... and why

Key inserted guardrails:
- ...

No full-file rewrites performed: yes/no
Potential follow-up:
- ...
```
