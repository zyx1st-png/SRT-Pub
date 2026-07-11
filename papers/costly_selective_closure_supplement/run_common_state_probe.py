"""Run the common-state policy probe -> results/common_state_probe.json.

Retrains the experiment (evaluation seeds and separate bank-generation seeds),
saves two frozen checkpoints per condition, builds a mortality=0 common-support
observation bank, and scores every frozen policy on the same global bank.

    python run_common_state_probe.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
import csc_probe  # noqa: E402

rep = csc_probe.run()
s = rep["summary"]["end_of_withdrawal"]
d = s["real_minus_resettable"]
print("wrote results/common_state_probe.json")
print(f"bank: {rep['bank']['bank_size']} pairs, {rep['bank']['n_valid_cells']} common-support cells")
print(f"end-of-withdrawal common-state P(CC): real={s['real']['mean']:.3f}  "
      f"resettable={s['resettable']['mean']:.3f}  simulated={s['simulated']['mean']:.3f}")
print(f"real-resettable paired diff={d['mean_diff']:+.3f}  95% CI={d['boot95']}  p={d['paired_signflip_p']:.4f}")
