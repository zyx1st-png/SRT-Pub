---
id: EC-THERMO-LANDAUER-SELECTION-COST
type: evidence_card
status: draft_v1
layer: external_convergence
claim_mode: external_convergence
canonical: false
domain: physics_thermodynamics
evidence_level: E2
target_srt_anchor:
  - selection_cost
  - Psi_f
---

# Evidence Card: Landauer Principle / Irreversible Record Formation as a Candidate Interface for Selection Cost and `Psi_f`

This draft card records a sourced structural-convergence candidate. It is not canonical, not accepted evidence, and not proof of SRT.

## 1. External finding

Landauer's principle states that logically irreversible information processing, classically exemplified by erasing one bit, has a thermodynamic cost: in an environment at temperature `T`, erasure is associated with a minimum heat dissipation of order `kT ln 2` per bit under ideal conditions.

The checked literature also sharpens the boundary:

- logical irreversibility, thermodynamic irreversibility, and heat generation are related but not identical;
- reversible computation is a central pressure case, because computation can in principle be arranged so that information is not logically erased at each step;
- information thermodynamics studies feedback, measurement, erasure, and the thermodynamic bookkeeping of information processing, but its claims remain physical and protocol-dependent;
- durable records, resets, and erasures are better candidates for this card than every informal act of "choice."

For SRT, this suggests a candidate physical interface for selection cost: when a physical system turns alternatives into a durable record, resets a memory, or erases distinguishable states, the operation is not automatically cost-free. This is only a structural convergence / bridge-support candidate.

## 2. Source domain

Physics / thermodynamics of computation / information thermodynamics / statistical physics.

## 3. SRT construct involved

Primary SRT anchors:

- selection cost as the burden of constraining alternatives into a maintained outcome.
- [`../../_SRT_PSI_F_CANONICAL.md`](../../_SRT_PSI_F_CANONICAL.md), especially the boundary that physical, metabolic, and geometric readings of `Psi_f` are projections / proxies rather than replacements for the canonical anchor.

This card concerns physical erasure / reset / durable record formation. It does not treat thermodynamic cost as a universal definition of selection cost.

## 4. Support type

Structural convergence and bridge-support candidate.

This is not an operational proxy yet. It becomes operational only if a later card specifies a physical system, a memory or record protocol, a temperature / entropy accounting frame, and a measurable link between erasure / reset / record formation and SRT-relevant selection burden.

## 5. Evidence level: E0-E5

E2 = structural convergence.

Reason for E2: Landauer-style information thermodynamics provides a mature physical framework in which erasing, resetting, and recording information carry constrained thermodynamic bookkeeping. That structure is compatible with the SRT intuition that durable selection, when physically instantiated, can require cost-bearing stabilization.

Reason not to rate E3: this draft card does not yet provide a domain-specific operational proxy for SRT selection cost or `Psi_f`. It does not show how to measure `Psi_f` in a given physical, biological, cognitive, AI, or social system.

## 6. Why it matters

SRT treats selection cost and `Psi_f` as the burden involved in constraining open possibilities into a maintained, actionable, or coordinated reality-slice. Landauer-style thermodynamics supplies a careful physical analogue: where information-bearing alternatives are physically erased, reset, or stabilized into durable records, there are thermodynamic constraints on what can be done for free.

The relevance is structural:

- irreversible erasure gives a concrete physical case where eliminating alternatives is not costless;
- reset operations make the link between information state, physical state, and environmental entropy visible;
- durable record formation helps separate a transient fluctuation from a maintained trace;
- reversible computation warns against treating every information transformation as dissipative;
- information thermodynamics shows that measurement, feedback, memory, and erasure require protocol-level bookkeeping rather than broad metaphor.

This makes Landauer-style thermodynamics a candidate physical bridge for selection cost and one projection of `Psi_f`. It does not show that all selection has thermodynamic cost in the Landauer sense.

## 7. Alternative explanations

The same external findings can be explained without SRT:

- ordinary physical energy cost: a system may dissipate heat because of implementation losses, friction, or hardware inefficiency rather than selection cost;
- information-theoretic bookkeeping: erasure cost may concern memory reset protocols, not reality-selection;
- computational architecture: cost may depend on device design, error correction, temperature, clocking, and physical substrate;
- reversible computation: if information is preserved and operations are logically reversible, strong erasure-cost claims may not apply;
- purely formal selection: a mathematical restriction over possibilities may have no immediate physical erasure or record-forming event.

## 8. What would weaken this

