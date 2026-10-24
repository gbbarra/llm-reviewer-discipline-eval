"""Results figures of the pilot (Fig. 2-6, Fig. S1), regenerated from runs/*.graded.jsonl and the raw logs.

    python docs/figures/make_results_figs.py          # prints the aggregate tables, writes SVG + PNG + CSV

Rules (the same as the text and plausibility_eval/report.py):
- excerpt: the twin contrast on correct cells uses evidence-absent cells only; full report: all correct cells.
- flip = 'switched' on a correct cell; erase = 'removed'; flag = 'kept_flagged'; kept = 'kept'.
- miss = 'missed' | 'missed_flagged' | 'miscorrected' on a provable wrong cell (success not null).
- collateral = mean of `collateral` per reply (format failures excluded; there are none).
- tokens = mean usage.completion_tokens per reply, raw logs, type == 'result', first record per job_key.
- 95% intervals: Wilson.
Inputs used: runs/excerpt-*, excerptR-*, excerptH-*, pilotB-*.
Not used: pilot-* (earlier round without provenance), excerptA-*/excerptC-* (preliminary narrow-cut round,
left out of the paper), smoke-*, test-*, *gemma*.
"""
from __future__ import annotations

import csv
import glob
import json
import math
import os
import re
from collections import Counter, defaultdict

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch, Rectangle  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
RUNS = os.path.join(ROOT, "runs")

# palette of Fig. 1 (Okabe-Ito): green = keep/flag, vermilion = erase, blue = switch, grey = keep without note
GREEN, VERM, BLUE = "#009E73", "#D55E00", "#0072B2"
GREY = "#BDBDBD"
INK, MID, RULE = "#1A1A1A", "#555555", "#9A9A9A"
HILITE = "#F7EFA0"  # same yellow as the target cells of Fig. 1, used to mark Llama 4 Maverick
MM = 1 / 25.4
W2 = 180 * MM  # two-column width

plt.rcParams.update({
    "font.family": "sans-serif", "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "font.size": 7, "axes.titlesize": 7.5, "axes.labelsize": 7, "xtick.labelsize": 7, "ytick.labelsize": 7,
    "legend.fontsize": 7, "axes.edgecolor": RULE, "axes.linewidth": 0.5, "xtick.color": MID,
    "ytick.color": INK, "xtick.major.width": 0.5, "ytick.major.width": 0.5, "xtick.major.size": 2.5,
    "ytick.major.size": 0, "axes.labelcolor": INK, "text.color": INK, "svg.fonttype": "none",
    "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white",
    "axes.titlelocation": "left", "axes.titleweight": "bold", "axes.titlepad": 4,
})

MODELS = {  # file id -> label
    "opus55": "Claude Opus 5.5", "sonnet55": "Claude Sonnet 5.5", "haiku55": "Claude Haiku 5.5",
    "gpt61solpro": "GPT-6.1 Sol Pro", "gpt61sol": "GPT-6.1 Sol", "gpt6luna": "GPT-6 Luna",
    "gemini4argon": "Gemini 4 Argon", "gemini38flash": "Gemini 3.8 Flash", "grok47": "Grok 4.7",
    "qwen38max": "Qwen 3.8 Max", "deepseekv4pro": "DeepSeek V4 Pro", "deepseekv41flash": "DeepSeek V4.1 Flash",
    "llama4maverick": "Llama 4 Maverick",
}
LLAMA = "llama4maverick"
NORULE = ("neutral", "flagged", "flagged_cite")
CONDS = ("neutral", "flagged", "flagged_cite", "keep_rule")
COND_LABEL = {"neutral": "neutral", "flagged": "flagged", "flagged_cite": "flagged + cite",
              "keep_rule": "keep rule"}
REASON = {"noreason": "off", "lowreason": "low", "highreason": "high"}
MISS = {"missed", "missed_flagged", "miscorrected"}


def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"),) * 3
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return p, max(0.0, c - h), min(1.0, c + h)


def read_jsonl(path):
    with open(path, encoding="utf8") as f:
        return [json.loads(line) for line in f if line.strip()]


def load_graded(prefix):
    """{(model_id, reasoning): [records]} for runs/<prefix>-<model>-<reasoning>.graded.jsonl."""
    out = {}
    for p in sorted(glob.glob(os.path.join(RUNS, f"{prefix}-*.graded.jsonl"))):
        m = re.fullmatch(rf"{prefix}-([a-z0-9]+)-([a-z]+)\.graded\.jsonl", os.path.basename(p))
        if not m or "gemma" in p or m.group(1) not in MODELS:
            continue
        recs, seen = [], set()
        for r in read_jsonl(p):
            if r["job_key"] not in seen:
                seen.add(r["job_key"])
                recs.append(r)
        out[(m.group(1), m.group(2))] = recs
    return out


