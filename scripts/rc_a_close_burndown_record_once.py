from pathlib import Path

p = Path("Operations/Audits/SRT_RC_A_P1_T05_DEMOTION_DERIVATIVE_SYNC_2026-08-17.md")
text = p.read_text(encoding="utf-8")


def replace_exact(old: str, new: str, expected: int = 1) -> None:
    global text
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"expected {expected}, found {count}: {old[:140]!r}")
    text = text.replace(old, new)


replace_exact(
    "record_stage: semantic_burndown_active",
    "record_stage: semantic_burndown_complete",
)
replace_exact(
    "## 7. Semantic burn-down ledger — first verified owner pass",
    "## 7. Semantic burn-down ledger — completed verified owner pass",
)

stop = "**Stop rule**: do not reopen former P1-T05 at P1 without a new author decision and an independent constitutive derivation."
completion = '''### Completion record — 2026-08-17

Semantic owner sync is complete for the four directly verified live owners in §7:

```text
Core_Law/SRT_L1_Formalism.md
Core_Law/SRT_Collective_Selection.md
Core_Law/SRT_Irreversibility.md
_SRT_T_DIR_CANONICAL.md
```

Completed corrections:

- `r(t)` no longer receives P1 authority from former P1-T05 and cannot define whether Selection exists;
- `d_c` is no longer reverse-defined by the `r` proxy in the L1 formalism; the `r` expression is explicitly a P2/P3 operationalization candidate;
- T-COLL-1 is separated from T-COLL-4: higher-order collective ISP structure is not the same as stronger collective agency / reauthorization;
- T-COLL-4 is explicitly P2/P3 and cannot decide whether collective Selection occurred;
- `Irreversibility` retains ST-A / former-P1-T07 provenance while narrowing only the `r(t)` visibility / generative-health use;
- `T_dir` Part I blocks `L2 automation -> no Selection`, and Part II carries an explicit RC-A supersession note instead of a wholesale historical rewrite;
- no new Choice subtype, scalar, operator, P0 or P1 claim was introduced.

All large-owner edits were applied through asserted exact replacements. The temporary helper workflows / scripts self-delete from the branch after successful execution; they are not part of the intended PR diff.

**Verification boundary**：this record closes the **semantic owner-sync** portion of RC-A. Merge remains gated by the repository Governance Preflight. The optional bounded-retrieval rerun in §9 condition 8 was **not executed in this pass** because the existing protocol requires genuine repeated agent runs under a frozen retrieval budget; it is not simulated or marked as passed here.'''
replace_exact(stop, completion + "\n\n" + stop)

p.write_text(text, encoding="utf-8")
print("RC-A closure record updated")
