from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass, fields
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import torch

from .environment import EnvSnapshot, PersistentChoiceGrid
from .metrics import (
    counterfactual_sensitivity,
    evaluate_policy,
    linear_cka,
    manipulation_metrics,
    model_readouts,
    observations_from_records,
    policy_kl,
    probe_records,
    reach20,
    emp5,
)
from .model import ActorCritic
from .ppo import build_optimizer, train_steps
from .utils import (
    append_jsonl,
    condition_parts,
    load_yaml,
    make_read_only,
    set_global_seed,
    sha256_file,
    utc_now,
    write_json,
)


@dataclass(frozen=True)
class ABArtifacts:
    master_seed: int
    cell: str
    condition: str
    severity: str
    agent_id: str
    branch_id: str
    a_end_success: float
    a_end_return: float
    b_rows: tuple[dict[str, Any], ...]
    dV_CF_B0: float
    dPi_CF_B0: float
    dV_CF_pre: float
    dPi_CF_pre: float
    manipulation: dict[str, Any]


def assert_ab_only_schema(candidate: type = ABArtifacts) -> None:
    names = {field.name.lower() for field in fields(candidate)}
    forbidden_exact = {"c", "q_c", "c_outcomes", "c_rows", "c_success"}
    leaked = {name for name in names if name in forbidden_exact or name.startswith("c_")}
    if leaked:
        raise AssertionError(f"C-stage field leaked into A/B schema: {sorted(leaked)}")


def reject_c_fields(record: dict[str, Any]) -> None:
    leaked = [key for key in record if key.lower() == "q_c" or key.lower().startswith("c_")]
    if leaked:
        raise ValueError(f"C-stage field supplied to pre-C freeze: {sorted(leaked)}")


def _area(rows: list[dict[str, Any]], key: str) -> float:
    x = np.asarray([float(row["step"]) for row in rows], dtype=np.float64)
    y = np.asarray([float(row[key]) for row in rows], dtype=np.float64)
    if len(rows) < 2:
        return float(y[0]) if len(y) else 0.0
    return float(np.trapezoid(y, x=x) / max(1.0, x[-1] - x[0]))


def compute_preC_features(artifacts: ABArtifacts) -> dict[str, Any]:
    assert_ab_only_schema()
    rows = list(artifacts.b_rows)
    first = rows[0]
    end = rows[-1]
    condition_numeric = {"X": 0.0, "T": 1.0, "S": 2.0}[artifacts.condition]
    result = {
        "master_seed": artifacts.master_seed,
        "cell": artifacts.cell,
        "condition": artifacts.condition,
        "condition_numeric": condition_numeric,
        "severity": artifacts.severity,
        "severity_high": float(artifacts.severity == "high"),
        "agent_id": artifacts.agent_id,
        "branch_id": artifacts.branch_id,
        "uses_c_data": False,
        "created_utc": utc_now(),
        "A_end_success": artifacts.a_end_success,
        "A_end_return": artifacts.a_end_return,
        "B_start_success": float(first["eval_success"]),
        "B_end_success": float(end["eval_success"]),
        "B_success_gain": float(end["eval_success"] - first["eval_success"]),
        "B_end_return": float(end["eval_return"]),
        "B_end_integrity": float(end["integrity"]),
        "B_integrity_loss": float(1.0 - end["integrity"]),
        "B_hazard_contacts": int(end["hazard_contacts"]),
        "B_damage_events": int(end["damage_events"]),
        "B_cumulative_reward": float(end["cumulative_reward"]),
        "B_energy_deviation_area": float(end["energy_deviation_area"]),
        "representation_drift_area": _area(rows, "representation_drift_from_B0"),
        "policy_KL_area": _area(rows, "policy_KL_from_previous"),
        "actor_entropy_area": _area(rows, "actor_entropy"),
        "gradient_norm_area": _area(rows, "gradient_norm"),
        "cumulative_update_norm": float(sum(float(row["parameter_update_norm"]) for row in rows[1:])),
        "cumulative_parameter_path_length": float(sum(float(row["parameter_path_length"]) for row in rows[1:])),
        "Reach20": float(end["reach20_score"]),
        "Reach20_unique_states": float(end["reach20_unique_states"]),
        "Reach20_spatial_area": float(end["reach20_spatial_area"]),
        "Reach20_target_states": float(end["reach20_target_states"]),
        "Reach20_future_entropy": float(end["reach20_future_entropy"]),
        "Emp5": float(end["emp5"]),
        "dV_CF_B0": artifacts.dV_CF_B0,
        "dPi_CF_B0": artifacts.dPi_CF_B0,
        "dV_CF_pre": artifacts.dV_CF_pre,
        "dPi_CF_pre": artifacts.dPi_CF_pre,
        "manip_reach_delta": float(artifacts.manipulation["reach20_score_delta_i1_minus_i07"]),
        "manip_emp5_delta": float(artifacts.manipulation["emp5_delta_i1_minus_i07"]),
        "identity_continuity_AB": True,
    }
    reject_c_fields(result)
    return result