def load_tokens(prefix, mid, reasoning):
    """{job_key: (completion_tokens, cost_usd)} from the raw log, first 'result' record per job_key."""
    out = {}
    for r in read_jsonl(os.path.join(RUNS, f"{prefix}-{mid}-{reasoning}.jsonl")):
        if r.get("type") == "result" and r["job_key"] not in out:
            out[r["job_key"]] = ((r.get("usage") or {}).get("completion_tokens"), r.get("cost_usd"))
    return out


def twin_cells(*sources):
    """{scenario_id: cell_ids} of the twin contrast: the cells that are correct-implausible in the implausible
    twin (their counterparts in the plausible twin carry kind correct_plausible). The other correct-plausible
    cells are controls present in both twins and are not part of the contrast."""
    out = defaultdict(set)
    for src in sources:
        for recs in src.values():
            for r in recs:
                if r["twin"] == "implausible":
                    for t in r["targets"]:
                        if t["kind"] == "correct_implausible":
                            out[r["scenario_id"]].add(t["cell_id"])
    return out


def correct_cells(recs, conds, twin, absent_only):
    """Outcomes on the twin-contrast cells; excerpt: evidence-absent ones only. Format failures excluded."""
    c = Counter()
    for r in recs:
        if r["condition"] in conds and r["twin"] == twin and not r["format_failure"]:
            for t in r["targets"]:
                if t["cell_id"] in TWIN_CELLS[r["scenario_id"]] and (t.get("evidence_absent") or not absent_only):
                    c[t["outcome"]] += 1
    return c


def miss_cells(recs, conds):
    k = n = 0
    for r in recs:
        if r["condition"] in conds and not r["format_failure"]:
            for t in r["targets"]:
                if t["kind"].startswith("wrong") and t["success"] is not None:
                    n += 1
                    k += t["outcome"] in MISS
    return k, n


def collateral(recs, conds):
    v = [r["collateral"] or 0 for r in recs if r["condition"] in conds and not r["format_failure"]]
    return (sum(v) / len(v) if v else float("nan")), len(v)


# ---------------------------------------------------------------- data
EXC = load_graded("excerpt")      # main excerpt round: one reasoning setting per model
EXR = load_graded("excerptR")     # within-model off/low variants
EXH = load_graded("excerptH")     # high effort, neutral only
FULL = load_graded("pilotB")      # full report with provenance

TWIN_CELLS = twin_cells(EXC, FULL)
FORMAT_FAILURES = sorted((p, mid, rs, r["job_key"]) for p, src in (("excerpt", EXC), ("excerptR", EXR), ("excerptH", EXH),
                                                                  ("pilotB", FULL))
                         for (mid, rs), recs in src.items() for r in recs if r["format_failure"])

main_exc = {mid: (rs, recs) for (mid, rs), recs in EXC.items()}
main_full = {mid: (rs, recs) for (mid, rs), recs in FULL.items()}
assert set(main_exc) == set(MODELS) == set(main_full), (set(main_exc), set(main_full))

ROWS = []  # long-format CSV rows


def row(fig, mid, metric, k=None, n=None, value=None, **kw):
    d = {"figure": fig, "model": MODELS.get(mid, mid), "model_id": mid, "metric": metric,
         "reasoning": kw.pop("reasoning", ""), "context": kw.pop("context", ""),
         "conditions": kw.pop("conditions", ""), "twin": kw.pop("twin", ""), "k": k, "n": n}
    if k is not None and n:
        p, lo, hi = wilson(k, n)
        d.update(value=round(p, 4), ci_low=round(lo, 4), ci_high=round(hi, 4))
    else:
        d.update(value=None if value is None else round(value, 4), ci_low=None, ci_high=None)
    d.update(kw)
    ROWS.append(d)
    return d


# excerpt, three no-rule conditions, evidence-absent correct cells, per twin
EXC_AGG = {}
for mid, (rs, recs) in main_exc.items():
    a = {"reasoning": REASON[rs]}
    for tw in ("implausible", "plausible"):
        c = correct_cells(recs, NORULE, tw, True)
        a[tw] = c
    a["miss"] = miss_cells(recs, NORULE)
    a["coll"] = collateral(recs, NORULE)
    a["by_cond"] = {}
    for cond in CONDS:
        ci = correct_cells(recs, (cond,), "implausible", True)
        cp = correct_cells(recs, (cond,), "plausible", True)
        a["by_cond"][cond] = (ci["removed"] + cp["removed"], sum(ci.values()) + sum(cp.values()),
                              ci["kept_flagged"] + cp["kept_flagged"])
    EXC_AGG[mid] = a

