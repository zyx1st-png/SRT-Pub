from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.stats import pearsonr, spearmanr
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler


TARGET = "Q_C_changed_AULC_gain"
CONDITIONS = ["constrained", "standard", "high_update", "replay"]
B_PERFORMANCE = ["B_end_validation_accuracy", "B_end_validation_loss"]
B_INTERNAL_STATE = [
    "B_end_predictive_entropy",
    "B_end_representation_coherence",
    "B_end_gradient_disagreement",
    "B_end_probe_gradient_norm",
    "B_end_parameter_distance",
    "B_end_representation_drift",
]


def load_v1_frame(repo_root: Path) -> pd.DataFrame:
    processed = repo_root / "Experiments" / "selective_resynchronization_mvp" / "outputs" / "processed"
    pre = pd.read_parquet(processed / "preC_features.parquet")
    outcomes = pd.read_parquet(processed / "C_outcomes.parquet")
    phase = pd.read_csv(processed / "phase_summary.csv")
    b_end = phase[phase["phase"] == "B"].copy()
    b_end = b_end.rename(
        columns={
            "predictive_entropy": "B_end_predictive_entropy",
            "representation_coherence": "B_end_representation_coherence",
            "gradient_disagreement": "B_end_gradient_disagreement",
            "probe_gradient_norm": "B_end_probe_gradient_norm",
            "parameter_distance_from_phase_start": "B_end_parameter_distance",
            "representation_drift_from_A": "B_end_representation_drift",
        }
    )
    endpoint_columns = ["seed", "condition"] + B_INTERNAL_STATE
    frame = pre.merge(outcomes, on=["seed", "condition"], validate="one_to_one")
    frame = frame.merge(b_end[endpoint_columns], on=["seed", "condition"], validate="one_to_one")
    frame["C_mean_changed_balanced_accuracy"] = (
        frame[TARGET] + frame["C0_changed_balanced_accuracy"]
    )
    frame["C0_changed_headroom"] = 1.0 - frame["C0_changed_balanced_accuracy"]
    return frame.sort_values(["seed", "condition"]).reset_index(drop=True)


def _condition_dummies(frame: pd.DataFrame) -> pd.DataFrame:
    categorical = pd.Categorical(frame["condition"], categories=CONDITIONS)
    return pd.get_dummies(categorical, prefix="condition", drop_first=True, dtype=float)


def _fit_predict(
    train: pd.DataFrame,
    test: pd.DataFrame,
    continuous: list[str],
    include_condition: bool,
    target: str = TARGET,
) -> np.ndarray:
    x_train = train[continuous].astype(float).reset_index(drop=True) if continuous else pd.DataFrame(index=range(len(train)))
    x_test = test[continuous].astype(float).reset_index(drop=True) if continuous else pd.DataFrame(index=range(len(test)))
    if continuous:
        scaler = StandardScaler().fit(x_train)
        x_train.loc[:, continuous] = scaler.transform(x_train)
        x_test.loc[:, continuous] = scaler.transform(x_test)
    if include_condition:
        x_train = pd.concat([x_train, _condition_dummies(train).reset_index(drop=True)], axis=1)
        x_test = pd.concat([x_test, _condition_dummies(test).reset_index(drop=True)], axis=1)
    if x_train.shape[1] == 0:
        x_train = pd.DataFrame({"intercept_feature": np.zeros(len(train))})
        x_test = pd.DataFrame({"intercept_feature": np.zeros(len(test))})
    model = LinearRegression().fit(x_train, train[target].to_numpy(dtype=float))
    return model.predict(x_test)


def _cv_metrics(
    frame: pd.DataFrame,
    continuous: list[str],
    include_condition: bool,
    splits: list[tuple[np.ndarray, np.ndarray]],
    target: str = TARGET,
) -> dict[str, float]:
    predictions = np.full(len(frame), np.nan, dtype=float)
    for train_index, test_index in splits:
        predictions[test_index] = _fit_predict(
            frame.iloc[train_index].reset_index(drop=True),
            frame.iloc[test_index].reset_index(drop=True),
            continuous,
            include_condition,
            target=target,
        )
    if np.isnan(predictions).any():
        raise RuntimeError("Diagnostic CV produced missing predictions")
    truth = frame[target].to_numpy(dtype=float)
    rmse = math.sqrt(mean_squared_error(truth, predictions))
    return {
        "r2": float(r2_score(truth, predictions)),
        "rmse": float(rmse),
        "nrmse": float(rmse / (truth.std(ddof=0) + 1e-12)),
    }


def _group_splits(frame: pd.DataFrame, group: str) -> list[tuple[np.ndarray, np.ndarray]]:
    values = frame[group].to_numpy()
    return [
        (np.flatnonzero(values != held_out), np.flatnonzero(values == held_out))
        for held_out in sorted(frame[group].unique())
    ]


