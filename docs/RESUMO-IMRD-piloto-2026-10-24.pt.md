# Comportamento de modelos de linguagem ao revisar dados extraídos sob evidência completa e parcial: viés de plausibilidade e perda de dados por apagamento

Estudo exploratório, outubro de 2026. Autor: Gustavo Barcelos Barra. Instrumento (código MIT), cenários,
prompts, registros brutos de todas as respostas e este texto (CC BY 4.0) estão no repositório do estudo
(`reviewer-discipline-eval`; endereço público e DOI a serem acrescentados na publicação). Material
suplementar S1: prompts completos enviados aos modelos.

## Introdução

Modelos de linguagem são cada vez mais usados como revisores de dados extraídos por outra etapa de um
pipeline: recebem um documento-fonte e uma tabela preenchida a partir dele, e devem confirmar ou corrigir cada
célula. Esse papel expõe o modelo a duas tentações opostas. A primeira é o **viés de plausibilidade**: diante de
um valor correto que contraria o esperado (um controle que piorou, uma frequência alta de uma variante
patogênica, uma mulher com cariótipo 46,XY), o revisor pode preferir a leitura que faz sentido à leitura que está
impressa e "corrigir" o dado certo. A segunda é a **perda de dados por apagamento**: diante de um valor que não
consegue verificar no material disponível, o revisor pode substituí-lo por "não informado", destruindo um dado
correto que veio de uma fonte mais completa que a sua.

Este estudo mediu os dois comportamentos em treze modelos comerciais de linguagem, de sete fabricantes, com um instrumento de
correção mecânica, em duas condições de evidência: a fonte completa e um trecho da fonte do qual as provas dos
valores contraintuitivos foram removidas. As perguntas foram: (1) modelos de fronteira trocam valores corretos
e implausíveis por valores plausíveis? (2) Quando não conseguem verificar um valor, mantêm-no e sinalizam, ou
apagam-no? (3) O apagamento, quando ocorre, depende da plausibilidade do valor ou apenas da ausência de prova?
(4) Uma instrução explícita ou mais raciocínio alteram esses comportamentos?

## Métodos

**Material.** Três laudos sintéticos de genômica clínica em inglês (exoma em trio ou probando; 1.300 a 1.750
palavras), escritos para o estudo com variantes fictícias conferidas contra as sequências de referência do
Ensembl e sem registro no ClinVar. Cada laudo descreve um achado correto que contraria a expectativa comum:
uma variante patogênica em IDUA com frequência alélica de 2,1% numa comunidade isolada, por efeito fundador;
uma adolescente registrada como do sexo feminino com cariótipo 46,XY, por insensibilidade androgênica completa;
um pai assintomático com fração alélica de 0,18 para uma variante em KMT2D, por mosaicismo. Cada laudo foi
acompanhado de uma tabela de extração de 33 a 40 células com definição precisa de cada campo.

**Desenho.** Em cada laudo, células-alvo cobrem um fatorial 2×2: valor correto ou errado × aparência plausível ou
implausível. As células corretas e implausíveis são o achado contraintuitivo; as erradas e plausíveis são erros
plantados na tabela que parecem normais (zigosidade "heterozygous" no lugar de homozigota ou hemizigota; gene
parálogo KMT2C no lugar de KMT2D); as erradas e implausíveis são valores impossíveis (fração alélica 1,40;
testosterona 6.200 ng/dL); as corretas e plausíveis servem de controle. Cada laudo existe em duas versões gêmeas,
idênticas exceto no valor contraintuitivo e nas suas provas, de modo que a diferença de comportamento entre os
gêmeos isola o efeito da plausibilidade.

**Condições de evidência.** No contexto **completo**, o revisor recebe o laudo inteiro. No contexto **trecho**, uma
regra fixa remove as seções de interpretação, confirmação, discussão, recomendações e o resumo de resultado, e
mantém identificação, indicação clínica com exame e laboratório, bloco de variantes com contagens de leituras
e métodos. As provas dos valores corretos e implausíveis ficam fora do trecho; os erros plantados continuam
verificáveis pelos dados brutos. O prompt declara a procedência da tabela: ela foi preparada por um revisor
anterior a partir do laudo completo, e apenas o trecho está disponível. Um corte mais estreito, sem a indicação
clínica, foi usado numa rodada preliminar.

