from pathlib import Path

p = Path("STATUS.md")
text = p.read_text(encoding="utf-8")


def replace_once(old: str, new: str) -> None:
    global text
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"expected one match, got {n}: {old[:120]!r}")
    text = text.replace(old, new, 1)


def replace_between(start: str, end: str, new: str) -> None:
    global text
    i = text.find(start)
    if i < 0:
        raise SystemExit(f"start marker missing: {start!r}")
    j = text.find(end, i + len(start))
    if j < 0:
        raise SystemExit(f"end marker missing: {end!r}")
    text = text[:i] + new.rstrip() + "\n\n" + text[j:]

replace_once(
    "#931/#933/#938 继续作为重构与纠偏 provenance；当前形成层 canonical 路由以 #940（Stable-ISP standing decoupling）与 #942（One / Selection-position owner landing）为准。",
    "#931/#933/#938 继续作为历史重构与纠偏 provenance；#940/#942 是局部 landing。自 #947 起，跨 owner 的当前生成顺序、非同一性与 OPEN gate 以 `Core_Law/SRT_Generative_Ontology_Spine.md` 为第一 canonical 路由，旧 canonical 的冲突跨层推论转为 cleanup / retyping debt。",
)

replace_between(
    "## Fast Status",
    "---\n\n## Current theory spine",
    """## Fast Status

### 1. 当前工作状态

```text
latest merged canonical checkpoint:
#947 Land canonical generative ontology spine before old-canonical cleanup
merge = 9afe036b1bf35b896afa3b9900613fdfb563cfd9
status = MERGED / CROSS-OWNER CANONICAL SPINE

prior bounded canonical landings:
#942 One / Selection-position formation owner
#940 Stable-ISP standing decoupling

current phase:
POST-#947 STATUS / CONTEXT CLOSEOUT
-> then OLD-CANONICAL REVERSE AUDIT FROM NEW SPINE

cross-owner generative routing owner = `Core_Law/SRT_Generative_Ontology_Spine.md`
local One / Selection-position owner = `Core_Law/SRT_One_Formation.md`
Stable ISP standing owner = P1-T06, stronger and separate
Bearer semantic route = formed One + P prospective self-indexing + E same-One prospective exposure -> Bearer
formal cross-domain P+E N&S theorem = OPEN
Bearer -> actual 承担 / concern / agency / subject / cognition / phenomenality = separately OPEN
new Level 1 = NOT ASSIGNED
Level 2 = HOLD
HOLD EXIT REVIEW 2 = NOT TRIGGERED
scientific distinctiveness = NOT ESTABLISHED
whole-architecture non-substitutability = NOT ESTABLISHED
research_mode = U
```

### 2. Current controlling route

For current ontology / canonical-cleanup work, load in this order:

1. `Core_Law/SRT_Generative_Ontology_Spine.md` — current cross-owner canonical order / non-identity / OPEN-gate owner
2. `CANONICAL_REGISTRY.md` — local owner routing after the spine
3. `Governance/SRT_CLAIM_LADDER.md` / `Governance/SRT_CLAIM_MODE_AUDIT.md` — claim hardness / demotion state
4. `Core_Law/SRT_L0_Metaphysics.md` / `Core_Law/SRT_One_Formation.md` / P1-T06 / d / Psi_f / T_dir — local owners, only within spine-compatible scope
5. `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GENERATIVE_SPINE_FIRST_CANONICAL_CLEANUP_2026-09-11.md` — author execution-order provenance
6. `Operations/Audits/SRT_GENERATIVE_ONTOLOGY_SPINE_CANONICAL_LANDING_SCOPE_2026-09-11.md` — cleanup scope / next audit order

Current cleanup rule:

```text
new spine = research / audit constraint;
older conflicting cross-layer canonical prose = audit target, not veto authority;
compatible local definitions survive;
retiring an old claim does not require inventing a replacement theorem;
OPEN stays OPEN unless separately adjudicated.
```

The pre-#947 unmerged branch `theory/canonical-cleanup-b1-individuation-20260911` is candidate patch material only. Do not merge it as-is; re-audit / rebase its useful repairs against the new spine.""",
)

replace_once(
    "## Current theory spine — post-#942 canonical reading",
    "## Current theory spine — post-#947 canonical reading",
)

