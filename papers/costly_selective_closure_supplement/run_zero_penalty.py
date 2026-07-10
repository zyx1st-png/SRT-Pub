"""Regenerate results/zero_penalty_results.json: zero-death-penalty ablation
(the only consequence of depletion is that the return stream ends), 30 seeds.
Thin wrapper around src/csc_experiment.py.

    python run_zero_penalty.py
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "src"))
import csc_experiment as ce  # noqa: E402

ce.ROOT = HERE / "results"
ce.ROOT.mkdir(exist_ok=True)
cfg = dict(train_eps=1000, withdraw_eps=300, window=100, lr=0.04, lr_w=0.04,
           gamma=0.97, death_penalty=0.0, sim_danger_penalty=1.5)
ce.main(cfg, seeds=list(range(1, 31)), out_prefix="zero_penalty_results")
print("wrote results/zero_penalty_results.json")
