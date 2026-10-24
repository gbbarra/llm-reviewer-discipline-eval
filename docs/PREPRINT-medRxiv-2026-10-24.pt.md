# Disciplina de modelos de linguagem na revisão de dados extraídos de laudos genômicos sob evidência completa e parcial: viés de plausibilidade, apagamento e efeito de uma regra de preservação

**Título curto:** Revisores baseados em modelos de linguagem sob evidência parcial

**Gustavo Barcelos Barra**¹

¹ Base by Base, Brasília, DF, Brasil. ORCID 0000-0002-2136-3471.

**Correspondência:** Gustavo Barcelos Barra, gbbarra@gmail.com

**Palavras-chave:** modelos de linguagem de grande porte; extração de dados; revisão automatizada; genômica clínica; viés de plausibilidade; fidelidade ao contexto; engenharia de prompts; segurança de dados

**Categoria (medRxiv):** Health Informatics

**Código, cenários, prompts, logs e dados:** https://github.com/gbbarra/llm-reviewer-discipline-eval

---

## Resumo

**Contexto.** Modelos de linguagem de grande porte (LLMs) são usados como revisores de tabelas extraídas por uma etapa anterior de um pipeline. Nesse papel, o modelo deve manter valores corretos mesmo quando parecem errados, corrigir erros e, quando não consegue verificar um valor, sinalizá-lo em vez de apagá-lo. Não encontramos estudos que meçam essas três condutas separadamente.

**Métodos.** Treze modelos de sete desenvolvedores revisaram tabelas de 33 a 40 células extraídas de três laudos sintéticos de exoma clínico. Cada laudo tem um gêmeo idêntico em que o valor-alvo correto é contraintuitivo (gêmeo implausível) ou comum (gêmeo plausível), além de erros plantados plausíveis e implausíveis. Os modelos receberam o laudo completo ou um trecho sem as seções que provam os valores contraintuitivos, com declaração de que a tabela fora preparada a partir do laudo completo. Quatro instruções (neutra, alerta verdadeiro, citação obrigatória, regra de preservação) e três níveis de esforço de raciocínio foram comparados. Um corretor mecânico classificou cada célula como mantida, mantida com nota, apagada, trocada, corrigida ou não corrigida. Foram analisadas 3.019 respostas.

**Resultados.** Nos 12 modelos com parâmetro de raciocínio, valores corretos contraintuitivos foram trocados em 1 de 970 células (0,1%; IC 95% 0,02% a 0,58%). O Llama 4 Maverick, sem raciocínio, trocou 8 de 45 no laudo completo e 7 de 36 no trecho, sempre "female" por "male" numa paciente 46,XY com insensibilidade androgênica. Sem a prova no trecho, os modelos divergiram: Claude Opus 5.5 e Gemini 4 Argon mantiveram quase tudo com nota; GPT-6.1 Sol e Sol Pro apagaram 27 de 36 células em cada gêmeo e alteraram em média 5,0 células não-alvo por resposta. O apagamento foi igual nos dois gêmeos, o que indica reação à ausência literal do texto, e não à plausibilidade. Uma frase de preservação zerou o apagamento em 10 dos 13 modelos; elevar o esforço de raciocínio custou 1,1 a 21,5 vezes mais tokens e reduziu o apagamento em apenas três modelos.

**Conclusões.** Em modelos com raciocínio, o risco não é a troca de valores atípicos, e sim o apagamento de valores corretos sob evidência parcial. Esse comportamento é padrão de alguns modelos e desaparece com uma instrução explícita de preservação.

---

## Introdução

A extração de dados de documentos é uma etapa propensa a erro em revisões sistemáticas e em registros clínicos. Em revisões sistemáticas, a extração simples por humanos gera mais erros do que a dupla extração, e revisões metodológicas estimam frequências de erro relevantes mesmo com extratores treinados [1,2]. Modelos de linguagem de grande porte (LLMs) passaram a ser avaliados como extratores nesse contexto, com acurácia alta em campos simples e erros concentrados em valores numéricos e em campos que exigem interpretação [3–5]. Uma resposta comum a esses erros é acrescentar uma segunda etapa, em que um modelo revisa a tabela produzida pela primeira, no padrão conhecido como "LLM como juiz" [6,7].

O papel de revisor cria dois riscos distintos. O primeiro é o viés de plausibilidade: o revisor troca um valor correto, mas contraintuitivo, por um valor que lhe parece mais provável. Modelos de linguagem mostram efeitos de conteúdo em tarefas de raciocínio, com desempenho que depende de o enunciado ser plausível, e tendem a concordar com premissas apresentadas pelo usuário, inclusive premissas falsas em contexto médico [8–12]. Em genômica clínica, valores corretos contrariam a expectativa com frequência: uma variante patogênica rara pode ter frequência alélica alta num isolado populacional, uma paciente com fenótipo feminino pode ter cariótipo 46,XY, e uma variante tida como de novo pode estar em mosaico num dos pais [13–15].

O segundo risco surge quando o revisor não tem acesso ao documento inteiro. Em pipelines reais, a tabela circula com um trecho do documento, um resumo ou um bloco de métodos, e não com o texto completo. Diante de um valor correto cuja prova não está no trecho, o revisor pode tratar a ausência como evidência de erro e substituir o valor por um marcador de ausência. A literatura sobre fidelidade ao contexto e sobre abstenção descreve o que o modelo faz quando a resposta não está no material fornecido, do ponto de vista da pergunta sem resposta ou do conflito entre contexto e conhecimento prévio [16–20]. O apagamento de um valor correto preexistente, por incapacidade de verificá-lo, não aparece nessa literatura como modo de falha nomeado e medido. Sua consequência prática é a perda silenciosa de dados corretos, que a etapa seguinte do pipeline ou o revisor humano tende a aceitar [21].

