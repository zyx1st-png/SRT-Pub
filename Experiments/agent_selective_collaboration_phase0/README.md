---
id: SRT-AGENT-COLLAB-PHASE0-README-20261010
type: experiment_readme
tags: [ChoiceMap, GRG, Beacon, Agent, Phase0]
status: draft
canonical: false
layer: operations
epistemic_layer: os
claim_mode: engineering_hypothesis
date: 2026-10-10
---

# Agent selective collaboration — Phase 0 sandbox

This directory starts a *downstream, noncanonical* engineering package. It does not alter existing ChoiceMap experiments or STATUS.md CURRENT NEXT. The GRG-inspired **condition–prediction–failure record** is a neutral engineering mechanism only: results cannot count toward GRG §8.1 / M4 / M5, cannot unlock the paused fusion lane, and cannot establish ontological or scientific distinctiveness. `Beacon` is WORKING_LABEL_ONLY, not a canonical term.

Read PROTOCOL_DRAFT.md before treating a code test as evidence. Only a smoke-level contract implementation belongs in Phase 0: frame changes preserve rejected/stale proposal provenance, hypothesis assessment requires a prospective record and later tool observation, and retrieved Beacon events are distinguished from *new* situated re-entry events. Approval and actor checks here are string-labelled **test fixtures**, not authenticated security or a production tool-side policy. Events are returned as detached snapshots, but this in-memory demo is neither tamper-proof storage nor a production event log.

To run the intended standard-library smoke tests after the Python files are present:

~~~bash
python -m unittest discover -s Experiments/agent_selective_collaboration_phase0 -p 'test_*.py' -v
~~~

Phase-0 contract fixtures now include `simulated_user_contract.py` and its regression tests: hidden-truth/oracle perturbation invariance at fixed public view, canonical same-key reply equality across B1+/C+/D+ labels and interface formats, and user-turn/question/approval budget fail-closed checks. These fixture-level tests must be rerun against an **actual environment adapter** before an effectiveness study; no simulator, Agent policies or effect outcomes have been implemented here. `Hypothesis.measurement_key` is specified on proposal; linked observations (including a tool action's own result) must match this preregistered key and distinguish self-generated intervention evidence from independent evidence. Tool actors remain spoofable strings only. Revocation of an unissued action is rejected instead of logged as a completed revocation.

`PROTOCOL_DRAFT.md` is the single controlling source for the **nine named arms**, F1–F6, proposed sample plan and H1/H2/H3 comparisons; the parent design proposal is explanatory. This protocol is **not frozen or registered**. The current plan does not assume the repository has a usable benchmark dataset. No simulation of successful agent task performance or human usability result has yet been executed in this branch. Model policies, environment generators, strongest baselines, preregistration lock and result cards are subsequent independently reviewed work. In particular the test suite does not prove actual task effectiveness, authorized execution in a live system, or true independent model evaluations.

Relevant lineage:
- Operations/Proposals/SRT_CHOICEMAP_GRG_AGENT_COLLABORATION_DESIGN_V0_1_2026-10-10.md
- papers/choicemap_explicit_scaffolding/06_final_decision.md
- Operations/Proposals/SRT_GRG_FOUNDATIONAL_PROTO_GRAMMAR_V0_3_2026-09-21.md
