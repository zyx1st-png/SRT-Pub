from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.protocol import ProtocolRunner


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=ROOT / "configs/smoke.yaml")
    args = parser.parse_args()
    runner = ProtocolRunner(ROOT, args.config)
    results = []
    for seed in runner.config["master_seeds"]:
        runner.run_a(int(seed))
        for cell in runner.config["conditions"]:
            runner.run_ab_cell(int(seed), str(cell))
            results.append(runner.run_c_cell(int(seed), str(cell)))
    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