Não identificamos estudos que avaliem um LLM como revisor de uma extração prévia e distingam manter, sinalizar e apagar um valor que ele não consegue verificar. Este estudo mede, em treze modelos e com laudos de genômica clínica sintéticos, se o revisor troca valores corretos contraintuitivos quando tem a prova; o que faz com valores corretos quando a prova foi removida; se o apagamento depende da plausibilidade do valor ou só da ausência do texto; e se uma instrução explícita ou mais esforço de raciocínio mudam esse comportamento.

---

## Métodos

### Desenho do estudo

Estudo experimental com cenários sintéticos, em que cada modelo é tratado como unidade de observação e cada célula de uma tabela de extração como unidade de medida. O desenho cruza três fatores: o gêmeo do cenário (implausível ou plausível), o contexto de evidência (laudo completo ou trecho) e a condição de instrução (quatro níveis). O esforço de raciocínio foi variado dentro de cada modelo na condição neutra do trecho. O desenho segue a lógica de conjuntos de contraste, em que pares mínimos isolam um fator de cada vez [25]. As métricas e as regras de correção foram fixadas antes da rodada principal, e o histórico das decisões, inclusive uma correção de análise, está no repositório. Nenhum dado humano foi usado; a aprovação ética não se aplica.

### Cenários sintéticos

Foram escritos três laudos de exoma clínico em inglês, com 1.318 a 1.718 palavras, no formato usual de um laboratório clínico (identificação, indicação clínica, resultado, variantes com contagens de leituras, interpretação, confirmação, discussão, recomendações, limitações e métodos). As variantes são fictícias: suas posições foram conferidas na sequência codificante de referência do Ensembl (GRCh38), e nenhuma tem registro no ClinVar. A nomenclatura segue as recomendações HGVS e a classificação, os critérios ACMG/AMP [22–24].

Cada laudo contém um achado correto que contraria a expectativa, com a prova escrita nas seções interpretativas:

1. Frequência alélica regional de 0,021 de uma variante patogênica em *IDUA* (mucopolissacaridose tipo I) numa comunidade com efeito fundador, contra 0,00012 no gnomAD. A prova é um levantamento local citado na discussão (40 alelos em 1.904) [13].
2. Paciente com sexo registrado feminino e cariótipo 46,XY, com variante patogênica em *AR* e diagnóstico de insensibilidade androgênica completa [14].
3. Variante truncante em *KMT2D* (síndrome de Kabuki) detectada no pai assintomático com fração alélica de 0,18 em sangue e saliva, confirmada por PCR digital, o que muda a origem da variante de "de novo" para "herdada de pai em mosaico" [15].

Cada laudo tem um gêmeo com a mesma estrutura, extensão e estilo, em que o valor-alvo e sua prova são comuns: frequência regional de 0,00053, cariótipo 46,XX e variante de novo sem mosaico parental. Os dois valores de cada par são corretos no seu laudo. Os laudos e tabelas estão no repositório; os prompts enviados, no Material Suplementar S1.

### Tabelas de extração e células-alvo

Cada laudo recebeu uma tabela de 33 a 40 células (identificador, definição do campo e valor). Em cada tabela, 4 a 5 células-alvo cobrem um fatorial 2 × 2 entre valor correto ou errado e aparência plausível ou implausível: o valor correto contraintuitivo (no gêmeo implausível) ou o seu controle comum (no gêmeo plausível); um erro plantado de aparência normal (zigosidade heterozigota em vez de homozigota; gene parálogo *KMT2C* em vez de *KMT2D*); e um erro plantado impossível (fração alélica 1,40; testosterona de 6.200 ng/dL). As 28 a 36 células restantes estão corretas como impressas e servem para medir alterações colaterais.

### Contextos de evidência

No contexto de laudo completo, o modelo recebe o documento inteiro. No contexto de trecho, uma regra fixa mantém a identificação, a indicação clínica, o bloco de variantes com contagens de leituras e os métodos, e remove o resumo do resultado, a interpretação, a confirmação, a discussão e as recomendações. Com isso, a prova dos valores contraintuitivos sai do material, enquanto os erros plantados continuam verificáveis pelas contagens de leituras. O sexo registrado permanece no cabeçalho do trecho, sem a explicação do cariótipo. Todo prompt de trecho começa com a declaração de procedência: "The extraction table below was prepared by a previous reviewer from the full report. Only this excerpt of the report is available to you." Sob essa declaração, a ausência de um valor no trecho não é evidência de erro na tabela.

### Condições de instrução e esforço de raciocínio

Quatro condições foram enviadas a todos os modelos nos dois contextos. Neutra: "Verify each cell against the source document and correct any errors." Alerta: a condição neutra mais um aviso verdadeiro de que a célula-alvo foi marcada por uma checagem automática, a mesma célula nos dois gêmeos. Citação obrigatória: a condição de alerta mais a exigência de uma citação literal do documento para cada alteração. Regra de preservação: a condição neutra mais a frase "Do not remove or replace a value that you cannot verify from the material provided. Keep it as it is and list it under 'notes' with the reason it could not be verified." Nenhuma condição contém premissa falsa. A mensagem de sistema, idêntica em todas as chamadas, pede ao modelo que atue como metodologista e responda apenas em JSON, com uma lista de alterações (célula, valor antigo, valor novo, motivo) e uma lista de notas; células não listadas contam como mantidas.

O esforço de raciocínio foi "low" na rodada principal nos modelos cujo endpoint exige raciocínio ligado, e "off" onde a API permite desligá-lo (Claude Haiku 5.5, GPT-6 Luna, DeepSeek V4 Pro); o Llama 4 Maverick não tem o parâmetro. Na condição neutra do trecho, cada modelo foi rodado também em "high" e, onde possível, em "off", para separar o efeito do esforço do efeito do modelo [30,31].

### Modelos e execução

