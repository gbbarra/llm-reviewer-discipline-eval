# Referências do preprint: lista anotada e mapeada por seção

Preprint: *Comportamento de modelos de linguagem ao revisar dados extraídos sob evidência completa e parcial:
viés de plausibilidade e perda de dados por apagamento* (medRxiv, Health Informatics).

- **40 referências**, agrupadas pelos 9 temas pedidos. BibTeX correspondente: `referencias-preprint.bib`
  (mesmas chaves, formato autorAnoPalavra).
- **Verificação (24/10/2026):** cada DOI foi resolvido na API do Crossref, e cada preprint do arXiv na API do
  arXiv. Título, autores, periódico/anais, volume e páginas foram copiados do registro retornado, e não de
  memória. Os itens do PubMed foram conferidos também pelo esummary/efetch do NCBI. Os resumos dos itens menos
  conhecidos foram lidos para confirmar a afirmação atribuída a cada um.
- **Seções:** I = Introdução; M = Métodos; D = Discussão.
- **Preprints sem revisão por pares:** Zhang 2026, Zhou 2023 e Miller 2024 (só arXiv). Sharma 2024 está nos anais
  da ICLR 2024, confirmados em proceedings.iclr.cc, e é citado com o arXiv como URL. Gema 2025 foi publicado na
  TMLR (referência de periódico registrada no arXiv).

---

## 1. LLMs como juízes/avaliadores e seus vieses

**[zheng2023judging]** Zheng L, Chiang W-L, Sheng Y, Zhuang S, Wu Z, Zhuang Y, Lin Z, Li Z, Li D, Xing E, Zhang H,
Gonzalez J, Stoica I. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. *Advances in Neural Information
Processing Systems 36* (NeurIPS 2023), p. 46595–46623. doi:10.52202/075280-2020
- *Por que entra:* é o trabalho de origem do paradigma "LLM-as-a-judge" e descreve os vieses de posição, de
  verbosidade e de autopromoção. Também estabelece que modelos já são usados como avaliadores de saídas de outros
  modelos.
- *Seção:* **I**. Apoia a afirmação de que modelos de linguagem são cada vez mais usados para avaliar ou revisar
  saídas de outra etapa automatizada. **D**. Os vieses conhecidos dos juízes são de forma e de posição; o viés de
  conteúdo contra o impresso (plausibilidade) foi pouco medido.

**[chen2024humans]** Chen GH, Chen S, Liu Z, Jiang F, Wang B. Humans or LLMs as the Judge? A Study on Judgement Bias.
*Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing* (EMNLP 2024), p. 8301–8327.
doi:10.18653/v1/2024.emnlp-main.474
- *Por que entra:* mede, com perturbações controladas, vieses de juízes humanos e de LLMs, entre eles o viés de
  autoridade, o viés de beleza e a tolerância a erro factual. É um precedente de desenho por perturbação que
  isola um único fator.
- *Seção:* **I**. Vieses de juízes vão além da forma e incluem a aceitação de conteúdo errado. **D**. Contraste
  com o nosso achado de 0 trocas por plausibilidade.

**[mccoy2024embers]** McCoy RT, Yao S, Friedman D, Hardy MD, Griffiths TL. Embers of autoregression show how large
language models are shaped by the problem they are trained to solve. *Proceedings of the National Academy of
Sciences* 2024;121(41):e2322420121. doi:10.1073/pnas.2322420121
- *Por que entra:* mostra que o desempenho de LLMs depende da probabilidade da saída e da entrada: saídas de
  baixa probabilidade são produzidas com menos acurácia, mesmo em tarefas determinísticas. É a base teórica para
  esperar um viés de plausibilidade.
- *Seção:* **I**. Motiva a hipótese de que o revisor "corrija" o valor improvável para o provável. **D**.
  Interpretação do episódio único do Haiku, com prior forte e sem pista explicativa.

**[lampinen2024content]** Lampinen AK, Dasgupta I, Chan SCY, Sheahan HR, Creswell A, Kumaran D, McClelland JL,
Hill F. Language models, like humans, show content effects on reasoning tasks. *PNAS Nexus* 2024;3(7):pgae233.
doi:10.1093/pnasnexus/pgae233
- *Por que entra:* documenta o equivalente, em LLMs, do *belief bias* humano: o modelo raciocina melhor quando a
  conclusão é crível e pior quando contraria o conhecimento de mundo. É o conceito mais próximo do nosso viés de
  plausibilidade.