FULL_AGG = {}
for mid, (rs, recs) in main_full.items():
    FULL_AGG[mid] = {"reasoning": REASON[rs],
                     "implausible": correct_cells(recs, NORULE, "implausible", False),
                     "plausible": correct_cells(recs, NORULE, "plausible", False),
                     "implausible4": correct_cells(recs, CONDS, "implausible", False),
                     "plausible4": correct_cells(recs, CONDS, "plausible", False),
                     "coll": collateral(recs, NORULE), "miss": miss_cells(recs, NORULE)}


KEEP_I = {}  # keep_rule, implausible twin: (erase, flag), as in the README column
for mid, (rs, recs) in main_exc.items():
    c = correct_cells(recs, ("keep_rule",), "implausible", True)
    KEEP_I[mid] = (c["removed"], c["kept_flagged"])


def erase_pooled(mid):
    a = EXC_AGG[mid]
    return (a["implausible"]["removed"] + a["plausible"]["removed"],
            sum(a["implausible"].values()) + sum(a["plausible"].values()))


# display order: ascending erasure under partial evidence (Fig. 3), ties by more flagging
ORDER = sorted(MODELS, key=lambda m: (erase_pooled(m)[0],
                                      -(EXC_AGG[m]["implausible"]["kept_flagged"] + EXC_AGG[m]["plausible"]["kept_flagged"]),
                                      MODELS[m]))

# reasoning ladder, excerpt, neutral condition
LADDER = defaultdict(dict)  # mid -> level -> dict
for src, prefix in ((EXC, "excerpt"), (EXR, "excerptR"), (EXH, "excerptH")):
    for (mid, rs), recs in src.items():
        lvl = REASON[rs]
        ci = correct_cells(recs, ("neutral",), "implausible", True)
        cp = correct_cells(recs, ("neutral",), "plausible", True)
        tok = load_tokens(prefix, mid, rs)
        keys = [r["job_key"] for r in recs if r["condition"] == "neutral"]
        toks = [tok[k][0] for k in keys if k in tok and tok[k][0] is not None]
        costs = [tok[k][1] for k in keys if k in tok and tok[k][1] is not None]
        assert len(toks) == len(keys), (prefix, mid, rs, len(toks), len(keys))
        LADDER[mid][lvl] = {"erase_i": (ci["removed"], sum(ci.values())), "erase_p": (cp["removed"], sum(cp.values())),
                            "flag": ci["kept_flagged"] + cp["kept_flagged"], "flip_i": ci["switched"],
                            "coll": collateral(recs, ("neutral",))[0], "replies": len(keys),
                            "tokens": sum(toks) / len(toks),
                            "cost": sum(costs) / len(costs) if costs else float("nan"), "source": prefix}


# ---------------------------------------------------------------- print + check
def tables():
    print("\n== Excerpt, three no-rule conditions, evidence-absent correct cells (per twin) ==")
    print(f"{'model':22} {'rs':4} {'flip I/P':>9} {'erase I/P':>10} {'flag':>7} {'kept':>7} {'coll':>5} {'miss':>7}"
          f" | keep_rule erase/flag   | full: flip I(3c) I(4c) P(4c) erase(4c) coll")
    for m in ORDER:
        a, f = EXC_AGG[m], FULL_AGG[m]
        i, p = a["implausible"], a["plausible"]
        n = sum(i.values())
        kr = a["by_cond"]["keep_rule"]
        print(f"{MODELS[m]:22} {a['reasoning']:4} {i['switched']:>3}/{p['switched']:<3}/{n:<2}"
              f" {i['removed']:>3}/{p['removed']:<3}"
              f" {i['kept_flagged'] + p['kept_flagged']:>3}/{n:<3}"  # flag pooled? printed both below
              f" {i['kept']:>3}/{p['kept']:<3} {a['coll'][0]:5.1f} {a['miss'][0]:>3}/{a['miss'][1]:<3}"
              f" | {kr[0]:>2}/{kr[1]} flag {kr[2]:>2}      "
              f" | {f['implausible']['switched']}/{sum(f['implausible'].values())}"
              f"  {f['implausible4']['switched']}/{sum(f['implausible4'].values())}"
              f"  {f['plausible4']['switched']}/{sum(f['plausible4'].values())}"
              f"  {f['implausible4']['removed'] + f['plausible4']['removed']}"
              f"/{sum(f['implausible4'].values()) + sum(f['plausible4'].values())}"
              f"  {f['coll'][0]:.2f}")
        print(f"{'':27} flag I {i['kept_flagged']}/{n}, P {p['kept_flagged']}/{sum(p.values())}")
    print("\n== Reasoning ladder, excerpt neutral (erase I/P of n per twin, flag, collateral, tokens) ==")
    for m in ORDER:
        s = []
        for lvl in ("off", "low", "high"):
            d = LADDER[m].get(lvl)
            if d:
                s.append(f"{lvl}: {d['erase_i'][0]}/{d['erase_p'][0]} of {d['erase_i'][1]} · {d['flag']} · "
                         f"{d['coll']:.1f} · {d['tokens']:,.0f} tok (n={d['replies']}, flip {d['flip_i']})")
        print(f"{MODELS[m]:22} " + " | ".join(s))
    flips12 = sum(EXC_AGG[m]["implausible"]["switched"] + FULL_AGG[m]["implausible"]["switched"]
                  for m in MODELS if m != LLAMA)
    opp12 = sum(sum(EXC_AGG[m]["implausible"].values()) + sum(FULL_AGG[m]["implausible"].values())
                for m in MODELS if m != LLAMA)
    print(f"\n12 models with a reasoning setting: {flips12}/{opp12} flips on correct implausible cells")
    return flips12, opp12


