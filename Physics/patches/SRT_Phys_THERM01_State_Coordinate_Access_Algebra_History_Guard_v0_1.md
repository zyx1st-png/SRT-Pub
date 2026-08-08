---
id: SRT-PHYS-THERM01-STATE-COORDINATE-ACCESS-ALGEBRA-HISTORY-GUARD
type: hardening_patch
tags: [Physics, Quantum Many Body, Floquet, ETH, Feynman Kitaev, History State, Entanglement, Access Algebra, State Coordinates, Bridge]
status: active
version: v0_1
layer: L1
epistemic_layer: bridge
claim_mode: bridge
claim_level: P3
canonical_status: non_canonical
canonical: false
date: 2026-08-08
source_ids:
  - SRC-2026-08-08-PHYSICS-IPPOLITI-LONG-INFINITE-TEMPERATURE-ZERO-ENERGY
dependency:
  - Physics/README.md
  - Physics/SRT_Physics_Claim_Status.md
  - Physics/_SRT_Phys_Bridge.md
  - Physics/_SRT_Physics_Hardening_Index.md
  - Physics/patches/SRT_Phys_P08_Closure_Dynamics_and_Physical_Law_v0_1.md
  - Core/SRT_Core_21_Minimal_Axioms.md
  - _SRT_SYMBOL_TABLE.md
  - Governance/SRT_CLAIM_LADDER.md
machine_summary: >
  Non-canonical P3 physics hardening patch based on Ippoliti and Long's 2026 PRX
  construction of geometrically local Hamiltonians with infinite-temperature-like
  eigenstate properties at zero energy. Adds five guards: state-coordinate
  insufficiency, observable/access-algebra qualification, history-representation
  versus irreversible L2 sedimentation, diagnostic-criterion versus generating-
  mechanism separation, and local-rule versus global-state-complexity separation.
  The source does not prove SRT, observer-created reality, or any identity between
  entanglement/ETH and canonical SRT variables.
---

# SRT Physics THERM01: State Coordinate, Access Algebra, and History-Encoding Guard

> **Status**: non-canonical P3 physics hardening bridge.  
> **Source anchor**: Matteo Ippoliti and David M. Long, *Infinite Temperature at Zero Energy*, *Physical Review X* 16, 031030 (2026), DOI `10.1103/tvny-gtzp`.  
> **Boundary**: this patch does not establish SRT physics, identify entanglement with `d`, identify thermalization with `Psi_f`, derive `L_2`, or imply that physical facts are created by observation.

## 0. Adjudication

Pipeline 1 verdict:

```text
A -- bounded non-canonical P3 physics hardening bridge
```

The source is unusually useful because it creates a controlled edge case in which properties normally bundled together can be separated without ambiguity:

```text
low spectral position
!= low entanglement

ETH-like local structure
!= unique dynamical mechanism

history encoding
!= irreversible historical sedimentation

restricted observable readout
!= complete global-state description
```

The SRT gain is therefore primarily a **distinction hardener** and **negative-control case**, not a new ontology claim.

## 1. Narrow external result

Ippoliti and Long modify the Feynman-Kitaev circuit-to-Hamiltonian construction by imposing periodic boundary conditions on the clock register. A full clock cycle then imposes a Floquet eigenstate condition. This permits periodically driven eigenstate structure to be embedded into eigenstates of a static, geometrically local Hamiltonian.

When the input Floquet circuit obeys infinite-temperature ETH, the static Hamiltonian inherits local infinite-temperature-like eigenstate properties and volume-law entanglement throughout its spectrum, including the ground state. The authors then provide an exactly solvable LFSR-based Floquet family with provable ETH behavior, converting the main existence statement from a merely conditional construction into an explicit family.

The resulting model therefore allows:

```text
static Hamiltonian ground-state energy
+
Floquet-derived thermal-looking local eigenstate structure
```

