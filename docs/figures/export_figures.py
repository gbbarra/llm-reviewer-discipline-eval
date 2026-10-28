"""Export each figure as a separate vector PDF (from the SVG) and a 300 dpi JPG (from the PNG).

Output: docs/figures/export/Figure1.pdf, Figure1.jpg, ..., FigureS1.pdf, FigureS1.jpg

Usage: python docs/figures/export_figures.py
Chrome: set CHROME to the browser executable when it is not at the default Windows path.
"""
import os
import re
import subprocess
import sys
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
OUT = HERE / "export"
CHROME = os.environ.get("CHROME", r"C:\Program Files\Google\Chrome\Application\chrome.exe")
FIGURES = {
    "Figure1": "fig1-methods-ABCD",
    "Figure2": "fig2-plausibility-flip",
    "Figure3": "fig3-partial-evidence-outcomes",
    "Figure4": "fig4-collateral-edits",
    "Figure5": "fig5-instruction-erasure",
    "Figure6": "fig6-reasoning-effort",
    "FigureS1": "figS1-metric-summary",
}
TO_MM = {"mm": 1.0, "pt": 25.4 / 72, "px": 25.4 / 96, "in": 25.4}


def size_mm(svg: Path):
    head = svg.read_text(encoding="utf-8")[:2000]
    dims = []
    for attr in ("width", "height"):
        value, unit = re.search(rf'{attr}="([\d.]+)(mm|pt|px|in)?"', head).groups()
        dims.append(float(value) * TO_MM[unit or "px"])
    return dims


def export_pdf(svg: Path, pdf: Path) -> None:
    w, h = size_mm(svg)
    html = OUT / f"_{svg.stem}.html"
    html.write_text(
        f"<!doctype html><html><head><meta charset='utf-8'><style>"
        f"@page {{ size: {w:.2f}mm {h:.2f}mm; margin: 0; }} html, body {{ margin: 0; }}"
        f"img {{ display: block; width: {w:.2f}mm; height: {h:.2f}mm; }}</style></head>"
        f"<body><img src='{svg.as_uri()}'></body></html>", encoding="utf-8")
    flags = ["--no-sandbox"] if sys.platform != "win32" and os.geteuid() == 0 else []
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", *flags,
                    "--allow-file-access-from-files", f"--print-to-pdf={pdf}", html.as_uri()],
                   check=True, stderr=subprocess.DEVNULL)
    html.unlink()


def export_jpg(png: Path, jpg: Path) -> None:
    im = Image.open(png)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, "white")
        bg.paste(im, mask=im.split()[-1])
        im = bg
    im.convert("RGB").save(jpg, "JPEG", quality=95, dpi=(300, 300), subsampling=0)


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for name, stem in FIGURES.items():
        export_pdf(HERE / f"{stem}.svg", OUT / f"{name}.pdf")
        export_jpg(HERE / f"{stem}.png", OUT / f"{name}.jpg")
        print(name)


if __name__ == "__main__":
    main()