def checks(flips12, opp12):
    """Numbers quoted in README; a mismatch stops the script instead of being plotted."""
    e = lambda m: (EXC_AGG[m]["implausible"]["removed"], EXC_AGG[m]["plausible"]["removed"])
    fl = lambda m: EXC_AGG[m]["implausible"]["kept_flagged"]
    want = {
        "Opus excerpt erase 0/0": (e("opus55"), (0, 0)),
        "Opus excerpt flag (implausible) 27/36": ((fl("opus55"), sum(EXC_AGG["opus55"]["implausible"].values())), (27, 36)),
        "GPT-6.1 Sol excerpt erase 27/27": (e("gpt61sol"), (27, 27)),
        "GPT-6.1 Sol Pro excerpt erase 27/27": (e("gpt61solpro"), (27, 27)),
        "GPT-6 Luna excerpt erase 27/21": (e("gpt6luna"), (27, 21)),
        "Grok excerpt erase 17/17": (e("grok47"), (17, 17)),
        "Haiku excerpt erase 9/10": (e("haiku55"), (9, 10)),
        "Llama excerpt flip 7/36": ((EXC_AGG[LLAMA]["implausible"]["switched"], sum(EXC_AGG[LLAMA]["implausible"].values())), (7, 36)),
        "Llama full flip 11/60 (four conditions)": ((FULL_AGG[LLAMA]["implausible4"]["switched"], sum(FULL_AGG[LLAMA]["implausible4"].values())), (11, 60)),
        "Qwen high erase 3/3": ((LADDER["qwen38max"]["high"]["erase_i"][0], LADDER["qwen38max"]["high"]["erase_p"][0]), (3, 3)),
        "GPT-6.1 Sol high erase 3/7": ((LADDER["gpt61sol"]["high"]["erase_i"][0], LADDER["gpt61sol"]["high"]["erase_p"][0]), (3, 7)),
        "Gemini 3.8 Flash high erase 0/0": ((LADDER["gemini38flash"]["high"]["erase_i"][0], LADDER["gemini38flash"]["high"]["erase_p"][0]), (0, 0)),
        "Haiku off neutral erase 3/4": ((LADDER["haiku55"]["off"]["erase_i"][0], LADDER["haiku55"]["off"]["erase_p"][0]), (3, 4)),
        "keep_rule (implausible twin) erase/flag: Luna 9/0, Opus 0/9, Haiku 3/8, Llama 3/3": (
            tuple(KEEP_I[m] for m in ("gpt6luna", "opus55", "haiku55", LLAMA)), ((9, 0), (0, 9), (3, 8), (3, 3))),
        # README/text: 1/972 counts nominal opportunities; 2 evidence-absent cells sit in the two DeepSeek V4.1 Flash
        # excerpt replies that failed to parse (format failures, excluded here as in report.py) -> 970 parsed cells
        "12 models flips 1/972 (970 parsed)": ((flips12, opp12), (1, 970)),
        "Haiku full erase 8/60 (implausible, four conditions)": (
            (FULL_AGG["haiku55"]["implausible4"]["removed"], sum(FULL_AGG["haiku55"]["implausible4"].values())), (8, 60)),
        "Opus tokens low 567": (round(LADDER["opus55"]["low"]["tokens"]), 567),
        "Qwen tokens high 14,454": (round(LADDER["qwen38max"]["high"]["tokens"]), 14454),
    }
    print("  format failures (excluded from every rate):", FORMAT_FAILURES or "none")
    bad = []
    for name, (got, exp) in want.items():
        ok = got == exp
        print(f"  [{'ok' if ok else 'MISMATCH'}] {name}: got {got}")
        if not ok:
            bad.append(name)
    if bad:
        raise SystemExit(f"README check failed: {bad}")