def freeze_preC_files(run_dir: Path, record: dict[str, Any]) -> dict[str, Any]:
    reject_c_fields(record)
    json_path = run_dir / "preC_features.json"
    parquet_path = run_dir / "preC_features.parquet"
    hash_path = run_dir / "preC_features.sha256"
    for path in (json_path, parquet_path, hash_path):
        if path.exists():
            raise FileExistsError(f"immutable pre-C artifact already exists: {path}")
    write_json(json_path, record, overwrite=False)
    pd.DataFrame([record]).to_parquet(parquet_path, index=False)
    hash_record = {
        "created_utc": utc_now(),
        "parquet": parquet_path.name,
        "parquet_sha256": sha256_file(parquet_path),
        "json_sha256": sha256_file(json_path),
    }
    write_json(hash_path, hash_record, overwrite=False)
    for path in (json_path, parquet_path, hash_path):
        make_read_only(path)
    return hash_record


def verify_preC_files(run_dir: Path) -> dict[str, Any]:
    record = json.loads((run_dir / "preC_features.sha256").read_text(encoding="utf-8"))
    if sha256_file(run_dir / record["parquet"]) != record["parquet_sha256"]:
        raise RuntimeError("frozen pre-C Parquet hash mismatch")
    if sha256_file(run_dir / "preC_features.json") != record["json_sha256"]:
        raise RuntimeError("frozen pre-C JSON hash mismatch")
    return record


def _snapshot_from_dict(value: dict[str, Any]) -> EnvSnapshot:
    return EnvSnapshot(
        phase=value["phase"],
        integrity=float(value["integrity"]),
        energy=float(value["energy"]),
        agent_id=value["agent_id"],
        branch_id=value["branch_id"],
        position=tuple(value["position"]),
        episode_index=int(value["episode_index"]),
        damaged_hazards=tuple(tuple(item) for item in value["damaged_hazards"]),
    )


