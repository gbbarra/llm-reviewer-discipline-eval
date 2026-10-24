"""Build a one-page PDF resume from the public ORCID record (no third-party packages).

Facts only from ORCID 0000-0002-2136-3471 and the author's own public repositories. Output goes to the
session scratchpad, not the project.
"""
from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

ORCID = "0000-0002-2136-3471"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("resume-gustavo-barra.pdf")


def fetch():
    req = urllib.request.Request(f"https://pub.orcid.org/v3.0/{ORCID}/record", headers={"Accept": "application/json"})
    return json.load(urllib.request.urlopen(req))


def lines_from(rec) -> list[tuple[str, str]]:
    name = f"{rec['person']['name']['given-names']['value']} {rec['person']['name']['family-name']['value']}"
    out = [("H1", name), ("P", f"ORCID {ORCID}  |  Brasília, Brazil  |  Clinical laboratory medicine, molecular diagnostics")]
    out.append(("H2", "Experience"))
    for g in rec["activities-summary"]["employments"]["affiliation-group"]:
        s = g["summaries"][0]["employment-summary"]
        y0 = s["start-date"]["year"]["value"] if s.get("start-date") else ""
        y1 = s["end-date"]["year"]["value"] if s.get("end-date") else "present"
        role = s["role-title"].replace("Analist", "Analyst")  # spelling as on ORCID, corrected
        out.append(("P", f"{role}, {s['organization']['name']} ({y0}-{y1})"))
    out.append(("H2", "Education"))
    for g in rec["activities-summary"]["educations"]["affiliation-group"]:
        s = g["summaries"][0]["education-summary"]
        y0 = s["start-date"]["year"]["value"] if s.get("start-date") else ""
        y1 = s["end-date"]["year"]["value"] if s.get("end-date") else ""
        out.append(("P", f"{s['role-title']}, {s['organization']['name']} ({y0}-{y1})"))
    works = rec["activities-summary"]["works"]["group"]
    out.append(("H2", f"Publications ({len(works)} works on ORCID; selected)"))
    seen = set()
    for g in works:
        w = g["work-summary"][0]
        t = w["title"]["title"]["value"]
        if t.lower().startswith("correction") or t in seen:
            continue
        seen.add(t)
        y = w["publication-date"]["year"]["value"] if w.get("publication-date") else ""
        j = (w.get("journal-title") or {}).get("value") or ""
        out.append(("P", f"{y}  {t}" + (f"  ({j})" if j else "")))
        if len(seen) >= 8:
            break
    out.append(("H2", "Open benchmarks and tools"))
    out.append(("P", "EXTRAI: evidence-extraction benchmark for local LLMs (Brazilian Portuguese), MIT, DOI 10.5281/zenodo.22159050"))
    out.append(("P", "FIEL: summarization-faithfulness benchmark for local LLMs (Brazilian Portuguese), github.com/gbbarra"))
    out.append(("P", "Reviewer discipline under partial evidence: an eval of LLM reviewers of extracted data (in progress, 2026)"))
    return out


def wrap(text: str, width: int) -> list[str]:
    words, cur, res = text.split(), "", []
    for w in words:
        if len(cur) + len(w) + 1 > width:
            res.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        res.append(cur)
    return res


def pdf(lines: list[tuple[str, str]]) -> bytes:
    esc = lambda s: s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    ops, y = [], 790
    for kind, text in lines:
        size, font, gap, width = {"H1": (18, "F2", 26, 60), "H2": (12, "F2", 18, 90), "P": (9.5, "F1", 13, 110)}[kind]
        if kind == "H2":
            y -= 6
        for seg in wrap(text, width):
            ops.append(f"BT /{font} {size} Tf 50 {y} Td ({esc(seg)}) Tj ET")
            y -= gap
    # non-ASCII (accents, dashes) -> closest ASCII, since the base-14 fonts here are Latin-1 only
    import unicodedata
    content = "\n".join(ops)
    content = unicodedata.normalize("NFKD", content).encode("latin-1", "ignore")
    objs = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Contents 4 0 R /Resources << /Font << /F1 5 0 R /F2 6 0 R >> >> >>",
        b"<< /Length " + str(len(content)).encode() + b" >>\nstream\n" + content + b"\nendstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>",
    ]
    out, offsets = bytearray(b"%PDF-1.4\n"), []
    for i, o in enumerate(objs, 1):
        offsets.append(len(out))
        out += f"{i} 0 obj\n".encode() + o + b"\nendobj\n"
    xref = len(out)
    out += f"xref\n0 {len(objs)+1}\n0000000000 65535 f \n".encode()
    for off in offsets:
        out += f"{off:010d} 00000 n \n".encode()
    out += f"trailer\n<< /Size {len(objs)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
    return bytes(out)


if __name__ == "__main__":
    rec = fetch()
    lines = lines_from(rec)
    OUT.write_bytes(pdf(lines))
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes, {len(lines)} lines)")
    for k, t in lines:
        print(f"  [{k}] {t[:110]}")
