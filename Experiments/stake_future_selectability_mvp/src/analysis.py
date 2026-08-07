from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.stats import spearmanr
from sklearn.linear_model import Ridge

from .protocol import verify_preC_files
from .utils import write_json


BLOCKS = {
    "M0": [
        "B_end_success",
        "B_end_return",
        "B_end_integrity",
        "B_hazard_contacts",
        "B_cumulative_reward",
    ],
    "M1": ["B_energy_deviation_area"],
    "M2": ["Reach20", "Emp5"],
    "M3": [
        "representation_drift_area",
        "policy_KL_area",
        "cumulative_update_norm",
        "cumulative_parameter_path_length",
    ],
    "M4": ["dV_CF_pre"],
}


def features_for(model: str) -> list[str]:
    order = ["M0", "M1", "M2", "M3", "M4"]
    features: list[str] = []
    for name in order:
        features.extend(BLOCKS[name])
        if name == model:
            break
    return features


def _design(train: pd.DataFrame, test: pd.DataFrame, features: list[str]):
    means = train[features].mean()
    scales = train[features].std(ddof=0).replace(0.0, 1.0)
    train_numeric = (train[features] - means) / scales
    test_numeric = (test[features] - means) / scales
    train_x = pd.DataFrame({"intercept": np.ones(len(train))}, index=train.index)
    test_x = pd.DataFrame({"intercept": np.ones(len(test))}, index=test.index)
    for feature in features:
        train_x[feature] = train_numeric[feature]
        test_x[feature] = test_numeric[feature]
    for condition in ("T", "S"):
        train_x[f"condition_{condition}"] = (train["condition"] == condition).astype(float)
        test_x[f"condition_{condition}"] = (test["condition"] == condition).astype(float)
    train_x["severity_high"] = (train["severity"] == "high").astype(float)
    test_x["severity_high"] = (test["severity"] == "high").astype(float)
    return train_x.astype(float), test_x.astype(float)


def _ols_predict(train: pd.DataFrame, test: pd.DataFrame, features: list[str]) -> np.ndarray:
    train_x, test_x = _design(train, test, features)
    beta = np.linalg.lstsq(train_x.to_numpy(), train["Q_C"].to_numpy(), rcond=None)[0]
    return test_x.to_numpy() @ beta


def grouped_cv(frame: pd.DataFrame, features: list[str]) -> dict[str, Any]:
    predictions = np.full(len(frame), np.nan)
    for seed in sorted(frame["master_seed"].unique()):
        test_mask = frame["master_seed"] == seed
        train = frame.loc[~test_mask]
        test = frame.loc[test_mask]
        predictions[test_mask.to_numpy()] = _ols_predict(train, test, features)
    observed = frame["Q_C"].to_numpy(dtype=float)
    residual = observed - predictions
    sse = float(np.sum(np.square(residual)))
    sst = float(np.sum(np.square(observed - observed.mean())))
    r2 = 1.0 - sse / sst if sst > 0 else float("nan")
    rmse = float(np.sqrt(np.mean(np.square(residual))))
    sd = float(np.std(observed, ddof=0))
    return {"cv_r2": r2, "nrmse": rmse / sd if sd > 0 else float("nan"), "predictions": predictions}


def full_ols(frame: pd.DataFrame, features: list[str]):
    design, _ = _design(frame, frame, features)
    result = sm.OLS(frame["Q_C"].astype(float), design).fit(cov_type="HC3")
    return result, design


def _standard_beta(frame: pd.DataFrame, features: list[str], coefficient: str = "dV_CF_pre") -> float:
    try:
        result, _ = full_ols(frame, features)
        return float(result.params[coefficient])
    except Exception:
        return float("nan")


def cluster_bootstrap_beta(
    frame: pd.DataFrame, features: list[str], *, samples: int = 2000, seed: int = 20260808
) -> tuple[float, float, np.ndarray]:
    rng = np.random.default_rng(seed)
    seeds = np.asarray(sorted(frame["master_seed"].unique()))
    estimates = []
    for _ in range(samples):
        selected = rng.choice(seeds, size=len(seeds), replace=True)
        parts = []
        for copy_index, selected_seed in enumerate(selected):
            part = frame[frame["master_seed"] == selected_seed].copy()
            part["master_seed"] = copy_index
            parts.append(part)
        estimate = _standard_beta(pd.concat(parts, ignore_index=True), features)
        if np.isfinite(estimate):
            estimates.append(estimate)
    values = np.asarray(estimates, dtype=float)
    if len(values) < samples * 0.9:
        return float("nan"), float("nan"), values
    low, high = np.quantile(values, [0.025, 0.975])
    return float(low), float(high), values


