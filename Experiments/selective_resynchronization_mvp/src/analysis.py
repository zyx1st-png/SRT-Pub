from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from scipy.stats import spearmanr
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

from .protocol import verify_preC_files
from .utils import load_yaml, sha256_file, utc_now, write_json


TARGET = "Q_C_changed_AULC_gain"
M0_CONTINUOUS = [
    "B_end_validation_accuracy",
    "B_end_validation_loss",
    "A_end_validation_accuracy",
]
SIMPLE_FEATURES = [
    "gradient_norm_area",
    "update_norm_area",
    "parameter_distance_B_end",
    "predictive_KL_area",
    "predictive_entropy_change_area",
    "representation_drift_area",
]
COMPONENTS = [
    "opening_dimension",
    "stabilization_dimension",
    "adaptation_dimension",
    "nonrollback_dimension",
    "incorporation_dimension",
]


@dataclass
class ModelResult:
    name: str
    features: list[str]
    n: int
    adjusted_r2: float
    cv_r2: float
    cv_rmse: float
    cv_nrmse: float
    cv_mae: float


def _condition_dummies(frame: pd.DataFrame) -> pd.DataFrame:
    categories = ["constrained", "standard", "high_update", "replay"]
    categorical = pd.Categorical(frame["condition"], categories=categories)
    return pd.get_dummies(categorical, prefix="condition", drop_first=True, dtype=float)


def design_frame(frame: pd.DataFrame, features: list[str]) -> pd.DataFrame:
    numeric = frame[features].astype(float).copy()
    dummies = _condition_dummies(frame)
    return pd.concat([numeric.reset_index(drop=True), dummies.reset_index(drop=True)], axis=1)


def fit_standardized_ols(frame: pd.DataFrame, features: list[str]):
    x = design_frame(frame, features)
    continuous_columns = [column for column in x.columns if not column.startswith("condition_")]
    x.loc[:, continuous_columns] = StandardScaler().fit_transform(x[continuous_columns])
    y = frame[TARGET].to_numpy(dtype=float)
    y = (y - y.mean()) / (y.std(ddof=0) + 1e-12)
    x = sm.add_constant(x, has_constant="add")
    fitted = sm.OLS(y, x).fit().get_robustcov_results(cov_type="HC3")
    names = list(x.columns)
    params = dict(zip(names, fitted.params, strict=True))
    ses = dict(zip(names, fitted.bse, strict=True))
    pvalues = dict(zip(names, fitted.pvalues, strict=True))
    intervals = {
        name: [float(low), float(high)]
        for name, (low, high) in zip(names, fitted.conf_int(), strict=True)
    }
    return fitted, params, ses, pvalues, intervals


def cross_validated_predictions(
    frame: pd.DataFrame,
    features: list[str],
) -> tuple[np.ndarray, dict[str, float]]:
    predictions = np.full(len(frame), np.nan, dtype=float)
    for seed in sorted(frame["seed"].unique()):
        train_mask = frame["seed"] != seed
        test_mask = ~train_mask
        train = frame.loc[train_mask].reset_index(drop=True)
        test = frame.loc[test_mask].reset_index(drop=True)
        x_train = design_frame(train, features)
        x_test = design_frame(test, features)
        x_test = x_test.reindex(columns=x_train.columns, fill_value=0.0)
        continuous = [column for column in x_train.columns if not column.startswith("condition_")]
        scaler = StandardScaler().fit(x_train[continuous])
        x_train.loc[:, continuous] = scaler.transform(x_train[continuous])
        x_test.loc[:, continuous] = scaler.transform(x_test[continuous])
        model = LinearRegression()
        model.fit(x_train, train[TARGET])
        predictions[np.flatnonzero(test_mask)] = model.predict(x_test)
    if np.isnan(predictions).any():
        raise RuntimeError("Cross-validation produced missing predictions")
    truth = frame[TARGET].to_numpy(dtype=float)
    rmse = math.sqrt(mean_squared_error(truth, predictions))
    metrics = {
        "cv_r2": float(r2_score(truth, predictions)),
        "cv_rmse": float(rmse),
        "cv_nrmse": float(rmse / (truth.std(ddof=0) + 1e-12)),
        "cv_mae": float(mean_absolute_error(truth, predictions)),
    }
    return predictions, metrics


def evaluate_model(frame: pd.DataFrame, name: str, features: list[str]) -> ModelResult:
    fitted, _, _, _, _ = fit_standardized_ols(frame, features)
    _, metrics = cross_validated_predictions(frame, features)
    return ModelResult(
        name=name,
        features=features,
        n=len(frame),
        adjusted_r2=float(fitted.rsquared_adj),
        **metrics,
    )