- *Seção:* **I**. Definição e precedente do viés de plausibilidade. **D**. Nossa ausência de trocas sugere que,
  na verificação de valores impressos, esse efeito de conteúdo é suprimido quando há evidência literal.

## 2. Bajulação (sycophancy) e aceitação de premissas falsas

**[perez2023discovering]** Perez E, Ringer S, Lukošiūtė K, et al. (63 autores). Discovering Language Model Behaviors
with Model-Written Evaluations. *Findings of the Association for Computational Linguistics: ACL 2023*,
p. 13387–13434. doi:10.18653/v1/2023.findings-acl.847
- *Por que entra:* é uma das primeiras medições sistemáticas de *sycophancy*, isto é, o modelo repetir a opinião
  declarada pelo usuário, e mostra que o comportamento cresce com escala e com RLHF.
- *Seção:* **I**. Distingue bajulação, que é uma resposta à pressão do interlocutor, de viés de plausibilidade,
  que é uma resposta ao prior do conteúdo. **M**. Justifica que nenhuma condição contenha premissa falsa nem
  opinião do usuário.

**[sharma2024sycophancy]** Sharma M, Tong M, Korbak T, Duvenaud D, Askell A, Bowman SR, et al. Towards Understanding
Sycophancy in Language Models. *The Twelfth International Conference on Learning Representations* (ICLR 2024).
arXiv:2310.13548. https://arxiv.org/abs/2310.13548
- *Por que entra:* mostra bajulação consistente em cinco assistentes comerciais e a atribui em parte a
  julgamentos humanos de preferência. Isso inclui modelos que abandonam uma resposta correta quando o usuário a
  contesta.
- *Seção:* **I**. Delimita o conceito. **M**. O alerta verdadeiro ("a célula X foi marcada") foi desenhado para
  não induzir a troca: aponta a célula sem sugerir valor. **D**. O alerta não produziu trocas.

**[chen2025helpfulness]** Chen S, Gao M, Sasse K, Hartvigsen T, Anthony B, Fan L, Aerts H, Gallifant J,
Bitterman DS. When helpfulness backfires: LLMs and the risk of false medical information due to sycophantic
behavior. *npj Digital Medicine* 2025;8:605. doi:10.1038/s41746-025-02008-z
- *Por que entra:* em medicina, modelos de fronteira atendem a pedidos ilógicos baseados em premissas falsas
  sobre medicamentos, e instruções explícitas para rejeitar o pedido reduzem o problema. É o paralelo clínico de
  "instrução de uma frase corrige o comportamento-padrão".
- *Seção:* **I**. Risco de bajulação em contexto clínico. **D**. Paralelo com a correção do apagamento do
  GPT-6.1 Sol pela regra explícita.

## 3. Fidelidade ao contexto (RAG): abstenção versus fabricação quando a evidência falta

**[rajpurkar2018know]** Rajpurkar P, Jia R, Liang P. Know What You Don't Know: Unanswerable Questions for SQuAD.
*Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)*
2018, p. 784–789. doi:10.18653/v1/P18-2124
- *Por que entra:* é a origem clássica da avaliação de abstenção, com perguntas sem resposta no trecho, em que o
  sistema deve reconhecer que a evidência não está no contexto.
- *Seção:* **I**. Genealogia do problema "o que fazer quando a prova não está no material". **D**. Nosso caso
  inverte o problema: o valor já existe e veio de fonte mais completa, então abster-se de verificar não equivale
  a apagar.

**[wen2025know]** Wen B, Yao J, Feng S, Xu C, Tsvetkov Y, Howe B, Wang LL. Know Your Limits: A Survey of Abstention
in Large Language Models. *Transactions of the Association for Computational Linguistics* 2025;13:529–556.
doi:10.1162/tacl_a_00754
- *Por que entra:* é a revisão de referência sobre abstenção em LLMs, com taxonomia por consulta, modelo e
  valores humanos, e métodos de avaliação.
- *Seção:* **I**. Enquadra "manter e sinalizar" como abstenção de alterar, e "apagar" como uma abstenção mal
  dirigida que destrói o dado. **D**. Propõe distinguir a abstenção sobre a resposta da abstenção sobre a
  alteração.

