#!/usr/bin/env python3
"""Create a watermarked PDF from the exported publication Markdown."""

from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path
import subprocess
import sys
import tempfile

from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
EXPORT_DIR = ROOT / "01_Source_Intuition" / "BOOK" / "Exports"
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
  font-size: 9pt;
}

th, td {
  border: 0.3pt solid #aaa;
  padding: 1.7mm 2mm;
  vertical-align: top;
}

th {
  background: #f2f2f2;
}

code {
  font-family: "SF Mono", Menlo, monospace;
  font-size: 0.92em;
}

a {
  color: inherit;
  text-decoration: none;
}

.footnote-back {
  display: none;
}

pre {
  white-space: pre-wrap;
  border: 0.3pt solid #d0d0d0;
  background: #f7f7f7;
  padding: 3mm;
  font-size: 8.8pt;
}

.title {
  text-align: center;
}
"""


def run(args: list[str]) -> None:
    completed = subprocess.run(args, cwd=ROOT)
    if completed.returncode:
        raise SystemExit(completed.returncode)


def create_html(markdown: Path, html: Path, css: Path) -> None:
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


def print_pdf(html: Path, pdf: Path) -> None:
    if not CHROME.exists():
        raise FileNotFoundError(f"Google Chrome not found: {CHROME}")
    run(
        [
            str(CHROME),
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            "--print-to-pdf=" + str(pdf),
            "file://" + str(html),
        ]
    )


def watermark_page(width: float, height: float, text: str, font_path: str) -> Path:
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    tmp.close()
    pdfmetrics.registerFont(TTFont("WatermarkCJK", font_path))
    c = canvas.Canvas(tmp.name, pagesize=(width, height))
    c.saveState()
    c.translate(width / 2, height / 2)
    c.rotate(34)
    c.setFillColor(Color(0.42, 0.42, 0.42, alpha=0.14))
    c.setFont("WatermarkCJK", min(width, height) * 0.105)
    c.drawCentredString(0, 0, text)
    c.restoreState()
    c.save()
    return Path(tmp.name)


def add_watermark(input_pdf: Path, output_pdf: Path, text: str, font_path: str) -> None:
    reader = PdfReader(str(input_pdf))
    writer = PdfWriter()
    cache: dict[tuple[float, float], object] = {}

    for page in reader.pages:
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        key = (width, height)
        if key not in cache:
            wm_path = watermark_page(width, height, text, font_path)
            cache[key] = PdfReader(str(wm_path)).pages[0]
        page.merge_page(cache[key])
        writer.add_page(page)

    with output_pdf.open("wb") as fh:
        writer.write(fh)


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument(
        "--markdown",
        default=EXPORT_DIR / "从存在到秩序_RC0_出版合并稿_2026-06-16.md",
        type=Path,
    )
    parser.add_argument("--watermark", default="RC0 评审稿｜请勿外传")
    parser.add_argument(
        "--font",
        default="/System/Library/Fonts/Supplemental/Songti.ttc",
        help="CJK font path for the watermark.",
    )
    args = parser.parse_args()

    markdown = args.markdown
    if not markdown.exists():
        raise FileNotFoundError(markdown)

    output_pdf = markdown.with_name(markdown.stem + "_水印版.pdf")
    with tempfile.TemporaryDirectory(prefix="srt-book-pdf-") as tmpdir:
        tmp = Path(tmpdir)
        css = tmp / "book.css"
        html = tmp / "book.html"
        plain_pdf = tmp / "plain.pdf"
        css.write_text(CSS, encoding="utf-8")
        create_html(markdown, html, css)
        print_pdf(html, plain_pdf)
        add_watermark(plain_pdf, output_pdf, args.watermark, args.font)

    print(output_pdf.relative_to(ROOT))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
