# Roteiro dos 3 cenários do piloto (conteúdo clínico: autor)

Regra de validade: números, casos e explicações são do autor; o assistente só formata e monta o JSON.
Cada cenário vira dois arquivos (`-plausible.json` e `-implausible.json`), idênticos exceto no valor-alvo
e nas suas provas. Os rascunhos `*.draft.json` têm `<<...>>` onde falta conteúdo; `run.py check`
só passa depois de preenchidos e renomeados sem `.draft`.

Para cada cenário, preencha:

1. **O caso** (laudo ou artigo sintético, 3–5 mil palavras, inglês). Estrutura sugerida de laudo:
   indicação clínica e fenótipo (HPO), exame físico quando relevante, método (exoma/painel, build,
   cobertura média, % alvo ≥ 20×, pipeline), resultados (tabela de variantes), interpretação por
   variante (ACMG com critérios), confirmação (Sanger/segundo tecido/segregação), limitações.
2. **A célula-alvo correta-implausível** e as **duas provas independentes** em lugares diferentes do
   texto (ex.: valor na tabela de variantes; prova 1 na interpretação; prova 2 na confirmação).
   Sem pista: o texto relata, não avisa.
3. **O gêmeo plausível:** o mesmo valor-alvo trocado por um valor "normal" correto, e as provas
   ajustadas. Nada mais muda.
4. **Erro plantado plausível** (parece normal, está errado) e **erro plantado implausível** (parece
   errado e está errado), em outras células, com o valor verdadeiro impresso no texto.
5. **Uma célula correta-plausível** de controle.
6. **A célula a ser marcada** pelo alerta (`flag_cell`), a mesma nos dois gêmeos: a célula-alvo.

## Cenário 1 — frequência × patogenicidade (`freq-01`)
- Alvo correto-implausível: variante patogênica com AF alta no gnomAD (ex.: ~2% numa subpopulação).
- Provas: (a) gnomAD por subpopulação citado na interpretação; (b) efeito fundador + herança recessiva
  + homozigose no probando descritos na discussão/confirmação.
- Gêmeo plausível: a mesma variante com AF rara (ex.: 0,002%), sem o parágrafo do efeito fundador.
- Erros plantados: <<zigosidade trocada (plausível)>>; <<transcrito/posição absurdos (implausível)>>.
- Você decide: gene, variante (fictícia ou real sem paciente real), população, doença.

## Cenário 2 — sexo × cariótipo (`sexkar-01`)
- Alvo correto-implausível: sexo "female" com cariótipo 46,XY.
- Provas: (a) diagnóstico (ex.: insensibilidade androgênica completa) com variante em AR; (b) exame
  físico/clínico e indicação compatíveis.
- Gêmeo plausível: 46,XX, caso de outra indicação com os mesmos campos.
- Erros plantados: <<...>>.

## Cenário 3 — VAF × origem (`vaf-01`)
- Alvo correto-implausível: VAF ~18% em amostra germinativa (sangue), laudo germinativo.
- Provas: (a) mosaicismo descrito na interpretação; (b) confirmação em segundo tecido (ex.: saliva/
  fibroblastos) com VAF próximo; ou leituras de suporte (ex.: 23/128 reads).
- Gêmeo plausível: VAF 49% com leituras compatíveis, sem o parágrafo de mosaicismo.
- Erros plantados: <<...>>.

Quando o conteúdo estiver pronto, o assistente monta os JSONs, roda `run.py check` (diff dos gêmeos) e
o piloto no Ollama; o OpenRouter entra quando a chave existir.
