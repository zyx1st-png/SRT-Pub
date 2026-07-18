---
id: SRT-NEURO-09-BIOQUANTUM-CISS-AMENDMENT
type: amendment
tags: [Neuroscience, BioQuantum, CISS, Xenon, Decoherence, ClaimBoundary]
status: hypothesis_boundary_v2
layer: L1
epistemic_layer: bridge
claim_mode: hypothesis
canonical: false
claim_level: P3-P5
supersedes: [Neuroscience/SRT_Neuro_09_Integ_Eq.md#iv-亚细胞量子接口候选]
dependency: [SRT-NEURO-09, SRT-NEUROSCIENCE-CLAIM-STATUS, SRT-CORE-000]
updated: 2026-07-16
---

# BioQuantum Boundary Amendment: CISS, Nuclear Spin, and Mechanism-Specific Survival Gates

> **Authority rule**: This amendment supersedes the mechanism boundary and falsification language in `SRT_Neuro_09_Integ_Eq.md` §IV wherever that section treats long-lived quantum coherence as a universal prerequisite for all neural quantum contributions. The original section remains historical bridge material until it is directly integrated through a human-reviewed owner-file revision.
>
> **Claim status**: hypothesis-level physical interface only. This file does not define consciousness, `d-value`, `Ψ_f`, `L_0`, value, subjecthood, or the SRT core ontology.

## 1. Problem corrected

The prior BioQuantum boundary compressed several physically distinct proposals into a single condition:

\[
\tau_{coh}^{micro}>\tau_{min}\Rightarrow \text{detectable quantum contribution}.
\]

That clause is appropriate only for mechanisms whose causal contribution requires phase coherence over a task-relevant interval. It is not a universal gate for quantum-origin biological effects.

In particular, chiral-induced spin selectivity (CISS), nuclear-spin-dependent transport, radical-pair chemistry, and tunnelling can leave measurable classical biochemical consequences without requiring the brain to preserve a large-scale coherent quantum state. A short phase-coherence time can therefore falsify a coherence-dependent mechanism without falsifying every possible quantum-sensitive biological interface.

The previous microtubule-centered wording was also too narrow. Microtubules remain one candidate substrate, not the owner of the entire BioQuantum interface.

## 2. Corrected mechanism-family abstraction

Define a family of candidate quantum-sensitive physical interfaces:

\[
\mathcal{M}_{Q}=\{m_{coh},m_{spin/CISS},m_{radical},m_{tunnel},m_{vib},m_{MT}\}.
\]

The neural-scale candidate contribution is:

\[
\hat G_{\theta,neural}
=
\Lambda_Q\!\left(\{\hat G_{\theta,micro}^{(m)}\}_{m\in\mathcal{M}_Q}\right),
\qquad
\Lambda_Q=\bigoplus_{m\in\mathcal{M}_Q}\Lambda_m.
\]

Each mechanism has its own survival and transduction gate:

\[
S_m(X_m,E_{bio})>\eta_m
\;\land\;
T_m:\Delta X_m\mapsto\Delta B_m\mapsto\Delta N_m
\Rightarrow
\Lambda_m\text{ is empirically admissible}.
\]

Where:

- `S_m` is the mechanism-specific survival functional;
- `X_m` is the relevant microscopic variable, such as phase, spin, tunnelling coordinate, or radical-pair yield;
- `E_bio` is the physiological environment;
- `T_m` is a demonstrated transduction chain from microscopic variation to biochemical and neural variation;
- `η_m` is a mechanism-specific detectability threshold.

No single `τ_coh` threshold is allowed to stand in for all `S_m`.

## 3. Mechanism-specific gates

| Candidate mechanism | Necessary physical gate | Required biological transduction | What would directly weaken it |
|---|---|---|---|
| Phase-coherent / Orch-OR-like | task-relevant `T_2` or phase-coherence time | coherent state changes a molecular or neural observable | `T_2` far below the required interaction window, with no protected or recurrent mechanism |
| Nuclear spin / CISS | spin-dependent interaction in an oriented chiral medium; adequate `T_1`; non-null spin-filter factor | altered permeability, charge reorganisation, ligand access, or receptor occupancy | no spin-dependent transport/binding under physiological conditions; effect persists unchanged in achiral controls |
| Radical pair | verified radical-pair formation, hyperfine coupling, and singlet-triplet yield sensitivity | identified chemical product changes a neural target | no endogenous radical pair at the proposed target or no downstream physiological mapping |
| Quantum tunnelling | measurable tunnelling contribution under physiological temperature and geometry | rate change modifies a relevant enzymatic, channel, or receptor process | classical kinetics fully explain isotope, temperature, and field dependencies |
| Quantum vibration | reproducible mode-specific coherence or vibronic coupling | perturbing the mode changes the biological outcome | spectral perturbation changes the mode but not the biological outcome |
| Microtubule-sensitive interface | substrate-specific quantum or spin-sensitive effect in microtubules | microtubule perturbation changes neural dynamics independently of ordinary structural and transport effects | effects disappear after controlling for cytoskeletal, axonal-transport, synaptic, and toxicity confounds |

## 4. CISS / xenon candidate interface

The 2018 mouse result reported that spin-active xenon isotopes, especially `129Xe` and `131Xe`, were approximately 45% less potent than spin-zero isotopes when co-administered with 0.5% isoflurane. This observation remains load-bearing and requires independent replication.

Wang and Ozturk (2026) proposed a CISS-based kinetic account in which homochiral biological media generate nuclear-spin-dependent permeability or binding differences. Their model reproduces the reported isotope-dependent potency curve, but it is a perspective plus model, not a new animal replication or direct molecular confirmation.

The candidate chain is:

\[
(I_{Xe},\chi_{bio},T_1,\alpha_{CISS})
\xrightarrow{\Lambda_{CISS}}
\Delta P_{perm}
\rightarrow
\Delta [Xe]_{active}
\rightarrow
\Delta \theta_{bind}
\rightarrow
\Delta A_{anesthetic}.
\]

Where:

- `I_Xe` is xenon nuclear spin;
- `χ_bio` is the handedness and orientation of the biological medium;
- `T_1` is longitudinal spin-relaxation time;
- `α_CISS` is the spin-chirality transport or binding asymmetry;
- `P_perm` is permeability into the active compartment;
- `θ_bind` is receptor or functional-site occupancy;
- `A_anesthetic` is the anaesthetic-state effect.

This pathway shifts the key constraint from universal long-range phase coherence (`T_2`) to mechanism-specific spin persistence, orientation, transport, and biochemical amplification. Dissipation is not automatically disqualifying and may be part of the CISS mechanism.

## 5. SRT interpretation boundary

CISS offers a useful physical example of amplification:

\[
\text{microscopic non-neutrality}
\rightarrow
\text{chiral filtering}
\rightarrow
\text{probability bias}
\rightarrow
\text{biochemical inscription}
\rightarrow
\text{macroscopic state difference}.
\]

This structure may serve as a candidate physical implementation or analogy for cross-scale selective amplification. It does **not** establish that CISS is SRT selection in the ontological sense.

The following inference is allowed:

> A quantum-origin variable may influence a consciousness-related state through a mechanism-specific biological transduction chain, without the whole brain functioning as a long-lived coherent quantum computer.

The following inferences are forbidden:

- `nuclear spin affects anaesthetic potency` therefore `consciousness is quantum`;
- `CISS fits the xenon curve` therefore `CISS is experimentally confirmed in anaesthesia`;
- `a quantum-sensitive neural mechanism exists` therefore `subjective experience is explained`;
- `microtubules contain quantum effects` therefore `Orch-OR is established`;
- `spin filtering resembles selection` therefore `L_0`, `d-value`, or `Ψ_f` has been physically derived.

SRT consciousness claims still require their independent conditions and cannot be inherited from a BioQuantum mechanism.

## 6. Falsification and discrimination programme

### FC-BQ-CISS-1: independent isotope-potency replication

Repeat the xenon-isotope anaesthesia experiment with preregistered analysis, adequate power, blinded isotope handling, and both isoflurane-present and xenon-only arms.

- Failure to reproduce the spin-active versus spin-zero potency difference substantially weakens the entire xenon-CISS branch.
- Replication supports an isotope-sensitive mechanism but does not by itself distinguish CISS, radical-pair, receptor, or other quantum-sensitive explanations.

### FC-BQ-CISS-2: chiral versus achiral transport control

Measure isotope fractionation, permeability, or binding across matched chiral and achiral membranes or molecular channels.

- A CISS-specific signal should depend on chirality and molecular orientation.
- An unchanged isotope effect in achiral controls weakens the CISS explanation.

### FC-BQ-CISS-3: target-level binding or inhibition

Use isotopically purified xenon in NMDA-receptor, membrane, or candidate-target assays.

- Demonstrate a spin-dependent difference in access, occupancy, inhibition, or transport under physiological conditions.
- If no target-level difference exists despite a replicated in-vivo potency effect, the proposed transduction chain is incomplete.

### FC-BQ-CISS-4: spin-lifetime and field dependence

Vary conditions that alter `T_1`, spin polarisation, orientation, temperature, or weak magnetic fields while preserving ordinary pharmacological variables.

- The direction and scale of the effect must match a preregistered CISS model.
- Post-hoc parameter fitting without out-of-sample prediction is insufficient.

### FC-BQ-CISS-5: network and consciousness-state separation

Distinguish molecular anaesthetic potency, neural communication breakdown, behavioural unresponsiveness, and subjective report.

- A demonstrated molecular spin effect may explain part of anaesthetic action without identifying the constitutive mechanism of subjective experience.
- No consciousness-level upgrade is permitted unless the model predicts a consciousness-specific measure beyond ordinary receptor and network variables.

## 7. Evidence ladder

| Claim | Current level | Upgrade requirement |
|---|---:|---|
| Xenon isotope potency may depend on nuclear spin | P3, single-study empirical anchor | independent preregistered replication |
| CISS can mathematically reproduce the reported potency pattern | P3 modelling result | parameter robustness and out-of-sample tests |
| CISS mediates xenon transport or binding in neural tissue | P4 hypothesis | direct chiral/achiral transport or receptor evidence |
| A quantum-sensitive mechanism contributes to anaesthetic state transitions | P4 hypothesis | replicated molecular-to-neural causal chain |
| Quantum dynamics constitute consciousness | P5 speculation | not supported by the cited evidence |
| CISS validates SRT ontology | prohibited inference | no direct upgrade path from these data alone |

## 8. Integration rule for the owner file

When `SRT_Neuro_09_Integ_Eq.md` §IV is next revised:

1. rename the boundary from `Microtubule Operator Coupling` to `Mechanism-Family Quantum-Sensitive Coupling`;
2. replace the universal `Ax-BioQuantum-1: Decoherence Constraint Clause` with the mechanism-specific `S_m + T_m` gate;
3. retain microtubules as one substrate-level candidate;
4. add `Λ_spin/CISS` and separate its `T_1`, chirality, transport, and binding tests from `Λ_coh` and its `T_2` tests;
5. keep the section non-canonical and hypothesis-level;
6. retain the anti-overclaim boundary that no quantum mechanism alone yields subjectivity, `d-value`, `Ψ_f`, or value.

## References

- Li N, Lu D, Yang L, Tao H, Xu Y, Wang C, Fu L, Liu H, Chummum Y, Zhang S. **Nuclear spin attenuates the anesthetic potency of xenon isotopes in mice.** *Anesthesiology* (2018).
- Wang A, Ozturk SF. **Xenon Anesthesia and Nuclear Spin Effects in Chiral Systems.** arXiv:2605.19395 (2026). https://arxiv.org/abs/2605.19395
- Smith J, Zadeh-Haghighi H, Salahub D, Simon C. **Radical pairs may play a role in xenon-induced general anesthesia.** arXiv:2009.01661; later published in *Scientific Reports*.
- New Scientist. **Can consciousness be quantum? We may now have an answer.** Archived 2026-07-16. Used as a reporting lead only; evidence status is determined from primary research.
