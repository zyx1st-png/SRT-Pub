from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.protocol import ProtocolRunner
from src.utils import verify_formal_manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=ROOT / "configs/formal_locked.yaml")
    parser.add_argument("--stage", choices=["ab", "c", "all"], required=True)
    parser.add_argument("--seeds", type=int, nargs="+", help="Disjoint execution shard; values must be locked seeds.")
    args = parser.parse_args()
    try:
        verify_formal_manifest(ROOT)
    except RuntimeError as exc:
        raise SystemExit(str(exc)) from exc
    runner = ProtocolRunner(ROOT, args.config)
    locked_seeds = [int(seed) for seed in runner.config["master_seeds"]]
    seeds = args.seeds if args.seeds is not None else locked_seeds
    if not seeds or len(set(seeds)) != len(seeds) or any(seed not in locked_seeds for seed in seeds):
        raise SystemExit("--seeds must be a non-empty unique subset of the locked formal seed list")
    if args.stage in {"ab", "all"}:
        for seed in seeds:
            print(f"[formal:ab] master seed {seed}: A", flush=True)
            runner.run_a(int(seed))
            for cell in runner.config["conditions"]:
                print(f"[formal:ab] master seed {seed}: {cell}", flush=True)
                runner.run_ab_cell(int(seed), str(cell))
        if args.seeds is None:
            runner.collate_pre_c()
    if args.stage in {"c", "all"}:
        for seed in seeds:
            for cell in runner.config["conditions"]:
                print(f"[formal:c] master seed {seed}: {cell}", flush=True)
                runner.run_c_cell(int(seed), str(cell))
        if args.seeds is None:
            runner.collate_c()


if __name__ == "__main__":
    main()