def paired_cv_bootstrap(
    frame: pd.DataFrame,
    reference_predictions: np.ndarray,
    candidate_predictions: np.ndarray,
    resamples: int,
    seed: int = 20260711,
) -> dict[str, Any]:
    """Paired seed-cluster bootstrap of held-out prediction-metric differences."""
    rng = np.random.default_rng(seed)
    seed_ids = np.asarray(sorted(frame["seed"].unique()))
    truth_all = frame[TARGET].to_numpy(dtype=float)
    delta_r2 = []
    relative_nrmse = []
    for _ in range(resamples):
        sampled = rng.choice(seed_ids, size=len(seed_ids), replace=True)
        indices = np.concatenate(
            [np.flatnonzero(frame["seed"].to_numpy() == sampled_seed) for sampled_seed in sampled]
        )
        truth = truth_all[indices]
        reference = reference_predictions[indices]
        candidate = candidate_predictions[indices]
        if np.std(truth, ddof=0) <= 1e-12:
            continue
        reference_rmse = math.sqrt(mean_squared_error(truth, reference))
        candidate_rmse = math.sqrt(mean_squared_error(truth, candidate))
        delta_r2.append(r2_score(truth, candidate) - r2_score(truth, reference))
        relative_nrmse.append(
            (reference_rmse - candidate_rmse) / (reference_rmse + 1e-12)
        )
    if not delta_r2:
        raise RuntimeError("Paired CV bootstrap produced no valid resamples")
    return {
        "valid_resamples": len(delta_r2),
        "delta_cv_r2_interval": [
            float(np.quantile(delta_r2, 0.025)),
            float(np.quantile(delta_r2, 0.975)),
        ],
        "relative_nrmse_improvement_interval": [
            float(np.quantile(relative_nrmse, 0.025)),
            float(np.quantile(relative_nrmse, 0.975)),
        ],
    }


def cluster_bootstrap_beta(
    frame: pd.DataFrame,
    features: list[str],
    coefficient: str,
    resamples: int,
    seed: int = 20260710,
) -> np.ndarray:
    rng = np.random.default_rng(seed)
    seeds = np.asarray(sorted(frame["seed"].unique()))
    values = []
    for _ in range(resamples):
        sampled = rng.choice(seeds, size=len(seeds), replace=True)
        pieces = []
        for cluster_id, sampled_seed in enumerate(sampled):
            piece = frame[frame["seed"] == sampled_seed].copy()
            piece["bootstrap_cluster"] = cluster_id
            pieces.append(piece)
        boot = pd.concat(pieces, ignore_index=True)
        try:
            _, params, _, _, _ = fit_standardized_ols(boot, features)
            values.append(float(params[coefficient]))
        except Exception:
            continue
    return np.asarray(values, dtype=np.float64)


def leave_out_coefficients(frame: pd.DataFrame, features: list[str]) -> tuple[dict[str, float], dict[int, float]]:
    by_condition = {}
    for condition in sorted(frame["condition"].unique()):
        subset = frame[frame["condition"] != condition].reset_index(drop=True)
        try:
            _, params, _, _, _ = fit_standardized_ols(subset, features)
            by_condition[condition] = float(params["SR_preC"])
        except Exception:
            by_condition[condition] = float("nan")
    by_seed = {}
    for seed in sorted(frame["seed"].unique()):
        subset = frame[frame["seed"] != seed].reset_index(drop=True)
        try:
            _, params, _, _, _ = fit_standardized_ols(subset, features)
            by_seed[int(seed)] = float(params["SR_preC"])
        except Exception:
            by_seed[int(seed)] = float("nan")
    return by_condition, by_seed


def score_robustness(frame: pd.DataFrame) -> dict[str, Any]:
    correlations = {}
    coefficients = {}
    full = frame["SR_preC"].to_numpy(dtype=float)
    for component in COMPONENTS:
        remaining = [item for item in COMPONENTS if item != component]
        alternative = frame[remaining].mean(axis=1).to_numpy(dtype=float)
        correlations[component] = float(spearmanr(full, alternative).statistic)
        alternative_frame = frame.copy()
        alternative_frame["SR_preC"] = alternative
        try:
            _, params, _, _, _ = fit_standardized_ols(
                alternative_frame, M0_CONTINUOUS + ["SR_preC"]
            )
            coefficients[component] = float(params["SR_preC"])
        except Exception:
            coefficients[component] = float("nan")
    coefficient_values = np.asarray(list(coefficients.values()), dtype=float)
    return {
        "leave_one_component_out_spearman": correlations,
        "leave_one_component_out_coefficients": coefficients,
        "median_spearman": float(np.nanmedian(list(correlations.values()))),
        "positive_coefficients": int(np.sum(coefficient_values > 0)),
        "directionally_consistent": bool(
            np.sum(coefficient_values > 0) >= 4 and np.nanmedian(coefficient_values) > 0
        ),
    }


