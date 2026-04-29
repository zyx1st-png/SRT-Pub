---
id: SRT-OPS-H3-SYMBOL-TABLE-GOVERNANCE-PATCH-2026-04-29
type: patch_record
tags: [Operations, Governance, SymbolTable, Patch, Hygiene]
status: active_record_v1
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-29
dependency:
  - _SRT_SYMBOL_TABLE.md
  - SRT_Glossary_Structural_Governance_Terms.md
  - ANNEX_REGISTRY.md
  - Operations/Closure_Index_2026-04-29.md
  - Operations/H1_Index_Readme_Glossary_Sync_Record.md
machine_summary: >
  PR-H3 patch record. Surgical governance cross-reference patch to _SRT_SYMBOL_TABLE.md.
  Adds structural governance dependencies to frontmatter, a Governance boundary note under
  Purpose, and two Usage Rules (13, 14) clarifying governance terms vs canonical symbols.
  No symbol rows, formulas, or thresholds were changed.
---

# H3 Symbol Table Governance Patch Record

## 0. Scope

PR-H3 performs a surgical governance cross-reference patch to `_SRT_SYMBOL_TABLE.md`.

This record documents what changed, what was not changed, and what is confirmed safe.

---

## 1. What changed in `_SRT_SYMBOL_TABLE.md`

### 1a. Frontmatter — dependency list expanded

Before:

```yaml
dependency: [SRT-REF-AXIOMS, SRT-REF-DYNAMICS]
```

After:

```yaml
dependency:
  - SRT-REF-AXIOMS
  - SRT-REF-DYNAMICS
  - SRT-GLOSSARY-STRUCTURAL-GOVERNANCE-TERMS
  - SRT-ANNEX-REGISTRY
  - SRT-OPS-CLOSURE-INDEX-2026-04-29
```

Rationale: the symbol table now explicitly acknowledges the governance layer it sits inside, making the relationship machine-readable without altering any canonical claim.

### 1b. Governance boundary note added under Purpose

Added immediately after the existing `> **Purpose** ...` line:

```
> **Governance boundary**: Terms such as `interface_annex`, `copy-to-annex`,
> `owner-bound`, `claim_mode`, and `canonical:false` are structural governance
> vocabulary (see `SRT_Glossary_Structural_Governance_Terms.md`); they are not
> canonical mathematical symbols and do not appear in this table's symbol rows.
> Non-canonical annexes and Operations records may reference symbols defined here
> but must not redefine them.
```

### 1c. Usage Rules 13 and 14 added

**Rule 13 — Governance terms are not theory symbols**

Clarifies that `interface_annex`, `copy-to-annex`, `owner-bound`, `claim_mode`,
`canonical:false`, and related structural governance vocabulary are repository-organisation
terms, not canonical mathematical or phenomenological symbols. They must not be added as
rows to the symbol table.

**Rule 14 — Annex and Operations reference scope**

Clarifies that non-canonical annex files and Operations records may cite symbols from
this table but must not introduce new symbol definitions, override usage rules, or alter
the scope of canonical symbols established here.

---

## 2. What was deliberately NOT changed

- No symbol table rows modified.
- No symbol definitions changed.
- No formulas changed.
- No thresholds changed.
- No D-Value Alignment section changed.
- No Ψ_f Alignment section changed.
- No existing Usage Rules (1–12) changed.
- No files in Core/, Core_Law/, AI/, Physics/, Neuroscience/, Philosophy/, Public/, Papers/, graphify-out/ touched.
- `SRT_Glossary_Structural_Governance_Terms.md` was not merged into `_SRT_SYMBOL_TABLE.md`.
- No governance terms were promoted into canonical theory symbols.

---

## 3. Verification checklist

| Check | Result |
|---|---|
| Symbol row definitions unchanged | ✓ |
| Formulas unchanged | ✓ |
| Thresholds unchanged | ✓ |
| Only frontmatter / Purpose note / Usage Rules touched | ✓ |
| `Operations/H3_Symbol_Table_Governance_Patch_Record.md` created | ✓ |

---

## 4. Relationship to prior governance records

| Record | Relationship |
|---|---|
| `Operations/H1_Index_Readme_Glossary_Sync_Record.md` | H1 explicitly deferred symbol-table governance patch to a future safe task; H3 executes that task |
| `Operations/Closure_Index_2026-04-29.md` | provides the governance stop-rule and annex-layer inventory that motivates Rules 13–14 |
| `SRT_Glossary_Structural_Governance_Terms.md` | defines the governance terms that Rules 13–14 reference |
| `ANNEX_REGISTRY.md` | lists the active annex layers cited in Rule 14 |

---

## 5. Bottom line

`_SRT_SYMBOL_TABLE.md` now has an explicit governance boundary note and two usage rules
that prevent governance terms from being conflated with canonical mathematical symbols,
and prevent annexes or Operations records from redefining symbols.

No theory content was modified.
