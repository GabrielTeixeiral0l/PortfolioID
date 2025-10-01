# Arquitetura de ETL &nbsp; [![Ir para README](https://img.shields.io/badge/Indice-Verde?style=for-the-badge)](../README.md#indice)

Extract: dados vindos de várias fontes (ficheiros, BD, APIs).

Transform: normalização, limpeza, enriquecimento, agregação.

Load: carregamento em DW, DL ou outra BD.

[Fontes] → [Extract] → [Transform] → [Load] → [Data Warehouse] → [BI Reports]

## Fase 1: Extração (Extract)

A primeira fase consiste em recolher ou extrair os dados das
suas fontes de origem. Estas fontes podem ser extremamente
variadas e heterogéneas.

Fontes de Dados Comuns:
• Bancos de dados relacionais (SQL Server, Oracle, MySQL).
• Bancos de dados NoSQL (MongoDB, Cassandra).
• Sistemas empresariais como ERPs e CRMs.
• Ficheiros planos (CSV, JSON, XML).
• APIs de serviços web.
• Sensores de dispositivos IoT.

Os dados extraídos são geralmente movidos para uma área
de preparação (staging area), que é um repositório
intermédio onde os dados são armazenados temporariamente
antes de serem transformados.

### Métodos de Extração

• Carga Completa (Full Load): Todos os dados da fonte são
extraídos de uma só vez. Este método é mais simples, mas
pode ser impraticável para grandes volumes de dados.

• Carga Incremental (Incremental Load): Apenas os dados
novos ou modificados desde a última extração são recolhidos.
Este método é mais eficiente, pois reduz o volume de dados
transferidos e o tempo de processamento.