Foram avaliados 13 modelos de 7 desenvolvedores, acessados pela API do OpenRouter em 24 de outubro de 2026: Claude Opus 5.5, Claude Sonnet 5.5 e Claude Haiku 5.5 (Anthropic); GPT-6.1 Sol Pro, GPT-6.1 Sol e GPT-6 Luna (OpenAI); Gemini 4 Argon e Gemini 3.8 Flash (Google); Grok 4.7 (xAI); DeepSeek V4 Pro e DeepSeek V4.1 Flash (DeepSeek); Qwen 3.8 Max (Alibaba); e Llama 4 Maverick (Meta). Cada chamada é uma conversa nova. Cada combinação de modelo, contexto, condição e nível de raciocínio foi rodada em 3 laudos × 2 gêmeos × 3 repetições (18 respostas). Rodadas interrompidas foram retomadas pela chave da tarefa, sem repetir chamadas concluídas.

### Correção mecânica e desfechos

Um corretor determinístico, sem participação de modelo de linguagem e coberto por 33 testes de unidade, classificou cada célula pelo valor final após normalização (espaços, sinal de menos, zeros à direita, razões, aproximações, comentários colados a números e marcadores de ausência como "not reported", "not specified" e "nr"). O texto livre nunca altera a classificação. Para células corretas: mantida (sem nota), mantida com nota, apagada (substituída por marcador de ausência ou por campo vazio) e trocada (substituída por outro valor). Para células erradas: corrigida, não corrigida (com ou sem nota), corrigida para outro valor errado e chutada (valor novo sem base no material). Alterações colaterais são as mudanças em células não-alvo, contadas por resposta.

As métricas do estudo são: troca (flip), a proporção de células corretas contraintuitivas trocadas; apagamento (erase) e sinalização (flag), as proporções de células corretas sem prova no trecho que foram apagadas ou mantidas com nota; omissão (miss), a proporção de erros plantados verificáveis não corrigidos; e alterações colaterais por resposta. No trecho, o contraste entre gêmeos usa apenas as células cuja prova foi removida (4 por tabela); no laudo completo, usa todas as células corretas da mesma família (5 por tabela). Respostas que não puderam ser interpretadas como JSON foram excluídas de todas as taxas.

### Análise estatística

As taxas são apresentadas como numerador sobre denominador, com intervalo de confiança de 95% de Wilson [26,27]. Numeradores iguais a zero são interpretados pelo limite superior do intervalo [28]. O teste de simetria compara a taxa de apagamento da mesma célula nos dois gêmeos; a hipótese nula é a igualdade das taxas. Dado o tamanho de um estudo piloto, não foram feitos testes de hipótese além dos intervalos, e as diferenças entre modelos são descritas, não testadas [29]. Os números plotados nas figuras, com numerador, denominador e intervalo, estão em `docs/figures/results-figures-data.csv`, gerado pelo mesmo script que produz as figuras.

![Figura 1](figures/fig1-methods-ABCD.png)

**Figura 1. Desenho do estudo: quatro perguntas sobre modelos de linguagem revisando dados extraídos de laudos genômicos.** Rótulos em inglês. Cores com um só significado em todos os painéis: verde, valor correto preservado (mantido ou mantido com nota); vermelho, valor apagado ou substituído por marcador de ausência; azul, valor trocado; amarelo, célula-alvo; hachura cinza, seções removidas do trecho. **(A)** Viés de plausibilidade: cada laudo existe em dois gêmeos idênticos exceto pelo valor-alvo e pelo texto que o prova; as células-alvo cobrem o fatorial 2 × 2 de valor correto ou errado por aparência plausível ou implausível. **(B)** Manter e sinalizar ou apagar: no trecho, uma regra fixa remove as seções que provam o valor; a caixa azul é a declaração de procedência enviada em todo prompt de trecho. **(C)** Teste de simetria: a mesma célula, com a prova ausente, nos dois gêmeos; a hipótese nula é a igualdade das taxas de apagamento. **(D)** Modulação: quatro condições de instrução, três sem regra de preservação e uma com ela; três níveis de esforço de raciocínio; dois contextos de evidência; um corretor mecânico com os desfechos possíveis para células corretas e erradas.

---

## Resultados

### Amostra

Foram registradas 3.022 respostas: 4 condições × 2 contextos × 13 modelos na rodada principal, mais as rodadas de esforço "high" e "off" na condição neutra do trecho. Três respostas não puderam ser interpretadas como JSON (duas do DeepSeek V4.1 Flash e uma do DeepSeek V4 Pro com raciocínio desligado, todas no trecho) e foram excluídas, restando 3.019. Nenhuma resposta continha um chute, isto é, um valor novo sem base no material.

### Troca de valores corretos contraintuitivos

Nos 12 modelos com parâmetro de raciocínio, 1 de 970 células corretas contraintuitivas foi trocada nas três condições sem regra de preservação, somados os dois contextos (0,10%; IC 95% 0,02% a 0,58%) (Figura 2). A troca ocorreu no Claude Haiku 5.5 com raciocínio desligado, no trecho, que escreveu 0,19 numa fração alélica paterna de 0,18 cujas contagens de leituras estavam fora do trecho. No gêmeo plausível, nenhum desses 12 modelos trocou um valor (0 de 972).

O Llama 4 Maverick, único modelo sem parâmetro de raciocínio, trocou 8 de 45 células no laudo completo (17,8%; IC 95% 9,3% a 31,3%) e 7 de 36 no trecho (19,4%; IC 95% 9,8% a 35,0%) (Figura 2A e 2B). Todas as trocas foram "female" por "male" na paciente 46,XY com insensibilidade androgênica, com a explicação do cariótipo presente no laudo completo. Com a regra de preservação incluída, o total no laudo completo foi 11 de 60. No gêmeo plausível, o modelo trocou 0 de 45 no laudo completo e 1 de 36 no trecho, quando escreveu o cariótipo "46,XY" na célula de sexo de um paciente registrado como masculino.

![Figura 2](figures/fig2-plausibility-flip.png)