**[kalai2026evaluating]** Kalai AT, Nachum O, Vempala SS, Zhang E. Evaluating large language models for accuracy
incentivizes hallucinations. *Nature* 2026;653(8116):1047–1051. doi:10.1038/s41586-026-10549-w
- *Por que entra:* mostra que métricas baseadas apenas em acurácia recompensam o chute em vez da admissão de
  incerteza, e propõe ajustar os incentivos da avaliação.
- *Seção:* **I**. Explica por que se espera fabricação ("guess") quando a evidência falta. **D**. Em nosso
  estudo não houve nenhum chute; a falha observada foi a oposta, apagar. Isso reforça que a métrica precisa
  separar manter, sinalizar, apagar e chutar.

**[xu2024knowledge]** Xu R, Qi Z, Guo Z, Wang C, Wang H, Zhang Y, Xu W. Knowledge Conflicts for LLMs: A Survey.
*Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing* (EMNLP 2024), p. 8541–8565.
doi:10.18653/v1/2024.emnlp-main.486
- *Por que entra:* revisa os conflitos entre o conhecimento paramétrico e o contexto, e entre contextos
  diferentes. O valor correto e implausível é exatamente um conflito entre contexto e memória.
- *Seção:* **I**. Formaliza a tensão entre o prior e o impresso. **D**. Com o contexto completo, todos os
  modelos ficaram com o contexto.

**[zhang2026rethinking]** Zhang Z, Peng X, Sun J, Yao R, Jiang B, Han B. Rethinking Faithfulness in LLMs: A Pairwise
Context-Sensitive Perspective. arXiv:2610.07894 (preprint, 2026). https://arxiv.org/abs/2610.07894
- *Por que entra:* avalia em pares a mesma pergunta com contexto que a sustenta e com contexto que não a
  sustenta, em 39 modelos de 7 famílias. Encontra viés para responder, ou seja, fabricar com contexto
  insuficiente. É um desenho pareado análogo aos nossos gêmeos e um achado de direção contrária ao apagamento.
