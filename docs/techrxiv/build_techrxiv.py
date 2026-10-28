"""Build the TechRxiv version of the preprint from the English manuscript.

- same text as ../PREPRINT-medRxiv-2026-10-24.en.md, with the medRxiv category line replaced
- PDF built with ../build_preprint_pdf.py (set CHROME when Chrome is not at the Windows default path)

Usage: python docs/techrxiv/build_techrxiv.py [--date "28 October 2026"]
"""
import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS = HERE.parent
SRC = DOCS / "PREPRINT-medRxiv-2026-10-24.en.md"
OUT_MD = HERE / "TECHRXIV-manuscript.en.md"
OUT_PDF = HERE / "TECHRXIV-manuscript.en.pdf"

OLD_CATEGORY = "**Category (medRxiv):** Health Informatics"
NEW_CATEGORY = "**Subject (TechRxiv):** Computing and Processing; Bioengineering"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default="28 October 2026")
    args = ap.parse_args()
    md = SRC.read_text(encoding="utf-8")
    assert md.count(OLD_CATEGORY) == 1, "category line not found in the source manuscript"
    OUT_MD.write_text(md.replace(OLD_CATEGORY, NEW_CATEGORY), encoding="utf-8")
    subprocess.run([sys.executable, str(DOCS / "build_preprint_pdf.py"), "--src", str(OUT_MD),
                    "--pdf", str(OUT_PDF), "--date", args.date], check=True)


if __name__ == "__main__":
    main()
