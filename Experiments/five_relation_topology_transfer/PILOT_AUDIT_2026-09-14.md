---
id: SRT-EXP-FIVE-RELATION-PILOT-AUDIT-20260914
type: experiment_audit
status: active
date: 2026-09-14
layer: meta
epistemic_layer: research_program
claim_mode: audit
canonical: false
ai_do_not_use_for_definition: true
---

# Five-relation topology transfer — pilot audit

## 1. Why this audit exists

During engineering validation, the originally provisional ranges were inspected:

```text
A: 52000-52063
B: 53000-53031
```

They are therefore **not holdout data** and must never be reported as confirmatory evidence.

They are reclassified as engineering/pilot seeds.

## 2. What the pilot was allowed to do

The pilot was used only to:

```text
verify exact pre-shift matching in Control A;
confirm that post-shift topology can produce non-identical trajectories;
identify an implementation bug in the first Control-B generator update;
replace unbounded generator accumulation with bounded generator reconstruction.
```

No scientific or architecture claim is assigned to pilot outcomes.

## 3. Model change before freeze

The initial B implementation accumulated generator bias indefinitely. That confounded `Revision` with historical lock-in.

Before confirmatory freeze it was replaced by a bounded update:

```text
generator <- (1 - half_budget) * generator + half_budget * current_target
```

Control B remains calibration-only under the preregistration.

## 4. Frozen-parameter decision

After this engineering step, no further parameter tuning may use post-shift outcomes from fresh confirmatory seeds.

The next config uses new untouched ranges:

```text
A confirmatory holdout: 62000-62063
B calibration replication: 63000-63031
C permutation / transfer bookkeeping: 64000-64063
```

The previous 51001-51020 range remains an engineering matching/calibration set.

## 5. Interpretation guard

```text
52000-52063 = PILOT ONLY
53000-53031 = PILOT ONLY
fresh confirmatory ranges = not inspected before config freeze
```

If the fresh holdout is weak or null, parameters must not be retuned and the result must stand.
