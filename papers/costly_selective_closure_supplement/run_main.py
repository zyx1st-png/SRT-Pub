"""Regenerate results/main_results.json: main experiment, 30 seeds, matched
death penalty in all regimes. Thin wrapper around src/csc_experiment.py.

    python run_main.py
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "src"))
import csc_experiment as ce  # noqa: E402

ce.ROOT = HERE / "results"
ce.ROOT.mkdir(exist_ok=True)
cfg = dict(train_eps=1000, withdraw_eps=300, window=100, lr=0.04, lr_w=0.04, gamma=0.97)
ce.main(cfg, seeds=list(range(1, 31)), out_prefix="main_results")
print("wrote results/main_results.json")
