# Master Data Management (MDM) &nbsp; [![Ir para README](https://img.shields.io/badge/Indice-Verde?style=for-the-badge)](../README.md#indice)

O **Master Data Management (MDM)** é uma prática que se foca na criação e manutenção de uma visão única, consistente e precisa dos dados de negócio mais críticos (*Master Data*) em toda a organização.

O *Master Data* inclui entidades como Clientes, Produtos, Fornecedores e Localizações.

## Relação com a Integração de Dados

A integração de dados é o mecanismo que alimenta o MDM, e o MDM, por sua vez, garante a qualidade e a consistência dos dados integrados.

## Estratégias de MDM

Existem várias abordagens para implementar o MDM, que se refletem na forma como os dados mestres são integrados. A implementação de uma estratégia de MDM é um passo avançado na integração de dados, garantindo que as decisões de negócio são baseadas numa fonte de verdade única e fiável.

| Estratégia        | Descrição                                                                                                                            | Vantagem                                                              |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------- |
| **Registry**      | Cria um índice centralizado dos dados mestres, mas os dados reais permanecem nos sistemas de origem.                                 | Implementação mais rápida e menos disruptiva.                         |
| **Consolidation** | Os dados mestres são extraídos dos sistemas de origem, limpos, unificados e carregados num repositório central (o Hub MDM).         | Fornece uma "visão dourada" única para análise e relatórios.          |
| **Coexistence**   | Semelhante à Consolidação, mas o Hub MDM também sincroniza as alterações de volta para os sistemas de origem.                      | Garante que todos os sistemas operativos utilizam a mesma versão dos dados mestres. |