replace_once(
    "Bearer\n= downstream reconstruction problem around anticipatory / consequence bearing\n  of an already formed position;\n  exact necessary / sufficient conditions OPEN.",
    "Bearer\n= canonically routed as an already formed One / Selection-position satisfying\n  P prospective self-indexing + E same-One prospective exposure at semantic / architectural strength;\n  a universal formal / empirical cross-domain N&S theorem remains OPEN.",
)

replace_once(
    "Post-#942 routing:",
    "Post-#947 routing:",
)

replace_between(
    "### 20. Canonical authority chain",
    "### 21. Publication carve-outs",
    """### 20. Canonical authority chain

For exact registered meanings and current cross-owner order:

1. `CANONICAL_REGISTRY.md` — find the registered route
2. `Core_Law/SRT_Generative_Ontology_Spine.md` — cross-owner generation order, non-identities and OPEN gates
3. `Governance/SRT_CLAIM_LADDER.md` / `Governance/SRT_CLAIM_MODE_AUDIT.md` — claim hardness / demotion state
4. local owners such as `Core_Law/SRT_L0_Metaphysics.md`, `Core_Law/SRT_One_Formation.md`, P1-T06, `_SRT_D_VALUE_CANONICAL.md`, `_SRT_PSI_F_CANONICAL.md`, `_SRT_T_DIR_CANONICAL.md`, `Core/SRT_Core_22_Equations.md`
5. bridge / domain / reader surfaces only within the scope permitted by the above

`STATUS.md` is routing / programme state, not definition authority.

If an older local canonical surface conflicts with the new spine at the cross-layer inference level, preserve any compatible local content but route the conflict into canonical cleanup rather than allowing historical status to override the new spine.""",
)

replace_once(
    "For current R1 work, load `Core_Law/SRT_One_Formation.md` and the #941 A/O3 author adjudication first; then load the #938 final supersession / Bearer reconciliation before #931/#933 historical Bearer routing.",
    "For current ontology / cleanup work, load `Core_Law/SRT_Generative_Ontology_Spine.md` first, then its local owners and claim-hardness governance. Historical #931/#933/#938 material is provenance and only controls where not superseded by #947 or later explicit author decisions.",
)

replace_once(
    "#938 remains a merged noncanonical reconstruction checkpoint; #940 and #942 are the bounded canonical landings derived from later author/governance gates. #942 does not authorize Bearer, subjecthood, phenomenality, `d`, `sigma`, `T_dir`, or collective-subject closure beyond its explicit scope.",
    "#947 is now the controlling cross-owner canonical spine. #940/#942 remain compatible local landings; #938 remains a noncanonical reconstruction checkpoint. #947 canonically fixes the P+E Bearer semantic route but does not close Bearer->actual 承担 / concern / agency / subject / cognition / phenomenality, nor does it re-ratify every historical L0 primitive or downstream canonical claim.",
)

replace_once(
    "Bearer necessary conditions;\nBearer sufficient conditions;",
    "formal cross-domain necessary-and-sufficient theorem for P+E Bearer;\nunique empirical / numerical Bearer admission threshold;",
)

replace_between(
    "## Immediate routing",
    "## Historical navigation",
    """## Immediate routing

```text
1. treat #947 / `SRT_Generative_Ontology_Spine.md` as the current cross-owner canonical audit standard;
2. keep local owners only for scope-compatible local definitions;
3. start old-canonical reverse audit from the spine rather than from historical canonical authority;
4. audit first: actual canonical anchors / L0 downstream overreach / primitive placement;
5. then re-audit Individuation / sigma subject gate, using the pre-#947 B1 branch only as candidate patch material;
6. then audit Stable-ISP / Suffering / Occlusion shortcuts and d / T_dir / Psi_f circular imports;
7. then propagate cleanup into Collective / AI / Philosophy and remove duplicate reader / argument / alignment authority;
8. prefer KEEP | RETYPE | DEMOTE | RETIRE | MERGE | SIMPLIFY | OPEN; do not invent replacement theorems to fill retired claims;
9. preserve Level 2 HOLD, no new Level 1, and no scientific-distinctiveness promotion unless separately earned.
```

""",
)

p.write_text(text, encoding="utf-8")
print("post-#947 STATUS closeout applied")