def paired_s_minus_x(frame: pd.DataFrame) -> pd.DataFrame:
    pivot = frame.pivot_table(index=["master_seed", "severity"], columns="condition", values="dV_CF_pre")
    pivot["S_minus_X"] = pivot["S"] - pivot["X"]
    return pivot.reset_index()


def paired_cluster_bootstrap(values: pd.DataFrame, samples: int = 2000, seed: int = 20260809):
    rng = np.random.default_rng(seed)
    seeds = np.asarray(sorted(values["master_seed"].unique()))
    estimates = []
    for _ in range(samples):
        selected = rng.choice(seeds, size=len(seeds), replace=True)
        sample = pd.concat([values[values["master_seed"] == item] for item in selected], ignore_index=True)
        estimates.append(float(sample["S_minus_X"].mean()))
    return float(values["S_minus_X"].mean()), [float(x) for x in np.quantile(estimates, [0.025, 0.975])]


def paired_contrast(
    frame: pd.DataFrame,
    outcome: str,
    left: str,
    right: str,
    *,
    samples: int = 2000,
    seed: int = 20260810,
) -> dict[str, Any]:
    pivot = frame.pivot_table(index=["master_seed", "severity"], columns="condition", values=outcome)
    values = (pivot[left] - pivot[right]).rename("difference").reset_index()
    rng = np.random.default_rng(seed)
    master_seeds = np.asarray(sorted(values["master_seed"].unique()))
    estimates = []
    for _ in range(samples):
        selected = rng.choice(master_seeds, size=len(master_seeds), replace=True)
        sample = pd.concat([values[values.master_seed == item] for item in selected], ignore_index=True)
        estimates.append(float(sample["difference"].mean()))
    return {
        "left": left,
        "right": right,
        "outcome": outcome,
        "mean_difference": float(values["difference"].mean()),
        "master_seed_bootstrap_95": [float(x) for x in np.quantile(estimates, [0.025, 0.975])],
    }


def _spearman(frame: pd.DataFrame, left: str, right: str) -> dict[str, float]:
    coefficient, p_value = spearmanr(frame[left].astype(float), frame[right].astype(float))
    return {"rho": float(coefficient), "p_value_descriptive": float(p_value)}


def _ridge_nested_cv(frame: pd.DataFrame, features: list[str]) -> dict[str, Any]:
    alphas = [0.01, 0.1, 1.0, 10.0, 100.0]
    predictions = np.full(len(frame), np.nan)
    selected_alphas = []
    for outer_seed in sorted(frame["master_seed"].unique()):
        outer_test = frame[frame["master_seed"] == outer_seed]
        outer_train = frame[frame["master_seed"] != outer_seed]
        scores = []
        for alpha in alphas:
            errors = []
            for inner_seed in sorted(outer_train["master_seed"].unique()):
                inner_test = outer_train[outer_train["master_seed"] == inner_seed]
                inner_train = outer_train[outer_train["master_seed"] != inner_seed]
                train_x, test_x = _design(inner_train, inner_test, features)
                model = Ridge(alpha=alpha, fit_intercept=False).fit(train_x, inner_train["Q_C"])
                errors.extend((inner_test["Q_C"].to_numpy() - model.predict(test_x)).tolist())
            scores.append(float(np.mean(np.square(errors))))
        alpha = alphas[int(np.argmin(scores))]
        selected_alphas.append(alpha)
        train_x, test_x = _design(outer_train, outer_test, features)
        model = Ridge(alpha=alpha, fit_intercept=False).fit(train_x, outer_train["Q_C"])
        predictions[outer_test.index.to_numpy()] = model.predict(test_x)
    observed = frame["Q_C"].to_numpy()
    sse = float(np.sum(np.square(observed - predictions)))
    sst = float(np.sum(np.square(observed - observed.mean())))
    nrmse = float(np.sqrt(np.mean(np.square(observed - predictions))) / np.std(observed, ddof=0))
    return {"cv_r2": 1.0 - sse / sst, "nrmse": nrmse, "selected_alphas": selected_alphas}


