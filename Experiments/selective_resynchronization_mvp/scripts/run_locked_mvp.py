from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.protocol import ProtocolRunner, create_formal_manifest  # noqa: E402
from src.utils import (  # noqa: E402
    append_jsonl,
    make_read_only,
    sha256_file,
    sha256_paths,
    utc_now,
)


def verify_existing_manifest(runner: ProtocolRunner, path: Path) -> None:
    manifest = json.loads(path.read_text(encoding="utf-8"))
    code_paths = list((ROOT / "src").glob("*.py")) + list((ROOT / "scripts").glob("*.py"))
    checks = {
        "config_sha256": sha256_file(runner.config_path),
        "standardization_sha256": sha256_file(ROOT / runner.config["standardization_constants"]),
        "state_thresholds_sha256": sha256_file(ROOT / runner.config["state_thresholds"]),
        "split_sha256": sha256_file(ROOT / "manifests" / "dataset_splits.json"),
        "probe_sha256": sha256_file(ROOT / "manifests" / "probe_ids.json"),
        "spec_sha256": sha256_file((ROOT / runner.config["spec_lock"]).resolve()),
        "code_tree_sha256": sha256_paths(code_paths, ROOT),
    }
    mismatches = {key: (manifest.get(key), value) for key, value in checks.items() if manifest.get(key) != value}
    if mismatches:
        raise RuntimeError(f"Formal manifest mismatch: {mismatches}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default=None)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--condition", default=None)
    parser.add_argument("--max-runs", type=int, default=None)
    args = parser.parse_args()

    config_path = ROOT / "configs" / "mvp_locked.yaml"
    runner = ProtocolRunner(ROOT, config_path, device=args.device)
    if runner.standardization_constants is None:
        raise RuntimeError("A/B-only pilot standardization is missing")
    threshold_path = ROOT / runner.config["state_thresholds"]
    if not threshold_path.exists():
        raise RuntimeError("A/B-only state thresholds are missing")

    manifest_path = ROOT / "manifests" / "formal_lock_manifest.json"
    if manifest_path.exists():
        verify_existing_manifest(runner, manifest_path)
    else:
        snapshot = ROOT / "manifests" / "mvp_locked.snapshot.yaml"
        shutil.copy2(config_path, snapshot)
        make_read_only(snapshot)
        create_formal_manifest(ROOT, config_path)
        make_read_only(manifest_path)

    seeds = [args.seed] if args.seed is not None else runner.config["seeds"]
    conditions = [args.condition] if args.condition is not None else runner.config["conditions"]
    completed = 0
    for seed in seeds:
        if seed not in runner.config["seeds"]:
            raise ValueError(f"Seed {seed} is not in the locked seed list")
        for condition in conditions:
            if condition not in runner.config["conditions"]:
                raise ValueError(f"Condition {condition} is not locked")
            if args.max_runs is not None and completed >= args.max_runs:
                return
            print(f"locked run seed={seed} condition={condition} device={runner.device}", flush=True)
            try:
                runner.run_full(seed, condition, force=False)
            except Exception as exc:
                append_jsonl(
                    ROOT / "outputs" / "logs" / "locked_failures.jsonl",
                    {
                        "seed": seed,
                        "condition": condition,
                        "error_type": type(exc).__name__,
                        "message": str(exc),
                        "timestamp_utc": utc_now(),
                    },
                )
                print(f"FAILED seed={seed} condition={condition}: {exc}", flush=True)
            completed += 1


if __name__ == "__main__":
    main()
