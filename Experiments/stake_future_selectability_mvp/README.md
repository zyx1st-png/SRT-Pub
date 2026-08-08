---
id: SRT-EXP-STAKE-FUTURE-SELECTABILITY-MVP
type: experiment_readme
status: frozen
record_stage: completed_uninterpretable_protocol
layer: lab
epistemic_layer: p4
claim_mode: experiment
canonical: false
---

# Stake–Future Selectability MVP

This independent P4 experiment implements `PersistentChoiceGrid-v0`. It does not continue, reinterpret, or modify the NO-GO selective-resynchronization program.

The target is narrow: test whether an early-B counterfactual critic sensitivity to integrity (`dV_CF_pre`) adds grouped out-of-sample prediction of later C adaptation beyond reward/current performance, energy homeostasis, Reach20/Emp5 controllability, and generic PPO adaptation dynamics.

`dV_CF` and `dPi_CF` are counterfactual stake-sensitivity proxies. They are not canonical `d`. No result establishes consciousness, subjecthood, suffering, or validation of SRT.

## Environment

```bash
uv venv .venv --python 3.12
uv pip install --python .venv/bin/python -r requirements.txt
```

The locked runtime is CPU-first for deterministic auditability.

## Execution order

```bash
uv run --python .venv/bin/python -m pytest tests -q
uv run --python .venv/bin/python scripts/run_smoke.py
uv run --python .venv/bin/python scripts/run_pilot.py
uv run --python .venv/bin/python scripts/lock_formal.py
uv run --python .venv/bin/python scripts/run_formal.py --stage ab
uv run --python .venv/bin/python scripts/run_formal.py --stage c
uv run --python .venv/bin/python scripts/analyze_formal.py
```

The pilot script is A/B-only and never constructs C. Formal pre-C artifacts are immutable and hashed before C instantiation. Analysis re-verifies every hash before joining outcomes.

## Conditions

- X: visible but capability-uncoupled integrity.
- T: B capability coupling with explicit preregistered C reset.
- S: same-bearer persistent capability coupling with no reset/replacement.

Reward and ordinary energy formulas are identical across conditions. Integrity changes capability only through the locked effective-integrity mapping.

## Artifacts

- smoke: `outputs/smoke/`
- A/B-only pilot: `outputs/pilot/`
- formal run: `outputs/formal/`
- formal lock: `manifests/formal_manifest.json`
- paper audit/spec/analysis/decision: `../../papers/stake_future_selectability/`

Raw checkpoints and run-local artifacts remain under `outputs/formal/raw/` and `outputs/formal/checkpoints/`; compact processed results are written under `outputs/formal/processed/`.

The optional Fisher comparator is not implemented in this MVP: per the preregistration it is non-privileged, while update norm, path length, gradient norm, policy KL, entropy, and representation drift provide the locked generic-adaptation controls. Its absence cannot be repaired or promoted after formal inspection.

## Result

The complete 12×6 formal cohort finished. The frozen decision is **UNINTERPRETABLE PROTOCOL** because 8/48 T/S cells failed the preregistered per-cell Reach20 reduction gate. The other structural checks passed: 24/24 T resets, 24/24 S persistence checks, 72/72 identity checks, zero replacements, and 72/72 pre-C hash verifications.

The unfavorable predictive result is retained but not promoted over the failed structural gate: M4 versus M3 changed LOSO CV R² by −1.0275 and worsened NRMSE by 13.04%; standardized `dV_CF_pre` β was 0.0300 with master-seed bootstrap 95% interval [−0.2610, 0.1924]. See `../../papers/stake_future_selectability/03_mvp_decision.md` and `outputs/formal/processed/confirmatory_results.json`.
