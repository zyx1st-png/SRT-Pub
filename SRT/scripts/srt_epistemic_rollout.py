#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


BRIDGE_NOTE = (
    "> **Bridge Layer Note**\n"
    "> 本文件按 `Bridge` 层处理：主要承担互译、比较、接口重写与边界说明，"
    "不应直接读成“已被外部经验验证的胜出理论”。若文中使用 `Axiom`、`Theorem`、"
    "`Corollary` 等强标签，默认理解为框架内翻译命题，除非另有独立经验锚定。"
)


@dataclass(frozen=True)
class Classification:
    layer: str
    mode: str
    add_bridge_note: bool = False


def iter_md_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.md"):
        if ".venv" in path.parts or path.parts[0] in {"data", "papers"}:
            continue
        yield path


def has_frontmatter(text: str) -> bool:
    return text.startswith("---\n") and "\n---\n" in text[4:]


def split_frontmatter(text: str) -> tuple[str, str]:
    _, rest = text.split("---\n", 1)
    frontmatter, body = rest.split("\n---\n", 1)
    return frontmatter, body


def classify(path: Path) -> Classification | None:
    p = str(path)
    name = path.name

    if p == "Governance/SRT_LAB_HYPOTHESES.md" or name.startswith("SRT_EXP_") or "Experimental" in name or "Experiments" in name:
        return Classification("lab", "canonical")

    bridge_tokens = [
        "Bridge",
        "Comparison",
        "Clin_",
        "Alignment",
        "Not_PreferredPriors",
        "Override",
        "Interface",
        "_Batch",
        "Luhmann_ANT",
        "Language_Eco",
        "PP_ALIGNMENT",
    ]
    if any(token in p or token in name for token in bridge_tokens):
        return Classification("bridge", "translation", not name.startswith("README"))
    if any(seg in p for seg in ("/Foundations_Annex/", "/Ontology_Annex/", "/Dynamics_Scaling_Annex/")):
        return Classification("bridge", "translation", not name.startswith("README"))

    if p.startswith("memory/") or p == "STATUS.md":
        return Classification("os", "evidence")

    return Classification("os", "canonical")


def update_frontmatter(frontmatter: str, classification: Classification) -> tuple[str, bool]:
    lines = frontmatter.splitlines()
    changed = False

    has_epistemic = any(line.startswith("epistemic_layer:") for line in lines)
    has_claim = any(line.startswith("claim_mode:") for line in lines)
    if has_epistemic and has_claim:
        return frontmatter, False

    status_idx = next((i for i, line in enumerate(lines) if line.startswith("status:")), None)
    dependency_idx = next((i for i, line in enumerate(lines) if line.startswith("dependency:")), None)
    insert_idx = len(lines)
    if status_idx is not None:
        insert_idx = status_idx + 1
    elif dependency_idx is not None:
        insert_idx = dependency_idx

    inserts = []
    if not has_epistemic:
        inserts.append(f"epistemic_layer: {classification.layer}")
    if not has_claim:
        inserts.append(f"claim_mode: {classification.mode}")

    if inserts:
        lines[insert_idx:insert_idx] = inserts
        changed = True

    return "\n".join(lines), changed


def add_bridge_note(body: str) -> tuple[str, bool]:
    if "Bridge Layer Note" in body or "Bridge Note" in body:
        return body, False

    lines = body.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("# "):
            insert_at = i + 1
            note_lines = ["", BRIDGE_NOTE, ""]
            lines[insert_at:insert_at] = note_lines
            return "\n".join(lines), True

    return BRIDGE_NOTE + "\n\n" + body, True


def process_file(path: Path, write: bool) -> tuple[bool, bool]:
    text = path.read_text()
    if not has_frontmatter(text):
        return False, False

    classification = classify(path)
    if classification is None:
        return False, False

    frontmatter, body = split_frontmatter(text)
    new_frontmatter, frontmatter_changed = update_frontmatter(frontmatter, classification)
    body_changed = False

    if classification.add_bridge_note:
        body, body_changed = add_bridge_note(body)

    if not frontmatter_changed and not body_changed:
        return False, False

    new_text = f"---\n{new_frontmatter}\n---\n{body}"
    if write:
        path.write_text(new_text)
    return frontmatter_changed, body_changed


def main() -> None:
    parser = argparse.ArgumentParser(description="Roll out epistemic layer metadata and bridge notes across SRT markdown files.")
    parser.add_argument("--write", action="store_true", help="Apply changes in place.")
    args = parser.parse_args()

    root = Path(".")
    fm_count = 0
    note_count = 0
    touched = 0

    for path in iter_md_files(root):
        frontmatter_changed, body_changed = process_file(path, write=args.write)
        if frontmatter_changed or body_changed:
            touched += 1
            fm_count += int(frontmatter_changed)
            note_count += int(body_changed)
            print(f"{path}\tfrontmatter={int(frontmatter_changed)}\tbridge_note={int(body_changed)}")

    print(f"\nTouched: {touched}")
    print(f"Frontmatter updates: {fm_count}")
    print(f"Bridge notes added: {note_count}")


if __name__ == "__main__":
    main()
