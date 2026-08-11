---
id: SRT-PAPER-FORCING-CH-CONTROL-ARCHIVE-UNIT-JSL-1953-1955-PARADOX-01
title: "Corpus Archive Unit — Shen–Stanley–Müller–Montague"
type: evidence_corpus_archive_unit
status: active
canonical: false
layer: philosophy_bridge
epistemic_layer: evidence
claim_mode: evidence
date: 2026-08-11
updated: 2026-08-11
unit_key: CAU-JSL-1953-1955-PARADOX-01
unit_state: assembled_page_verified
candidate_enumeration: false
part_ii_attested: false
governed_by: Philosophy/Papers/Forcing_CH_Evidence/CONTROL_ARCHIVE_ADEQUACY_CERTIFICATE_v0_1.md
---

# Corpus Archive Unit — Shen–Stanley–Müller–Montague

**Unit key:** `CAU-JSL-1953-1955-PARADOX-01`

**Archive status:** assembled and page-verified corpus material under `CONTROL_ARCHIVE_ADEQUACY_CERTIFICATE_v0_1` §4.2. This is not a candidate record.

> **SCOPE LOCK**
>
> This record performs corpus reconstruction and a local evidentiary-capacity audit only. It creates no candidate pool and makes no admission, exclusion, scoring, ranking, selection, or individuation judgement. Part II remains unsigned. It does not modify the fixed boundary, either frozen protocol, the staged manuscript, `EVD-D05-0001`, `EVD-D05-0005`, `EVD-D04-0002`, D06 `H/N/S`, institutionalization, or any forcing/SRT verdict.

## 1. Unit composition and page map

| Stable key | Role in the unit | Exact page checked |
|---|---|---|
| `SHEN1953-GROUNDED-CLASSES` | in-window primary publication | JSL 18(2), p. 114, entire publication including footnote 1 |
| `STANLEY1953-NOTE-PARADOX` | in-window primary publication | JSL 18(3), p. 233, entire publication and displayed derivations |
| `MULLER1955-SHEN-STANLEY-REVIEW` | contemporaneous review | JSL 20(1), p. 84, joint review entry from bibliographic headings through signature |
| `MONTAGUE1955-GROUNDED-CLASSES` | contemporaneous technical reconstruction | JSL 20(2), p. 140, entire publication |

Full metadata, page-verification states, evidentiary functions, and limitations are registered in `CONTROL_ARCHIVE_SOURCE_MANIFEST.md`.

## 2. Shen 1953 — controlled reconstruction

### 2.1 Groundless and grounded

Shen calls a class `A` **groundless** when there is an infinite progression `A₁, A₂, …`, not necessarily of distinct classes, with

\[
\cdots \in A_2 \in A_1 \in A.
\]

A class is **grounded** when it is not groundless. This is an infinite descending-membership condition, not merely self-membership.

### 2.2 The class of all grounded classes

Let `K` be the class of all grounded classes.

1. If `K` were groundless, a chain beginning with `A₁ ∈ K` would make `A₁` both grounded (by membership in `K`) and groundless (by the tail of the chain). Hence `K` is grounded.
2. Because `K` is grounded, `K ∈ K`.
3. Repeating `K` produces an allowed infinite membership progression `… ∈ K ∈ K ∈ K`, so `K` is groundless.

The contradiction therefore uses the definition of the total class together with an infinite chain whose terms need not be distinct.

### 2.3 Related finite forms and the referee notice

Shen also defines circular and `n`-circular classes and states analogous paradoxes for the classes of all non-circular and all non-`n`-circular classes. Footnote 1 records that the referee pointed to Quine, *Mathematical Logic*, revised edition (1951), pp. 128–130, result `*181`, as amounting to the same result as the non-`n`-circular paradox. This is evidence of a contemporaneous priority notice, not an independent verification of Quine’s text in this unit.

## 3. Stanley 1953 — controlled reconstruction

Stanley begins from Russell’s class and its finite-cycle relatives `R₀, R₁, R₂, …`, whose self-membership substitutions yield the familiar contradiction under unrestricted rules of inference. He then identifies a class condition that is doubly paradoxical:

- **self-paradoxical:** substituting the constructed class into its own defining condition yields a contradiction concerning its own membership;
- **complement-paradoxical:** the corresponding substitution for the complement yields a second contradiction, unlike the behavior Stanley reports for the `R_i` series.

Stanley next replaces the Russell-style class condition by one carrying a Curry conditional with the false consequent `2+2=5`. The displayed derivations reproduce the same two-sided pattern in Curry form. Stanley’s own technical claim is therefore a relation between the constructed class condition and two already existing paradox-generating forms. He also says that no parallel `K_i` series had yet been found. None of this by itself decides whether the constructions instantiate one modern method family.

## 4. Müller 1955 — contemporaneous reception

Müller’s joint review supplies three bounded period assessments.

1. He reconstructs Shen’s groundless, circular, and `n`-circular definitions and says that the contradictory classes are obtained by the **“familiar Russell method.”** The phrase applies to the contradiction pattern used for those three total classes. It is not a judgement about every component in Shen’s paper, Stanley’s separate construction, or any modern operation-family boundary.
2. He repeats the referee’s priority notice: the non-`n`-circular result had also been derived in Quine’s `*181`.
3. He describes Stanley’s first pair of equivalences as related to Russell’s paradox and the conditional pair as related to Curry’s paradox in the corresponding way.

The review is evidence of contemporaneous description and perceived technical relation. Its compact wording must not be expanded into an admission, novelty, or individuation verdict.

