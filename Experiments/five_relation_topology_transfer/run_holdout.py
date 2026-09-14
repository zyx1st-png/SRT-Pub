from __future__ import annotations

import json
from pathlib import Path
import numpy as np

from model import load_config, run_control_a, run_control_b

ROOT = Path(__file__).resolve().parent
CONFIG = ROOT / "config_frozen_v1.json"
OUT = ROOT / "results_holdout_v1.json"


def summarize_pair(left, right, keys):
    out = {}
    for key in keys:
        a = np.asarray([x[key] for x in left], dtype=float)
        b = np.asarray([x[key] for x in right], dtype=float)
        d = b - a
        out[key] = {
            "left_mean": float(a.mean()),
            "right_mean": float(b.mean()),
            "paired_diff_mean": float(d.mean()),
            "paired_diff_sd": float(d.std(ddof=1)) if len(d) > 1 else 0.0,
            "paired_diff_median": float(np.median(d)),
            "nonzero_pair_count": int(np.count_nonzero(np.abs(d) > 1e-12)),
        }
    return out


def main():
    c = load_config(CONFIG)

    a_seeds = range(c["A_holdout_seed_start"], c["A_holdout_seed_start"] + c["A_holdout_seed_count"])
    ext = [run_control_a(s, "externalized", c) for s in a_seeds]
    ret = [run_control_a(s, "returned_revision", c) for s in a_seeds]

    match = {
        "pre_reward_max_abs_diff": float(max(abs(x["pre_reward"] - y["pre_reward"]) for x, y in zip(ext, ret))),
        "pre_cost_max_abs_diff": float(max(abs(x["pre_cost"] - y["pre_cost"]) for x, y in zip(ext, ret))),
        "pre_alt_mass_max_abs_diff": float(max(abs(x["pre_alt_mass"] - y["pre_alt_mass"]) for x, y in zip(ext, ret))),
    }
    match_pass = (
        match["pre_reward_max_abs_diff"] <= c["A_match_tolerance_reward"]
        and match["pre_cost_max_abs_diff"] <= c["A_match_tolerance_cost"]
        and match["pre_alt_mass_max_abs_diff"] <= c["A_match_tolerance_alt_mass"]
    )

    b_seeds = range(c["B_replication_seed_start"], c["B_replication_seed_start"] + c["B_replication_seed_count"])
    bp = [run_control_b(s, "policy_only", c) for s in b_seeds]
    bg = [run_control_b(s, "generator_revision", c) for s in b_seeds]

    result = {
        "config_status": c["status"],
        "seed_status": {
            "A_holdout": [c["A_holdout_seed_start"], c["A_holdout_seed_start"] + c["A_holdout_seed_count"] - 1],
            "B_replication": [c["B_replication_seed_start"], c["B_replication_seed_start"] + c["B_replication_seed_count"] - 1],
            "pilot_ranges_excluded": [[c["A_pilot_seed_start"], c["A_pilot_seed_start"] + c["A_pilot_seed_count"] - 1], [c["B_pilot_seed_start"], c["B_pilot_seed_start"] + c["B_pilot_seed_count"] - 1]],
        },
        "control_A": {
            "interpretation": "conditional-discrimination-test",
            "matching": match,
            "matching_pass": bool(match_pass),
            "summary": summarize_pair(
                ext,
                ret,
                [
                    "post_reward_early",
                    "post_reward_late",
                    "post_cost_early",
                    "post_cost_late",
                    "post_alt_mass_early",
                    "post_alt_mass_late",
                ],
            ),
        },
        "control_B": {
            "interpretation": "calibration-only",
            "summary": summarize_pair(
                bp,
                bg,
                ["pre_performance", "post_performance_early", "post_performance_late"],
            ),
        },
        "guards": {
            "bearer_claim": False,
            "canonical_claim": False,
            "distinctiveness_claim": False,
            "control_B_counts_toward_distinctiveness": False,
        },
    }

    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
