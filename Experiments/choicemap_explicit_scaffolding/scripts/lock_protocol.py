from __future__ import annotations

import csv
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.environment_generator import FAMILIES
from src.future_tasks import task_catalog
from src.utils import load_config, sha256_file, sha256_tree, stable_json_hash

if __name__ == "__main__":
    manifests = ROOT / "manifests"; manifests.mkdir(exist_ok=True)
    config_path = ROOT / "configs" / "confirmatory_locked.yaml"
    cfg = load_config(config_path)
    split = {"calibration_seeds": [1001, 1002], "pilot_seeds": [2101,2102,2103,2104,2105],
             "confirmatory_seeds": cfg["seeds"], "disjoint": True}
    (manifests / "data_split_manifest.json").write_text(json.dumps(split, indent=2), encoding="utf-8")
    with (manifests / "environment_seed_manifest.csv").open("w", newline="", encoding="utf-8") as f:
        w=csv.writer(f); w.writerow(["seed","split"])
        for name, values in [("calibration", split["calibration_seeds"]), ("pilot", split["pilot_seeds"]), ("confirmatory", split["confirmatory_seeds"])]:
            w.writerows((s,name) for s in values)
    future = {"development_templates": [t.task_id for t in task_catalog()[:4]],
              "held_out_templates": [t.task_id for t in task_catalog()[4:]],
              "held_out_regime_combinations": [[0,2],[1,0],[2,1]]}
    (manifests / "future_task_split.json").write_text(json.dumps(future, indent=2), encoding="utf-8")
    hashes = {"confirmatory_locked.yaml": sha256_file(config_path), "future_task_split": stable_json_hash(future),
              "experiment_source_tree": sha256_tree(ROOT),
              "protocol_lock.md": sha256_file(ROOT.parents[1] / "papers" / "choicemap_explicit_scaffolding" / "02_protocol_lock.md"),
              "locked_utc_note": "Generated after pilot; any subsequent change is a protocol deviation."}
    (manifests / "protocol_hashes.json").write_text(json.dumps(hashes, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(hashes, indent=2))