- *Seção:* **I**/**D**. A literatura de fidelidade descreve sobretudo o excesso de resposta; nós documentamos o
  excesso de remoção. **M**. Precedente para a avaliação pareada por contexto. *(Preprint sem revisão por
  pares.)*

## 4. Extração de dados por LLM (revisões sistemáticas e documentos clínicos)

**[mathes2017frequency]** Mathes T, Klaßen P, Pieper D. Frequency of data extraction errors and methods to increase
data extraction quality: a methodological review. *BMC Medical Research Methodology* 2017;17(1):152.
doi:10.1186/s12874-017-0431-4
- *Por que entra:* quantifica a frequência de erros de extração humana em revisões sistemáticas e os métodos
  para reduzi-los, como a dupla extração. É a linha de base humana.
- *Seção:* **I**. A extração humana já erra, e por isso se usa uma segunda etapa de revisão. **D**. O revisor
  automatizado precisa ser comparado a essa linha de base, e não à perfeição.

**[buscemi2006single]** Buscemi N, Hartling L, Vandermeer B, Tjosvold L, Klassen TP. Single data extraction
generated more errors than double data extraction in systematic reviews. *Journal of Clinical Epidemiology*
2006;59(7):697–703. doi:10.1016/j.jclinepi.2005.11.010
- *Por que entra:* é o estudo clássico que mostra que a extração única gera mais erros que a dupla. É a
  justificativa histórica do papel de "revisor" que o LLM agora ocupa.
- *Seção:* **I**. Origem do desenho extrator mais revisor que o nosso estudo reproduz.

**[gartlehner2024data]** Gartlehner G, Kahwati L, Hilscher R, Thomas I, Kugley S, Crotty K, Viswanathan M,
Nussbaumer-Streit B, Booth G, Erskine N, Konet A, Chew R. Data extraction for evidence synthesis using a large
language model: A proof-of-concept study. *Research Synthesis Methods* 2024;15(4):576–589. doi:10.1002/jrsm.1710
- *Por que entra:* é a prova de conceito de extração por LLM para síntese de evidência, com análise dos tipos de
  erro.
- *Seção:* **I**. LLMs já são usados como extratores em revisões sistemáticas.

**[gartlehner2025artificial]** Gartlehner G, Kugley S, Crotty K, Viswanathan M, Dobrescu A, Nussbaumer-Streit B,
et al. Artificial Intelligence–Assisted Data Extraction With a Large Language Model: A Study Within Reviews.
*Annals of Internal Medicine* 2025;178(12):1763–1771. doi:10.7326/ANNALS-25-00739
- *Por que entra:* é um estudo prospectivo em 6 revisões reais (9.341 elementos). A extração por LLM verificada
  por humano teve acurácia de 91,0%, contra 89,0% da extração só humana, e o dado omitido foi o erro mais
  frequente nos dois braços.
- *Seção:* **I**. O fluxo "LLM extrai, alguém revisa" já está em uso. **D**. A omissão já é o erro dominante na
  extração; um revisor que apaga o que não verifica soma omissões ao fluxo.

**[huang2024critical]** Huang J, Yang DM, Rong R, Nezafati K, Treager C, Chi Z, et al. A critical assessment of
using ChatGPT for extracting structured data from clinical notes. *npj Digital Medicine* 2024;7:106.
doi:10.1038/s41746-024-01079-8
- *Por que entra:* avalia a extração estruturada de laudos e notas clínicas reais (anatomia patológica) por LLM
  e discute erros e reprodutibilidade.
- *Seção:* **I**. A extração de documentos clínicos por LLM, e não apenas de artigos, é o cenário dos nossos
  laudos.

## 5. LLMs em genômica clínica e interpretação de variantes

**[richards2015standards]** Richards S, Aziz N, Bale S, Bick D, Das S, Gastier-Foster J, Grody WW, Hegde M, Lyon E,
Spector E, Voelkerding K, Rehm HL. Standards and guidelines for the interpretation of sequence variants: a joint
consensus recommendation of the American College of Medical Genetics and Genomics and the Association for
Molecular Pathology. *Genetics in Medicine* 2015;17(5):405–424. doi:10.1038/gim.2015.30
- *Por que entra:* é o padrão ACMG/AMP de classificação de variantes que estrutura os laudos e as tabelas,
  incluindo a definição do critério BS1 (frequência maior que a esperada para o distúrbio).
- *Seção:* **I**. Contexto da genômica clínica. **M**. Campos de classificação das tabelas; cenário do efeito
  fundador (ver também tema 9).

**[dendunnen2016hgvs]** den Dunnen JT, Dalgleish R, Maglott DR, Hart RK, Greenblatt MS, McGowan-Jordan J, Roux A-F,
Smith T, Antonarakis SE, Taschner PEM. HGVS Recommendations for the Description of Sequence Variants: 2016 Update.
*Human Mutation* 2016;37(6):564–569. doi:10.1002/humu.22981
- *Por que entra:* é a norma de nomenclatura HGVS usada nas variantes fictícias, que foram conferidas contra o
  Ensembl.
- *Seção:* **M**. Construção das variantes e normalização da correção.

**[duong2024analysis]** Duong D, Solomon BD. Analysis of large-language model versus human performance for genetics
questions. *European Journal of Human Genetics* 2024;32(4):466–468. doi:10.1038/s41431-023-01396-8
- *Por que entra:* compara o ChatGPT com humanos em perguntas de genética. O desempenho é semelhante ao humano
  em perguntas de memorização e pior nas que exigem raciocínio crítico, e o modelo dá explicações plausíveis
  tanto para respostas certas quanto erradas.
- *Seção:* **I**. LLMs em genética clínica e o risco de respostas plausíveis, porém erradas.

**[lu2025boosting]** Lu S, Cosgun E. Boosting GPT models for genomics analysis: generating trusted genetic variant
annotations and interpretations through RAG and Fine-tuning. *Bioinformatics Advances* 2025;5(1):vbaf019.
doi:10.1093/bioadv/vbaf019
- *Por que entra:* integra 190 milhões de anotações de variantes a um GPT por RAG e mostra que o RAG supera o
  ajuste fino na injeção de conhecimento factual. Ilustra pipelines de genômica que dependem de trechos
  recuperados.
- *Seção:* **I**/**D**. Pipelines de genômica com recuperação de trechos podem reproduzir a janela estreita de
  evidência em que observamos os dois comportamentos.