def _smd(a: np.ndarray, b: np.ndarray) -> float:
    pooled = math.sqrt((np.var(a, ddof=1) + np.var(b, ddof=1)) / 2.0 + 1e-12)
    return float((np.mean(a) - np.mean(b)) / pooled)


def run_matching(frame: pd.DataFrame, config: dict[str, Any]) -> tuple[pd.DataFrame, dict[str, Any]]:
    low_cut = frame["SR_preC"].quantile(1 / 3)
    high_cut = frame["SR_preC"].quantile(2 / 3)
    selected = frame[(frame["SR_preC"] <= low_cut) | (frame["SR_preC"] >= high_cut)].copy()
    selected["high_sr"] = (selected["SR_preC"] >= high_cut).astype(int)
    matching_features = M0_CONTINUOUS
    x = design_frame(selected, matching_features)
    scaler = StandardScaler().fit(x)
    x_scaled = scaler.transform(x)
    logistic = LogisticRegression(max_iter=2000, C=1e6).fit(x_scaled, selected["high_sr"])
    propensity = np.clip(logistic.predict_proba(x_scaled)[:, 1], 1e-6, 1 - 1e-6)
    selected["propensity_logit"] = np.log(propensity / (1 - propensity))
    caliper = float(config["matching"]["caliper_sd"]) * float(selected["propensity_logit"].std(ddof=1))
    high = selected[selected["high_sr"] == 1].sort_values("SR_preC", ascending=False)
    low = selected[selected["high_sr"] == 0].copy()
    available = set(low.index.tolist())
    pairs = []
    for high_index, high_row in high.iterrows():
        if not available:
            break
        candidates = low.loc[list(available)]
        distances = np.abs(candidates["propensity_logit"] - high_row["propensity_logit"])
        low_index = int(distances.idxmin())
        distance = float(distances.loc[low_index])
        if distance <= caliper:
            pairs.append(
                {
                    "pair_id": len(pairs),
                    "high_seed": int(high_row["seed"]),
                    "high_condition": high_row["condition"],
                    "low_seed": int(low.loc[low_index, "seed"]),
                    "low_condition": low.loc[low_index, "condition"],
                    "propensity_distance": distance,
                    "high_Q_C": float(high_row[TARGET]),
                    "low_Q_C": float(low.loc[low_index, TARGET]),
                    "Q_C_difference": float(high_row[TARGET] - low.loc[low_index, TARGET]),
                }
            )
            available.remove(low_index)
    pair_frame = pd.DataFrame(pairs)
    balance = {}
    valid_balance = False
    if pairs:
        high_indices = []
        low_indices = []
        for pair in pairs:
            high_indices.append(
                frame[(frame.seed == pair["high_seed"]) & (frame.condition == pair["high_condition"])].index[0]
            )
            low_indices.append(
                frame[(frame.seed == pair["low_seed"]) & (frame.condition == pair["low_condition"])].index[0]
            )
        for feature in M0_CONTINUOUS:
            balance[feature] = abs(
                _smd(frame.loc[high_indices, feature].to_numpy(), frame.loc[low_indices, feature].to_numpy())
            )
        dummy = _condition_dummies(frame)
        for column in dummy.columns:
            balance[column] = abs(
                _smd(dummy.loc[high_indices, column].to_numpy(), dummy.loc[low_indices, column].to_numpy())
            )
        valid_balance = all(
            value < float(config["matching"]["max_smd_continuous"])
            for key, value in balance.items()
            if not key.startswith("condition_")
        ) and all(
            value < float(config["matching"]["max_smd_condition"])
            for key, value in balance.items()
            if key.startswith("condition_")
        )
    difference_interval = None
    if len(pair_frame):
        rng = np.random.default_rng(20260711)
        differences = pair_frame["Q_C_difference"].to_numpy(dtype=float)
        boot_means = [
            float(np.mean(rng.choice(differences, size=len(differences), replace=True)))
            for _ in range(int(config.get("bootstrap_resamples", 2000)))
        ]
        difference_interval = [
            float(np.quantile(boot_means, 0.025)),
            float(np.quantile(boot_means, 0.975)),
        ]
    summary = {
        "pairs": len(pair_frame),
        "minimum_pairs": int(config["matching"]["min_pairs"]),
        "caliper": caliper,
        "balance_absolute_smd": balance,
        "balance_valid": valid_balance,
        "analysis_valid": len(pair_frame) >= int(config["matching"]["min_pairs"]) and valid_balance,
        "mean_Q_C_difference": float(pair_frame["Q_C_difference"].mean()) if len(pair_frame) else None,
        "paired_bootstrap_interval": difference_interval,
    }
    return pair_frame, summary


