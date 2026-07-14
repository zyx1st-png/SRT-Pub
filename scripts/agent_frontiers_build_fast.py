#!/usr/bin/env python3
"""Run the Frontiers build without remote LibreOffice page rendering.

The generated DOCX and PDF are bundled after text verification. Full page rendering
is performed after the artifact is downloaded into the local document-QA runtime.
"""

from __future__ import annotations

import shutil
import subprocess
import sys

import agent_frontiers_build as build


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


def main() -> int:
    build.install_toolchain = install_fast_toolchain
    build.render_qa_pages = lambda: (0, 0)
    return build.main()


if __name__ == "__main__":
    raise SystemExit(main())