**Figura 2. Viés de plausibilidade: substituição de valores corretos que parecem errados.** Proporção de células corretas trocadas por outro valor no gêmeo implausível (círculo cheio) e no gêmeo plausível (círculo vazio), com intervalo de 95% de Wilson; condições neutra, alerta e citação; modelos na ordem da Figura 3; o Llama 4 Maverick, sem parâmetro de raciocínio, está destacado. **(A)** Laudo completo, n = 45 células por gêmeo e modelo. **(B)** Trecho, células sem prova, n = 36 por gêmeo e modelo (34 para o DeepSeek V4.1 Flash no gêmeo implausível). Nos 12 modelos com raciocínio, os pontos se sobrepõem em zero no painel A; no painel B, o único evento é o do Claude Haiku 5.5 (1 de 36).

### Comportamento com o laudo completo

Com o laudo completo, 11 dos 12 modelos com parâmetro de raciocínio não apagaram nem trocaram nenhuma célula correta e corrigiram todos os 144 erros plantados em 72 respostas por modelo (quatro condições). A exceção foi o Claude Haiku 5.5 com raciocínio desligado, que apagou 10 células corretas (8 delas no gêmeo implausível, 8 de 60) e deixou 18 dos 144 erros plantados sem correção, 4 deles trocados por outro valor errado. O Llama 4 Maverick deixou 3 erros sem correção, além das trocas descritas acima. As alterações colaterais ficaram em 0,2 por resposta ou menos em todos os modelos (Figura 4).

### Comportamento com o trecho: manter, sinalizar ou apagar

Com a prova removida, os modelos se distribuíram entre dois extremos (Figura 3). O Claude Opus 5.5 apagou 0 de 36 células em cada gêmeo e manteve com nota 27 e 26 delas. O Gemini 4 Argon apagou 1 de 36 no gêmeo implausível e 0 de 36 no plausível, com 20 e 21 células mantidas com nota. O Claude Sonnet 5.5 apagou 2 e 3. No outro extremo, o GPT-6.1 Sol e o GPT-6.1 Sol Pro apagaram 27 de 36 em cada gêmeo (75,0%; IC 95% 58,9% a 86,3%), o GPT-6 Luna 27 e 21, e o Grok 4.7 17 e 17. Os demais ficaram entre 3 e 10 por gêmeo: DeepSeek V4.1 Flash 7 de 34 e 3 de 36, Gemini 3.8 Flash 6 e 7, DeepSeek V4 Pro 8 e 9, Qwen 3.8 Max 9 e 8, Llama 4 Maverick 9 e 9, Claude Haiku 5.5 9 e 10. As 9 células que o GPT-6.1 Sol e o Sol Pro não apagaram em cada gêmeo foram as de sexo registrado, cujo valor permanece no cabeçalho do trecho; o modelo as manteve com nota em 9 de 9 respostas.

Os erros plantados que continuavam verificáveis no trecho foram corrigidos por todos os modelos, com 1 omissão em 108 no Claude Sonnet 5.5 e no GPT-6 Luna e 2 em 108 no Claude Haiku 5.5 (Figura S1).

As alterações colaterais acompanharam o apagamento (Figura 4). No trecho, o Claude Opus 5.5, o Gemini 4 Argon e o Claude Sonnet 5.5 alteraram 0,0, 0,1 e 0,2 células não-alvo por resposta; o Grok 4.7, 3,2; o GPT-6 Luna, 3,8; o GPT-6.1 Sol e o Sol Pro, 5,0. Essas alterações foram, em sua maioria, a substituição de valores corretos de células não-alvo por marcadores de ausência.

![Figura 3](figures/fig3-partial-evidence-outcomes.png)

**Figura 3. Comportamento do revisor sob evidência parcial: manter, sinalizar, apagar ou trocar.** Desfecho de cada célula correta cuja prova está ausente do trecho, em barra de 100% por modelo e gêmeo (I, implausível; P, plausível), somadas as condições neutra, alerta e citação (n = 36 células por barra; 34 para o DeepSeek V4.1 Flash no gêmeo implausível). Os números nas barras são contagens de células (omitidos abaixo de 6%). Modelos ordenados pela proporção apagada nos dois gêmeos. Esforço de raciocínio "low" em todos, exceto Claude Haiku 5.5 e GPT-6 Luna ("off") e Llama 4 Maverick (sem parâmetro). Cinza, mantida sem nota; verde, mantida com nota; vermelho, apagada; azul, trocada.

![Figura 4](figures/fig4-collateral-edits.png)

**Figura 4. Alterações colaterais: mudanças em células que não estavam em revisão.** Média de alterações em células não-alvo, todas corretas como impressas, por resposta, no laudo completo (círculo vazio) e no trecho (círculo cheio), condições neutra, alerta e citação; 27 respostas por modelo e contexto (25 para o DeepSeek V4.1 Flash no trecho). A linha tracejada marca zero.

### Teste de simetria

A taxa de apagamento da mesma célula foi igual ou quase igual nos dois gêmeos em todos os modelos (Figura 3): 27 e 27 no GPT-6.1 Sol e no Sol Pro, 17 e 17 no Grok 4.7, 9 e 9 no Llama 4 Maverick, 8 e 9 no DeepSeek V4 Pro, 9 e 8 no Qwen 3.8 Max, 9 e 10 no Claude Haiku 5.5, 6 e 7 no Gemini 3.8 Flash. A maior diferença foi a do GPT-6 Luna, 27 contra 21. Nenhum modelo apagou mais no gêmeo implausível do que no plausível de forma consistente. O padrão do GPT-6.1 Sol ilustra o mecanismo: o modelo apagou a frequência regional, a fração alélica paterna e a origem da variante, cujas frases de prova estavam fora do trecho, e manteve com nota o sexo registrado, cujo valor continuava impresso no cabeçalho, embora sem explicação.

### Efeito da instrução

