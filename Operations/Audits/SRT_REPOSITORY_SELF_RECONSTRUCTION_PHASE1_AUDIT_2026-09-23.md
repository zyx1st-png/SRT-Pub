---
id: SRT-REPOSITORY-SELF-RECONSTRUCTION-PHASE1-AUDIT-20260923
type: audit
status: active
date: 2026-09-23
layer: operations
epistemic_layer: operations
claim_mode: audit
canonical: false
research_mode: U
comparative_claim: none
named_comparator: none
dependency:
  - Core_Law/SRT_Irreversibility.md
  - Core/SRT_Core_21_Minimal_Axioms.md
  - Core_Law/SRT_Generative_Ontology_Spine.md
  - Core_Law/SRT_L0_Metaphysics.md
  - CANONICAL_REGISTRY.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_O0_PRIMITIVE_GENERATIVITY_2026-09-14.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_SELECTION_TOTALITY_NONFLAT_MONISM_2026-09-14.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_SELECTION_GENERATIVE_VERTICAL_DYNAMICS_2026-09-22.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GRG_GENERATIVE_CAPACITY_INTERVENTION_GRAMMAR_2026-09-22.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GRG_REACH_RECONSTRUCTIBILITY_GENERATIVE_DEBT_2026-09-22.md
tags: [RepositoryReconstruction, Selection, Provenance, Vocabulary, GRG, GenerativeDebt]
---

# Repository self-reconstruction — Phase 1 audit and bounded reconciliation plan

## 0. Baseline and scope

Verified live `main` before this audit:

```text
94e144d4ee7650b5805bca5586e75b69dc05b4ac
```

This pass treats recent external review as a hypothesis source only. Findings below are independently checked against live repository owners, author source and governance.

This audit does not authorize BCTB T2, new cross-domain experiments, wholesale GRG canonicalization, or closure of currently OPEN theory questions.

## 1. Selection canonical conflict — CONFIRMED

`Core_Law/SRT_Irreversibility.md` already carries the correct typed decomposition:

```text
A. occurrence non-equivalence
B. retained historical efficacy
C. declared path dependence
D. declared absorbing / terminal dynamics
```

Only A follows unconditionally from P0-03.

The following active surfaces still encode the superseded stronger 2026-09-22 criterion that Selection occurrence itself requires retained / inheritable later consequence:

```text
Core/SRT_Core_21_Minimal_Axioms.md
Core_Law/SRT_Generative_Ontology_Spine.md
Core_Law/SRT_L0_Metaphysics.md
SRT_AI_START.md
CANONICAL_REGISTRY.md
```

The three first files are Freeze-A canonical owners. The latter two are routing/bootstrap mirrors and must not become competing definition owners.

## 2. Author-source reconciliation — SUFFICIENT FOR BOUNDED CORRECTION

The earlier same-day source `SRT_AUTHOR_ADJUDICATION_SELECTION_GENERATIVE_VERTICAL_DYNAMICS_2026-09-22.md §A` strengthened Selection into:

```text
actualised non-neutral differentiation
+ not-fully-erasable generative consequence
```

but that same file's later §Q explicitly points to the continuation record as a correction.

The later same-day author record `SRT_AUTHOR_ADJUDICATION_GRG_GENERATIVE_CAPACITY_INTERVENTION_GRAMMAR_2026-09-22.md §A` explicitly separates:

```text
Selection occurrence
!= Selection sediment
!= generative inheritance
!= wholeward integration.
```

It also restores the terminal case:

```text
a genuine Selection can occur
even if no later process remains
in which sediment can persist.
```

This matches the earlier 2026-09-14 hard guard in `SRT_AUTHOR_ADJUDICATION_O0_PRIMITIVE_GENERATIVITY_2026-09-14.md §G`:

```text
terminal Selection as ontologically defective: REJECTED.
```

Therefore the occurrence/sedimentation correction does not require a new author theory decision.

## 3. What remains OPEN after the correction

The correction must not make Selection synonymous with arbitrary change.

Preserve:

```text
Selection
!= conscious choice
!= choosing from a completed pre-given menu
!= arbitrary descriptive change / arbitrary state transition.
```

Remain OPEN:

```text
What distinguishes genuine actualised Selection
from merely descriptive / modelled change?
```

The 2026-09-14 O0 wording supplies a candidate anti-tautology route:

