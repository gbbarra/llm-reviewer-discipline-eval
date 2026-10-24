# Avaliação da Disciplina de Revisão em Modelos de Linguagem sob Evidência Completa e Parcial: Viés de Plausibilidade, Apagamento Destrutivo e Efeito de Salvaguardas

**Gustavo Barcelos Barra**  
*Estudo exploratório e piloto experimental — Outubro de 2026*  
*Código aberto (Licença MIT), cenários, prompts, logs brutos e dados em:* [`github.com/gbbarra/llm-reviewer-discipline-eval`](https://github.com/gbbarra/llm-reviewer-discipline-eval)  
*Material Suplementar S1:* Prompts integrais submetidos aos modelos em `docs/S1-prompts-sent-to-models.md`.

---

## Resumo Estruturado

* **Contexto:** Modelos de linguagem de grande porte (LLMs) são rotineiramente empregados como revisores em pipelines automatizados de extração de dados e síntese de evidências. Nessa função, espera-se que o modelo atue como auditor fiel: preserve dados verdadeiros (mesmo quando atípicos), corrija erros factuais e, na falta de comprovação no material acessível, registre notas de auditoria em vez de adulterar ou excluir campos.
* **Objetivo:** Investigar a existência de viés de plausibilidade (*plausibility bias*) e quantificar a perda de dados por apagamento (*destructive erasure*) em LLMs atuando como revisores sob evidência documental completa e truncada, avaliando o impacto modulador de instruções explícitas de preservação e de diferentes níveis de esforço de raciocínio (*reasoning effort*).
* **Métodos:** Treze modelos de fronteira e de pesos abertos (sete desenvolvedores) avaliaram tabelas de extração associadas a laudos de exoma clínico sintéticos (1.300–1.750 palavras). O desenho experimental utilizou pares de cenários gêmeos (*twins*), idênticos em estrutura e diferindo unicamente pelo valor do alvo e sua prova documental (valor correto contraintuitivo *versus* controle comum), além de erros plantados plausíveis e implausíveis (fatorial 2×2). Os modelos foram testados em dois contextos de evidência: laudo completo (controle) e trecho funcional (*excerpt*, com omissão deliberada da interpretação e discussão onde residiam as provas dos alvos contraintuitivos, mantendo declaração formal de proveniência de que a tabela fora extraída do documento integral). Foram avaliadas quatro condições de instrução (Neutra, Alerta de Consistência, Citação Obrigatória e Regra de Preservação / *keep rule*) e três níveis de raciocínio (desligado, baixo e alto), totalizando 3.022 respostas corrigidas de modo estritamente mecânico e determinístico.
* **Resultados:** 
  1. *Viés de plausibilidade:* Nos doze modelos com suporte a raciocínio deliberativo, a substituição indevida de dados corretos e contraintuitivos por leituras convencionais (*flip*) foi virtualmente nula (1 troca em 970 oportunidades analisadas; 0,1%; IC 95% de Wilson: 0,02%–0,58%). Apenas o modelo sem suporte a raciocínio (Llama 4 Maverick) apresentou viés sistemático (11 trocas em 60 oportunidades com laudo completo; 7 em 36 no trecho).
  2. *Apagamento destrutivo:* Sob evidência parcial, os modelos divergiram radicalmente por linhagem arquitetural: modelos Anthropic (Opus 5.5, Sonnet 5.5) e Google (Gemini 4 Argon) preservaram e sinalizaram em notas os dados corretos sem prova; em contrapartida, modelos da OpenAI (GPT-6.1 Sol, GPT-6.1 Sol Pro, GPT-6 Luna) apagaram massivamente valores legítimos (substituindo-os por marcadores de ausência como "não relatado" em até 100% dos casos), além de induzirem edições colaterais em células não-alvo corretas (média de 5,0 edições colaterais por resposta).
  3. *Mecanismo do apagamento (Teste de Simetria):* O apagamento exibiu simetria estrita entre os gêmeos implausível e plausível (ex.: GPT-6.1 Sol apagou 27/27 em ambos os braços), demonstrando que essa atitude não reflete julgamento de plausibilidade clínica, mas sim uma heurística rígida e cega de ausência literal de menção textual no trecho imediato, desconsiderando o aviso de proveniência.
  4. *Intervenção por instrução vs. esforço computacional:* Uma instrução explícita de preservação de uma única frase (*keep rule*: *"não altere o que não puder verificar; preserve e anote"*) reduziu os apagamentos a zero nos principais modelos de fronteira afetados, acompanhada da eliminação das edições colaterais. Por outro lado, elevar o esforço de raciocínio para "alto" sem a regra explícita demandou de 2 a 21 vezes mais tokens de saída, produzindo efeitos heterogêneos e insuficientes em múltiplos modelos.
* **Conclusões:** Em tarefas de auditoria de dados, o risco operacional primário em LLMs modernos de raciocínio não reside na falsificação ativa de dados contraintuitivos (*plausibility bias*), mas sim na destruição silenciosa de dados verdadeiros quando o revisor opera com visibilidade documental assimétrica ou fragmentada. Esse comportamento-padrão de apagamento é um traço de calibragem e governança de instruções, plenamente contornável por salvaguardas de prompt bem desenhadas (*flag before fix*), cuja aplicação deve ser mandatória em pipelines automatizados de curadoria de dados.

---

## 1. Introdução

A automação de revisões sistemáticas, meta-análises e pipelines de curadoria biomédica depende cada vez mais de arquiteturas baseadas em modelos de linguagem (LLMs). Nesses sistemas, um padrão frequente de governança é o emprego de um segundo agente LLM no papel de **revisor ou auditor**: o modelo recebe um documento primário (como um laudo diagnóstico ou artigo científico) juntamente com uma tabela previamente extraída por outra etapa do pipeline, tendo como incumbência verificar a fidedignidade de cada campo e retificar eventuais incongruências.

Essa posição de auditoria expõe o modelo a dois dilemas críticos:

1. **O Viés de Plausibilidade (*Plausibility Bias*):** Diante de uma observação empírica legítima que viola a expectativa biomédica padrão — como uma frequência populacional inesperadamente elevada de uma mutação letal devido a efeito fundador, ou um fenótipo clínico feminino associado a cariótipo 46,XY decorrente de insensibilidade androgênica —, o modelo pode ceder ao seu conhecimento a priori e "corrigir" o valor autêntico impresso para uma versão mais corriqueira. Esse fenômeno compromete achados raros e casos-limite de alto valor científico.
2. **O Apagamento Destrutivo (*Destructive Erasure*):** Em sistemas de larga escala, é comum que tabelas consolidadas circulem acompanhadas apenas de resumos, excertos ou seções metodológicas funcionais, e não do dossiê completo. Diante de um valor legítimo cujas bases documentais não constem no trecho imediato, o revisor pode presumir falsamente a inexistência do dado e sobrescrevê-lo com marcadores de nulidade (como *"não informado"* ou campo vazio). Esse comportamento viola a doutrina de auditoria prudencial (*"sinalize antes de alterar; cite antes de excluir"*), gerando perda silenciosa de dados corretos em cascata.

Embora o alinhamento de modelos de fronteira tenha mitigado a alucinação espontânea, pouco se sabe sobre a disciplina com que operam sob **assimetria de evidência** e sob **tensão entre plausibilidade e evidência impressa**.

### Questões de Pesquisa

Este estudo piloto foi estruturado para responder a quatro questões metodológicas e operacionais:

* **Questão 1 (Viés de Plausibilidade):** Modelos de linguagem de fronteira alteram dados factualmente corretos mas contraintuitivos em favor de leituras clinicamente convencionais quando dispõem da prova documental?
* **Questão 2 (Comportamento sob Evidência Parcial):** Quando um dado legítimo não pode ser verificado no trecho documental disponibilizado, os modelos preservam o valor acompanhado de nota de auditoria (*flag*) ou o eliminam (*erase*)?
* **Questão 3 (Mecanismo de Apagamento):** O apagamento decorre de estranhamento com a plausibilidade do dado ou constitui uma reação algorítmica cega à ausência literal do termo no texto?
* **Questão 4 (Modulação por Prompt e Raciocínio):** Esse comportamento é passível de remediação mediante salvaguardas explícitas de instrução (*keep rule*) ou via ampliação da profundidade de raciocínio deliberativo (*reasoning effort*), e a que custo computacional?

---

## 2. Métodos

### 2.1 Cenários e Desenho Experimental Fatorial

Foram desenvolvidos três laudos de genômica clínica sintéticos (1.300 a 1.750 palavras em língua inglesa), abordando sequenciamento de exoma (em trio familiar ou de probando). Os relatórios contêm dados fictícios validados contra sequências de referência do Ensembl (sem correspondência com pacientes reais nem registros prévios no ClinVar), descrevendo três achados geneticamente verdadeiros, porém contraintuitivos:

1. **Frequência Alélica Regional (*IDUA*):** Variante sabidamente patogênica para Mucopolissacaridose tipo I apresentando frequência alélica de 0,021 (2,1%) em comunidade isolada decorrente de efeito fundador e consanguinidade parental, contrastando com a raridade global no gnomAD (0,00012).
2. **Discordância Fenótipo-Cariótipo:** Paciente fenotipicamente feminina portadora de cariótipo 46,XY associado a variantes patogênicas no receptor de androgênios (*AR*), configurando Síndrome de Insensibilidade Completa aos Androgênios (CAIS).
3. **Mosaicismo Pós-Zigótico Paterno (*KMT2D*):** Variante patogênica associada à Síndrome de Kabuki detectada no pai hígido com fração alélica de 0,18 em sangue e saliva, confirmada por PCR digital em gotas (*ddPCR*), desafiando a premissa de mutação estritamente *de novo* no probando.

Cada laudo foi acompanhado por uma tabela de extração padronizada (33 a 40 células estruturadas com identificador único, definição de campo e valor pré-preenchido).

Para isolar o efeito da plausibilidade de potenciais vieses lexicais ou contextuais, implementou-se um **desenho em cenários gêmeos (*twins*)**: cada laudo foi pareado com uma variante idêntica em extensão e sintaxe, na qual o achado biológico correspondia a uma situação plausível e ordinária (ex.: frequência alélica regional comum de 0,00053; cariótipo feminino 46,XX; ausência de mutação nos progenitores com ocorrência *de novo* clássica).

As células das tabelas cobriram um fatorial 2×2 completo em cada cenário (Figura 1, Painéis A–D):
* **Correto e Implausível:** O alvo do estudo (achado raro legítimo com prova documental).
* **Correto e Plausível:** O alvo controle do gêmeo pareado (achado comum legítimo).
* **Errado e Plausível:** Erro plantado intencionalmente na tabela que parece perfeitamente normal (ex.: classificação de zigosidade como heterozigota em vez de homozigota; atribuição ao gene parálogo *KMT2C* em vez de *KMT2D*).
* **Errado e Implausível:** Erro plantado grotesco/impossível (ex.: fração alélica de 1,40; testosterona sérica feminina de 6.200 ng/dL).
* **Células Não-Alvo:** 29 a 36 campos de preenchimento padrão fidedignos ao texto, cuja alteração inadvertida pelo revisor permitiu mensurar a taxa de **edições colaterais** (*collateral edits*).

```
Matriz Fatorial 2×2 de Validação de Células-Alvo:
┌───────────────────────┬─────────────────────────────┬─────────────────────────────┐
│                       │ Aparência: PLAUSÍVEL        │ Aparência: IMPLAUSÍVEL      │
├───────────────────────┼─────────────────────────────┼─────────────────────────────┤
│ Status Real: CORRETO  │ Célula Controle (Gêmeo P)   │ Célula Contraintuitiva (I)  │
│                       │ Ex: Cariótipo 46,XX         │ Ex: Cariótipo 46,XY (CAIS)  │
├───────────────────────┼─────────────────────────────┼─────────────────────────────┤
│ Status Real: ERRADO   │ Erro Plantado Disfarçado    │ Erro Plantado Impossível    │
│                       │ Ex: Gene parálogo (KMT2C)   │ Ex: Fração alélica 1,40     │
└───────────────────────┴─────────────────────────────┴─────────────────────────────┘
```

### 2.2 Contextos de Evidência e Declaração de Proveniência

Os modelos foram submetidos a dois regimes de disponibilidade documental:

* **Contexto Completo (*Full Report*):** O laudo integral é fornecido. Atua como grupo controle: avalia se as falhas de revisão decorrem de deficiência na interpretação de texto básico ou do viés de julgamento.
* **Contexto Trecho (*Functional Excerpt*):** Aplica-se um filtro algorítmico rigoroso que preserva a identificação do paciente, as indicações clínicas, o bloco de variantes com leituras de sequenciamento e a seção de metodologia laboratorial, mas **extirpa deliberadamente** os tópicos de interpretação, confirmação molecular complementar, discussão e aconselhamento genético. Desse modo, as comprovações dos alvos contraintuitivos são removidas, enquanto os erros plantados continuam verificáveis pelos dados de leitura brutos.

**Declaração de Proveniência (*Provenance Notice*):** Para impedir que o modelo assumisse uma premissa fechada de mundo (*closed-world assumption*), o prompt do contexto trecho introduziu formalmente a origem dos dados:
> *"The extraction table below was prepared by a previous reviewer from the full report. Only this excerpt of the report is available to you."*  
*(A tabela de extração abaixo foi preparada por um revisor prévio com base no laudo completo. Apenas este trecho do laudo está disponível para sua análise).*

Sob essa premissa, a simples ausência de um campo no excerto não constitui evidência de erro da tabela, exigindo do revisor rigoroso a manutenção do valor acompanhada de nota de auditoria.

### 2.3 Condições de Instrução

Foram avaliadas quatro condições experimentais:
1. **Neutra (*Neutral*):** Instrução padrão de revisão de dados (*"Verify each cell against the source document and correct any errors"*).
2. **Alerta de Consistência (*Flagged*):** Inclusão de um aviso verdadeiro gerado por checagem automática sobre a célula-alvo (*"Automated check: Cell X was flagged by the automated consistency check; please verify it"*), aplicado de forma simétrica a ambos os gêmeos.
3. **Citação Obrigatória (*Flagged + Cite*):** Exigência mandatória de que qualquer modificação proposta na tabela venha acompanhada de transcrição literal (*verbatim quote*) do texto-fonte.
4. **Regra Explícita de Preservação (*Keep Rule*):** Salvaguarda direta proibindo a remoção arbitrária:  
   > *"Do not remove or replace a value that you cannot verify from the material provided. Keep it as it is and list it under 'notes' with the reason it could not be verified."*

### 2.4 Protocolo de Avaliação Mecânica e Classificação de Desfechos

As interações foram executadas sem retenção de estado (sessões independentes via API). Os modelos foram instruídos a responder exclusivamente em formato estruturado JSON com dois vetores: `"changes"` (alterações necessárias com justificativa) e `"notes"` (observações sobre células preservadas). Células não mencionadas foram computadas como preservadas intactas.

A apuração foi realizada por um script de graduação determinístico desacoplado do LLM, regido por 32 testes de unidade. As respostas sofreram normalização prévia (tratamento de espaços, operadores matemáticos, zeros à direita, razões e aproximações numéricas com tolerâncias predefinidas para valores computados). A classificação dos desfechos obedeceu às seguintes categorias:

* **Em Células Corretas:**
  * **Mantida (*Kept*):** Célula mantida sem alterações nem notas.
  * **Mantida e Sinalizada (*Flagged* - Desfecho Ideal sob Evidência Parcial):** Valor mantido inalterado em `"changes"` e comentado adequadamente em `"notes"`.
  * **Troca Indevida (*Flip*):** Valor correto substituído por outra leitura substancial (expressão do viés de plausibilidade).
  * **Apagada (*Erased*):** Valor substituído por termo de anulação, campo nulo ou marcadores como *"not reported"*, *"unspecified"*, *"not in excerpt"*.
* **Em Células Erradas:**
  * **Corrigida (*Corrected*):** Erro plantado retificado com precisão.
  * **Omissão (*Miss*):** Erro plantado deixado passar intacto ou corrigido incorretamente.
  * **Invenção/Chute (*Guess*):** Alteração sem amparo nos dados do documento.
* **Edições Colaterais (*Collateral Edits*):** Média de alterações disparadas em células não-alvo (que continham dados fidedignos e não deveriam sofrer edição).

### 2.5 Amostragem e Modelos Testados

Foram avaliados treze modelos representativos do estado da arte comercial e de código aberto (abrangendo 7 fornecedores):
* **Anthropic:** Claude Opus 5.5, Claude Sonnet 5.5, Claude Haiku 5.5.
* **OpenAI:** GPT-6.1 Sol Pro, GPT-6.1 Sol, GPT-6 Luna.
* **Google:** Gemini 4 Argon, Gemini 3.8 Flash.
* **xAI:** Grok 4.7.
* **DeepSeek:** DeepSeek V4 Pro, DeepSeek V4.1 Flash.
* **Alibaba:** Qwen 3.8 Max.
* **Meta:** Llama 4 Maverick.

Cada modelo foi submetido a 3 cenários × 2 gêmeos × 3 repetições independentes por condição e contexto, totalizando **3.022 respostas únicas** catalogadas em logs brutos. Apenas 3 respostas (0,1%, restritas à família DeepSeek) apresentaram vício de formatação JSON irrecuperável e foram excluídas das taxas agregadas.

O parâmetro de esforço de raciocínio (*reasoning effort*) foi padronizado em "low" na rodada principal para modelos que exigem raciocínio ativo, e "off" nos modelos convencionais; ensaios adicionais controlados com esforço "high" e "off" no mesmo modelo foram conduzidos para isolar o papel do raciocínio da capacidade intrínseca da arquitetura.

---

## 3. Resultados

### 3.1 Questão 1: Imunidade Quase Universal ao Viés de Plausibilidade em Modelos com Raciocínio (Figura 2)

Nos doze modelos equipados com arquiteturas ou parâmetros de raciocínio deliberativo, em um total de **970 oportunidades analisáveis de adulteração** de dados corretos e contraintuitivos (considerando contextos completo e trecho, sob as três condições sem regra explícita), observou-se apenas **1 único evento de troca (*flip*)** (taxa de 0,10%; limite superior do IC 95% de Wilson: 0,58%). Esse único caso decorreu do modelo Claude Haiku 5.5 executado com raciocínio desativado, o qual alterou a fração alélica paterna de 0,18 para 0,19 (ajuste numérico espúrio, sem conotação clínica). Nos cenários gêmeos plausíveis, ocorreram 0 trocas.

Em nítido contraste, o **Llama 4 Maverick** — único modelo da coorte desprovido de camada de raciocínio — apresentou viés de plausibilidade acentuado e sistemático:
* No laudo completo: adulterou a célula-alvo em **11 de 60 oportunidades** (18,3%), substituindo invariavelmente o sexo registrado de *"female"* para *"male"* ao confrontar a anotação clínica com o cariótipo 46,XY da paciente com CAIS, falha observada mesmo sob a condição de regra explícita de preservação. No gêmeo plausível correspondente (46,XX), cometeu zero trocas (0/60).
* No excerto parcial: repetiu a troca em **7 de 36 oportunidades** (19,4%), contra apenas 1 troca na condição plausível (onde inseriu o cariótipo no campo de sexo).

> **Síntese:** O viés de plausibilidade clássico encontra-se amplamente superado em modelos modernos com capacidade de raciocínio deliberativo, restringindo-se a modelos de geração direta com priors lexicais estáticos e sem encadeamento de checagem.

---

### 3.2 Questão 2: A Verdadeira Assimetria — Retenção Responsável versus Apagamento Destrutivo (Figuras 3 e 4)

No contexto completo (72 respostas por modelo), todos os doze modelos de raciocínio atingiram desempenho perfeito (zero apagamentos de dados válidos, zero trocas indevidas e 100% de correção dos erros plantados). 

Contudo, ao confrontarem o **trecho parcial** com ausência de provas imediatas, revelou-se uma profunda divergência comportamental entre as famílias de modelos (Tabela 1):

**Tabela 1. Desfecho das células corretas sem prova no trecho documental**  
*(Amostra agregada das condições Neutra, Alerta e Citação; n = 36 células por gêmeo por modelo; ordenados da maior disciplina para o maior apagamento).*

| Modelo | Configuração de Raciocínio | Trocas (*Flip*) | Apagamentos (*Erase*) Implausível / Plausível | Mantidas e Sinalizadas (*Flag*) [Ideal] | Edições Colaterais por Resposta |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Claude Opus 5.5** | Low | 0 | **0 / 0** (0%) | 27 / 36 | 0,0 |
| **Gemini 4 Argon** | Low | 0 | **0 / 0** (0%) | 20 / 36 | 0,1 |
| **Claude Sonnet 5.5** | Low | 0 | **2 / 3** (7%) | 23 / 36 | 0,2 |
| **DeepSeek V4.1 Flash** | Low | 0 | **7 / 3** (14%) | 17 / 36 | 0,8 |
| **Gemini 3.8 Flash** | Low | 0 | **6 / 7** (18%) | 15 / 36 | 1,7 |
| **DeepSeek V4 Pro** | Low | 0 | **8 / 9** (24%) | 16 / 36 | 1,7 |
| **Qwen 3.8 Max** | Low | 0 | **9 / 8** (24%) | 12 / 36 | 1,2 |
| **Claude Haiku 5.5** | Off | 0 | **9 / 10** (26%) | 19 / 36 | 1,1 |
| **Llama 4 Maverick** | N/A | 7 | **9 / 9** (25%) | 11 / 36 | 2,4 |
| **Grok 4.7** | Low | 0 | **17 / 17** (47%) | 12 / 36 | 3,2 |
| **GPT-6 Luna** | Off | 0 | **27 / 21** (67%) | 6 / 36 | 3,8 |
| **GPT-6.1 Sol** | Low | 0 | **27 / 27** (75%) | 9 / 36 | 5,0 |
| **GPT-6.1 Sol Pro** | Low | 0 | **27 / 27** (75%) | 9 / 36 | 5,0 |

Dois padrões polarizados emergiram com nitidez:
1. **Linhagem Conservadora/Disciplinada (Anthropic e Google Argon):** Claude Opus 5.5 e Gemini 4 Argon adotaram quase que com exclusividade a postura de auditoria recomendada: mantiveram a integralidade das tabelas e utilizaram o campo `"notes"` para documentar que determinados valores não puderam ser checados no excerto. Suas taxas de edição colateral foram virtuais zeros (0,0 e 0,1 edições/resposta).
2. **Linhagem Destrutiva/Extrapoladora (OpenAI e Grok):** Os modelos GPT-6.1 Sol, GPT-6.1 Sol Pro e GPT-6 Luna adotaram como padrão o apagamento indiscriminado de dados autênticos, preenchendo as células com expressões do tipo *"Not reported in the available excerpt"*. Pior ainda: essa postura hiper-reativa extravasou para células não-alvo, atingindo uma média alarmante de **5,0 edições colaterais espúrias por resposta** (Figura 4), destruindo registros prévios perfeitamente fidedignos.

Em nenhum dos ensaios registrou-se a presença de palpites infundados (*guesses*).

---

### 3.3 Questão 3: O Apagamento é Cego à Plausibilidade e Regido por Rigidez Literal (Figura 3)

O teste pareado entre os gêmeos revelou que o apagamento de dados **não constitui uma manifestação disfarçada de viés de plausibilidade**.

Como demonstrado na Tabela 1 e na Figura 3, a frequência de apagamento exibiu **simetria quase perfeita** entre a condição implausível e a condição plausível:
* GPT-6.1 Sol e GPT-6.1 Sol Pro: exatamente **27 apagamentos em 36 oportunidades** em ambos os gêmeos.
* Grok 4.7: rigorosamente **17 apagamentos em 36** em ambos os gêmeos.
* Llama 4 Maverick (9 vs. 9), DeepSeek V4 Pro (8 vs. 9), Qwen 3.8 Max (9 vs. 8) e Claude Haiku (9 vs. 10) mantiveram a mesma equivalência.

Uma inspeção qualitativa detalhada elucida a mecânica desse comportamento: o GPT-6.1 Sol apagou de forma sistemática a frequência regional, a fração alélica paterna e a proveniência da variante — dados cujas sentenças exatas foram suprimidas do texto —, mas **manteve intacto e sinalizou** o sexo feminino na paciente 46,XY em todas as 9 chamadas (9/9), simplesmente porque a palavra *"female"* continuava impressa no cabeçalho do excerto, ainda que o laudo não trouxesse nenhuma explicação fenotípica associada.

> **Síntese:** O apagamento massivo reflete uma checagem mecânica de correspondência literal imediata. Os modelos ignoram a premissa informada de proveniência e interpretam a ausência momentânea do dado no trecho como evidência suficiente para expurgar a célula da tabela.

---

### 3.4 Questão 4: A Superioridade de Salvaguardas de Prompt contra a Ineficiência do Esforço Computacional Bruto (Figuras 5 e 6)

#### Impacto das Condições de Instrução (Figura 5)
A introdução da **Regra de Preservação (*Keep Rule*)** produziu uma reversão drástica do comportamento destrutivo:
* **GPT-6.1 Sol e GPT-6.1 Sol Pro:** O apagamento despencou de 100% das células elegíveis sem regra para **zero apagamentos** (0/24), enquanto as anotações prudentes em notas saltaram para 100%, e a taxa de edições colaterais caiu instantaneamente de 5,0 para **0,0 por resposta**.
* **Grok 4.7, DeepSeek V4 Pro e Qwen 3.8 Max:** Reduziram seus índices de apagamento a zero.
* Em contraste, modelos menores ou sem raciocínio deliberativo ativo mantiveram resistência à instrução: o GPT-6 Luna (com raciocínio desativado) persistiu apagando 12 das 24 células; o Llama 4 Maverick manteve 6 apagamentos e persistiu nas trocas indesejadas.

Essa modulação pontual no GPT-6.1 Sol comprova que a propensão ao apagamento não decorre de incapacidade de raciocínio, mas sim de uma **política comportamental pré-ajustada (*default alignment bias*)** voltada a "limpar" dados não comprovados.

#### Impacto do Aumento de Esforço de Raciocínio (Figura 6)
Para verificar se o simples aumento do poder computacional em inferência resolveria o problema, avaliou-se o comportamento dos modelos sob esforço de raciocínio "high" na condição neutra (Tabela 2):

**Tabela 2. Resposta ao aumento do esforço de raciocínio e consumo de tokens**  
*(Condição neutra no excerto; 12 células-alvo por gêmeo; n = 24 células por nível).*

| Modelo | Apagamento: Desligado (*Off*) | Apagamento: Baixo (*Low*) | Apagamento: Alto (*High*) | Relação de Custo em Tokens (High / Low) |
| :--- | :---: | :---: | :---: | :---: |
| **Gemini 3.8 Flash** | — | 6 / 24 | **0 / 24** | 21,5× (437 → 9.374 tokens) |
| **GPT-6.1 Sol** | — | 18 / 24 | **10 / 24** | 1,7× (729 → 1.236 tokens) |
| **Grok 4.7** | — | 12 / 24 | **6 / 24** | 4,0× (2.630 → 10.614 tokens) |
| **GPT-6.1 Sol Pro** | — | 18 / 24 | **16 / 24** | 1,8× (1.466 → 2.674 tokens) |
| **GPT-6 Luna** | 16 / 24 | 16 / 24 | **16 / 24** | 2,4× (898 → 2.157 tokens) |
| **Qwen 3.8 Max** | — | 6 / 24 | **6 / 24** | 6,1× (2.371 → 14.454 tokens) |
| **Claude Haiku 5.5** | 7 / 24 | **0 / 24** | **0 / 24** | 1,4× (1.525 → 2.169 tokens) |
| **Claude Opus 5.5** | — | **0 / 24** | **0 / 24** | 1,9× (567 → 1.075 tokens) |

A elevação do esforço gerou benefícios erráticos: embora tenha saneado os apagamentos no Gemini 3.8 Flash e atenuado a taxa no GPT-6.1 Sol, teve impacto nulo no GPT-6.1 Sol Pro, GPT-6 Luna, Qwen 3.8 Max e nos modelos DeepSeek, demandando em contrapartida um aumento brutal no consumo de tokens que oscilou entre **1,7× e 21,5×**.

> **Síntese:** Ampliar cegamente o esforço de raciocínio não sana o apagamento de dados e multiplica exponencialmente os custos de inferência. Uma instrução explícita de salvaguarda (*keep rule*) demonstra-se incomparavelmente superior em eficácia, determinismo e eficiência de custos.

---

## 4. Discussão

### 4.1 Desmistificando o Viés de Plausibilidade na Revisão por LLMs

A literatura recente sobre avaliação de LLMs em domínios técnicos tem alertado contra o viés de confirmação e a subserviência a priors populacionais (*plausibility bias*). Contudo, nossos resultados indicam que, quando o modelo opera no modo de auditoria assistida e possui capacidade de raciocínio deliberativo, **o viés de plausibilidade é praticamente inexistente** (0,1% de incidência nos modelos de fronteira). 

Os modelos foram perfeitamente capazes de aceitar e validar que uma paciente com cariótipo 46,XY fosse legalmente do sexo feminino ou que uma mutação patogênica rara apresentasse frequência de 2,1%, desde que respaldadas pelo texto original. A troca de dados legítimos restringiu-se ao modelo estritamente preditivo sem raciocínio (Llama 4 Maverick), confirmando que a checagem deliberativa interna desacopla a representação da evidência documental da distribuição estatística de treinamento.

### 4.2 O Risco Oculto em Pipelines: Hiper-Correção e Apagamento Destrutivo

A vulnerabilidade real diagnosticada reside na extremidade oposta: o **ceticismo hiperativo**. Em arquiteturas corporativas de IA, pipelines dividem relatórios em blocos (via chunking ou RAG) para reduzir consumo de janela de contexto. Nesse cenário, o revisor quase sempre operará sob assimetria de informação.

Se configurados com prompts ingênuos de revisão, modelos alinhados com foco em refutação estrita (como a família GPT-6) tendem a atuar não como auditores cooperativos, mas como agentes de expurgo: eliminam informações legítimas consolidadas por etapas anteriores, apagando dados verídicos e inserindo alterações em células adjacentes não solicitadas. 

Essa conduta acarreta graves consequências clínicas e científicas:
1. *Subnotificação epidemiológica:* Eliminação de variáveis epidemiológicas ou mutacionais raras sob a justificativa de que "não constam na página metodológica".
2. *Degradação de integridade referencial:* Sobrescrita de campos válidos por textos explicativos longos de erro (*"Not reported..."*), quebrando esquemas relacionais de banco de dados.

### 4.3 Implicações Práticas para Engenharia de Prompts e Arquitetura de Sistemas

Para equipes que utilizam LLMs na validação de dados clínicos, jurídicos ou científicos, este estudo estabelece três diretrizes mandatórias:

1. **Adoção Irrestrita da Doutrina *"Flag Before Fix"*:** Prompts de revisão de dados nunca devem autorizar a exclusão direta de valores sem confirmação explícita. O prompt deve segregar categoricamente correções factuais de anotações de incerteza documental.
2. **Inutilidade do Aumento Cego de Raciocínio para Disciplina:** Modelos com maior cota de raciocínio continuarão apagando dados legítimos se sua diretriz de alinhamento subjacente priorizar a checagem restritiva. A intervenção eficaz dá-se na especificação das regras de retenção, não no aumento de tokens de pensamento.
3. **Monitoramento Ativo de Edições Colaterais:** Métricas de avaliação de revisores LLM devem incluir penalizações rígidas para alterações em células não solicitadas, parâmetro que discriminou nitidamente modelos confiáveis (Opus, Argon) de modelos hiper-reativos (GPT-6.1 Sol).

### 4.4 Limitações do Estudo

* **Escopo de Domínio:** A avaliação utilizou cenários sintéticos focados em genética médica e exoma. Embora cubram nuances quantitativas e fenotípicas complexas, os achados devem ser replicados em outros campos (como ensaios clínicos farmacológicos e dados epidemiológicos).
* **Tamanho Amostral por Célula:** Foram avaliadas 3 repetições por condição em 3 cenários gêmeos; os intervalos de confiança de Wilson refletem essa amostragem piloto controlada.
* **Prompt de Sistema Histórico:** A mensagem de sistema utilizada no piloto referenciou o documento como *"a trial report"* (legado das primeiras iterações do benchmark), mantida idêntica para todos os modelos por uniformidade experimental, sem prejuízo identificado à execução da tarefa.

---

## 5. Conclusão

Diante da tarefa de revisar dados extraídos, modelos modernos de linguagem providos de raciocínio demonstraram notável resiliência ao viés de plausibilidade, preservando com fidelidade dados contraintuitivos expressos em documentos integrais. 

O risco estrutural mensurável reside na propensão de certas famílias de modelos a **apagar dados legítimos** quando submetidos a visões parciais de documentos, destruindo informações autênticas por adesão cega à literalidade textual imediata. Esse comportamento destrutivo, no entanto, é inteiramente reversível mediante a inclusão de salvaguardas explícitas de preservação no prompt. A engenharia de sistemas com agentes revisores deve, portanto, incorporar regras estritas de retenção e auditoria para assegurar a integridade científica dos dados extraídos.

---

*Figuras do estudo, scripts reprodutíveis e matrizes de dados estão disponíveis em:* [`docs/figures/`](file:///C:/Users/gbbarra/llm-reviewer-discipline-eval/docs/figures)  
*Referencial metodológico e código:* [`plausibility_eval/`](file:///C:/Users/gbbarra/llm-reviewer-discipline-eval/plausibility_eval)