**[li2025autopm3]** Li S, Wang Y, Liu C-M, Huang Y, Lam T-W, Luo R. AutoPM3: enhancing variant interpretation via
LLM-driven PM3 evidence extraction from scientific literature. *Bioinformatics* 2025;41(7):btaf382.
doi:10.1093/bioinformatics/btaf382
- *Por que entra:* extrai por LLM com RAG a evidência ACMG/AMP PM3 da literatura, com 86,1% de acurácia nos
  acertos de variante. É um exemplo concreto de curadoria de variantes automatizada por extração.
- *Seção:* **I**. LLMs já extraem evidência para classificação de variantes, o que torna relevante o papel de
  revisor dessas extrações.

## 6. Segurança do dado e automation bias

**[goddard2012automation]** Goddard K, Roudsari A, Wyatt JC. Automation bias: a systematic review of frequency,
effect mediators, and mitigators. *Journal of the American Medical Informatics Association* 2012;19(1):121–127.
doi:10.1136/amiajnl-2011-000089
- *Por que entra:* é a revisão sistemática de referência sobre *automation bias* em sistemas de apoio à decisão
  clínica: o usuário aceita a saída automatizada mesmo quando ela está errada.
- *Seção:* **I**/**D**. Um campo apagado como "not reported" por um revisor automatizado tende a ser aceito a
  jusante. A perda de dado propaga-se porque o humano confia na revisão.

**[parasuraman2010complacency]** Parasuraman R, Manzey DH. Complacency and Bias in Human Use of Automation: An
Attentional Integration. *Human Factors* 2010;52(3):381–410. doi:10.1177/0018720810376055
- *Por que entra:* é a integração teórica clássica de complacência e viés de automação, com erros de omissão e
  de comissão.
- *Seção:* **D**. O apagamento é um erro do sistema que induz um erro de omissão no humano que confia nele.

**[dratsch2023automation]** Dratsch T, Chen X, Rezazade Mehrizi M, Kloeckner R, Mähringer-Kunz A, Püsken M,
Baeßler B, Sauer S, Maintz D, Pinto dos Santos D. Automation Bias in Mammography: The Impact of Artificial
Intelligence BI-RADS Suggestions on Reader Performance. *Radiology* 2023;307(4):e222176.
doi:10.1148/radiol.222176
- *Por que entra:* é uma demonstração experimental recente de que sugestões erradas de IA degradam o desempenho
  de leitores humanos, inclusive dos experientes.
- *Seção:* **D**. Evidência atual de que erros da IA contaminam a decisão humana em diagnóstico.

## 7. Efeito de instruções explícitas e de esforço de raciocínio

**[wei2022chain]** Wei J, Wang X, Schuurmans D, Bosma M, Ichter B, Xia F, Chi E, Le QV, Zhou D. Chain-of-Thought
Prompting Elicits Reasoning in Large Language Models. *Advances in Neural Information Processing Systems 35*
(NeurIPS 2022), p. 24824–24837. doi:10.52202/068431-1800
- *Por que entra:* é a origem da cadeia de pensamento como meio de melhorar o raciocínio e o antecedente
  conceitual do "reasoning effort" configurável.
- *Seção:* **I**/**M**. Justifica testar o esforço "high" contra o "low".

**[zhou2023instruction]** Zhou J, Lu T, Mishra S, Brahma S, Basu S, Luan Y, Zhou D, Hou L. Instruction-Following
Evaluation for Large Language Models. arXiv:2311.07911 (preprint, 2023). https://arxiv.org/abs/2311.07911
- *Por que entra:* avalia a obediência a instruções verificáveis (IFEval) e mostra que modelos diferem na adesão
  a regras explícitas.
- *Seção:* **D**. A regra de uma frase foi obedecida pelo GPT-6.1 Sol e não pelo GPT-6 Luna: a adesão a
  instruções varia entre modelos da mesma família. *(Preprint.)*

**[turpin2023language]** Turpin M, Michael J, Perez E, Bowman SR. Language Models Don't Always Say What They Think:
Unfaithful Explanations in Chain-of-Thought Prompting. *Advances in Neural Information Processing Systems 36*
(NeurIPS 2023), p. 74952–74965. doi:10.52202/075280-3275
- *Por que entra:* mostra que as explicações em cadeia de pensamento podem não refletir a causa real da
  resposta.
