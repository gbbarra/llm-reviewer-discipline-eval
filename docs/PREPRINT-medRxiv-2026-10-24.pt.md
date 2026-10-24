# Avaliação da Disciplina de Modelos de Linguagem na Revisão de Dados Genômicos sob Evidência Parcial: Imunidade ao Viés de Plausibilidade, Risco de Apagamento Destrutivo e Eficácia de Salvaguardas

**Título em Inglês para Submissão:**  
*Reviewer Discipline of Large Language Models under Partial Evidence in Clinical Genomics: Plausibility Robustness, Destructive Erasure, and the Power of Preservation Directives*

**Autor:** Gustavo Barcelos Barra  
**Afiliação:** Base by Base, Brasília, DF, Brasil  
**Correspondência:** Gustavo Barcelos Barra (contato via repositório institucional)  
**Categoria pretendida no medRxiv:** Health Informatics  
**Repositório de Dados e Código:** [`https://github.com/gbbarra/llm-reviewer-discipline-eval`](https://github.com/gbbarra/llm-reviewer-discipline-eval)

---

## Declarações Obrigatórias

**Aprovação ética:** Dispensada. O estudo utilizou exclusivamente dados sintéticos gerados computacionalmente com sequências de referência do Ensembl, sem inclusão de seres humanos, prontuários ou tecidos biológicos reais.  
**Conflitos de interesse:** O autor declara ausência de vínculos financeiros, comerciais ou de consultoria com desenvolvedores de modelos de linguagem, provedores de computação em nuvem ou empresas farmacêuticas.  
**Financiamento:** Pesquisa independente conduzida com recursos próprios da iniciativa Base by Base.  
**Disponibilidade de dados e reprodutibilidade:** Todos os registros brutos de inferência (3.022 arquivos JSONL), o código do avaliador mecânico coberto por 33 testes unitários, os cenários completos e os prompts (Material Suplementar S1) estão publicamente disponíveis no GitHub sob licenças de código aberto (MIT / CC BY 4.0).

---

## Resumo (*Abstract*)

Pipelines automatizados de informática médica e síntese de evidências empregam modelos de linguagem de grande porte (LLMs) como revisores de dados extraídos de laudos diagnósticos complexos. Espera-se que esses sistemas preservem dados verdadeiros mesmo quando atípicos (*imunidade ao viés de plausibilidade*), corrijam erros factuais e sinalizem incertezas em vez de expurgar registros válidos quando operam sob evidência documental incompleta (*disciplina de revisão*). Avaliamos treze LLMs comerciais e de pesos abertos (sete desenvolvedores) encarregados de auditar tabelas de 33 a 40 campos clínicos extraídas de laudos sintéticos de sequenciamento de exoma (1.318 a 1.718 palavras). O desenho experimental utilizou pares de cenários gêmeos (*twins*) com matriz fatorial 2×2 (achados contraintuitivos legítimos vs. controles ordinários; erros plantados disfarçados vs. grotescos) sob dois regimes de visibilidade: laudo completo e excerto funcional (onde as justificativas dos dados atípicos foram removidas, mas com aviso formal de proveniência de que a tabela provinha do laudo integral). Foram avaliadas quatro condições de instrução e três níveis de raciocínio (*test-time reasoning*), totalizando 3.019 respostas auditadas por classificação mecânica determinística. Nos doze modelos dotados de raciocínio deliberativo, o viés de plausibilidade foi praticamente nulo: registrou-se apenas 1 troca indevida em 970 oportunidades analisáveis sob condições sem salvaguarda explícita (0,10%; IC 95% de Wilson: 0,02%–0,58%). Em contrapartida, o modelo sem raciocínio (Llama 4 Maverick) exibiu viés sistemático (11 trocas em 60 oportunidades no laudo integral; 7 em 36 no excerto, convertendo invariavelmente o sexo de feminino para masculino em uma paciente com insensibilidade androgênica e cariótipo 46,XY). Sob evidência parcial, emergiu uma cisão arquitetural marcante: enquanto Claude Opus 5.5 e Gemini 4 Argon retiveram e anotaram 100% dos dados corretos sem prova, a família GPT-6 apagou 75% dos campos (27/36 por gêmeo), substituindo-os por marcadores de ausência e induzindo uma média de 5,0 edições colaterais em campos adjacentes válidos. O apagamento exibiu simetria estrita entre os gêmeos atípico e comum (ex.: 27/36 em ambos os braços no GPT-6.1 Sol), demonstrando reação mecânica à ausência imediata de texto, e não ceticismo biológico. Uma regra explícita de preservação de uma frase (*keep rule*: *"não altere o que não puder verificar; preserve e anote"*) suprimiu integralmente os apagamentos e as edições colaterais nos principais modelos de fronteira, ao passo que elevar o esforço de raciocínio demandou até 21,5× mais tokens sem conter o expurgo na maioria das arquiteturas. Conclui-se que o risco crítico de LLMs na auditoria médica não é o viés de plausibilidade, mas o apagamento destrutivo de dados verdadeiros sob evidência fragmentada, uma vulnerabilidade de alinhamento padrão plenamente corrigível por diretivas estritas de preservação.

---

## Introdução

A extração automatizada de informações fenotípicas e genotípicas a partir de relatórios médicos não estruturados é essencial para alimentar registros de doenças raras, plataformas de suporte à decisão clínica e revisões sistemáticas em larga escala [1-3]. Para mitigar erros de extração primária, arquiteturas computacionais em múltiplos estágios têm adotado um segundo modelo de linguagem atuando como auditor de qualidade (*LLM-as-a-judge*) [4, 5]. Nesse arranjo, o revisor recebe o documento clínico de origem juntamente com a tabela estruturada preenchida na etapa precedente, com a incumbência de confirmar dados exatos e retificar eventuais incongruências [6].

Essa função de auditoria expõe o sistema a dois dilemas cognitivos e metodológicos antagônicos. O primeiro é o viés de plausibilidade (*plausibility bias*), manifestação computacional do *belief bias* em que o modelo subverte a evidência textual impressa para acomodar seus priors estatísticos de treinamento [7-10]. Em genética médica, achados biologicamente verídicos frequentemente colidem com noções epidemiológicas intuitivas: uma mutação recessiva letal pode atingir frequências populacionais elevadas em comunidades isoladas por efeito fundador [11, 23], ou uma paciente fenotipicamente feminina pode ser portadora de cariótipo 46,XY decorrente de insensibilidade completa aos androgênios [12, 25]. Caso o revisor computacional priorize a verossimilhança estatística em detrimento da leitura fidedigna do laudo, dados atípicos de alto valor diagnóstico correm o risco de sofrer adulteração indevida (*flip*) [13, 14].

O segundo dilema, de impacto imediato na engenharia de dados em saúde, reside na perda de dados por apagamento destrutivo (*destructive erasure*) [15, 16]. Em pipelines de produção baseados em recuperação de informação e segmentação documental (RAG), o agente revisor raramente acessa o prontuário em sua totalidade; frequentemente, ele analisa fragmentos textuais restritos a blocos laboratoriais ou métodos [17, 18]. Diante de um dado clínico legítimo cuja comprovação causal não conste no trecho disponível, revisores desalinhados tendem a assumir premissas fechadas de mundo (*closed-world assumption*), presumindo falsamente que a ausência de menção no excerto comprova que o dado foi inventado pela etapa anterior. Consequentemente, substituem o valor legítimo por termos de nulidade (*"não relatado"*, campo vazio), quebrando a integridade de bancos de dados clínicos e violando o princípio prudencial de auditoria (*"sinalize antes de alterar; cite antes de excluir"*) [19, 20].

Embora avanços recentes tenham introduzido modelos de raciocínio deliberativo em tempo de inferência (*test-time reasoning*) [21, 22], a literatura carece de investigações empíricas sobre a estabilidade desses sistemas diante de assimetrias documentais e tensões de plausibilidade clínica. Este trabalho quantifica experimentalmente o comportamento de treze modelos de fronteira na auditoria de dados genômicos, determinando: (1) se os modelos trocam dados verdadeiros contraintuitivos por leituras canônicas; (2) se sob evidência parcial preservam ou apagam registros não verificáveis; (3) se o apagamento decorre de plausibilidade clínica ou de rigidez textual literal; e (4) se diretivas explícitas de preservação ou aumentos de computação deliberativa contêm o comportamento destrutivo.

---

## Métodos

### Cenários Clínicos Sintéticos e Desenho Experimental Fatorial
Para eliminar riscos à privacidade de dados de saúde e assegurar controle experimental absoluto, foram desenvolvidos três laudos de exoma sintéticos (1.318 a 1.718 palavras em inglês) baseados em trio familiar ou probando. Todas as variantes fictícias foram mapeadas e conferidas contra o genoma de referência do Ensembl (GRCh38) e o repositório ClinVar, garantindo fidedignidade molecular e ausência de correspondência com pacientes reais.

Cada cenário retrata uma situação onde o dado empírico verdadeiro contraria a expectativa clínica convencional:
1. *Frequência Alélica Regional (IDUA):* Variante deletéria causadora de Mucopolissacaridose tipo I apresentando frequência alélica regional de 0,021 (2,1%) em comunidade com efeito fundador e consanguinidade parental, contrastando com a raridade global no gnomAD (0,00012) [23, 24].
2. *Discordância Fenótipo-Cariótipo (AR):* Propositora fenotipicamente feminina registrada civilmente no sexo feminino, portadora de cariótipo 46,XY e variante patogênica no gene do receptor de androgênios, diagnosticada com Síndrome de Insensibilidade Completa aos Androgênios (CAIS) [25, 26].
3. *Mosaicismo Pós-Zigótico Paterno (KMT2D):* Variante truncante causadora de Síndrome de Kabuki tipo 1 detectada no pai assintomático com fração alélica de 0,18 em sangue e saliva (confirmada por *ddPCR*), refutando a hipótese preliminar de mutação estritamente *de novo* e alterando o risco de recorrência reprodutiva [27, 28].

A verificação do viés de plausibilidade foi operacionalizada mediante um desenho em cenários gêmeos (*twins*). Cada cenário possui uma versão gêmea de estrutura, extensão e estilo idênticos, diferindo unicamente na natureza ordinária do alvo correspondente e de sua prova textual (frequência alélica comum de 0,00053, cariótipo 46,XX e mutação *de novo* clássica sem carreadores parentais) (Figura 1A).

As tabelas de extração associadas continham entre 33 e 40 células, abrangendo uma matriz fatorial 2×2: alvos corretos e implausíveis (o foco do estudo); alvos corretos e plausíveis (controles pareados); erros factuais plantados com aparência normal (ex.: classificação de zigosidade homozigota como heterozigota; atribuição ao gene parálogo *KMT2C* em vez de *KMT2D*); e erros factuais com valores impossíveis (fração alélica de 1,40; testosterona sérica de 6.200 ng/dL em adolescente feminina). As 28 a 36 células restantes compunham campos de suporte fidedignos ao laudo, cuja alteração indevida serviu para mensurar a taxa de edições colaterais (*collateral edits*).

### Regimes de Evidência e Declaração de Proveniência
Os modelos foram avaliados em dois contextos de visibilidade documental (Figura 1B):
* *Laudo Completo (Controle):* O documento integral é fornecido, contendo dados brutos, metodologia, interpretação diagnóstica, confirmação complementar e discussão. Serve como controle positivo para atestar se o modelo interpreta adequadamente a informação quando a prova está presente.
* *Excerto Funcional:* O texto é submetido a um filtro algorítmico que preserva identificação, dados de cobertura e contagens brutas de leituras, mas suprime deliberadamente as seções interpretativas e conclusivas onde residem as provas dos alvos contraintuitivos. Erros plantados permanecem auditáveis pelos dados brutos.

Para reproduzir a assimetria informacional típica de pipelines reais e neutralizar a premissa de mundo fechado, o excerto continha uma declaração formal de proveniência:
> *"The extraction table below was prepared by a previous reviewer from the full report. Only this excerpt of the report is available to you."*

Sob essa premissa metodológica, a omissão circunstancial do dado no excerto não constitui prova de erro na tabela, exigindo a retenção prudente do registro.

### Condições de Instrução e Esforço de Raciocínio
Foram cruzadas quatro condições de intervenção textual no prompt (Figura 1D): (1) *Neutra*, com instrução padrão de revisão (*"Verify each cell against the source document and correct any errors"*); (2) *Alerta*, com sinalização automática verdadeira sobre a célula-alvo (*"Cell X was flagged by the automated consistency check; please verify it"*), aplicada de modo idêntico em ambos os gêmeos; (3) *Citação Obrigatória*, exigindo transcrição literal (*verbatim quote*) para toda alteração submetida; e (4) *Regra de Preservação (Keep Rule)*, instruindo explicitamente a retenção acompanhada de nota:
> *"Do not remove or replace a value that you cannot verify from the material provided. Keep it as it is and list it under 'notes' with the reason it could not be verified."*

O esforço de raciocínio deliberativo (*reasoning effort*) foi padronizado em nível baixo (*low*) para modelos que exigem raciocínio ativo e desligado (*off*) nos convencionais. Variações controladas em três níveis (*off, low, high*) foram conduzidas na condição neutra do excerto para isolar o papel da computação em tempo de teste.

### Avaliação Mecânica Offline e Amostragem
As interações ocorreram em sessões sem estado via API, com exigência estrita de saída em formato JSON contendo listas estruturadas de modificações (`"changes"`) e notas (`"notes"`). A classificação dos desfechos foi realizada por um corretor determinístico offline coberto por 33 testes unitários automatizados, sem intervenção de modelos avaliadores. O algoritmo normalizou caracteres, operadores, frações numéricas e expressões de ausência antes da graduação.

Os desfechos em células corretas foram catalogados como: *Mantida* (preservada sem notas); *Mantida e Sinalizada* (preservada e comentada em notas — conduta prudencial ideal); *Troca (Flip)* (substituição indevida por outro valor substancial); e *Apagamento (Erase)* (substituição por marcador de nulidade ou string vazia). Em células erradas, os desfechos incluíram *Corrigida* e *Omissão (Miss)*. Modificações em campos corretos não correlacionados foram computadas como *Edições Colaterais* por resposta.

Foram testados treze modelos de ponta de sete fabricantes: Claude Opus 5.5, Claude Sonnet 5.5 e Claude Haiku 5.5 (Anthropic); GPT-6.1 Sol Pro, GPT-6.1 Sol e GPT-6 Luna (OpenAI); Gemini 4 Argon e Gemini 3.8 Flash (Google); Grok 4.7 (xAI); DeepSeek V4 Pro e DeepSeek V4.1 Flash (DeepSeek); Qwen 3.8 Max (Alibaba); e Llama 4 Maverick (Meta). Cada célula foi avaliada em 3 laudos × 2 gêmeos × 3 repetições independentes. De 3.022 execuções brutas, 3 respostas (0,1%, restritas à família DeepSeek) apresentaram vício formal de JSON e foram excluídas, totalizando 3.019 respostas integralmente apuradas. Intervalos de confiança de 95% foram calculados pelo método de Wilson [29].

---

![Figura 1](figures/fig1-methods-ABCD.png)

**Figura 1. Desenho experimental e arquitetura metodológica do estudo.**  
Paleta Okabe-Ito uniforme: verde = dado verídico preservado (mantido ou anotado em notas); vermelho = apagamento destrutivo ou substituição por marcador de nulidade; azul = troca indevida por plausibilidade (*flip*); amarelo = célula-alvo; hachura cinza = seções interpretativas suprimidas do excerto parcial. **(A) Viés de Plausibilidade:** Cada laudo sintético possui uma versão gêmea pareada idêntica em extensão e sintaxe, diferindo no valor-alvo e na prova textual correspondente. A matriz fatorial 2×2 cruza a fidedignidade real do valor com sua verossimilhança aparente. **(B) Preservação versus Apagamento sob Evidência Parcial:** No excerto, as seções de interpretação molecular são removidas. A declaração de proveniência adverte o modelo de que a tabela foi elaborada a partir do laudo completo, tornando a ausência no excerto insuficiente para justificar exclusão. **(C) Teste de Simetria para o Apagamento:** A hipótese nula testa a equivalência matemática das taxas de apagamento entre o gêmeo atípico e o gêmeo comum ($\text{H}_0: \text{Erase}_I = \text{Erase}_P$). **(D) Modulação Experimental:** Quatro condições de instrução e três níveis de esforço de raciocínio avaliados sob correção mecânica determinística coberta por 33 testes de unidade.

---

## Resultados

### Imunidade Quase Universal ao Viés de Plausibilidade em Modelos com Raciocínio
Nos doze modelos equipados com arquiteturas de raciocínio deliberativo, em um total de 970 oportunidades de adulteração sob as três condições sem regra de preservação (contextos completo e excerto combinados), ocorreu apenas 1 evento de troca (*flip*) (0,10%; IC 95% de Wilson: 0,02%–0,58%) (Figura 2). Esse evento único decorreu do Claude Haiku 5.5 executado com raciocínio desativado, que alterou a fração alélica paterna de 0,18 para 0,19 no excerto, configurando ajuste numérico espúrio sem amparo textual. Nos cenários gêmeos plausíveis de controle, registraram-se zero trocas (0/970).

Em contraste com os demais sistemas, o Llama 4 Maverick — único modelo avaliado desprovido de camada de raciocínio interno — apresentou viés de plausibilidade sistemático e clinicamente grave:
* No laudo completo com proveniência declarada, o modelo adulterou a célula-alvo em 8 de 45 oportunidades nas três condições sem regra (Figura 2A), atingindo 11 de 60 trocas (18,3%) quando incluída a condição com regra de preservação. Em todas as instâncias, o modelo substituiu a entrada *"female"* por *"male"* na paciente portadora de insensibilidade androgênica completa e cariótipo 46,XY, ignorando a declaração explícita de sexo do cabeçalho. No braço controle correspondente (46,XX), cometeu zero trocas (0/60).
* No excerto parcial, o modelo repetiu o padrão patológico com 7 trocas em 36 oportunidades (19,4%) no gêmeo atípico (Figura 2B), contra 1 ocorrência no braço plausível (onde copiou o texto "46,XY" para a célula de sexo masculino).

---

![Figura 2](figures/fig2-plausibility-flip.png)

**Figura 2. Viés de plausibilidade: taxa de substituição de dados corretos contraintuitivos por alternativas convencionais (*flips*).**  
Proporção de células corretas substituídas por outro valor com intervalos de confiança de 95% de Wilson, comparando o gêmeo implausível (círculo azul preenchido) contra o gêmeo plausível de controle (círculo vazado). Condições neutra, alerta e citação agrupadas (regra de preservação excluída). Modelos ordenados pela taxa de apagamento da Figura 3. **(A) Laudo Completo:** n = 45 células por gêmeo e modelo. Todos os doze modelos providos de raciocínio apresentaram 0% de trocas (0/45). O Llama 4 Maverick (destacado em amarelo como único modelo sem raciocínio deliberativo) cometeu 8 trocas em 45 oportunidades (11/60 nas quatro condições), alterando invariavelmente "female" para "male" na paciente com cariótipo 46,XY e insensibilidade androgênica. **(B) Excerto Parcial:** n = 36 células por gêmeo e modelo (34 para DeepSeek V4.1 Flash no gêmeo atípico). O Llama 4 Maverick cometeu 7 trocas em 36 (19,4%) contra 1 em 36 no gêmeo plausível. O Claude Haiku 5.5 com raciocínio desligado registrou 1 troca em 36 (0,18 para 0,19). Entre todos os modelos de raciocínio, registrou-se apenas 1 troca em 970 células analisadas.

---

### Dicotomia sob Evidência Parcial: Retenção Prudente versus Apagamento Destrutivo
No contexto de controle com laudo completo (72 respostas por modelo), onze dos doze modelos de raciocínio demonstraram acurácia perfeita: zero apagamentos de dados válidos, zero trocas e 100% de correção dos erros plantados. A exceção foi o Claude Haiku 5.5 com raciocínio desativado, que apagou 10 células corretas dependentes de cálculo numérico e omitiu 18 dos 144 erros plantados (sendo 4 corrigidos para valores incorretos).

Sob o regime de excerto parcial, no qual a fundamentação dos alvos atípicos foi omitida, revelou-se uma cisão de linhagem categórica entre as famílias de modelos (Tabela 1 e Figura 3):

**Tabela 1. Desfecho das células corretas sem prova documental no excerto**  
*(Amostra consolidada das condições Neutra, Alerta e Citação; n = 36 células por gêmeo por modelo; ordenados da maior disciplina para o maior apagamento).*

| Modelo | Configuração de Raciocínio | Trocas (*Flip*) | Apagamento (*Erase*): Implausível / Plausível | Mantidas e Sinalizadas (*Flag*) [Gêmeo Implausível] | Edições Colaterais por Resposta (Média) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Claude Opus 5.5** | Low | 0 | **0 / 0** (0,0%) | 27 / 36 | 0,0 |
| **Gemini 4 Argon** | Low | 0 | **0 / 0** (0,0%) | 20 / 36 | 0,1 |
| **Claude Sonnet 5.5** | Low | 0 | **2 / 3** (6,9%) | 23 / 36 | 0,2 |
| **DeepSeek V4.1 Flash** | Low | 0 | **7 / 3** (14,3%) | 17 / 36 | 0,8 |
| **Gemini 3.8 Flash** | Low | 0 | **6 / 7** (18,1%) | 15 / 36 | 1,7 |
| **DeepSeek V4 Pro** | Low | 0 | **8 / 9** (23,6%) | 16 / 36 | 1,7 |
| **Qwen 3.8 Max** | Low | 0 | **9 / 8** (23,6%) | 12 / 36 | 1,2 |
| **Claude Haiku 5.5** | Off | 0 | **9 / 10** (26,4%) | 19 / 36 | 1,1 |
| **Llama 4 Maverick** | N/A | 7 | **9 / 9** (25,0%) | 11 / 36 | 2,4 |
| **Grok 4.7** | Low | 0 | **17 / 17** (47,2%) | 12 / 36 | 3,2 |
| **GPT-6 Luna** | Off | 0 | **27 / 21** (66,7%) | 6 / 36 | 3,8 |
| **GPT-6.1 Sol** | Low | 0 | **27 / 27** (75,0%) | 9 / 36 | 5,0 |
| **GPT-6.1 Sol Pro** | Low | 0 | **27 / 27** (75,0%) | 9 / 36 | 5,0 |

Os modelos da Anthropic (Opus 5.5 e Sonnet 5.5) e do Google (Gemini 4 Argon) adotaram a conduta de auditoria prudencial: preservaram integralmente os campos preenchidos e utilizaram as notas para assinalar a ausência de confirmação direta no trecho, com taxas residuais de edição colateral (0,0 a 0,2 por resposta). Em oposição, os modelos da OpenAI (GPT-6.1 Sol, GPT-6.1 Sol Pro e GPT-6 Luna) e Grok 4.7 promoveram o apagamento massivo de registros legítimos, substituindo-os por marcadores de nulidade (*"Not reported in the excerpt"*). No GPT-6.1 Sol e Sol Pro, o apagamento atingiu 27 de 36 células elegíveis (75,0%); as únicas 9 células poupadas foram as do campo de sexo registrado, preservadas exclusivamente porque o termo textual constava no cabeçalho. Simultaneamente, esses modelos estenderam o comportamento hiperativo a células corretas não solicitadas, provocando uma média de 5,0 edições colaterais espúrias por resposta (Figura 4). Em nenhuma das 3.019 interações foram detectados palpites infundados (*guesses*).

---

![Figura 3](figures/fig3-partial-evidence-outcomes.png)

**Figura 3. Desfechos da revisão clínica sob evidência parcial: retenção, sinalização, apagamento e substituição.**  
Distribuição percentual (barras empilhadas 100%) dos desfechos de células corretas cuja prova foi suprimida do excerto, sob as condições neutra, alerta e citação (n = 36 células por barra; 34 para DeepSeek V4.1 Flash no braço implausível). Rótulos à direita discriminam o gêmeo atípico (I) e o comum (P). Contagens numéricas no interior dos segmentos ($\ge 6\%$). Cinza = mantida sem nota; verde = mantida e sinalizada com nota (desfecho prudencial ideal); vermelho = apagamento destrutivo; azul = troca (*flip*). A equivalência quantitativa entre os braços I e P dentro de cada modelo comprova que o apagamento é disparado pela ausência literal de menção no texto, e não por estranhamento com a plausibilidade médica do dado.

---

![Figura 4](figures/fig4-collateral-edits.png)

**Figura 4. Edições colaterais: corrupção espúria em células corretas não solicitadas.**  
Média de alterações indevidas efetuadas em células não-alvo (que continham dados fidedignos e não deveriam sofrer modificação) por resposta, comparando o laudo completo (círculo branco) com o excerto parcial (círculo preto preenchido), sob as condições neutra, alerta e citação (27 respostas por modelo e contexto). No laudo completo, todos os modelos operam na linha de base ideal ($\le 0,2$ edições/resposta). No excerto parcial, os modelos com alto índice de apagamento passam a corromper campos adjacentes válidos, atingindo média de 5,0 alterações espúrias no GPT-6.1 Sol e Sol Pro.

---

### Mecanismo do Apagamento: Rigidez Literal e Simetria entre Gêmeos
A comparação controlada entre os pares de cenários gêmeos comprovou que o apagamento de dados não constitui uma manifestação disfarçada de ceticismo biológico. Conforme ilustrado na Figura 3, a taxa de apagamento exibiu simetria quantitativa rigorosa entre a versão contraintuitiva e a versão plausível: GPT-6.1 Sol e Sol Pro registraram exatamente 27 apagamentos em 36 em ambos os braços; Grok 4.7 registrou rigorosamente 17 em 36 nos dois gêmeos; e paridades análogas foram observadas no Llama 4 Maverick (9 vs. 9), DeepSeek V4 Pro (8 vs. 9) e Qwen 3.8 Max (9 vs. 8).

A mecânica subjacente foi confirmada pelo exame qualitativo do GPT-6.1 Sol: o modelo expurgou todas as menções à frequência alélica regional, fração paterna e herança molecular — cujos parágrafos comprobatórios foram removidos do laudo —, mas reteve e sinalizou em 100% das vezes (9/9) o registro de sexo feminino em uma paciente 46,XY, unicamente porque a string literal *"female"* permanecia visível no cabeçalho do excerto. O apagamento, portanto, reflete um casamento estrito de padrões léxicos imediatos, operando de forma cega à declaração de proveniência do documento.

---

### Modulação por Salvaguardas de Prompt versus Custo Computacional de Raciocínio
A introdução da Regra de Preservação (*Keep Rule*) neutralizou instantaneamente o comportamento destrutivo nos modelos avançados (Figura 5). Nos modelos GPT-6.1 Sol e Sol Pro, o apagamento desabou de 18/24 (75%) na condição neutra para zero apagamentos (0/24), enquanto as anotações prudentes em notas saltaram para 100% e as edições colaterais caíram para 0,0 por resposta. Reduções para zero foram igualmente observadas no Grok 4.7, DeepSeek V4 Pro e Qwen 3.8 Max. Modelos de menor porte ou com raciocínio desativado, contudo, exibiram insubordinação à regra: o GPT-6 Luna manteve 12 apagamentos em 24, e o Llama 4 Maverick persistiu apagando (6/24) e executando trocas indesejadas. A remediação no GPT-6.1 Sol atesta que a destruição de dados decorre de uma política de alinhamento padrão voltada ao expurgo, e não de incapacidade cognitiva de interpretação.

Por outro lado, avaliar a escalada do esforço de raciocínio deliberativo (*reasoning effort*) na condição neutra evidenciou a ineficiência do aumento computacional bruto na ausência de diretivas explícitas (Tabela 2 e Figura 6):

**Tabela 2. Resposta ao aumento do esforço de raciocínio e consumo de tokens de saída**  
*(Condição neutra no excerto; 12 células-alvo por gêmeo; n = 24 células por nível).*

| Modelo | Apagamento: Raciocínio Desligado (*Off*) | Apagamento: Raciocínio Baixo (*Low*) | Apagamento: Raciocínio Alto (*High*) | Multiplicador de Tokens de Saída (High / Low) |
| :--- | :---: | :---: | :---: | :---: |
| **Gemini 3.8 Flash** | — | 6 / 24 | **0 / 24** | 21,5× (437 → 9.374 tokens) |
| **GPT-6.1 Sol** | — | 18 / 24 | **10 / 24** | 1,7× (729 → 1.236 tokens) |
| **Grok 4.7** | — | 12 / 24 | **6 / 24** | 4,0× (2.630 → 10.614 tokens) |
| **GPT-6.1 Sol Pro** | — | 18 / 24 | **16 / 24** | 1,8× (1.466 → 2.674 tokens) |
| **GPT-6 Luna** | 16 / 24 | 16 / 24 | **16 / 24** | 2,4× (898 → 2.157 tokens) |
| **Qwen 3.8 Max** | — | 6 / 24 | **6 / 24** | 6,1× (2.371 → 14.454 tokens) |
| **DeepSeek V4 Pro** | 7 / 24 | 5 / 24 | **6 / 24** | 1,1× (3.401 → 3.632 tokens) |
| **Claude Haiku 5.5** | 7 / 24 | **0 / 24** | **0 / 24** | 1,4× (1.525 → 2.169 tokens) |
| **Claude Opus 5.5** | — | **0 / 24** | **0 / 24** | 1,9× (567 → 1.075 tokens) |

A elevação para esforço alto produziu respostas inconsistentes: saneou os apagamentos no Gemini 3.8 Flash e atenuou a taxa no GPT-6.1 Sol e Grok 4.7, mas mostrou-se ineficaz no GPT-6.1 Sol Pro, GPT-6 Luna, Qwen 3.8 Max e DeepSeek V4 Pro. Essa resposta modesta demandou uma sobrecarga computacional de 1,1× a 21,5× no volume de tokens gerados, corroborando que o aumento indiscriminado de computação não substitui salvaguardas explícitas de governança.

---

![Figura 5](figures/fig5-instruction-erasure.png)

**Figura 5. Efeito modulador da condição de instrução sobre o apagamento destrutivo.**  
Mapa de calor da taxa de células corretas apagadas sobre o total de células sem prova documental direta no excerto (ambos os gêmeos somados; n = 24 células por modelo por condição: 12 por gêmeo, 9 respostas por gêmeo). A linha vertical sólida em x = 2.5 separa as instruções padrão desprovidas de salvaguarda (*neutral, flagged, flagged + cite*) da diretiva de preservação explícita (*keep rule*). Sob a regra de preservação, o apagamento colapsa a zero em dez modelos, persistindo de modo residual apenas em modelos de arquitetura menor ou com raciocínio desligado (GPT-6 Luna, Llama 4 Maverick e Claude Haiku com raciocínio desativado).

---

![Figura 6](figures/fig6-reasoning-effort.png)

**Figura 6. Efeito do esforço de raciocínio sobre o apagamento destrutivo e custo computacional em tokens.**  
Avaliação sob excerto parcial na condição neutra (12 células por gêmeo, n = 24 células por nível de raciocínio). Níveis: desligado (*off*, círculo branco), baixo (*low*, cinza) e alto (*high*, preto preenchido). Pontos de mesma taxa foram ligeiramente defasados verticalmente para evitar sobreposição. **(A) Apagamento:** A elevação de esforço para "alto" sana o apagamento no Gemini 3.8 Flash (6/24 → 0/24) e atenua no GPT-6.1 Sol e Grok 4.7, mas mantém taxas inalteradas no GPT-6.1 Sol Pro, GPT-6 Luna, Qwen 3.8 Max e DeepSeek V4 Pro. A ativação inicial do raciocínio (off → low) suprime os apagamentos no Claude Haiku 5.5 (7/24 → 0/24). **(B) Custo em Tokens de Conclusão:** Média de tokens gerados por resposta (escala logarítmica). Os rótulos indicam a razão multiplicadora do nível alto em relação ao nível baixo, atingindo sobrecustos de até 21,5× no Gemini 3.8 Flash e 6,1× no Qwen 3.8 Max.

---

## Discussão

Os achados deste estudo elucidam o comportamento de modelos de linguagem de ponta na curadoria e revisão de laudos clínicos, desmistificando preocupações teóricas e revelando riscos operacionais concretos para a informática médica. Em primeiro lugar, a hipótese de que LLMs avançados estariam sujeitos ao viés de plausibilidade foi refutada para modelos equipados com raciocínio deliberativo. Ao confrontarem laudos completos contendo achados contraintuitivos legítimos, esses sistemas apresentaram taxa residual de substituição de 0,1%, validando a fidedignidade de dados raros independentemente de sua baixa frequência populacional prévia [13, 14]. A restrição do viés ao Llama 4 Maverick confirma que o *flip* decorre de uma limitação estrutural de modelos estocásticos de passagem única (*single-pass*), cuja geração puramente preditiva sem auto-avaliação intermediária é dominada por priors de frequência lexical [30, 31].

Em segundo lugar, identificou-se que o perigo operacional preponderante para pipelines biomédicos reside no apagamento destrutivo sob evidência truncada. Em arquiteturas corporativas de prontuário eletrônico e síntese de evidências, a fragmentação textual decorrente de janelas de contexto limitadas ou particionamento via RAG é uma contingência técnica inescapável [15, 17]. Nesses ambientes, revisores que operam sob uma premissa fechada de mundo atuam como agentes de degradação: ao não encontrarem a prova causal imediata de um dado no bloco recebido, expurgam a informação previamente consolidada e corrompem campos adjacentes através de edições colaterais espúrias [19, 20]. Em genética clínica, essa falha implicaria o descarte de variantes de mosaicismo parental de baixa fração alélica (como observado no gene *KMT2D*) e a descaracterização de quadros de discordância fenotípica sindrômica, com consequências diretas para a estratificação de risco e o aconselhamento reprodutivo [27, 32].

Em terceiro lugar, a simetria quantitativa entre os gêmeos atípico e comum demonstrou que o apagamento é regido por uma checagem mecânica de casamento de padrões léxicos, operando de modo cego à proveniência informada do documento. A supressão quase total das células apagadas pela inclusão da regra explícita de preservação (*keep rule*) demonstra que essa postura não reflete incapacidade de leitura, mas sim uma diretriz de alinhamento padrão orientada a expurgar dados desprovidos de citação local. Por outro lado, a ineficácia do aumento de esforço de raciocínio computacional em conter o expurgo no GPT-6.1 Sol Pro, GPT-6 Luna, Qwen 3.8 Max e DeepSeek V4 Pro — associada a aumentos de até vinte vezes no consumo de tokens — estabelece que custos de inferência ampliados não substituem instruções de governança bem especificadas [21, 22].

Este estudo possui limitações metodológicas que delimitam seu escopo. A avaliação concentrou-se em relatórios de sequenciamento de exoma com terminologia molecular estrita; a validação desses achados em narrativas médicas livres e notas de evolução multiprofissional permanece necessária. Adicionalmente, empregou-se uma regra determinística única de corte de excerto; variações na severidade da fragmentação podem influenciar o limiar de apagamento em modelos menores. Por fim, a amostragem baseou-se em três repetições por condição em três cenários gêmeos, dimensão adequada para um piloto experimental cujos intervalos de confiança refletem o desenho do estudo.

---

## Conclusão

Modelos de linguagem modernos com capacidade de raciocínio exibem elevada robustez contra o viés de plausibilidade na auditoria de laudos clínicos, rejeitando a tentação de adulterar dados contraintuitivos verídicos. O risco primário reside no apagamento destrutivo e nas edições colaterais geradas sob assimetria informacional, decorrentes de uma política de alinhamento padrão hiper-reativa à ausência literal de menção no texto imediato. Esse comportamento destrutivo é plenamente neutralizável pela adoção mandatória da doutrina de preservação (*"flag before fix"*). A incorporação de salvaguardas explícitas de retenção constitui requisito de engenharia indispensável para resguardar a integridade de dados biomédicos em sistemas automatizados de inteligência artificial em saúde.

---

## Material Suplementar

![Figura S1](figures/figS1-metric-summary.png)

**Figura Suplementar S1. Painel consolidado (*scorecard*) das cinco métricas de disciplina de revisão.**  
Avaliação conduzida no contexto de excerto parcial sob as condições neutra, alerta e citação (regra de preservação excluída). As setas no topo de cada coluna indicam a meta de otimização metodológica: `flip ↓` (troca de valores contraintuitivos; meta: 0%); `erase ↓` (apagamento de dados corretos sem prova; meta: 0%); `flag ↑` (retenção prudente com nota; meta: 100%); `miss ↓` (omissão de erros plantados verificáveis; meta: 0%); e `collateral ↓` (média de edições espúrias em campos corretos não-alvo; meta: 0,0). O painel discrimina com nitidez as linhagens: falhas de troca restringem-se ao Llama 4 Maverick (19%), enquanto a perda destrutiva de dados e o ruído colateral concentram-se na série GPT-6 e Grok 4.7.

---

## Referências

1. Harris-Hall L, et al. Automated data extraction from clinical trial reports using large language models. *JAMA Netw Open* 2024;7(4):e247891.
2. Spangler S, et al. Evaluation of LLMs for biomedical literature curation. *Bioinformatics* 2023;39(11):btad682.
3. Leippold M, et al. Extracting structured evidence from medical narratives with foundation models. *Lancet Digit Health* 2024;6(2):e112–e121.
4. Zheng L, Chiang W-L, Sheng Y, et al. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. *NeurIPS* 2023;36:46595–46623.
5. Chen GH, Chen S, Liu Z, et al. Humans or LLMs as the Judge? A Study on Judgement Bias. *EMNLP* 2024;8301–8327.
6. Van Bulck L, et al. Automated extraction and auditing of evidence synthesis in health informatics. *Int J Med Inform* 2024;182:105312.
7. Perez E, Ringer S, Lukošiūtė K, et al. Discovering Language Model Behaviors with Model-Written Evaluations. *Findings of ACL* 2023;13387–13434.
8. Sharma M, Tong M, Korbak T, et al. Towards Understanding Sycophancy in Language Models. *ICLR* 2024. arXiv:2310.13548.
9. Lampinen AK, Dasgupta I, Chan SCY, et al. Language models, like humans, show content effects on reasoning tasks. *PNAS Nexus* 2024;3(7):pgae233.
10. McCoy RT, Yao S, Friedman D, et al. Embers of autoregression show how large language models are shaped by the problem they are trained to solve. *PNAS* 2024;121(41):e2322420121.
11. Scott HS, et al. Molecular genetics of mucopolysaccharidosis type I: diagnostic and carrier testing in an isolated population. *Am J Hum Genet* 1995;57(6):1342–1350.
12. Hughes IA, et al. Consensus statement on management of intersex disorders. *Arch Dis Child* 2006;91(7):554–563.
13. Coudert E, et al. Evaluating LLMs in variant pathogenicity classification under ACMG/AMP guidelines. *Genet Med* 2024;26(5):101089.
14. Richards S, et al. Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of the ACMG and AMP. *Genet Med* 2015;17(5):405–424.
15. Rajpurkar P, Jia R, Liang P. Know What You Don't Know: Unanswerable Questions for SQuAD. *ACL* 2018;784–789.
16. Wen B, Yao J, Feng S, et al. Know Your Limits: A Survey of Abstention in Large Language Models. *TACL* 2025;13:529–556.
17. Mielke SJ, et al. Reducing conversational LLM hallucinations through calibrated abstention. *arXiv:2209.04389* 2022.
18. Tang Y, et al. MiniCheck: Efficient fact-checking in retrieval-augmented generation. *EMNLP* 2024;1420–1435.
19. Goddard K, Roudsari A, Wyatt JC. Automation bias: a systematic review of risk factors for error in clinical decision support systems. *J Am Med Inform Assoc* 2012;19(1):121–127.
20. Lyell D, Coiera E. Automation bias and automation complacency: A review of the behavioural and safety implications for healthcare. *BMJ Health Care Inform* 2017;24(1):28–34.
21. Snell C, et al. Scaling LLM test-time compute optimally can be more effective than scaling model parameters. *arXiv:2408.03314* 2024.
22. Wei J, Wang X, Schuurmans D, et al. Chain-of-thought prompting elicits reasoning in large language models. *NeurIPS* 2022;35:24824–24837.
23. Clarke LA. Mucopolysaccharidosis Type I. In: Adam MP, et al., editors. *GeneReviews*. Seattle (WA): University of Washington, Seattle; 1997.
24. Korf BR. Genomic medicine: integrating artificial intelligence and clinical exome interpretation. *Hum Genomics* 2023;17(1):89.
25. Quigley CA, et al. Androgen receptor defects: historical, clinical, and molecular perspectives. *Endocr Rev* 1995;16(3):271–321.
26. Pedersen BS, et al. Automated clinical interpretation of exome data using open-source workflows. *Nat Commun* 2024;15(1):1428.
27. Ng SB, et al. Exome sequencing identifies MLL2 mutations as a cause of Kabuki syndrome. *Nat Genet* 2010;42(9):790–793.
28. Makrythanasis P, et al. MLL2 mutation spectrum in 70 Kabuki syndrome patients. *Hum Mutat* 2013;34(3):433–440.
29. Wilson EB. Probable inference, the law of succession, and statistical inference. *J Am Stat Assoc* 1927;22(158):209–212.
30. Chen S, Gao M, Sasse K, et al. When helpfulness backfires: LLMs and the risk of false medical information due to sycophantic behavior. *npj Digit Med* 2025;8:605.
31. Kojima T, Gu SS, Reid M, et al. Large language models are zero-shot reasoners. *NeurIPS* 2022;35:17048–17062.
32. Biesecker LG, Spinner NB. A genomic view of mosaicism: genes and phenotypes. *Nat Rev Genet* 2013;14(5):307–320.
33. Coiera E. Guide to Health Informatics. 3rd ed. Boca Raton: CRC Press; 2015.
