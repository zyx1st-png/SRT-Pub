#!/usr/bin/env python3
"""Fail when runtime/canonical routing drifts away from the Registry + generative spine single-source rule."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return (ROOT / path).read_text(encoding="utf-8")

checks = []

def require(path, needle):
    text = read(path)
    if needle not in text:
        checks.append(f"{path}: missing required routing marker: {needle}")

def forbid(path, needle):
    text = read(path)
    if needle in text:
        checks.append(f"{path}: forbidden duplicate/stale routing marker remains: {needle}")

require("SRT_AI_START.md", "CANONICAL_REGISTRY.md §C")
require("SRT_AI_START.md", "Core_Law/SRT_Generative_Ontology_Spine.md")
forbid("SRT_AI_START.md", "follow the existing authority chain")

require("CLAUDE.md", "CANONICAL_REGISTRY.md")
require("CLAUDE.md", "SRT_Generative_Ontology_Spine.md")
forbid("CLAUDE.md", "默认优先级：")

require("_SRT_MANIFEST.yaml", 'generative_spine: "Core_Law/SRT_Generative_Ontology_Spine.md"')
require("_SRT_AGENT_RETRIEVAL_PROFILE.md", "Core_Law/SRT_Generative_Ontology_Spine.md")
require("AGENTS.md", "完整 canonical 引用优先级唯一 owner")
require("AGENTS.md", "跨 owner 本体生成主轴")

require("CANONICAL_REGISTRY.md", "A1/A2/P/E")
forbid("CANONICAL_REGISTRY.md", "A1/A2/A3 anticipation")

require("Core_Law/SRT_One_Formation.md", "cross-owner trunk fixed by `Core_Law/SRT_Generative_Ontology_Spine.md`")
forbid("Core_Law/SRT_One_Formation.md", "The canonical order is:")

require("Core_Law/SRT_Generative_Ontology_Spine.md", "formed One / Selection-position + P + E -> Bearer.")
forbid("Core_Law/SRT_Generative_Ontology_Spine.md", "\nP + E -> Bearer.\n")

if checks:
    print("authority-routing consistency: FAIL")
    for item in checks:
        print(f"- {item}")
    raise SystemExit(1)

print("authority-routing consistency: PASS")
