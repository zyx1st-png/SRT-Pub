---
id: SRT-OBSERVED-CALIBRATION-OPERATIONS-20261026
type: execution-handoff
status: draft
record_stage: preparation-only-not-execution-authorized
date: 2026-10-26
layer: operations
epistemic_layer: experimental
claim_mode: protocol
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Experiments/neuro_sleep_null_calibration/OBSERVED_CALIBRATION_RESOURCE_REQUEST_2026-10-26.md
tags: [RIKEN, ObservedBaseline, Operations, Draft]
---

# Observed-only calibration operations

This is the scoped implementation handoff for the independent resource-review request, not permission to run. No production UUID or authorization has been created. Freeze the final reviewed PR HEAD after code/CI review; a hash is deliberately not embedded in its own source file. Sample and method pins are in `observed_calibration_runner.py`. The exact complete sample and candidate budget are executable validation inputs, not defaults that can be silently overridden.

## Preparation delivered

- Public H3 closure JSON and Markdown, with original run HEAD/UUID, aggregate differences, source warning analysis and file/hash-chain anchors. No signal, Q vector, original neuron ID or private path is in these public closure files.
- Deterministically generated 47-row primary / 40-row non-executable reserve manifest, outcome-blind selection and fixed order. Primary sample SHA-256: `f29acb99a05387b128f724bf818e3f402f7ced8a4080c12da4a936b9284d95c4`.
- Observed-only scientific path: original private job/subset/seed validation, historical reconstruction + independent topology check, shared canonical 200-Q helper, full graph/seed/Q/diagnostic hashes and private artifacts.
- One-entry raw-window cache, native I/O and phase timing, durable aborted/completed phase evidence; one worker supervised by existing Mac Watchdog, host activity lock and cumulative single-attempt ledger.
- Read-only preflight and pending-draft mode, exact researcher confirmation, audit-only verification; no resume or overwrite path.

## Reproduce synthetic validation

Use the target macOS arm64 / Python 3.14.0 environment with `g0-runtime-macos-arm64.lock` (unchanged: h5py 3.16.0, NetworkX 3.6.1, NumPy 2.5.3, python-louvain 0.16, SciPy 1.18.1). Test-only pytest/Ruff are outside the scientific lock.

```sh
"$PYTHON" -m pytest -p no:cacheprovider -q \
  Experiments/neuro_sleep_null_calibration/test_observed_calibration.py \
  Experiments/neuro_sleep_null_calibration/test_g0_q_protocol.py \
  Experiments/neuro_sleep_null_calibration/test_riken_source_identity.py \
  Experiments/neuro_sleep_null_calibration/test_h3_supervised_pilot.py \
  Experiments/neuro_sleep_null_calibration/test_h3_120_supervised_panel.py
"$PYTHON" Experiments/neuro_sleep_null_calibration/observed_calibration_runner.py --validate-sample
```

Synthetic tests create generated HDF5 arrays and small graphs with engineering seeds. Their real Watchdog child is the test module's `--synthetic-worker`; it rejects non-synthetic graph IDs and never opens RIKEN roots. Test authorizations use a fake all-`a` HEAD and temporary paths, which production Git identity rejects. Production child admission is tested separately up to a mocked scientific dispatcher, so no real source is computed. Actual synthetic scientific parity uses the same unmocked canonical 200-Q helper and compares with the original read/correlation/independent-builder path. Production MACOS_SAMPLED_PRESSURE configuration remains distinct from SAMPLED_ONLY fault tests; inherited native policy faults are covered by H3/Watchdog tests and run-time admission.

Local target verification on 2026-10-26: macOS 15.7.4 arm64, Python 3.14.0 and all five locked science dependencies match. The affected six-file suite (observed, shared Q, source identity, H3 pilot, H3-120 and Watchdog) passed **99 tests / 48 subtests**. This includes the optional hash-verified historical builder source used only with a synthetic HDF5 fixture and engineering seeds; no RIKEN signal/Q replay occurred. Ruff, compilation and deterministic sample hash checks pass. Native process-attributed I/O/RSS calls work on this Mac. The separately added Ubuntu CI tests the portable synthetic path; it does not prove macOS telemetry by simulation.

