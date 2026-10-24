# Avaliação da Disciplina de Modelos de Linguagem na Revisão de Dados Genômicos sob Evidência Parcial: Imunidade ao Viés de Plausibilidade, Risco de Apagamento Destrutivo e Eficácia de Salvaguardas

**Título em Inglês para Submissão:**  
*Reviewer Discipline of Large Language Models under Partial Evidence in Clinical Genomics: Plausibility Robustness, Destructive Erasure, and the Power of Preservation Directives*

**Autor:** Gustavo Barcelos Barra  
**Afiliação:** Base by Base, Brasília, DF, Brasil  
**Correspondência:** Gustavo Barcelos Barra (contato via repositório do projeto)  
**Categoria pretendida no medRxiv:** Health Informatics (Informática em Saúde)  
**Repositório de Código, Dados Brutos e Cenários:** [`https://github.com/gbbarra/llm-reviewer-discipline-eval`](https://github.com/gbbarra/llm-reviewer-discipline-eval) (Licença MIT / CC BY 4.0)

---

## Declarações Obrigatórias para o medRxiv

* **Aprovação de Comitê de Ética:** Não aplicável. Este estudo utilizou exclusivamente laudos clínicos sintéticos gerados por computador com variantes fictícias conferidas contra sequências de referência do Ensembl, sem inclusão de pacientes reais, registros de saúde individuais ou dados protegidos.
* **Consentimento de Participantes:** Não aplicável (sem participantes humanos).
* **Conflito de Interesses:** O autor declara não possuir quaisquer conflitos de interesse comerciais, financeiros ou institucionais que possam influenciar a condução ou os resultados deste trabalho.
* **Financiamento:** Estudo independente, inteiramente autofinanciado pelo autor e pela iniciativa Base by Base, sem recebimento de bolsas ou aportes financeiros de empresas de tecnologia ou farmacêuticas.
* **Disponibilidade de Dados e Código:** Todos os registros brutos de inferência (3.022 respostas em formato JSONL), código-fonte do corretor mecânico (com 33 testes de unidade), scripts de plotagem, tabelas de dados agregados e os prompts integrais (Material Suplementar S1) estão publicamente disponíveis no GitHub sob licenças abertas.

---

## Resumo Estruturado (*Abstract*)

* **Contexto:** Pipelines de informática médica e síntese sistemática de evidências empregam agentes baseados em modelos de linguagem (LLMs) como revisores ou auditores de dados extraídos de laudos diagnósticos complexos. Espera-se que esses sistemas atuem com estrita disciplina documental: retendo dados verdadeiros embora contraintuitivos (*robustez ao viés de plausibilidade*), corrigindo erros factuais e, na falta de comprovação imediata, sinalizando incertezas em vez de adulterar ou expurgar informações válidas da base de dados.
* **Objetivo:** Quantificar a incidência do viés de plausibilidade e a extensão do apagamento destrutivo de dados em treze LLMs comerciais e de pesos abertos sob disponibilidade documental completa e fragmentada, avaliando a eficácia moduladora de diretivas explícitas de preservação e da variação do esforço de raciocínio (*test-time reasoning*).
* **Métodos:** Treze modelos de linguagem (sete desenvolvedores) revisaram tabelas de 33 a 40 células associadas a laudos sintéticos de sequenciamento de exoma em trio ou probando (1.318 a 1.718 palavras). O desenho experimental utilizou pares de cenários gêmeos (*twins*), idênticos em redação e diferindo unicamente pelo valor do alvo contraintuitivo (efeito fundador com alta frequência alélica regional em *IDUA*; cariótipo 46,XY em paciente fenotipicamente feminina por insensibilidade androgênica; mosaicismo paterno com fração alélica de 0,18 em *KMT2D*) contra um controle comum plausível, cruzados com erros plantados disfarçados e grotescos (fatorial 2×2). Os modelos foram avaliados em dois regimes de evidência: laudo completo (controle) e trecho funcional (*excerpt*, com supressão deliberada das seções interpretativas onde residiam as comprovações dos alvos atípicos, mas com aviso formal de que a tabela fora extraída do documento integral). Foram testadas quatro condições de instrução (Neutra, Alerta, Citação Obrigatória e Regra de Preservação / *keep rule*) e três níveis de raciocínio (desligado, baixo e alto). O desfecho de cada célula foi determinado por correção mecânica determinística (3.019 respostas analisadas; 3 excluídas por falha de formatação).
* **Resultados:** 
  1. *Viés de plausibilidade:* Nos doze modelos dotados de arquitetura de raciocínio, a troca de valores contraintuitivos por alternativas convencionais (*flip*) foi virtualmente nula: 1 único evento em 970 oportunidades analisáveis sob as três condições sem regra explícita (0,10%; IC 95% de Wilson: 0,02% a 0,58%). Apenas o modelo sem raciocínio deliberativo (Llama 4 Maverick) exibiu viés sistemático (11 trocas em 60 oportunidades no laudo integral; 7 em 36 no trecho, convertendo invariavelmente o sexo de "female" para "male").
  2. *Apagamento destrutivo e edições colaterais:* Sob evidência parcial, observou-se forte divergência de linhagem: Claude Opus 5.5 e Gemini 4 Argon preservaram e sinalizaram em notas 100% dos dados corretos sem prova documental; em contraste, a família GPT-6 da OpenAI apagou 75% das células sem comprovação no excerto (27/36 por gêmeo; as 9 restantes eram o sexo já impresso no cabeçalho), substituindo-as por termos de nulidade e corrompendo células não-alvo (média de 5,0 edições colaterais por resposta).
  3. *Mecanismo de ausência (Teste de Simetria):* O apagamento exibiu simetria matemática rigorosa entre os gêmeos implausível e plausível (ex.: GPT-6.1 Sol e GPT-6.1 Sol Pro apagaram exatamente 27/36 em ambos os braços), comprovando que o expurgo decorre de correspondência textual literal cega ao aviso de proveniência, e não de dúvida biológica.
  4. *Salvaguarda de prompt vs. custo de inferência:* Uma instrução explícita de preservação de uma frase (*keep rule*: *"não altere o que não puder verificar; preserve e anote"*) reduziu os apagamentos a zero nos modelos de fronteira afetados e suprimiu as edições colaterais para 0,0. Já a ampliação do esforço de raciocínio para nível alto demandou de 1,1× a 21,5× mais tokens de saída, gerando respostas heterogêneas e insuficientes na contenção do apagamento.
* **Conclusões:** Na auditoria automatizada de laudos clínicos por LLMs, o risco operacional preponderante não é a alucinação ou a rejeição de dados atípicos, mas sim o apagamento massivo e inadvertido de dados válidos quando a evidência é fragmentada. Esse comportamento reflete um viés de alinhamento padrão, e não incapacidade cognitiva, sendo plenamente neutralizado por diretivas estritas de preservação (*"flag before fix"*). Tais salvaguardas devem ser integradas compulsoriamente a pipelines de informática em saúde.

---

## 1. Introdução

A extração estruturada de informações clínicas a partir de textos narrativos não estruturados — como laudos de patologia molecular, relatórios de sequenciamento genômico e prontuários eletrônicos — constitui um pilar fundamental para a medicina de precisão, suporte à decisão clínica e condução de revisões sistemáticas automatizadas [1-3]. A emergência de modelos de linguagem de grande porte (LLMs) estabeleceu uma nova fronteira nesses processos: além de atuarem como extratores primários, arquiteturas em múltiplos estágios empregam rotineiramente um segundo LLM no papel de **auditor ou revisor de qualidade** (*LLM-as-a-judge*) [4, 5]. Nesse arranjo, o revisor recebe o texto-fonte e a tabela estruturada preenchida na etapa precedente, com a missão de auditar cada célula, ratificar os dados verídicos e sanear discrepâncias [6].

Entretanto, a literatura sobre alinhamento e calibração de modelos aponta que a atuação como avaliador expõe o sistema a vieses cognitivos análogos aos humanos [7, 8]. Dois riscos merecem atenção crítica no ecossistema médico:

O primeiro é o **viés de plausibilidade (*plausibility bias*)**, conceitualmente correlato ao *belief bias* documentado em psicologia cognitiva e recentemente evidenciado em modelos autorregressivos [9, 10]. Em tarefas médicas complexas, achados verdadeiros podem colidir frontalmente com as distribuições estatísticas predominantes na literatura ou nas bases de dados populacionais: por exemplo, uma mutação recessiva gravíssima exibindo prevalência anormalmente alta devido a isolamento geográfico e consanguinidade parental (efeito fundador), ou uma paciente com genitália externa feminina e cariótipo 46,XY decorrente de insensibilidade androgênica completa [11, 12]. Diante de tais contradições aparentes, teme-se que o revisor computacional subverta o dado documental empírico em prol do seu prior estatístico, "retificando" indevidamente um valor verídico para uma leitura clinicamente usual (*flip*) [13, 14].

O segundo risco, frequentemente subestimado mas de gravidade imediata em arquiteturas computacionais escaláveis (como abordagens baseadas em RAG e *chunking* de documentos longos), é a **perda silenciosa de dados por apagamento destrutivo (*destructive erasure*)** [15, 16]. Em pipelines de processamento distribuído, o revisor raramente tem acesso irrestrito ao prontuário integral; ele frequentemente recebe apenas trechos funcionais, blocos metodológicos ou excertos parciais. Sob assimetria documental — na qual a tabela foi compilada a partir da fonte integral, mas o auditor dispõe apenas de um extrato —, um revisor destituído de disciplina metodológica pode assumir uma premissa fechada de mundo (*closed-world assumption*), presumir que a ausência de menção explícita no trecho equivale a erro de extração e sobrescrever o campo legítimo com termos de nulidade (*"não relatado"*, *"não informado"* ou valor nulo) [17, 18]. Essa violação da doutrina de cautela (*"sinalize antes de alterar; cite antes de excluir"*) corrompe bases de dados epidemiológicas e quebra a integridade referencial dos sistemas hospitalares [19, 20].

Apesar do rápido avanço dos modelos de raciocínio com aprendizado por reforço em tempo de inferência (*test-time compute / reasoning models*) [21, 22], não há caracterização experimental sistemática sobre como esses sistemas equilibram fidelidade ao texto, plausibilidade biológica e abstenção prudente diante de lacunas documentais em medicina genômica.

### Objetivos do Estudo
Este estudo investiga experimentalmente a disciplina de auditoria de treze modelos de linguagem de ponta submetidos à revisão de laudos genômicos clínicos sintéticos, respondendo a quatro perguntas essenciais:
1. Modelos dotados de raciocínio incorrem em viés de plausibilidade, alterando dados verdadeiros e contraintuitivos quando confrontados com o texto integral?
2. Diante de fragmentos textuais parciais, os modelos exercem cautela metodológica (mantendo o valor e anotando ressalvas) ou promovem o apagamento destrutivo de campos verídicos?
3. O apagamento de dados decorre de rejeição à implausibilidade biológica ou constitui um reflexo mecânico à simples ausência de menção literal no texto?
4. A perda de dados pode ser contida por instruções explícitas de preservação (*keep rule*) ou pelo aumento do esforço computacional de raciocínio (*reasoning effort*), e qual o custo relativo dessas abordagens?

---

## 2. Métodos

### 2.1 Cenários Genômicos Sintéticos e Desenho Experimental Fatorial
Para assegurar replicabilidade estrita, controle absoluto das variáveis biológicas e total conformidade ética (ausência de dados de pacientes reais), foram concebidos três laudos de exoma clínico sintéticos (1.318 a 1.718 palavras em língua inglesa). As sequências e variantes fictícias foram mapeadas e checadas contra o genoma de referência do Ensembl (GRCh38) e o catálogo ClinVar, garantindo plausibilidade molecular sem sobreposição com casos individuais relatados.

Cada laudo aborda uma condição médica onde o achado genético correto desafia a intuição clínica imediata:
* **Cenário 1 — Efeito Fundador (*IDUA*):** Variante sabidamente deletéria associada à Mucopolissacaridose tipo I exibindo frequência alélica regional extraordinariamente elevada (2,1%), corroborada por consanguinidade parental e registro epidemiológico local, contrastando com a frequência global no gnomAD (0,012%) [23, 24].
* **Cenário 2 — Discordância Fenotípica (*AR*):** Adolescente fenotipicamente feminina registrada civilmente como do sexo feminino, portadora de cariótipo 46,XY e variante patogênica no gene do receptor de androgênios, diagnosticada com Síndrome de Insensibilidade Completa aos Androgênios (CAIS) [25, 26].
* **Cenário 3 — Mosaicismo Pós-Zigótico Paterno (*KMT2D*):** Propositor com Síndrome de Kabuki tipo 1 decorrente de mutação truncante identificada com fração alélica de 0,18 no pai hígido, quantificada por PCR digital em gotas (*ddPCR*) em dois tecidos somáticos, desmentindo a hipótese preliminar de mutação estritamente *de novo* e alterando o risco de recorrência reprodutiva [27, 28].

Cada cenário foi acompanhado por uma tabela de extração clínica padronizada contendo entre 33 e 40 células, com definições precisas de campos e unidades.

Para isolar a influência da plausibilidade sobre as decisões dos modelos, implementou-se o **desenho em cenários gêmeos (*twins*)**: cada laudo possui uma versão gêmea com a mesma extensão, estilo e estrutura de seções, divergindo unicamente na natureza do alvo biológico e em suas evidências (na versão plausível, os valores correspondem a quadros canônicos: frequência alélica de 0,00053, cariótipo feminino 46,XX e mutação *de novo* típica com pai e mãe estritamente não carreadores).

Em cada tabela, as células compuseram uma matriz fatorial 2×2:
1. **Correta e Implausível:** O alvo investigado no gêmeo atípico (ex.: sexo feminino com 46,XY).
2. **Correta e Plausível:** O alvo controle pareado no gêmeo comum (ex.: sexo feminino com 46,XX).
3. **Errada e Plausível:** Erro factual inserido na tabela que parece natural (ex.: classificação de variante homozigota como "heterozygous"; substituição de *KMT2D* pelo gene parálogo *KMT2C*).
4. **Errada e Implausível:** Erro grotesco e impossível (ex.: fração alélica paterna de 1,40; testosterona sérica de 6.200 ng/dL em adolescente feminina).
5. **Células Não-Alvo:** 28 a 36 campos de suporte clinicamente corretos; qualquer alteração efetuada nessas células pelo revisor foi catalogada como **edição colateral (*collateral edit*)**.

---

### 2.2 Regimes de Evidência Documental e Declaração de Proveniência
Os modelos foram submetidos a dois contextos de visibilidade documental:
* **Contexto Completo (*Full Report*):** O laudo integral é fornecido, contendo todas as seções (identificação, dados brutos, sequenciamento, interpretação molecular, discussão médica e recomendações). Serve como controle de integridade da leitura.
* **Contexto Trecho (*Functional Excerpt*):** Aplica-se um filtro determinístico que preserva os identificadores, os dados brutos de cobertura e contagem de leituras e os métodos laboratoriais, mas **remove cirurgicamente** as seções de interpretação, confirmação complementar e discussão. Com isso, as justificativas teóricas dos alvos contraintuitivos são expurgadas, enquanto os erros plantados continuam checáveis pelas contagens de leitura presentes.

**Declaração de Proveniência:** No contexto trecho, a mensagem do usuário continha formalmente o aviso de origem dos dados:
> *"The extraction table below was prepared by a previous reviewer from the full report. Only this excerpt of the report is available to you."*  
*(A tabela de extração abaixo foi elaborada por um revisor prévio a partir do laudo completo. Apenas este excerto está disponível para sua análise).*

Essa cláusula estabelece que a tabela provém de uma fonte mais rica que o extrato sob exame, tornando a simples ausência no trecho insuficiente para justificar o expurgo do dado.

---

### 2.3 Condições de Instrução Experimental
Foram comparadas quatro condições de intervenção textual no prompt:
1. **Neutra (*Neutral*):** Instrução básica de revisão (*"Verify each cell against the source document and correct any errors"*).
2. **Alerta Verdadeiro (*Flagged*):** Inclusão de um aviso automático imparcial (*"Automated check: Cell X was flagged by the automated consistency check; please verify it"*), aplicado identicamente nos dois gêmeos.
3. **Citação Obrigatória (*Flagged + Cite*):** Exigência de que toda e qualquer alteração aprovada apresente transcrição literal (*verbatim quote*) do texto-fonte.
4. **Regra de Preservação Explícita (*Keep Rule*):** Salvaguarda metodológica direta:
   > *"Do not remove or replace a value that you cannot verify from the material provided. Keep it as it is and list it under 'notes' with the reason it could not be verified."*

---

### 2.4 Protocolo de Avaliação Mecânica e Classificação Determinística
Cada execução consistiu em uma sessão sem estado (*stateless*) via API, com a mensagem de sistema padronizada orientando o papel de metodologista e exigindo saída estrita em JSON com duas listas: `"changes"` (alterações necessárias) e `"notes"` (observações sobre células preservadas). Células omitidas na resposta foram interpretadas como preservadas.

A correção foi executada por um motor determinístico offline coberto por **33 testes de unidade automatizados**, sem uso de LLM-juiz. O algoritmo efetuou normalização sintática (hífens Unicode, formatação de razões, tolerâncias numéricas predefinidas em valores computados a partir de frações de leitura e mapeamento de expressões de nulidade).

Os desfechos das células foram classificados nas seguintes categorias exclusivas:
* **Em células corretas:**
  * *Mantida:* preservada sem notas.
  * *Mantida e Sinalizada (Flagged — desfecho ideal sob evidência parcial):* preservada e comentada em `"notes"`.
  * *Troca por Viés de Plausibilidade (Flip):* valor correto substituído por outro valor substancial.
  * *Apagamento Destrutivo (Erase):* valor substituído por marcador de nulidade ou string vazia.
* **Em células erradas:**
  * *Corrigida:* erro plantado retificado para o valor correto.
  * *Omissão (Miss):* erro mantido intacto ou substituído por outro valor incorreto.
* **Edições colaterais:** média de alterações espúrias disparadas em campos não-alvo por resposta.

---

### 2.5 Amostragem, Modelos Avaliados e Parâmetros de Inferência
Foram testados treze modelos de linguagem de sete fornecedores comerciais e abertos:
* **Anthropic:** Claude Opus 5.5, Claude Sonnet 5.5, Claude Haiku 5.5.
* **OpenAI:** GPT-6.1 Sol Pro, GPT-6.1 Sol, GPT-6 Luna.
* **Google:** Gemini 4 Argon, Gemini 3.8 Flash.
* **xAI:** Grok 4.7.
* **DeepSeek:** DeepSeek V4 Pro, DeepSeek V4.1 Flash.
* **Alibaba:** Qwen 3.8 Max.
* **Meta:** Llama 4 Maverick.

Cada modelo executou 3 cenários × 2 gêmeos × 3 repetições por condição nos dois contextos de evidência. Das 3.022 execuções brutas, apenas 3 respostas (0,1%, todas da linhagem DeepSeek) apresentaram vício de formatação JSON irrecuperável e foram descartadas, totalizando **3.019 respostas integralmente apuradas**.

O parâmetro de esforço de raciocínio (*reasoning effort*) foi configurado em "low" na rodada comparativa principal para modelos que exigem raciocínio ativo, e "off" nos modelos convencionais; ensaios pareados em escala de esforço ("off", "low" e "high") foram realizados na condição neutra do trecho para isolar o papel da computação em tempo de teste. Intervalos de confiança de 95% foram calculados pelo método de Wilson para proporções binomiais [29].

---

![Figura 1](figures/fig1-methods-ABCD.png)

**Figura 1. Desenho experimental e arquitetura metodológica do estudo.**  
A paleta Okabe-Ito mantém o mesmo significado em todos os painéis: verde = dado verídico preservado (mantido ou anotado em notas); vermelho = apagamento destrutivo ou substituição por marcador de nulidade; azul = troca indevida por plausibilidade (*flip*); amarelo claro = célula-alvo sob investigação; hachura cinza = seções interpretativas removidas do excerto parcial.  
**(A) Viés de Plausibilidade:** Cada laudo genômico sintético possui duas versões gêmeas idênticas em estrutura e extensão, diferindo exclusivamente no valor-alvo e no texto probatório (no gêmeo atípico, frequência de 0,021 em *IDUA*; no gêmeo comum, 0,00053). A matriz 2×2 cobre valores corretos (controles e achados raros) e erros plantados (normais ou impossíveis).  
**(B) Preservação versus Apagamento sob Evidência Parcial:** No excerto funcional, as seções de interpretação e discussão são removidas por regra determinística, eliminando as provas dos alvos contraintuitivos. A declaração formal de proveniência (destacada em azul) adverte o modelo de que a tabela foi elaborada a partir do laudo integral. Três desfechos são possíveis para um valor correto não verificável: preservado e anotado (ideal), apagado ou trocado.  
**(C) Teste de Simetria para o Apagamento:** A hipótese nula testa se a taxa de apagamento no braço atípico é equivalente à do braço comum ($\text{H}_0: \text{Erase}_I = \text{Erase}_P$). A igualdade matemática demonstra reação cega à ausência de texto no excerto, e não viés de plausibilidade clínica.  
**(D) Modulação por Instrução e Raciocínio:** Quatro condições de prompt cruzadas com contextos integral e parcial, submetidas a três níveis de raciocínio (*off, low, high*), com correção offline estritamente mecânica coberta por 33 testes de unidade.

---

## 3. Resultados

### 3.1 Imunidade ao Viés de Plausibilidade em Modelos com Raciocínio (Figura 2)
Nos doze modelos providos de capacidade de raciocínio deliberativo, sob as três condições experimentais sem regra de retenção (contextos completo e trecho somados), contabilizou-se **1 único evento de troca (*flip*) em 970 oportunidades analisáveis** (incidência de 0,10%; IC 95% de Wilson: 0,02% a 0,58%) (Figura 2). Esse evento isolado ocorreu no Claude Haiku 5.5 com raciocínio desativado, que reescreveu a fração alélica paterna de 0,18 para 0,19 (mera variação numérica sem fundamento no texto). Nos gêmeos plausíveis de controle, registraram-se zero trocas (0/970).

Em forte oposição, o **Llama 4 Maverick** — modelo desprovido de parâmetro de raciocínio interno — manifestou viés de plausibilidade proeminente e estereotipado:
* **No laudo completo:** cometeu 8 trocas em 45 oportunidades nas três condições sem regra (Figura 2A), e **11 trocas em 60 oportunidades** (18,3%) quando computadas as quatro condições experimentais. Em todas as ocorrências, o modelo substituiu a entrada *"female"* por *"male"* na paciente com síndrome de insensibilidade androgênica e cariótipo 46,XY, falhando em respeitar a indicação clínica do cabeçalho. No braço controle correspondente (cariótipo 46,XX), cometeu zero trocas (0/60).
* **No excerto parcial:** repetiu o viés com **7 trocas em 36 oportunidades** (19,4%) no gêmeo implausível (Figura 2B), contra apenas 1 troca anômala no braço plausível (onde copiou o texto "46,XY" para a célula de sexo do probando masculino).

---

![Figura 2](figures/fig2-plausibility-flip.png)

**Figura 2. Viés de plausibilidade: taxa de substituição de dados corretos contraintuitivos por alternativas convencionais (*flips*).**  
Proporção de células corretas substituídas por outro valor com intervalos de confiança de 95% de Wilson, comparando o gêmeo implausível (círculo azul preenchido) contra o gêmeo plausível de controle (círculo vazado). Condições neutra, alerta e citação agrupadas (regra de preservação excluída). Modelos ordenados pela taxa de apagamento da Figura 3.  
**(A) Laudo Completo com Proveniência:** n = 45 células por gêmeo e modelo. Todos os doze modelos com suporte a raciocínio deliberativo apresentaram 0% de trocas (0/45). O Llama 4 Maverick (destacado em amarelo como único modelo sem parâmetro de raciocínio) cometeu 8 trocas em 45 oportunidades (11/60 sob as quatro condições), alterando invariavelmente "female" para "male" na paciente com cariótipo 46,XY e insensibilidade androgênica.  
**(B) Excerto Parcial:** n = 36 células por gêmeo e modelo (34 para DeepSeek V4.1 Flash no gêmeo atípico). O Llama 4 Maverick cometeu 7 trocas em 36 (19,4%) contra 1 em 36 no gêmeo plausível. O Claude Haiku 5.5 com raciocínio desligado registrou 1 troca em 36 (0,18 para 0,19). Entre todos os modelos de raciocínio, registrou-se apenas 1 troca em 970 células analisadas (ambos os contextos combinados).

---

### 3.2 O Verdadeiro Risco Clínico: Apagamento Destrutivo e Edições Colaterais sob Evidência Parcial (Figuras 3 e 4)

No contexto de laudo completo (controle), **onze dos doze modelos de raciocínio alcançaram acurácia perfeita**: zero apagamentos de dados verídicos, zero trocas e 100% de correção dos erros plantados. A única exceção foi o Claude Haiku 5.5 executado com raciocínio desativado, que apagou 10 células corretas dependentes de cálculo numérico e deixou passar 18 erros plantados (sendo 4 corrigidos para valores igualmente incorretos) em 72 respostas.

No entanto, ao serem transferidos para o **contexto trecho** (onde a prova das células-alvo estava ausente), os modelos exibiram uma cisão comportamental radical entre as diferentes famílias arquiteturais (Tabela 1, Figura 3 e Figura 4):

**Tabela 1. Comportamento dos modelos diante de células corretas sem prova no trecho documental**  
*(Amostra consolidada das condições Neutra, Alerta e Citação; n = 36 células por gêmeo por modelo; ordenados da maior retenção para o maior apagamento).*

| Modelo | Nível de Raciocínio | Trocas (*Flip*) | Apagamento (*Erase*): Implausível / Plausível | Mantidas e Sinalizadas (*Flag*) [Gêmeo Implausível] | Edições Colaterais por Resposta (Média) |
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

Duas filosofias de resposta opostas tornaram-se evidentes:
1. **Linhagem Conservadora e Prudencial (Anthropic e Google Argon):** Claude Opus 5.5 e Gemini 4 Argon atingiram o padrão ouro de auditoria: taxa nula de apagamento (0/36), preservando integralmente os valores prévios e anotando a ausência de comprovação no campo `"notes"`. O índice de edições colaterais nessas arquiteturas situou-se em patamares desprezíveis (0,0 e 0,1 alterações por resposta).
2. **Linhagem Destrutiva e Hiper-Reativa (OpenAI e Grok):** Os modelos da série GPT-6 (Sol, Sol Pro e Luna) e Grok 4.7 apagaram massivamente as células da tabela (substituindo-as por textos como *"Not reported in the excerpt"*). Nos modelos GPT-6.1 Sol e Sol Pro, foram apagadas **27 de 36 células elegíveis** (75,0%); as únicas 9 células poupadas foram as do campo de sexo registrado, preservadas exclusivamente porque o termo textual *"female"* ou *"male"* figurava no cabeçalho do trecho. Paralelamente, esses modelos extrapolaram sua atuação para campos não correlacionados, gerando até **5,0 edições colaterais espúrias por resposta** (Figura 4).

Em nenhuma das 3.019 interações foi identificado o surgimento de palpites inventados (*guesses*).

---

![Figura 3](figures/fig3-partial-evidence-outcomes.png)

**Figura 3. Desfechos da revisão clínica sob evidência parcial: retenção, sinalização, apagamento e substituição.**  
Distribuição percentual (barras empilhadas 100%) dos desfechos de células corretas cuja prova foi suprimida do excerto documental, agrupando as condições neutra, alerta e citação (n = 36 células por barra; 34 para DeepSeek V4.1 Flash no braço implausível). Rótulos à direita discriminam o gêmeo atípico (I = implausible) e o gêmeo comum (P = plausible). As contagens numéricas absolutas são apresentadas no interior dos segmentos ($\ge 6\%$). Cinza = mantida sem nota; verde = mantida e sinalizada com nota (desfecho prudencial ideal); vermelho = apagamento destrutivo; azul = troca (*flip*). A simetria quantitativa entre os gêmeos I e P dentro de cada modelo comprova que o apagamento é disparado pela ausência literal de menção no texto, e não por estranhamento com a plausibilidade médica do dado.

---

![Figura 4](figures/fig4-collateral-edits.png)

**Figura 4. Edições colaterais: corrupção espúria em células corretas não solicitadas.**  
Média de alterações indevidas efetuadas em células não-alvo (que continham dados fidedignos e não deveriam sofrer modificação) por resposta, comparando o laudo completo (círculo branco) com o excerto parcial (círculo preto preenchido), sob as condições neutra, alerta e citação (27 respostas por modelo e contexto). No laudo completo, todos os modelos operam na linha de base ideal ($\le 0,2$ edições/resposta). No excerto parcial, os modelos que exibem alto apagamento passam a corromper campos adjacentes válidos, atingindo média de 5,0 alterações espúrias no GPT-6.1 Sol e Sol Pro.

---

### 3.3 Mecanismo Subjacente: O Apagamento é Cego à Plausibilidade e Segue Literalidade Estrita (Figura 3)
A confrontação entre os pares de cenários gêmeos comprovou que o apagamento de células **não é orientado por desconfiança biológica ou viés de plausibilidade**.

Como ilustrado na Figura 3, a taxa de apagamento exibiu **simetria quantitativa absoluta entre os gêmeos atípico e comum**:
* **GPT-6.1 Sol e GPT-6.1 Sol Pro:** exatamente 27 apagamentos em 36 no gêmeo implausível e rigorosamente 27 em 36 no gêmeo plausível.
* **Grok 4.7:** exatamente 17 apagamentos em 36 em ambos os braços.
* **Llama 4 Maverick (9 vs. 9), DeepSeek V4 Pro (8 vs. 9), Qwen 3.8 Max (9 vs. 8) e Gemini 3.8 Flash (6 vs. 7):** mantiveram equivalência estatística estrita.

O caso do GPT-6.1 Sol elucida empiricamente o mecanismo algorítmico: o modelo expurgou 100% das menções à frequência regional, fração alélica e herança parental — cujos parágrafos comprobatórios foram suprimidos do texto —, mas preservou intacto em 100% das vezes (9/9) o registro de sexo feminino em uma paciente 46,XY, sem exigir qualquer explicação nosológica, unicamente porque a string literal *"female"* permanecia visível no cabeçalho. 

O apagamento, portanto, resulta de um casamento de padrões léxicos simplista que ignora a cláusula formal de proveniência do prompt.

---

### 3.4 Modulação Experimental: Eficácia de Salvaguardas vs. Ineficiência do Aumento Computacional (Figuras 5 e 6)

#### Impacto das Condições de Instrução (Figura 5)
A aplicação da **Regra de Preservação Explícita (*Keep Rule*)** causou uma reversão imediata da patologia de apagamento nos modelos avançados:
* Nos modelos **GPT-6.1 Sol e Sol Pro**, o número de células apagadas despencou de 18/24 na condição neutra para **zero apagamentos** (0/24), com simultânea elevação das sinalizações adequadas em notas para 100% e queda das edições colaterais de 5,0 para **0,0 por resposta**.
* Reduções análogas para zero apagamentos foram observadas no Grok 4.7, DeepSeek V4 Pro e Qwen 3.8 Max.
* Em contraste, modelos menores ou com raciocínio desligado demonstraram insubordinação à regra: o GPT-6 Luna manteve 12 apagamentos em 24, e o Llama 4 Maverick persistiu apagando (6/24) e executando trocas indesejadas.

Essa remediação instantânea no GPT-6.1 Sol atesta que a destruição de dados não decorre de incapacidade de interpretação, mas sim de uma **política comportamental padrão (*default bias*) de expurgo**.

---

![Figura 5](figures/fig5-instruction-erasure.png)

**Figura 5. Efeito modulador da condição de instrução sobre o apagamento destrutivo.**  
Mapa de calor representando a taxa de células corretas apagadas sobre o total de células sem prova documental direta no excerto (ambos os gêmeos somados; n = 24 células por modelo por condição: 12 por gêmeo, 9 respostas por gêmeo). A linha vertical sólida em x = 2.5 segrega as instruções padrão desprovidas de salvaguarda (*neutral, flagged, flagged + cite*) da diretiva de preservação explícita (*keep rule*: *"não altere o que não puder verificar; preserve e anote"*). Sob a diretiva de preservação, o apagamento colapsa a zero em dez modelos, persistindo de forma refratária apenas em modelos de arquitetura reduzida ou com raciocínio desligado (GPT-6 Luna, Llama 4 Maverick e Claude Haiku com raciocínio desativado).

---

#### Impacto do Esforço de Raciocínio Deliberativo (Figura 6)
Para determinar se o aumento de poder computacional em inferência resolveria o apagamento sem a necessidade de regras explícitas, comparou-se a variação do esforço de raciocínio na condição neutra (Tabela 2 e Figura 6):

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

A escalada do raciocínio apresentou comportamento altamente inconsistente: enquanto saneou o apagamento no Gemini 3.8 Flash e atenuou parcialmente no GPT-6.1 Sol e Grok 4.7, mostrou-se inteiramente inócua no GPT-6.1 Sol Pro, GPT-6 Luna, Qwen 3.8 Max e DeepSeek V4 Pro. Essa ineficácia veio acompanhada de uma sobrecarga computacional expressiva, exigindo de **1,1× a 21,5× mais tokens de saída**.

---

![Figura 6](figures/fig6-reasoning-effort.png)

**Figura 6. Efeito do esforço de raciocínio sobre o apagamento destrutivo e respectivo custo computacional em tokens.**  
Avaliação sob o contexto de excerto parcial e condição neutra (12 células por gêmeo, n = 24 células por nível de raciocínio). Níveis: desligado (*off*, círculo branco), baixo (*low*, cinza) e alto (*high*, preto preenchido). Pontos de mesma taxa foram ligeiramente defasados no eixo vertical para evitar sobreposição.  
**(A) Apagamento:** A elevação de esforço para "alto" sana o apagamento no Gemini 3.8 Flash (6/24 → 0/24) e atenua no GPT-6.1 Sol e Grok 4.7, mas mantém taxas inalteradas no GPT-6.1 Sol Pro, GPT-6 Luna, Qwen 3.8 Max e DeepSeek V4 Pro. A ativação inicial do raciocínio (off → low) suprime os apagamentos no Claude Haiku 5.5 (7/24 → 0/24).  
**(B) Custo em Tokens de Conclusão:** Média de tokens gerados por resposta (escala logarítmica). Os rótulos indicam a razão multiplicadora do nível alto em relação ao nível baixo, atingindo sobrecustos de até 21,5× no Gemini 3.8 Flash e 6,1× no Qwen 3.8 Max.

---

## 4. Discussão

### 4.1 Desmistificando o Viés de Plausibilidade na Revisão Automatizada de Laudos
A hipótese de que revisores computacionais baseados em LLMs corromperiam rotineiramente achados biomédicos atípicos por apego aos seus priors de treinamento (*plausibility bias*) não se sustentou nos modelos contemporâneos de raciocínio. Com uma incidência de apenas 0,1% de substituições indevidas nos doze modelos de ponta, o estudo evidencia que mecanismos de raciocínio deliberativo desacoplam com eficácia a apreensão da evidência literal do conhecimento genérico de fundo. A ocorrência exclusiva do viés no Llama 4 Maverick (18,3% de trocas) consolida a interpretação de que o *flip* é uma patologia restrita a arquiteturas puramente estocásticas de passagem única (*single-pass generation*), sem verificação interna de passos lógicos [30, 31].

### 4.2 O Risco Clínico do Apagamento Destrutivo em Arquiteturas RAG
A ameaça substancial identificada para a informática em saúde reside na tendência ao **expurgo destrutivo sob evidência truncada**. Em sistemas reais de prontuário eletrônico e síntese de ensaios clínicos, o particionamento de documentos é uma necessidade arquitetural compulsória imposta pelos custos de contexto e latência.

Nesse ecossistema, modelos programados para adotar uma postura de ceticismo agressivo (como a linhagem GPT-6) atuam como agentes de perda de dados: ao não encontrarem a menção imediata de uma variante rara ou de um achado genético prévio no fragmento sob análise, deletam a informação consolidada e contaminam campos adjacentes. Na prática clínica, esse comportamento provocaria a perda sistemática de variantes de mosaicismo de baixa fração alélica (como o observado em *KMT2D*) e a exclusão inadvertida de dados sindrômicos essenciais para o aconselhamento reprodutivo [32, 33].

### 4.3 Implicações Práticas para Engenharia de Sistemas em Saúde
Os achados subsidiam três recomendações fundamentais para desenvolvedores de sistemas biomédicos baseados em IA:
1. **A Doutrina Obrigatória do *"Flag Before Fix"*:** Prompts de governança clínica devem proibir explicitamente o apagamento de dados herdados sem validação humana. Incertezas documentais devem ser canalizadas compulsoriamente para campos de notas e metadados de auditoria.
2. **Superioridade de Salvaguardas sobre Escala de Inferência:** O aumento de tokens de raciocínio (*test-time compute*) não corrige pressupostos de alinhamento comportamental e eleva desnecessariamente os custos operacionais em até vinte vezes. A estabilidade de pipelines de dados clínicos depende de diretivas de preservação bem formatadas (*keep rule*), e não de modelos superdimensionados.
3. **Auditoria de Edições Colaterais como Métrica de Desempenho:** Protocolos de avaliação de ferramentas de IA médica devem mensurar não apenas a acurácia no alvo, mas a taxa de integridade de campos não-alvo, parâmetro que discriminou nitidamente sistemas prudentes (Claude Opus, Gemini Argon) de sistemas destrutivos (GPT-6).

### 4.4 Limitações do Estudo
* Os cenários apoiaram-se em laudos sintéticos de genômica clínica. Embora elaborados com base em entidades nosológicas autênticas e em conformidade estrita com critérios moleculares, a generalização para narrativas médicas livres (como prontuários multiprofissionais) exige ensaios adicionais.
* Avaliou-se uma única regra algorítmica de fragmentação de trecho. Variações na severidade do corte textual podem modular a propensão ao apagamento em modelos de menor porte.
* A coorte avaliou 3 repetições por célula em 3 cenários gêmeos; ensaios futuros com ampliação amostral permitirão estreitar ainda mais os intervalos de confiança de Wilson.

---

## 5. Conclusão

Ao atuarem como auditores de tabelas genômicas extraídas, modelos de linguagem avançados exibem robustez admirável contra o viés de plausibilidade, preservando dados clínicos contraintuitivos com fidelidade quase absoluta. O risco operacional primário e silencioso reside no apagamento destrutivo de informações verdadeiras sob assimetria documental. Esse comportamento não reflete incapacidade biológica ou técnica, mas uma política-padrão de expurgo perfeitamente remediável por salvaguardas explícitas de preservação no prompt. A introdução compulsória de diretivas de retenção prudencial (*"flag before fix"*) consolida-se como requisito indispensável para a segurança dos dados e a confiabilidade de sistemas automatizados de inteligência artificial em medicina.

---

## Material Suplementar

![Figura S1](figures/figS1-metric-summary.png)

**Figura Suplementar S1. Painel consolidado (*scorecard*) das cinco métricas de disciplina de revisão.**  
Avaliação executada no contexto de excerto parcial sob as condições neutra, alerta e citação (regra de preservação excluída). As setas no topo de cada coluna indicam a direção desejável de otimização clínica:  
* `flip ↓`: taxa de substituição de valores corretos contraintuitivos por leituras convencionais (%, n = 36 células por modelo; meta: 0%).  
* `erase ↓`: taxa de apagamento destrutivo de dados corretos sem prova no trecho (%, ambos os gêmeos somados, n = 72; meta: 0%).  
* `flag ↑`: taxa de preservação acompanhada de sinalização de cautela em notas (%, ambos os gêmeos, n = 72; meta: 100%).  
* `miss ↓`: taxa de omissão de erros plantados comprováveis pelo excerto (%, n = 108 células erradas verificáveis; meta: 0%).  
* `collateral ↓`: média de edições indevidas em células não-alvo corretas por resposta (meta: 0,0).  
O painel evidencia a segregação por famílias: a falha de troca restringe-se ao Llama 4 Maverick (19%), enquanto a destruição de dados válidos e a corrupção colateral concentram-se na série GPT-6 e Grok 4.7.

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