def classify_states(frame: pd.DataFrame, thresholds: dict[str, Any]) -> tuple[pd.Series, dict[str, Any]]:
    labels = []
    selective_threshold = float(thresholds["selective_incorporation_permutation_p95"])
    for _, row in frame.iterrows():
        condition_threshold = thresholds["condition_thresholds"][row["condition"]]
        opening = bool(
            row["d_repr_peak"] > condition_threshold["d_repr_peak"]
            or row["d_grad_peak"] > condition_threshold["d_grad_peak"]
        )
        stable = bool(
            row["v_late"] <= condition_threshold["v_late"]
            and abs(row["B_loss_slope_late"]) <= condition_threshold["abs_loss_slope"]
        )
        adequate = bool(
            row["a_B"] > thresholds["B_adequacy_gain"]
            and row["B_end_validation_accuracy"] > thresholds["B_adequacy_end_accuracy"]
        )
        selective = bool(row["S_B"] > selective_threshold)
        if not opening and not adequate:
            label = "rigidity"
        elif opening and stable and adequate and selective:
            label = "candidate_selective_resynchronization"
        elif opening and not (stable and adequate and selective):
            label = "disorganization_or_unresolved_opening"
        else:
            label = "endpoint_adaptation_unclassified"
        labels.append(label)
    series = pd.Series(labels, index=frame.index, name="preC_state")
    counts = series.value_counts().to_dict()
    agreement_values = []
    classified = frame[["seed", "condition"]].copy()
    classified["preC_state"] = series
    for held_out_seed in sorted(classified["seed"].unique()):
        training = classified[classified["seed"] != held_out_seed]
        held_out = classified[classified["seed"] == held_out_seed]
        modal_by_condition = (
            training.groupby("condition")["preC_state"]
            .agg(lambda values: sorted(values.mode().tolist())[0])
            .to_dict()
        )
        agreement_values.extend(
            row.preC_state == modal_by_condition.get(row.condition)
            for row in held_out.itertuples()
        )
    leave_seed_agreement = float(np.mean(agreement_values)) if agreement_values else float("nan")
    class_count_valid = len(counts) >= 2 and all(count >= 5 for count in counts.values())
    valid = class_count_valid and leave_seed_agreement >= 0.70
    reasons = []
    if not class_count_valid:
        reasons.append("class count below five or fewer than two classes")
    if leave_seed_agreement < 0.70:
        reasons.append("leave-one-seed modal-label agreement below 0.70")
    return series, {
        "counts": counts,
        "leave_one_seed_label_agreement": leave_seed_agreement,
        "figure_valid": valid,
        "reason": None if valid else "; ".join(reasons),
    }


def collate_locked_outputs(experiment_root: Path, config: dict[str, Any]) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    raw_root = experiment_root / config["output_root"]
    processed = experiment_root / "outputs" / "processed"
    processed.mkdir(parents=True, exist_ok=True)
    lock_manifest = json.loads(
        (experiment_root / "manifests" / "formal_lock_manifest.json").read_text(encoding="utf-8")
    )
    pre_records = []
    outcomes = []
    steps = []
    failures = []
    manifests = []
    for seed in config["seeds"]:
        for condition in config["conditions"]:
            run_dir = raw_root / f"seed_{seed}__condition_{condition}"
            failure_path = run_dir / "failure_record.json"
            if failure_path.exists():
                failures.append(json.loads(failure_path.read_text(encoding="utf-8")))
            if not (run_dir / "C_complete.json").exists():
                manifests.append(
                    {
                        "seed": seed,
                        "condition": condition,
                        "complete": False,
                        "git_sha": lock_manifest["git_sha"],
                        "config_sha256": lock_manifest["config_sha256"],
                        "code_tree_sha256": lock_manifest["code_tree_sha256"],
                    }
                )
                continue
            hash_record = verify_preC_files(run_dir)
            pre = json.loads((run_dir / "preC_features.json").read_text(encoding="utf-8"))
            outcome = json.loads((run_dir / "C_outcomes.json").read_text(encoding="utf-8"))
            if pre.get("uses_c_data") is not False:
                raise RuntimeError(f"Leakage flag invalid in {run_dir}")
            if outcome["preC_sha256"] != hash_record["sha256"]:
                raise RuntimeError(f"Outcome/pre-C hash mismatch in {run_dir}")
            if outcome["preC_created_utc"] >= outcome["C_started_utc"]:
                raise RuntimeError(f"Pre-C timestamp does not precede C in {run_dir}")
            pre_records.append(pre)
            outcomes.append(outcome)
            steps.append(pd.read_parquet(run_dir / "step_metrics.parquet"))
            runtime = json.loads((run_dir / "run_runtime.json").read_text())
            manifests.append(
                {
                    "seed": seed,
                    "condition": condition,
                    "complete": True,
                    "preC_sha256": hash_record["sha256"],
                    "wall_seconds": runtime["wall_seconds"],
                    "device": runtime["device"],
                    "git_sha": lock_manifest["git_sha"],
                    "config_sha256": lock_manifest["config_sha256"],
                    "code_tree_sha256": lock_manifest["code_tree_sha256"],
                }
            )
    pre_frame = pd.DataFrame(pre_records)
    outcome_frame = pd.DataFrame(outcomes)
    if len(pre_frame) != len(config["seeds"]) * len(config["conditions"]):
        raise RuntimeError(
            f"Locked cohort incomplete: {len(pre_frame)} complete of {len(config['seeds']) * len(config['conditions'])}"
        )
    merged = pre_frame.merge(outcome_frame, on=["seed", "condition"], validate="one_to_one")
    step_frame = pd.concat(steps, ignore_index=True)
    pd.DataFrame(manifests).to_csv(processed / "run_manifest.csv", index=False)
    step_frame.to_parquet(processed / "step_metrics.parquet", index=False)
    pre_frame.to_parquet(processed / "preC_features.parquet", index=False)
    outcome_frame.to_parquet(processed / "C_outcomes.parquet", index=False)
    pd.DataFrame(failures).to_csv(processed / "failed_runs.csv", index=False)
    phase_summary = (
        step_frame.sort_values(["seed", "condition", "phase", "phase_epoch"])
        .groupby(["seed", "condition", "phase"], as_index=False)
        .tail(1)
    )
    phase_summary.to_csv(processed / "phase_summary.csv", index=False)
    return merged, step_frame, pd.DataFrame(manifests)


