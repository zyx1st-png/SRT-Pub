---
id: SRT-GRG-R1-SOURCE-FIDELITY-PASS2-BOWLER-SYNERGETICS-20260921
type: audit
status: active
record_stage: source_fidelity_pass2
date: 2026-09-21
layer: operations
epistemic_layer: os
claim_mode: audit
canonical: false
ai_do_not_use_for_definition: true
research_mode: U
comparative_claim: none
named_comparator: none
n_mode_triggered: false
dependency:
  - Operations/Audits/SRT_GRG_R1_CROSS_REALIZATION_SOURCE_FIDELITY_PASS1_2026-09-21.md
  - Materials/2026/SRC_2026_09_08_Neuro_Bowler_Structured_Experience_Strategy_Dynamics.md
  - Materials/2026/SRC_2026_09_21_Synergetics_OrderParameter_Slaving_CircularCausality.md
tags: [GRG, GRGR1, SourceFidelity, Bowler, Synergetics, MaintainedScaffold, CausalReentry]
---

# GRG-R1 source-fidelity Pass 2 — Bowler + synergetics

## 0. Question

After splitting GRG-R1 into R1a retained imprint, R1b maintained scaffold, R1c causal re-entry and R1d prospective transfer, what exactly pays R1b/R1c in the strongest current source-native examples?

## 1. Bowler: what is actually manipulated?

The public seed_weights_run.py establishes the intervention sequence more precisely than the shorthand eigenvalue intervention.

### 1.1 Scaffold extraction

~~~text
loads shaping-trained recurrent networks
-> eigendecomposes recurrent weight matrices
-> sorts eigenvalues
-> takes the leading four
-> averages them across shaping networks
~~~

Those four mean values are the intervention scaffold.

### 1.2 Recipient manipulation

For an otherwise unshaped recipient network:

~~~text
eigendecompose current recurrent matrix
-> replace four eigenvalues with shaping-associated scaffold
-> reconstruct recurrent matrix
-> train 100 epochs
-> re-impose scaffold
-> train 100 epochs
-> re-impose scaffold
-> train 100 epochs
-> re-impose scaffold
-> train 700 further epochs without another forced reset
~~~

Therefore the manipulated object is not well described as a static history marker inserted once.

The stronger source-faithful description is:

~~~text
a spectral regime externally maintained across an early learning interval
and then released to later learning dynamics
~~~

### 1.3 What downstream effects are directly shown?

The source figure workflow shows training-history curves for seed-run versus no-shaping networks, final task behavior of altered networks, and PCA state-space structure of seed-run networks.

The broader Bowler study also identifies shaping-associated low-dimensional trajectories, recurrent connectivity differences and fixed/slow-point / switching dynamical motifs.

However:

~~~text
eigenvalue intervention causally affects later learning
~~~

does not by itself prove:

~~~text
a specific fixed point / limit cycle is the unique mediator of that effect
~~~

The fixed-point / attractor analyses characterize shaped-network dynamics, but the seed intervention does not independently ablate each downstream dynamical motif.

## 2. Bowler R1 typing

### R1a

Paid. Shaping history leaves recurrent-operator signatures.

### R1b

Paid under an important qualifier:

~~~text
maintenance mode = EXOGENOUS EXPERIMENTAL CLAMP during early training
~~~

The scaffold is repeatedly restored by the experiment. This demonstrates a maintained operator regime, not endogenous self-maintenance.

### R1c

Paid as causal capacity:

~~~text
intervened maintained spectral regime
-> altered later learning trajectory / learned organization
~~~

This is stronger than the toy one-time transplant, but the exact internal mediator downstream of the maintained spectral intervention remains underdetermined.

### R1d

Not automatically paid. Bowler's novel probes demonstrate generalization / strategy readout, but the GRG programme should not infer R1d merely from R1b/R1c.

## 3. Synergetics: what makes an order parameter causal?

The synergetics source bundle supplies a different causal architecture:

~~~text
interacting components
-> emergent order parameter
-> order parameter constrains component dynamics
-> components continue to sustain the order parameter
~~~

The slaving principle is therefore not a statement that a macro-description predicts micro-behavior.

It is a dynamical claim that the collective variable participates in the effective evolution of the component variables.

## 4. Synergetics R1 typing

