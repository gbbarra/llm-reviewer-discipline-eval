"""Build the English preprint PDF from Markdown: Markdown -> HTML -> headless Chrome PDF.

Layout imitates a LaTeX article (Latin Modern, numbered sections, centred title
block and abstract, indented paragraphs). Latin Modern fonts (GUST Font License)
are in docs/fonts.

Usage: python docs/build_preprint_pdf.py [--src MD] [--pdf PDF] [--date "28 October 2026"]
Chrome: set CHROME to the browser executable when it is not at the default Windows path.
"""
import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

import markdown

DOCS = Path(__file__).resolve().parent
SRC = DOCS / "PREPRINT-medRxiv-2026-10-24.en.md"
HTML = DOCS / "PREPRINT-medRxiv-2026-10-24.en.html"
PDF = DOCS / "PREPRINT-medRxiv-2026-10-24.en.pdf"
CHROME = os.environ.get("CHROME", r"C:\Program Files\Google\Chrome\Application\chrome.exe")
DATE = "24 October 2026"

CSS = """
@font-face { font-family: LM; src: url(fonts/LM-regular.woff2); font-weight: normal; font-style: normal; }
@font-face { font-family: LM; src: url(fonts/LM-italic.woff2); font-weight: normal; font-style: italic; }
@font-face { font-family: LM; src: url(fonts/LM-bold.woff2); font-weight: bold; font-style: normal; }
@font-face { font-family: LM; src: url(fonts/LM-bold-italic.woff2); font-weight: bold; font-style: italic; }
@page { size: A4; margin: 2.5cm;
  @top-center { content: "%(short)s"; font-family: LM, serif; font-size: 9pt; font-style: italic; color: #333; }
  @bottom-center { content: counter(page); font-family: LM, serif; font-size: 10pt; } }
@page :first { @top-center { content: none; } }
body { font-family: LM, 'Times New Roman', serif; font-size: 11pt; line-height: 1.32; color: #000;
  hyphens: auto; -webkit-hyphens: auto; }
p { margin: 0; text-align: justify; text-indent: 1.5em; }
h2 + p, h3 + p, figure + p, .abstract p, li p, figcaption, .meta p { text-indent: 0; }
a { color: #000; text-decoration: none; }
code { font-family: 'Consolas', monospace; font-size: 9pt; }

.titleblock { text-align: center; margin: 0 0 0.6cm; }
.titleblock h1 { font-size: 17pt; line-height: 1.25; font-weight: bold; margin: 0 0 14pt;
  hyphens: none; -webkit-hyphens: none; }
.titleblock .author { font-size: 12pt; margin-bottom: 4pt; }
.titleblock .affil, .titleblock .corr, .titleblock .date { font-size: 10pt; margin-bottom: 2pt; }
.titleblock .date { margin-top: 8pt; }

.abstract { margin: 0 1.2cm 0.5cm; font-size: 10pt; }
.abstract h2 { text-align: center; font-size: 10.5pt; margin: 0 0 6pt; counter-increment: none; }
.abstract h2::before { content: none; }
.abstract p { margin-bottom: 4pt; }
.meta { margin: 0 1.2cm 0.6cm; font-size: 9.5pt; }
.meta p { margin-bottom: 2pt; text-align: left; }

body { counter-reset: sec; }
h2 { font-size: 13pt; margin: 16pt 0 6pt; break-after: avoid; counter-increment: sec; counter-reset: sub; }
h2::before { content: counter(sec) "\\2003"; }
h2.nonum { counter-increment: none; }
h2.nonum::before { content: none; }
h3 { font-size: 11pt; margin: 10pt 0 3pt; break-after: avoid; counter-increment: sub; }
h3::before { content: counter(sec) "." counter(sub) "\\2003"; }

ol { padding-left: 2em; margin: 4pt 0 6pt; }
ol li { margin-bottom: 2pt; text-align: justify; }
.refs ol li { font-size: 9.5pt; line-height: 1.25; text-align: left; overflow-wrap: anywhere; margin-bottom: 3pt; }

figure { margin: 10pt 0 12pt; break-inside: avoid; page-break-inside: avoid; }
figure img { display: block; max-width: 100%%; max-height: 16.5cm; margin: 0 auto 6pt; }
figure figcaption { font-size: 9.5pt; line-height: 1.28; text-align: justify; }
"""


