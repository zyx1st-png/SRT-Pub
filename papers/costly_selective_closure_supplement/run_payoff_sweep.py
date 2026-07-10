"""Regenerate results/payoff_sweep_results.json: payoff sweep over three
temptation values x two starvation settings, real (one life) vs resettable
(unbounded), 15 seeds per cell. Thin wrapper around src/csc_robustness.py.

    python run_payoff_sweep.py
"""
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "src"))
import csc_robustness as cr  # noqa: E402

results = HERE / "results"
results.mkdir(exist_ok=True)
cr.ROOT = results
cr.sweep(list(range(1, 16)))
os.replace(results / "results_sweep.json", results / "payoff_sweep_results.json")
print("wrote results/payoff_sweep_results.json")