- *Seção:* **M**. Justifica a correção mecânica pelo valor da célula: o texto livre ("reason") nunca altera a
  classificação. **D**. A justificativa do Haiku ("a fonte diz female") contradiz a ação de trocar o valor.

**[gema2025inverse]** Gema AP, Hägele A, Chen R, Arditi A, Goldman-Wetzler J, Fraser-Taliente K, Sleight H,
Petrini L, Michael J, Alex B, Minervini P, Chen Y, Benton J, Perez E. Inverse Scaling in Test-Time Compute.
*Transactions on Machine Learning Research* 2025. arXiv:2507.14417. https://openreview.net/forum?id=NXgyHW1c7M
- *Por que entra:* mostra que mais raciocínio no momento da inferência pode piorar o desempenho em algumas
  tarefas, ou seja, que o efeito do "reasoning effort" não é monotônico.
- *Seção:* **D**. O esforço "high" reduziu sem eliminar o apagamento no GPT-6.1 Sol: mais raciocínio não
  substitui a instrução.

## 8. Metodologia

**[wilson1927probable]** Wilson EB. Probable Inference, the Law of Succession, and Statistical Inference. *Journal of
the American Statistical Association* 1927;22(158):209–212. doi:10.1080/01621459.1927.10502953
- *Por que entra:* é a origem do intervalo de Wilson usado nos limites superiores (0/777, limite de 0,5%).
- *Seção:* **M** (análise estatística).

**[brown2001interval]** Brown LD, Cai TT, DasGupta A. Interval Estimation for a Binomial Proportion. *Statistical
Science* 2001;16(2):101–133. doi:10.1214/ss/1009213286
- *Por que entra:* mostra o mau desempenho do intervalo de Wald e recomenda o de Wilson, sobretudo com
  proporções próximas de 0.
- *Seção:* **M**. Justifica a escolha do Wilson para contagens de zero.

**[hanley1983nothing]** Hanley JA, Lippman-Hand A. If Nothing Goes Wrong, Is Everything All Right? Interpreting Zero
Numerators. *JAMA* 1983;249(13):1743–1745. doi:10.1001/jama.1983.03330370053031
- *Por que entra:* é a "regra de três" para interpretar numeradores zero: 0 eventos não significa risco zero.
- *Seção:* **D**. Leitura correta de "0 trocas em 459" como limite superior, e não como ausência do fenômeno.

**[gardner2020contrast]** Gardner M, Artzi Y, Basmov V, Berant J, Bogin B, Chen S, et al. Evaluating Models' Local
Decision Boundaries via Contrast Sets. *Findings of the Association for Computational Linguistics: EMNLP 2020*,
p. 1307–1323. doi:10.18653/v1/2020.findings-emnlp.117
- *Por que entra:* é a origem dos *contrast sets*: pares de exemplos minimamente alterados que isolam o efeito
  de um único fator. É o fundamento dos nossos gêmeos, idênticos exceto no valor contraintuitivo e nas suas
  provas.
- *Seção:* **M**. Desenho por cenários gêmeos.

**[nosek2018preregistration]** Nosek BA, Ebersole CR, DeHaven AC, Mellor DT. The preregistration revolution.
*Proceedings of the National Academy of Sciences* 2018;115(11):2600–2606. doi:10.1073/pnas.1708274114
- *Por que entra:* é a referência geral sobre pré-registro e a distinção entre análise confirmatória e
  exploratória.
