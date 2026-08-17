from pathlib import Path
import re


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise SystemExit(f"missing marker: {label}")
    return text.replace(old, new, 1)

# 1) Claim Ladder: namespace PD-A and harden symmetric evidence / review accounting.
ladder = Path("Governance/SRT_CLAIM_LADDER.md")
text = ladder.read_text(encoding="utf-8")
text = replace_once(
    text,
    "### 1A. P0 / Empirical Discrimination Boundary — Author Decision A (2026-08-17)",
    "### 1A. P0 / Empirical Discrimination Boundary — PD-A (2026-08-17)",
    "claim-ladder PD-A heading",
)
text = replace_once(
    text,
    "3. **A downstream D2 does not directly prove the primitive ontology.** It supports the empirical fruitfulness of the SRT architecture and the specific derivation that generated the forecast; it does not convert P0 into an experimentally observed object.\n4. **Persistent empirical underdetermination limits scientific claims, not automatically P0 membership.** If mature P3/P4 bridges repeatedly fail to produce D2, SRT must say that its Selection-first ontology remains empirically underdetermined relative to the tested rivals. P0 may still be reassessed for redundancy, incoherence, lack of derivational fruitfulness, or by a later author architecture decision, but `D2 = 0` alone is not a mechanical demotion rule.\n\nTherefore the correct research sequence is:",
    "3. **A downstream D2 does not directly prove the primitive ontology.** One D2-positive workline supports the empirical fruitfulness of that specific derivation / workline and counts as one architecture-fruitfulness exhibit; it does **not** by itself license architecture-wide empirical superiority.\n4. **Persistent empirical underdetermination limits scientific claims, not automatically P0 membership.** If mature P3/P4 bridges repeatedly fail to produce D2, SRT must say that its Selection-first ontology remains empirically underdetermined relative to the tested rivals. P0 may still be reassessed for redundancy, incoherence, lack of derivational fruitfulness, or by a later author architecture decision, but `D2 = 0` alone is not a mechanical demotion rule.\n\n**PD-A governance trigger (not a statistical confidence threshold).** A workline counts as `mature` for this trigger only if it freezes, before outcome inspection: an independently motivated middle-level consequence, a bounded rival state/update/calibration family, a common intervention and observable, symmetric failure criteria, and a terminal disposition (`spec-stage NO-GO`, executed D2-negative/rival-equivalent, or D2-positive). Mere dataset swaps or rephrasings of the same derivation do not count as independent worklines.\n\n- **Negative trigger**: after **3 independent mature worklines** spanning at least **2 distinct middle-level consequences** end D2-negative / rival-equivalent, `Core/SRT_OPEN_TENSIONS.md §13` must open a P0-01 fruitfulness / redundancy review **before a fourth substantially similar mature workline is authorized**. The review owner is §13; any P0 change remains author-gated.\n- **Positive attribution rule**: architecture-level empirical-fruitfulness language requires at least **2 independent D2-positive worklines grounded in distinct middle-level consequences**. A single positive remains local to its derivation / workline.\n- Historical A2 / P24 NO-GO results inform the review but are **not automatically back-counted** under this trigger because they were not all frozen under the PD-A maturity contract. The qualifying count at PD-A adoption is therefore `0`.\n\nDecision record: `Operations/SRT_PD_A_P0_D2_BOUNDARY_AUTHOR_DECISION_PACKET_2026-08-17.md`.\n\nTherefore the correct research sequence is:",
    "claim-ladder symmetry trigger",
)
ladder.write_text(text, encoding="utf-8")

# 2) P0 owner: namespace decision and point to the record.
core = Path("Core/SRT_Core_21_Minimal_Axioms.md")
text = core.read_text(encoding="utf-8")
text = replace_once(
    text,
    "### P0-01 / D2 Boundary — Author Decision A (2026-08-17)",
    "### P0-01 / D2 Boundary — PD-A (2026-08-17)",
    "core PD-A heading",
)
text = replace_once(
    text,
    "The corresponding governance rule is `Governance/SRT_CLAIM_LADDER.md §1A`.",
    "The corresponding governance rule is `Governance/SRT_CLAIM_LADDER.md §1A`; author record: `Operations/SRT_PD_A_P0_D2_BOUNDARY_AUTHOR_DECISION_PACKET_2026-08-17.md`.",
    "core PD-A record pointer",
)
core.write_text(text, encoding="utf-8")

