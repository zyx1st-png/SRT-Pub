---
id: SRT-GENERATIVE-MAINTENANCE-REFERENCE-TRANSITIONS-20261028
type: proposal
status: draft
canonical: false
layer: operations
epistemic_layer: machine_analysis
claim_mode: paper_only_reference_transition_profile
created: 2026-10-28
updated: 2026-10-28
research_mode: U
dependency:
  - Operations/Proposals/SRT_GENERATIVE_MAINTENANCE_FULL_EXPERIMENT_DESIGN_V0_1_2026-10-28.md
tags: [Simulation, TransitionKernel, PaperOnly, Audit]
---

# Reference transition profile v0.1 (paper-only; not frozen)

**Purpose:** resolve low-level ambiguities in the companion full protocol into one candidate executable transition definition, without authorizing code, training or experiments. This reference profile controls over optional examples in its companion until R1 review; R1 may version it to v0.2 rather than silently editing confirmed data.

## A. Initial state and event clock

- Initial state: energy E=6 (cap 8), material B=2 (cap 4), protective module M=2, perception module C=2, conversion module R=2 (all caps 2), construction J=none, consecutive disabled counter H=0.
- The location field in the general proposal is *not persistent in this minimum profile*: each step starts at home; a single `traverse` action models an entire home–resource–home trip as one decision-time step for every arm. The physical abstraction must be stated in any paper. A 2-step travel model would be a separate robustness version.
- At t, exogenous U_t and V_t are independent Bernoulli(0.20); they are scheduled to cause tissue damage at t+2. Initial due queue U_-2,V_-2,U_-1,V_-1 are zero. The cues q_U,q_V about U_t,V_t are generated before the action with per-bit accuracy 0.85 when C>=1 and 0.50 when C=0. There is no access to the true queued future hazard.
- A visible traverse-route requirement alternates U on even t, V on odd t. It is separate from the queued tissue hazards. Both are logged under distinct IDs; the route requirement does not reveal future hazards.
- Exactly 7 available actions: `harvest,repair_M,calibrate_C,service_R,build_U,build_V,traverse`. The general protocol's optional `observe` is **omitted in this reference profile** because no explicit added observation advantage is yet specified. All model families have the same action set.

## B. Deterministic action effects and random effects

1. All actions charge one energy unit; E=0 means the current individual can take no further action. Clamp E to [0,8] and B to [0,4].
2. Harvest: if M,C,R each >=1 then E+=3 and B+=1 (after the base cost); otherwise E+=1 and B does not increase.
3. Repair M: needs B>=1,R>=1,C>=1, consumes one B and increases M by one up to cap2.
4. Calibrate C: needs B>=1,R>=1, consumes one B and increases C by one up to cap2.
5. Service R: needs B>=1,C>=1, consumes one B and increases R by one up to cap2.
6. Build U or V: needs B>=2,R=2,C>=1, consumes two B, replaces J with chosen construction. No free material refund from replacing the old J.
7. Traverse: requires M,C,R>=1 and enough energy. If J matches today's route, success probability is 0.90, else 0.10. Success gives fixed external task reward +1 and B+=1 (clipped); failure reward 0 and no resource. The transition is a round-trip within the current decision step, no additional module damage from travel. J provides a hard-coded manipulation of action effectiveness; it is **not** evidence of novel absolute possibility.

After applying the action, process hazards U_(t-2),V_(t-2) once: U reduces M by one with p=0.75 without U-shield and p=0.15 with it; V analogously reduces C with/without V-filter. The two damage draws are independent keyed events. Clamp to module bounds. Next apply one R-wear random draw, then update H and termination. H increases by one (max 2) only if C=0 and R=0, otherwise resets to 0. Terminate if E=0 or H=2. Reset starts a *new simulated individual episode*; controller parameter survival between episodes must be separately recorded.

## C. Exact closure-vs-open-loop reference contrast

For R wear, the **single structure edge being tested** is M-dependent protection of R:
- Closed: p(R decreases by 1)=w(M_after_hazards), where w(0)=0.50,w(1)=0.15,w(2)=0.05.
- Open: same process but p=0.05 regardless of current M; this is a time-independent protection input matched to the healthy M=2 reference state, with no live M feedback. **It may outperform closed after M damage**. Do not predetermine a positive sign or claim strict match over all M states.
- Sham: same as closed with only a dummy intervention label; no physical/resource changes.
- External yoked-repair: secondary policy-control comparison only; a repair schedule is generated from prior lawful history, receives no future oracle, respects material/energy/action preconditions and logs any mismatches. It is **not** part of the core G0 causal estimate.

The observer may compare under controlled identical pre-state, intervention and keyed exogenous draws, and must also report health-state equivalence tests and the limits of only matching at M=2. Different subsequent states are lawful mediators; do not force them equal when estimating total effects.

## D. Keyed random tape and objective

Pre-generate independent uniform subdraws indexed by (episode_id,t,event_type,subdraw_id) for U/V event occurrence, two cues, U/V damage, R wear, traverse success; every arm must use the same event IDs even when a branch does not need a random draw. This is a counterfactual coupling, not merely resetting the same PRNG seed.

External reward r_t=+1 only for successful traverse, otherwise zero; resource, energy and ability changes occur via true transitions. No dedicated survival, novelty or philosophical goal reward is added. HRL intrinsic drive is a separately declared algorithmic comparison and may not be hidden inside the common reward.

## E. Unresolved *review* decisions, not missing source facts

This profile is one concrete candidate, not validated: R1 must review the potentially severe advantage of open R protection after M falls; decide whether this deliberately negative-control contrast is appropriate, and if necessary produce separately versioned alternatives with matched healthy marginals and independent shock sensitivity. Before G0 execution, check for trivial all-alive/all-dead regimes, material conservation and sensitivity to H. No numerical result, successful calibration, code, or CI run is claimed. Current CURRENT NEXT, FR-ADV, and toy-execution HOLD remain in force.
