---
id: SRT-CORE-21A-MINIMAL-AXIOMS
type: axiom_set
tags: [Formal logic, Axioms, Minimal Core, Claim Ladder]
status: active_v1
layer: L1
epistemic_layer: os
claim_mode: canonical
claim_level: P0
dependency: [SRT-CORE-21, SRT-CLAIM-LADDER, SRT-L0-METAPHYSICS, SRT-SYMBOL-TABLE]
---

# SRT Core 21A: Minimal Axioms

> **Role**: This file contains only the strict P0 primitive axioms required for the SRT core to stand.
> It does not carry constitutive theorems, canonical interpretations, bridge mappings, lab hypotheses, or domain expositions.

## Quick Reference

- Claim level: **P0 = Primitive axiom**
- Numbering note: `P0-00` is a vocabulary gate / preface, not an additional substantive axiom.
- Source lineage: split from `Core/SRT_Core_21_Formal_Axioms.md`
- Governing ladder: `Governance/SRT_CLAIM_LADDER.md`
- Companion layers:
  - `Core/SRT_Core_21b_Constitutive_Theorems.md`
  - `Core/SRT_Core_21c_Bridge_Hypotheses.md`

## Inclusion Rule

A claim belongs here only if all four conditions hold:

1. Without it, SRT loses its core grammar.
2. It does not depend on a domain bridge such as AI, neuroscience, spirituality, physics, or social theory.
3. It does not depend on an empirical threshold, external model, or comparative mapping.
4. It is not better treated as a theorem derived from the SRT core.

When in doubt, demote to `P1` or below.

---

## Selection-First Framing Note (Non-Axiom)

SRT does not treat stable reality as a pre-given set of objects to which selection is later applied. Its starting point is selection-first: latent possibilities become manifest through constrained selection, and repeated manifestations harden into future constraints. The theory's cross-scale explanatory power comes from this floor replacement, not from an unrestricted claim to explain everything.

**Boundary**: This note frames the P0 set but does not add a new primitive axiom. It should not be cited as proof that all prior ontologies are false; rather, it marks the SRT departure from object-first ontology.

---

## P0-00: Formal Vocabulary Gate (Preface)

SRT minimally works with:

- `L_0`: latent / unselected possibility domain.
- `L_1`: manifest / selected reality slice.
- `L_2`: convergence / sedimented selection-history domain.
- `\hat{G}_\theta`: embodied selection / anchoring operator.
- `\Psi_f`: ontological friction / payability burden.
- `d-value`: existential stake radius / risk-coupled concern bandwidth.

This is a vocabulary gate, not an additional substantive axiom. Canonical definitions remain distributed through:

- `Core_Law/SRT_L0_Metaphysics.md`
- `_SRT_SYMBOL_TABLE.md`
- `_SRT_D_VALUE_CANONICAL.md`
- `_SRT_PSI_F_CANONICAL.md`
- `_SRT_T_DIR_CANONICAL.md`

**P0 purity note**: `P0-00` keeps a P0-style number only because it fixes the notation required to read the P0 set. It should not be cited as a separate axiom or as an independent theoretical burden.

---

## P0-01: Primacy of Selection

**Lineage**: former `Ax-F-01`.

**Formal Definition**: Selection precedes existence; existence is an image of selection.

$$
\exists x \iff x \in \mathrm{Range}(\hat{G})
$$

**Implication**: Existence is not a passive background given in advance. It is what appears as the output of selection / anchoring.

**Boundary**: This axiom does not by itself specify the domain mechanism, empirical substrate, or consciousness condition of any particular selector.

---

## P0-02: Existence as Anchoring

**Lineage**: former `Ax-F-02`.

**Formal Definition**: Existence equals stable anchoring against entropic flow.

$$
E = 1 - \frac{H(L_1)}{H(L_0)}
$$

**Implication**: Reality is the degree to which a selected slice has been stably anchored from open possibility.

**Boundary**: The equation is a compact formal handle for anchoring intensity. It should not be cited as an empirical measurement protocol without a bridge or lab layer.

---

## P0-03: Irreversible Selection Trace

**Lineage**: distilled from former `Ax-F-03b` and the core SRT claim that selection is not a reversible readout.

