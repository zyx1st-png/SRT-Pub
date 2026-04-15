#!/usr/bin/env python3
from __future__ import annotations

import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path


NS_W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS_PKG = "http://schemas.openxmlformats.org/package/2006/relationships"
NS_CT = "http://schemas.openxmlformats.org/package/2006/content-types"
NS_WP = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
NS_A = "http://schemas.openxmlformats.org/drawingml/2006/main"

FIGURE_WIDTH_EMU = 5943600  # 6.5 in
LINE_NUMBER_DISTANCE = "360"  # twips


def patch_docx(docx_path: Path) -> None:
    tmp_path = docx_path.with_suffix(".tmp.docx")

    ET.register_namespace("w", NS_W)
    ET.register_namespace("r", NS_R)
    ET.register_namespace("", NS_PKG)

    with zipfile.ZipFile(docx_path, "r") as zin:
        files = {name: zin.read(name) for name in zin.namelist()}

    document_root = ET.fromstring(files["word/document.xml"])
    for sect in document_root.findall(f".//{{{NS_W}}}sectPr"):
        for child in list(sect):
            if child.tag in {
                f"{{{NS_W}}}headerReference",
                f"{{{NS_W}}}footerReference",
                f"{{{NS_W}}}lnNumType",
            }:
                sect.remove(child)

        footer_ref = ET.Element(f"{{{NS_W}}}footerReference")
        footer_ref.set(f"{{{NS_W}}}type", "default")
        footer_ref.set(f"{{{NS_R}}}id", "rId999")
        sect.insert(0, footer_ref)

        line_numbers = ET.Element(f"{{{NS_W}}}lnNumType")
        line_numbers.set(f"{{{NS_W}}}countBy", "1")
        line_numbers.set(f"{{{NS_W}}}start", "1")
        line_numbers.set(f"{{{NS_W}}}restart", "newPage")
        line_numbers.set(f"{{{NS_W}}}distance", LINE_NUMBER_DISTANCE)
        sect.insert(1, line_numbers)

    for inline in document_root.findall(f".//{{{NS_WP}}}inline"):
        wp_extent = inline.find(f"{{{NS_WP}}}extent")
        a_extent = inline.find(f".//{{{NS_A}}}ext")
        if wp_extent is None or a_extent is None:
            continue
        old_cx = int(wp_extent.get("cx", "0"))
        old_cy = int(wp_extent.get("cy", "0"))
        if old_cx <= 0 or old_cy <= 0:
            continue
        new_cy = int(old_cy * FIGURE_WIDTH_EMU / old_cx)
        for node in (wp_extent, a_extent):
            node.set("cx", str(FIGURE_WIDTH_EMU))
            node.set("cy", str(new_cy))

    files["word/document.xml"] = ET.tostring(
        document_root, encoding="UTF-8", xml_declaration=True
    )

    rels_root = ET.fromstring(files["word/_rels/document.xml.rels"])
    for rel in list(rels_root):
        rel_type = rel.attrib.get("Type", "")
        if rel_type.endswith("/header") or rel_type.endswith("/footer"):
            rels_root.remove(rel)
    footer_rel = ET.Element(f"{{{NS_PKG}}}Relationship")
    footer_rel.set("Id", "rId999")
    footer_rel.set(
        "Type",
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer",
    )
    footer_rel.set("Target", "footer1.xml")
    rels_root.append(footer_rel)
    files["word/_rels/document.xml.rels"] = ET.tostring(
        rels_root, encoding="UTF-8", xml_declaration=True
    )

    files["word/footer1.xml"] = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="{NS_W}" xmlns:r="{NS_R}">
  <w:p>
    <w:pPr>
      <w:pStyle w:val="Footer"/>
      <w:jc w:val="center"/>
    </w:pPr>
    <w:r><w:fldChar w:fldCharType="begin"/></w:r>
    <w:r><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>
    <w:r><w:fldChar w:fldCharType="separate"/></w:r>
    <w:r><w:t>1</w:t></w:r>
    <w:r><w:fldChar w:fldCharType="end"/></w:r>
  </w:p>
</w:ftr>
""".encode("utf-8")

    content_root = ET.fromstring(files["[Content_Types].xml"])
    for child in list(content_root):
        if child.tag != f"{{{NS_CT}}}Override":
            continue
        part_name = child.attrib.get("PartName", "")
        if part_name.startswith("/word/header") or part_name.startswith("/word/footer"):
            content_root.remove(child)
    footer_override = ET.Element(f"{{{NS_CT}}}Override")
    footer_override.set("PartName", "/word/footer1.xml")
    footer_override.set(
        "ContentType",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml",
    )
    content_root.append(footer_override)
    files["[Content_Types].xml"] = ET.tostring(
        content_root, encoding="UTF-8", xml_declaration=True
    )

    for name in list(files):
        if name.startswith("word/header"):
            del files[name]
        if name.startswith("word/footer") and name != "word/footer1.xml":
            del files[name]

    with zipfile.ZipFile(tmp_path, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for name, data in files.items():
            zout.writestr(name, data)

    tmp_path.replace(docx_path)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: postprocess_frontiers_docx.py <docx_path>", file=sys.stderr)
        return 2
    docx_path = Path(sys.argv[1]).resolve()
    if not docx_path.exists():
        print(f"missing file: {docx_path}", file=sys.stderr)
        return 1
    patch_docx(docx_path)
    print(f"patched {docx_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
