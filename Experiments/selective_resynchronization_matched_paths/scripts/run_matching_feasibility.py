from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.protocol import MatchedPathRunner  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default=None)
    args = parser.parse_args()
    runner = MatchedPathRunner(ROOT, ROOT / "configs" / "feasibility.yaml", device=args.device)
    runner.run_ab()
    print("Feasibility A/B trajectories complete; no future loader was constructed.")


if __name__ == "__main__":
    main()
