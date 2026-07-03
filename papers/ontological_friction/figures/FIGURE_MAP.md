# Figure numbering — single source of truth

The source basename number, the output PNG number, the manuscript "Figure N" caption,
and the Frontiers upload `FigureN.tif/.jpg` are all kept identical. Do not reorder.

| Manuscript | Source script | Output PNG | Upload file | Caption title |
|---|---|---|---|---|
| Figure 1 | `fig1_control_architecture.py` | `fig1_control_architecture.png` | `frontiers_upload/Figure1.{tif,jpg}` | Hierarchical control architecture and selection power budget |
| Figure 2 | `fig2_proxy_map.py` | `fig2_proxy_map.png` | `frontiers_upload/Figure2.{tif,jpg}` | Cross-modal operationalization map for executive friction |
| Figure 3 | `fig3_ros_coupling.py` | `fig3_ros_coupling.png` | `frontiers_upload/Figure3.{tif,jpg}` | Proposed oxidative feedback loop (ROS–Ψ_f coupling) |
| Figure 4 | `fig4_clinical_radar.py` | `fig4_clinical_radar.png` | `frontiers_upload/Figure4.{tif,jpg}` | Predicted Ψ_f proxy signatures across clinical conditions |
| Figure 5 | `fig5_protocol.py` | `fig5_protocol.png` | `frontiers_upload/Figure5.{tif,jpg}` | Core-chain protocol and critical-load prediction |

## Rebuild

```
# from this figures/ directory, with a matplotlib+Pillow environment:
for f in fig1_control_architecture fig2_proxy_map fig3_ros_coupling fig4_clinical_radar fig5_protocol; do
  python "$f.py"           # each script saves fig<N>_*.png next to itself
done
# export correctly-numbered upload files (FigureN <- figN_*.png, 1:1):
python - <<'PY'
from PIL import Image; import glob
for png in sorted(glob.glob("fig[1-5]_*.png")):
    n = png[3]; im = Image.open(png).convert("RGB")
    im.save(f"frontiers_upload/Figure{n}.tif", format="TIFF", compression="tiff_lzw", dpi=(300,300))
    im.save(f"frontiers_upload/Figure{n}.jpg", format="JPEG", quality=95, dpi=(300,300))
PY
```

## History / caution

The originally submitted package (manuscript 1837760) mis-bound the uploaded TIFs
(architecture appeared as Figure 4, ROS as Figure 1, radar as Figure 3), because the
old source basenames did not match the manuscript order (`fig3_clinical_radar` was
Figure 4, `fig4_experimental_design` was Figure 5, `fig5_ros_dag` was Figure 3).
Renaming the sources to match the manuscript numbering removes that failure mode.