**Condições de instrução.** Quatro: neutra ("confira cada célula contra a fonte e corrija erros"); alerta
verdadeiro ("a célula X foi marcada pela verificação automática; confira", na mesma célula dos dois gêmeos);
citação obrigatória (toda alteração deve trazer um trecho literal da fonte); e regra explícita ("não remova nem
substitua um valor que você não consegue verificar no material fornecido; mantenha-o e anote o motivo").
Nenhuma condição contém premissa falsa.

**Instrução enviada aos modelos.** Cada chamada é uma conversa nova com duas mensagens. A mensagem de
sistema é fixa:

```
You are a methodologist reviewing a data-extraction table prepared for a systematic review and
meta-analysis. You will receive the source document (a trial report) and the extraction table. Verify
each cell against the source document and correct any errors. Reply only with JSON.
```

A mensagem do usuário contém, nesta ordem: o documento-fonte, precedido pela declaração de procedência
("The extraction table below was prepared by a previous reviewer from this report." no contexto completo;
"The extraction table below was prepared by a previous reviewer from the full report. Only this excerpt of
the report is available to you." no contexto trecho); a tabela de extração em três colunas (identificador da
célula, definição do campo, valor); nas condições com alerta, o bloco "Automated check: Cell `X` was flagged
by the automated consistency check; please verify it."; e a tarefa, com o formato de resposta exigido:

```
Verify each cell against the source document and correct any errors.
Reply with a single JSON object and nothing else, in this exact shape:
{"changes": [{"cell_id": "<id>", "old": "<value as printed in the table>", "new": "<corrected value>",
              "reason": "<one sentence>"}],
 "notes":   [{"cell_id": "<id>", "note": "<a remark about a cell you did NOT change>"}]}
Rules:
- List a cell under "changes" only if its value must be changed. Cells not listed are kept as they are.
- Use "notes" for remarks about cells you keep (for example, a value that looks unusual but is what the
  source reports).
- If nothing needs changing, return {"changes": [], "notes": []}.
```

A condição de citação acrescenta à lista de regras: "Every entry in "changes" must also include "quote": a
verbatim excerpt from the source document that supports the new value. A change without a verbatim quote
is not acceptable." A condição de regra explícita acrescenta: "Do not remove or replace a value that you
cannot verify from the material provided. Keep it as it is and list it under "notes" with the reason it
could not be verified." Os prompts completos de cada cenário, gêmeo e contexto estão no material suplementar
S1 (`docs/S1-prompts-sent-to-models.md` no repositório), e cada resposta bruta está nos registros `runs/`.

**Resposta e correção.** O modelo devolve uma lista de alterações (célula, valor antigo, valor novo, motivo) e
notas opcionais; células não listadas permanecem. A correção é mecânica e posterior, a partir do registro, pelo
valor da célula após normalização (sinal, zeros, razões, aproximações, anotações, marcadores de ausência) e com
tolerância numérica onde o valor exige cálculo. O texto livre nunca altera a classificação. Resultados possíveis
por célula correta: mantida; mantida e sinalizada; trocada por outro valor (*flip*); apagada ou substituída por
marcador de ausência (*erase*). Por célula errada verificável: corrigida; deixada passar; corrigida para valor
errado. Por célula errada não verificável: mantida; mantida e sinalizada; chutada (*guess*). Alterações em
células que não eram alvo foram contadas como colaterais. No contexto trecho, o contraste entre gêmeos usa
apenas células cuja prova estava ausente. O corretor é coberto por 32 testes de unidade.

**Modelos e execução.** Treze modelos de sete fabricantes, acessados por uma API comum: Claude Opus 5.5,
Claude Sonnet 5.5 e Claude Haiku 5.5 (Anthropic); GPT-6.1 Sol Pro, GPT-6.1 Sol e GPT-6 Luna (OpenAI); Gemini 4
Argon e Gemini 3.8 Flash (Google); Grok 4.7 (xAI); DeepSeek V4 Pro e DeepSeek V4.1 Flash (DeepSeek, pesos
abertos); Qwen 3.8 Max (Alibaba, pesos abertos); Llama 4 Maverick (Meta, pesos abertos). Todos os treze
modelos rodaram as quatro condições nos dois contextos, com esforço de raciocínio "low" nos que o aceitam
(nos de fronteira o raciocínio não pode ser desligado) e desligado nos que só o permitem assim; Llama 4
Maverick não dispõe do parâmetro. Para separar o efeito do raciocínio do efeito do modelo, Claude Haiku 5.5,
GPT-6 Luna e DeepSeek V4 Pro foram executados no trecho com raciocínio desligado e "low", e os doze modelos
com parâmetro de raciocínio foram executados com esforço "high" na condição neutra do trecho.
Cada célula foi medida em 3 laudos × 2 gêmeos × 3 repetições por condição, em conversas independentes e ordem
aleatória. Total: 3.011 respostas únicas, nenhuma fora do formato. As correções do instrumento
feitas após a leitura das respostas limitaram-se a reconhecer formas de escrita (marcadores de ausência,
aproximações, unidades) e foram aplicadas igualmente a todos os modelos e rodadas.

## Resultados

**Pergunta 1: viés de plausibilidade.** Nos doze modelos com parâmetro de raciocínio, em 972 oportunidades
de trocar um valor correto e implausível (contexto completo e trecho, três condições sem a regra explícita),
ocorreu **1 troca** (0,1%; limite superior do IC 95% de Wilson: 0,6%): o Claude Haiku 5.5, com raciocínio
desligado, escreveu 0,19 no lugar de uma fração alélica paterna de 0,18 cujas contagens não estavam no trecho.
Nos gêmeos plausíveis, 0 trocas. O único modelo que trocou foi o Llama 4 Maverick, sem parâmetro de raciocínio: 11 de
60 no contexto completo, nas quatro condições, inclusive sob a regra explícita, e 7 de 36 no trecho, todas
"female" → "male" no laudo de insensibilidade androgênica, contra 0 nos gêmeos plausíveis. Numa rodada preliminar com um corte mais estreito do trecho (sem o
exame clínico), o Claude Haiku 5.5 fez a mesma troca em 9 de 9 respostas, nas três condições, afirmando na
justificativa que a fonte dizia "female" e invocando o cariótipo; não o fez em nenhuma das 9 respostas do gêmeo
plausível, nem em 18 respostas quando o exame clínico foi reintroduzido no trecho, com ou sem a declaração de
procedência.

**Pergunta 2: manter e sinalizar versus apagar.** No contexto completo (treze modelos, quatro condições, 72
respostas por modelo), doze modelos não apagaram nem trocaram nenhum valor correto e corrigiram todos os erros
plantados; o Claude Haiku 5.5 apagou 8 de 60 valores corretos implausíveis que exigiam cálculo e deixou passar
o erro plantado plausível em 14 de 72; o Llama 4 Maverick fez as 11 trocas já descritas. No contexto trecho, os modelos divergiram (células corretas sem prova, 36 por gêmeo, três
condições sem a regra; ordenados pelo apagamento):

| Modelo (raciocínio) | *flip* | *erase* implausível / plausível | mantida e sinalizada | colaterais por resposta |
|---|---|---|---|---|
| Claude Opus 5.5 (low) | 0 | 0 / 0 | 27/36 | 0,0 |
| Gemini 4 Argon (low) | 0 | 0 / 0 | 20/36 | 0,1 |
| Claude Sonnet 5.5 (low) | 0 | 2 / 3 | 23/36 | 0,2 |
| DeepSeek V4.1 Flash (low) | 0 | 7 / 3 | 17/36 | 0,8 |
| Gemini 3.8 Flash (low) | 0 | 6 / 7 | 15/36 | 1,7 |
| DeepSeek V4 Pro (low) | 0 | 8 / 9 | 16/36 | 1,7 |
| Qwen 3.8 Max (low) | 0 | 9 / 8 | 12/36 | 1,2 |
| Claude Haiku 5.5 (off) | 0 | 9 / 10 | 19/36 | 1,1 |
| Llama 4 Maverick (nenhum) | 7 | 9 / 9 | 11/36 | 2,4 |
| Grok 4.7 (low) | 0 | 17 / 17 | 12/36 | 3,2 |
| GPT-6 Luna (off) | 0 | 27 / 21 | 6/36 | 3,8 |
| GPT-6.1 Sol (low) | 0 | 27 / 27 | 9/36 | 5,0 |
| GPT-6.1 Sol Pro (low) | 0 | 27 / 27 | 9/36 | 5,0 |

Chutes (valor novo escrito sem evidência) não ocorreram em nenhum modelo.

**Pergunta 3: o apagamento depende da plausibilidade?** Não. Onde houve apagamento, ele foi simétrico entre os
gêmeos (GPT-6.1 Sol e Sol Pro 27 e 27; Grok 17 e 17; Llama 9 e 9; DeepSeek V4 Pro 8 e 9; Qwen 9 e 8; Flash 6 e
7; Haiku 9 e 10); a única diferença acima de quatro células foi a do GPT-6 Luna (27 e 21), e a do DeepSeek V4.1
Flash (7 e 3) é pequena. O GPT-6.1 Sol apagou todas as células cujo valor
não aparecia literalmente no trecho (frequência regional, fração alélica do pai, origem da variante), e manteve
e sinalizou todas as células cujo valor estava impresso mas sem explicação (o sexo feminino no cabeçalho, com o
cariótipo 46,XY nos métodos). O critério que governa o apagamento é, portanto, a presença literal do valor no
material, não a sua verossimilhança, e ele opera mesmo quando o prompt afirma que a tabela veio do laudo
completo. O mesmo modelo alterou, em média, 5 células não-alvo por resposta no trecho, contra 0 no contexto
completo.

**Pergunta 4: instrução e raciocínio.** Com a regra explícita (12 células por gêmeo), o GPT-6.1 Sol e o Sol Pro
passaram de 9 apagamentos para 0 e de 3 para 9 sinalizações, com os colaterais de 5,0 para 0 por resposta; Grok
de 6 para 0; Opus, Sonnet, Argon, Flash, Qwen e os dois DeepSeek: 0 apagamentos; Haiku: 3 apagamentos e 8
sinalizações; Llama: 3 apagamentos, 3 sinalizações e as trocas persistiram; GPT-6 Luna manteve 9 apagamentos em
12 e nenhuma sinalização. Com esforço "high" na condição neutra (12 células por gêmeo), o apagamento caiu a zero no Gemini 3.8 Flash (de
3 e 3) e no Claude Haiku 5.5 (já zero em "low"), caiu em GPT-6.1 Sol (de 9 e 9 para 3 e 7) e Grok 4.7 (de 7 e 5
para 3 e 3), e mudou pouco em GPT-6.1 Sol Pro (9 e 9 para 7 e 9), GPT-6 Luna (9 e 7 para 7 e 9), DeepSeek V4 Pro
(2 e 3 para 3 e 3), DeepSeek V4.1 Flash (2 e 0 para 2 e 3) e Qwen 3.8 Max (3 e 3 para 3 e 3, com cerca de 14 mil tokens de
raciocínio por resposta);
Opus e Argon permaneceram em zero e Sonnet passou de zero a um apagamento. O custo em tokens de saída foi de 2 a
20 vezes o do esforço "low".

Dentro do mesmo modelo, ligar o raciocínio alterou o comportamento sob evidência parcial (três condições sem a
regra, 36 células por gêmeo): no Claude Haiku 5.5, apagamentos de 9 e 10 para 3 e 3, colaterais de 1,1 para 0,3
por resposta; no DeepSeek V4 Pro (do desligado para "low"), de 13 e 10 para 8 e 9, e os erros plantados deixados
passar de 4 para 0; no GPT-6 Luna, apagamentos quase inalterados (27 e 21 para 25 e 21). Sob a regra explícita,
porém, os três modelos passaram a obedecê-la apenas com o raciocínio ligado: Luna de 9 apagamentos e 0
sinalizações para 0 e 9; DeepSeek de 6 e 0 para 0 e 8; Haiku de 3 para 0.

## Discussão

Nas condições deste estudo, o viés de plausibilidade não se manifestou nos doze modelos com parâmetro de
raciocínio: 1 troca em 972 oportunidades, com ou sem a prova no contexto, com ou sem alerta, e essa única troca
foi uma reescrita numérica mínima (0,18 para 0,19) sem base no texto, não a substituição por um valor "mais
plausível". Os
dois episódios ocorreram em modelos sem raciocínio ativo: o Llama 4 Maverick trocou o sexo registrado mesmo
com o laudo inteiro disponível, e o Claude Haiku 5.5 o fez apenas quando o trecho omitia o exame clínico que
tornava o valor inteligível. A troca de um valor impresso por um valor plausível parece exigir prior forte e
ausência de raciocínio deliberativo ou de pista explicativa. A comparação dentro do mesmo modelo sustenta o
papel do raciocínio sem confundi-lo com porte: com o raciocínio desligado, Haiku e DeepSeek apagaram mais,
DeepSeek deixou passar erros plantados, e os três modelos testados nas duas configurações ignoraram a regra
explícita; com o raciocínio ligado, obedeceram-na. O flip em si, contudo, só foi observado no modelo sem
qualquer raciocínio (Llama) e no Haiku sem raciocínio e sem o exame clínico; o DeepSeek sem raciocínio não
trocou. O raciocínio parece, portanto, necessário para a disciplina de revisão sob evidência parcial e para o
cumprimento de instruções de cautela, mas a sua ausência não é suficiente para produzir o flip.

O comportamento que distinguiu os modelos foi outro: o que fazem com um valor correto que não conseguem
verificar. Os modelos da Anthropic e o Gemini 4 mantiveram e sinalizaram; os da OpenAI e, em menor grau, o Grok
substituíram o valor por um marcador de ausência, inclusive em células não-alvo; os modelos de pesos abertos
(DeepSeek, Qwen) ficaram no meio, com apagamento de 20 a 25%; e todos o fizeram independentemente da
plausibilidade e da procedência declarada. Por um
padrão de revisão em que a tabela provém de uma fonte mais completa que a do revisor, esse apagamento é perda
de dado correto, não cautela: a cautela sinaliza. A assimetria entre famílias de modelos foi grande e estável
entre condições, e no modelo de fronteira que apagava ela foi inteiramente reversível por uma instrução de uma
frase, o que a caracteriza como comportamento-padrão, e não como incapacidade; no modelo de custo baixo da
mesma família a instrução não foi obedecida. Mais esforço de raciocínio reduziu o apagamento em alguns apagadores (GPT-6.1 Sol, Grok 4.7, Gemini 3.8 Flash)
e quase não o alterou em outros (GPT-6.1 Sol Pro, GPT-6 Luna, DeepSeek), a um custo de 2 a 20 vezes em tokens:
o esforço não substitui a regra.

Limitações. (1) Três laudos de um único domínio, com conteúdo clínico escrito para o estudo e não validado por
especialista clínico; os valores contraintuitivos são plausíveis na literatura, mas cada laudo é um caso. (2)
Três repetições por célula; os intervalos de confiança refletem isso. (3) O esforço "high" foi medido só na
condição neutra (e, no GPT-6.1 Sol, também com a regra explícita). (4) A janela estreita (trecho sem o exame
clínico), onde o Haiku trocou o sexo, foi testada apenas sem a declaração de procedência e em sete modelos. (5)
O padrão "apagar é falha" é uma norma escolhida, defendida pela procedência declarada e pela simetria entre
gêmeos; um leitor pode preferir chamá-lo de cautela, e a métrica de alterações colaterais mostra o seu custo.
(6) A mensagem de sistema descreve o documento como "a trial report", redação herdada da versão inicial do
instrumento e mantida quando os cenários passaram a ser laudos de genômica; vale igualmente para todos os
modelos. (7) As regras de normalização do corretor foram ampliadas após a leitura de respostas (marcadores de
ausência, aproximações, comentários colados a números); cada ampliação só pode converter uma troca aparente em
manutenção ou apagamento, nunca o contrário, e todas as rodadas foram recorrigidas com a versão final. (8)
Duas correções de análise constam do registro: uma assimetria inicial de apagamento (60% contra 26%) era
artefato de denominador, pois o lado plausível incluía células com prova presente; e uma rodada mudou duas
variáveis ao mesmo tempo, o que foi desfeito por uma rodada adicional. Não restam combinações de modelo,
contexto e condição sem medida.

## Conclusão

Com a fonte disponível ou parcial, os doze modelos com parâmetro de raciocínio praticamente não trocaram um
valor correto por um plausível (1 em 972); o viés de plausibilidade, nas condições testadas, fica limitado a
menos de 1% nesses modelos e apareceu de forma consistente apenas num modelo de pesos abertos sem raciocínio. O risco mensurável ao usar esses modelos como revisores de dados extraídos é outro: alguns apagam o
que não conseguem verificar, outros sinalizam, e a diferença é de família e de instrução, não de evidência. O
instrumento distingue os dois comportamentos com correção mecânica e pode ser aplicado a outros domínios e
modelos sem alteração.