# ---------------------------------------------------------------- figure helpers
def save(fig, name):
    for ext in ("svg", "png"):
        fig.savefig(os.path.join(HERE, f"{name}.{ext}"), dpi=300)
    plt.close(fig)
    print("wrote", name)


def clean(ax, grid_axis="x"):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.grid(axis=grid_axis, color="#E6E6E6", linewidth=0.5, zorder=0)
    ax.set_axisbelow(True)


def ylabels(ax, mids, bold=(LLAMA,)):
    ax.set_yticks(range(len(mids)))
    ax.set_yticklabels([MODELS[m] for m in mids])
    for lab, m in zip(ax.get_yticklabels(), mids):
        if m in bold:
            lab.set_fontweight("bold")
    ax.set_ylim(len(mids) - 0.5, -0.5)


def pct_axis(ax, lo=0, hi=1):
    ax.set_xlim(lo - 0.02, hi + 0.02)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_xticklabels(["0", "25", "50", "75", "100"])


# ---------------------------------------------------------------- Fig. 2
def fig2():
    fig = plt.figure(figsize=(W2, 92 * MM))
    gs = fig.add_gridspec(1, 2, wspace=0.08, left=0.155, right=0.985, top=0.92, bottom=0.11)
    axA, axB = fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1])
    for ax, agg, title, ctx in ((axA, FULL_AGG, "A  Full report: only Llama 4 Maverick flips correct values", "full"),
                                (axB, EXC_AGG, "B  Excerpt: the same model, the same flip", "excerpt")):
        clean(ax)
        llama_y = ORDER.index(LLAMA)
        ax.add_patch(Rectangle((-0.04, llama_y - 0.5), 1.08, 1, color=HILITE, zorder=0, lw=0))
        for y, m in enumerate(ORDER):
            for tw, dy, face in (("implausible", -0.17, BLUE), ("plausible", 0.17, "white")):
                c = agg[m][tw]
                k, n = c["switched"], sum(c.values())
                p, lo, hi = wilson(k, n)
                ax.plot([lo, hi], [y + dy] * 2, color=BLUE, lw=0.8, solid_capstyle="butt", zorder=2)
                ax.plot(p, y + dy, "o", ms=3.6, mfc=face, mec=BLUE, mew=0.8, zorder=3)
                if k:
                    ax.text(hi + 0.025, y + dy, f"{k}/{n}", va="center", fontsize=7, color=INK)
                row("fig2", m, "flip", k, n, context=ctx, twin=tw, reasoning=agg[m]["reasoning"],
                    conditions="neutral+flagged+flagged_cite")
        pct_axis(ax)
        ax.set_xlabel("Correct values replaced by another value (%), 95% CI")
        ax.set_title(title)
        n_i = sum(agg[ORDER[0]]["implausible"].values())
        ax.text(1.0, len(ORDER) - 0.75, f"n = {n_i} cells per twin per model", ha="right", va="bottom",
                fontsize=7, color=MID)
    ylabels(axA, ORDER)
    axB.set_yticks(range(len(ORDER)))
    axB.set_yticklabels([])
    axB.set_ylim(len(ORDER) - 0.5, -0.5)
    h = [Line2D([], [], marker="o", ls="", mfc=BLUE, mec=BLUE, ms=4, label="implausible twin"),
         Line2D([], [], marker="o", ls="", mfc="white", mec=BLUE, ms=4, label="plausible twin")]
    axB.legend(handles=h, loc="center right", bbox_to_anchor=(1.0, 0.62), ncol=1, frameon=False,
               handletextpad=0.3)
    save(fig, "fig2-plausibility-flip")


# ---------------------------------------------------------------- Fig. 3
CATS = [("kept", "kept, no note", GREY), ("kept_flagged", "kept and flagged", GREEN),
        ("removed", "erased", VERM), ("switched", "flipped", BLUE)]


