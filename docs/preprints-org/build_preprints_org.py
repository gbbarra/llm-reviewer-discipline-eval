"""Build the Preprints.org version (Word) of the English preprint.

Preprints.org takes a Word or LaTeX manuscript whose first page carries title, authors, affiliations,
corresponding-author contact, abstract and keywords. This script rearranges the front matter of
../PREPRINT-medRxiv-2026-10-24.en.md accordingly, drops the medRxiv-only lines, and converts with pandoc.
Figure 1 is moved to the end of "Study design", where it is first cited, as in the PDF.

Usage: python docs/preprints-org/build_preprints_org.py
Needs pandoc on the PATH.
"""
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS = HERE.parent
SRC = DOCS / "PREPRINT-medRxiv-2026-10-24.en.md"
OUT_MD = HERE / "PREPRINTS-manuscript.en.md"
OUT_DOCX = HERE / "PREPRINTS-manuscript.en.docx"


def field(md: str, label: str) -> str:
    return re.search(rf"^\*\*{re.escape(label)}:\*\*\s*(.+)$", md, re.M).group(1).strip()


def build_md() -> str:
    md = SRC.read_text(encoding="utf-8")
    front, _, rest = md.partition("## Abstract")
    title = re.search(r"^# (.+)$", front, re.M).group(1)
    author = re.search(r"^\*\*(.+?)\*\*¹", front, re.M).group(1)
    affil = re.search(r"^¹ (.+)$", front, re.M).group(1)
    email = re.search(r"[\w.+-]+@[\w.-]+", field(front, "Correspondence")).group(0)
    keywords = field(front, "Keywords")

    abstract, _, body = rest.partition("\n---\n")
    body = body.replace("\n---\n", "\n")

    # Figure 1 (image + legend) goes after the first paragraph of "Study design".
    fig1 = re.search(r"\n!\[Figure 1\]\([^)]*\)\n\n\*\*Figure 1\..*?\n", body, re.S).group(0)
    body = body.replace(fig1, "\n")
    body = re.sub(r"(### Study design\n\n.+?\n)", lambda m: m.group(1) + fig1, body, count=1, flags=re.S)
    # Images at full text width.
    body = re.sub(r"(!\[[^\]]*\]\([^)]+\))", r"\1{width=100%}", body)

    head = (f"# {title}\n\n"
            f"{author} ^1,\\*^\n\n"
            f"^1^ {affil}\n\n"
            f"^\\*^ Correspondence: {email}\n\n"
            f"## Abstract\n{abstract.rstrip()}\n\n"
            f"**Keywords:** {keywords}\n\n")
    return head + body.lstrip()


def main() -> None:
    OUT_MD.write_text(build_md(), encoding="utf-8")
    subprocess.run(["pandoc", str(OUT_MD), "-f", "markdown-implicit_figures", "-t", "docx", "-o", str(OUT_DOCX),
                    f"--resource-path={DOCS}"], check=True)
    print(OUT_DOCX)


if __name__ == "__main__":
    main()
