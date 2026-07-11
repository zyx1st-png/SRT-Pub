from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.protocol import MatchedPathRunner  # noqa: E402


def feasibility_passed() -> bool:
    balance_path = ROOT / "outputs" / "feasibility" / "endpoint_balance.csv"
    if not balance_path.exists():
        return False
    balance = pd.read_csv(balance_path)
    matched = balance[balance["matched"] == True]  # noqa: E712
    if len(matched) < 3:
        return False
    diverse = (
        (matched["selected_epoch_range"] >= 2)
        | (matched["selected_representation_drift_range"] >= 0.05)
    )
    return float(diverse.mean()) >= 0.60


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", choices=["feasibility", "locked"], required=True)
    parser.add_argument("--device", default=None)
    args = parser.parse_args()
    if args.stage == "feasibility":
        config = ROOT / "configs" / "feasibility.yaml"
    else:
        if not feasibility_passed():
            raise RuntimeError("Locked A/B cannot start because matching feasibility did not pass")
        config = ROOT / "configs" / "locked_multifuture.yaml"
    runner = MatchedPathRunner(ROOT, config, device=args.device)
    if args.stage == "locked":
        runner.run_ab()
    result = runner.collate_and_freeze(args.stage)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