def generate_figures(
    frame: pd.DataFrame,
    steps: pd.DataFrame,
    model_table: pd.DataFrame,
    output_root: Path,
    state_summary: dict[str, Any],
) -> None:
    output_root.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid")

    c_steps = steps[steps["phase"] == "C"].copy()
    plt.figure(figsize=(8, 5))
    sns.lineplot(
        data=c_steps,
        x="phase_epoch",
        y="C_changed_balanced_accuracy",
        hue="condition",
        errorbar=("ci", 95),
        marker="o",
    )
    plt.title("C-stage changed-class adaptation")
    plt.tight_layout()
    plt.savefig(output_root / "abc_learning_curves.png", dpi=180)
    plt.close()

    plt.figure(figsize=(7, 5))
    sns.regplot(data=frame, x="SR_preC", y=TARGET, scatter=False, color="black")
    sns.scatterplot(data=frame, x="SR_preC", y=TARGET, hue="condition", s=55)
    plt.title("A/B-only SR_preC and C-stage retained adaptability")
    plt.tight_layout()
    plt.savefig(output_root / "sr_prec_vs_qc.png", dpi=180)
    plt.close()

    x0 = design_frame(frame, M0_CONTINUOUS)
    y_resid = frame[TARGET] - LinearRegression().fit(x0, frame[TARGET]).predict(x0)
    sr_resid = frame["SR_preC"] - LinearRegression().fit(x0, frame["SR_preC"]).predict(x0)
    partial = pd.DataFrame({"SR_preC_residual": sr_resid, "Q_C_residual": y_resid, "condition": frame["condition"]})
    plt.figure(figsize=(7, 5))
    sns.regplot(data=partial, x="SR_preC_residual", y="Q_C_residual", scatter=False, color="black")
    sns.scatterplot(data=partial, x="SR_preC_residual", y="Q_C_residual", hue="condition", s=55)
    plt.title("Partial relationship after B-performance controls")
    plt.tight_layout()
    plt.savefig(output_root / "partial_sr_prec_qc.png", dpi=180)
    plt.close()

    melted = model_table.melt(id_vars="name", value_vars=["cv_r2", "cv_nrmse"])
    plt.figure(figsize=(9, 5))
    sns.barplot(data=melted, x="name", y="value", hue="variable")
    plt.xticks(rotation=25, ha="right")
    plt.title("Locked model comparison")
    plt.tight_layout()
    plt.savefig(output_root / "model_comparison.png", dpi=180)
    plt.close()

    plt.figure(figsize=(7, 5))
    sns.scatterplot(data=frame, x="fisher_burden_area", y=TARGET, hue="condition", s=55)
    plt.xscale("symlog", linthresh=1e-10)
    plt.title("Empirical-Fisher burden and Q_C")
    plt.tight_layout()
    plt.savefig(output_root / "fisher_vs_simple_baselines.png", dpi=180)
    plt.close()

    numeric = frame[
        ["SR_preC", TARGET, "B_end_validation_accuracy", "B_end_validation_loss"]
        + SIMPLE_FEATURES
        + ["fisher_burden_area"]
    ].corr(method="spearman")
    plt.figure(figsize=(11, 9))
    sns.heatmap(numeric, cmap="vlag", center=0, vmin=-1, vmax=1)
    plt.title("Spearman metric correlation matrix")
    plt.tight_layout()
    plt.savefig(output_root / "metric_correlation_matrix.png", dpi=180)
    plt.close()

    condition_effects = []
    for condition in sorted(frame["condition"].unique()):
        subset = frame[frame["condition"] == condition]
        if len(subset) >= 5:
            coefficient = np.polyfit(subset["SR_preC"], subset[TARGET], 1)[0]
            condition_effects.append({"condition": condition, "slope": coefficient})
    plt.figure(figsize=(7, 4))
    sns.barplot(data=pd.DataFrame(condition_effects), x="condition", y="slope")
    plt.axhline(0, color="black", linewidth=1)
    plt.title("Within-condition SR_preC slopes")
    plt.tight_layout()
    plt.savefig(output_root / "condition_effect_stability.png", dpi=180)
    plt.close()

    if state_summary.get("figure_valid"):
        plt.figure(figsize=(8, 5))
        sns.boxplot(data=frame, x="preC_state", y=TARGET)
        sns.stripplot(data=frame, x="preC_state", y=TARGET, color="black", alpha=0.6)
        plt.xticks(rotation=20, ha="right")
        plt.tight_layout()
        plt.savefig(output_root / "four_state_secondary.png", dpi=180)
        plt.close()


