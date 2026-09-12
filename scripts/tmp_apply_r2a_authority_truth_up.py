#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: str, old: str, new: str) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"anchor not found in {path}: {old[:120]!r}")
    if text.count(old) != 1:
        raise SystemExit(f"anchor not unique in {path}: count={text.count(old)}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")


# F1: remove the duplicate full authority chain from bootstrap read #1.
replace_once(
    "SRT_AI_START.md",
    """When exact **current registered** meanings are required, still follow the existing authority chain:\n\n1. `CANONICAL_REGISTRY.md`\n2. `Governance/SRT_CLAIM_LADDER.md`\n3. `Governance/SRT_CLAIM_MODE_AUDIT.md`\n4. `Core_Law/SRT_L0_Metaphysics.md`\n5. `Core/SRT_Core_21_Minimal_Axioms.md`\n6. `Core/SRT_Core_21b_Constitutive_Theorems.md`\n7. `_SRT_D_VALUE_CANONICAL.md`\n8. `_SRT_PSI_F_CANONICAL.md`\n9. `_SRT_T_DIR_CANONICAL.md`\n10. `_SRT_CROSS_DOMAIN_MATRIX.md`\n11. `Core/SRT_Core_22_Equations.md`\n12. `_SRT_SYMBOL_TABLE.md`\n13. `Core/SRT_Core_21_Formal_Axioms.md`\n14. `Core/SRT_Core_21c_Bridge_Hypotheses.md`\n\nThis list records present repository authority. A later Core/Core_Law role-reclassification audit will decide what should remain constitutional source, commentary, domain formalization, operational proxy or historical formalization.\n""",
    """When exact **current registered** meanings are required, do **not** maintain or infer a second complete authority chain from this bootstrap file. Follow `CANONICAL_REGISTRY.md §C` as the single complete citation-priority owner.\n\nFor current cross-owner ontology generation order, non-identities, and OPEN routing, consult `Core_Law/SRT_Generative_Ontology_Spine.md` after the Registry and before compatible local owners. Local owners retain their detailed definitions only where compatible with that routing.\n\nThis runtime entry is a projection of the Registry, not an independent authority list. A later Core/Core_Law role-reclassification audit may still retype local owners without changing this single-source rule.\n""",
)

# F10: Claude compatibility layer must defer rather than restate a stale hierarchy.
replace_once(
    "CLAUDE.md",
    """## 权威层级\n\n默认优先级：\n\n1. [CANONICAL_REGISTRY.md](CANONICAL_REGISTRY.md)\n2. [Core_Law/SRT_L0_Metaphysics.md](Core_Law/SRT_L0_Metaphysics.md)\n3. [_SRT_D_VALUE_CANONICAL.md](_SRT_D_VALUE_CANONICAL.md)\n4. [_SRT_PSI_F_CANONICAL.md](_SRT_PSI_F_CANONICAL.md)\n5. [_SRT_T_DIR_CANONICAL.md](_SRT_T_DIR_CANONICAL.md)\n6. [_SRT_SYMBOL_TABLE.md](_SRT_SYMBOL_TABLE.md)\n7. [Core/SRT_Core_21_Formal_Axioms.md](Core/SRT_Core_21_Formal_Axioms.md)\n8. [Core/SRT_Core_22_Equations.md](Core/SRT_Core_22_Equations.md)\n\n""",
    """## 权威层级\n\n本兼容层**不维护第二套完整权威链**。精确的当前引用优先级唯一回链 [CANONICAL_REGISTRY.md](CANONICAL_REGISTRY.md) §C。涉及跨 owner 的本体生成顺序、非同一性与 OPEN gate 时，在 Registry 之后优先读取 [Core_Law/SRT_Generative_Ontology_Spine.md](Core_Law/SRT_Generative_Ontology_Spine.md)，再进入兼容的局部 owner。\n\n""",
)

