# ETL - Fase 2 (Transform) &nbsp; [![Ir para README](https://img.shields.io/badge/Indice-Verde?style=for-the-badge)](../README.md#indice)

Esta é a fase mais complexa e onde o maior valor é
acrescentado.
Os dados brutos extraídos são processados e convertidos
num formato limpo, consistente e adequado para o sistema
de destino.

As operações de transformação mais comuns incluem:

- **Limpeza (Cleansing)**: Corrigir ou remover dados incorretos,
  inconsistentes ou duplicados e tratar valores em falta (nulos).

- **Padronização (Standardization)**: Assegurar que os dados
  seguem um formato uniforme. Por exemplo, converter todas
  as datas para o formato AAAA-MM-DD ou unidades de medida
  para um padrão comum.

- **Agregação (Aggregation)**: Resumir dados para um nível de
  granularidade mais alto, como calcular o total de vendas
  diárias a partir de transações individuais.

- **Junção (Joining)**: Combinar dados de diferentes fontes. Por
  exemplo, juntar dados de clientes de um CRM com dados de
  vendas de um sistema transacional.

- **Validação (Validation)**: Aplicar regras para garantir a
  integridade e a qualidade dos dados (ex: verificar se um
  código postal tem o formato correto).

- **Enriquecimento (Enrichment)**: Adicionar novos dados
  calculados ou derivados dos dados existentes, como calcular a
  idade de um cliente a partir da sua data de nascimento.
