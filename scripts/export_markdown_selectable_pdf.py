#!/usr/bin/env python3
"""Render a Markdown file to a selectable-text PDF via HTML and Chrome."""

from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")


CSS = """
@page {
  size: A5;
  margin: 22mm 17mm 20mm 17mm;
}

html {
  color: #171717;
  font-family: "Songti SC", "PingFang SC", "Noto Serif CJK SC", serif;
  font-size: 10.7pt;
  line-height: 1.72;
}

body {
  margin: 0;
}

h1 {
  break-before: page;
  font-family: "Songti SC", "PingFang SC", serif;
  font-size: 20pt;
  line-height: 1.32;
  font-weight: 700;
  margin: 0 0 12mm;
  text-align: center;
}

body > h1:first-child {
  break-before: auto;
  margin-top: 32mm;
  margin-bottom: 10mm;
}

h2 {
  font-size: 14.5pt;
  line-height: 1.45;
  margin: 11mm 0 4mm;
}

h3 {
  font-size: 12.5pt;
  margin: 8mm 0 3mm;
}

p {
  margin: 0 0 4.2mm;
  text-align: justify;
}

blockquote {
  margin: 5mm 0 6mm;
  padding-left: 4mm;
  border-left: 1.4mm solid #d7d7d7;
  color: #333;
}

ul, ol {
  margin: 0 0 5mm 0;
  padding-left: 7mm;
}

li {
  margin-bottom: 1.4mm;
}

table {
  border-collapse: collapse;
  width: 100%;
  margin: 5mm 0 7mm;
  font-size: 8.4pt;
}

th, td {
  border: 0.3pt solid #aaa;
  padding: 1.6mm 1.8mm;
  vertical-align: top;
}

th {
  background: #f2f2f2;
}

a {
  color: inherit;
  text-decoration: none;
}

.footnote-back {
  display: none;
}

code {
  font-family: "SF Mono", Menlo, monospace;
  font-size: 0.92em;
}

pre {
  white-space: pre-wrap;
  border: 0.3pt solid #d0d0d0;
  background: #f7f7f7;
  padding: 3mm;
  font-size: 8.8pt;
}
"""


def run(args: list[str]) -> None:
    completed = subprocess.run(args, cwd=ROOT)
    if completed.returncode:
        raise SystemExit(completed.returncode)


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    markdown = args.markdown
    if not markdown.exists():
        raise FileNotFoundError(markdown)
    output = (args.output or markdown.with_suffix(".pdf")).resolve()

    if not CHROME.exists():
        raise FileNotFoundError(f"Google Chrome not found: {CHROME}")

    with tempfile.TemporaryDirectory(prefix="srt-selectable-pdf-") as tmpdir:
        tmp = Path(tmpdir)
        css = tmp / "book.css"
        html = tmp / "book.html"
        css.write_text(CSS, encoding="utf-8")
        run(
            [
                "pandoc",
                "--standalone",
                "--from",
                "markdown+raw_tex",
                "--metadata",
                "title=从存在到秩序",
                "--css",
                str(css),
                "--wrap=none",
                str(markdown),
                "-o",
                str(html),
            ]
        )
        run(
            [
                str(CHROME),
                "--headless",
                "--disable-gpu",
                "--no-pdf-header-footer",
                "--print-to-pdf=" + str(output),
                "file://" + str(html),
            ]
        )

    print(output.relative_to(ROOT))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
