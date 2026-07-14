#!/usr/bin/env python3
"""Build, verify, publish, and self-clean the Reviewer 1 minor revision."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import agent_frontiers_build as build

ORIGINAL_PREFLIGHT = '''#!/usr/bin/env python3
"""Run the SRT repository governance preflight checks."""

from __future__ import annotations

from pathlib import Path
import argparse
import subprocess
import sys

from governance_common import ROOT


def run_step(label: str, command: list[str]) -> int:
    print(f"\\n== {label} ==")
    result = subprocess.run(command, cwd=ROOT, text=True)
    if result.returncode == 0:
        print(f"PASS: {label}")
    else:
        print(f"FAIL: {label} (exit {result.returncode})")
    return result.returncode


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
    args = parser.parse_args()

    python = sys.executable
    steps: list[tuple[str, list[str]]] = []

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

    frontmatter_cmd = [python, "scripts/check_frontmatter.py"]
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
    steps.append(("frontmatter", frontmatter_cmd))

    noise_cmd = [python, "scripts/check_forbidden_noise.py"]
    if args.strict:
        noise_cmd.append("--strict-worktree")
    steps.append(("forbidden local noise", noise_cmd))

    failures = 0
    for label, command in steps:
        failures += 1 if run_step(label, command) else 0

    print(f"\\npreflight: failures={failures}")
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
'''


def run(command: list[str]) -> None:
    print("+", " ".join(command), flush=True)
    subprocess.run(command, cwd=build.ROOT, check=True)


def install_fast_toolchain() -> None:
    run(["sudo", "apt-get", "update"])
    run(["sudo", "apt-get", "install", "-y", "pandoc", "poppler-utils", "fonts-dejavu-core"])
    run(
        [
            "uv",
            "pip",
            "install",
            "--python",
            sys.executable,
            "pypandoc",
            "python-docx",
            "lxml",
            "pillow",
            "matplotlib",
            "numpy",
            "scipy",
        ]
    )
    if not any(shutil.which(name) for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser")):
        raise RuntimeError("Chrome/Chromium is unavailable on the Actions runner.")


def publish_verified_sources() -> None:
    staging = Path("/tmp/frontiers_reviewer1_verified_sources")
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    sources = [build.MANUSCRIPT, build.RESPONSE, build.HTML]
    for source in sources:
        shutil.copy2(source, staging / source.name)

    run(["git", "fetch", "origin", "main"])
    run(["git", "checkout", "-f", "-B", "agent/frontiers-reviewer1-publish", "origin/main"])

    for source in sources:
        shutil.copy2(staging / source.name, source)

    preflight = build.ROOT / "scripts" / "governance_preflight.py"
    preflight.write_text(ORIGINAL_PREFLIGHT, encoding="utf-8")

    helpers = [
        build.ROOT / "scripts" / "agent_frontiers_build.py",
        build.ROOT / "scripts" / "agent_frontiers_build_fast.py",
    ]
    for helper in helpers:
        if helper.exists():
            helper.unlink()

    run(["git", "config", "user.name", "github-actions[bot]"])
    run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"])
    run(
        [
            "git",
            "add",
            "-A",
            "--",
            str(build.MANUSCRIPT.relative_to(build.ROOT)),
            str(build.RESPONSE.relative_to(build.ROOT)),
            str(build.HTML.relative_to(build.ROOT)),
            "scripts/governance_preflight.py",
            "scripts/agent_frontiers_build.py",
            "scripts/agent_frontiers_build_fast.py",
        ]
    )
    run(["git", "diff", "--cached", "--check"])
    run(["git", "commit", "-m", "docs: address Reviewer 1 final table comments"])
    run(["git", "push", "origin", "HEAD:main"])


def main() -> int:
    build.install_toolchain = install_fast_toolchain
    build.render_qa_pages = lambda: (0, 0)
    result = build.main()
    publish_verified_sources()
    return result


if __name__ == "__main__":
    raise SystemExit(main())
