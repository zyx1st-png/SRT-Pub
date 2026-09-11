from pathlib import Path

p = Path("STATUS.md")
s = p.read_text()

def replace_once(old: str, new: str) -> None:
    global s
    if old not in s:
        raise RuntimeError(f"STATUS anchor not found: {old[:180]!r}")
    s = s.replace(old, new, 1)

replace_once(
    "> **历史快照**：pre-#931 根 STATUS 已保存在 `Operations/Status_History/SRT_STATUS_2026-09-11_PRE_PR931_ROOT_SNAPSHOT.txt`。#931/#933 的旧路由继续作为历史记录保留，但不再优先于本页明确列出的 #938 修复控制面。",
    "> **历史快照**：pre-#931 根 STATUS 已保存在 `Operations/Status_History/SRT_STATUS_2026-09-11_PRE_PR931_ROOT_SNAPSHOT.txt`。#931/#933/#938 继续作为重构与纠偏 provenance；当前形成层 canonical 路由以 #940（Stable-ISP standing decoupling）与 #942（One / Selection-position owner landing）为准。",
)

replace_once(
    """latest merged reconstruction checkpoint:
#938 Repair R1 around pre-object vertical formation before canonical landing
merge = 12b38e525470ea56cc1b0ce7da20502efe6743c9
status = MERGED / NONCANONICAL

historical merged checkpoints retained for provenance:
#931 Consolidate Selection, vertical One, Bearer, and position-indexed Active Selection
#933 author-adjudicated reviewer reconciliation

current phase:
POST-#938 STATUS / CONTEXT CLOSEOUT
-> then separate small C-risk canonical landing package

canonical edit in #938 = NO
new Level 1 = NOT ASSIGNED
Level 2 = HOLD
HOLD EXIT REVIEW 2 = NOT TRIGGERED
scientific distinctiveness = NOT ESTABLISHED
whole-architecture non-substitutability = NOT ESTABLISHED
research_mode = U""",
    """latest merged canonical checkpoint:
#942 Land thin One / Selection-position formation owner
merge = 2245995bde809f7ec6dcd6f5d6b68504e00eedf4
status = MERGED / BOUNDED R1 CANONICAL LANDING

immediately prior canonical standing repair:
#940 Decouple P1-T06 Stable ISP standing from formation and subject entry
status = MERGED

reconstruction / author provenance retained upstream:
#938 Repair R1 around pre-object vertical formation before canonical landing
#941 A/O3 author owner decision (dedicated thin L1 owner)

current phase:
POST-#942 STATUS / CONTEXT CLOSEOUT
-> then bounded Bearer necessary/sufficient-condition reconstruction

One / Selection-position canonical semantic owner = `Core_Law/SRT_One_Formation.md`
Stable ISP standing owner = P1-T06, stronger and separate
Bearer necessary/sufficient conditions = OPEN
new Level 1 = NOT ASSIGNED
Level 2 = HOLD
HOLD EXIT REVIEW 2 = NOT TRIGGERED
scientific distinctiveness = NOT ESTABLISHED
whole-architecture non-substitutability = NOT ESTABLISHED
research_mode = U""",
)

replace_once(
    """For current R1 meaning, load in this order:

1. `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_R1_POSITION_PERSPECTIVE_ANTICIPATION_BEARER_2026-09-11.md`
2. `01_Source_Intuition/SRT_AUTHOR_REENTRY_VERTICAL_FIRST_PERSON_BEARER_SUPERSESSION_2026-09-11.md`
3. `Operations/Audits/SRT_R1_FINAL_SUPERSESSION_AND_ROUTING_RECONCILIATION_2026-09-11.md`
4. `Operations/Audits/SRT_R1_FORMATION_STANDING_LANDING_PREPARATION_2026-09-11.md`
5. `Operations/Audits/SRT_R1_D3_STABLE_ISP_SUBJECT_WITNESS_2026-09-11.md`""",
    """For current R1 meaning, load in this order:

1. `Core_Law/SRT_One_Formation.md` — current canonical formation owner
2. `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_R1_ONE_SELECTION_POSITION_OWNER_2026-09-11.md` — A/O3 owner decision provenance
3. `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_R1_POSITION_PERSPECTIVE_ANTICIPATION_BEARER_2026-09-11.md`
4. `01_Source_Intuition/SRT_AUTHOR_REENTRY_VERTICAL_FIRST_PERSON_BEARER_SUPERSESSION_2026-09-11.md`
5. `Operations/Audits/SRT_R1_FINAL_SUPERSESSION_AND_ROUTING_RECONCILIATION_2026-09-11.md`
6. `Operations/Audits/SRT_R1_ONE_FORMATION_CANONICAL_LANDING_SCOPE_2026-09-11.md`
7. `Operations/Audits/SRT_R1_D3_STABLE_ISP_SUBJECT_WITNESS_2026-09-11.md`""",
)

replace_once(
    "## Current theory spine — repaired #938 reading",
    "## Current theory spine — post-#942 canonical reading",
)
replace_once(
    "This is the current primary reconstruction axis.",
    "This is now the current primary formation axis; its `active vertical organization -> One / Selection-position` semantics are canonically owned by `Core_Law/SRT_One_Formation.md`, while stronger standing remains downstream.",
)
replace_once(
    """One
= continuing localized vertical process-unit / formed unity candidate.

Selection-position_t
= time-local operative from-where of that continuing organization.

Bearer
= downstream reconstruction problem around anticipatory bearing
  of an already formed position;
  exact necessary / sufficient conditions OPEN.""",
    """One
= canonically: localized, lineage-relative, processual formed unity
  continuing through Selection-mediated recurrent reconstitution.

Selection-position_t
= canonically: time-local operative from-where of that continuing One.

Bearer
= downstream reconstruction problem around anticipatory / consequence bearing
  of an already formed position;
  exact necessary / sufficient conditions OPEN.""",
)