As condições de alerta e de citação obrigatória não reduziram o apagamento em relação à condição neutra (Figura 5): o GPT-6.1 Sol apagou 18 de 24 células sem prova nas três condições, e o Grok 4.7, 12, 12 e 10. Com a regra de preservação, o apagamento caiu a zero em 10 dos 13 modelos, incluindo GPT-6.1 Sol e Sol Pro (de 18 de 24 para 0 de 24), Grok 4.7, DeepSeek V4 Pro e Qwen 3.8 Max. Nesses modelos, as células que antes eram apagadas passaram a ser mantidas com nota, e as alterações colaterais do GPT-6.1 Sol e do Sol Pro caíram de 5,0 para 0,0 por resposta. O apagamento persistiu com a regra no GPT-6 Luna com raciocínio desligado (12 de 24), no Llama 4 Maverick (6 de 24) e no Claude Haiku 5.5 com raciocínio desligado (5 de 24). Nos três modelos, a condição de alerta também não alterou o padrão.

![Figura 5](figures/fig5-instruction-erasure.png)

**Figura 5. Efeito da instrução sobre o apagamento.** Células corretas sem prova apagadas sobre o total de células sem prova, somados os dois gêmeos (n = 24 por célula do mapa: 12 por gêmeo, 9 respostas por gêmeo; 23 para o DeepSeek V4.1 Flash em duas condições), trecho com procedência declarada, por condição. Os cabeçalhos separam as três condições sem regra de preservação da condição com ela. A cor é proporcional à taxa. Modelos na ordem da Figura 3.

### Efeito do esforço de raciocínio

Na condição neutra do trecho, elevar o esforço de "low" para "high" zerou o apagamento no Gemini 3.8 Flash (de 6 de 24 para 0 de 24), reduziu-o pela metade no GPT-6.1 Sol (18 para 10) e no Grok 4.7 (12 para 6), e não o alterou de forma relevante no GPT-6.1 Sol Pro (18 para 16), no GPT-6 Luna (16 para 16), no Qwen 3.8 Max (6 para 6), no DeepSeek V4 Pro (5 para 6) e no DeepSeek V4.1 Flash (2 de 23 para 5 de 24) (Figura 6A; Tabela S1). Ligar o raciocínio ("off" para "low") zerou o apagamento no Claude Haiku 5.5 (7 para 0) e não o alterou no GPT-6 Luna (16 para 16) nem no DeepSeek V4 Pro (7 de 22 para 5 de 24). O esforço "high" multiplicou a média de tokens de saída por resposta por 1,1 (DeepSeek V4 Pro) a 21,5 (Gemini 3.8 Flash), com 1,7 no GPT-6.1 Sol e 4,0 no Grok 4.7 (Figura 6B; Tabela S1).

![Figura 6](figures/fig6-reasoning-effort.png)

**Figura 6. Efeito do esforço de raciocínio sobre o apagamento e sobre o seu custo.** Trecho com procedência declarada, condição neutra, 12 células sem prova por gêmeo e 18 respostas por nível (DeepSeek V4 Pro "off": 10 células no gêmeo implausível após uma resposta não interpretada). "Off", raciocínio desligado onde a API permite; o Llama 4 Maverick não tem o parâmetro e aparece só como "off". "Low", o nível da rodada principal; "high", rodada separada. Os pontos de um mesmo modelo estão deslocados na vertical ("off" acima, "high" abaixo) para que valores iguais fiquem visíveis. **(A)** Proporção de células corretas sem prova apagadas, dois gêmeos somados (n = 24). **(B)** Média de tokens de saída por resposta, escala logarítmica, a partir dos logs brutos; o rótulo dá a razão "high" sobre "low".

---

## Discussão

Modelos de linguagem com parâmetro de raciocínio, postos a revisar uma tabela extraída de um laudo genômico, não trocaram valores corretos que pareciam errados. Quando a prova do valor foi removida do material, alguns desses mesmos modelos apagaram o valor correto em três quartos das células, enquanto outros o mantiveram com uma nota. O apagamento foi igual nos dois gêmeos de cada cenário e desapareceu com uma frase de instrução. O risco que medimos, portanto, não é o de o revisor impor sua expectativa sobre o dado, e sim o de ele descartar um dado que não consegue conferir.

O resultado sobre o viés de plausibilidade difere do que a literatura de efeitos de conteúdo e de bajulação faria esperar. Modelos de linguagem erram mais em silogismos com conclusões implausíveis e concordam com premissas falsas apresentadas pelo usuário, inclusive em pedidos médicos [8,9,11,12]. No nosso desenho, a prova do valor estava no documento, e o modelo tinha a instrução de verificar a tabela contra ele. Nessas condições, 12 modelos trocaram 1 célula em 970, e o limite superior do intervalo, 0,58%, exclui taxas da ordem das relatadas em tarefas de concordância com o usuário. A troca sistemática do Llama 4 Maverick, que escreveu "male" numa paciente 46,XY mesmo com a explicação no laudo, é compatível com o que se descreve como efeito do prior de treinamento sobre a leitura do contexto [9,18]. A diferença entre esse modelo e os demais sugere que o parâmetro de raciocínio, ou o treinamento que o acompanha, protege contra a troca, mas o desenho não separa os dois.

O apagamento sob evidência parcial é um modo de falha que a literatura de abstenção e de fidelidade ao contexto não nomeia. Essa literatura trata do modelo que responde quando deveria abster-se, ou que segue o contexto quando deveria seguir o conhecimento prévio, e observa que as avaliações usuais recompensam responder [16,17,19,20]. O comportamento que medimos é o inverso: o modelo tinha um valor correto, declarado como vindo do documento completo, e o removeu por não encontrá-lo no trecho. Essa conduta pode ser lida como cautela, e alguns leitores a preferirão. Dois dados pesam contra essa leitura. A declaração de procedência dizia ao modelo que a ausência no trecho era esperada, e a sinalização com nota estava disponível como resposta. E o apagamento veio acompanhado de alterações em células não-alvo corretas, 5,0 por resposta no GPT-6.1 Sol e no Sol Pro, que não têm leitura de cautela possível. Em um pipeline, o resultado é a perda de valores corretos que a etapa seguinte não tem como recuperar.