def manipulation_validity(
    frame: pd.DataFrame, outcomes: pd.DataFrame, thresholds: dict[str, float]
) -> dict[str, Any]:
    x_delta = frame.loc[frame.condition == "X", "manip_reach_delta"].abs()
    coupled_delta = frame.loc[frame.condition.isin(["T", "S"]), "manip_reach_delta"]
    tolerance = float(thresholds["identity_absolute_tolerance"])
    x_ok = bool((x_delta <= float(thresholds["x_max_abs_reach_delta"])).all())
    coupled_ok = bool((coupled_delta > float(thresholds["ts_min_reach_delta"])).all())
    t = outcomes[outcomes.condition == "T"]
    s = outcomes[outcomes.condition == "S"]
    t_reset = bool(
        t["B_to_C_reset"].all()
        and np.allclose(t["C_start_integrity"], 1.0, rtol=0.0, atol=tolerance)
    )
    s_persist = bool(
        (~s["B_to_C_reset"]).all()
        and np.allclose(
            s["C_start_integrity"], s["B_to_C_integrity_before"], rtol=0.0, atol=tolerance
        )
    )
    identity = bool(outcomes["identity_continuity_BC"].all() and (~outcomes["B_to_C_replacement"]).all())
    return {
        "X_uncoupled": x_ok,
        "X_max_abs_reach_delta": float(x_delta.max()),
        "TS_reach_reduction": coupled_ok,
        "TS_min_reach_delta": float(coupled_delta.min()),
        "T_reset": t_reset,
        "S_persistence": s_persist,
        "same_bearer_identity": identity,
        "all_valid": bool(x_ok and coupled_ok and t_reset and s_persist and identity),
    }


