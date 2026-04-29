---
id: SRT-GLOSSARY-STRUCTURAL-GOVERNANCE-TERMS
type: glossary_addendum
tags: [Glossary, Governance, Structure, Annex, Claim-Mode, Operations]
status: active_v1
layer: meta
epistemic_layer: workflow
claim_mode: navigation
canonical: false
date: 2026-04-29
dependency:
  - SRT_Glossary.md
  - ANNEX_REGISTRY.md
  - Operations/Closure_Index_2026-04-29.md
  - Operations/Structural_Governance_Rollup_2026-04-29.md
machine_summary: >
  Structural governance glossary addendum for recent repository organization work. Defines terms such as
  copy-to-annex, owner-bound, interface annex, claim_mode, canonical false, closure report, and frozen high-risk topic.
  This addendum does not replace the canonical symbol table or core glossary.
---

# Structural Governance Terms / 结构治理术语补充

> This file supplements `SRT_Glossary.md` for repository-structure governance terms. It does not define SRT primitives such as `L0/L1/L2`, `G_hat_theta`, `Psi_f`, d-value, or `T_dir`.

---

## 1. Core governance terms

### `canonical: false`

A frontmatter flag indicating that a file is not a canonical theory source. It may still be useful as a navigation, interface, audit, or bridge document.

**Do not infer** that a file is unimportant merely because `canonical: false`; infer only that it does not override canonical anchors.

### `claim_mode`

A frontmatter field describing the claim posture of a file.

Common current values:

| Value | Meaning |
|---|---|
| `canonical` | theory-definition / authority layer; use sparingly |
| `translation` | bridge / cross-domain translation; not a final definition |
| `navigation` | index / reading aid / directory entry |
| `audit` | claim-status, safety, or workflow inspection |
| `exploratory` | hardening note, pressure-test, or early bridge material |

### `interface_annex`

A non-canonical annex file that carries external comparison, interface, analogy, or boundary material outside the owner longform.

Default reading:

```text
interface_annex = useful bridge layer, not theory-definition layer
```

### `owner-bound`

A section or claim that must remain in its owner / hardening / bridge source because it contains formulas, operator definitions, thresholds, positive claim clusters, or high-risk physical / consciousness assertions.

Owner-bound material should not be moved into annexes without a new adjudication.

### `copy-to-annex`

A low-risk extraction pattern where selected interface material is copied into an annex while the source owner file remains intact.

Used when source deletion or section movement is too risky.

### `adjudication`

A read-only Operations decision record that determines what may be moved, copied, blocked, or left owner-bound before any extraction occurs.

Preferred sequence:

```text
pre-audit -> inventory -> adjudication -> small extraction -> closure
```

### `closure report`

An Operations record that marks a restructuring round as closed, records what was changed, what was not changed, and what remains frozen.

### `pressure-test domain`

A domain used to stress or test SRT language without serving as the definition engine for core primitives.

Examples from recent governance:

- AI as pressure-test / boundary-test field;
- Physics as high-risk bridge domain.

### `external interface`

Material translating SRT language against an external theory, article, empirical domain, or conceptual framework.

External interface material may clarify SRT but does not prove SRT by itself.

### `proxy mapping`

A table or model that maps external categories to SRT-facing language for interpretation.

Proxy mappings do not define SRT primitives and must not be treated as identity claims.

### `frozen high-risk topic`

A topic explicitly blocked from opportunistic extraction until a new read-only adjudication is prepared.

Examples:

- AI Biological Naturalism / autopoiesis formulas;
- AI suffering / moral patienthood;
- Physics gravity / `Psi_f` / tensor derivations;
- Physics discrete time / collapse / MWI / constants.

---

## 2. Current governance stop rule

Do not continue opportunistic extraction after a closure report unless a fresh pre-audit or adjudication is created.

Safe future actions:

- index repair;
- link checks;
- broken frontmatter fixes;
- explicit new-domain pre-audit.

Unsafe future actions without adjudication:

- moving formulas;
- moving thresholds;
- moving subjecthood / consciousness claims;
- moving physics proof-language claims;
- converting exploratory bridge notes into canonical files.