> the generative relation through which determinate actuality is instituted cannot be completely flattened into a role-interchangeable occurrence relation without erasing the very differentiation by which it is generative.

This candidate must not be silently converted into a requirement for durable later sediment.

## 4. Exact Phase 2 correction contract

### 4.1 Core 21A

Replace P0-01's retained-consequence criterion with actual non-neutral generative differentiation.

State explicitly:

```text
Selection occurrence
!= retained historical efficacy
!= sedimentation
!= generative inheritance.
```

Route occurrence non-equivalence to P0-03 / Irreversibility A.

Replace the current rule:

```text
fully generatively reversible fluctuation with no retained / inheritable consequence
= NOT Selection
```

with the narrower guard:

```text
descriptive / model-reversible variation
does not by itself establish Selection;

absence of later retained / inheritable consequence
does not by itself negate an otherwise genuine terminal Selection.
```

Keep the exact actualisation-vs-description criterion OPEN.

### 4.2 L0 Metaphysics

Remove retained consequence as a necessary Selection-occurrence criterion.

Keep:

```text
actual occurrence
!= anchoring persistence
!= durable / localized history
!= recurrent historical efficacy.
```

Make the existing terminal-Selection paragraph consistent with the term-of-art guard rather than leaving the two in internal tension.

### 4.3 Generative Ontology Spine

Retype primitive Selection to actual non-neutral generative differentiation without mandatory retained consequence.

Keep §4 History as the stronger conditional branch:

```text
prior Selection
-> may leave retained differences
-> where retention is established, materially alters later Selection.
```

### 4.4 Bootstrap / registry

`SRT_AI_START.md` and `CANONICAL_REGISTRY.md` should compress the corrected owner reading and point to the later same-day author correction.

They must not add a new anti-tautology criterion.

## 5. Generated / mirror closure

The semantic correction changes registered Context Bundle inputs.

Generated files under:

```text
Operations/Context_Bundles/
```

must be rebuilt only by:

```bash
uv run python scripts/build_srt_context_bundles.py
uv run python scripts/build_srt_context_bundles.py --check
```

No generated bundle may be hand edited.

`Core_Law/SRT_Core_Text_CN.md` and its explicit English mirror retain broader historical irreversibility prose. They are not definition owners for this bounded repair. They should be reviewed as a separate consumer/mirror truth-up only if the corrected canonical owners show a live contradiction requiring it; do not expand Phase 2 opportunistically.

## 6. Vocabulary reconciliation map — Phase 3 contract only

| 2026-09-22 term | Existing owner / vocabulary | Current relation | Planned action |
|---|---|---|---|
| Selection occurrence | P0-03 + Irreversibility A | exact primitive occurrence floor | INHERIT |
| sedimentation | Spine §4 / L0 history / L2 retained efficacy | stronger later-history burden | INHERIT |
| generative asymmetry | O0/S0 non-flat role structure + actualising differentiation | analytic face of Selection, not a second primitive | RETYPE |
| friction / constitutive friction / boundary friction | `Psi_f` owner + GRG research friction | partial overlap; boundary mismatch is not automatically canonical `Psi_f` | DISTINGUISH |
| expectation | `E_G` + prior generative-expectation adjudications / ledger | already typed programme vocabulary | INHERIT |
| generative inheritance | X4c / carrier architecture / prior inheritance work | broader author-level phrase than any one X4c case | DISTINGUISH |
| proxy | measurement-proxy vocabulary + 09-22 operative generative partition | collision confirmed | DISTINGUISH |
| support | earlier gain-of-generativity wording vs later neutral routing/buffering wording | later same-day source narrows mechanism and permits parasitic/integrative outcomes | RETYPE |
| generative reach | existing reachability / accessibility / propagation language | new research-level structural propagation grammar; not identical to reachability | KEEP AS RESEARCH TERM |
| reconstructibility | provenance / retrieval / reconstruction infrastructure | theory term is broader than repository retrieval mechanics | DISTINGUISH |
| generative debt | repository/theory debt language | new narrow GRG research burden, not ordinary repo debt | DISTINGUISH |

Phase 3 must not preserve a 2026-09-22 label merely because it is recent.

## 7. Support conflict — CONFIRMED, correction available without new theory choice

Earlier 2026-09-22 source:

```text
support
-> closes / suppresses some possibilities
   and opens / organizes others
   such that the higher-order whole gains generativity.
```