without making `zero temperature` and `infinite temperature` one undifferentiated thermodynamic variable.

## 2. Why this matters for SRT

SRT repeatedly moves across levels where a descriptive coordinate, a local proxy, a historical record, and the underlying selection structure can easily be conflated. THERM01 supplies a concrete physics case showing why these collapses are unsafe.

The source is especially valuable for three current repository boundaries:

1. canonical `L_2` requires irreversible trace rather than mere history representation;
2. Physics is a bridge / pressure-test domain and must not identify familiar physical observables with canonical primitives;
3. a domain-level diagnostic can constrain a model without uniquely specifying its generating mechanism or ontology.

## 3. THERM01-C1 -- State-coordinate insufficiency

### Claim

A single state coordinate can be physically meaningful without being a sufficient statistic for the state's full relational organization.

Bridge schema:

```text
x = state descriptor
R(s) = relational structure of state s

x(s1) < x(s2)
  does not entail
R(s1) is structurally simpler than R(s2)
```

For the source case, energy position and entanglement/ETH structure can be separated by construction.

### SRT consequence

Future SRT physics writing should avoid inferences of the form:

```text
one scalar physical coordinate
-> complete state type
-> ontological rank
```

unless an explicit theorem or domain model supplies the missing implication.

This applies not only to energy but to candidate projections involving entropy, Fisher information, curvature, complexity, bandwidth, or entanglement.

### Boundary

```text
energy is not sufficient
!= energy is unreal or unimportant
```

## 4. THERM01-C2 -- Access-algebra qualification

### Claim

An effective description should name the subsystem / observable algebra on which it is valid.

Let `s` be one global state and let `A` denote an accessible operator algebra. Define only schematically:

```text
D_A(s) := effective description recoverable through A
```

Then it is possible that:

```text
D_A1(s) != D_A2(s)
```

without contradiction when `A1` and `A2` interrogate different relational structure.

In the periodic-clock construction, spin-local observables can exhibit the inherited infinite-temperature-like behavior while clock-sensitive relations retain information tied to the static Hamiltonian's spectral organization.

### SRT consequence

Replace vague observer-relative language with an explicit access statement whenever possible:

```text
state s
+ declared access algebra A
-> operationally available description D_A(s)
```

This is more precise than saying merely that a property "depends on perspective."

### Boundary

Do not infer:

```text
access qualification
-> observer creates the state
-> arbitrary subjectivism
```

The global state and Hamiltonian remain objective elements of the source construction.

## 5. THERM01-C3 -- History representation is not L2 sedimentation

### Source-side structure

The Feynman-Kitaev history-state construction can encode a dynamical sequence into correlations of a static state:

```text
trajectory / circuit history
-> static relational history encoding
```

Local transition constraints can enforce global consistency of the encoded path.

### SRT pressure

Canonical SRT requires more than this. `Core/SRT_Core_21_Minimal_Axioms.md` P0-03 states that once selection is anchored and leaves history in `L_2`, it cannot be treated as never having occurred; reversal is itself a new selection event.

Therefore the safe distinction is:

```text
H_rep = history represented in present structure
H_dep = current dynamics depends on prior path
H_sed = prior selection irreversibly changes later accessibility / constraint structure

H_rep != H_dep != H_sed
```

A coherent unitary history state can realize `H_rep` without by itself satisfying `H_sed`.

### SRT consequence

Admission of an external physical mechanism as an `L_2` realization should require at minimum:

1. a retained trace;
2. future-state or future-transition consequences;
3. a specified irreversibility / non-erasability condition at the claimed level;
4. a reason reversal is a new event rather than exact cancellation of the old event.

The periodic FK construction is therefore useful as a **negative control** for the L2 gate.

## 6. THERM01-C4 -- Diagnostic criterion is not generating mechanism

The source's exactly solvable Floquet family is valuable methodologically because it separates an eigenstate diagnostic from assumptions normally bundled with it.