def analyze_locked(experiment_root: Path, config_path: Path) -> dict[str, Any]:
    config = load_yaml(config_path)
    frame, steps, manifest = collate_locked_outputs(experiment_root, config)
    processed = experiment_root / "outputs" / "processed"
    figures = experiment_root / "outputs" / "figures"
    frame = frame.replace([np.inf, -np.inf], np.nan)
    required = M0_CONTINUOUS + ["SR_preC", TARGET]
    if frame[required].isna().any().any():
        raise RuntimeError("Missing primary model data")

    model_specs = {
        "M0_performance": M0_CONTINUOUS,
        "M1_construct": M0_CONTINUOUS + ["SR_preC"],
        "M2_representation": M0_CONTINUOUS + ["representation_drift_area"],
        "M1_plus_representation": M0_CONTINUOUS + ["representation_drift_area", "SR_preC"],
        "M2_simple": M0_CONTINUOUS + SIMPLE_FEATURES,
        "M1_simple": M0_CONTINUOUS + SIMPLE_FEATURES + ["SR_preC"],
        "M3_fisher": M0_CONTINUOUS + SIMPLE_FEATURES + ["SR_preC", "fisher_burden_area"],
    }
    results = []
    predictions: dict[str, np.ndarray] = {}
    for name, features in model_specs.items():
        results.append(evaluate_model(frame, name, features).__dict__)
        predictions[name], _ = cross_validated_predictions(frame, features)
    model_table = pd.DataFrame(results)
    by_name = model_table.set_index("name")

    cv_bootstrap_by_model = {}
    for name in model_specs:
        if name == "M0_performance":
            continue
        comparison = paired_cv_bootstrap(
            frame,
            predictions["M0_performance"],
            predictions[name],
            resamples=int(config.get("bootstrap_resamples", 2000)),
        )
        cv_bootstrap_by_model[name] = comparison
        model_table.loc[model_table["name"] == name, "delta_cv_r2_vs_M0"] = float(
            by_name.loc[name].cv_r2 - by_name.loc["M0_performance"].cv_r2
        )
        model_table.loc[
            model_table["name"] == name, "relative_nrmse_improvement_vs_M0"
        ] = float(
            (by_name.loc["M0_performance"].cv_nrmse - by_name.loc[name].cv_nrmse)
            / (by_name.loc["M0_performance"].cv_nrmse + 1e-12)
        )
        model_table.loc[
            model_table["name"] == name, "delta_cv_r2_vs_M0_interval"
        ] = str(comparison["delta_cv_r2_interval"])
        model_table.loc[
            model_table["name"] == name, "relative_nrmse_improvement_vs_M0_interval"
        ] = str(comparison["relative_nrmse_improvement_interval"])
    model_table.to_csv(processed / "model_comparison.csv", index=False)

    fitted, params, ses, pvalues, intervals = fit_standardized_ols(frame, model_specs["M1_construct"])
    bootstrap = cluster_bootstrap_beta(
        frame,
        model_specs["M1_construct"],
        "SR_preC",
        resamples=int(config.get("bootstrap_resamples", 2000)),
    )
    bootstrap_interval = [float(np.quantile(bootstrap, 0.025)), float(np.quantile(bootstrap, 0.975))]
    by_condition, by_seed = leave_out_coefficients(frame, model_specs["M1_construct"])
    robustness = score_robustness(frame)
    pair_frame, matching = run_matching(frame, config)
    pair_frame.to_csv(processed / "matched_pairs.csv", index=False)

    thresholds_path = experiment_root / config["state_thresholds"]
    thresholds = json.loads(thresholds_path.read_text(encoding="utf-8"))
    states, state_summary = classify_states(frame, thresholds)
    frame["preC_state"] = states
    frame.to_csv(processed / "locked_analysis_frame.csv", index=False)

    m0 = by_name.loc["M0_performance"]
    m1 = by_name.loc["M1_construct"]
    m2r = by_name.loc["M2_representation"]
    m1r = by_name.loc["M1_plus_representation"]
    m1s = by_name.loc["M1_simple"]
    m3 = by_name.loc["M3_fisher"]
    delta_r2 = float(m1.cv_r2 - m0.cv_r2)
    nrmse_improvement = float((m0.cv_nrmse - m1.cv_nrmse) / (m0.cv_nrmse + 1e-12))
    construct_over_repr_r2 = float(m1.cv_r2 - m2r.cv_r2)
    construct_over_repr_nrmse = float((m2r.cv_nrmse - m1.cv_nrmse) / (m2r.cv_nrmse + 1e-12))
    sr_increment_to_repr = float(m1r.cv_r2 - m2r.cv_r2)
    fisher_delta_r2 = float(m3.cv_r2 - m1s.cv_r2)
    fisher_nrmse_improvement = float((m1s.cv_nrmse - m3.cv_nrmse) / (m1s.cv_nrmse + 1e-12))

    primary_cv_interval = cv_bootstrap_by_model["M1_construct"]
    representation_cv_interval = paired_cv_bootstrap(
        frame,
        predictions["M2_representation"],
        predictions["M1_construct"],
        resamples=int(config.get("bootstrap_resamples", 2000)),
        seed=20260712,
    )
    fisher_cv_interval = paired_cv_bootstrap(
        frame,
        predictions["M1_simple"],
        predictions["M3_fisher"],
        resamples=int(config.get("bootstrap_resamples", 2000)),
        seed=20260713,
    )

    _, fisher_params, _, _, fisher_intervals = fit_standardized_ols(
        frame, model_specs["M3_fisher"]
    )
    fisher_interval = fisher_intervals["fisher_burden_area"]
    fisher_bootstrap = cluster_bootstrap_beta(
        frame,
        model_specs["M3_fisher"],
        "fisher_burden_area",
        resamples=int(config.get("bootstrap_resamples", 2000)),
        seed=20260714,
    )
    fisher_bootstrap_interval = [
        float(np.quantile(fisher_bootstrap, 0.025)),
        float(np.quantile(fisher_bootstrap, 0.975)),
    ]
    fisher_kl_spearman = float(
        spearmanr(frame["fisher_burden_area"], frame["predictive_KL_area"]).statistic
    )
    simple_delta_r2 = float(m1s.cv_r2 - m1.cv_r2)
    simple_nrmse_improvement = float(
        (m1.cv_nrmse - m1s.cv_nrmse) / (m1.cv_nrmse + 1e-12)
    )
    if (
        fisher_delta_r2 >= 0.05
        and fisher_nrmse_improvement >= 0.05
        and fisher_bootstrap_interval[0] > 0
        and np.isfinite(fisher_kl_spearman)
        and fisher_kl_spearman >= 0
    ):
        fisher_status = "win"
    elif (
        fisher_cv_interval["delta_cv_r2_interval"][1] < 0
        and fisher_cv_interval["relative_nrmse_improvement_interval"][1] < 0
    ) or (
        simple_delta_r2 >= 0.05
        and simple_nrmse_improvement >= 0.05
        and (fisher_delta_r2 < 0.05 or fisher_nrmse_improvement < 0.05)
    ):
        fisher_status = "lose"
    elif (
        fisher_cv_interval["delta_cv_r2_interval"][0] >= -0.01
        and fisher_cv_interval["delta_cv_r2_interval"][1] <= 0.01
        and fisher_cv_interval["relative_nrmse_improvement_interval"][0] >= -0.02
        and fisher_cv_interval["relative_nrmse_improvement_interval"][1] <= 0.02
    ):
        fisher_status = "tie"
    else:
        fisher_status = "inconclusive"

    condition_values = np.asarray(list(by_condition.values()), dtype=float)
    seed_values = np.asarray(list(by_seed.values()), dtype=float)
    within_condition_slopes = {}
    for condition in sorted(frame["condition"].unique()):
        subset = frame[frame["condition"] == condition]
        if subset["SR_preC"].std(ddof=0) <= 1e-12:
            within_condition_slopes[condition] = float("nan")
        else:
            within_condition_slopes[condition] = float(
                np.polyfit(subset["SR_preC"], subset[TARGET], 1)[0]
            )
    within_condition_values = np.asarray(list(within_condition_slopes.values()), dtype=float)
    go_checks = {
        "positive_beta_bootstrap_excludes_zero": bool(params["SR_preC"] > 0 and bootstrap_interval[0] > 0),
        "cv_increment_meets_threshold": bool(delta_r2 >= 0.05 and nrmse_improvement >= 0.05),
        "beats_representation_baseline": bool(
            construct_over_repr_r2 >= 0.05 or construct_over_repr_nrmse >= 0.05
        ),
        "leave_condition_stable": bool(
            np.sum(condition_values > 0) >= 3 and np.nanmin(condition_values) > -0.10
        ),
        "one_robustness_consistent": bool(
            matching["analysis_valid"] and (matching["mean_Q_C_difference"] or 0) > 0
            or robustness["directionally_consistent"]
        ),
        "no_seed_sign_flip": bool(np.nanmin(seed_values) > 0),
        "score_robustness": bool(robustness["median_spearman"] >= 0.70),
        "leakage_valid": True,
    }

    no_go_reasons = []
    combined_robustness = np.concatenate([condition_values, seed_values])
    if params["SR_preC"] <= 0 and np.sum(combined_robustness <= 0) >= 2:
        no_go_reasons.append("non_positive_increment_and_condition_instability")
    if delta_r2 <= 0 and nrmse_improvement <= 0:
        no_go_reasons.append("no_cross_validated_increment")
    if m0.cv_r2 >= 0.90 and delta_r2 < 0.01:
        no_go_reasons.append("B_performance_nearly_fully_predicts_Q_C")
    if m2r.cv_r2 >= m1.cv_r2 and m2r.cv_nrmse <= m1.cv_nrmse and sr_increment_to_repr < 0.01:
        no_go_reasons.append("representation_drift_replaces_construct")
    if robustness["median_spearman"] < 0.50:
        no_go_reasons.append("score_weight_instability")
    if robustness["positive_coefficients"] <= 2:
        no_go_reasons.append("leave_one_component_direction_flips")
    if params["SR_preC"] > 0 and np.sum(within_condition_values > 0) <= 1:
        no_go_reasons.append("effect_confined_to_one_condition_or_none")

    if all(go_checks.values()):
        decision = "GO"
    elif no_go_reasons:
        decision = "NO-GO"
    else:
        decision = "CONDITIONAL GO"

    analysis = {
        "created_utc": utc_now(),
        "n_runs": len(frame),
        "n_seeds": int(frame["seed"].nunique()),
        "primary_beta_standardized": float(params["SR_preC"]),
        "primary_beta_hc3_se": float(ses["SR_preC"]),
        "primary_beta_hc3_p": float(pvalues["SR_preC"]),
        "primary_beta_hc3_interval": intervals["SR_preC"],
        "primary_beta_seed_bootstrap_interval": bootstrap_interval,
        "delta_cv_r2_M1_vs_M0": delta_r2,
        "relative_nrmse_improvement_M1_vs_M0": nrmse_improvement,
        "primary_cv_bootstrap_intervals": primary_cv_interval,
        "delta_cv_r2_M1_vs_representation": construct_over_repr_r2,
        "relative_nrmse_improvement_M1_vs_representation": construct_over_repr_nrmse,
        "representation_comparison_cv_bootstrap_intervals": representation_cv_interval,
        "SR_increment_to_representation_cv_r2": sr_increment_to_repr,
        "leave_one_condition_coefficients": by_condition,
        "leave_one_seed_coefficients": by_seed,
        "within_condition_slopes": within_condition_slopes,
        "score_robustness": robustness,
        "matching": matching,
        "state_classification": state_summary,
        "fisher": {
            "status": fisher_status,
            "standardized_coefficient": float(fisher_params["fisher_burden_area"]),
            "coefficient_interval": fisher_interval,
            "coefficient_seed_bootstrap_interval": fisher_bootstrap_interval,
            "delta_cv_r2": fisher_delta_r2,
            "relative_nrmse_improvement": fisher_nrmse_improvement,
            "cv_bootstrap_intervals": fisher_cv_interval,
            "fisher_KL_spearman": fisher_kl_spearman,
        },
        "go_checks": go_checks,
        "no_go_reasons": no_go_reasons,
        "decision": decision,
        "model_table": results,
        "model_cv_bootstrap_intervals_vs_M0": cv_bootstrap_by_model,
    }
    write_json(processed / "confirmatory_results.json", analysis)
    write_json(processed / "robustness_checks.json", {
        "leave_one_condition": by_condition,
        "leave_one_seed": by_seed,
        "score": robustness,
        "matching": matching,
        "states": state_summary,
    })
    generate_figures(frame, steps, model_table, figures, state_summary)
    return analysis
