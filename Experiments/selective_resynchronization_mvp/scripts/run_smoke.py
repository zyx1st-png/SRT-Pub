from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.protocol import ProtocolRunner  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default=None)
    parser.add_argument("--no-force", action="store_true")
    args = parser.parse_args()
    runner = ProtocolRunner(ROOT, ROOT / "configs" / "smoke.yaml", device=args.device)
    runner.run_full(seed=9001, condition="standard", force=not args.no_force)
    print(f"Smoke complete on {runner.device}: {runner.output_root}")


if __name__ == "__main__":
    main()
