#!/usr/bin/env python3
"""Audit frontmatter only in files changed by the current pull request."""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path

from check_frontmatter import (
    BASELINE_FILES,
    STATUS_RATCHET_ENUM,
    is_frontmatter_exempt,
    is_helper_path,
    load_baseline,
    missing_recommended_keys,
)
from governance_common import ROOT, frontmatter_for, iter_markdown, print_summary, relpath


def resolve_base_ref(base_ref: str) -> str:
    candidates = [base_ref]
    if not base_ref.startswith("origin/"):
        candidates.append(f"origin/{base_ref}")
    for candidate in candidates:
        result = subprocess.run(
            ["git", "rev-parse", "--verify", "--quiet", candidate],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        if result.returncode == 0:
            return candidate
    raise ValueError(
        f"cannot resolve base ref `{base_ref}`; fetch the base branch or pass --base-ref explicitly"
    )


def changed_relpaths(base_ref: str) -> set[str]:
    result = subprocess.run(
        [
            "git",
            "diff",
            "--name-only",
            "--diff-filter=ACMRT",
            f"{base_ref}...HEAD",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip() or "unknown git diff error"
        raise RuntimeError(f"failed to compute changed files against `{base_ref}`: {detail}")
    return {line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()}


def status_fix_suggestions(status_value: str, data: dict[str, str]) -> list[str]:
    if not status_value or status_value in STATUS_RATCHET_ENUM:
        return []

    versioned = re.fullmatch(
        r"(draft|active|frozen|archived)[_-](v\d+(?:[._-]\d+)*)",
        status_value,
    )
    if versioned:
        lifecycle, version = versioned.groups()
        return [f"status: {lifecycle}", f"version: {version}"]

    patch_version = re.fullmatch(r"patch[_-](v.+)", status_value)
    if patch_version:
        suggestions = ["status: active", f"version: {patch_version.group(1)}"]
        if not data.get("type"):
            suggestions.append("type: material_patch")
        return suggestions

    if status_value == "patch":
        suggestions = ["status: active"]
        if not data.get("type"):
            suggestions.append("type: material_patch")
        return suggestions

    if status_value == "source_card":
        suggestions = ["status: active"]
        if not data.get("type"):
            suggestions.append("type: material_source_card")
        return suggestions

    if re.fullmatch(r"preprint[_-]v.+", status_value):
        return ["status: active", f"source_stage: {status_value}"]

    if status_value.startswith("author_confirmed_"):
        return ["status: active", f"record_stage: {status_value}"]

    return [
        "status: <draft|active|frozen|archived>",
        f"record_stage: {status_value}",
    ]


def baseline_for_scope(baseline: set[str], scoped_rels: set[str]) -> set[str]:
    scoped = set()
    for item in baseline:
        if any(
            item.startswith(f"{rel}:")
            or f": {rel} /" in item
            or f" / {rel}" in item
            for rel in scoped_rels
        ):
            scoped.add(item)
    return scoped


def duplicate_id_warnings(all_paths: list[Path], scoped_rels: set[str]) -> list[str]:
    warnings: list[str] = []
    ids: dict[str, str] = {}
    for path in all_paths:
        rel = relpath(path)
        if rel in BASELINE_FILES or is_frontmatter_exempt(rel):
            continue
        fm = frontmatter_for(path)
        if fm is None or fm.malformed:
            continue
        file_id = fm.data.get("id")
        if not file_id:
            continue
        previous = ids.get(file_id)
        if previous and previous != rel:
            if previous in scoped_rels or rel in scoped_rels:
                warnings.append(f"duplicate frontmatter id `{file_id}`: {previous} / {rel}")
        ids[file_id] = rel
    return warnings


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref", default="main")
    parser.add_argument("--include-artifacts", action="store_true")
    parser.add_argument(
        "--baseline",
        default="Governance/Frontmatter_Warning_Baseline.txt",
    )
    parser.add_argument("--fail-on-new-warnings", action="store_true")
    parser.add_argument("--suggest-fixes", action="store_true")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    suggestions: list[str] = []

    try:
        resolved = resolve_base_ref(args.base_ref)
        changed = changed_relpaths(resolved)
    except (ValueError, RuntimeError) as exc:
        print_summary("frontmatter_changed", [str(exc)], [])
        raise SystemExit(1)

    all_paths = iter_markdown(include_artifacts=args.include_artifacts)
    by_rel = {relpath(path): path for path in all_paths}
    target_paths = [by_rel[item] for item in sorted(changed) if item in by_rel]
    print(f"frontmatter_scope: mode=changed base={resolved} files={len(target_paths)}")

    for path in target_paths:
        rel = relpath(path)
        if rel in BASELINE_FILES or is_frontmatter_exempt(rel):
            continue
        fm = frontmatter_for(path)
        if fm is None:
            warnings.append(f"{rel}: missing frontmatter")
            suggestions.append(
                f"{rel}: add YAML frontmatter with id, type, status, layer, "
                "epistemic_layer, and claim_mode"
            )
            continue
        if fm.malformed:
            errors.append(f"{rel}: malformed frontmatter fence")
            suggestions.append(f"{rel}: close the opening YAML block with a standalone `---`")
            continue

        missing = missing_recommended_keys(fm.data)
        if missing:
            warnings.append(
                f"{rel}: missing recommended frontmatter keys: {', '.join(missing)}"
            )
            suggestions.append(f"{rel}: add missing keys: {', '.join(missing)}")

        status_value = fm.data.get("status", "")
        if status_value and status_value not in STATUS_RATCHET_ENUM:
            warnings.append(
                f"{rel}: status `{status_value}` outside ratchet enum "
                "(draft|active|frozen|archived)"
            )
            repair = "; add ".join(status_fix_suggestions(status_value, fm.data))
            suggestions.append(f"{rel}: replace overloaded status; use {repair}")

        if is_helper_path(rel):
            claim_mode = fm.data.get("claim_mode", "")
            canonical = fm.data.get("canonical", "")
            if canonical.lower() == "true":
                errors.append(f"{rel}: helper-layer file declares canonical: true")
            if claim_mode == "canonical":
                warnings.append(f"{rel}: helper-layer file uses claim_mode: canonical")

    warnings.extend(duplicate_id_warnings(all_paths, changed))

    try:
        baseline = baseline_for_scope(load_baseline(args.baseline), changed)
    except FileNotFoundError as exc:
        errors.append(f"baseline file missing: {exc}")
        baseline = set()

    current = set(warnings)
    new_warnings = sorted(current - baseline)
    retired_warnings = sorted(baseline - current)
    known_count = len(current & baseline)
    print(
        "frontmatter_baseline: "
        f"known={known_count} new={len(new_warnings)} retired={len(retired_warnings)}"
    )
    if args.fail_on_new_warnings:
        errors.extend(f"new frontmatter warning: {item}" for item in new_warnings)
        display_warnings: list[str] = []
    else:
        display_warnings = new_warnings

    print_summary("frontmatter_changed", errors, display_warnings)
    if args.suggest_fixes:
        for item in sorted(set(suggestions)):
            print(f"SUGGESTION: {item}")
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
