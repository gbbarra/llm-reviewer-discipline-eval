# Recomendações Editoriais e Diretrizes Técnicas para Atualização das Figuras e Legendas

Este documento reúne as diretrizes para que outra LLM ou desenvolvedor implemente melhorias nas figuras (`fig1` a `fig6`, e `figS1`) e em suas respectivas legendas, alinhando a comunicação visual ao texto revisado em `docs/RESUMO-IMRD-piloto-2026-10-24.pt.md`.

---

## 1. Arquivos Envolvidos

* **Geração da Figura 1 (Esquema Metodológico):** `docs/figures/make_fig1.py`
* **Legenda da Figura 1:** `docs/figures/fig1-legend.md`
* **Geração das Figuras de Resultados (2 a 6 e S1):** `docs/figures/make_results_figs.py`
* **Legendas das Figuras de Resultados:** `docs/figures/results-figures-legends.md`

---

## 2. Instruções Detalhadas por Figura

### 🔹 Figura 1 (Diagrama Metodológico ABCD)
* **No script (`make_fig1.py`):**
  1. **Painel B (Provenance Notice):** A declaração de proveniência (*"The extraction table below was prepared by a previous reviewer from the full report..."*) é o fundamento que torna a exclusão de dados uma falha e não uma cautela. Destacar esse texto dentro de uma caixa com borda fina (`stroke="#0072B2"`, `fill="#D6E6F2"`, cantos arredondados) para evidenciar que o modelo foi formalmente informado sobre a origem dos dados.
  2. **Painel C (Symmetry Test):** Adicionar uma anotação visual explícita indicando a hipótese nula testada:  
     $$\text{H}_0: \text{Taxa de Apagamento}_{\text{Implausível}} = \text{Taxa de Apagamento}_{\text{Plausível}}$$
  3. **Painel D (Instruction Modulators):** Inserir chaves ou subtítulos agrupando as condições `neutral`, `flagged` e `flagged + cite` como *"Condições Padrão (Sem regra de retenção)"* e a condição `keep_rule` como *"Diretiva de Preservação Explícita"*.
* **Na legenda (`fig1-legend.md`):**
  - Desmembrar o texto em quatro tópicos bem estruturados: **(A) Viés de Plausibilidade**, **(B) Preservação vs. Apagamento**, **(C) Teste de Simetria** e **(D) Modulação por Instrução e Raciocínio**, explicitando o significado de cada cor da paleta Okabe-Ito (Verde = mantido/anotado; Vermelho = apagado; Azul = trocado; Amarelo = alvo; Hachura cinza = seções omitidas).

---

### 🔹 Figura 2 (Plausibility Bias / Flips)
* **No script (`make_results_figs.py: fig2`):**
  1. **Rótulo do Eixo X:** Substituir `"Correct values replaced by another value (%), 95% CI"` por `"Plausibility flip rate (%) [95% Wilson CI]"`.
  2. **Destaque do Llama 4 Maverick:** Na barra amarela (`#F7EFA0`), incluir anotação textual flutuante:  
     `"Llama 4 Maverick: único modelo sem parâmetro de raciocínio (11/60 flips no laudo completo)"`.
  3. **Painel A (Full Report):** Incluir anotação explicativa no quadrante inferior para orientar o leitor de que todos os pontos brancos estão sobrepostos em zero:  
     `"Todos os 12 modelos com raciocínio: 0% de trocas"`.

---

### 🔹 Figura 3 (Desfechos sob Evidência Parcial - 100% Stacked Bar)
* **No script (`make_results_figs.py: fig3`):**
  1. **Cabeçalho de Colunas para os Gêmeos:** Os identificadores `I` e `P` na margem direita das barras estão discretos. Inserir um cabeçalho acima deles:  
     `"Gêmeo: I = Implausível | P = Plausível"`.
  2. **Subtítulo Conceitual:** Inserir abaixo do título principal da figura uma linha em cor neutra (`#555555`):  
     `"O apagamento rigorosamente simétrico entre gêmeos comprova reação mecânica à ausência de texto, e não viés de plausibilidade."`

---

### 🔹 Figura 4 (Edições Colaterais em Células Não-Alvo)
* **No script (`make_results_figs.py: fig4`):**
  1. **Linha Base Ideal:** Inserir linha tracejada vertical sutil em $x = 0$ (`color="#009E73"`, `lw=0.8`, `alpha=0.6`) com rótulo `"Padrão ideal (0 edições)"`.
  2. **Nota Explicativa:** Adicionar nota de rodapé no gráfico:  
     `"Células não-alvo contêm dados fidedignos; edições indicam corrupção espúria do pipeline."`

---

### 🔹 Figura 5 (Impacto da Instrução no Apagamento - Heatmap)
* **No script (`make_results_figs.py: fig5`):**
  1. **Agrupamento Superior das Colunas:** A linha divisória preta em $x = 2.5$ separa as três condições sem regra da condição `keep_rule`. Criar dois cabeçalhos no topo do gráfico:
     * Acima de `neutral`, `flagged` e `flagged + cite`:  
       `"Instruções Padrão (Sem Regra de Retenção)"`
     * Acima de `keep rule`:  
       `"Salvaguarda Explícita (Keep Rule)"`
  2. Isso torna visualmente evidente que o colapso dos apagamentos para 0 decorre da regra de retenção.

---

### 🔹 Figura 6 (Escada de Esforço de Raciocínio e Custo de Tokens)
* **No script (`make_results_figs.py: fig6`):**
  1. **Painel A:** Adicionar nota na legenda ou rodapé explicando a dispersão vertical (*jitter*):  
     `"Pontos com taxas idênticas foram ligeiramente deslocados no eixo vertical (topo = off, meio = low, base = high) para evitar sobreposição visual."`
  2. **Painel B (Output Tokens):** Ajustar o título do eixo X para realçar o multiplicador:  
     `"Tokens de saída por resposta (média, escala log); multiplicadores indicam esforço Alto vs Baixo"`.

---

### 🔹 Figura Suplementar S1 (Scorecard Multimétrico)
* **No script (`make_results_figs.py: figS1`):**
  1. **Setas Indicativas de Direção:** Inserir no topo de cada coluna o sentido desejável da métrica:
     * `flip ↓` (ideal: 0%)
     * `erase ↓` (ideal: 0%)
     * `flag ↑` (ideal: 100% sob evidência ausente)
     * `miss ↓` (ideal: 0%)
     * `collateral ↓` (ideal: 0 edições)
