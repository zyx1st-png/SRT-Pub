"""Regenerate results/lives_gradient_results.json: lives-gradient dose-response
over allowed respawns {1, 2, 4, 8, unbounded}, 30 seeds. Thin wrapper around
src/csc_robustness.py.

    python run_lives_gradient.py
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
cr.gradient(list(range(1, 31)))
os.replace(results / "results_gradient.json", results / "lives_gradient_results.json")
print("wrote results/lives_gradient_results.json")