replace_once(
    """Scoped candidate retained:

```text
within declared same unit / scale / lineage / interval / perturbation range,
Stable ISP may realize D4a's thin formed-continuity function.
```

This is not a reverse implication, generation law or full One theorem.""",
    """Post-#942 routing:

```text
One / Selection-position formation
= owned upstream by `Core_Law/SRT_One_Formation.md` at D4a strength.

P1-T06 Stable ISP
= stronger recurrent standing criterion.

B13
= stabilization / generative-health crosswalk.
```

Do not infer `One -> Stable ISP`, `Stable ISP -> full One theorem`, or subjecthood from this routing. The formal necessary-and-sufficient One theorem remains OPEN.""",
)

replace_once(
    """1. `CANONICAL_REGISTRY.md`
2. `Governance/SRT_CLAIM_LADDER.md`
3. `Governance/SRT_CLAIM_MODE_AUDIT.md`
4. `Core_Law/SRT_L0_Metaphysics.md`
5. `Core/SRT_Core_21_Minimal_Axioms.md`
6. `Core/SRT_Core_21b_Constitutive_Theorems.md`
7. `_SRT_D_VALUE_CANONICAL.md`
8. `_SRT_PSI_F_CANONICAL.md`
9. `_SRT_T_DIR_CANONICAL.md`
10. `_SRT_CROSS_DOMAIN_MATRIX.md`
11. `Core/SRT_Core_22_Equations.md`
12. `_SRT_SYMBOL_TABLE.md`
13. `Core/SRT_Core_21_Formal_Axioms.md`
14. `Core/SRT_Core_21c_Bridge_Hypotheses.md`""",
    """1. `CANONICAL_REGISTRY.md`
2. `Governance/SRT_CLAIM_LADDER.md`
3. `Governance/SRT_CLAIM_MODE_AUDIT.md`
4. `Core_Law/SRT_L0_Metaphysics.md`
5. `Core/SRT_Core_21_Minimal_Axioms.md`
6. `Core_Law/SRT_One_Formation.md`
7. `Core/SRT_Core_21b_Constitutive_Theorems.md`
8. `_SRT_D_VALUE_CANONICAL.md`
9. `_SRT_PSI_F_CANONICAL.md`
10. `_SRT_T_DIR_CANONICAL.md`
11. `_SRT_CROSS_DOMAIN_MATRIX.md`
12. `Core/SRT_Core_22_Equations.md`
13. `_SRT_SYMBOL_TABLE.md`
14. `Core/SRT_Core_21_Formal_Axioms.md`
15. `Core/SRT_Core_21c_Bridge_Hypotheses.md`""",
)

replace_once(
    "For current R1 work, load the #938 author adjudication and final supersession reconciliation **before** #931/#933 historical Bearer routing.",
    "For current R1 work, load `Core_Law/SRT_One_Formation.md` and the #941 A/O3 author adjudication first; then load the #938 final supersession / Bearer reconciliation before #931/#933 historical Bearer routing.",
)
replace_once(
    "#938 is a merged noncanonical checkpoint. It controls current reconstruction routing within its scope but does not by itself authorize or constitute a canonical rewrite.",
    "#938 remains a merged noncanonical reconstruction checkpoint; #940 and #942 are the bounded canonical landings derived from later author/governance gates. #942 does not authorize Bearer, subjecthood, phenomenality, `d`, `sigma`, `T_dir`, or collective-subject closure beyond its explicit scope.",
)
replace_once(
    "canonical owner hardening;",
    "Bearer canonical ownership / sufficiency hardening;",
)

replace_once(
    """1. treat #938 as the latest merged noncanonical reconstruction checkpoint;
2. treat #938 author adjudication + final supersession reconciliation as current R1 routing control;
3. finish post-#938 STATUS / context-bundle freshness closeout without changing theory;
4. do not reopen broad theory expansion by default;
5. after mechanical closeout, open a separate small C-risk canonical landing package focused on formation ontology + standing de-coupling;
6. keep Bearer necessary/sufficient conditions, subjecthood, phenomenality, d/sigma/T_dir and collective subject sufficiency OPEN unless separately adjudicated;
7. preserve Level 2 HOLD and do not infer scientific distinctiveness from the canonical landing itself.""",
    """1. treat #942 as the latest bounded canonical R1 formation checkpoint;
2. use `Core_Law/SRT_One_Formation.md` as the canonical owner for active vertical formation -> One / Selection-position;
3. use P1-T06 only for stronger Stable-ISP standing and B13 only for stabilization / generative-health crosswalks;
4. complete this post-#942 STATUS / context-bundle closeout without further theory edits;
5. next substantive work: reconstruct Bearer necessary/sufficient conditions from the already formed One / Selection-position, with anticipatory self-relevance / non-outsourcable consequence bearing as the live pressure rather than retrospective writeback alone;
6. keep subjecthood, phenomenality, d/sigma/T_dir and collective subject sufficiency OPEN unless separately adjudicated;
7. preserve Level 2 HOLD and do not infer scientific distinctiveness from #942 itself.""",
)

p.write_text(s)
print("STATUS post-#942 closeout edits applied")
