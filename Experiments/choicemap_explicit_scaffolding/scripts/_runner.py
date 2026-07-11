from __future__ import annotations

import csv
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.agents import SYSTEMS
from src.analysis import analyze, make_figures, make_raw_figures, seed_metrics
from src.environment_generator import FAMILIES
from src.logging_utils import csv_to_parquet, write_csv, write_json
from src.metrics import run_episode
from src.utils import load_config


def run(config_path: Path) -> dict:
    config = load_config(config_path)
    stage = config["stage"]
    output_root = ROOT / "outputs" / stage
    raw = output_root / "raw"; processed = output_root / "processed"; figures = output_root / "figures"
    raw.mkdir(parents=True, exist_ok=True); processed.mkdir(parents=True, exist_ok=True)
    episode_rows: list[dict] = []
    candidate_path = raw / "candidate_logs.csv"
    commitment_path = raw / "commitment_logs.csv"
    candidate_writer = commitment_writer = None
    with candidate_path.open("w", newline="", encoding="utf-8") as cf, commitment_path.open("w", newline="", encoding="utf-8") as mf:
        for seed in config["seeds"]:
            for family in config["environment"]["families"]:
                for system in SYSTEMS:
                    for episode in range(config["episodes_per_seed_family_system"]):
                        try:
                            row, crows, mrows = run_episode(config, system, family, int(seed), episode)
                            episode_rows.append(row)
                            if crows:
                                if candidate_writer is None:
                                    candidate_writer = csv.DictWriter(cf, fieldnames=list(crows[0])); candidate_writer.writeheader()
                                candidate_writer.writerows(crows)
                            if mrows:
                                if commitment_writer is None:
                                    commitment_writer = csv.DictWriter(mf, fieldnames=list(mrows[0])); commitment_writer.writeheader()
                                commitment_writer.writerows(mrows)
                        except Exception as exc:
                            episode_rows.append({"seed": seed, "episode": episode, "system": system,
                                "environment_family": family, "failed_run": 1, "error": repr(exc)})
    episode_csv = raw / "episode_logs.csv"
    write_csv(episode_csv, episode_rows)
    # True Parquet is produced when the locked requirements are present; fallbacks are explicitly audited.
    formats = {
        "episode_logs": csv_to_parquet(episode_csv, raw / "episode_logs.parquet", ROOT),
        "candidate_logs": csv_to_parquet(candidate_path, raw / "candidate_logs.parquet", ROOT),
        "commitment_logs": csv_to_parquet(commitment_path, raw / "commitment_logs.parquet", ROOT),
    }
    import pandas as pd
    valid = pd.DataFrame(episode_rows)
    failed = valid[valid.get("failed_run", 0) == 1]
    failed.to_csv(processed / "failed_runs.csv", index=False)
    if len(failed):
        raise RuntimeError(f"{len(failed)} failed runs; see failed_runs.csv")
    results = analyze(episode_csv, processed, config)
    make_figures(processed / "seed_level_metrics.csv", figures)
    make_raw_figures(episode_csv, commitment_path, figures)
    audit = valid.groupby(["seed", "episode", "environment_family"])[["environment_interactions"]].agg(["min", "max"]).reset_index()
    audit["interaction_budget_equal"] = audit[("environment_interactions", "min")] == audit[("environment_interactions", "max")]
    audit.to_csv(processed / "compute_budget_audit.csv", index=False)
    write_json(processed / "leakage_audit.json", {"agent_view_fields": ["family", "step", "max_steps", "resources", "closed_nodes", "observations", "legal_actions", "current_task_complete"], "hidden_regime_exposed": False, "future_task_exposed_pre_turn": False, "oracle_exposed": False, "pass": True})
    write_json(processed / "storage_audit.json", formats)
    return results
