# Arquiteturas Lambda e Kappa &nbsp; [![Ir para README](https://img.shields.io/badge/Indice-Verde?style=for-the-badge)](../README.md#indice)

As arquiteturas Lambda e Kappa definem a forma como os dados são processados para garantir tanto a precisão histórica quanto a velocidade em tempo real.

## Arquitetura Lambda

A Arquitetura Lambda combina duas camadas de processamento:
-   **Camada Batch**: Responsável pela precisão e processamento de dados históricos.
-   **Camada Speed**: Responsável pela baixa latência e processamento de dados em tempo real.

Os resultados de ambas as camadas são combinados numa **camada Serving** para apresentar uma visão completa dos dados. A principal desvantagem desta arquitetura é a complexidade de manter e desenvolver código em duas camadas separadas.

## Arquitetura Kappa

A Arquitetura Kappa simplifica a Lambda ao eliminar a camada Batch. Todo o processamento é feito através de uma única **camada Stream** (processamento de fluxo). Os dados históricos são tratados simplesmente reprocessando o log de eventos desde o início. Esta arquitetura é mais simples de manter e mais económica, sendo a tendência atual para muitos sistemas de Big Data.
