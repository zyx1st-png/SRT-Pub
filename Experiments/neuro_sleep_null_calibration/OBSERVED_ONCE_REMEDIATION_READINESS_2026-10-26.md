---
id: SRT-OBSERVED-ONCE-REMEDIATION-READINESS-20261026
type: engineering-readiness
status: draft
date: 2026-10-26
layer: operations
epistemic_layer: experimental
claim_mode: evidence
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Experiments/neuro_sleep_null_calibration/OBSERVED_CALIBRATION_TELEMETRY_INCIDENT_AND_REMEDIATION_DRAFT_2026-10-26.md
  - Experiments/neuro_sleep_null_calibration/OBSERVED_CALIBRATION_REMEDIATION_SUFFIX_V1_2026-10-26.json
  - Experiments/neuro_sleep_null_calibration/OBSERVED_REMEDIATION_SYNTHETIC_TEST_PLAN_V1.json
tags: [RIKEN, ObservedBaseline, OneException, EngineeringOnly]
---

# One 41-row observed-only remediation: engineering handoff

**READY FOR INDEPENDENT REMEDIATION REVIEW. No real remediation authorization
or claim has been created.** This branch starts at #1133
`a270d29fe259b10fe7d0e1cf0645b66e602d7981`. The researcher's
[decision](https://github.com/zyx1st-png/SRT-Pub/pull/1133#issuecomment-6412266654)
approves engineering, synthetic tests and a later review of one exception;
it does not approve a real UUID or signal computation. The prior
[technical review](https://github.com/zyx1st-png/SRT-Pub/pull/1133#issuecomment-6412223225)
is a limited AI-assisted review, not external human peer review.

## Fixed science and prior identity

The full 47-graph sample remains
`f29acb99a05387b128f724bf818e3f402f7ced8a4080c12da4a936b9284d95c4`.
Only exact `primary_rows[6:47]`, original sample orders 7–47, can be dispatched:
41 graphs, 8,200 canonical trials. The first six are never recomputed; no reserve
row is available. Row 7 starts with a fresh raw-window cache and complete graph
reconstruction. Its abandoned partial old work is already charged to OLD.

- Suffix SHA-256: `9dbb10990d0cdffa2a864e6aaec12ca42bafcf85783e05668c1b8e06b5d28808`.
  Encoding: canonical UTF-8 JSON of the exact 41 row objects, without a newline.
- Packet SHA-256: `208121aad2f3a9d07c0b6dc98a005b5a126a4f3cc3c887c24f7cb6bbfa7639ae`.
  Encoding: canonical UTF-8 JSON plus one LF. `--validate-packet` reconstructs
  it from the original fixed sample and incident identities before accepting it.
- Original UUID: `cf726336-0f3b-4506-9cd3-cb36da3f7e12`;
  execution HEAD `b4a4b34ed7432efbf0d289a8b244345f73cf6a43`.
- Original terminal SHA:
  `4eae491304bd80294854c79227067144f2d6bb42ecdec42ae085adb1d81cc0b1`;
  manifest SHA:
  `92f52e49d82c81c208693f96ab4e2a0791dbdbc7dde04f710f6e28a8c1907a97`.

`observed_remediation_identity.verify_original()` calls the official old-run
verifier, then checks the exact directory inventory, regular-file identities,
six saved result hashes/input identities/200-seed and Q lengths, summary,
manifest, three audit tips, specific operational stop, unique host start/finish,
old measured resources, and the old approved-authorization → preparation-evidence
→ eight-CPU identity chain. All four original preparation files are also
hash-bound. The old host ledger is anchored through its finish at sequence 5,
tip `f33d477aae2003002a6e5e301a72699a9fcb557070839adedca999f048e678d9`;
legitimate later appends are allowed. The entire current chain must still verify.

The actual original was re-read successfully during this engineering work:
`VERIFIED_TERMINAL`, six rows, `completed=false`, `resume_allowed=false`.
No signal array or new real Q was computed. Original artifacts and the real
host ledger remained unchanged, and the real exception receipt does not exist.

## One-time entry and durable consumption

`observed_calibration_remediation.py` is a separate entry. The ordinary runner
continues to reject the consumed full sample. The new entry requires its own
`SRT_OBSERVED_ONCE_REMEDIATION_AUTHORIZATION_V1`, status
`APPROVED_FOR_SINGLE_REMEDIATION`, a new personally confirmed UUID and a clean
final HEAD. Pending drafts and old `APPROVED_FOR_SINGLE_RUN` credentials fail.
Bindings include the full sample/suffix/packet, old identities and directory,
new directory, active method, runtime/Q/implementation hashes, unchanged resource
caps, existing native-thread environment, eight-CPU host and exact host-state
directory. A caller cannot choose an unbound shadow ledger.

Under both existing host locks, the controller checks the unique closed old
attempt and absence of an earlier exception. It creates an exclusive,
non-replaceable `observed-remediation-<OLD_UUID>.claim.json` receipt and fsyncs
it, then appends/fsyncs `observed_remediation_claimed` in the existing ledger.
The receipt binds the predicted hash-chain record and its binding/auth hash.
It precedes expensive old/source identity checks and all signal processing.
An interrupted receipt remains an uncertain consumed marker; it is not cleaned
up for retry. A receipt without a claim, a claim without a receipt, a removed
whole claim suffix, a duplicate/new-UUID claim or an incomplete invocation all
fail closed. A preflight failure consumes the exception and records its reason
and measured or explicitly unknown cost. No automated recovery is implemented.

Existing supervision is reused with additional admission, cumulative-stop and
closing hooks. Those hooks do not skip the shared host-lock/packet checks.
The scientific child separately revalidates authorization, claim, old evidence,
HEAD, source/job/seed identities and runtime, then calls the existing row kernel
only for the fixed suffix. Host telemetry stays outside the scientific group;
the unchanged Watchdog still rejects unknown children. No broad helper whitelist
is added. Every stop exhausts this exception, including scientific, operational
and unknown failures. Joint reporting preserves the runner's scientific failure
category even where the inherited generic transport summary labels an exit.

Receipt plus hash chain detect accidental partial loss and single-artifact
rollback. They are local researcher-controlled files, **not independently
immutable custody**; coordinated malicious rewriting/removal of all local
anchors is outside that guarantee. Nothing here claims a third-party signature.

## Aggregate resource accounting

Caps remain 14,400 s wall, 14,400 CPU s, one compute worker, 4 GiB sampled RSS,
1 GiB combined output, one raw-window cache ≤256 MiB and each result ≤32 MiB.
All existing Data/VM 40-GiB start/30-GiB reserve, 20% memory, Swap growth, AC,
thermal, sleep and telemetry-failure rules remain. Sampled RSS is not a hard
memory limit. One compute worker may still use native-library threads.

| Old quantity | Observation or conservative charge |
|---|---:|
| Watchdog wall / accounted CPU | 183.267596722 s / 188.484654 s |
| Formal preflight wall / self CPU | 7.245956417 s / 6.289025 s |
| Host start-to-finish span | 183.435804 s |
| Segmented measured wall (host span + preflight) | 190.681760417 s |
| Charged wall: authenticated authorization confirmation → host finish | **201.318418 s** |
| Charged CPU upper bound | **332.891224227 s** |
| Old terminal directory actual bytes | 968,363 B |
| Old preparation files + attributed old host records | 100,801 + 1,839 = 102,640 B |

The wider wall window starts at the byte-authenticated old approval timestamp
`08:15:25.339488Z` and ends at the old host finish `08:18:46.657906Z`. It
conservatively charges waiting before launch and covers authorization/import
work outside the old preflight stopwatch. The contained preflight, controller
and Watchdog intervals are **not added a second time**. Old CPU self-only
preflight excluded helper CPU, so the charge is

```text
max(old_watchdog_CPU + old_preflight_self_CPU,
    old_watchdog_CPU + 8 * (authorization_wall_window - old_watchdog_wall))
```

Eight logical CPUs are supported by old hashed preparation evidence, not guessed
from the present host. This is an explicit conservative accounting charge;
it is not a new measurement of historical CPU, a completion bound, or T_PS-A.
This policy is stricter than the decision comment's theoretical segmented
remainder. It must be checked in independent remediation review and in the
future researcher-bound accounting choice, rather than silently described as
exact historic resource reconstruction.

New controller wall starts at its OS process-birth timestamp rounded down to a
second (less than one second of conservative rounding), including startup and
all identity/preflight work. CPU includes lifetime self + waited children and
sampled live-group CPU. Reaping may conservatively overlap; retain the high-water
charge and separately expose final native observed CPU. Do not add Watchdog CPU
again to this whole-controller observation. Verify closure charges against
Watchdog/controller and preflight lower bounds. Unknown/nonfinite/inconsistent
accounting or clock/sleep anomalies stop.

Before dispatch deduct new consumed costs, **5 s wall / 40 CPU s / 64 KiB** of
fully charged closing allowance, and a separate stopping margin of **1 s wall /
8 CPU s** (eight native CPUs × poll-plus-termination grace). A closing record
cannot include the cost of writing itself; this finite allowance covers the
last audit fsyncs and is labeled charged, not observed. Missing, damaged or
over-allowance closure cannot yield joint success. This remains sampled control,
not an OS hard CPU limit or a guarantee against an indefinitely stalled syscall.
Full OLD/NEW result verification runs before the final meter snapshot, with
budget checks between audited files/rows. Only after the tail check passes is
an exclusive `remediation-closed.json` written, binding the account hash, claim
tip and accounted-ledger tip. Its prospective encoded bytes are checked before
creation. A tail failure never creates that receipt; removing a complete
violation-log suffix cannot turn the failure into a valid success. The run
returns the already verified report; it does not perform uncharged heavy
verification after accounting closure. A later explicit `--verify` is a separate
read-only audit, not another experiment or recovery.

Before any new cost, available supervision ceilings after these reserves are
**14,192.681582 s wall / 14,019.108775773 CPU s / 1,072,605,285 B**.
These are upper ceilings only. Actual startup, old re-verification, new preflight,
authorization, receipt, host-log growth and all work further reduce them.
Output counts OLD real files + OLD auxiliary files + NEW directory, authorization,
receipt and this activity's ledger prefix through closure. Future unrelated
ledger appends do not become retrospective charges to this activity.

## OLD / NEW / TOTAL verification

`--verify` is audit-only. It requires old evidence verification, the exact
non-synthetic 41-row science start, source/graph/seed/Q metadata and file hashes,
the unique claim/receipt and closing account, independent resource lower bounds,
and reproduced cumulative charges. A completed NEW must contain exactly 41
committed results and 8,200 Q trials. Synthetic flags, short rows, partial writes,
missing closure, bad hashes, wrong HEAD or a ledger mismatch cannot become success.

The report contains OLD = six graphs / 1,200 Q with old worker-endpoint metrology;
NEW = up to 41 graphs / 8,200 Q with external Watchdog metrology; TOTAL = their
fixed unique coverage and cumulative charges. A full result is **6 OLD + 41 NEW
across two activities**, with independent startup/cache behavior. It is not one
continuous 47-row timing sample or a reliable 4,900-graph/G0 U95 forecast.

## Engineering validation and remaining gate

The checked-in synthetic plan predates execution. Initial affected-suite run:
**130 passed, 99 subtests passed, 96.61 s**, including exactly three predeclared
Mac-native 41-row engineering trials. All three completed; Watchdog wall/CPU
were approximately 10.105/13.532, 8.964/13.051 and 8.545/12.825 seconds, with
sampled peak RSS 91.5–97.8 MB and host memory telemetry minimum 34–38%.
No fourth native run was used to obtain a pass. One additional metadata-only
shadow-ledger test passed. A later read-only verifier correction excludes future
unrelated host-ledger growth; its predeclared targeted non-native complete-suffix
test passed once (9.12 s). No new native batch was run for that correction.
The closing-order/receipt revision then passed its predeclared four non-native
cases once (19.18 s): complete suffix, unknown child, child exit, and injected
tail overrun followed by deletion of the entire violation line. A final
metadata-only prospective-closing-byte boundary test passed once (0.57 s).
Final-audit exception recording was then added; one predeclared non-native
tail-overrun test passed once (8.81 s), deleting the **entire** violation suffix
and still requiring rejection without the independent closure receipt.
All failure/accounting evidence remains in retained fixtures. None of
these targeted changes reran the predeclared native three-trial batch.

Tests cover fixed suffix/order, no prefix computation, authorization positives
and mismatches, real spawn claim race, claim-then-controller-exit, whole claim
suffix deletion, absent approval, unknown child, child exit, write failure,
CPU/output exhaustion, native sampling without worker subprocesses, canonical
graph/seed/Q parity, account corruption and no overwrite. Local synthetic
fixtures and JUnit/stdout logs are retained; CI uploads synthetic evidence even
on failure with 14-day retention. Synthetic patches replace private identity
admission only; there is no production test-mode CLI. All fixture graph IDs and
rows explicitly identify engineering-only data.

The earlier untraceable Mac synthetic stop in #1133 remains disclosed; these
successful tests do not retroactively diagnose or erase it. Other residuals are
sampled memory/process limits, possibly conservative CPU overcharge at reaping,
the finite last-write allowance and local custody. These belong in the independent
remediation review, not in a renewed H3 methods audit.
The final scope-limited AI static review found its identified claim, joint-audit,
budget and closing blockers repaired and returned READY FOR INDEPENDENT
REMEDIATION REVIEW. It performed no additional native or real calculations;
this is still AI-assisted code review, not external human peer review.

After independent review, a researcher would still have to approve the final
accounting/code identity, supply a new UUID/path and pending authorization, pass
fresh live source/environment/Mac/lock checks, and personally enter:

```text
I AUTHORIZE ONE OBSERVED REMEDIATION <NEW_UUID> cf726336-0f3b-4506-9cd3-cb36da3f7e12 9dbb10990d0cdffa2a864e6aaec12ca42bafcf85783e05668c1b8e06b5d28808 <FINAL_HEAD>
```

Future commands use `observed_calibration_remediation.py --authorization-draft`,
`--run`, or read-only `--verify`, with explicit roots and the required
`--head/--run-id/--run-dir/--authorization/--researcher-confirmation` arguments.
No real new UUID, approved JSON, claim or computation was created in this work.
The 40 reserve graphs, full baseline, biological 4E nulls, G0 and T1 remain excluded;
G0/T1 remain RESOURCE NO-GO. Draft PRs remain unmerged.
