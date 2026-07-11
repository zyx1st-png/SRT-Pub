from __future__ import annotations

import numpy as np
import pandas as pd

from src.analysis import (
    COMPONENTS,
    M0_CONTINUOUS,
    SIMPLE_FEATURES,
    TARGET,
    evaluate_model,
    fit_standardized_ols,
    paired_cv_bootstrap,
    cross_validated_predictions,
    run_matching,
    score_robustness,
)


def _synthetic_locked_frame() -> pd.DataFrame:
    rng = np.random.default_rng(20260711)
    conditions = ["constrained", "standard", "high_update", "replay"]
    rows = []
    for seed in range(2001, 2011):
        for condition_index, condition in enumerate(conditions):
            sr = rng.normal() + 0.15 * condition_index
            b_accuracy = 0.75 + 0.03 * rng.normal()
            row = {
                "seed": seed,
                "condition": condition,
                "SR_preC": sr,
                "B_end_validation_accuracy": b_accuracy,
                "B_end_validation_loss": 0.8 - b_accuracy + 0.02 * rng.normal(),
                "A_end_validation_accuracy": 0.82 + 0.02 * rng.normal(),
                TARGET: 0.12 * sr + 0.20 * b_accuracy + 0.03 * rng.normal(),
            }
            for component in COMPONENTS:
                row[component] = sr + 0.20 * rng.normal()
            for feature in SIMPLE_FEATURES + ["fisher_burden_area"]:
                row[feature] = abs(rng.normal())
            rows.append(row)
    return pd.DataFrame(rows)


def test_locked_analysis_primitives_execute_on_synthetic_data() -> None:
    frame = _synthetic_locked_frame()
    features = M0_CONTINUOUS + ["SR_preC"]
    fitted, params, _, _, intervals = fit_standardized_ols(frame, features)
    result = evaluate_model(frame, "synthetic_M1", features)
    reference_predictions, _ = cross_validated_predictions(frame, M0_CONTINUOUS)
    candidate_predictions, _ = cross_validated_predictions(frame, features)
    cv_interval = paired_cv_bootstrap(
        frame,
        reference_predictions,
        candidate_predictions,
        resamples=100,
    )
    pairs, matching = run_matching(
        frame,
        {
            "matching": {
                "caliper_sd": 0.25,
                "min_pairs": 8,
                "max_smd_continuous": 0.10,
                "max_smd_condition": 0.20,
            }
        },
    )
    robustness = score_robustness(frame)

    assert np.isfinite(fitted.rsquared_adj)
    assert np.isfinite(params["SR_preC"])
    assert len(intervals["SR_preC"]) == 2
    assert np.isfinite(result.cv_rmse)
    assert cv_interval["valid_resamples"] == 100
    assert len(cv_interval["delta_cv_r2_interval"]) == 2
    assert set(pairs.columns).issubset(
        {
            "pair_id",
            "high_seed",
            "high_condition",
            "low_seed",
            "low_condition",
            "propensity_distance",
            "high_Q_C",
            "low_Q_C",
            "Q_C_difference",
        }
    )
    assert matching["pairs"] == len(pairs)
    assert np.isfinite(robustness["median_spearman"])