def analyze(experiment_root: Path, config: dict[str, Any], output_root: Path) -> dict[str, Any]:
    raw_root = output_root / "raw"
    protocol_errors = []
    missing_cells = []
    pre_rows = []
    outcome_rows = []
    for seed in config["master_seeds"]:
        for cell in config["conditions"]:
            run_dir = raw_root / f"master_{seed}" / cell
            required_pre = [
                run_dir / "preC_features.sha256",
                run_dir / "preC_features.json",
                run_dir / "preC_features.parquet",
            ]
            if not all(path.exists() for path in required_pre):
                missing_cells.append({"master_seed": seed, "cell": cell, "stage": "preC"})
                continue
            try:
                verify_preC_files(run_dir)
            except Exception as exc:
                protocol_errors.append({"master_seed": seed, "cell": cell, "error": str(exc)})
                continue
            outcome_path = run_dir / "C_outcomes.json"
            if not outcome_path.exists():
                missing_cells.append({"master_seed": seed, "cell": cell, "stage": "C"})
                continue
            pre_rows.append(pd.read_parquet(run_dir / "preC_features.parquet").iloc[0].to_dict())
            outcome_rows.append(json.loads(outcome_path.read_text(encoding="utf-8")))
    pre = pd.DataFrame(pre_rows)
    outcomes = pd.DataFrame(outcome_rows)
    frame = pre.merge(outcomes, on=["master_seed", "cell", "condition", "severity"], validate="one_to_one")
    frame = frame.reset_index(drop=True)
    processed = output_root / "processed"
    processed.mkdir(parents=True, exist_ok=True)
    frame.to_parquet(processed / "locked_analysis_frame.parquet", index=False)
    model_rows = []
    cv_results = {}
    for name in ("M0", "M1", "M2", "M3", "M4"):
        result = grouped_cv(frame, features_for(name))
        cv_results[name] = result
        model_rows.append({"model": name, "cv_r2": result["cv_r2"], "nrmse": result["nrmse"]})
    pd.DataFrame(model_rows).to_csv(processed / "model_comparison.csv", index=False)
    m4_features = features_for("M4")
    full_result, design = full_ols(frame, m4_features)
    beta = float(full_result.params["dV_CF_pre"])
    hc3_interval = [float(x) for x in full_result.conf_int().loc["dV_CF_pre"].tolist()]
    decision_thresholds = config["decision_thresholds"]
    bootstrap_samples = int(decision_thresholds["cluster_bootstrap_samples"])
    bootstrap_low, bootstrap_high, bootstrap_values = cluster_bootstrap_beta(
        frame, m4_features, samples=bootstrap_samples
    )
    leave_seed = {}
    for seed in sorted(frame["master_seed"].unique()):
        leave_seed[str(seed)] = _standard_beta(frame[frame.master_seed != seed], m4_features)
    severity_beta = {
        severity: _standard_beta(frame[frame.severity == severity], m4_features)
        for severity in ("low", "high")
    }
    sx_values = paired_s_minus_x(frame)
    sx_mean, sx_interval = paired_cluster_bootstrap(sx_values, samples=bootstrap_samples)
    validity = manipulation_validity(frame, outcomes, config["validity_thresholds"])
    delta_r2 = float(cv_results["M4"]["cv_r2"] - cv_results["M3"]["cv_r2"])
    nrmse_improvement = float(
        (cv_results["M3"]["nrmse"] - cv_results["M4"]["nrmse"]) / cv_results["M3"]["nrmse"]
    )
    condition_number = float(np.linalg.cond(design.to_numpy()))
    ridge = None
    if (
        not np.isfinite(condition_number)
        or condition_number > float(decision_thresholds["ols_condition_number_ridge_trigger"])
        or np.linalg.matrix_rank(design) < design.shape[1]
    ):
        ridge = {
            "M3": _ridge_nested_cv(frame, features_for("M3")),
            "M4": _ridge_nested_cv(frame, features_for("M4")),
        }
    completed_seeds = int(frame["master_seed"].nunique())
    completed_cells = int(len(frame))
    no_seed_sign_flip = bool(all(value > 0 for value in leave_seed.values()))
    large_reversal = float(decision_thresholds["severity_large_reversal"])
    severity_ok = bool(
        (severity_beta["low"] > 0 and severity_beta["high"] > 0)
        or (severity_beta["low"] > 0 and severity_beta["high"] > large_reversal)
        or (severity_beta["high"] > 0 and severity_beta["low"] > large_reversal)
    )
    criteria = {
        "manipulation_valid": validity["all_valid"],
        "S_dV_exceeds_X_nontrivially": sx_mean > 0 and sx_interval[0] > 0,
        "positive_beta_bootstrap_excludes_zero": beta > 0 and bootstrap_low > 0,
        "delta_cv_r2_ge_0_03": delta_r2 >= float(decision_thresholds["delta_cv_r2_min"]),
        "nrmse_reduction_ge_3pct": nrmse_improvement
        >= float(decision_thresholds["relative_nrmse_reduction_min"]),
        "not_one_seed": no_seed_sign_flip,
        "severity_robust": severity_ok,
        "no_leakage_or_protocol_failure": len(protocol_errors) == 0,
    }
    if protocol_errors:
        decision = "UNINTERPRETABLE PROTOCOL"
    elif completed_seeds < 12 or completed_cells < 72:
        decision = "INCONCLUSIVE / UNDERPOWERED"
    elif not validity["all_valid"]:
        decision = "UNINTERPRETABLE PROTOCOL"
    elif all(criteria.values()):
        decision = "SRT-BRIDGE GO"
    else:
        no_go = bool(
            (sx_mean <= 0)
            or (beta <= 0 and bootstrap_high <= 0)
            or (delta_r2 <= 0 and nrmse_improvement <= 0)
            or (not no_seed_sign_flip)
        )
        decision = "NO-GO" if no_go else "NARROW"
    secondary = {
        "paired_condition_contrasts": {
            f"{left}_minus_{right}_{outcome}": paired_contrast(frame, outcome, left, right)
            for outcome in ("dV_CF_pre", "Q_C")
            for left, right in (("S", "X"), ("S", "T"), ("T", "X"))
        },
        "dV_vs_hazard_contacts": _spearman(frame, "dV_CF_pre", "B_hazard_contacts"),
        "dV_vs_preserved_integrity": _spearman(frame, "dV_CF_pre", "B_end_integrity"),
        "dV_vs_representation_drift": _spearman(frame, "dV_CF_pre", "representation_drift_area"),
        "dV_vs_parameter_path": _spearman(frame, "dV_CF_pre", "cumulative_parameter_path_length"),
        "dPi_vs_dV": _spearman(frame, "dPi_CF_pre", "dV_CF_pre"),
        "dV_vs_post_C_Reach20": _spearman(frame, "dV_CF_pre", "post_C_Reach20"),
        "fisher_comparator": "not_implemented_optional_non_privileged",
    }
    result = {
        "decision": decision,
        "completed_master_seeds": completed_seeds,
        "completed_cells": completed_cells,
        "model_comparison": model_rows,
        "delta_cv_r2_M4_minus_M3": delta_r2,
        "relative_nrmse_reduction_M4_vs_M3": nrmse_improvement,
        "standardized_dV_beta": beta,
        "dV_beta_HC3_95": hc3_interval,
        "dV_beta_master_seed_bootstrap_95": [bootstrap_low, bootstrap_high],
        "S_minus_X_dV_mean": sx_mean,
        "S_minus_X_dV_bootstrap_95": sx_interval,
        "leave_one_seed_beta": leave_seed,
        "severity_beta": severity_beta,
        "condition_number": condition_number,
        "frozen_thresholds": {
            "validity": config["validity_thresholds"],
            "decision": decision_thresholds,
        },
        "ridge_sensitivity": ridge,
        "manipulation_validity": validity,
        "criteria": criteria,
        "failed_criteria": [name for name, passed in criteria.items() if not passed],
        "protocol_errors": protocol_errors,
        "missing_cells": missing_cells,
        "secondary": secondary,
    }
    write_json(processed / "confirmatory_results.json", result)
    write_json(
        processed / "robustness_checks.json",
        {
            "leave_one_seed_beta": leave_seed,
            "severity_beta": severity_beta,
            "ridge_sensitivity": ridge,
            "bootstrap_valid_samples": int(len(bootstrap_values)),
        },
    )
    return result
