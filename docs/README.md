# docs/ — manuscript material

Everything a reader or an editor needs to rewrite or check the study text is here. The code and the raw
logs are one level up (`../plausibility_eval/`, `../runs/`).

| file | what it is | edit? |
|---|---|---|
| `RESUMO-IMRD-piloto-2026-10-24.pt.md` | the study summary in IMRaD form, Portuguese; the source text for the preprint | **yes** — this is the file to rewrite |
| `S1-prompts-sent-to-models.md` | the exact prompts (system + user) sent to the models, per scenario, twin and context | no (data) |
| `referencias-preprint.md` / `.bib` | 40 verified references, grouped by theme, with the section each supports | yes (add/remove with care) |
| `figures/fig1-methods-ABCD.svg|png` + `fig1-legend.md` | Figure 1, methods, panels A–D | legend yes; figure via `make_fig1.py` |
| `figures/fig2…fig6, figS1 .svg|png` | results figures | figure via `make_results_figs.py` |
| `figures/results-figures-legends.md` | legends of Figs 2–6 and S1, with n and metric definitions | yes |
| `figures/results-figures-data.csv` | every plotted number (k, n, rate, Wilson 95% CI) | no (generated) |
| `figures/make_results_figs.py` | regenerates Figs 2–6/S1 from `../runs/*.graded.jsonl`; stops if a README number no longer matches | code |
| `../README.md` | English overview with the results tables | yes |
| `../runs/REPORT-pilot-2026-10-24.md` | consolidated per-model report produced by `run.py report` | no (generated) |

Numbers in the text must trace to `figures/results-figures-data.csv` or to `../runs/REPORT-pilot-2026-10-24.md`.
Rules kept throughout the text: figure titles name the analysis, not the result; the preliminary narrow-cut
round (`runs/excerptA-*`, `excerptC-*`) and the local development runs (`runs/pilot-gemma12-*`, `smoke-*`) are
not part of the analysis; 3 of 3,022 replies were unparseable and are excluded from every rate.
