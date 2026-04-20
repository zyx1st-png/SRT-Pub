---
id: SRT-CLAIM-LADDER
type: governance
tags: [Governance, Claim Ladder, Canonical, Bridge, Lab]
status: active_v1
layer: meta
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-CANONICAL-FREEZE, SRT-EDIT-PROTOCOL, SRT-CANONICAL-REGISTRY]
---

# SRT Claim Ladder

> **Purpose**: This file defines proposition-level hardness. File role and claim role are related but not identical: a canonical file may contain bridge claims, and a bridge file may quote primitive axioms. The claim level must be explicit whenever hardness matters.

## 0. Core Rule

Never let a lower-hardness claim wear the voice of a higher-hardness claim.

In particular, domain files must not present P3/P4/P5 claims as if they were P0/P1.

---

## 1. Claim Levels

| Level | Name | Definition | Allowed Voice |
|---:|---|---|---|
| P0 | Primitive axiom | A minimal SRT axiom without which the core grammar fails. It does not depend on a domain bridge, empirical threshold, or external theory. | "SRT assumes..."; "Within SRT, this is primitive..."; "Without this, the framework does not stand..." |
| P1 | Constitutive theorem | A claim treated as following from the SRT core structure. It is not primitive, but it is internally constitutive once P0 is granted. | "SRT entails..."; "Constitutively..."; "Given the core axioms..." |
| P2 | Canonical interpretation | A stable interpretive reading used across SRT, but not a primitive or theorem. It organizes meaning and usage. | "SRT reads this as..."; "Canonical interpretation..."; "Use this as the default reading..." |
| P3 | Bridge mapping | A mapping between SRT and another theory, domain, model, or scale. It may be useful and strong, but it depends on an interface. | "maps to..."; "can be modeled as..."; "bridge claim..."; "under this mapping..." |
| P4 | Lab hypothesis | A testable, measurable, empirical, or threshold-bearing claim. It may generate predictions or operational proxies. | "hypothesis..."; "candidate proxy..."; "to be tested..."; "under these measurement conditions..." |
| P5 | Phenomenological / companion exposition | A lived, pedagogical, literary, praxis, or companion explanation. It may be valuable but does not bear core-theory proof load. | "as exposition..."; "phenomenologically..."; "companion reading..."; "helps describe..." |

---

## 2. Relation to File Roles

File roles and claim levels do not automatically determine each other.

| File role | Typical claim levels | Rule |
|---|---|---|
| canonical | P0-P2, with occasional marked P3/P4 | Must mark mixed lower-hardness claims clearly |
| compact core | P1-P3 | May summarize P0/P1 but should link to canonical sources |
| bridge | P2-P4 | Must not silently upgrade mappings into axioms |
| lab | P4 | Must keep measurement/proxy conditions visible |
| navigation / registry / index | usually no substantive claim level | Should route to sources, not define theory |
| companion / praxis / public exposition | P5 plus quoted P0-P2 | Must distinguish explanation from definition |

The same file may mix P-levels. If it does, mark the level at least at section level. Inline marking is preferred for high-risk statements.

---

## 3. Level-Specific Tests

### P0 Test

A statement can be P0 only if:

1. Removing it breaks SRT's core grammar.
2. It does not require empirical data to become meaningful.
3. It does not borrow authority from another theory.
4. It is not more cleanly derivable from other SRT claims.

Failure of any condition means demote.

### P1 Test

A statement can be P1 only if:

1. Its premises are already P0 or accepted P1.
2. The derivation path is stated or obvious from the formal context.
3. Its negation would break the SRT structure or carry a high internal contradiction cost.

If it depends on a domain mapping or threshold, it is not P1.

### P2 Test

A statement can be P2 when:

1. SRT repeatedly uses it as a stable interpretation.
2. It clarifies the meaning of core terms.
3. It does not by itself claim external validation.

P2 may be canonical in practice without becoming P0/P1.

### P3 Test

A statement is P3 when it says that an SRT structure maps onto another theory, domain, or scale.

Typical markers:

- "physics-scale realization"
- "AI analogue"
- "neuroscience implementation"
- "Fisher / information-theory expression"
- "spirituality / praxis reading"

P3 can be strong. It is still not a primitive axiom.

### P4 Test

A statement is P4 when it involves:

- thresholds
- empirical proxies
- measurable predictions
- falsification conditions
- operational criteria
- lab or field validation

P4 should name its measurement boundary whenever possible.

### P5 Test

A statement is P5 when its main function is:

- human orientation
- lived description
- metaphor
- companion exposition
- practice guidance
- pedagogical compression

P5 may be important for understanding, but it cannot carry proof load.

---

## 4. Mixed Files

A file may contain different P-levels if one of the following is true:

1. The frontmatter declares `claim_mode: mixed`.
2. The file has a claim-level map near the top.
3. Each major section marks its level.

Recommended section prefix:

- `P0-Ax`
- `P1-T`
- `P2-Interp`
- `P3-Bridge`
- `P4-Hyp`
- `P5-Companion`

For older files, a short header block is enough:

```md
> Claim-level note: this file is mainly P3 bridge. It quotes P0/P1 claims but does not define them.
```

---

## 5. Promotion and Demotion

### Promotion

A claim may be promoted only when the missing support is explicit:

- P4 -> P3: empirical proxy becomes a stable bridge mapping.
- P3 -> P2: mapping becomes a stable SRT interpretation not dependent on the external domain.
- P2 -> P1: interpretation is shown to follow from the core structure.
- P1 -> P0: only in rare cases where the theorem is discovered to be primitive and non-derivable.

Promotions touching P0/P1 must cross-check:

1. `_SRT_SYMBOL_TABLE.md`
2. `CANONICAL_REGISTRY.md`
3. the relevant core/canonical file

### Demotion

Demotion is not deletion. It means:

- the claim remains available;
- its proof burden is lowered;
- its voice becomes more honest;
- domain files lose permission to quote it as primitive.

This is the default response to ambiguity.

---

## 6. Domain Rule

Domain files may support, test, interpret, or expose SRT. They may not reverse-define the SRT core.

Minimum header for domain main files:

```md
> Role: [bridge / companion / praxis / domain exposition]
> Claim level: mainly P3/P4/P5, with explicit back-links to P0/P1 sources.
> Does not define: primitive axioms, d-value, Ψ_f, T_dir, L0/L1/L2, or real choice moment.
> Depends on: [canonical files]
```

If a domain file needs a new P0/P1 claim, it must be moved or mirrored into the appropriate core/canonical file through the edit protocol.

---

## 7. Citation Rules

When citing a claim:

- Cite P0/P1 claims from core/canonical files.
- Cite P2 interpretations with the phrase "canonical interpretation" when hardness matters.
- Cite P3 mappings with the phrase "bridge" or "mapping."
- Cite P4 claims with the phrase "hypothesis," "proxy," or "candidate criterion."
- Cite P5 material as exposition, not evidence.

Forbidden citation pattern:

> "Because the AI file says X, SRT's primitive axiom is X."

Allowed citation pattern:

> "The AI file uses X as a P3 bridge mapping back to the P0/P1 core in..."

---

## 8. Current Immediate Application

`Core/SRT_Core_21_Formal_Axioms.md` has been split into:

- `Core/SRT_Core_21_Minimal_Axioms.md` — P0
- `Core/SRT_Core_21b_Constitutive_Theorems.md` — P1
- `Core/SRT_Core_21c_Bridge_Hypotheses.md` — P2/P3/P4

This split changes epistemic placement, not the underlying intended theory.
