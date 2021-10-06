# Resposta Dados - Q1

# Tabela de conteúdo - Geral

1. [ Questão pedida. ](#desc)
2. [ Solução. ](#usage)


<a name="desc"></a>
Questão
---
Consuma os dados da API do Instituto Nacional de Meteorologia (INMET).

Acesse a [documentação da API](https://portal.inmet.gov.br/manual/manual-de-uso-da-api-esta%C3%A7%C3%B5es).

Obtenha (1 pt todos):

- a lista de estações automáticas.
- uma série de 14 dias contendo todas as variáveis da uma estação qualquer.

Consolide (1 pt todos):

- a lista das estações automáticas em um dataframe.
- a série de 14 dias de dados em um dataframe.

Extras:

- use requisições assíncronas ou threadding para coletar dados de 15 estações (1 pt).
- há falhas nos dados? Crie uma forma de verificar (0.5 pt).
- há valores espúrios? Crie uma forma de verificar (0.5 pt).
- gere um gráfico de alguma variável contendo séries de duas estações (1 pt).
  - Nota: use matplotlib, plotly, altair ou qualquer outra biblioteca que você conheça (1 pt).

---

<a name="usage"></a>
<h2>Solução</h2>
---

