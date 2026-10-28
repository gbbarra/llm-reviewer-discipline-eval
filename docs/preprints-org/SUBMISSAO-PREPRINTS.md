# Submissão ao Preprints.org: o que vai em cada campo

Manuscrito: `PREPRINTS-manuscript.en.docx` (Word, 17 páginas, figuras embutidas), gerado por
`build_preprints_org.py` a partir de `../PREPRINT-medRxiv-2026-10-24.en.md`, com as correções de 28/10/2026 e as
declarações reescritas (Base by Base responsável pela pesquisa; CNPJ só nas declarações).

## Regras do Preprints.org que importam

- **Arquivo em Word ou LaTeX** (não PDF). A primeira página tem título, autor, afiliação, contato do autor
  correspondente, resumo e palavras-chave, como pedem as instruções.
- **Licença CC BY 4.0 obrigatória** para todos os preprints; o autor mantém o copyright. Coerente com o
  repositório público, que já está em CC BY 4.0.
- **Dados disponíveis** em repositório reconhecido: o GitHub do estudo atende.
- **Uso de IA documentado em Métodos** (política COPE adotada pelo Preprints.org): o manuscrito tem a subseção
  "Use of AI-assisted tools" em Methods, além da declaração no final. Ferramentas de IA não podem ser autoras.
- **Resumo gráfico** em JPG ou PNG; um print do resumo em texto não vale.
- A triagem verifica conteúdo científico básico, **formação do autor** e conformidade ética; costuma levar menos
  de um dia útil.
- Regras conferidas em https://www.preprints.org/instructions-for-authors (via busca, 28/10/2026). O limite de
  palavras do resumo e a lista de áreas não aparecem nas instruções: confira no formulário.

## Antes de começar (só você pode fazer)

- **Conta no Preprints.org** (gratuita, login MDPI/SciProfiles), ligada ao ORCID 0000-0002-2136-3471.
- **Cureus:** confirmar a retirada do artigo 548568.
- **Não postar também no TechRxiv**: um só servidor, para não ter dois DOIs do mesmo trabalho.

## Campos do formulário

| Campo | Conteúdo |
|---|---|
| Tipo | Article |
| Arquivo | `PREPRINTS-manuscript.en.docx` |
| Resumo gráfico (recomendado, JPG/PNG) | `docs/figures/fig3-partial-evidence-outcomes.png` (o resultado central) |
| Título | Discipline of language models reviewing data extracted from genomic reports under full and partial evidence: plausibility bias, erasure, and the effect of a keep rule |
| Autor | Gustavo Barcelos Barra; gustavo@basebybase.com; ORCID 0000-0002-2136-3471 |
| Afiliação | Base by Base, Brasília, DF, Brazil |
| Área (subject) | Uma área de ciências da vida ou medicina, para o preprint chegar às buscas biomédicas (Europe PMC): por exemplo **Medicine and Pharmacology** ou **Biology and Life Sciences**, na subárea mais próxima de informática em saúde, bioinformática ou genética. Se só houver opção de computação que sirva, **Computer Science and Mathematics → Artificial Intelligence and Machine Learning**. Confira os nomes exatos no formulário. |
| Palavras-chave | large language models; data extraction; automated review; clinical genomics; plausibility bias; context faithfulness; prompt engineering; data safety |
| Financiamento | Self-funded by Base by Base; no external funding. |
| Conflito de interesses | texto abaixo |
| Dados | https://github.com/gbbarra/llm-reviewer-discipline-eval |
| Publicado antes? | Não. Sem DOI; não publicado em revista. |
| Licença | CC BY 4.0 (automática) |

### Resumo (colar como texto; 364 palavras)

Background. Large language models (LLMs) are used as reviewers of tables extracted by an earlier step of a pipeline. In this role, the model must keep correct values even when they look wrong, correct errors, and, when it cannot verify a value, flag it instead of erasing it. We found no studies that measure these three behaviours separately.

Methods. Thirteen models from seven developers reviewed tables of 33 to 40 cells extracted from three synthetic clinical exome reports. Each report has an identical twin in which the correct target value is counterintuitive (implausible twin) or common (plausible twin), plus planted plausible and implausible errors. The models received the full report or an excerpt without the sections that prove the counterintuitive values, with a statement that the table had been prepared from the full report. Four instructions (neutral, true alert, mandatory citation, keep rule) and three levels of reasoning effort were compared. A mechanical grader classified each cell as kept, kept and flagged, erased, flipped, corrected, or not corrected. A total of 3,019 responses were analysed.

Results. In the 12 models with a reasoning parameter, correct counterintuitive values were flipped in 1 of 970 cells (0.1%; 95% CI 0.02% to 0.58%). Llama 4 Maverick, without reasoning, flipped 8 of 45 in the full report and 7 of 36 in the excerpt, always "female" to "male" in a 46,XY patient with androgen insensitivity. Without the proof in the excerpt, the models diverged: Claude Opus 5.5 and Gemini 4 Argon kept almost everything and flagged it; GPT-6.1 Sol and Sol Pro erased 27 of 36 cells in each twin and changed on average 5.0 non-target cells per response. Erasure was equal in the two twins, which indicates a reaction to the literal absence of the text, not to plausibility. A keep sentence brought erasure to zero in 10 of the 13 models; raising reasoning effort cost 1.1 to 21.5 times more tokens and reduced erasure in only three models.

Conclusions. In models with reasoning, the risk is not the flipping of atypical values but the erasure of correct values under partial evidence. This behaviour is a default of some models and disappears with an explicit keep instruction.

### Conflito de interesses (colar)

G.B.B. is employed by Laboratório Sabin (Brasília, Brazil); this work was carried out independently of that employment. The author declares no other competing interests.

### Responsabilidade pela pesquisa (se houver campo de declarações adicionais)

This study was conducted and funded by Base by Base (CNPJ 69.561.948/0001-12), Brasília, DF, Brazil, which is responsible for the research and for any correspondence on research integrity (contact: gustavo@basebybase.com).

### Uso de IA (se o formulário pedir; também está no manuscrito)

Claude (Anthropic) assisted in writing the code, generating the figures, and drafting and revising the text; Gemini 3.8 Flash (Google) reviewed style and structure. The models used as assistants include versions of the evaluated families. The author verified every number against the data and takes full responsibility for the content. The runs were executed and graded by deterministic code; no language model classified outcomes.

## Depois da submissão

- Guardar o e-mail de confirmação e, quando o preprint sair, o DOI do Preprints.org.
- Com o DOI: atualizar o README e o `CITATION.cff` deste repositório e o `manifest.yaml` do pacote
  agentic-article.