- *Seção:* **M**/**D** (limitações). O estudo é exploratório, e as duas correções de análise foram registradas;
  a etapa confirmatória deve ser pré-registrada.

**[vanmiltenburg2021preregistering]** van Miltenburg E, van der Lee C, Krahmer E. Preregistering NLP research.
*Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational
Linguistics: Human Language Technologies* (NAACL 2021), p. 613–623. doi:10.18653/v1/2021.naacl-main.51
- *Por que entra:* adapta o pré-registro à pesquisa em PLN e avaliação de modelos.
- *Seção:* **D** (limitações e próximos passos). Pré-registrar a replicação em avaliações de LLM.

**[miller2024adding]** Miller E. Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations.
arXiv:2411.00640 (preprint, 2024). https://arxiv.org/abs/2411.00640
- *Por que entra:* argumenta que avaliações de LLM devem reportar incerteza, levando em conta repetições e
  agrupamento por item.
- *Seção:* **M**. Repetições por célula (3) e conversas independentes. **D** (limitações). As respostas estão
  agrupadas por laudo e gêmeo, e os intervalos por resposta são aproximados. *(Preprint.)*

## 9. Contexto clínico dos cenários

**[ghosh2018updated]** Ghosh R, Harrison SM, Rehm HL, Plon SE, Biesecker LG; ClinGen Sequence Variant Interpretation
Working Group. Updated recommendation for the benign stand-alone ACMG/AMP criterion. *Human Mutation*
2018;39(11):1525–1530. doi:10.1002/humu.23642
- *Por que entra:* atualiza os critérios de frequência do ACMG/AMP (BA1) e lista exceções de variantes
  patogênicas com frequência alta em populações específicas. É a base do cenário IDUA, em que 2,1% é correto.
  Combina com Richards 2015 (BS1).
- *Seção:* **M**. Desenho do cenário do efeito fundador: frequência alta não implica variante benigna.

**[arcosburgos2002genetics]** Arcos-Burgos M, Muenke M. Genetics of population isolates. *Clinical Genetics*
2002;61(4):233–247. doi:10.1034/j.1399-0004.2002.610401.x
- *Por que entra:* é uma revisão sobre isolados populacionais, efeito fundador e aumento da frequência de alelos
  de doenças recessivas.
- *Seção:* **M**. Plausibilidade clínica de uma variante patogênica em IDUA com 2,1% numa comunidade isolada.

**[hughes2012androgen]** Hughes IA, Davies JD, Bunch TI, Pasterski V, Mastroyannopoulou K, MacDougall J. Androgen
insensitivity syndrome. *The Lancet* 2012;380(9851):1419–1428. doi:10.1016/S0140-6736(12)60071-3
- *Por que entra:* é uma revisão da síndrome de insensibilidade androgênica: na forma completa há cariótipo
  46,XY com fenótipo feminino e testosterona normal ou alta.
- *Seção:* **M**. Cenário da adolescente 46,XY registrada como do sexo feminino. **D**. Episódio do Haiku.

**[campbell2014parental]** Campbell IM, Yuan B, Robberecht C, Pfundt R, Szafranski P, McEntagart ME, et al. Parental
Somatic Mosaicism Is Underrecognized and Influences Recurrence Risk of Genomic Disorders. *The American Journal of
Human Genetics* 2014;95(2):173–182. doi:10.1016/j.ajhg.2014.07.003
- *Por que entra:* mostra que o mosaicismo parental assintomático é subdiagnosticado e altera o risco de
  recorrência. É a base do cenário KMT2D, com pai assintomático e fração alélica de 0,18.
- *Seção:* **M**. Cenário do mosaicismo parental.

---

## Mapa rápido por seção

| Seção | Chaves |
|---|---|
| Introdução | zheng2023judging, chen2024humans, mccoy2024embers, lampinen2024content, perez2023discovering, sharma2024sycophancy, chen2025helpfulness, rajpurkar2018know, wen2025know, kalai2026evaluating, xu2024knowledge, zhang2026rethinking, mathes2017frequency, buscemi2006single, gartlehner2024data, gartlehner2025artificial, huang2024critical, richards2015standards, duong2024analysis, lu2025boosting, li2025autopm3, goddard2012automation, wei2022chain |
| Métodos | perez2023discovering, sharma2024sycophancy, zhang2026rethinking, richards2015standards, dendunnen2016hgvs, wei2022chain, turpin2023language, wilson1927probable, brown2001interval, gardner2020contrast, nosek2018preregistration, miller2024adding, ghosh2018updated, arcosburgos2002genetics, hughes2012androgen, campbell2014parental |
| Discussão | zheng2023judging, chen2024humans, mccoy2024embers, lampinen2024content, sharma2024sycophancy, chen2025helpfulness, rajpurkar2018know, wen2025know, kalai2026evaluating, xu2024knowledge, zhang2026rethinking, mathes2017frequency, gartlehner2025artificial, lu2025boosting, goddard2012automation, parasuraman2010complacency, dratsch2023automation, zhou2023instruction, turpin2023language, gema2025inverse, hanley1983nothing, nosek2018preregistration, vanmiltenburg2021preregistering, miller2024adding, hughes2012androgen |

## Lacunas

1. **Erros de nomenclatura HGVS cometidos por LLMs.** Nenhum estudo verificável avalia especificamente LLMs na
   geração ou validação de nomenclatura HGVS. A busca no PubMed por LLM + HGVS/nomenclatura não retornou estudo
   pertinente, e a busca na web encontrou apenas trabalhos com ferramentas não-LLM (Mutalyzer; discordância
   entre ANNOVAR, SnpEff e VEP). Usar den Dunnen 2016 apenas como a norma.
2. **Submissão a ClinVar assistida por LLM.** Não encontrei estudo revisado por pares sobre LLMs na preparação ou
   submissão de registros ao ClinVar. Se o texto mencionar o ClinVar (por exemplo, "variantes sem registro no
   ClinVar" nos Métodos), a referência natural é o artigo do banco: Landrum MJ et al., *Nucleic Acids Research*
   2018, doi:10.1093/nar/gkx1153. O DOI foi resolvido no Crossref, mas o artigo ficou fora da lista para
   respeitar o limite de 40.
3. **Classificação ACMG completa assistida por LLM, revisada por pares e com modelos de fronteira.** Os trabalhos
   encontrados tratam de critérios isolados (AutoPM3: PM3), de anotação (Lu 2025) ou de domínios específicos
   (oncologia somática, perda auditiva). Não encontrei avaliação de referência de classificação germinativa
   completa por LLMs comerciais atuais.
4. **LLM como revisor (segunda etapa) de dados já extraídos.** Toda a literatura de extração avalia o LLM como
   extrator, ou o humano revisando o LLM (Gartlehner 2025). Não encontrei estudo que avalie o LLM revisando uma
   extração prévia e diferencie manter, sinalizar e apagar. Isso sustenta a originalidade do estudo, mas deve
   ser escrito como "não identificamos", e não como "não existe".
5. **"Apagamento" como modo de falha distinto da alucinação.** A literatura de fidelidade e abstenção descreve
   o excesso de resposta (Zhang 2026; Kalai 2026) ou a recusa de responder (Wen 2025). Não encontrei referência
   que nomeie e meça a remoção de um dado correto preexistente por incapacidade de verificá-lo.
6. **Segurança do dado em pipelines automatizados, em sentido estrito** (integridade e linhagem do dado em
   pipelines de ML ou de laboratório). Cobri apenas o lado humano (*automation bias*). Não incluí referência
   técnica de validação ou linhagem de dados em pipelines por não ter achado uma específica de genômica clínica
   com LLM. Se o texto precisar, vale uma busca dedicada.
7. **Efeito fundador de IDUA especificamente.** Usei revisões gerais (Arcos-Burgos 2002; Ghosh 2018). Não
   procurei uma referência de frequência de IDUA em população isolada, porque a variante do cenário é fictícia.

## Possíveis acréscimos (verificados, fora dos 40)

Se o limite permitir, todos estes tiveram o DOI ou o arXiv conferido:
- Wang P et al. *Large Language Models are not Fair Evaluators*. ACL 2024, doi:10.18653/v1/2024.acl-long.511
  (viés de posição).
- Panickssery A, Bowman SR, Feng S. *LLM Evaluators Recognize and Favor Their Own Generations*. arXiv:2404.13076
  (autopreferência).
- Lin S, Hilton J, Evans O. *TruthfulQA*. ACL 2022, doi:10.18653/v1/2022.acl-long.229.
- Longpre S et al. *Entity-Based Knowledge Conflicts in Question Answering*. EMNLP 2021,
  doi:10.18653/v1/2021.emnlp-main.565.
- Liu NF et al. *Lost in the Middle*. TACL 2024, doi:10.1162/tacl_a_00638.
- Khraisha Q et al. *Can large language models replace humans in systematic reviews?* Res Synth Methods 2024,
  doi:10.1002/jrsm.1715.
- Adam MP et al. *Kabuki syndrome: international consensus diagnostic criteria*. J Med Genet 2019,
  doi:10.1136/jmedgenet-2018-105625.
- Whiffin N et al. *Using high-resolution variant frequencies to empower clinical genome interpretation*.
  Genet Med 2017, doi:10.1038/gim.2017.26 (limiar de frequência máxima crível, base quantitativa do BS1).