# 3) OPEN_TENSIONS summary row + complete §13 repair.
tensions = Path("Core/SRT_OPEN_TENSIONS.md")
text = tensions.read_text(encoding="utf-8")
old_row = "| selection irreducibility / competitor-vocabulary deletion (§13) | Claim Ladder: `selection` remains a P0 primitive axiom; GOV-SUB01 Pass 1 executed `K=0` / limited-K / broad-K decomposition on 2026-08-16 and found substantial downstream reconstructability | no §13 qualifying `E_cf / E_int / divergence experiment / E_phen-E_norm` exhibit yet; Step 5 joint removal and perturbation sweep remain unexecuted | GOV-SUB01 residue remains **unassigned**; Pass-1 `R* / N* / P` readings are candidate-only; P0 status is not proof of irreducibility and broad-K reconstruction is not proof of role absence |"
new_row = "| Selection primitive fruitfulness / derivational indispensability (§13) | PD-A separates P0 primitive admission from downstream D2; Pass 1/1.5 establish literal dependence plus substantial reconstructability, but their historical residue verdict remains `UNASSIGNED` | no non-circular middle-level consequence has yet both survived deletion/replacement and earned D2 downstream; no post-PD-A full GOV-SUB01 re-adjudication has reassigned residue | do not treat P0 as empirical proof, D2 null as automatic P0 falsification, or retirement of the old extra §13 exhibit gate as a retroactive residue upgrade |"
text = replace_once(text, old_row, new_row, "open-tensions summary row")

