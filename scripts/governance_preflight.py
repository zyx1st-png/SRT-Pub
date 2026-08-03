#!/usr/bin/env python3
"""Run the SRT repository governance preflight checks."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys

from governance_common import ROOT


def run_step(label: str, command: list[str]) -> dict[str, object]:
    print(f"\n== {label} ==")
    result = subprocess.run(command, cwd=ROOT, text=True)
    if result.returncode == 0:
        print(f"PASS: {label}")
    else:
        print(f"FAIL: {label} (exit {result.returncode})")
    return {
        "label": label,
        "command": command,
        "returncode": result.returncode,
        "status": "pass" if result.returncode == 0 else "fail",
    }


def step_failed(results: list[dict[str, object]], label: str) -> bool | None:
    for result in results:
        if result["label"] == label:
            return result["returncode"] != 0
    return None


def write_json(path_arg: str, payload: dict[str, object]) -> None:
    path = ROOT / path_arg
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="Escalate warning-prone checks.")
    parser.add_argument(
        "--strict-split-metadata",
        action="store_true",
        help="Require source-owner SHA metadata without enabling all strict checks.",
    )
    parser.add_argument(
        "--frontmatter-baseline",
        default="Governance/Frontmatter_Warning_Baseline.txt",
        help="Known frontmatter warning baseline.",
    )
    parser.add_argument("--no-frontmatter-baseline", action="store_true")
    parser.add_argument("--skip-write-report", action="store_true")
    parser.add_argument(
        "--base-ref",
        help="Base branch SHA/ref for PR-local governance attribution.",
    )
    parser.add_argument(
        "--json-report",
        default="governance-preflight-summary.json",
        help="Machine-readable preflight summary output.",
    )
    parser.add_argument(
        "--frontmatter-local-json",
        default="frontmatter-pr-local.json",
        help="PR-local frontmatter diagnostic output.",
    )
    parser.add_argument(
        "--frontmatter-repository-json",
        default="frontmatter-repository.json",
        help="Repository-wide frontmatter diagnostic output.",
    )
    args = parser.parse_args()

    python = sys.executable
    steps: list[tuple[str, list[str]]] = []

    if (ROOT / "scripts" / "test_check_frontmatter.py").is_file():
        steps.append(("frontmatter checker tests", [python, "scripts/test_check_frontmatter.py"]))

    if args.base_ref:
        steps.append(
            (
                "frontmatter (PR-local)",
                [
                    python,
                    "scripts/check_frontmatter.py",
                    "--changed-only",
                    "--base-ref",
                    args.base_ref,
                    "--fail-on-warnings",
                    "--check-baseline-nonexpansion",
                    "--baseline-policy-file",
                    args.frontmatter_baseline,
                    "--json-report",
                    args.frontmatter_local_json,
                ],
            )
        )

    audit_cmd = [python, "scripts/audit_large_files.py"]
    if not args.skip_write_report:
        audit_cmd.append("--write-report")
    steps.append(("large-file audit", audit_cmd))

    if (ROOT / "scripts" / "check_book_outline_split.py").is_file():
        steps.append(("book outline split", [python, "scripts/check_book_outline_split.py"]))

    split_cmd = [python, "scripts/check_split_freshness.py"]
    if args.strict or args.strict_split_metadata:
        split_cmd.append("--strict-metadata")
    steps.append(("split freshness", split_cmd))

    registry_cmd = [python, "scripts/check_registry_consistency.py"]
    if args.strict:
        registry_cmd.append("--strict")
    steps.append(("registry consistency", registry_cmd))

    frontmatter_cmd = [
        python,
        "scripts/check_frontmatter.py",
        "--json-report",
        args.frontmatter_repository_json,
    ]
    if args.strict:
        frontmatter_cmd.append("--strict")
    baseline_path = ROOT / args.frontmatter_baseline
    if not args.no_frontmatter_baseline and baseline_path.is_file():
        frontmatter_cmd.extend(
            [
                "--baseline",
                args.frontmatter_baseline,
                "--fail-on-new-warnings",
            ]
        )
    steps.append(("frontmatter (repository)", frontmatter_cmd))

    if (ROOT / "scripts" / "test_check_hooks.py").is_file():
        steps.append(
            ("integration hook checker tests", [python, "scripts/test_check_hooks.py"])
        )

    hooks_cmd = [python, "scripts/check_hooks.py"]
    if args.strict:
        hooks_cmd.append("--strict")
    steps.append(("integration hook closure", hooks_cmd))

    if (ROOT / "scripts" / "test_build_context_bundles.py").is_file():
        steps.append(
            ("context bundle builder tests", [python, "scripts/test_build_context_bundles.py"])
        )

    if (ROOT / "Operations" / "Context_Bundles" / "SRT_CONTEXT_BUNDLE_SPINE.md").is_file():
        steps.append(
            (
                "context bundle freshness",
                [python, "scripts/build_srt_context_bundles.py", "--check"],
            )
        )

    noise_cmd = [python, "scripts/check_forbidden_noise.py"]
    if args.strict:
        noise_cmd.append("--strict-worktree")
    steps.append(("forbidden local noise", noise_cmd))

    results: list[dict[str, object]] = []
    for label, command in steps:
        results.append(run_step(label, command))

    failed_steps = [
        str(result["label"])
        for result in results
        if result["returncode"] != 0
    ]
    local_failed = step_failed(results, "frontmatter (PR-local)")
    repository_frontmatter_failed = step_failed(results, "frontmatter (repository)")

    if local_failed is True:
        failure_scope = "pr_local"
        local_verdict = "dirty"
        main_health = "unknown"
        merge_disposition = "do_not_merge"
    elif repository_frontmatter_failed is True and local_failed is False:
        failure_scope = "base_main"
        local_verdict = "clean"
        main_health = "blocked"
        merge_disposition = "governance_hotfix_only"
    elif failed_steps:
        failure_scope = "repository_check"
        local_verdict = "clean" if local_failed is False else "not_run"
        main_health = "unknown"
        merge_disposition = "do_not_merge"
    else:
        failure_scope = "none"
        local_verdict = "clean" if local_failed is False else "not_run"
        main_health = "healthy"
        merge_disposition = "normal_merge"

    payload = {
        "schema_version": 1,
        "base_ref": args.base_ref,
        "local_verdict": local_verdict,
        "main_health": main_health,
        "merge_disposition": merge_disposition,
        "failure_scope": failure_scope,
        "failed_steps": failed_steps,
        "steps": results,
    }
    write_json(args.json_report, payload)

    print("\n== Governance anti-blocking verdict ==")
    print(f"LOCAL {local_verdict.upper().replace('_', ' ')}")
    print(f"MAIN {main_health.upper().replace('_', ' ')}")
    print(merge_disposition.upper().replace("_", " "))
    print(f"failure_scope={failure_scope}")
    print(f"diagnostic_report={args.json_report}")
    print(f"\npreflight: failures={len(failed_steps)}")
    raise SystemExit(1 if failed_steps else 0)


if __name__ == "__main__":
    main()