This card should be downgraded toward E1 if:

- the relevant "selection" does not involve physical erasure, reset, memory, or durable record formation;
- reversible computation or logically reversible protocols explain the case without the proposed cost burden;
- the observed cost is fully accounted for by ordinary engineering inefficiency rather than information processing constraints;
- the thermodynamic description cannot be connected to SRT-relevant payability, stabilization, or future constraint;
- the interpretation drifts into claiming that all choices, distinctions, or formal selections obey Landauer cost directly.

It should be routed to a pressure ledger if later cards repeatedly fail to separate physical erasure / record cost from loose metaphor.

## 9. Boundary: what this does not prove

This card does not establish any canonical SRT definition.

Specifically:

- Landauer principle does not define SRT selection cost.
- thermodynamic cost does not generalize to all forms of selection.
- reversible computation and purely formal selection are pressure cases.
- this card concerns physical erasure / reset / durable record formation, not every act of choice.
- this card is a structural convergence / bridge-support candidate, not proof of SRT.
- thermodynamic heat dissipation should not be read as a direct measure of `Psi_f`, value, subjecthood, or `d-value`.
- no bridge or evidence card may override the canonical `Psi_f` file.

## 10. Upgrade path

Possible next steps:

1. Create a bridge note separating Landauer erasure, reversible computation, durable records, and SRT selection cost.
2. Define a scoped lab hypothesis only for a physical or computational system with explicit memory reset / record formation.
3. Upgrade toward E3 only if a measurable thermodynamic or information-processing quantity predicts SRT-relevant payability, stabilization burden, or recovery cost better than implementation-specific alternatives.
4. Keep purely formal selection out of scope unless a physical record, reset, or constraint-maintenance process is specified.
5. Add a pressure-ledger entry in a later pass for reversible computation, generic energy cost, and overextension beyond physical information processing.

## Sources Checked

The following sources were checked online for this draft. They are used only to support the external thermodynamics / information-processing background, not to establish SRT.

- [S1] Rolf Landauer, "Irreversibility and Heat Generation in the Computing Process," *IBM Journal of Research and Development* 5(3), 183-191, 1961. Used as the primary source for the erasure / heat-generation principle. DOI: <https://doi.org/10.1147/rd.53.0183>; reliable course reprint checked at <https://www.cs.princeton.edu/courses/archive/fall06/cos576/papers/landauer61.pdf>
- [S2] Charles H. Bennett, "Logical Reversibility of Computation," *IBM Journal of Research and Development* 17(6), 525-532, 1973. Used for the reversible-computation pressure boundary. <https://doi.org/10.1147/rd.176.0525>
- [S3] Charles H. Bennett, "The Thermodynamics of Computation: A Review," *International Journal of Theoretical Physics* 21, 905-940, 1982. Used as a classic review on computation, reversibility, and thermodynamic cost. <https://fab.cba.mit.edu/classes/862.19/notes/computation/Bennett-1982.pdf>
- [S4] Takahiro Sagawa and Masahito Ueda, "Nonequilibrium thermodynamics of feedback control," *Physical Review E* 85, 021104, 2012. Used for information-thermodynamic treatment of feedback, measurement, and thermodynamic bookkeeping. <https://journals.aps.org/pre/abstract/10.1103/PhysRevE.85.021104>
- [S5] Juan M. R. Parrondo, Jordan M. Horowitz, and Takahiro Sagawa, "Thermodynamics of information," *Nature Physics* 11, 131-139, 2015. Used as a modern authoritative review of information thermodynamics. <https://www.nature.com/articles/nphys3230>
- [S6] Takahiro Sagawa, "Second law, entropy production, and reversibility in thermodynamics of information," arXiv:1712.06858, 2017. Used for the boundary among thermodynamic reversibility, logical reversibility, and heat emission in the context of Landauer's principle. <https://arxiv.org/abs/1712.06858>
- [S7] Takahiro Sagawa, "Thermodynamics of Information Processing in Small Systems," *Progress of Theoretical Physics* 127(1), 1-56, 2012. Used as a review of small-system information processing and thermodynamic costs. <https://academic.oup.com/ptp/article/127/1/1/1850101>
- [S8] Takahiro Sagawa, "Thermodynamic and Logical Reversibilities Revisited," *Journal of Statistical Mechanics: Theory and Experiment* P03025, 2014 / arXiv:1311.1886. Used for the claim that logical irreversibility and thermodynamic reversibility require careful separation. <https://arxiv.org/abs/1311.1886>