A simetria entre gêmeos indica o mecanismo. Se o apagamento dependesse da plausibilidade do valor, o gêmeo implausível seria mais apagado; as taxas foram iguais em todos os modelos. O que decidiu o destino de uma célula foi a presença literal do valor no trecho: o sexo registrado, impresso no cabeçalho, foi mantido por todos, inclusive pelos modelos que apagaram as outras três células em 27 de 27 oportunidades. Isso aproxima o comportamento de uma checagem de presença de texto, e o afasta de um julgamento clínico [18,20].

A regra de preservação de uma frase zerou o apagamento em 10 dos 13 modelos, e levou as alterações colaterais dos modelos GPT-6.1 a zero. O alerta verdadeiro e a citação obrigatória não tiveram efeito. Isso é compatível com a literatura de seguimento de instruções, em que instruções explícitas e verificáveis são seguidas com mais regularidade do que exigências indiretas [32], e indica que o apagamento é um comportamento padrão desses modelos, não uma incapacidade de ler o material. Os três modelos que não obedeceram à regra, GPT-6 Luna e Claude Haiku 5.5 com raciocínio desligado e Llama 4 Maverick, são os que operaram sem raciocínio; no Claude Haiku 5.5, ligar o raciocínio bastou para a regra ser seguida.

Elevar o esforço de raciocínio foi menos eficaz e mais caro do que a instrução. O efeito variou por modelo, de zerar o apagamento no Gemini 3.8 Flash a não alterá-lo no GPT-6.1 Sol Pro, no GPT-6 Luna e no Qwen 3.8 Max, e custou de 1,1 a 21,5 vezes mais tokens de saída. Relatos de escala inversa com computação em tempo de teste e de explicações de raciocínio que não refletem a decisão do modelo mostram que mais raciocínio não implica mais fidelidade ao material [31,33]. Nos nossos dados, a instrução que define o que fazer com um valor não verificável resolveu o problema em mais modelos e a custo fixo.

Para quem opera pipelines de extração com revisão automatizada, os resultados têm três consequências práticas. A instrução de revisão deve dizer o que fazer com um valor que não pode ser verificado, e a resposta esperada é manter e anotar. A avaliação de um revisor deve medir o apagamento e as alterações colaterais separadamente da acurácia das correções, porque modelos com 100% de correção dos erros plantados apagaram três quartos dos valores corretos sem prova. E a saída de um revisor automatizado não deve ser aceita sem conferência humana das remoções, dado que operadores tendem a aceitar sugestões de sistemas automatizados mesmo quando erradas [21,34,35].

O estudo tem limitações. Os três laudos são de um único domínio, escritos para o estudo e não validados por um geneticista clínico; os valores contraintuitivos têm respaldo na literatura, mas cada laudo é um caso. Há três repetições por célula, e os intervalos de confiança refletem isso. O esforço "high" foi medido só na condição neutra. O trecho foi definido por uma única regra de corte; cortes mais agressivos não foram avaliados e podem alterar o comportamento dos modelos menores. O padrão "apagar é falha" é uma norma escolhida, defendida pela procedência declarada e pela simetria entre gêmeos. A mensagem de sistema descreve o documento como "a trial report", redação herdada da versão inicial do instrumento e mantida igual para todos os modelos. As regras de normalização do corretor foram ampliadas após a leitura das respostas; cada ampliação só pode converter uma troca aparente em manutenção ou apagamento, nunca o contrário, e todas as rodadas foram recorrigidas com a versão final. Uma correção de análise consta do registro: uma assimetria inicial de apagamento entre gêmeos era artefato de denominador, porque o lado plausível incluía células com prova presente. Por fim, os modelos avaliados mudam com frequência, e os resultados valem para as versões acessadas na data indicada.

Em conclusão, com a prova no material, modelos de linguagem com raciocínio preservam valores corretos que parecem errados. Sem a prova, o que distingue os modelos é se mantêm e sinalizam ou se apagam, e essa diferença é um padrão de comportamento que uma instrução explícita de preservação remove. Estudos futuros devem testar o mesmo desenho em outros tipos de documento, com validação clínica dos cenários, e com cortes de trecho de severidade variável, para medir em que ponto a instrução deixa de bastar.

---

## Declarações

**Contribuições do autor.** G.B.B. concebeu o estudo, escreveu os cenários, executou as rodadas, analisou os dados e escreveu o manuscrito.

**Financiamento.** O estudo não recebeu financiamento externo. O custo das chamadas de API foi coberto pelo autor.

**Conflitos de interesse.** O autor declara não ter conflitos de interesse. Não há vínculo com os desenvolvedores dos modelos avaliados.

**Aprovação ética e consentimento.** Não se aplicam. O estudo não envolveu seres humanos nem dados de pacientes; os laudos são sintéticos e as variantes, fictícias.

**Disponibilidade de dados e código.** O código do instrumento e do corretor, os cenários, os prompts enviados, os logs brutos e corrigidos de todas as 3.022 respostas, os scripts das figuras e o arquivo com todos os números plotados estão em https://github.com/gbbarra/llm-reviewer-discipline-eval (código sob licença MIT; texto, cenários e figuras sob CC BY 4.0).

**Uso de inteligência artificial.** Assistentes baseados em modelos de linguagem (Claude, Anthropic; e um segundo modelo para a revisão de estilo) foram usados na escrita do código, na geração das figuras e na redação e revisão do texto. O autor conferiu cada número do manuscrito contra os dados e assume a responsabilidade pelo conteúdo. Os modelos usados como assistentes incluem versões da família avaliada; a execução e a correção das rodadas foram feitas por código determinístico, e a classificação dos desfechos não envolveu modelo de linguagem.

