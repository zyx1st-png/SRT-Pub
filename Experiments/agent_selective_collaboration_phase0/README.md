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

This directory starts a *downstream, noncanonical* engineering package. It does not alter existing ChoiceMap experiments or STATUS.md CURRENT NEXT.

Read PROTOCOL_DRAFT.md before treating a code test as evidence. Only a smoke-level contract implementation belongs in Phase 0: it checks whether frame changes preserve provenance, GTS hypotheses remain unverified until an observation, user decisions are not forged by model proposals, and authorization is checked outside the model.

To run the intended standard-library smoke tests after the Python files are present:

~~~bash
python -m unittest discover -s Experiments/agent_selective_collaboration_phase0 -p 'test_*.py' -v
~~~

The current plan does not assume the repository has a usable benchmark dataset. No simulation of successful agent task performance or human usability result has yet been executed in this branch. Model policies, environment generators, strongest baselines, preregistration lock and result cards are subsequent independently reviewed work.

Relevant lineage:
- Operations/Proposals/SRT_CHOICEMAP_GRG_AGENT_COLLABORATION_DESIGN_V0_1_2026-10-10.md
- papers/choicemap_explicit_scaffolding/06_final_decision.md
- Operations/Proposals/SRT_GRG_FOUNDATIONAL_PROTO_GRAMMAR_V0_3_2026-09-21.md
