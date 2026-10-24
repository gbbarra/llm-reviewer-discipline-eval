"""Build figures/fig1-methods-ABCD.svg (methods schematic, four panels A-D).

Units are millimetres (viewBox 0 0 180 H, width 180 mm). Text stays as <text>.
Okabe-Ito colours with one meaning each across panels:
  green = value preserved (kept / kept + flagged), vermillion = erased, blue = flipped,
  pale yellow = target cell, grey hatch = sections removed from the excerpt.
Run:  python make_fig1.py   (writes the SVG next to this script)
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).with_name("fig1-methods-ABCD.svg")

GREEN, VERM, BLUE = "#009E73", "#D55E00", "#0072B2"
GREEN_T, VERM_T, BLUE_T = "#D9F0E8", "#F8E0CF", "#D6E6F2"
TARGET = "#F7EFA0"
INK, MID, LIGHT, RULE = "#1A1A1A", "#555555", "#F2F2F2", "#9A9A9A"
FONT = "Arial, Helvetica, sans-serif"
FL, FT, FS, FX = 4.6, 3.1, 2.6, 2.5   # letter, title, body, small (2.5 mm = 7.1 pt)

W, PW, PH, GAP, M = 180.0, 87.6, 100.0, 4.0, 0.4   # M: outer margin so frame strokes are not cropped
H = 2 * PH + GAP + 2 * M

_rid = [0]


def rect(x, y, w, h, fill="none", stroke=RULE, sw=0.25, rx=0.6, extra=""):
    _rid[0] += 1
    rid = f"r{_rid[0]}"
    return rid, (f'<rect id="{rid}" x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" '
                 f'rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>')


def text(x, y, lines, size=FS, weight="normal", anchor="start", fill=INK, style="normal", box=None, lh=1.22):
    if isinstance(lines, str):
        lines = [lines]
    attrs = (f'x="{x:.2f}" y="{y:.2f}" font-size="{size}" font-weight="{weight}" '
             f'font-style="{style}" text-anchor="{anchor}" fill="{fill}"')
    if box:
        attrs += f' data-in="{box}"'
    spans = "".join(
        f'<tspan x="{x:.2f}" dy="{0 if i == 0 else size * lh:.2f}">{escape(s)}</tspan>'
        for i, s in enumerate(lines))
    return f"<text {attrs}>{spans}</text>"


def arrow(x1, y1, x2, y2, color=MID, sw=0.35, head=True):
    m = ' marker-end="url(#ah)"' if head else ""
    return (f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{color}" '
            f'stroke-width="{sw}"{m}/>')


def boxed(x, y, w, h, lines, fill="#FFFFFF", stroke=RULE, sw=0.25, size=FS, weight="normal",
          color=INK, anchor="middle", pad=1.6, first=None, style="normal"):
    """Rectangle with vertically centred lines; returns svg parts."""
    rid, r = rect(x, y, w, h, fill, stroke, sw)
    if isinstance(lines, str):
        lines = [lines]
    n = len(lines)
    lh = size * 1.22
    y0 = y + h / 2 - (n - 1) * lh / 2 + size * 0.35
    tx = x + w / 2 if anchor == "middle" else x + pad
    out = [r]
    for i, s in enumerate(lines):
        wgt = first if (first and i == 0) else weight
        out.append(text(tx, y0 + i * lh, s, size, wgt, anchor, color, style, box=rid))
    return out


def header(letter, title, subtitle, box):
    return [text(3.0, 6.6, letter, FL, "bold", box=box),
            text(9.0, 6.2, title, FT, "bold", box=box),
            text(9.0, 10.4, subtitle, FX, fill=MID, box=box)]


def mini_table(x, y, rows, target_row, w=36.0, rh=4.4, split=19.0):
    """Two-column extraction table (Cell | Value); target row highlighted."""
    out = []
    rid, r = rect(x, y, w, rh, fill="#E6E6E6", rx=0)
    out += [r, text(x + 1.2, y + rh * 0.72, "Cell", FX, "bold", box=rid),
            text(x + split + 1.2, y + rh * 0.72, "Value", FX, "bold", box=rid)]
    for i, (k, v) in enumerate(rows):
        yy = y + rh * (i + 1)
        tgt = i == target_row
        rid, r = rect(x, yy, w, rh, fill=TARGET if tgt else "#FFFFFF", rx=0,
                      stroke=INK if tgt else RULE, sw=0.45 if tgt else 0.25)
        out += [r, text(x + 1.2, yy + rh * 0.72, k, FX, box=rid),
                text(x + split + 1.2, yy + rh * 0.72, v, FX, "bold" if tgt else "normal", box=rid)]
    out.append(f'<line x1="{x + split:.2f}" y1="{y:.2f}" x2="{x + split:.2f}" y2="{y + rh * (len(rows) + 1):.2f}" '
               f'stroke="{RULE}" stroke-width="0.25"/>')
    return out


def section_rows(x, y, w, rows, rh=4.4, gap=0.6):
    """Report sections; rows are (label, removed?)."""
    out = []
    for i, (lab, removed) in enumerate(rows):
        yy = y + i * (rh + gap)
        rid, r = rect(x, yy, w, rh, fill="url(#hatch)" if removed else "#FFFFFF",
                      stroke="#B5B5B5" if removed else RULE, rx=0.3)
        out += [r, text(x + 1.2, yy + rh * 0.72, lab, FX, fill="#7A7A7A" if removed else INK,
                        style="italic" if removed else "normal", box=rid)]
    return out


# ---------------------------------------------------------------- panel A
def panel_a():
    fid, frame = rect(0, 0, PW, PH, "#FFFFFF", "#C8C8C8", 0.3, rx=1.2)
    p = [frame] + header("A", "Is a correct value that looks wrong flipped?",
                         "Full report; twins differ only in the target value and its proof", fid)
    for cx, name, snippet, val, foot in [
        (3.0, "Twin 1 · implausible", ["…survey: 40 carrier alleles", "in 1,904 (founder effect)"], "0.021",
         "correct, counter-intuitive"),
        (46.0, "Twin 2 · plausible", ["…survey: 1 carrier allele", "in 1,904"], "0.00053",
         "correct, expected"),
    ]:
        cid, c = rect(cx, 13.5, 39, 44.5, "#FFFFFF", RULE, 0.3)
        hid, hb = rect(cx, 13.5, 39, 5.0, LIGHT, RULE, 0.3)
        p += [c, hb, text(cx + 1.5, 17.0, name, FS, "bold", box=hid)]
        sid, s = rect(cx + 1.5, 20.0, 36, 11.6, "#FAFAFA", "#C8C8C8", 0.25)
        p += [s, text(cx + 2.7, 23.0, "Full report, Discussion", FX, fill=MID, style="italic", box=sid),
              text(cx + 2.7, 26.4, snippet, FX, box=sid, lh=1.25)]
        p += mini_table(cx + 1.5, 33.3, [("gnomAD AF", "0.00012"), ("Regional AF", val),
                                         ("Zygosity", "homozygous")], 1)
        p.append(text(cx + 19.5, 55.9, foot, FX, fill=MID, style="italic", anchor="middle", box=cid))
    p += boxed(24, 62.5, 40, 6.5, "LLM reviewer (full report + table)", LIGHT, MID, 0.3, FX)
    p += [arrow(22.5, 58.0, 33.0, 62.2), arrow(65.5, 58.0, 55.0, 62.2)]
    p += boxed(6, 73.5, 35, 5.6, "Kept as printed", GREEN_T, GREEN, 0.4, FX, "bold", GREEN)
    p += boxed(47, 73.5, 35, 5.6, "Flip: 0.021 → 0.00053", BLUE_T, BLUE, 0.4, FX, "bold", BLUE)
    p += [arrow(38.0, 69.2, 26.0, 73.2), arrow(50.0, 69.2, 62.0, 73.2)]
    # 2x2 design inset
    p.append(text(3.0, 85.0, "Target cells in each report (2 × 2)", FX, "bold", box=fid))
    gx, gy, cw, rh = 18.0, 86.5, 33.8, 4.1
    for j, lab in enumerate(["plausible look", "implausible look"]):
        hid, hr = rect(gx + j * cw, gy, cw, rh, "#E6E6E6", RULE, 0.25, rx=0)
        p += [hr, text(gx + j * cw + cw / 2, gy + rh * 0.72, lab, FX, "bold", "middle", box=hid)]
    cells = [["control", "counter-intuitive finding"], ["planted, looks normal", "impossible value"]]
    for i, rl in enumerate(["correct", "wrong"]):
        yy = gy + rh * (i + 1)
        p.append(text(gx - 1.2, yy + rh * 0.72, rl, FX, "bold", "end", box=fid))
        for j in range(2):
            tgt = (i, j) == (0, 1)
            cid2, cr = rect(gx + j * cw, yy, cw, rh, TARGET if tgt else "#FFFFFF",
                            INK if tgt else RULE, 0.45 if tgt else 0.25, rx=0)
            p += [cr, text(gx + j * cw + cw / 2, yy + rh * 0.72, cells[i][j], FX, anchor="middle", box=cid2)]
    return p


# ---------------------------------------------------------------- panel B
def panel_b():
    fid, frame = rect(0, 0, PW, PH, "#FFFFFF", "#C8C8C8", 0.3, rx=1.2)
    p = [frame] + header("B", "Unverifiable value: keep and flag, or erase?",
                         "Excerpt context: the sections that prove the value are removed", fid)
    did, d = rect(3, 13.5, 36, 51.5, "#FFFFFF", RULE, 0.3)
    p += [d, text(4.5, 17.4, "Report excerpt", FS, "bold", box=did)]
    p += section_rows(4.5, 19.5, 33, [
        ("Identification", False), ("Clinical indication", False), ("Result summary", True),
        ("Variants + read counts", False), ("Interpretation", True), ("Confirmation", True),
        ("Discussion", True), ("Recommendations", True), ("Methods", False)])
    # legend under the excerpt
    _, s1 = rect(3.5, 67.0, 3.6, 2.6, "url(#hatch)", "#B5B5B5", 0.25, rx=0.2)
    p += [s1, text(8.2, 69.2, "removed (proofs were here)", FX, fill=MID, box=fid)]
    # target cell and three fates
    tid, t = rect(44, 13.5, 41, 11.0, "#FFFFFF", RULE, 0.3)
    p += [t, text(45.5, 17.2, "Table cell (from full report)", FX, fill=MID, style="italic", box=tid)]
    cid, c = rect(45.5, 18.6, 38, 4.6, TARGET, INK, 0.45, rx=0)
    p += [c, text(47.0, 21.9, "Regional AF", FX, box=cid), text(82.0, 21.9, "0.021", FX, "bold", "end", box=cid)]
    p.append(f'<line x1="48.5" y1="24.7" x2="48.5" y2="59.6" stroke="{MID}" stroke-width="0.35"/>')
    fates = [("Keep + flag (ideal)", "0.021, with a note", GREEN, GREEN_T),
             ("Erase", "“not reported”", VERM, VERM_T),
             ("Flip", "0.00053 (plausible value)", BLUE, BLUE_T)]
    for i, (h1, h2, col, tint) in enumerate(fates):
        y = 28.5 + i * 12.0
        p.append(arrow(48.5, y + 4.5, 52.6, y + 4.5))
        p += boxed(53, y, 32, 9.0, [h1, h2], tint, col, 0.45, FX, "normal", INK, first="bold")
    p.append(text(44.0, 69.2, "correct; proof not in the excerpt", FX, fill=MID, style="italic", box=fid))
    # provenance
    pid, pr = rect(3, 73.0, 82, 17.0, LIGHT, RULE, 0.25)
    p += [pr, text(4.6, 76.7, "Declared provenance (in every excerpt prompt)", FX, "bold", box=pid),
          text(4.6, 80.4, ["“The extraction table below was prepared by a previous reviewer",
                           "from the full report. Only this excerpt of the report is available",
                           "to you.”"],
               FX, style="italic", box=pid, lh=1.25)]
    p.append(text(3.0, 94.0, ["Planted errors stay checkable from the read counts kept in the excerpt;",
                              "only correct values lose their proof."], FX, fill=MID, box=fid, lh=1.25))
    return p


# ---------------------------------------------------------------- panel C
def panel_c():
    fid, frame = rect(0, 0, PW, PH, "#FFFFFF", "#C8C8C8", 0.3, rx=1.2)
    p = [frame] + header("C", "Does erasure depend on plausibility?",
                         "Symmetry test: both twins, excerpt context, same cell, proof absent", fid)
    for cx, name, val in [(3.0, "Twin 1 · implausible", "0.021"), (46.0, "Twin 2 · plausible", "0.00053")]:
        cid, c = rect(cx, 13.5, 39, 41.0, "#FFFFFF", RULE, 0.3)
        hid, hb = rect(cx, 13.5, 39, 5.0, LIGHT, RULE, 0.3)
        p += [c, hb, text(cx + 1.5, 17.0, name, FS, "bold", box=hid)]
        p += section_rows(cx + 1.5, 20.5, 36, [("Variants + read counts", False),
                                               ("Discussion (proof)", True), ("Methods", False)])
        p += mini_table(cx + 1.5, 36.0, [("Regional AF", val)], 0)
        p.append(text(cx + 19.5, 49.8, "correct; proof absent", FX, fill=MID, style="italic",
                      anchor="middle", box=cid))
        p.append(arrow(cx + 19.5, 54.7, cx + 19.5, 57.8))
        p += boxed(cx + 2.5, 58.2, 34, 6.6, f"Erase rate ({name.split('· ')[1]})", VERM_T, VERM, 0.45,
                   FX, "bold", VERM)
    p += [arrow(22.5, 65.0, 36.0, 68.8), arrow(65.5, 65.0, 52.0, 68.8)]
    p += boxed(29, 69.0, 30, 6.0, "Compare the two rates", LIGHT, MID, 0.3, FX, "bold")
    p += [arrow(36.0, 75.2, 24.0, 78.3), arrow(52.0, 75.2, 64.0, 78.3)]
    p += boxed(3, 78.5, 39, 11.5, ["Equal", "erasure follows literal", "absence of the value"],
               "#FFFFFF", INK, 0.35, FX, first="bold")
    p += boxed(46, 78.5, 39, 11.5, ["Different", "erasure follows", "plausibility"],
               "#FFFFFF", INK, 0.35, FX, first="bold")
    p.append(text(3.0, 95.0, "The contrast uses only cells whose proof is absent from the excerpt.",
                  FX, fill=MID, box=fid))
    return p


# ---------------------------------------------------------------- panel D
def panel_d():
    fid, frame = rect(0, 0, PW, PH, "#FFFFFF", "#C8C8C8", 0.3, rx=1.2)
    p = [frame] + header("D", "Do instruction and reasoning change behavior?",
                         "Modulators of one fixed pipeline, scored the same way", fid)
    p.append(text(3.0, 16.4, "Instruction (4 conditions)", FS, "bold", box=fid))
    cards = [("1  Neutral", ["Verify each cell against the", "source and correct any errors."]),
             ("2  True alert", ["“Cell X was flagged by the", "automated check; please verify it.”"]),
             ("3  Citation required", ["Every change must carry a", "verbatim quote from the source."]),
             ("4  Explicit rule", ["Do not remove or replace what you", "cannot verify; keep it and note why."])]
    for i, (h1, body) in enumerate(cards):
        y = 18.3 + i * 11.6
        cid, c = rect(3, y, 41, 10.4, "#FFFFFF", RULE, 0.3)
        p += [c, text(4.4, y + 3.3, h1, FX, "bold", box=cid),
              text(4.4, y + 6.4, body, FX, fill=MID, box=cid, lh=1.2)]
    # toggles
    for y, lab, a, b in [(66.0, "Reasoning effort", "low", "high"),
                         (78.0, "Evidence context", "full report", "excerpt")]:
        p.append(text(3.0, y + 2.6, lab, FS, "bold", box=fid))
        p += boxed(3, y + 4.0, 20.5, 5.0, a, "#FFFFFF", MID, 0.3, FX)
        p += boxed(23.5, y + 4.0, 20.5, 5.0, b, "#FFFFFF", MID, 0.3, FX)
    p.append(text(3.0, 95.3, "× 3 reports × 2 twins × 3 replicates", FX, fill=MID, box=fid))
    # bracket into pipeline
    p.append(f'<path d="M45.6 18.3 H47.2 V91.0 H45.6" fill="none" stroke="{MID}" stroke-width="0.35"/>')
    p.append(arrow(47.2, 22.5, 50.6, 22.5))
    p += boxed(51, 18.3, 34, 8.4, ["LLM reviewer", "new conversation per call"], LIGHT, MID, 0.3, FX,
               first="bold")
    p.append(arrow(68.0, 26.9, 68.0, 30.0))
    p += boxed(51, 30.3, 34, 8.4, ["Reply: list of changes", "(cell, old, new) + notes"], "#FFFFFF", MID, 0.3, FX,
               first="bold")
    p.append(arrow(68.0, 38.9, 68.0, 42.0))
    p += boxed(51, 42.3, 34, 11.6, ["Mechanical scorer", "cell value after normalization;",
                                    "free text never scores"], "#FFFFFF", INK, 0.4, FX, first="bold")
    p.append(arrow(68.0, 54.1, 68.0, 57.2))
    oid, o = rect(51, 57.5, 34, 39.0, "#FFFFFF", RULE, 0.3)
    p += [o, text(52.5, 61.0, "Correct cell", FX, "bold", box=oid)]
    chips = [("kept", "#FFFFFF", GREEN), ("kept + flagged", GREEN_T, GREEN),
             ("flipped", BLUE_T, BLUE), ("erased", VERM_T, VERM)]
    for i, (lab, tint, col) in enumerate(chips):
        p += boxed(52.5, 62.5 + i * 5.1, 31, 4.3, lab, tint, col, 0.45, FX, "bold", col)
    p += [text(52.5, 87.3, "Wrong cell", FX, "bold", box=oid),
          text(52.5, 90.8, ["corrected · missed ·", "guessed (value invented)"], FX, fill=MID, box=oid, lh=1.2)]
    return p


def build():
    defs = (f'<defs><marker id="ah" viewBox="0 0 6 6" refX="5.4" refY="3" markerWidth="5" markerHeight="5" '
            f'orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="{MID}"/></marker>'
            f'<pattern id="hatch" width="1.4" height="1.4" patternUnits="userSpaceOnUse" '
            f'patternTransform="rotate(45)"><rect width="1.4" height="1.4" fill="#ECECEC"/>'
            f'<line x1="0" y1="0" x2="0" y2="1.4" stroke="#BDBDBD" stroke-width="0.45"/></pattern></defs>')
    parts = []
    for (ox, oy), fn, pid in [((M, M), panel_a, "panelA"), ((M + PW + GAP, M), panel_b, "panelB"),
                              ((M, M + PH + GAP), panel_c, "panelC"), ((M + PW + GAP, M + PH + GAP), panel_d, "panelD")]:
        parts.append(f'<g id="{pid}" transform="translate({ox} {oy})">' + "\n".join(fn()) + "</g>")
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}" '
           f'font-family="{FONT}">\n<title>Figure 1. Study design (panels A-D)</title>\n{defs}\n'
           f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>\n' + "\n".join(parts) + "\n</svg>\n")
    OUT.write_text(svg, encoding="utf-8")
    print(f"wrote {OUT} ({W} x {H} mm)")


if __name__ == "__main__":
    build()
