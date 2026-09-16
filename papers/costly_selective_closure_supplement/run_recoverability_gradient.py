"""Run preregistered CSC Experiment 2 recoverability gradient.

    python run_recoverability_gradient.py

Confirmatory design is locked in EXPERIMENT2_RECOVERABILITY_PREREGISTRATION.md.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "src"))
import csc_recoverability as cr  # noqa: E402

cfg = dict(
    train_eps=1000,
    withdraw_eps=300,
    window=100,
    lr=0.04,
    lr_w=0.04,
    gamma=0.97,
)
out = HERE / "results" / "recoverability_gradient_results.json"
payload = cr.run_confirmatory(cfg, seeds=list(range(1, 31)), output_path=out)
print(f"wrote {out}")
print("primary rho:", payload["primary_test"]["tie_aware_spearman_rho"])
print("primary p:", payload["primary_test"]["blocked_by_seed_two_sided_p"])
print("primary supported:", payload["primary_test"]["supported"])
print("endpoint mean diff:", payload["endpoint_tau_inf_minus_tau0"]["mean_difference"])
print("endpoint 95% CI:", payload["endpoint_tau_inf_minus_tau0"]["paired_bootstrap_95_ci"])
print("strong manuscript support:", payload["strong_manuscript_support"])