### R1a

Insufficient. A macro signature alone is not enough.

### R1b

Paid in the source architecture:

~~~text
maintenance mode = ENDOGENOUS / SELF-CONSISTENT
~~~

The order parameter is part of the ongoing collective dynamics.

### R1c

Paid in the source architecture:

~~~text
order parameter -> constrained component dynamics
~~~

while components -> order parameter closes the circular causal relation.

### R1d

Not paid by the general slaving principle alone. A stable order parameter in one regime does not establish transfer into an unseen context.

## 5. New distinction forced by source fidelity

R1b needs a maintenance-provenance declaration.

At minimum:

~~~text
maintenance mode:
A. endogenous self-consistent
B. exogenous experimental clamp
C. environmental / institutional external maintenance
D. mixed / coupled
~~~

Why this matters:

~~~text
externally clamped causal capacity
!= endogenous self-maintaining organization
~~~

An experiment may validly prove that O can causally constrain later dynamics while still not proving that the system naturally maintains O on its own.

## 6. R1c also needs two directions declared

For higher-order organization:

~~~text
formation direction: components / prior operation -> O
re-entry direction: O -> later component / process constraints
~~~

Where both are live:

~~~text
circular causality
~~~

Where only O is externally imposed:

~~~text
causal intervention capacity
~~~

but not full endogenous circularity.

This distinction prevents a laboratory clamp from being mistaken for self-organization.

## 7. Revised source-fidelity declaration for any GRG-R1 mapping

A future source or experiment should record:

1. formation source — how O arose;
2. retention evidence — how O remains identifiable;
3. maintenance mode — endogenous, exogenous, environmental/institutional, mixed;
4. operator status — how O participates in transition dynamics;
5. intervention target — what exactly is changed;
6. downstream consequence — what transition / accessibility / coordination changes;
7. component-to-O evidence;
8. O-to-component evidence;
9. grain / timescale;
10. withdrawal / failure condition;
11. R1 burden claimed — R1a, R1b, R1c, R1d.

## 8. Cross-source invariant after Pass 2

The strongest surviving cross-source relation is not history leaves a trace and not a low-dimensional variable exists.

It is closer to:

~~~text
prior / component-level process
-> forms an organization O
-> O is maintained during the relevant later process
-> O participates in that process's transition structure
-> perturbing / removing O changes later organization
~~~

This is the current R1b -> R1c core. Prospective transfer remains a separate R1d burden.

## 9. Does this rescue the toy spectral family?

No.

The toy O3 protocol tested a one-time transplant and returned NULL. Bowler's repeated-reset intervention is a different causal contract.

Source fidelity explains why the toy intervention was a weaker realization; it does not convert the null into support.

Any repeated-reset toy study would be a new experiment with a new preregistration and would need an independent reason beyond the last test was null.

## 10. Does GRG-R1 now have scientific distinctiveness?

Not established.

Bowler and synergetics already contain strong source-native R1b/R1c structures.

The current GRG contribution is explicit burden separation, transfer discipline, maintenance-provenance typing, refusal to infer causal re-entry from retained markers, and cross-domain routing.

Whether that becomes a scientific content increment remains open.

## 11. Next gate

Do not run a new toy experiment yet.

Next = candidate-selection audit for one genuinely different domain realization of R1c.

Requirements:

~~~text
not another RNN spectral variant
source-native R1b/R1c already present
independent perturbation / intervention possible
maintenance provenance explicit
no O4 / transfer target yet
the GRG decomposition must change a control / distinction before result inspection
~~~

Possible candidate families may include coordination dynamics / phase-transition systems, but no candidate is selected by this file.

## 12. Programme disposition

~~~text
Bowler:
R1a = PASS
R1b = PASS under exogenous early-training clamp
R1c = PASS as causal capacity
R1d = not established by this routing

Synergetics:
R1a = insufficient alone
R1b = strong endogenous exemplar
R1c = strong circular-causality exemplar
R1d = not established

GRG-R1 causal core = RETAIN / NARROW
maintenance provenance declaration = ADD TO PROGRAMME METHOD
new experiment = HOLD
O4 = BLOCKED
canonical edit = NO
Level change = NO
scientific distinctiveness = NOT ESTABLISHED
~~~