class ProtocolRunner:
    def __init__(self, experiment_root: Path, config_path: Path, *, output_override: Path | None = None) -> None:
        self.root = experiment_root.resolve()
        self.repo_root = self.root.parents[1]
        self.config_path = config_path.resolve()
        self.config = load_yaml(self.config_path)
        self.output_root = output_override.resolve() if output_override else self.root / self.config["output_root"]
        self.output_root.mkdir(parents=True, exist_ok=True)
        self.device = torch.device(str(self.config.get("device", "cpu")))

    def _a_dir(self, seed: int) -> Path:
        return self.output_root / "checkpoints" / f"master_{seed}" / "A"

    def _run_dir(self, seed: int, cell: str) -> Path:
        return self.output_root / "raw" / f"master_{seed}" / cell

    def _save_checkpoint(self, path: Path, model: ActorCritic, optimizer, metadata: dict[str, Any]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        torch.save({"model": model.state_dict(), "optimizer": optimizer.state_dict(), "metadata": metadata}, path)

    def _load_checkpoint(self, path: Path) -> tuple[ActorCritic, torch.optim.Optimizer, dict[str, Any]]:
        model = ActorCritic().to(self.device)
        optimizer = build_optimizer(model, self.config["ppo"])
        payload = torch.load(path, map_location=self.device, weights_only=False)
        model.load_state_dict(payload["model"])
        optimizer.load_state_dict(payload["optimizer"])
        return model, optimizer, payload["metadata"]

    def run_a(self, master_seed: int) -> dict[str, Any]:
        output_dir = self._a_dir(master_seed)
        checkpoint = output_dir / "A_checkpoint.pt"
        summary_path = output_dir / "A_summary.json"
        if checkpoint.exists() and summary_path.exists():
            return json.loads(summary_path.read_text(encoding="utf-8"))
        output_dir.mkdir(parents=True, exist_ok=True)
        set_global_seed(master_seed)
        agent_id = f"sf-master-{master_seed}"
        env = PersistentChoiceGrid(
            self.config,
            master_seed=master_seed,
            condition="X",
            severity="low",
            phase="A",
            agent_id=agent_id,
            branch_id="A-common",
        )
        model = ActorCritic().to(self.device)
        optimizer = build_optimizer(model, self.config["ppo"])
        before_reward = env.cumulative_reward
        stats = train_steps(model, optimizer, env, int(self.config["steps"]["A"]), self.config["ppo"])
        snapshot = env.snapshot()
        evaluation = evaluate_policy(
            model,
            self.config,
            snapshot,
            master_seed=master_seed,
            condition="X",
            severity="low",
            branch_id="A-common",
            episodes=int(self.config["evaluation_episodes"]),
        )
        summary = {
            "master_seed": master_seed,
            "agent_id": agent_id,
            "steps": int(self.config["steps"]["A"]),
            "success": evaluation["success"],
            "return": evaluation["return"],
            "training_reward": env.cumulative_reward - before_reward,
            "integrity": env.integrity,
            "created_utc": utc_now(),
        }
        self._save_checkpoint(checkpoint, model, optimizer, summary)
        write_json(summary_path, summary)
        return summary

    def run_ab_cell(self, master_seed: int, cell: str) -> dict[str, Any]:
        run_dir = self._run_dir(master_seed, cell)
        complete_path = run_dir / "AB_complete.json"
        if complete_path.exists():
            return json.loads(complete_path.read_text(encoding="utf-8"))
        run_dir.mkdir(parents=True, exist_ok=True)
        a_summary = self.run_a(master_seed)
        condition, severity = condition_parts(cell)
        cell_seed = master_seed * 100 + ["X-low", "X-high", "T-low", "T-high", "S-low", "S-high"].index(cell)
        set_global_seed(cell_seed)
        model, optimizer, a_metadata = self._load_checkpoint(self._a_dir(master_seed) / "A_checkpoint.pt")
        agent_id = a_metadata["agent_id"]
        branch_id = f"master-{master_seed}/{cell}"
        env = PersistentChoiceGrid(
            self.config,
            master_seed=master_seed,
            condition=condition,
            severity=severity,
            phase="B",
            agent_id=agent_id,
            branch_id=branch_id,
        )
        branch_event = {
            "event": "preregistered_A_checkpoint_branch",
            "agent_id": agent_id,
            "branch_id": branch_id,
            "replacement": False,
            "source_checkpoint": str(self._a_dir(master_seed) / "A_checkpoint.pt"),
            "timestamp": utc_now(),
        }
        write_json(run_dir / "branch_event.json", branch_event)
        records = probe_records(self.config, master_seed)
        probe_obs = observations_from_records(
            self.config, records, master_seed=master_seed, condition=condition, severity=severity, integrity=1.0
        )
        baseline_readout = model_readouts(model, probe_obs)
        previous_readout = baseline_readout
        cf_b0 = counterfactual_sensitivity(
            model, self.config, records, master_seed=master_seed, condition=condition, severity=severity
        )
        b0_eval = evaluate_policy(
            model,
            self.config,
            env.snapshot(),
            master_seed=master_seed,
            condition=condition,
            severity=severity,
            branch_id=branch_id,
            episodes=int(self.config["evaluation_episodes"]),
        )
        rows: list[dict[str, Any]] = [
            {
                "step": 0,
                "eval_success": b0_eval["success"],
                "eval_return": b0_eval["return"],
                "integrity": env.integrity,
                "hazard_contacts": 0,
                "damage_events": 0,
                "cumulative_reward": 0.0,
                "energy_deviation_area": 0.0,
                "representation_drift_from_B0": 0.0,
                "policy_KL_from_previous": 0.0,
                "actor_entropy": float(np.mean(baseline_readout["entropy"])),
                "gradient_norm": 0.0,
                "parameter_update_norm": 0.0,
                "parameter_path_length": 0.0,
                "reach20_score": float("nan"),
                "reach20_unique_states": float("nan"),
                "reach20_spatial_area": float("nan"),
                "reach20_target_states": float("nan"),
                "reach20_future_entropy": float("nan"),
                "emp5": float("nan"),
            }
        ]
        early_step = int(self.config["probe"]["early_B_step"])
        total_steps = int(self.config["steps"]["B"])
        interval = int(self.config.get("evaluation_interval_B", early_step))
        checkpoints = sorted(set([early_step, *range(interval, total_steps + 1, interval), total_steps]))
        current_step = 0
        early_cf: dict[str, float] | None = None
        for target_step in checkpoints:
            chunk = target_step - current_step
            reward_before = env.cumulative_reward
            energy_before = env.energy_deviation_area
            stats = train_steps(model, optimizer, env, chunk, self.config["ppo"])
            current_step = target_step
            evaluation = evaluate_policy(
                model,
                self.config,
                env.snapshot(),
                master_seed=master_seed,
                condition=condition,
                severity=severity,
                branch_id=branch_id,
                episodes=int(self.config["evaluation_episodes"]),
            )
            current_readout = model_readouts(model, probe_obs)
            row = {
                "step": current_step,
                "eval_success": evaluation["success"],
                "eval_return": evaluation["return"],
                "integrity": env.integrity,
                "hazard_contacts": env.hazard_contacts,
                "damage_events": env.damage_events,
                "cumulative_reward": env.cumulative_reward,
                "interval_reward": env.cumulative_reward - reward_before,
                "energy_deviation_area": env.energy_deviation_area,
                "interval_energy_deviation": env.energy_deviation_area - energy_before,
                "representation_drift_from_B0": 1.0 - linear_cka(
                    baseline_readout["representations"], current_readout["representations"]
                ),
                "policy_KL_from_previous": policy_kl(
                    previous_readout["probabilities"], current_readout["probabilities"]
                ),
                "actor_entropy": float(np.mean(current_readout["entropy"])),
                "gradient_norm": stats.mean_gradient_norm,
                "parameter_update_norm": stats.parameter_update_norm,
                "parameter_path_length": stats.parameter_path_length,
                "reach20_score": float("nan"),
                "reach20_unique_states": float("nan"),
                "reach20_spatial_area": float("nan"),
                "reach20_target_states": float("nan"),
                "reach20_future_entropy": float("nan"),
                "emp5": float("nan"),
            }
            if current_step == early_step:
                early_cf = counterfactual_sensitivity(
                    model,
                    self.config,
                    records,
                    master_seed=master_seed,
                    condition=condition,
                    severity=severity,
                )
            rows.append(row)
            previous_readout = current_readout
        if early_cf is None:
            raise RuntimeError("early-B counterfactual checkpoint was not evaluated")
        actual_reach = reach20(
            self.config, master_seed=master_seed, condition=condition, severity=severity, integrity=env.integrity
        )
        rows[-1].update(
            {
                "reach20_score": actual_reach["reach20_score"],
                "reach20_unique_states": actual_reach["unique_reachable_states"],
                "reach20_spatial_area": actual_reach["reachable_spatial_area"],
                "reach20_target_states": actual_reach["reachable_target_states"],
                "reach20_future_entropy": actual_reach["future_state_entropy"],
                "emp5": emp5(
                    self.config,
                    master_seed=master_seed,
                    condition=condition,
                    severity=severity,
                    integrity=env.integrity,
                ),
            }
        )
        manipulation = manipulation_metrics(
            self.config, master_seed=master_seed, condition=condition, severity=severity
        )
        artifacts = ABArtifacts(
            master_seed=master_seed,
            cell=cell,
            condition=condition,
            severity=severity,
            agent_id=agent_id,
            branch_id=branch_id,
            a_end_success=float(a_summary["success"]),
            a_end_return=float(a_summary["return"]),
            b_rows=tuple(rows),
            dV_CF_B0=float(cf_b0["dV_CF"]),
            dPi_CF_B0=float(cf_b0["dPi_CF"]),
            dV_CF_pre=float(early_cf["dV_CF"]),
            dPi_CF_pre=float(early_cf["dPi_CF"]),
            manipulation=manipulation,
        )
        pre_c = compute_preC_features(artifacts)
        freeze_preC_files(run_dir, pre_c)
        self._save_checkpoint(run_dir / "B_checkpoint.pt", model, optimizer, {"master_seed": master_seed, "cell": cell})
        snapshot_record = asdict(env.snapshot())
        write_json(run_dir / "B_end_snapshot.json", snapshot_record)
        write_json(run_dir / "B_metrics.json", rows)
        write_json(run_dir / "manipulation_metrics.json", manipulation)
        completion = {
            "master_seed": master_seed,
            "cell": cell,
            "agent_id": agent_id,
            "branch_id": branch_id,
            "B_end_integrity": env.integrity,
            "preC_hash_verified": bool(verify_preC_files(run_dir)),
            "completed_utc": utc_now(),
        }
        write_json(complete_path, completion)
        return completion

    def run_c_cell(self, master_seed: int, cell: str) -> dict[str, Any]:
        run_dir = self._run_dir(master_seed, cell)
        complete_path = run_dir / "C_complete.json"
        if complete_path.exists():
            return json.loads(complete_path.read_text(encoding="utf-8"))
        if not (run_dir / "AB_complete.json").exists():
            raise RuntimeError("A/B must complete before C")
        # Hard boundary: verify immutable A/B artifact before constructing any C-capable environment.
        hash_record = verify_preC_files(run_dir)
        condition, severity = condition_parts(cell)
        model, optimizer, _ = self._load_checkpoint(run_dir / "B_checkpoint.pt")
        b_snapshot = _snapshot_from_dict(json.loads((run_dir / "B_end_snapshot.json").read_text(encoding="utf-8")))
        env = PersistentChoiceGrid(
            self.config,
            master_seed=master_seed,
            condition=condition,
            severity=severity,
            phase="B",
            agent_id=b_snapshot.agent_id,
            branch_id=b_snapshot.branch_id,
        )
        env.restore(b_snapshot)
        transition_event = env.transition_phase("C")
        write_json(run_dir / "B_to_C_event.json", transition_event)
        c_start_snapshot = env.snapshot()
        c0 = evaluate_policy(
            model,
            self.config,
            c_start_snapshot,
            master_seed=master_seed,
            condition=condition,
            severity=severity,
            branch_id=b_snapshot.branch_id,
            episodes=int(self.config["evaluation_episodes"]),
        )
        rows = [{"step": 0, "success": c0["success"], "return": c0["return"], "integrity": env.integrity}]
        total = int(self.config["steps"]["C"])
        interval = int(self.config["evaluation_interval_C"])
        current = 0
        while current < total:
            chunk = min(interval, total - current)
            stats = train_steps(model, optimizer, env, chunk, self.config["ppo"])
            current += chunk
            evaluation = evaluate_policy(
                model,
                self.config,
                env.snapshot(),
                master_seed=master_seed,
                condition=condition,
                severity=severity,
                branch_id=b_snapshot.branch_id,
                episodes=int(self.config["evaluation_episodes"]),
            )
            rows.append(
                {
                    "step": current,
                    "success": evaluation["success"],
                    "return": evaluation["return"],
                    "integrity": env.integrity,
                    "gradient_norm": stats.mean_gradient_norm,
                    "parameter_update_norm": stats.parameter_update_norm,
                    "parameter_path_length": stats.parameter_path_length,
                }
            )
        trained = rows[1:]
        q_c = float(np.mean([row["success"] - c0["success"] for row in trained]))
        threshold = 0.80
        threshold_steps = next((row["step"] for row in trained if row["success"] >= threshold), None)
        post_reach = reach20(
            self.config, master_seed=master_seed, condition=condition, severity=severity, integrity=env.integrity
        )
        pre_c_record = json.loads((run_dir / "preC_features.json").read_text(encoding="utf-8"))
        a_env = PersistentChoiceGrid(
            self.config,
            master_seed=master_seed,
            condition="X",
            severity=severity,
            phase="A",
            agent_id=b_snapshot.agent_id,
            branch_id=b_snapshot.branch_id,
            evaluation=True,
        )
        a_after = evaluate_policy(
            model,
            self.config,
            a_env.snapshot(),
            master_seed=master_seed,
            condition="X",
            severity=severity,
            branch_id=b_snapshot.branch_id,
            episodes=int(self.config["evaluation_episodes"]),
        )
        b_env = PersistentChoiceGrid(
            self.config,
            master_seed=master_seed,
            condition=condition,
            severity=severity,
            phase="B",
            agent_id=b_snapshot.agent_id,
            branch_id=b_snapshot.branch_id,
            evaluation=True,
        )
        b_env.integrity = env.integrity
        b_env.energy = min(0.8, b_env.energy_max)
        b_after = evaluate_policy(
            model,
            self.config,
            b_env.snapshot(),
            master_seed=master_seed,
            condition=condition,
            severity=severity,
            branch_id=b_snapshot.branch_id,
            episodes=int(self.config["evaluation_episodes"]),
        )
        outcome = {
            "master_seed": master_seed,
            "cell": cell,
            "condition": condition,
            "severity": severity,
            "agent_id": b_snapshot.agent_id,
            "branch_id": b_snapshot.branch_id,
            "Q_C": q_c,
            "C0_success": c0["success"],
            "C_final_success": rows[-1]["success"],
            "C_return_AULC": float(np.mean([row["return"] for row in trained])),
            "C_steps_to_success_0_80": threshold_steps,
            "C_failure_rate": 1.0 - rows[-1]["success"],
            "post_C_integrity": env.integrity,
            "post_C_Reach20": post_reach["reach20_score"],
            "post_C_A_success": a_after["success"],
            "post_C_B_success": b_after["success"],
            "A_forgetting": float(pre_c_record["A_end_success"] - a_after["success"]),
            "B_forgetting": float(pre_c_record["B_end_success"] - b_after["success"]),
            "B_to_C_integrity_before": transition_event["integrity_before"],
            "C_start_integrity": transition_event["integrity_after"],
            "B_to_C_reset": transition_event["reset"],
            "B_to_C_replacement": transition_event["replacement"],
            "identity_continuity_BC": b_snapshot.agent_id == env.agent_id and b_snapshot.branch_id == env.branch_id,
            "preC_parquet_sha256": hash_record["parquet_sha256"],
            "completed_utc": utc_now(),
        }
        write_json(run_dir / "C_metrics.json", rows)
        write_json(run_dir / "C_outcomes.json", outcome)
        self._save_checkpoint(run_dir / "C_checkpoint.pt", model, optimizer, outcome)
        write_json(complete_path, outcome)
        return outcome

    def collate_pre_c(self) -> pd.DataFrame:
        rows = []
        for seed in self.config["master_seeds"]:
            for cell in self.config["conditions"]:
                run_dir = self._run_dir(int(seed), str(cell))
                verify_preC_files(run_dir)
                rows.append(pd.read_parquet(run_dir / "preC_features.parquet").iloc[0].to_dict())
        frame = pd.DataFrame(rows)
        processed = self.output_root / "processed"
        processed.mkdir(parents=True, exist_ok=True)
        frame.to_parquet(processed / "preC_features.parquet", index=False)
        frame.to_json(processed / "preC_features.json", orient="records", indent=2)
        return frame

    def collate_c(self) -> pd.DataFrame:
        rows = []
        for seed in self.config["master_seeds"]:
            for cell in self.config["conditions"]:
                path = self._run_dir(int(seed), str(cell)) / "C_outcomes.json"
                rows.append(json.loads(path.read_text(encoding="utf-8")))
        frame = pd.DataFrame(rows)
        processed = self.output_root / "processed"
        processed.mkdir(parents=True, exist_ok=True)
        frame.to_parquet(processed / "C_outcomes.parquet", index=False)
        frame.to_json(processed / "C_outcomes.json", orient="records", indent=2)
        return frame
