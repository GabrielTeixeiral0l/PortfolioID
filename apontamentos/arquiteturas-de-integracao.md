# Arquiteturas de Integração &nbsp; [![Ir para README](https://img.shields.io/badge/Indice-Verde?style=for-the-badge)](../README.md#indice)

Uma arquitetura de integração define o modelo e a
infraestrutura para conectar diferentes aplicações e fontes de
dados.

A escolha da arquitetura depende dos requisitos de negócio,
como o volume de dados, a latência (tempo real vs. agendado)
e a complexidade dos sistemas.

Existem várias formas de integrar dados:

- Integração em **Batch**
- Integração em **Streaming** (tempo real)
- Integração via **APIs/Serviços** Web

## Batch (em Lote)

**Descrição**: Os dados são recolhidos, processados e movidos em grandes lotes, de forma agendada (ex: todas as noites). É uma das abordagens mais tradicionais.

**Tecnologia Comum**: Processos ETL (Extract, Transform, Load).

**Casos de Uso**: Atualização noturna de um Data Warehouse, processamento de folhas de pagamento, geração de relatórios mensais.

**Vantagens**: Ideal para grandes volumes de dados, fiável e menos
complexo de gerir para processos não críticos em tempo real.

**Desvantagens**: Alta latência (os dados não estão disponíveis em tempo
real).

## Streaming (em Tempo Real)

**Descrição**: Os dados são processados e movidos continuamente,
evento a evento ou em micro-lotes, assim que são gerados.

**Tecnologia Comum**: Plataformas de streaming como Apache Kafka, AWS
Kinesis, Azure Event Hubs.

**Casos de Uso**: Deteção de fraude em transações financeiras,
monitorização de sensores IoT (Internet of Things), análise de cliques em
websites em tempo real.

**Vantagens**: Baixa latência, permite a tomada de decisão imediata.

**Desvantagens**: Mais complexo de implementar e gerir, pode ser mais
caro.

## Serviços Web / APIs

**Descrição**: A integração é feita através de chamadas a serviços web ou APIs (Application Programming Interfaces). Um sistema expõe funcionalidades e
dados que outros sistemas podem consumir através de pedidos (requests).

**Tecnologia Comum**: APIs REST (baseadas em HTTP), SOAP, gRPC, GraphQL.

**Casos de Uso**: Uma aplicação móvel que consulta o stock de um produto,
um site de reservas de voos que se conecta a várias companhias aéreas.

**Vantagens**: Promove o desacoplamento entre sistemas, é flexível, escalável
e reutilizável.

**Desvantagens**: Requer uma boa gestão de APIs (segurança, versão,
documentação).