def model_decomposition(frame: pd.DataFrame) -> pd.DataFrame:
    models: dict[str, tuple[list[str], bool]] = {
        "condition_only": ([], True),
        "B_accuracy_loss_only": (B_PERFORMANCE, False),
        "B_internal_state_only": (B_INTERNAL_STATE, False),
        "condition_plus_B_accuracy_loss": (B_PERFORMANCE, True),
        "condition_plus_complete_B_state": (B_PERFORMANCE + B_INTERNAL_STATE, True),
        "complete_locked_M0": (B_PERFORMANCE + ["A_end_validation_accuracy"], True),
    }
    ordinary = list(KFold(n_splits=5, shuffle=True, random_state=20260712).split(frame))
    leave_condition = _group_splits(frame, "condition")
    leave_seed = _group_splits(frame, "seed")
    records = []
    for name, (continuous, include_condition) in models.items():
        metrics = {
            "ordinary_5fold": _cv_metrics(frame, continuous, include_condition, ordinary),
            "leave_one_condition_out": _cv_metrics(
                frame, continuous, include_condition, leave_condition
            ),
            "leave_one_seed_out": _cv_metrics(frame, continuous, include_condition, leave_seed),
        }
        pooled_truth = []
        pooled_prediction = []
        within_r2 = {}
        for condition in CONDITIONS:
            subset = frame[frame["condition"] == condition].reset_index(drop=True)
            splits = _group_splits(subset, "seed")
            within = _cv_metrics(subset, continuous, False, splits)
            within_r2[condition] = within["r2"]
            predictions = np.full(len(subset), np.nan)
            for train_index, test_index in splits:
                predictions[test_index] = _fit_predict(
                    subset.iloc[train_index].reset_index(drop=True),
                    subset.iloc[test_index].reset_index(drop=True),
                    continuous,
                    False,
                )
            pooled_truth.extend(subset[TARGET].tolist())
            pooled_prediction.extend(predictions.tolist())
        records.append(
            {
                "model": name,
                "continuous_features": continuous,
                "includes_condition": include_condition,
                "ordinary_cv_r2": metrics["ordinary_5fold"]["r2"],
                "leave_one_condition_out_cv_r2": metrics["leave_one_condition_out"]["r2"],
                "leave_one_seed_out_cv_r2": metrics["leave_one_seed_out"]["r2"],
                "within_condition_pooled_r2": float(
                    r2_score(np.asarray(pooled_truth), np.asarray(pooled_prediction))
                ),
                "within_condition_r2": within_r2,
            }
        )
    return pd.DataFrame(records)


def _safe_corr(x: pd.Series, y: pd.Series, method: str) -> float:
    if x.std(ddof=0) <= 1e-12 or y.std(ddof=0) <= 1e-12:
        return float("nan")
    if method == "pearson":
        return float(pearsonr(x, y).statistic)
    return float(spearmanr(x, y).statistic)


