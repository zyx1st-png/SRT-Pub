---
id: HOOK-PHYS-THERM01-STATE-COORDINATE-ACCESS-ALGEBRA-HISTORY
patch_id: SRT-PHYS-THERM01-STATE-COORDINATE-ACCESS-ALGEBRA-HISTORY-GUARD
type: integration_hook
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
domain: physics_quantum_manybody_floquet_eth_entanglement_computation
status: active
integration_status: pending
landing_ledger:
  - target: "Physics/_SRT_Phys_Bridge.md"
    state: pending
    blocked_by: "Physics is a dormant/frozen bridge layer. Future synthesis should add THERM01 only as a state-descriptor/access-algebra and L2-negative-control guard, without promoting ETH, entanglement, or energy to canonical SRT variables."
  - target: "Physics/patches/SRT_Phys_P08_Closure_Dynamics_and_Physical_Law_v0_1.md"
    state: pending
    blocked_by: "P08 is already a non-canonical hardening patch. If touched later, add only the local-rule/global-state-complexity qualification and keep law-as-grammar language explicitly bridge-level."
---

# THERM01 Integration Hook: State Coordinate, Access Algebra, and History Encoding

## 1. Target documents

```text
Physics/_SRT_Phys_Bridge.md
Physics/patches/SRT_Phys_P08_Closure_Dynamics_and_Physical_Law_v0_1.md
```

## 2. Landing positions

### Main physics bridge

Place near the section that discusses effective physical descriptions, entanglement, thermodynamic/information-theoretic proxies, or the relation between local observables and global physical structure.

The future synthesis should add a compact audit rule:

```text
descriptor
+ access set
+ generator
+ history gate
+ diagnostic
```

and require each strong bridge claim to state which of these fields it is actually about.

### P08 closure-dynamics patch

Place near the law/locality discussion only as a qualification:

```text
local / compact admissibility grammar
!= globally simple admissible state
```

Do not use the PRX paper as evidence that SRT has derived physical law, nonlocal ontology, or a special role for entanglement.

## 3. Suggested native paragraph -- state descriptor and access algebra

> A physical state can admit several jointly correct effective descriptions without those descriptions being interchangeable. A spectral coordinate such as energy may locate a state within one Hamiltonian while leaving much of its internal relational structure undetermined; conversely, a restricted observable algebra may support a thermal-looking local description while other correlations retain information not available through that algebra. Physics-facing SRT claims should therefore name both the descriptor and the access set that support an inference, rather than promoting one successful coordinate or subsystem summary into a complete state characterization.

## 4. Suggested native paragraph -- history representation versus sedimentation

> Encoding a trajectory into a static relational structure is weaker than historical sedimentation. A history-state construction can preserve the consistency of an entire sequence without establishing that any step irreversibly changed later accessibility. For SRT purposes, `L_2` admission requires a stronger gate: the prior event must leave a trace that continues to constrain later selectable or accessible states, and an apparent reversal must itself be a new event rather than exact erasure of the old one.

## 5. Suggested native paragraph -- criterion versus mechanism

> A diagnostic should not be treated as a mechanism label. If two architectures satisfy the same high-level criterion through different dynamics, the criterion constrains the resulting state or behavior but does not uniquely identify the generator. The same discipline should apply to SRT proxies: decodability, Fisher geometry, energetic cost, behavioral success, entanglement, or thermal-looking statistics can support bounded bridge claims without becoming identities with anchoring, `Psi_f`, `d`, `L_2`, or real choice.

## 6. Suggested comparison table

| Question | PRX construction | SRT-safe use | Do not infer |
|---|---|---|---|
| Where is the state in the spectrum? | can be placed at zero energy / ground state | spectral coordinate is one descriptor | low energy = simple ontology |
| What do local spin observables see? | infinite-temperature-like ETH structure | access-algebra-qualified effective description | observer creates temperature |
| What retains spectral/history information? | clock-sensitive relational structure | not all state information is in one restricted algebra | clock = subject / selector |
| How is history represented? | periodic FK history encoding | negative control for history representation | history state = `L_2` |
| What does ETH identify? | eigenstate matrix-element structure | diagnostic-mechanism separation | ETH = chaos/equilibration by definition |
| How local is the generator? | geometrically local | local rule can support complex global states | locality is irrelevant |

## 7. Do not include

- `energy` as an SRT primitive;
- entanglement entropy as canonical `d` or `Psi_f`;
- ETH as a definition of thermalization, chaos, consciousness, agency, or selection;
- the claim that one global state literally has contradictory absolute temperatures;
- `observable algebra` as a synonym for observer perspective, subjecthood, or consciousness;
- Feynman-Kitaev history states as a direct realization of canonical `L_2`;
- the claim that static encoding proves irreversible causal memory;
- the claim that local laws cannot constrain global states;
- the claim that the paper proves SRT or a selection-first ontology.

## 8. Future synthesis target

Compress THERM01 into three bounded guards when the physics synthesis reopens:

1. state descriptor / access-algebra qualification;
2. history representation / dependence / sedimentation separation;
3. diagnostic / mechanism separation with explicit negative-control testing.

Source patch:

```text
Physics/patches/SRT_Phys_THERM01_State_Coordinate_Access_Algebra_History_Guard_v0_1.md
```
