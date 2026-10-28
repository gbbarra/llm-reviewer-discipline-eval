# Submissão ao TechRxiv: o que vai em cada campo

Manuscrito: `TECHRXIV-manuscript.en.pdf` (16 páginas, 1,4 MB; limite do TechRxiv: 10 MB por arquivo), gerado por
`build_techrxiv.py` a partir de `../PREPRINT-medRxiv-2026-10-24.en.md`, já com as correções de 28/10/2026
(IC 86,2%; exceção do Gemini 3.8 Flash na citação obrigatória).

## Regras do TechRxiv que importam para este artigo

- **Escopo:** engenharia, ciência da computação e tecnologias relacionadas. O artigo entra como **avaliação de
  modelos de linguagem** (computação), com laudos genômicos sintéticos como domínio de aplicação. Não há dado de
  paciente nem recomendação clínica.
- **Só inglês**, qualquer formato de arquivo (vamos de PDF), até 10 MB por arquivo.
- **Recusa** conteúdo que já tenha DOI, conjunto de dados ou código isolados, e afiliação apresentada de forma
  enganosa. O manuscrito não tem DOI; a afiliação é a Base by Base, MEI com CNPJ, declarada como responsável pela pesquisa.
- Triagem por moderadores do IEEE, normalmente em até 4 dias úteis. Recurso: appeal@TechRxiv.org.
- Não consegui abrir a página de diretrizes do TechRxiv a partir da sessão (domínio bloqueado na rede); confira
  no formulário a lista de categorias e as opções de licença, que podem ter mudado.

## Antes de começar (só você pode fazer)

- **Conta IEEE** (gratuita) para entrar no TechRxiv, ligada ao ORCID 0000-0002-2136-3471.
- **Cureus:** confirmar a retirada do artigo 548568 (não é exigência do TechRxiv, mas evita duas submissões
  abertas do mesmo texto).
- **Licença:** o TechRxiv pede uma licença Creative Commons. O texto e as figuras já estão sob CC BY 4.0 no
  repositório público; escolher **CC BY 4.0** mantém tudo coerente. Decisão sua.

## Campos do formulário

| Campo | Conteúdo |
|---|---|
| Arquivo | `TECHRXIV-manuscript.en.pdf` |
| Título | Discipline of language models reviewing data extracted from genomic reports under full and partial evidence: plausibility bias, erasure, and the effect of a keep rule |
| Autor | Gustavo Barcelos Barra; ORCID 0000-0002-2136-3471; gustavo@basebybase.com |
| Afiliação | Base by Base (CNPJ 69.561.948/0001-12), Brasília, DF, Brazil |
| Categoria (assunto) | **Computing and Processing**; se aceitar uma segunda, **Bioengineering** |
| Palavras-chave | large language models; data extraction; automated review; clinical genomics; plausibility bias; context faithfulness; prompt engineering; data safety |
| Financiamento | Self-funded by Base by Base; no external funding. |
| Conflito de interesses | texto abaixo |
| Dados e código | https://github.com/gbbarra/llm-reviewer-discipline-eval |
| Licença | CC BY 4.0 (recomendado; ver acima) |
| Publicado antes? | Não. Sem DOI. Não está publicado em revista. |

### Resumo (colar como texto)

Background. Large language models (LLMs) are used as reviewers of tables extracted by an earlier step of a pipeline. In this role, the model must keep correct values even when they look wrong, correct errors, and, when it cannot verify a value, flag it instead of erasing it. We found no studies that measure these three behaviours separately.
Methods. Thirteen models from seven developers reviewed tables of 33 to 40 cells extracted from three synthetic clinical exome reports. Each report has an identical twin in which the correct target value is counterintuitive (implausible twin) or common (plausible twin), plus planted plausible and implausible errors. The models received the full report or an excerpt without the sections that prove the counterintuitive values, with a statement that the table had been prepared from the full report. Four instructions (neutral, true alert, mandatory citation, keep rule) and three levels of reasoning effort were compared. A mechanical grader classified each cell as kept, kept and flagged, erased, flipped, corrected, or not corrected. A total of 3,019 responses were analysed.
Results. In the 12 models with a reasoning parameter, correct counterintuitive values were flipped in 1 of 970 cells (0.1%; 95% CI 0.02% to 0.58%). Llama 4 Maverick, without reasoning, flipped 8 of 45 in the full report and 7 of 36 in the excerpt, always "female" to "male" in a 46,XY patient with androgen insensitivity. Without the proof in the excerpt, the models diverged: Claude Opus 5.5 and Gemini 4 Argon kept almost everything and flagged it; GPT-6.1 Sol and Sol Pro erased 27 of 36 cells in each twin and changed on average 5.0 non-target cells per response. Erasure was equal in the two twins, which indicates a reaction to the literal absence of the text, not to plausibility. A keep sentence brought erasure to zero in 10 of the 13 models; raising reasoning effort cost 1.1 to 21.5 times more tokens and reduced erasure in only three models.
Conclusions. In models with reasoning, the risk is not the flipping of atypical values but the erasure of correct values under partial evidence. This behaviour is a default of some models and disappears with an explicit keep instruction.

### Conflito de interesses (colar)

G.B.B. is employed by Laboratório Sabin (Brasília, Brazil); this work was carried out independently of that employment. The author declares no other competing interests.

### Responsabilidade pela pesquisa (se o formulário tiver campo de declarações adicionais)

This study was conducted and funded by Base by Base (CNPJ 69.561.948/0001-12), Brasília, DF, Brazil, which is responsible for the research and for any correspondence on research integrity (contact: gustavo@basebybase.com).

### Uso de IA (se o formulário pedir; também está no manuscrito)

Claude (Anthropic) assisted in writing the code, generating the figures, and drafting and revising the text; Gemini 3.8 Flash (Google) reviewed style and structure. The models used as assistants include versions of the evaluated families. The author verified every number against the data and takes full responsibility for the content. The runs were executed and graded by deterministic code; no language model classified outcomes.

## Depois da submissão

- Guardar o e-mail de confirmação e, quando o preprint sair, o DOI do TechRxiv.
- Com o DOI: atualizar o README e o `CITATION.cff` deste repositório e o `manifest.yaml` do pacote
  agentic-article (campo `doi` do artigo original).