## 5. Montague 1955 — contemporaneous technical reconstruction

Montague identifies Shen’s result as a new paradox of intuitive set theory and restates the grounded-class condition. He then removes the explicit use of natural numbers and infinite sequences.

### 5.1 Regular classes

Montague calls `x` **regular** exactly when every class `k` containing `x` contains some `y` for which no member `z` of `k` belongs to `y`:

\[
(k)\bigl(x\in k \supset (\exists y)(y\in k\;\land\;\neg(\exists z)(z\in k\land z\in y))\bigr).
\]

Let `Reg` be the class of all regular classes.

### 5.2 The `Reg` contradiction

- Assuming `Reg` is regular forces `Reg ∈ Reg`; applying regularity to the singleton-like class described by `z = Reg` requires a member with no predecessor there, but `Reg` itself supplies the prohibited predecessor relation.
- Assuming `Reg` is non-regular supplies a class `k` containing `Reg` in which every member has a predecessor in `k`. A member of `k` that is also in `Reg` then yields the opposite existential condition, contradicting that assumption.

Thus `Reg` is neither regular nor non-regular in the unrestricted intuitive-class setting.

### 5.3 Relation to Shen

Montague states that, with the aid of the axiom of choice, the regular classes are exactly Shen’s grounded classes. The source therefore supplies an explicit period representation change and a conditional relation between the two formulations. Because the equivalence is asserted rather than proved on p. 140, it supports representation comparison but not a complete conservative-substitution or removal analysis.

## 6. Part II §2(2) — local contemporaneous-record capacity

`§2(2) demonstrated for this archive unit`

The unit contains:

- the authors’ own primary publications;
- a period review jointly characterizing both 1953 publications;
- and a period technical reconstruction that changes the formulation and relates it back to Shen under a stated assumption.

This is a local capacity finding only. It must not be restated as `§2(2) globally attested`, because no full-period or full-subfield archive has been assembled.

## 7. Part II §2(3) — six-test runnability capacity

The statuses below concern whether the **record is deep enough to support a future test**, not the result of applying the individuation protocol to this unit.

| Frozen test | Capacity status | Archive-depth reason |
|---|---|---|
| 1. Historical availability | **partially demonstrated** | The 1953 primaries and 1955 reception/reconstruction are directly available and dated. Russell, Curry, and Quine are present only through the four sources’ own references; their baseline texts and the wider earlier repertoire have not been independently assembled here. |
| 2. Functional role | **demonstrated** | The primaries specify the infinite-chain, complement, and conditional constructions, and Montague specifies the regular-class replacement and where it enters the contradiction. The role of the principal components can be reconstructed from the reached pages. |
| 3. Load-bearing removal/replacement | **insufficient** | The one-page publications and one-page reconstruction do not distinguish, with source-backed control, whether removing a component destroys the target generation relation or merely degrades, lengthens, or reformulates it. Montague shows an alternative presentation, but not the required destruction-versus-degradation comparison. |
| 4. Conservative substitution | **partially demonstrated** | Montague supplies a candidate substitution and states equivalence to groundedness under choice. The record does not establish the full earlier repertoire, type-correct alternatives, or a source-backed no-substitute result. |
| 5. Representation invariance | **demonstrated** | Shen’s infinite-sequence formulation and Montague’s regular-class formulation provide a real period representation change, with an explicit axiom-of-choice relation. This makes the bounded invariance question runnable without deciding it here. |
| 6. Granularity sanity | **partially demonstrated** | The record distinguishes contradiction output, defining class condition, and inherited Russell/Curry descriptions, which blocks immediate output-only collapse. It lacks enough removal and repertoire evidence to check both the coarseness and fineness bounds completely. |

Because one test is **insufficient** and three are only **partially demonstrated**, §2(3) is not attested even for this local unit, much less globally. Part II remains unsigned.

## 8. Part II §2(4) — coverage statement

This is one local archive unit covering:

- *The Journal of Symbolic Logic*;
- 1953–1955;
- a paradox / intuitive-set-theory cluster.

It does not establish:

- 1938–1963 full-period coverage;
- mathematical-logic subfield coverage;
- exhaustive JSL coverage;
- or review-of-record coverage beyond the reached Müller entry.

The unit was obtained opportunistically from supplied materials. It is not the result of a systematic sweep. Detailed reached/not-reached fields are in `CONTROL_ARCHIVE_COVERAGE_LOG.md`.

## 9. Minimum remaining corpus requirements

For Part II to become signable later, the minimum missing evidence functions are:

1. **Additional in-window logic-subfield and temporal breadth.** Assemble archive units outside this local paradox cluster, including material from separated portions of the fixed 1938–1963 window, so the archive is not a single-venue, two-year pocket.
2. **Review-of-record coverage.** Record a declared sweep or sample of period review/survey venues across the fixed boundary, with reached and not-reached ranges, rather than relying on one supplied review.
3. **At least one technically deep construction record.** Add primary and contemporaneous reconstruction detail sufficient to distinguish removal-induced destruction from mere degradation and to assess type-correct conservative substitution.
4. **Explicit exhaustive/sample boundaries.** For every venue/year block relied on, state what was exhaustively swept, what was sampled, and what was not reached, so an empty result can be distinguished from a thin archive.

These are evidence functions, not a list of works and not a candidate pool. Existing sources in this unit are not re-enumerated as future requirements.

## 10. Explicit non-enumeration statement

No candidate was enumerated. The four sources remain corpus material regardless of how completely they were read. No candidate-directed search, admission/exclusion screening, scoring, ranking, selection, or control-case individuation was performed.
