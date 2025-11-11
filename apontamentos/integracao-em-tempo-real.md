# Integração em Tempo Real &nbsp; [![Ir para README](https://img.shields.io/badge/Indice-Verde?style=for-the-badge)](../README.md#indice)

A **Integração de Dados em Tempo Real** é um paradigma que visa capturar, processar e entregar dados no momento em que são gerados, com uma latência mínima, geralmente medida em milissegundos ou segundos. Distingue-se do processamento em lotes (*batch processing*), que lida com grandes volumes de dados em intervalos de tempo programados (ex: diário ou noturno).

A necessidade de integração em tempo real surge em cenários onde a informação tem um valor temporal crítico, como:
-   **Deteção de fraude** em transações financeiras.
-   **Monitorização de sistemas de IoT** para alertas imediatos.
-   **Personalização de experiências web** baseada no comportamento atual do utilizador.

## Change Data Capture (CDC)

O **Change Data Capture (CDC)** é uma técnica essencial que identifica e rastreia as alterações (inserções, atualizações e eliminações) numa base de dados de origem e as entrega a um sistema de destino em tempo real, mantendo-os sincronizados sem a necessidade de leituras completas e dispendiosas.

### Métodos de Implementação de CDC

1.  **Baseado em Logs (Log-Based CDC)**:
    -   Considerado o método mais eficiente e menos intrusivo.
    -   Lê diretamente os logs de transações da base de dados (ex: Binlog do MySQL, Redo Logs do Oracle) para capturar as alterações.

2.  **Baseado em Triggers**:
    -   Utiliza *triggers* (gatilhos) na base de dados para registar as alterações numa tabela de auditoria separada.
    -   Embora simples, pode introduzir sobrecarga (*overhead*) no desempenho da base de dados de origem.

3.  **Baseado em Colunas de Timestamp**:
    -   Envolve a consulta periódica de tabelas que possuem colunas de data/hora de última modificação.
    -   É o método menos "real-time" e mais propenso a falhas na captura de alterações.

## Message Queues e Stream Processing

A integração em tempo real é frequentemente implementada com plataformas de **Message Queues** ou **Event Streaming**, que atuam como intermediários de alta velocidade para o fluxo de dados.

-   **RabbitMQ**: Um *message broker* tradicional, otimizado para o encaminhamento de mensagens individuais e para a gestão de filas de tarefas (*task queues*). É ideal para comunicação ponto-a-ponto.

-   **Apache Kafka**: Uma plataforma de *event streaming* distribuída, concebida para lidar com elevados volumes de dados contínuos e processamento em tempo real em grande escala. É a escolha preferencial para a maioria dos pipelines de Big Data.
