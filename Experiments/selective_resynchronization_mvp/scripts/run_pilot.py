from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.protocol import (  # noqa: E402
    ProtocolRunner,
    compute_pilot_standardization,
    compute_state_thresholds,
)


def run_pilot_ab(device: str | None, force: bool) -> None:
    runner = ProtocolRunner(ROOT, ROOT / "configs" / "pilot.yaml", device=device)
    for seed in runner.config["seeds"]:
        for condition in runner.config["conditions"]:
            print(f"pilot AB seed={seed} condition={condition}", flush=True)
            runner.run_ab(seed, condition, no_shift=False, force=force)


def calibrate() -> None:
    compute_pilot_standardization(
        experiment_root=ROOT,
        pilot_root=ROOT / "outputs" / "pilot",
        output_path=ROOT / "manifests" / "pilot_standardization.json",
    )
    print("A/B-only pilot standardization locked", flush=True)


def run_no_shift(device: str | None, force: bool) -> None:
    runner = ProtocolRunner(
        ROOT,
        ROOT / "configs" / "pilot.yaml",
        device=device,
        output_root_override=ROOT / "outputs" / "no_shift_calibration",
    )
    for seed in runner.config["no_shift_seeds"]:
        for condition in runner.config["conditions"]:
            print(f"no-shift AB seed={seed} condition={condition}", flush=True)
            runner.run_ab(seed, condition, no_shift=True, force=force)


def threshold() -> None:
    compute_state_thresholds(
        no_shift_root=ROOT / "outputs" / "no_shift_calibration",
        output_path=ROOT / "manifests" / "state_thresholds.json",
        k=8,
    )
    print("A/B-only state thresholds locked", flush=True)


def run_pilot_c(device: str | None, force: bool) -> None:
    runner = ProtocolRunner(ROOT, ROOT / "configs" / "pilot.yaml", device=device)
    for seed in runner.config["seeds"]:
        for condition in runner.config["conditions"]:
            print(f"pilot C seed={seed} condition={condition}", flush=True)
            runner.run_c(seed, condition, force=force)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--stage",
        choices=["ab", "calibrate", "no-shift", "threshold", "c", "all"],
        default="all",
    )
    parser.add_argument("--device", default=None)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    if args.stage in {"ab", "all"}:
        run_pilot_ab(args.device, args.force)
    if args.stage in {"calibrate", "all"}:
        calibrate()
    if args.stage in {"no-shift", "all"}:
        run_no_shift(args.device, args.force)
    if args.stage in {"threshold", "all"}:
        threshold()
    if args.stage in {"c", "all"}:
        run_pilot_c(args.device, args.force)


if __name__ == "__main__":
    main()
