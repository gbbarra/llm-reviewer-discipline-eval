"""Build the English preprint PDF from Markdown: Markdown -> HTML -> headless Chrome PDF.

Usage: python docs/build_preprint_pdf.py
"""
import re
import subprocess
from pathlib import Path

import markdown

DOCS = Path(__file__).resolve().parent
SRC = DOCS / "PREPRINT-medRxiv-2026-10-24.en.md"
HTML = DOCS / "PREPRINT-medRxiv-2026-10-24.en.html"
PDF = DOCS / "PREPRINT-medRxiv-2026-10-24.en.pdf"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

CSS = """
@page { size: A4; margin: 2.5cm;
  @bottom-center { content: counter(page); font-family: 'Times New Roman', serif; font-size: 10pt; } }
body { font-family: 'Times New Roman', Times, serif; font-size: 11pt; line-height: 1.45; color: #000; }
h1 { font-size: 16pt; line-height: 1.3; margin: 0 0 14pt; }
h2 { font-size: 13pt; margin: 18pt 0 6pt; break-after: avoid; }
h3 { font-size: 11pt; font-style: italic; margin: 12pt 0 4pt; break-after: avoid; }
p { margin: 0 0 7pt; text-align: justify; }
hr { border: 0; margin: 6pt 0; }
code { font-family: 'Consolas', monospace; font-size: 9.5pt; }
a { color: #000; text-decoration: none; }
ol { padding-left: 22pt; }
ol li { margin-bottom: 3pt; font-size: 10pt; text-align: left; overflow-wrap: anywhere; }
figure { margin: 10pt 0 12pt; break-inside: avoid; page-break-inside: avoid; }
figure img { display: block; max-width: 100%; max-height: 17cm; margin: 0 auto 6pt; }
figure figcaption { font-size: 10pt; line-height: 1.35; text-align: justify; }
.titlepage { break-after: page; }
.titlepage p { text-align: left; }
"""


def build_html() -> str:
    text = SRC.read_text(encoding="utf-8")
    body = markdown.markdown(text, extensions=["extra"])
    # Image paragraph followed by its legend paragraph -> one unbreakable <figure>.
    body = re.sub(
        r'<p><img alt="([^"]*)" src="([^"]+)" /></p>\s*<p>(<strong>(?:Figure|Fig).*?)</p>',
        r'<figure><img alt="\1" src="\2" /><figcaption>\3</figcaption></figure>',
        body, flags=re.S)
    # Title page: everything before the Abstract heading.
    head, sep, rest = body.partition("<h2>Abstract</h2>")
    head = head.replace("<hr />", "")
    body = f'<div class="titlepage">{head}</div>{sep}{rest}'
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<title>Language-model reviewers under partial evidence</title>'
            f'<style>{CSS}</style></head><body>{body}</body></html>')


def main() -> None:
    HTML.write_text(build_html(), encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={PDF}", HTML.as_uri()], check=True)
    HTML.unlink()
    print(PDF)


if __name__ == "__main__":
    main()