def fig3():
    fig, ax = plt.subplots(figsize=(W2, 128 * MM))
    fig.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.08)
    clean(ax)
    ax.grid(False)
    ys, labels = [], []
    y = 0
    for m in ORDER:
        for tw, short in (("implausible", "I"), ("plausible", "P")):
            c = EXC_AGG[m][tw]
            n = sum(c.values())
            left = 0
            for key, _, col in CATS:
                w = c[key] / n
                if w:
                    ax.barh(y, w - 0.003, left=left + 0.0015, height=0.78, color=col, lw=0, zorder=2)
                    if w >= 0.06:
                        ax.text(left + w / 2, y, str(c[key]), ha="center", va="center", fontsize=7,
                                color="white" if key in ("kept_flagged", "removed", "switched") else INK)
                left += w
                row("fig3", m, key, c[key], n, context="excerpt", twin=tw, reasoning=EXC_AGG[m]["reasoning"],
                    conditions="neutral+flagged+flagged_cite", cells="evidence-absent correct")
            ax.text(1.012, y, f"{short}  n = {n}", va="center", fontsize=7, color=MID)
            ys.append(y)
            y += 1
        y += 0.55
    # model labels centred on each pair
    centers = [(ys[2 * i] + ys[2 * i + 1]) / 2 for i in range(len(ORDER))]
    ax.set_yticks(centers)
    ax.set_yticklabels([MODELS[m] for m in ORDER])
    for lab, m in zip(ax.get_yticklabels(), ORDER):
        if m == LLAMA:
            lab.set_fontweight("bold")
    ax.set_ylim(ys[-1] + 0.7, -0.7)
    ax.set_xlim(0, 1)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_xticklabels(["0", "25", "50", "75", "100"])
    ax.set_xlabel("Correct values whose proof is absent from the excerpt (%); I = implausible twin, P = plausible twin")
    fig.text(0.015, 0.985, "Under partial evidence, erasing is symmetric between twins: it follows the absence of "
             "the proof, not plausibility", ha="left", va="top", fontsize=7.5, fontweight="bold")
    h = [Patch(color=c, label=l) for _, l, c in CATS]
    fig.legend(handles=h, loc="lower left", bbox_to_anchor=(0.2, 0.905), ncol=4, frameon=False,
               handlelength=1.2, handletextpad=0.4, columnspacing=1.5)
    fig.text(0.9, 0.915, "excerpt · neutral, flagged, flagged + cite", ha="right", va="bottom", fontsize=7,
             color=MID)
    save(fig, "fig3-partial-evidence-outcomes")


# ---------------------------------------------------------------- Fig. 4
def fig4():
    fig, ax = plt.subplots(figsize=(W2 * 0.62, 92 * MM))
    fig.subplots_adjust(left=0.3, right=0.96, top=0.87, bottom=0.13)
    clean(ax)
    for y, m in enumerate(ORDER):
        e, ne = EXC_AGG[m]["coll"]
        f, nf = FULL_AGG[m]["coll"]
        ax.plot([f, e], [y, y], color="#CFCFCF", lw=1.2, zorder=1)
        ax.plot(f, y, "o", ms=4, mfc="white", mec=INK, mew=0.8, zorder=3)
        ax.plot(e, y, "o", ms=4, mfc=INK, mec=INK, zorder=3)
        ax.text(max(e, f) + 0.12, y, f"{e:.1f}", va="center", fontsize=7, color=MID)
        row("fig4", m, "collateral_per_reply", value=e, n=ne, context="excerpt", reasoning=EXC_AGG[m]["reasoning"],
            conditions="neutral+flagged+flagged_cite")
        row("fig4", m, "collateral_per_reply", value=f, n=nf, context="full", reasoning=FULL_AGG[m]["reasoning"],
            conditions="neutral+flagged+flagged_cite")
    ylabels(ax, ORDER)
    ax.set_xlim(-0.15, 6)
    ax.set_xlabel("Changes to non-target cells per reply (mean)")
    fig.text(0.02, 0.985, "Collateral edits appear only under partial evidence", ha="left", va="top",
             fontsize=7.5, fontweight="bold")
    h = [Line2D([], [], marker="o", ls="", mfc="white", mec=INK, ms=4, label="full report"),
         Line2D([], [], marker="o", ls="", mfc=INK, mec=INK, ms=4, label="excerpt")]
    fig.legend(handles=h, loc="lower left", bbox_to_anchor=(0.29, 0.875), ncol=2, frameon=False,
               handletextpad=0.3, columnspacing=1.2)
    fig.text(0.96, 0.885, "neutral, flagged, flagged + cite", ha="right", va="bottom", fontsize=7, color=MID)
    save(fig, "fig4-collateral-edits")


