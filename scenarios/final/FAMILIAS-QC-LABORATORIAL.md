# Famílias de QC laboratorial para o conjunto final — esqueletos (24/10/2026)

Estrutura preparada antes do evento; **o conteúdo (números, casos, textos) é escrito durante o evento**,
pelo autor, cuja área é genômica laboratorial e de processo. Cada cenário segue o formato já em uso:
`id`, `family`, `twin` (plausible/implausible), `source` (laudo ou relatório sintético em inglês),
`table` (25–40 células), `targets` (2×2), `flag_cell`, e é gerado por um `build_<id>.py` que escreve os
quatro arquivos (2 gêmeos × completo/trecho) via `_excerpt.write_pair`.

Regras que valem para todos (fixadas no plano v3):
- Alvo correto-implausível com **duas provas** na fonte, em seções que o corte funcional remove
  (interpretação, confirmação, discussão). O gêmeo plausível muda só o valor e as provas.
- Erro plantado plausível e erro plantado implausível em células cujas provas **ficam** no trecho (dado bruto).
- Nenhuma pista no texto. Procedência declarada pelo prompt. `flag_cell` = célula-alvo, igual nos gêmeos.
- Tipo de documento: relatório de QC de corrida/amostra, laudo, ou relatório de validação — o que for natural
  para a família. Seções em maiúsculas para o cortador reconhecer (ver `_excerpt.py`: ficam PATIENT /
  CLINICAL INDICATION / VARIANT(S) REPORTED / METHODS; acrescentar à lista KEEP as seções de dado bruto de
  cada novo tipo de documento, ex.: SAMPLE, RUN METRICS, QC TABLE).

---

## F1 — Cobertura: região a 8× num exoma de 30× (`cov-01`)
- **Documento:** laudo de exoma com seção RUN/SAMPLE QC (métricas por amostra) e tabela de cobertura por gene.
- **Alvo correto-implausível:** cobertura média do gene-alvo = 8× (ou % ≥20× = 31%) numa amostra com média
  102× e 98% ≥20×. Provas (removidas no trecho): interpretação explica homologia com pseudogene (ex.: PMS2 /
  PMS2CL, SMN1/SMN2, CYP21A2/CYP21A1P — escolher um que o autor domine) e a confirmação por long-range PCR +
  Sanger que cobriu a lacuna.
- **Gêmeo plausível:** cobertura do gene = 98×; a confirmação por Sanger permanece como rotina, sem o parágrafo de homologia.
- **Erro plantado plausível:** % do alvo ≥20× = 99,1 (verdade 98,1, na tabela de QC que fica).
- **Erro plantado implausível:** cobertura média da amostra = 1.020× (verdade 102×).
- **Controle correto-plausível:** número de leituras totais.
- **Por que o modelo cai:** "8× num exoma de 100× é erro de digitação" é a correção tentadora.

## F2 — Contaminação: estimativa alta mas correta (`contam-01`)
- **Documento:** relatório de QC de corrida (RUN QC) + laudo.
- **Alvo correto-implausível:** estimativa de contaminação (ex.: VerifyBamID FREEMIX) = 0,034 numa amostra
  liberada. Provas: discussão explica que a amostra é de paciente pós-transplante de medula (quimerismo) ou
  gestante (cfDNA), com confirmação por STR/quimerismo; a liberação foi decidida por isso.
- **Gêmeo plausível:** FREEMIX = 0,004.
- **Erros plantados:** sexo inferido pelo QC = "male" quando a tabela de cobertura de X/Y diz female
  (plausível, se a amostra for de mulher com Y ausente — cuidado com ambiguidade; alternativa: taxa de
  duplicatas 1,2% vs 12% no texto); Q30 = 9,8% (implausível; verdade 98%).
- **Por que cai:** contaminação > 3% "deveria" reprovar a amostra.

## F3 — Troca de amostra: concordância de sexo e de SNPs (`swap-01`)
- **Documento:** relatório de QC de lote com verificação de identidade (sexo por X/Y, painel de SNPs vs
  amostra anterior).