def variance_diagnostic(frame: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    variables = [
        "SR_preC",
        TARGET,
        "B_end_validation_accuracy",
        "B_end_validation_loss",
    ]
    condition_records = []
    for condition in CONDITIONS:
        subset = frame[frame["condition"] == condition]
        record: dict[str, Any] = {"condition": condition, "n": len(subset)}
        for variable in variables:
            record[f"var__{variable}"] = float(subset[variable].var(ddof=1))
        record["corr_SR_Q_pearson"] = _safe_corr(subset["SR_preC"], subset[TARGET], "pearson")
        record["corr_B_accuracy_Q_pearson"] = _safe_corr(
            subset["B_end_validation_accuracy"], subset[TARGET], "pearson"
        )
        record["corr_B_loss_Q_pearson"] = _safe_corr(
            subset["B_end_validation_loss"], subset[TARGET], "pearson"
        )
        condition_records.append(record)

    decomposition = []
    for variable in variables:
        grand = frame[variable].mean()
        between_ss = 0.0
        within_ss = 0.0
        within_variances = []
        condition_means = []
        for condition in CONDITIONS:
            values = frame.loc[frame["condition"] == condition, variable]
            between_ss += len(values) * float((values.mean() - grand) ** 2)
            within_ss += float(np.sum((values - values.mean()) ** 2))
            within_variances.append(float(values.var(ddof=1)))
            condition_means.append(float(values.mean()))
        total_ss = between_ss + within_ss
        decomposition.append(
            {
                "variable": variable,
                "between_ss_fraction": float(between_ss / (total_ss + 1e-12)),
                "between_to_within_ss": float(between_ss / (within_ss + 1e-12)),
                "variance_of_condition_means": float(np.var(condition_means, ddof=1)),
                "mean_within_condition_variance": float(np.mean(within_variances)),
                "between_to_within_variance_ratio": float(
                    np.var(condition_means, ddof=1) / (np.mean(within_variances) + 1e-12)
                ),
            }
        )
    return pd.DataFrame(condition_records), pd.DataFrame(decomposition)


def _incremental_standardized_beta(frame: pd.DataFrame, feature: str) -> tuple[float, list[float]]:
    continuous = B_PERFORMANCE + ["A_end_validation_accuracy", feature]
    x = frame[continuous].astype(float).copy()
    x.loc[:, continuous] = StandardScaler().fit_transform(x)
    x = pd.concat([x.reset_index(drop=True), _condition_dummies(frame).reset_index(drop=True)], axis=1)
    x = sm.add_constant(x, has_constant="add")
    y = frame[TARGET].to_numpy(dtype=float)
    y = (y - y.mean()) / (y.std(ddof=0) + 1e-12)
    fitted = sm.OLS(y, x).fit().get_robustcov_results(cov_type="HC3")
    names = list(x.columns)
    index = names.index(feature)
    interval = fitted.conf_int()[index]
    return float(fitted.params[index]), [float(interval[0]), float(interval[1])]


def component_diagnostic(frame: pd.DataFrame) -> pd.DataFrame:
    candidates = [
        "opening_dimension",
        "stabilization_dimension",
        "adaptation_dimension",
        "nonrollback_dimension",
        "incorporation_dimension",
        "d_repr_peak",
        "d_grad_peak",
        "r_grad",
        "v_late",
        "B_loss_slope_late",
        "representation_drift_area",
        "gradient_norm_area",
        "update_norm_area",
        "parameter_distance_B_end",
        "predictive_KL_area",
        "loss_change_area",
        "fisher_burden_area",
    ]
    centered_target = frame[TARGET] - frame.groupby("condition")[TARGET].transform("mean")
    records = []
    for feature in candidates:
        centered_feature = frame[feature] - frame.groupby("condition")[feature].transform("mean")
        beta, interval = _incremental_standardized_beta(frame, feature)
        records.append(
            {
                "feature": feature,
                "pearson_raw": _safe_corr(frame[feature], frame[TARGET], "pearson"),
                "spearman_raw": _safe_corr(frame[feature], frame[TARGET], "spearman"),
                "pearson_within_condition_centered": _safe_corr(
                    centered_feature, centered_target, "pearson"
                ),
                "incremental_beta_after_locked_M0": beta,
                "incremental_beta_hc3_interval": interval,
            }
        )
    return pd.DataFrame(records)


def coupling_diagnostic(frame: pd.DataFrame) -> dict[str, Any]:
    variables = [
        "B_end_validation_accuracy",
        "B_end_validation_loss",
        "C0_changed_balanced_accuracy",
        "C0_changed_headroom",
        "C_mean_changed_balanced_accuracy",
    ]
    correlations = {
        variable: {
            "pearson_with_Q": _safe_corr(frame[variable], frame[TARGET], "pearson"),
            "spearman_with_Q": _safe_corr(frame[variable], frame[TARGET], "spearman"),
        }
        for variable in variables
    }
    return {
        "definition": "Q_C = mean_e[BA_changed(C_e)] - BA_changed(C_0)",
        "direct_B_accuracy_term": False,
        "direct_B_loss_term": False,
        "direct_C0_term": True,
        "B_budget_constant": bool(frame["B_budget_updates"].nunique() == 1),
        "B_budget_updates_unique": sorted(frame["B_budget_updates"].unique().tolist()),
        "C_optimizer_inherited_from_B_condition": True,
        "correlations": correlations,
        "condition_means": frame.groupby("condition")[[TARGET, "C0_changed_balanced_accuracy", "C_mean_changed_balanced_accuracy", "B_end_validation_accuracy", "B_end_validation_loss"]].mean().to_dict(orient="index"),
    }


def run_diagnostic(repo_root: Path, output_root: Path) -> dict[str, Any]:
    output_root.mkdir(parents=True, exist_ok=True)
    frame = load_v1_frame(repo_root)
    models = model_decomposition(frame)
    by_condition, variance = variance_diagnostic(frame)
    components = component_diagnostic(frame)
    coupling = coupling_diagnostic(frame)
    models.to_csv(output_root / "v1_m0_decomposition.csv", index=False)
    by_condition.to_csv(output_root / "v1_within_condition_variance.csv", index=False)
    variance.to_csv(output_root / "v1_variance_decomposition.csv", index=False)
    components.to_csv(output_root / "v1_component_diagnostic.csv", index=False)
    frame.to_parquet(output_root / "v1_diagnostic_frame.parquet", index=False)
    payload = {
        "n": len(frame),
        "models": models.to_dict(orient="records"),
        "coupling": coupling,
        "variance_decomposition": variance.to_dict(orient="records"),
        "condition_diagnostics": by_condition.to_dict(orient="records"),
        "component_diagnostics": components.to_dict(orient="records"),
        "v1_decision_changed": False,
    }
    (output_root / "v1_failure_diagnostic.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return payload