def field(md: str, label: str) -> str:
    return re.search(rf"\*\*{re.escape(label)}:\*\*\s*(.+)", md).group(1).strip()


def build_html(src: Path = SRC, date: str = DATE) -> str:
    md = src.read_text(encoding="utf-8")
    front, _, rest = md.partition("## Abstract")
    title = re.search(r"^# (.+)$", front, re.M).group(1)
    author = re.search(r"^\*\*(.+?)\*\*¹", front, re.M).group(1)
    affil = re.search(r"^¹ (.+)$", front, re.M).group(1)
    short = field(front, "Short title")
    corr = field(front, "Correspondence")
    keywords = field(front, "Keywords")

    abstract_md, _, main_md = rest.partition("---")
    conv = lambda s: markdown.markdown(s, extensions=["extra", "smarty"])
    abstract = conv(abstract_md)
    body = conv(main_md).replace("<hr />", "")

    # Image paragraph followed by its legend paragraph -> one unbreakable <figure>.
    body = re.sub(
        r'<p><img alt="([^"]*)" src="([^"]+)" /></p>\s*<p>(<strong>(?:Figure|Fig).*?)</p>',
        r'<figure><img alt="\1" src="\2" /><figcaption>\3</figcaption></figure>',
        body, flags=re.S)
    # Figure 1 goes right after the paragraph that first cites it (Study design).
    fig1 = re.search(r'<figure><img alt="Figure 1".*?</figure>', body, flags=re.S).group(0)
    body = body.replace(fig1, "")
    body = re.sub(r'(<h3>Study design</h3>\s*<p>.*?</p>)', lambda m: m.group(1) + fig1, body,
                  count=1, flags=re.S)
    # Keep citation groups such as [13–15] on one line.
    body = re.sub(r"\[(\d[\d,–]*)\]", r'<span style="white-space:nowrap">[\1]</span>', body)
    # Back matter is unnumbered, as in a LaTeX article.
    for h in ("Declarations", "References", "Supplementary Material"):
        body = body.replace(f"<h2>{h}</h2>", f'<h2 class="nonum">{h}</h2>')
    body = re.sub(r'(<h2 class="nonum">References</h2>\s*)(<ol>.*?</ol>)',
                  r'\1<div class="refs">\2</div>', body, flags=re.S)
    # Declarations sub-items read better without the paragraph indent.
    body = re.sub(r"<p><strong>", r'<p style="text-indent:0;margin-top:3pt"><strong>', body)

    head = (
        f'<div class="titleblock"><h1>{title}</h1>'
        f'<div class="author">{author}<sup>1</sup></div>'
        f'<div class="affil"><sup>1</sup>{affil}</div>'
        f'<div class="corr">Correspondence: {corr}</div>'
        f'<div class="date">{date}</div></div>'
        f'<div class="abstract"><h2>Abstract</h2>{abstract}</div>'
        f'<div class="meta"><p><strong>Keywords:</strong> {keywords}</p></div>'
    )
    css = CSS % {"short": short}
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<title>{short}</title><style>{css}</style></head>'
            f'<body>{head}{body}</body></html>')


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", type=Path, default=SRC)
    ap.add_argument("--pdf", type=Path, default=PDF)
    ap.add_argument("--date", default=DATE)
    args = ap.parse_args()
    # The HTML stays in docs/ so that figure paths (figures/...) resolve for any source file.
    HTML.write_text(build_html(args.src, args.date), encoding="utf-8")
    flags = ["--no-sandbox"] if sys.platform != "win32" and os.geteuid() == 0 else []
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", *flags,
                    "--allow-file-access-from-files", "--virtual-time-budget=10000",
                    f"--print-to-pdf={args.pdf.resolve()}", HTML.as_uri()], check=True)
    HTML.unlink()
    print(args.pdf)


if __name__ == "__main__":
    main()