# F10: manifest exposes the cross-owner owner explicitly.
replace_once(
    "_SRT_MANIFEST.yaml",
    "canonical_anchors:\n  l0: \"Core_Law/SRT_L0_Metaphysics.md\"\n",
    "canonical_anchors:\n  generative_spine: \"Core_Law/SRT_Generative_Ontology_Spine.md\"\n  l0: \"Core_Law/SRT_L0_Metaphysics.md\"\n",
)

# F10: theory-advancement retrieval must load the spine before local claim surfaces.
replace_once(
    "_SRT_AGENT_RETRIEVAL_PROFILE.md",
    """Read:\n\n1. `CANONICAL_REGISTRY.md`\n2. `Governance/SRT_CLAIM_LADDER.md`\n3. `Governance/SRT_CLAIM_MODE_AUDIT.md`\n4. `_SRT_CONTEXT_ROUTER.md`\n5. `_SRT_DEEP_THEORY_MAP.md`\n6. the route's Primary files\n7. the route's Secondary files when domain depth is needed\n8. `Core/SRT_OPEN_TENSIONS.md`\n9. the relevant coverage index when the route may miss support files\n""",
    """Read:\n\n1. `CANONICAL_REGISTRY.md`\n2. `Core_Law/SRT_Generative_Ontology_Spine.md` when the task touches ontology order, formation, position/perspective/Bearer routing, or old-canonical cleanup\n3. `Governance/SRT_CLAIM_LADDER.md`\n4. `Governance/SRT_CLAIM_MODE_AUDIT.md`\n5. `_SRT_CONTEXT_ROUTER.md`\n6. `_SRT_DEEP_THEORY_MAP.md`\n7. the route's Primary files\n8. the route's Secondary files when domain depth is needed\n9. `Core/SRT_OPEN_TENSIONS.md`\n10. the relevant coverage index when the route may miss support files\n""",
)

# F10: runtime overlay names the Registry and the cross-owner owner without duplicating the full chain.
replace_once(
    "AGENTS.md",
    """3. `STATUS.md §Fast Status` — compact current status; note that the 2026-09-05 author-reentry amendment below supersedes stale bearer-totalizing / direct-to-increment programme wording.\n\n### Current programme expansion — Author Re-entry + Constitution + Domain Reconstruction\n""",
    """3. `STATUS.md §Fast Status` — compact current status; note that the 2026-09-05 author-reentry amendment below supersedes stale bearer-totalizing / direct-to-increment programme wording.\n\nAuthority routing is single-source: use `CANONICAL_REGISTRY.md §C` for the complete current citation priority. For ontology-order / canonical-cleanup work, load `Core_Law/SRT_Generative_Ontology_Spine.md` after the Registry and before compatible local owners; do not reconstruct a competing complete authority chain in runtime files.\n\n### Current programme expansion — Author Re-entry + Constitution + Domain Reconstruction\n""",
)
replace_once(
    "AGENTS.md",
    """## Canonical Runtime Paths\n\n- AI 最小首读入口：`SRT_AI_START.md`\n""",
    """## Canonical Runtime Paths\n\n- 完整 canonical 引用优先级唯一 owner：`CANONICAL_REGISTRY.md §C`\n- 跨 owner 本体生成主轴：`Core_Law/SRT_Generative_Ontology_Spine.md`\n- AI 最小首读入口：`SRT_AI_START.md`\n""",
)

# F4: use the current canonical labels; keep A3 only as historical provenance outside the Registry.
replace_once(
    "CANONICAL_REGISTRY.md",
    "- typed layering：One-level endogenous perspective、A1/A2/A3 anticipation 分层须保留；`all Ones automatically perspective-bearing` 仍未建立。\n",
    "- typed layering：One-level endogenous perspective、A1/A2/P/E 分层须保留；`all Ones automatically perspective-bearing` 仍未建立。历史 `A3` 仅作为 R1 gate lineage 标签，不作为当前 canonical token。\n",
)

