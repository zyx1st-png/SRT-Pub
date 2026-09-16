WHO BEARS FAILURE? — reviewer evidence and reproduction entry package
Version: v19.1 / 2026-09-16

PURPOSE
This package accompanies the manuscript “Who Bears Failure? Consequence Scope and Terminality in Survival-Coupled Artificial Agents.” It is a static reviewer-facing evidence and reproducibility entry package. It is not the historical supplement root README and does not revive earlier scalar-V or four-dimension validation claims.

STUDY STATUS
- Experiment 1: discovery study; not preregistered.
- Experiment 2: separately repository-preregistered before its confirmatory execution; predicted positive damage-persistence gradient not supported.
- Experiment 3: separately repository-preregistered before its confirmatory execution; predicted positive individual recovery-latency gradient not supported; observed ordinal direction negative.
- Experiment 4: separately repository-preregistered before implementation/confirmatory execution; first and only confirmatory run supports a positive but modest shared-versus-individual scope effect; the preregistered +0.10 strong-effect threshold was not reached.
- The additional E4 individual-scope latency analysis is post-hoc exploratory only and does not alter the E3 or E4 confirmatory verdicts.

CORE INTERPRETATION BOUNDARY
The paper does not claim that Experiment 4 quantitatively explains a fraction of the Experiment 1 terminality effect. E1 and E4 differ in update semantics, evaluation endpoint/state bank, confirmatory seed set, and baseline dynamics. E4 also bundles two submechanisms: the partner loses its own normal action opportunity and the individual-recovery exploitation window disappears.

REPRODUCTION ENTRY POINTS
E1 main and robustness:
  run_main.py
  run_zero_penalty.py
  run_lives_gradient.py
  run_payoff_sweep.py
  run_common_state_probe.py
  src/csc_experiment.py
  src/csc_robustness.py
  src/csc_probe.py

E2:
  EXPERIMENT2_RECOVERABILITY_PREREGISTRATION.md
  EXPERIMENT2_RECOVERABILITY_RESULT.md
  run_recoverability_gradient.py
  src/csc_recoverability.py
  results/recoverability_gradient_results.json

E3:
  EXPERIMENT3_CONSEQUENCE_RECOVERY_PREREGISTRATION.md
  EXPERIMENT3_CONSEQUENCE_RECOVERY_RESULT.md
  run_consequence_recovery.py
  src/csc_consequence_recovery.py
  results/consequence_recovery_results.json

E4:
  EXPERIMENT4_CONSEQUENCE_SCOPE_PREREGISTRATION.md
  EXPERIMENT4_CONSEQUENCE_SCOPE_ADJUDICATION.md
  run_consequence_scope.py
  src/csc_consequence_scope.py
  results/consequence_scope_results_E4_confirmatory_record.json
  full_first_confirmatory/consequence_scope_results.json

Post-hoc E4 latency cross-check:
  analyze_e4_individual_latency_exploratory.py
  results/consequence_scope_E4_individual_latency_exploratory.json

E1 committed results used by the manuscript:
  results/main_results.json
  results/zero_penalty_results.json
  results/lives_gradient_results.json
  results/payoff_sweep_results.json
  results/common_state_probe.json

Figures:
  figures/figure1_experiment_architectures_v19.svg
  figures/figure2_evidence_summary_v19_1.svg
  generate_v19_1_evidence_summary.py

ENVIRONMENT
The historical E1 package records both broad minimum requirements and a locked environment for exact common-state-probe reproduction. Cross-platform or different NumPy/Python versions can cause trajectory-level divergence even under identical seeds; use the locked environment when bit-level identity is required.

E4 FULL FIRST-CONFIRMATORY ARTIFACT
The preserved GitHub Actions artifact is named csc-e4-first-confirmatory-result. At packaging time its artifact ID is 10400498866, run ID 34977281851, head SHA 96e9a8bf0a1a45a39c7327533477e1bb76633d89, and GitHub artifact digest sha256:236c35cb1c7c44b404632438b4e411cc7113dd68ed4780e744af2cdf53dd3d4f. The inner consequence_scope_results.json provenance is separately recorded by the project’s result/adjudication files.

WHAT IS INTENTIONALLY EXCLUDED
- the historical supplement README.md, because it describes an earlier manuscript and contains superseded scalar-V/four-dimensional framing;
- internal post-result theory audits and mechanism-development notes not necessary to reproduce the reported analyses;
- Git history and repository metadata;
- any private or permission-gated reviewer link.

ANONYMITY / ACCESS
This package should be uploaded directly with the submission or through a static access route that does not request reviewer authentication and does not expose reviewer identity to the author. The journal’s current instructions require review-stage supplementary access not to facilitate or potentially undermine reviewer anonymity.

CONTACT
Questions about the package should be routed through the journal during peer review.
