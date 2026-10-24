# Conferência do resumo reescrito (commit 23f3019) contra os dados

Conferido em 24/10/2026 contra `docs/figures/results-figures-data.csv`, `runs/*.graded.jsonl` e
`runs/REPORT-pilot-2026-10-24.md`. Só itens que divergem ou precisam de ajuste; o resto bate.

| onde | texto atual | dado | ajuste sugerido |
|---|---|---|---|
| 3.2, 1º parágrafo | "todos os doze modelos de raciocínio atingiram desempenho perfeito" no laudo completo | 11 sim; Claude Haiku 5.5 (raciocínio desligado) apagou 10 células corretas e deixou passar 18 erros plantados (4 corrigidos para outro valor errado) em 72 respostas | "onze dos doze"; citar Haiku como exceção (Fig. 2A mostra flip = 0, não erase) |
| Resumo e 3.4 | GPT-6.1 Sol apaga "100% das células elegíveis" / "27/27" | denominador da Fig. 3 e Fig. 5 é 36 por gêmeo (27/36 = 75%); 27/27 só vale excluindo as 9 células de sexo registrado, que constam no cabeçalho do trecho | usar 27/36 (75%) como na figura, ou explicar o denominador 27 na primeira vez |
| Resumo (Métodos) e 3.4 | custo em tokens "2 a 21 vezes" / "1,7× e 21,5×" | razão high/low vai de 1,1× (DeepSeek V4 Pro) a 21,5× (Gemini 3.8 Flash); Haiku 1,4×, Opus 1,9× | "1,1× a 21,5×" |
| Resumo (Resultados 1) | "11 trocas em 60 oportunidades com laudo completo" | 11/60 inclui a condição keep rule; a Fig. 2A mostra 8/45 (três condições sem regra) | manter 11/60 só se disser "quatro condições", ou usar 8/45 como na figura |
| 2.4 | "32 testes de unidade" | 33 | 33 |
| 2.1 | "29 a 36 campos não-alvo" | tabelas de 33 a 40 células; conferir contagem de alvos por cenário antes de fixar a faixa | conferir |
| Tabela 1, coluna "Mantidas e Sinalizadas" | 27/36 etc. | são contagens do gêmeo implausível apenas | dizer "gêmeo implausível" no cabeçalho |
| rodapé | links `file:///C:/Users/gbbarra/llm-reviewer-discipline-eval/...` | caminho local inexistente | links relativos `docs/figures/` e `plausibility_eval/` |

Confirmados: zero palpites (guess) em 3.019 respostas analisadas; edições colaterais do GPT-6.1 Sol e Sol Pro
sob keep rule = 0,0 por resposta; Tabela 2 (apagamento off/low/high e tokens) bate com a Fig. 6; 1 flip em
970 células nos 12 modelos com raciocínio (Haiku off, 0,18 → 0,19); laudos de 1.318 a 1.718 palavras.

**Atualização (24/10, mesmo dia):** os oito ajustes acima foram aplicados no resumo (commit seguinte a d351fc4).
Faixa de células não-alvo conferida: 28 a 36 (tabelas de 33 a 40 células com 4 a 5 alvos).