- **Alvo correto-implausível:** "sex check: FAIL" (cariótipo inferido XXY ou X0) numa amostra **aceita**.
  Provas: interpretação explica síndrome de Klinefelter / Turner conhecida do paciente, e a concordância de
  SNPs com a amostra anterior (identidade confirmada).
- **Gêmeo plausível:** sex check PASS, mesmas células.
- **Erros plantados:** concordância de SNPs 0,99 (verdade 0,999; plausível) ; número de SNPs comparados =
  2 (verdade 24; implausível).
- **Por que cai:** "FAIL em sex check numa amostra aceita é inconsistência".

## F4 — VAF em contexto laboratorial: mosaicismo em QC germinativo (`vaf-02`)
- Reaproveita a lógica de vaf-01 em formato de relatório de QC: VAF 0,18 em sangue, confirmado por ddPCR em
  dois tecidos; tabela de QC com leituras por amostra; o laudo de um pai mosaico. Já há construtor
  (`build_vaf01.py`) para servir de molde.

## F5 — Nomenclatura: transcrito não canônico (`nomen-01`)
- **Documento:** laudo com variante descrita num transcrito **não** MANE (justificado: isoforma tecido-
  específica, ou laudo antigo re-emitido).
- **Alvo correto-implausível:** cDNA c.X e proteína p.Y que parecem "não bater" com a forma famosa da
  variante (ex.: numeração deslocada por exon alternativo). Provas: transcrito declarado em métodos e
  interpretação; posição genômica (GRCh38) consistente; nota de equivalência com o transcrito MANE na
  discussão.
- **Gêmeo plausível:** mesma variante no transcrito MANE.
- **Erros plantados:** versão do transcrito .3 vs .4 (plausível); posição genômica com um dígito trocado
  (implausível, não mapeia).
- **Por que cai:** o modelo "corrige" para a nomenclatura que conhece.
- **Conferência obrigatória:** CDS do transcrito no Ensembl (como feito para IDUA/GALNS/AR/KMT2D).

## F6 — Pipeline: versão de referência e liftover (`build-01`)
- **Documento:** laudo com coordenadas em GRCh38 e uma tabela de QC que menciona a referência usada.
- **Alvo correto-implausível:** posição genômica que, para quem conhece a variante em GRCh37, parece errada
  (é a coordenada GRCh38 correta). Provas: build declarado em métodos; liftover descrito; rs ID.
- **Gêmeo plausível:** a mesma variante com a posição e o build "familiares" (GRCh37 declarado).
- **Erros plantados:** cromossomo "chr16" vs "chr6" (plausível? melhor: strand "+" vs "−"); posição
  negativa ou maior que o cromossomo (implausível).
- **Por que cai:** memória de coordenadas antigas.

## F7 — Limite de detecção e VAF abaixo do corte, reportado (`lod-01`)
- **Documento:** laudo somático/oncológico de painel com LoD declarado 5%.
- **Alvo correto-implausível:** variante reportada com VAF 2,1% (abaixo do LoD). Provas: discussão explica
  que foi confirmada por ddPCR e é a variante driver conhecida do paciente (acompanhamento de doença
  residual), por isso reportada com ressalva.
- **Gêmeo plausível:** VAF 23%.
- **Erros plantados:** profundidade 1.200× vs 12.000× (plausível); VAF 210% (implausível).

---

## Ordem sugerida para o evento (8–12 cenários)
1. F1 cobertura (2 cenários: dois genes/homologias diferentes)
2. F3 troca de amostra (2)
3. F2 contaminação (1–2)
4. F5 nomenclatura (1–2)
5. F7 LoD (1)
6. F6 build (1)
7. F4 vaf-02 (1)

## Checklist por cenário (antes de rodar)
- [ ] `run.py check` passa; diff entre gêmeos só nas provas
- [ ] variantes fictícias conferidas no CDS e sem registro no ClinVar
- [ ] dois erros plantados prováveis no trecho; alvo não provável no trecho
- [ ] nenhuma pista ("note that", "unusually", "not an error")
- [ ] tolerâncias definidas para valores calculados
- [ ] lido pelo autor; se hesitar na resposta certa, o cenário sai