SRT hardening rule:

```text
criterion C is satisfied
!= mechanism M uniquely generated C
!= neighboring criteria C2, C3 are automatically satisfied
```

Applied generally:

```text
ETH
!= equilibration by definition
!= random-matrix spectral statistics by definition
!= generic quantum chaos by definition
!= one unique microscopic mechanism
```

SRT should use the same discipline for its own proxies:

```text
behavioral success
!= real choice

high decodability
!= anchoring

large Fisher proxy
!= canonical Psi_f

large capacity proxy
!= canonical d

history representation
!= L2 sedimentation
```

This does not deny empirical correlations among these quantities. It blocks identity claims that outrun the evidence.

## 7. THERM01-C5 -- Local-rule simplicity does not bound global-state simplicity

The source Hamiltonians are geometrically local, yet support globally extensive entanglement.

Bridge rule:

```text
simple / local constraint grammar
!= simple admissible global relational structure
```

This supplies a useful constraint on SRT's law-as-grammar language in `SRT_Phys_P08_Closure_Dynamics_and_Physical_Law_v0_1.md`:

> Even if law is treated at bridge level as an invariant grammar of admissible closure, the apparent locality or compactness of that grammar does not license an inference that globally admitted states must be low-complexity, weakly entangled, or easily compressible.

No direct edit to P08 is made in this material pass.

## 8. Mapping table

| External structure | Safe SRT bridge use | Forbidden identity |
|---|---|---|
| spectral energy | one physically meaningful state coordinate | energy = complete ontological state |
| volume-law entanglement | example of relational complexity not fixed by low spectral position | entanglement entropy = `d` / `Psi_f` / `L_2` |
| periodic FK clock | explicit history-to-static-constraint encoding | FK history state = canonical `L_2` |
| phase twist selecting zero-energy state | example that spectral embedding depends on constructed Hamiltonian/boundary condition | boundary choice makes energy unreal |
| spin-local ETH behavior | access-qualified effective thermal description | local infinite-temperature behavior = whole global state at `T=infinity` |
| clock-sensitive observables | retained relational information outside spin-only readout | clock = observer / subject |
| LFSR Floquet family | diagnostic-mechanism separation / exact edge case | classical pseudorandom generator = SRT selector |
| geometrical locality | simple/local generator with complex global states | locality = global simplicity |

## 9. Formal audit interface

For a proposed SRT physics bridge claim `Q`, record five fields:

```text
Q = (
  descriptor,
  access_set,
  generator,
  history_gate,
  diagnostic
)
```

where:

- `descriptor`: which physical coordinate/statistic is being used;
- `access_set`: which subsystem or observable algebra supports the statement;
- `generator`: which dynamics/Hamiltonian/circuit produces the state;
- `history_gate`: whether the claim concerns representation, dependence, or irreversible sedimentation;
- `diagnostic`: which empirical/theoretical criterion is actually satisfied.

Audit questions:

1. Is the descriptor being promoted into a complete state characterization?
2. Is an access-limited statement being presented as globally exhaustive?
3. Is a history representation being promoted into irreversible `L_2`?
4. Is one diagnostic being used to infer a unique mechanism?
5. Is local generator simplicity being used to infer global-state simplicity?

If yes, demote or qualify the bridge.

## 10. New bounded claim cluster

### THERM01-C1 -- State-coordinate insufficiency

A physically meaningful scalar descriptor need not determine full relational organization.

### THERM01-C2 -- Access-algebra qualification

Effective state descriptions must be indexed to the observables/subsystems through which they are valid when different access sets reveal non-equivalent summaries.

### THERM01-C3 -- History sedimentation gate

Static encoding of a trajectory is insufficient for `L_2`; irreversible future-constraining trace remains an additional admission condition.

### THERM01-C4 -- Criterion-mechanism separation

A satisfied diagnostic does not uniquely identify the mechanism that generated it or guarantee neighboring diagnostics.