# F6: only the spine owns the cross-owner canonical order; One Formation owns local elaboration.
replace_once(
    "Core_Law/SRT_One_Formation.md",
    """## §0. Formation order\n\nThe canonical order is:\n""",
    """## §0. Local One-formation elaboration\n\nWithin the cross-owner trunk fixed by `Core_Law/SRT_Generative_Ontology_Spine.md`, the local One-formation segment is:\n""",
)
replace_once(
    "Core_Law/SRT_One_Formation.md",
    "This order preserves the L0 rule that Selection does not require a pre-existing chooser.",
    "This local elaboration preserves the L0 rule that Selection does not require a pre-existing chooser.",
)

# F8: prevent extraction of P+E without the formed-One precondition.
replace_once(
    "Core_Law/SRT_Generative_Ontology_Spine.md",
    "P + E -> Bearer.\n",
    "formed One / Selection-position + P + E -> Bearer.\n",
)

# F11: permanent regression checker.
checker = ROOT / "scripts/check_authority_routing.py"
checker.write_text('''#!/usr/bin/env python3\n"""Fail when runtime/canonical routing drifts away from the Registry + generative spine single-source rule."""\nfrom pathlib import Path\nimport sys\n\nROOT = Path(__file__).resolve().parents[1]\n\ndef read(path):\n    return (ROOT / path).read_text(encoding="utf-8")\n\nchecks = []\n\ndef require(path, needle):\n    text = read(path)\n    if needle not in text:\n        checks.append(f"{path}: missing required routing marker: {needle}")\n\ndef forbid(path, needle):\n    text = read(path)\n    if needle in text:\n        checks.append(f"{path}: forbidden duplicate/stale routing marker remains: {needle}")\n\nrequire("SRT_AI_START.md", "CANONICAL_REGISTRY.md §C")\nrequire("SRT_AI_START.md", "Core_Law/SRT_Generative_Ontology_Spine.md")\nforbid("SRT_AI_START.md", "follow the existing authority chain")\n\nrequire("CLAUDE.md", "CANONICAL_REGISTRY.md")\nrequire("CLAUDE.md", "SRT_Generative_Ontology_Spine.md")\nforbid("CLAUDE.md", "默认优先级：")\n\nrequire("_SRT_MANIFEST.yaml", 'generative_spine: "Core_Law/SRT_Generative_Ontology_Spine.md"')\nrequire("_SRT_AGENT_RETRIEVAL_PROFILE.md", "Core_Law/SRT_Generative_Ontology_Spine.md")\nrequire("AGENTS.md", "完整 canonical 引用优先级唯一 owner")\nrequire("AGENTS.md", "跨 owner 本体生成主轴")\n\nrequire("CANONICAL_REGISTRY.md", "A1/A2/P/E")\nforbid("CANONICAL_REGISTRY.md", "A1/A2/A3 anticipation")\n\nrequire("Core_Law/SRT_One_Formation.md", "cross-owner trunk fixed by `Core_Law/SRT_Generative_Ontology_Spine.md`")\nforbid("Core_Law/SRT_One_Formation.md", "The canonical order is:")\n\nrequire("Core_Law/SRT_Generative_Ontology_Spine.md", "formed One / Selection-position + P + E -> Bearer.")\nforbid("Core_Law/SRT_Generative_Ontology_Spine.md", "\\nP + E -> Bearer.\\n")\n\nif checks:\n    print("authority-routing consistency: FAIL")\n    for item in checks:\n        print(f"- {item}")\n    raise SystemExit(1)\n\nprint("authority-routing consistency: PASS")\n''', encoding="utf-8")

# Hook the checker into governance preflight immediately after registry consistency.
replace_once(
    "scripts/governance_preflight.py",
    """    steps.append((\"registry consistency\", registry_cmd))\n\n    if (ROOT / \"scripts\" / \"check_material_log_consistency.py\").is_file():\n""",
    """    steps.append((\"registry consistency\", registry_cmd))\n\n    if (ROOT / \"scripts\" / \"check_authority_routing.py\").is_file():\n        steps.append(\n            (\"authority-routing consistency\", [python, \"scripts/check_authority_routing.py\"])\n        )\n\n    if (ROOT / \"scripts\" / \"check_material_log_consistency.py\").is_file():\n""",
)

print("R2-A authority truth-up applied")