# ---------------------------------------------------------------- Fig. 5
ERASE_CMAP = LinearSegmentedColormap.from_list("erase", ["#FFFFFF", "#F8E0CF", VERM, "#7A3300"])


def fig5():
    fig, ax = plt.subplots(figsize=(W2 * 0.62, 100 * MM))
    fig.subplots_adjust(left=0.3, right=0.97, top=0.86, bottom=0.1)
    for y, m in enumerate(ORDER):
        for x, cond in enumerate(CONDS):
            k, n, flag = EXC_AGG[m]["by_cond"][cond]
            p = k / n
            ax.add_patch(Rectangle((x - 0.5, y - 0.5), 1, 1, facecolor=ERASE_CMAP(p * 0.85),
                                   edgecolor="white", lw=1.5))
            ax.text(x, y, f"{k}/{n}", ha="center", va="center", fontsize=7,
                    color="white" if p > 0.45 else INK)
            row("fig5", m, "erase", k, n, context="excerpt", conditions=cond, twin="both",
                reasoning=EXC_AGG[m]["reasoning"], flagged=flag)
    ax.axvline(2.5, color=INK, lw=0.8)
    ax.set_xlim(-0.5, 3.5)
    ax.set_xticks(range(4))
    ax.set_xticklabels([COND_LABEL[c] for c in CONDS])
    ax.xaxis.tick_top()
    ax.tick_params(axis="x", length=0, colors=INK)
    ylabels(ax, ORDER)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_title("One sentence (keep rule) stops erasure in 10 of 13 models", x=-0.42, pad=16)
    fig.text(0.97, 0.025, "Erased / evidence-absent correct cells, both twins, excerpt (9 replies per twin "
             "per condition)", ha="right", fontsize=7, color=MID)
    save(fig, "fig5-instruction-erasure")


# ---------------------------------------------------------------- Fig. 6
LEVELS = ("off", "low", "high")
LV_STYLE = {"off": dict(mfc="white", mec=INK), "low": dict(mfc="#9A9A9A", mec="#6A6A6A"),
            "high": dict(mfc=INK, mec=INK)}


def fig6():
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(W2, 98 * MM), sharey=True,
                                   gridspec_kw=dict(wspace=0.08))
    fig.subplots_adjust(left=0.155, right=0.98, top=0.86, bottom=0.12)
    order = ORDER
    for ax in (axA, axB):
        clean(ax)
        ax.add_patch(Rectangle((-1e9, order.index(LLAMA) - 0.5), 2e9, 1, color=HILITE, zorder=0, lw=0))
    for y, m in enumerate(order):
        lv = [l for l in LEVELS if l in LADDER[m]]
        er = []
        for l in lv:
            d = LADDER[m][l]
            k = d["erase_i"][0] + d["erase_p"][0]
            n = d["erase_i"][1] + d["erase_p"][1]
            er.append(k / n)
            row("fig6", m, "erase", k, n, context="excerpt", conditions="neutral", twin="both", reasoning=l,
                source=d["source"], flagged=d["flag"])
            row("fig6", m, "output_tokens_per_reply", value=d["tokens"], n=d["replies"], context="excerpt",
                conditions="neutral", reasoning=l, source=d["source"], cost_usd_per_reply=round(d["cost"], 5))
        tk = [LADDER[m][l]["tokens"] for l in lv]
        # jitter equal erasure values vertically so off/low/high stay visible
        offs = {"off": -0.22, "low": 0.0, "high": 0.22}
        for ax, vals in ((axA, er), (axB, tk)):
            ax.plot(vals, [y + offs[l] for l in lv], color="#B5B5B5", lw=0.8, zorder=1)
            for l, v in zip(lv, vals):
                ax.plot(v, y + offs[l], "o", ms=3.8, mew=0.8, zorder=3, **LV_STYLE[l])
        if len(lv) > 1 and lv[-1] == "high":
            r = tk[-1] / LADDER[m]["low"]["tokens"]
            axB.text(max(tk) * 1.12, y, f"×{r:.1f}", va="center", fontsize=7, color=MID)
    ylabels(axA, order)
    pct_axis(axA)
    axA.set_xlabel("Correct values erased, evidence-absent cells, both twins (%)")
    axA.set_title("A  More effort lowers erasure in some models, not all")
    axB.set_xscale("log")
    axB.set_xlim(250, 30000)
    axB.set_xticks([300, 1000, 3000, 10000])
    axB.set_xticklabels(["300", "1,000", "3,000", "10,000"])
    axB.minorticks_off()
    axB.set_xlabel("Output tokens per reply (mean, log scale)")
    ratios = [LADDER[m]["high"]["tokens"] / LADDER[m]["low"]["tokens"] for m in order
              if "high" in LADDER[m] and "low" in LADDER[m]]
    axB.set_title(f"B  …and costs ×{min(ratios):.1f} to ×{max(ratios):.0f} the output tokens (high / low)")
    h = [Line2D([], [], marker="o", ls="", ms=4, mew=0.8, label=f"reasoning {l}", **LV_STYLE[l]) for l in LEVELS]
    fig.legend(handles=h, loc="upper left", bbox_to_anchor=(0.155, 0.965), ncol=3, frameon=False,
               handletextpad=0.3, columnspacing=1.4)
    fig.text(0.98, 0.965, "excerpt · neutral · 12 cells per twin, 18 replies per level", ha="right",
             va="bottom", fontsize=7, color=MID)
    save(fig, "fig6-reasoning-effort")