### THERM01-C5 -- Local/global complexity separation

Local or simple rule structure does not imply simple global admissible states.

All five claims are P3 hardening statements. None is a P0/P1 SRT theorem or an established implication beyond the source's bounded construction.

## 11. Operational consequences for SRT work

### 11.1 Physics bridge audit

When a future physics patch uses energy, entropy, entanglement, Fisher geometry, complexity, thermalization, or local observables, add an explicit statement answering:

```text
What exactly is the descriptor?
Which observable set supports it?
What mechanism generated it?
What does it fail to determine?
```

### 11.2 L2 admission audit

For any proposed physical `L_2` realization, distinguish:

```text
stored representation
path dependence
irreversible future-access rewriting
```

Only the third is eligible for the strongest SRT sedimentation language, and even then only under the relevant domain assumptions.

### 11.3 Mechanism-negative-control design

Where an SRT proxy is proposed, actively seek systems that satisfy the proxy under a different mechanism. Such edge cases are more informative than additional positive correlations because they test whether the proxy has been mistaken for the construct.

## 12. Reverse pressure / failure conditions

THERM01 has little SRT value if it is reduced to the generic slogan that "one number cannot describe everything." Its value survives only if future SRT work actually uses the five-field audit to prevent concrete conflations.

The bridge should be weakened if:

1. the claimed access-algebra distinction cannot be stated without importing observer subjectivity absent from the physics;
2. future SRT work cannot specify an empirical/structural difference between history representation and irreversible sedimentation;
3. the criterion-mechanism distinction is used only rhetorically and does not change proxy admission decisions;
4. local/global complexity language is stretched into claims about consciousness, agency, or metaphysical depth unsupported by the source.

## 13. Boundary cautions

Do not claim:

- the paper proves SRT;
- zero energy literally equals infinite thermodynamic temperature;
- energy is nonphysical or merely perspectival;
- the same global state has contradictory absolute temperatures;
- volume-law entanglement is `d-value`, `Psi_f`, `L_2`, consciousness, agency, or selection;
- the Feynman-Kitaev clock proves that time is spatial or unreal;
- static history encoding proves irreversible causal memory;
- access-algebra dependence implies observer-created reality;
- ETH is meaningless because it can occur in an unusual solvable circuit;
- locality is ontologically superficial or incapable of constraining global structure.

Preserve:

```text
spectral coordinate
!= complete relational state

access-qualified description
!= subjective creation

history representation
!= irreversible sedimentation

diagnostic match
!= mechanism identity

local rule
!= globally simple state
```

## 14. Integration hook

Future synthesis should compress THERM01 into three additions rather than importing the paper narrative:

1. a state-descriptor / access-algebra guard in the quantum bridge;
2. a history-representation versus `L_2` sedimentation negative-control paragraph;
3. a criterion-mechanism audit rule for physics proxies.

Hook:

```text
Physics/hooks/THERM01_State_Coordinate_Access_Algebra_History_Integration_Hook.md
```

SourceCard:

```text
Materials/2026/SRC_2026_08_08_Physics_Ippoliti_Long_Infinite_Temperature_Zero_Energy.md
```

## 15. One-paragraph abstract

Ippoliti and Long's periodic Feynman-Kitaev construction shows that a static, geometrically local Hamiltonian can host ground states whose selected local and entanglement properties resemble infinite-temperature Floquet eigenstates. SRT should use this not as evidence for its ontology but as a hardening counterexample to several conflations: low spectral position need not imply simple relational structure; an effective thermal description must be indexed to the observable algebra supporting it; coherent history encoding is weaker than irreversible `L_2` sedimentation; a diagnostic such as ETH does not uniquely determine its generating mechanism; and local rule simplicity does not bound global-state complexity. THERM01 therefore adds a five-field audit—descriptor, access set, generator, history gate, diagnostic—for future SRT physics bridges.
