from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
sys.path.insert(0, str(ROOT))

from src.analysis import analyze_locked  # noqa: E402
from src.utils import load_yaml, sha256_file, utc_now  # noqa: E402


def fmt(value, digits=4):
    if value is None:
        return "not available"
    return f"{value:.{digits}f}" if isinstance(value, (int, float)) else str(value)


def write_reports(analysis: dict) -> None:
    config = load_yaml(ROOT / "configs" / "mvp_locked.yaml")
    manifest = json.loads((ROOT / "manifests" / "formal_lock_manifest.json").read_text())
    processed = ROOT / "outputs" / "processed"
    paper_root = REPO / "papers" / "selective_resynchronization"
    implementation = f"""---
id: PAPER-SELECTIVE-RESYNCHRONIZATION-MVP-IMPLEMENTATION-20260711
type: implementation_report
status: completed_mvp_v1
canonical: false
created: 2026-07-11
---

# Fashion-MNIST MVP Implementation Report

## Scope

This report documents implementation and execution only. The experiment tests a P4 domain-level proxy prediction and does not test SRT ontology.

## Implemented structure

- deterministic Fashion-MNIST `A -> B -> C` pipeline;
- separate 50,000/8,000/2,000/10,000 train/validation/probe/test partitions;
- light CNN with a 64-dimensional penultimate representation;
- constrained, standard, high-update, and replay paths;
- A/B-only pre-C schema and read-only hash freeze before C;
- epoch-level loss, accuracy, entropy, gradient, parameter, KL, representation, coherence, and diagonal empirical-Fisher metrics;
- regression-control, matching, simple-baseline, Fisher-increment, seed/condition robustness, and secondary state analyses.

## Locked protocol

- seeds: `{config['seeds']}` in every condition;
- A/B/C epochs: `{config['epochs']}`;
- primary predictor: equal-weight five-dimensional `SR_preC` from `06_mvp_spec_lock.md`;
- primary outcome: changed-class C AULC gain over eight epochs;
- configuration SHA-256: `{manifest['config_sha256']}`;
- specification SHA-256: `{manifest['spec_sha256']}`;
- code-tree SHA-256: `{manifest['code_tree_sha256']}`;
- Git commit at lock: `{manifest['git_sha']}`.

## Leakage and immutability checks

All {analysis['n_runs']} completed runs passed pre-C file hash and timestamp verification before analysis. `preC_features` records carried `uses_c_data: false`; C outcomes stored and matched the frozen pre-C SHA-256.

## Deviations

The pre-formal implementation clarification in `06_mvp_spec_lock.md` made bootstrap, state-stability, and Fisher decision computations executable before the formal manifest was created. It did not change `SR_preC`, `Q_C`, windows, weights, conditions, seeds, or effect thresholds. No outcome-dependent change was permitted. Any runtime deviations or failed runs are recorded in `outputs/processed/failed_runs.csv` and the run logs.

## Software and numerical checks

- nine automated tests passed before formal locking, including C-schema rejection, frozen-artifact mutation detection, phase separation, deterministic shifts, reproducibility, metric shapes, Fisher non-negativity, and a synthetic analysis-path test;
- smoke and three-seed pilot flows completed before the formal cohort;
- pilot standardization and no-shift state calibration were produced from A/B-only artifacts before formal C execution.

## Known limitations

- Fashion-MNIST is a mechanism gate, not evidence of generality.
- The C shift can be solved partly in the output head.
- The empirical Fisher is diagonal and based on 20 fixed examples.
- Four-state classification is secondary and may be invalid due to sparse classes.
- Forty trajectories limit precision for multi-predictor comparisons.
"""
    results = f"""---
id: PAPER-SELECTIVE-RESYNCHRONIZATION-MVP-RESULTS-20260711
type: empirical_results
status: completed_mvp_v1
canonical: false
created: 2026-07-11
---

# Fashion-MNIST MVP Results

## Primary result

The locked cohort contained **{analysis['n_runs']} runs across {analysis['n_seeds']} paired seeds**.

- standardized `SR_preC` coefficient: `{fmt(analysis['primary_beta_standardized'])}`;
- HC3 95% interval: `{analysis['primary_beta_hc3_interval']}`;
- seed-cluster bootstrap 95% interval: `{analysis['primary_beta_seed_bootstrap_interval']}`;
- HC3 p-value: `{fmt(analysis['primary_beta_hc3_p'])}`;
- incremental leave-one-seed-out CV R-squared over B-performance controls: `{fmt(analysis['delta_cv_r2_M1_vs_M0'])}`;
- relative NRMSE improvement: `{fmt(analysis['relative_nrmse_improvement_M1_vs_M0'])}`;
- paired seed-bootstrap CV intervals: `{analysis['primary_cv_bootstrap_intervals']}`.

These quantities are reported as effect size, uncertainty, and predictive increment. Statistical significance alone does not determine the decision.

## Simple-baseline comparison

- `SR_preC` minus representation-only CV R-squared: `{fmt(analysis['delta_cv_r2_M1_vs_representation'])}`;
- relative NRMSE improvement over representation-only: `{fmt(analysis['relative_nrmse_improvement_M1_vs_representation'])}`;
- incremental CV R-squared when `SR_preC` is added to representation drift: `{fmt(analysis['SR_increment_to_representation_cv_r2'])}`.

## Cross-condition and score robustness

- leave-one-condition coefficients: `{analysis['leave_one_condition_coefficients']}`;
- leave-one-component-out median Spearman stability: `{fmt(analysis['score_robustness']['median_spearman'])}`;
- secondary matching: `{analysis['matching']}`.

## Fisher result

- status: **{analysis['fisher']['status']}**;
- standardized coefficient: `{fmt(analysis['fisher']['standardized_coefficient'])}`;
- coefficient interval: `{analysis['fisher']['coefficient_interval']}`;
- incremental CV R-squared beyond construct and simple baselines: `{fmt(analysis['fisher']['delta_cv_r2'])}`;
- relative NRMSE improvement: `{fmt(analysis['fisher']['relative_nrmse_improvement'])}`;
- seed-bootstrap coefficient interval: `{analysis['fisher']['coefficient_seed_bootstrap_interval']}`;
- paired CV intervals: `{analysis['fisher']['cv_bootstrap_intervals']}`;
- Fisher-area/predictive-KL-area Spearman sanity relation: `{fmt(analysis['fisher']['fisher_KL_spearman'])}`.

This is a result about one diagonal empirical-Fisher predictor. It is separate from the construct result and is not an estimate of `Psi_f`.

## Four-state analysis

`{analysis['state_classification']}`

State results are reported visually only if the locked class-count criterion was met.

## Nulls, failures, and uncertainty

- GO checks: `{analysis['go_checks']}`;
- NO-GO triggers: `{analysis['no_go_reasons']}`;
- failed-run table: `experiments/selective_resynchronization_mvp/outputs/processed/failed_runs.csv`.

No Fashion-MNIST result is generalized to consciousness, ontology, or SRT as a whole.
"""
    decision = analysis["decision"]
    enter_cifar = "yes" if decision == "GO" else "no pending human review"
    term = "retain provisionally" if decision == "GO" else ("retain only conditionally" if decision == "CONDITIONAL GO" else "withdraw or reframe")
    state_keep = "retain" if analysis["state_classification"].get("figure_valid") else "downgrade/remove"
    fisher_keep = "retain as candidate" if analysis["fisher"]["status"] == "win" else "do not privilege"
    decision_doc = f"""---
id: PAPER-SELECTIVE-RESYNCHRONIZATION-MVP-DECISION-20260711
type: empirical_gate_decision
status: final_mvp_gate_v1
canonical: false
created: 2026-07-11
---

# Fashion-MNIST MVP Decision

## Decision: {decision}

This decision applies only to the locked MVP and follows the criteria in `06_mvp_spec_lock.md`.

## Criterion audit

- GO checks: `{analysis['go_checks']}`;
- NO-GO reasons: `{analysis['no_go_reasons']}`;
- Fisher status: `{analysis['fisher']['status']}`;
- state-classification status: `{analysis['state_classification']}`.

## Consequences

- enter CIFAR-10 now: **{enter_cifar}**;
- selective-resynchronization term: **{term}**;
- four-state classification: **{state_keep}**;
- Fisher: **{fisher_keep}**;
- retained-plasticity reframe: **{'required for review' if decision == 'NO-GO' else 'not yet required'}**.

The experiment and decision stop here. No CIFAR-10 run and no full-paper drafting is authorized without human review.
"""
    (paper_root / "07_mvp_implementation_report.md").write_text(implementation, encoding="utf-8")
    (paper_root / "08_mvp_results.md").write_text(results, encoding="utf-8")
    (paper_root / "09_mvp_decision.md").write_text(decision_doc, encoding="utf-8")


def main() -> None:
    analysis = analyze_locked(ROOT, ROOT / "configs" / "mvp_locked.yaml")
    write_reports(analysis)
    print(json.dumps({"decision": analysis["decision"], "fisher": analysis["fisher"]["status"]}, indent=2))


if __name__ == "__main__":
    main()
