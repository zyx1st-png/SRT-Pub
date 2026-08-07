from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
sys.path.insert(0, str(ROOT))

from src.metrics import fixed_action_bank, probe_records
from src.utils import environment_info, git_sha, load_yaml, sha256_file, sha256_paths, utc_now, write_json


def main() -> None:
    config_path = ROOT / "configs/formal_locked.yaml"
    if not config_path.exists():
        raise SystemExit("configs/formal_locked.yaml does not exist")
    pilot_summary = ROOT / "outputs/pilot/pilot_summary.json"
    tracked_pilot_summary = ROOT / "manifests/pilot_summary.json"
    if not pilot_summary.exists() or not tracked_pilot_summary.exists():
        raise SystemExit("A/B-only pilot summary missing")
    if sha256_file(pilot_summary) != sha256_file(tracked_pilot_summary):
        raise SystemExit("tracked pilot summary differs from executed pilot summary")
    if list((ROOT / "outputs/pilot").rglob("C_outcomes.json")):
        raise SystemExit("pilot C outcome exists; formal lock refuses this pilot tree")
    formal_root = ROOT / "outputs/formal"
    if formal_root.exists() and list(formal_root.rglob("C_outcomes.json")):
        raise SystemExit("formal C outcome already exists")
    spec_path = REPO / "papers/stake_future_selectability/01_mvp_spec_lock.md"
    if "status: locked_before_formal" not in spec_path.read_text(encoding="utf-8"):
        raise SystemExit("spec document is not marked locked_before_formal")
    config = load_yaml(config_path)
    probe_manifest = {
        str(seed): probe_records(config, int(seed)) for seed in config["master_seeds"]
    }
    probe_path = ROOT / "manifests/probe_state_bank.json"
    reach_path = ROOT / "manifests/reach20_action_bank.json"
    emp_path = ROOT / "manifests/emp5_action_bank.json"
    write_json(probe_path, probe_manifest)
    write_json(
        reach_path,
        fixed_action_bank(
            int(config["reach20"]["sequences"]),
            int(config["reach20"]["horizon"]),
            int(config["reach20"]["seed"]),
        ).tolist(),
    )
    write_json(
        emp_path,
        fixed_action_bank(
            int(config["emp5"]["sequences"]),
            int(config["emp5"]["horizon"]),
            int(config["emp5"]["seed"]),
        ).tolist(),
    )
    code_paths = [
        *sorted((ROOT / "src").glob("*.py")),
        *sorted((ROOT / "scripts").glob("*.py")),
        *sorted((ROOT / "tests").glob("*.py")),
    ]
    locked_paths = [
        config_path,
        spec_path,
        REPO / "papers/stake_future_selectability/02_analysis_plan.md",
        probe_path,
        reach_path,
        emp_path,
        tracked_pilot_summary,
        ROOT / "requirements.txt",
    ]
    artifact_hashes = {str(path.relative_to(REPO)): sha256_file(path) for path in locked_paths}
    manifest = {
        "lock_status": "formal_scientific_lock",
        "locked_utc": utc_now(),
        "formal_C_outcomes_seen_at_lock": False,
        "pilot_C_outcomes_used": False,
        "pilot_summary_sha256": sha256_file(pilot_summary),
        "git_commit_sha": git_sha(REPO),
        "code_tree_sha256": sha256_paths(code_paths, REPO),
        "environment_module_sha256": sha256_file(ROOT / "src/environment.py"),
        "probe_state_bank_sha256": sha256_file(probe_path),
        "reach20_action_bank_sha256": sha256_file(reach_path),
        "emp5_action_bank_sha256": sha256_file(emp_path),
        "formal_master_seeds": config["master_seeds"],
        "formal_cells": config["conditions"],
        "artifact_hashes": artifact_hashes,
        "environment": environment_info(),
    }
    write_json(ROOT / "manifests/formal_manifest.json", manifest, overwrite=False)
    print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