Later continuation:

```text
support
= helps determine how consequences
  persist, localize, buffer, translate, amplify or propagate.
```

The later form is neutral with respect to outcome and is compatible with:

```text
integrative support
parasitic / compensatory support.
```

Phase 3 should therefore retype the base term neutrally rather than define support as necessarily generativity-increasing.

## 8. Provenance debt — CONFIRMED

The v0.3 GRG owner already defines the provenance schema:

```text
A0-Q = direct author quotation
A0-P = faithful author paraphrase
A1   = machine consolidation explicitly accepted by author
M    = machine synthesis / research proposal
```

The three 2026-09-22 author-adjudication files mostly use blanket prose such as “the author accepts” rather than local A0/A1/M labels. Location under `01_Source_Intuition/` is not sufficient to resolve origin.

Direct author-originated events that must remain reconstructible include at least:

- the AI-era intuition preserved as “low-cost construction and tracing of reconstructibility”;
- the direct forgetting/reach question preserved in the derivation trace: “Is generative forgetting not just the vertical structure using reach to flatten differences?”;
- explicit author acceptance of the narrow generative-debt definition.

Progressive reconstructibility, generative redundancy, active/latent reach, friction conversion and similar machine-generated consolidations that were later accepted must be labelled A1 rather than rewritten as if they were A0.

The derivation trace must remain intact; provenance repair must add typing, not fabricate a cleaner history.

## 9. BCTB provenance state

Main contains the programme-level consequence:

```text
BCTB relation-transfer calibration = secondary diagnostic candidate;
relation-transfer != clarified GRG core burden;
T2 = not automatic.
```

The actual T1 execution package and scored packets were explicitly kept off main under the separate execution ref described by PR #1027.

Therefore main currently preserves the rebase conclusion but not a self-contained minimal evidence lineage sufficient to reconstruct why T1 caused that rebase.

Required later action:

```text
minimal provenance landing only
-> identify frozen T1 result / packet lineage
-> record the bounded inference to secondary-diagnostic status
-> no rerun
-> no T2
-> no promotion of benchmark result into theory authority.
```

## 10. STATUS / owner drift — CONFIRMED

Current STATUS contains three simultaneous routing layers:

1. §0.4 / §0.4a — latest 2026-09-22 theory-rich summaries;
2. §0.5 — older 2026-09-20/21 “current” GRG owner / next sequence;
3. `Immediate routing` — a long 09-21 execution ledger whose item 81 still says to select the next underconstrained burden.

This is reconstructible history but not a clean single-current route.

Phase 4 should make STATUS a compact execution/router surface, mark superseded routes provenance-only, and retain one current next.

## 11. GRG owner convergence — preferred bounded route

Do not create a v0.4 foundational owner merely to absorb 09-22 vocabulary.

The latest author sources explicitly say the reach/reconstructibility architecture should be pressure-tested before wholesale canonical landing.

Preferred current disposition is therefore the minimal-authority route:

```text
Option C:
v0.3 remains the bounded foundational owner for the grammar already admitted there;
09-22 reach / reconstructibility / generative-debt concepts remain source-level research terms;
v0.3 and STATUS gain an explicit synchronization boundary rather than pretending full incorporation.
```

This is a routing/authority decision supported by the latest source guards, not a new theory decision.

## 12. Governance gaps

Repository history repeatedly uses independent content review before major canonical landings, but `Governance/SRT_EDIT_PROTOCOL.md` does not currently state a general C/foundation-level pre-merge independent-content-review rule.

No general governance rule was found that forbids direct Freeze-A editing while a same-day author dialogue is still rapidly generating and unresolved.

Phase 4 should add only these missing general guards, without duplicating the many historical one-off review gates:

1. unresolved same-day rapid author dialogue -> source/adjudication first; no direct Freeze-A semantic landing until the dialogue is bounded;
2. C-class / foundation-level canonical semantic edit -> independent content review before merge.

## 13. Phase boundary

Phase 2 may proceed because Selection occurrence vs sedimentation is already author-decided.

After semantic owner edits:

```text
regenerate deterministic Context Bundles
-> --check
-> strict governance preflight
-> independent content review
```

If the execution environment cannot run the owning generator, STOP at the generated-closure boundary. Do not hand edit bundles and do not enter Phase 3 before Phase 2 closes.