**Minimal Claim**: Once a selection is anchored into `L_1` and leaves history in `L_2`, it cannot be treated as never having occurred. Any reversal is itself a new selection event with its own trace.

**Implication**: SRT requires historical asymmetry. Without irreversible trace, `L_2`, stable perspective, and real choice moments collapse into reversible bookkeeping.

**Why P0 here**: This entry does not carry the fuller theory of ontological time, causality, or stable ISP. It only preserves the irreversibility floor needed for `L_2` and real choice to mean anything in SRT. The derived expressions and scoped theorems remain P1 in `Core/SRT_Core_21b_Constitutive_Theorems.md`.

**Boundary**: The fuller ontological-time expression is not primitive here; it is carried as a P1 theorem in `Core/SRT_Core_21b_Constitutive_Theorems.md`.

---

## P0-04: Operator Well-Formedness

**Lineage**: former Part B `A4` ("dynamics definability").

**Minimal Claim**: `\hat{G}_\theta` must be a well-formed selection operator over an admissible state space. It must be sufficiently definable for SRT claims to have an object.

Legacy compact form:

$$
\hat{G}_\theta : S \to S
$$

**Implication**: SRT cannot make formal claims about selection if the selection operator is undefined, non-addressable, or outside any admissible state space.

**Boundary**: This does not assert a specific implementation of `\hat{G}_\theta`; implementation details belong to bridge, domain, or lab layers.

### P0-04 Exposure Note: Origin of Selectability

> **Level**: core boundary / unresolved ontology exposure. This note does not solve the origin of selectability.

P0-04 gives SRT a minimum object for formal claims: an admissible selection operator. It does **not** derive the first possibility of selecting from a prior non-selective ground.

Current dependency split:

| Claim type | Relation to P0-04 |
|---|---|
| minimal claims about operator well-formedness, trace, irreversibility, and `L_1/L_2` anchoring | valid once an admissible `\hat{G}_\theta` is given |
| claims about `d`, `Ψ_f`, `T_dir`, reorientation, concern, agency, or subject-like selection | downstream of assuming a selector / selectable operator exists |
| bridge claims about biology, AI, spirituality, society, or political agency | may instantiate or constrain selectability, but must not be back-cited as a derivation of its origin |

Therefore, files may cite P0-04 as an exposure point or admission condition. They must not cite a downstream bridge as if it had closed the origin problem.

---

## Demoted From The Old "Minimal Core"

The former hybrid `Core_21` placed several claims beside the primitive axioms. In the claim ladder they are now separated:

| Former item | New role | New home |
|---|---:|---|
| `Ax-F-03` causality as projection | P1 constitutive theorem | `Core/SRT_Core_21b_Constitutive_Theorems.md` |
| `Ax-F-03b` ontological time expression | P1 constitutive theorem | `Core/SRT_Core_21b_Constitutive_Theorems.md` |
| `Ax-F-04` information-existence equivalence | P2 canonical interpretation / P3 bridge when formalized through external information theory | `Core/SRT_Core_21c_Bridge_Hypotheses.md` |
| `Ax-F-05` fitness beats truth | P3/P4 bridge hypothesis | `Core/SRT_Core_21c_Bridge_Hypotheses.md` |
| `Ax-F-06` assembly threshold | P4 lab / empirical threshold hypothesis | `Core/SRT_Core_21c_Bridge_Hypotheses.md` |
| `Ax-F-07` holographic duality | P3/P4 bridge hypothesis | `Core/SRT_Core_21c_Bridge_Hypotheses.md` |
| `Ax-F-09` scale consistency | P3 bridge mapping | `Core/SRT_Core_21c_Bridge_Hypotheses.md` |
| `Ax-F-11` ghost operator universality | P3 high-ambition bridge | `Core/SRT_Core_21c_Bridge_Hypotheses.md` |
| `Ax-F-12` Fisher-form `\Psi_f` generativity | P2/P3 mixed canonical interpretation / bridge | `Core/SRT_Core_21c_Bridge_Hypotheses.md` |
| `Ax-F-13` strong information-creation unification | P2/P3 mixed canonical interpretation / bridge | `Core/SRT_Core_21c_Bridge_Hypotheses.md` |

This demotion changes epistemic rank, not the intended theoretical meaning of those claims.
