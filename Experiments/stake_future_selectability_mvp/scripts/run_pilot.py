from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.protocol import ProtocolRunner


def main() -> None:
    parser = argparse.ArgumentParser(description="A/B-only pilot; this script never constructs C.")
    parser.add_argument("--config", type=Path, default=ROOT / "configs/pilot.yaml")
    args = parser.parse_args()
    runner = ProtocolRunner(ROOT, args.config)
    results = []
    for seed in runner.config["master_seeds"]:
        print(f"[pilot] master seed {seed}: A", flush=True)
        runner.run_a(int(seed))
        for cell in runner.config["conditions"]:
            print(f"[pilot] master seed {seed}: A/B {cell}", flush=True)
            results.append(runner.run_ab_cell(int(seed), str(cell)))
    frame = runner.collate_pre_c()
    x_reach = frame.loc[frame.condition == "X", "manip_reach_delta"].abs()
    ts_reach = frame.loc[frame.condition.isin(["T", "S"]), "manip_reach_delta"]
    x_emp = frame.loc[frame.condition == "X", "manip_emp5_delta"].abs()
    ts_emp = frame.loc[frame.condition.isin(["T", "S"]), "manip_emp5_delta"]
    integrity_by_cell = frame.groupby("cell")["B_end_integrity"].median().to_dict()
    integrity_target = {
        cell: (0.80 <= value <= 0.95 if cell.endswith("low") else 0.60 <= value <= 0.85)
        for cell, value in integrity_by_cell.items()
    }
    summary = {
        "rows": len(frame),
        "integrity_by_cell": integrity_by_cell,
        "integrity_target_by_cell": integrity_target,
        "success_by_cell": frame.groupby("cell")["B_end_success"].mean().to_dict(),
        "dV_by_cell": frame.groupby("cell")["dV_CF_pre"].median().to_dict(),
        "manipulation": {
            "X_max_abs_reach_delta": float(x_reach.max()),
            "TS_min_reach_delta": float(ts_reach.min()),
            "X_max_abs_emp5_delta": float(x_emp.max()),
            "TS_min_emp5_delta": float(ts_emp.min()),
            "X_uncoupled_pass": bool((x_reach <= 1e-12).all()),
            "TS_reach_pass": bool((ts_reach > 0.001).all()),
            "all_integrity_targets_pass": bool(all(integrity_target.values())),
        },
        "C_constructed": False,
    }
    (runner.output_root / "pilot_summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
