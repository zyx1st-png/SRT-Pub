"""Run preregistered CSC Experiment 3 consequence-bearing recovery gradient.

    python run_consequence_recovery.py

Confirmatory design is locked in
EXPERIMENT3_CONSEQUENCE_RECOVERY_PREREGISTRATION.md.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "src"))
import csc_consequence_recovery as cc  # noqa: E402

cfg = dict(
    train_eps=1000,
    withdraw_eps=300,
    window=100,
    lr=0.04,
    lr_w=0.04,
    gamma=0.97,
)

out = HERE / "results" / "consequence_recovery_results.json"
payload = cc.run_confirmatory(cfg, seeds=list(range(1, 31)), output_path=out)
print(f"wrote {out}")
print("primary rho:", payload["primary_test"]["tie_aware_spearman_rho"])
print("primary p:", payload["primary_test"]["blocked_by_seed_two_sided_p"])
print("primary supported:", payload["primary_test"]["supported"])
print("endpoint mean diff:", payload["endpoint_k10_minus_k0"]["mean_difference"])
print("endpoint 95% CI:", payload["endpoint_k10_minus_k0"]["paired_bootstrap_95_ci"])
print("strong manuscript support:", payload["strong_manuscript_support"])
print(
    "secondary common-state rho (descriptive):",
    payload["secondary_common_state_probe"]["tie_aware_spearman_rho_descriptive"],
)