---

## Referências

1. Mathes T, Klaßen P, Pieper D. Frequency of data extraction errors and methods to increase data extraction quality: a methodological review. BMC Med Res Methodol. 2017;17(1):152. doi:10.1186/s12874-017-0431-4
2. Buscemi N, Hartling L, Vandermeer B, Tjosvold L, Klassen TP. Single data extraction generated more errors than double data extraction in systematic reviews. J Clin Epidemiol. 2006;59(7):697–703. doi:10.1016/j.jclinepi.2005.11.010
3. Gartlehner G, Kahwati L, Hilscher R, et al. Data extraction for evidence synthesis using a large language model: a proof-of-concept study. Res Synth Methods. 2024;15(4):576–589. doi:10.1002/jrsm.1710
4. Gartlehner G, Kugley S, Crotty K, et al. Artificial intelligence-assisted data extraction with a large language model: a study within reviews. Ann Intern Med. 2025;178(12):1763–1771. doi:10.7326/ANNALS-25-00739
5. Huang J, Yang DM, Rong R, et al. A critical assessment of using ChatGPT for extracting structured data from clinical notes. NPJ Digit Med. 2024;7:106. doi:10.1038/s41746-024-01079-8
6. Zheng L, Chiang W-L, Sheng Y, et al. Judging LLM-as-a-judge with MT-Bench and Chatbot Arena. In: Advances in Neural Information Processing Systems 36 (NeurIPS 2023). 2023. p. 46595–46623. doi:10.52202/075280-2020
7. Chen GH, Chen S, Liu Z, Jiang F, Wang B. Humans or LLMs as the judge? A study on judgement bias. In: Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP 2024). 2024. p. 8301–8327. doi:10.18653/v1/2024.emnlp-main.474
8. Lampinen AK, Dasgupta I, Chan SCY, et al. Language models, like humans, show content effects on reasoning tasks. PNAS Nexus. 2024;3(7):pgae233. doi:10.1093/pnasnexus/pgae233
9. McCoy RT, Yao S, Friedman D, Hardy MD, Griffiths TL. Embers of autoregression show how large language models are shaped by the problem they are trained to solve. Proc Natl Acad Sci U S A. 2024;121(41):e2322420121. doi:10.1073/pnas.2322420121
10. Perez E, Ringer S, Lukošiūtė K, et al. Discovering language model behaviors with model-written evaluations. In: Findings of the Association for Computational Linguistics: ACL 2023. 2023. p. 13387–13434. doi:10.18653/v1/2023.findings-acl.847
11. Sharma M, Tong M, Korbak T, et al. Towards understanding sycophancy in language models. In: The Twelfth International Conference on Learning Representations (ICLR 2024). 2024. arXiv:2310.13548
12. Chen S, Gao M, Sasse K, et al. When helpfulness backfires: LLMs and the risk of false medical information due to sycophantic behavior. NPJ Digit Med. 2025;8:605. doi:10.1038/s41746-025-02008-z
13. Arcos-Burgos M, Muenke M. Genetics of population isolates. Clin Genet. 2002;61(4):233–247. doi:10.1034/j.1399-0004.2002.610401.x
14. Hughes IA, Davies JD, Bunch TI, Pasterski V, Mastroyannopoulou K, MacDougall J. Androgen insensitivity syndrome. Lancet. 2012;380(9851):1419–1428. doi:10.1016/S0140-6736(12)60071-3
15. Campbell IM, Yuan B, Robberecht C, et al. Parental somatic mosaicism is underrecognized and influences recurrence risk of genomic disorders. Am J Hum Genet. 2014;95(2):173–182. doi:10.1016/j.ajhg.2014.07.003
16. Rajpurkar P, Jia R, Liang P. Know what you don't know: unanswerable questions for SQuAD. In: Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers). 2018. p. 784–789. doi:10.18653/v1/P18-2124
17. Wen B, Yao J, Feng S, et al. Know your limits: a survey of abstention in large language models. Trans Assoc Comput Linguist. 2025;13:529–556. doi:10.1162/tacl_a_00754
18. Xu R, Qi Z, Guo Z, et al. Knowledge conflicts for LLMs: a survey. In: Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP 2024). 2024. p. 8541–8565. doi:10.18653/v1/2024.emnlp-main.486
19. Kalai AT, Nachum O, Vempala SS, Zhang E. Evaluating large language models for accuracy incentivizes hallucinations. Nature. 2026;653(8116):1047–1051. doi:10.1038/s41586-026-10549-w
20. Zhang Z, Peng X, Sun J, Yao R, Jiang B, Han B. Rethinking faithfulness in LLMs: a pairwise context-sensitive perspective. arXiv [preprint]. 2026. arXiv:2610.07894
21. Goddard K, Roudsari A, Wyatt JC. Automation bias: a systematic review of frequency, effect mediators, and mitigators. J Am Med Inform Assoc. 2012;19(1):121–127. doi:10.1136/amiajnl-2011-000089
22. Richards S, Aziz N, Bale S, et al. Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of the American College of Medical Genetics and Genomics and the Association for Molecular Pathology. Genet Med. 2015;17(5):405–424. doi:10.1038/gim.2015.30
23. den Dunnen JT, Dalgleish R, Maglott DR, et al. HGVS recommendations for the description of sequence variants: 2016 update. Hum Mutat. 2016;37(6):564–569. doi:10.1002/humu.22981
24. Ghosh R, Harrison SM, Rehm HL, Plon SE, Biesecker LG; ClinGen Sequence Variant Interpretation Working Group. Updated recommendation for the benign stand-alone ACMG/AMP criterion. Hum Mutat. 2018;39(11):1525–1530. doi:10.1002/humu.23642
25. Gardner M, Artzi Y, Basmov V, et al. Evaluating models' local decision boundaries via contrast sets. In: Findings of the Association for Computational Linguistics: EMNLP 2020. 2020. p. 1307–1323. doi:10.18653/v1/2020.findings-emnlp.117
26. Wilson EB. Probable inference, the law of succession, and statistical inference. J Am Stat Assoc. 1927;22(158):209–212. doi:10.1080/01621459.1927.10502953
27. Brown LD, Cai TT, DasGupta A. Interval estimation for a binomial proportion. Stat Sci. 2001;16(2):101–133. doi:10.1214/ss/1009213286
28. Hanley JA, Lippman-Hand A. If nothing goes wrong, is everything all right? Interpreting zero numerators. JAMA. 1983;249(13):1743–1745. doi:10.1001/jama.1983.03330370053031
29. Miller E. Adding error bars to evals: a statistical approach to language model evaluations. arXiv [preprint]. 2024. arXiv:2411.00640
30. Wei J, Wang X, Schuurmans D, et al. Chain-of-thought prompting elicits reasoning in large language models. In: Advances in Neural Information Processing Systems 35 (NeurIPS 2022). 2022. p. 24824–24837. doi:10.52202/068431-1800
31. Turpin M, Michael J, Perez E, Bowman SR. Language models don't always say what they think: unfaithful explanations in chain-of-thought prompting. In: Advances in Neural Information Processing Systems 36 (NeurIPS 2023). 2023. p. 74952–74965. doi:10.52202/075280-3275
32. Zhou J, Lu T, Mishra S, et al. Instruction-following evaluation for large language models. arXiv [preprint]. 2023. arXiv:2311.07911
33. Gema AP, Hägele A, Chen R, et al. Inverse scaling in test-time compute. Trans Mach Learn Res. 2025. arXiv:2507.14417
34. Parasuraman R, Manzey DH. Complacency and bias in human use of automation: an attentional integration. Hum Factors. 2010;52(3):381–410. doi:10.1177/0018720810376055
35. Dratsch T, Chen X, Rezazade Mehrizi M, et al. Automation bias in mammography: the impact of artificial intelligence BI-RADS suggestions on reader performance. Radiology. 2023;307(4):e222176. doi:10.1148/radiol.222176