# ---------------------------------------------------------------- Fig. S1
def figS1():
    metrics = [("flip", "flip\n(implausible)", BLUE, 1.0), ("erase", "erase", VERM, 1.0),
               ("flag", "flag", GREEN, 1.0), ("miss", "miss\n(provable error)", "#555555", 1.0),
               ("coll", "collateral\nedits / reply", "#555555", 6.0)]
    fig, ax = plt.subplots(figsize=(W2 * 0.7, 100 * MM))
    fig.subplots_adjust(left=0.27, right=0.98, top=0.84, bottom=0.09)
    for y, m in enumerate(ORDER):
        a = EXC_AGG[m]
        i, p = a["implausible"], a["plausible"]
        ni, nb = sum(i.values()), sum(i.values()) + sum(p.values())
        vals = {"flip": (i["switched"], ni), "erase": (i["removed"] + p["removed"], nb),
                "flag": (i["kept_flagged"] + p["kept_flagged"], nb), "miss": a["miss"], "coll": a["coll"]}
        for x, (key, _, col, vmax) in enumerate(metrics):
            if key == "coll":
                v, n = vals[key]
                txt = f"{v:.1f}"
                row("figS1", m, "collateral_per_reply", value=v, n=n, context="excerpt",
                    conditions="neutral+flagged+flagged_cite", reasoning=a["reasoning"])
            else:
                k, n = vals[key]
                v = k / n
                txt = f"{v * 100:.0f}"
                row("figS1", m, key, k, n, context="excerpt", conditions="neutral+flagged+flagged_cite",
                    reasoning=a["reasoning"], twin="implausible" if key == "flip" else "both")
            cm = LinearSegmentedColormap.from_list(key, ["#FFFFFF", col])
            frac = min(v / vmax, 1)
            ax.add_patch(Rectangle((x - 0.5, y - 0.5), 1, 1, facecolor=cm(0.08 + 0.8 * frac) if v else "#FFFFFF",
                                   edgecolor="#E6E6E6", lw=0.6))
            ax.text(x, y, txt, ha="center", va="center", fontsize=7, color="white" if frac > 0.55 else INK)
    ax.set_xlim(-0.5, len(metrics) - 0.5)
    ax.set_xticks(range(len(metrics)))
    ax.set_xticklabels([mm[1] for mm in metrics])
    ax.xaxis.tick_top()
    ax.tick_params(axis="x", length=0, colors=INK)
    ylabels(ax, ORDER)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_title("Under partial evidence the models differ in erasing and flagging, not in flipping",
                 x=-0.36, pad=24)
    fig.text(0.98, 0.025, "Excerpt, three no-rule conditions; rates in %, collateral as mean per reply",
             ha="right", fontsize=7, color=MID)
    save(fig, "figS1-metric-summary")


def write_csv():
    keys = ["figure", "model", "model_id", "reasoning", "context", "conditions", "twin", "metric", "k", "n",
            "value", "ci_low", "ci_high", "flagged", "cells", "source", "cost_usd_per_reply"]
    with open(os.path.join(HERE, "results-figures-data.csv"), "w", newline="", encoding="utf8") as f:
        w = csv.DictWriter(f, fieldnames=keys, extrasaction="raise")
        w.writeheader()
        for r in ROWS:
            w.writerow({k: r.get(k, "") for k in keys})
    print("wrote results-figures-data.csv", len(ROWS), "rows")


if __name__ == "__main__":
    checks(*tables())
    fig2(); fig3(); fig4(); fig5(); fig6(); figS1()
    write_csv()
