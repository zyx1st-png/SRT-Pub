---
id: SRT-EXP-CHOICEMAP-EXPLICIT-SCAFFOLDING-README
type: experiment_readme
status: active_locked
layer: lab
epistemic_layer: p4
claim_mode: experiment
canonical: false
---

# Explicit ChoiceMap Scaffolding Experiment

This directory is a self-contained, falsifiable P4/lab experiment. It tests an explicit
decision scaffold in a small synthetic world; it does not test SRT ontology and does not
modify earlier negative experimental conclusions.

## Reproduce

From this directory, with the dependencies in `requirements.txt` installed:

```bash
python -m unittest discover -s tests -p 'test_*.py'
python scripts/run_smoke.py
python scripts/run_pilot.py
python scripts/lock_protocol.py
python scripts/run_confirmatory.py
python scripts/analyze_confirmatory.py
```

Stages are gated. Smoke is diagnostic only; pilot is calibration only; confirmatory
results are valid only when `manifests/protocol_hashes.json` still matches the locked
configuration.

The existing human-facing ChoiceMap prototype delegates convergence to the human. This
experiment is a different construct: an autonomous, explicit engineering scaffold with
candidate records, probes, reversibility metadata, and a commitment gate. Neither one
silently redefines the other.