section13 = r'''## 13. Selection Primitive Fruitfulness / Derivational Indispensability (open; PD-A 2026-08-17)

### PD-A

P0-01 remains SRT's explicit Selection-first primitive commitment. Direct `D2 / D3` rival discrimination is **not** an admission condition for P0. The two burdens remain separate:

- **P0 architecture**: coherence, non-redundancy, derivational fruitfulness, and load-bearing role inside SRT.
- **P3/P4 science**: a concrete bridge / lab hypothesis must freeze a bounded rival and produce a prospective counterfactual or intervention disagreement before SRT may claim empirical discrimination.

Therefore `D2 = 0` does not mechanically demote P0-01, while P0 status is not evidence that Selection is empirically irreducible or experimentally established.

Decision owner: `Governance/SRT_CLAIM_LADDER.md §1A`; record: `Operations/SRT_PD_A_P0_D2_BOUNDARY_AUTHOR_DECISION_PACKET_2026-08-17.md`.

### Current State

- `Core/SRT_Core_21_Minimal_Axioms.md P0-01 / AM-A` retain the primitive actualisation kernel with Selection.
- GOV-SUB01 Pass 1 found literal `K=0` dependence but substantial limited-/broad-K reconstruction. At execution time, the then-current §13 imposed an **additional exhibit gate**, so the audit correctly recorded formal residue as `UNASSIGNED` and treated `R* / N* / P` only as candidate readings.
- Pass 1.5 executed the frozen lowest-cost joint-removal case but did not complete the declared perturbation sweep or a full residue re-adjudication.
- RC-A removed former `Real Choice Moment` as a primitive-Selection discriminator.
- Core 24 remains a prediction-candidate / falsification-target surface with established D2 count `0`; current Selection-near P24 candidates remain rival-absorbable under the tested formulations.

These results constrain current empirical distinctiveness but do not, by themselves, decide whether the Selection primitive is theoretically fruitful or redundant.

### Problem Point

> Starting from Selection-first rather than object-first ontology, can SRT derive a non-trivial middle-level structure that is not merely a restatement of the primitive, and can a mature downstream workline turn that structure into a genuine D2/D3 disagreement?

This remains two tests, not one:

1. **Derivational fruitfulness / indispensability**: after deleting or replacing Selection under declared refit budgets, what internal structure, compression, dependency, or explanatory organization is lost without hidden reparameterization?
2. **Empirical discrimination**: does a specific P3/P4 operationalization prospectively forecast `O_SRT != O_R2` against a frozen bounded rival?

Passing (1) is not D2. Passing (2) does not experimentally prove P0 ontology.

### GOV-SUB01 after PD-A — residue re-adjudication rule

The **old §13 extra D2/exhibit gate is retired** by PD-A because direct D2 is no longer a P0-admission requirement. This retirement does **not** retroactively attach a GOV-SUB01 residue label to Pass 1 or Pass 1.5.

Their historical `UNASSIGNED` verdict remains the current formal record until a **post-PD-A re-adjudication** explicitly reopens the residue question. Any such pass must, at minimum:

1. declare the target, boundary, bearer where relevant, horizon, and refit budget;
2. use `Governance/SRT_GOV_SUB01_Subtractive_Audit_Protocol_v0_1.md §8.1` for primitive-Selection deletion;
3. execute Step 5 joint-removal / minimum-set tests wherever compensation remains live;
4. execute Step 6 perturbation robustness before assigning a robust residue reading;
5. rerun the mandatory hidden-reparameterization, target-laundering, bearer-relocation, short-horizon, and scale-collapse checks;
6. state an explicit `R* / N* / P` label rationale under GOV-SUB01 and state what evidence would reverse it.

Until such a record exists, formal residue stays **`UNASSIGNED`**. D2 remains mandatory for **scientific discrimination claims**, but it is neither a universal prerequisite for every GOV-SUB01 residue label nor a P0-admission condition.

### Mature-workline accounting / anti-immunization trigger

For PD-A governance, a workline counts as `mature` only when all are frozen before result inspection:

1. an independently motivated middle-level consequence, not a restatement of P0-01;
2. a bounded rival with declared state variables, update family, calibration range, and revision / complexity cost;
3. a common intervention and observable outcome;
4. symmetric SRT and rival failure criteria;
5. a terminal disposition: `spec-stage NO-GO`, executed/preregistered D2-negative or rival-equivalent result, or D2-positive result.

Dataset swaps, wording changes, or multiple implementations of the same derivation are not automatically independent worklines.

**Scoreboard at PD-A adoption**: `0` qualifying mature worklines. Historical A2 / P24 NO-GO results remain relevant pressure evidence but are not automatically back-counted because they were not all frozen under this maturity contract.

**Mandatory negative trigger**: after **3 independent mature worklines spanning at least 2 distinct middle-level consequences** end D2-negative / rival-equivalent, this §13 becomes a mandatory P0-01 fruitfulness / redundancy review **before a fourth substantially similar mature workline may be authorized**. This is a governance stop rule, not a statistical confidence threshold. §13 owns the review record; any P0 change remains an author decision.

**Positive attribution symmetry**: one D2-positive workline supports only that derivation / workline and counts as one architecture-fruitfulness exhibit. Architecture-level empirical-fruitfulness language requires at least **2 independent D2-positive worklines grounded in distinct middle-level consequences**. Neither case directly proves the P0 ontology.

### Future Hardening Direction

1. **Derive before testing**: choose one non-circular middle-level consequence from P0/P1.
2. **Run deletion / replacement**: use GOV-SUB01 with hidden-reparameterization controls; if a formal residue label is sought, satisfy the post-PD-A re-adjudication rule above.
3. **Only then operationalize** at P3/P4 without identifying the proxy with the ontology.
4. **Freeze bounded R2 + outcome** and require prospective `O_SRT != O_R2`; D0/D1 do not count as scientific discrimination.
5. **Report nulls symmetrically**: `NO-GO / rival-equivalent for this workline` counts toward the PD-A negative trigger when the workline is mature; a positive remains local until the positive attribution threshold is met.
6. **Obey the stop rule**: do not open an indefinite sequence of confirmatory-looking worklines once the mandatory review trigger fires.

The research priority is therefore:

> **derive a non-circular middle-level consequence from Selection-first, audit its theoretical dependence, then ask whether it can earn D2 downstream.**
'''
text, n = re.subn(
    r"## 13\. Selection Primitive Fruitfulness / Derivational Indispensability.*?(?=\n---\n\n## 14\.)",
    section13.rstrip(),
    text,
    count=1,
    flags=re.S,
)
if n != 1:
    raise SystemExit(f"expected one §13 replacement, got {n}")
# Ensure a blank line before the section delimiter.
text = text.replace(
    "> **derive a non-circular middle-level consequence from Selection-first, audit its theoretical dependence, then ask whether it can earn D2 downstream.**\n---\n\n## 14.",
    "> **derive a non-circular middle-level consequence from Selection-first, audit its theoretical dependence, then ask whether it can earn D2 downstream.**\n\n---\n\n## 14.",
    1,
)
tensions.write_text(text, encoding="utf-8")

# 4) Historical Pass-1 audit: preserve execution-time logic, add post-PD-A read-back.
p1 = Path("Operations/Audits/SRT_SELECTION_IRREDUCIBILITY_RIVAL_TEST_2026-08-16.md")
text = p1.read_text(encoding="utf-8")n