from __future__ import annotations

import io
import re
import shutil
import subprocess
from pathlib import Path

import pypandoc
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "paper_ontological_friction_preprint.md"
HTML_OUT = ROOT / "paper_ontological_friction_preprint.html"
PDF_RAW = ROOT / "paper_ontological_friction_preprint.raw.pdf"
PDF_OUT = ROOT / "paper_ontological_friction_preprint.pdf"


def extract_title(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("Could not find the manuscript title.")


def build_html(title: str, body_html: str) -> str:
    css = r"""
    @page {
      size: A4;
      margin: 18mm 17mm 22mm 17mm;
    }
    html, body {
      background: #fff;
    }
    body {
      font-family: Georgia, "Times New Roman", serif;
      color: #111;
      margin: 0;
      padding: 0;
      font-size: 10.4pt;
      line-height: 1.46;
    }
    h1, h2, h3 {
      line-height: 1.25;
      page-break-after: avoid;
      break-after: avoid-page;
    }
    h1 {
      text-align: center;
      font-size: 20pt;
      margin: 0 0 0.75em;
    }
    h2 {
      font-size: 14pt;
      margin: 1.4em 0 0.5em;
      border-top: 0.7pt solid #bbb;
      padding-top: 0.45em;
    }
    h3 {
      font-size: 11.5pt;
      margin: 1.05em 0 0.35em;
    }
    p {
      margin: 0.55em 0;
      text-align: justify;
      orphans: 3;
      widows: 3;
    }
    h1 + p,
    h1 + p + p,
    h1 + p + p + p,
    h1 + p + p + p + p,
    h1 + p + p + p + p + p,
    h1 + p + p + p + p + p + p,
    h1 + p + p + p + p + p + p + p,
    h1 + p + p + p + p + p + p + p + p,
    h1 + p + p + p + p + p + p + p + p + p,
    h1 + p + p + p + p + p + p + p + p + p + p {
      text-align: center;
      margin: 0.25em 0;
    }
    ul, ol {
      margin: 0.55em 0 0.75em 1.35em;
      padding: 0;
    }
    li {
      margin: 0.2em 0;
    }
    hr {
      border: 0;
      border-top: 0.7pt solid #bbb;
      margin: 1em 0;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      table-layout: fixed;
      margin: 0.8em 0 1em;
      font-size: 7.15pt;
      line-height: 1.25;
      page-break-inside: auto;
    }
    thead {
      display: table-header-group;
    }
    tr {
      page-break-inside: avoid;
      break-inside: avoid;
    }
    th, td {
      border: 0.55pt solid #aaa;
      padding: 0.32em 0.4em;
      vertical-align: top;
      overflow-wrap: anywhere;
      word-break: normal;
    }
    th {
      background: #f2f2f2;
      text-align: left;
      font-weight: 700;
    }
    img {
      display: block;
      max-width: 100%;
      max-height: 235mm;
      height: auto;
      margin: 0.65em auto 0.35em;
      page-break-inside: avoid;
      break-inside: avoid;
    }
    figure, .figure {
      page-break-inside: avoid;
      break-inside: avoid;
    }
    blockquote {
      margin: 0.7em 1.2em;
      padding-left: 0.8em;
      border-left: 2pt solid #bbb;
    }
    code {
      font-family: "DejaVu Sans Mono", monospace;
      font-size: 0.9em;
    }
    .math.display {
      overflow: visible;
      margin: 0.75em 0;
      text-align: center;
      page-break-inside: avoid;
      break-inside: avoid;
    }
    a {
      color: #111;
      text-decoration: none;
    }
    """
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>{css}</style>
  <script>
    window.MathJax = {{
      tex: {{tags: 'ams'}},
      options: {{enableMenu: false}}
    }};
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml-full.js"></script>
</head>
<body>
{body_html}
</body>
</html>
"""


def find_chrome() -> Path:
    candidates = []
    for executable in (
        "google-chrome",
        "google-chrome-stable",
        "chromium",
        "chromium-browser",
    ):
        resolved = shutil.which(executable)
        if resolved:
            candidates.append(Path(resolved))
    candidates.extend(
        [
            Path("/usr/bin/google-chrome"),
            Path("/usr/bin/google-chrome-stable"),
            Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
        ]
    )
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise FileNotFoundError("Google Chrome or Chromium is required to render the PDF.")


def render_html(title: str) -> None:
    body_html = pypandoc.convert_file(
        str(SRC),
        "html5",
        format="md",
        extra_args=[
            "--from=markdown+tex_math_dollars+raw_tex+pipe_tables+table_captions",
            "--to=html5",
            "--mathjax",
            f"--resource-path={ROOT}",
        ],
    )
    HTML_OUT.write_text(build_html(title, body_html), encoding="utf-8")


def render_raw_pdf() -> None:
    chrome = find_chrome()
    subprocess.run(
        [
            str(chrome),
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--allow-file-access-from-files",
            "--no-pdf-header-footer",
            "--virtual-time-budget=40000",
            "--run-all-compositor-stages-before-draw",
            f"--print-to-pdf={PDF_RAW}",
            HTML_OUT.resolve().as_uri(),
        ],
        check=True,
        timeout=180,
    )


def footer_overlay(width: float, height: float, page_number: int) -> bytes:
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=(width, height))
    c.setFont("Helvetica", 7.5)
    c.drawString(40, 18, "Preprint - not peer reviewed")
    c.drawCentredString(width / 2, 18, str(page_number))
    c.save()
    return packet.getvalue()


def add_footers() -> None:
    reader = PdfReader(str(PDF_RAW))
    writer = PdfWriter()
    for index, page in enumerate(reader.pages, start=1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        overlay = PdfReader(io.BytesIO(footer_overlay(width, height, index))).pages[0]
        page.merge_page(overlay)
        writer.add_page(page)
    with PDF_OUT.open("wb") as f:
        writer.write(f)


def verify_pdf(title: str) -> None:
    if not PDF_OUT.exists() or PDF_OUT.stat().st_size < 100_000:
        raise RuntimeError("Generated PDF is missing or unexpectedly small.")
    reader = PdfReader(str(PDF_OUT))
    if len(reader.pages) < 10:
        raise RuntimeError(f"Expected a long manuscript PDF, found only {len(reader.pages)} pages.")
    sample = "\n".join((page.extract_text() or "") for page in reader.pages[:4])
    normalized = re.sub(r"\s+", " ", sample)
    if title not in normalized:
        raise RuntimeError("The title was not recoverable from the generated PDF.")
    if "Preprint" not in normalized:
        raise RuntimeError("The preprint status was not recoverable from the generated PDF.")
    if "Target journal" in normalized:
        raise RuntimeError("Journal-specific target metadata remains in the generated PDF.")
    print(f"Verified {PDF_OUT.name}: {len(reader.pages)} pages, {PDF_OUT.stat().st_size} bytes")


def main() -> None:
    raw = SRC.read_text(encoding="utf-8")
    title = extract_title(raw)
    render_html(title)
    render_raw_pdf()
    add_footers()
    verify_pdf(title)
    PDF_RAW.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