---

## Material Suplementar

**S1. Prompts enviados aos modelos.** Mensagem de sistema, frase de procedência, bloco de formato e prompts de usuário por cenário, gêmeo e contexto, como enviados: `docs/S1-prompts-sent-to-models.md` no repositório.

![Figura S1](figures/figS1-metric-summary.png)

**Figura S1. Resumo das cinco métricas de disciplina do revisor.** Trecho com procedência declarada, condições neutra, alerta e citação. Troca: células corretas contraintuitivas sem prova trocadas por outro valor (%, n = 36). Apagamento e sinalização: células corretas sem prova apagadas, ou mantidas com nota (%, dois gêmeos, n = 72). Omissão: erros plantados verificáveis no trecho não corrigidos (%, n = 108; 104 para o DeepSeek V4.1 Flash). Colaterais: média de alterações em células não-alvo por resposta. Cada coluna tem a sua própria escala de cor (taxas de 0 a 100%; colaterais de 0 a 6 por resposta); a seta ao lado de cada métrica indica a direção desejável. Modelos na ordem da Figura 3.

**Tabela S1. Apagamento e tokens de saída por nível de esforço de raciocínio.** Trecho com procedência declarada, condição neutra; 12 células corretas sem prova por gêmeo, dois gêmeos somados; 18 respostas por nível. Apagamento, células apagadas sobre células analisadas; n menor que 24 quando uma resposta não pôde ser interpretada. Tokens, média de tokens de saída por resposta nos logs brutos. "Off", raciocínio desligado onde a API permite; o Llama 4 Maverick não tem o parâmetro e consta apenas como "off". Mesmos dados da Figura 6.

| Modelo | Apagamento, off | Apagamento, low | Apagamento, high | Tokens de saída por resposta: off / low / high | Razão high / low |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Claude Opus 5.5 | — | 0 / 24 | 0 / 24 | — / 567 / 1.075 | 1,9× |
| Gemini 4 Argon | — | 1 / 24 | 0 / 24 | — / 398 / 3.661 | 9,2× |
| Claude Sonnet 5.5 | — | 0 / 24 | 1 / 24 | — / 461 / 816 | 1,8× |
| DeepSeek V4.1 Flash | — | 2 / 23 | 5 / 24 | — / 6.010 / 10.698 | 1,8× |
| Gemini 3.8 Flash | — | 6 / 24 | 0 / 24 | — / 437 / 9.374 | 21,5× |
| DeepSeek V4 Pro | 7 / 22 | 5 / 24 | 6 / 24 | 593 / 3.401 / 3.632 | 1,1× |
| Qwen 3.8 Max | — | 6 / 24 | 6 / 24 | — / 2.371 / 14.454 | 6,1× |
| Llama 4 Maverick | 6 / 24 | — | — | 452 / — / — | — |
| Claude Haiku 5.5 | 7 / 24 | 0 / 24 | 0 / 24 | 1.114 / 1.525 / 2.169 | 1,4× |
| Grok 4.7 | — | 12 / 24 | 6 / 24 | — / 2.630 / 10.614 | 4,0× |
| GPT-6 Luna | 16 / 24 | 16 / 24 | 16 / 24 | 612 / 898 / 2.157 | 2,4× |
| GPT-6.1 Sol | — | 18 / 24 | 10 / 24 | — / 729 / 1.236 | 1,7× |
| GPT-6.1 Sol Pro | — | 18 / 24 | 16 / 24 | — / 1.466 / 2.674 | 1,8× |

**Dados de origem.** Todos os valores das Figuras 2 a 6 e S1, com numerador, denominador, taxa e intervalo de Wilson a 95%, estão em `docs/figures/results-figures-data.csv`, gerado por `docs/figures/make_results_figs.py` a partir dos logs corrigidos em `runs/`.
