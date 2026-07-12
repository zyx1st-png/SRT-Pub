---
id: SRT-EXP-SELECTIVE-RESYNCHRONIZATION-MATCHED-PATHS-README
type: experiment_readme
status: feasibility_closed
layer: lab
epistemic_layer: p4
claim_mode: experiment
canonical: false
---

# Matched-Endpoint, Multi-Future Diagnostic

This experiment tests whether different B-stage adaptation paths retain an
effect on several future tasks after B validation accuracy, NLL, and ECE are
matched within a shared seed/A-checkpoint group.

It does not revise the v1 NO-GO and does not define `SR_preC v2`.

## Environment

The implementation can reuse the pinned v1 virtual environment:

```bash
uv run --python ../selective_resynchronization_mvp/.venv/bin/python -m pytest tests -q
```

Device selection supports CPU, Apple Silicon MPS, and CUDA.

## Locked order

```bash
uv run --python ../selective_resynchronization_mvp/.venv/bin/python scripts/diagnose_v1.py
uv run --python ../selective_resynchronization_mvp/.venv/bin/python -m pytest tests -q
uv run --python ../selective_resynchronization_mvp/.venv/bin/python scripts/run_matching_feasibility.py
uv run --python ../selective_resynchronization_mvp/.venv/bin/python scripts/freeze_matched_checkpoints.py --stage feasibility
```

The feasibility gate produced 0/5 complete four-path groups. Consequently the
locked ten-seed run and multi-future runner/analysis were not executed. See
`papers/selective_resynchronization/12_matching_feasibility_report.md` and
`15_path_effect_decision.md`.

The feasibility command cannot import or construct future-task loaders. The
matched checkpoint table would have to be frozen and hash-verified before any
multi-future runner could be authorized; that authorization was not granted.
