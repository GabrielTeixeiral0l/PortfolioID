# ELT (Extract, Load, Transform) &nbsp; [![Ir para README](https://img.shields.io/badge/Indice-Verde?style=for-the-badge)](../README.md#indice)

O ELT é um processo de integração de dados que inverte as duas últimas fases do ETL tradicional.

A sequência de operações é a seguinte:

- **Extract (Extração)**: Os dados são extraídos das fontes de origem, de forma semelhante ao ETL.
- **Load (Carga)**: **Em vez de serem enviados para uma área de preparação para transformação, os dados brutos são imediatamente carregados diretamente no sistema de destino**, que é tipicamente um Data Warehouse ou Data Lake na nuvem (como Google BigQuery, Amazon Redshift ou Snowflake).
- **Transform (Transformação)**: A **transformação dos dados ocorre dentro do sistema de destino**. As regras de negócio, limpeza e padronização são aplicadas aos dados já carregados, aproveitando o poder de processamento massivo e paralelo do Data Warehouse moderno.

## ETL vs ELT

A escolha entre ETL e ELT depende de vários fatores, como o
volume de dados, a infraestrutura disponível e os objetivos de
análise.

### Devemos utilizar ETL quando:

- Os dados são maioritariamente estruturados e provêm de fontes relacionais.
- As transformações são complexas, pesadas e requerem um motor dedicado.
- Existem fortes requisitos de segurança e conformidade que exigem que os dados sensíveis sejam limpos ou mascarados antes de entrarem no Data Warehouse.
- A infraestrutura de destino (Data Warehouse) não tem poder de processamento suficiente para realizar as transformações de forma eficiente.
- O volume de dados não é massivo (embora o ETL também possa lidar com grandes volumes, o ELT é geralmente mais escalável para Big Data)

### Devemos utilizar ELT quando:

- Lidamos com grandes volumes de dados (Big Data), incluindo
  dados não estruturados ou semiestruturados.
- A velocidade de ingestão dos dados é uma prioridade. O ELT permite que os dados estejam disponíveis para consulta quase imediatamente após a extração.