A separate read-only identity check verified all 47 selected historical jobs/subsets/seeds, the original seed-ledger file and six complete MAT hashes, without opening signal datasets or constructing graphs. A point resource sample showed Data/VM each 46.37 GiB free (shared capacity), host free-memory telemetry 58%, Swap used about 5.02 GiB/current-pool free about 0.98 GiB, AC power and normal thermal state. This is not a single-run preflight or authorization; Swap current-pool free is not a fixed remaining capacity. A new UUID/live check is still required. All inherited H3 method, source-manifest and packet hashes remain unchanged. H3 closure storage reporting distinguishes the Watchdog exit sample (which includes emergency scratch) from the smaller terminal directory after scratch cleanup.

## Future single-run procedure — requires new approval

1. Independent resource review assesses this exact sample, metrology and proposed 4h wall / 4 CPUh / 1 worker / 4-GiB sampled RSS / 1-GiB output envelope and existing system stops. Researcher decides explicitly. H3's earlier approval cannot be reused as this decision.
2. On the clean final reviewed HEAD, set the two existing private-root environment variables explicitly. Use the locked interpreter, generate a new UUID at that time and choose the new internal-APFS directory `$SRT_PSA_ROOT/canonical_observed_resource_calibration_2026-10-26/<UUID>`. Do not reuse any H3 directory or UUID.
3. Run read-only preflight. It hashes sources/jobs/seed ledger, checks runtime/method/sample/HEAD/output/host ledger and lock availability, and reads Mac resource telemetry. It neither loads a source signal dataset nor computes Q nor creates the run directory. `--authorization-draft` runs the same preflight and prints a **PENDING** draft with complete bindings; it cannot approve itself. Save its JSON privately only after examining it. No actual preflight result should be inferred from today's synthetic tests.

```sh
"$PYTHON" Experiments/neuro_sleep_null_calibration/observed_calibration_runner.py \
  --authorization-draft --head "$REVIEWED_HEAD" --run-id "$NEW_UUID" --run-dir "$NEW_RUN_DIR"
```

4. Researcher inspects exact method/source/sample/runtime hashes, resource limits, remaining macOS and audit-custody risks, final UUID/output and actual live preflight. Only after their explicit approval may the private JSON be completed with `APPROVED_FOR_SINGLE_RUN`, actual identity/time/resource-decision record and their complete confirmation. `PENDING` or mismatched binding is rejected. This is researcher accountability, not a cryptographic signature or a guarantee of human independent peer review.
5. Real entry (not to be run during preparation):

```sh
"$PYTHON" Experiments/neuro_sleep_null_calibration/observed_calibration_runner.py \
  --run --head "$REVIEWED_HEAD" --run-id "$NEW_UUID" --run-dir "$NEW_RUN_DIR" \
  --authorization "$PRIVATE_APPROVAL_JSON" --researcher-confirmation "$RESEARCHER_TYPED_LINE"
```

The exact line is `I AUTHORIZE OBSERVED CALIBRATION <UUID> f29acb99a05387b128f724bf818e3f402f7ced8a4080c12da4a936b9284d95c4 <FULL_HEAD>`. No assistant may supply it on behalf of the researcher. Launch repeats real-time checks and deducts measured preflight CPU/wall from the approved supervision allocation. The child rechecks identity under the Watchdog before reading signals. No sample expansion, recovery retry, budget increase or null stage follows automatically.

6. After completion/stop, use `--verify "$NEW_RUN_DIR"` and inspect its stdout/control/resource/phase/row records. The report returns each row's sampled RSS count/max (or `null` when no sample), and never describes it as a hard or true peak. A terminated process has only the durable completed prefix and aborted meters; unmeasured remaining work is not assigned zero cost. Verification failure or unknown resources requires manual audit, not another attempt.

Public follow-up should include resource aggregates, hashes and failures, not private source files or full per-neuron/Q artifacts. G0/T1 and the full observed baseline need their own later decisions.
