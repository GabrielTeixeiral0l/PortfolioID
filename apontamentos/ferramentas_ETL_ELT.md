# Ferramentas ETL e ELT &nbsp; [![Ir para README](https://img.shields.io/badge/Indice-Verde?style=for-the-badge)](../README.md#indice)

## O Papel das Ferramentas no Processo ETL

As ferramentas de integração de dados automatizam o processo de **Extração, Transformação e Carregamento (ETL)** — ou a sua variação mais recente, **Extração, Carregamento e Transformação (ELT)**.  
Estas ferramentas são essenciais para consolidar dados de **múltiplas fontes heterogéneas** num destino comum, como um **Data Warehouse** ou **Data Lake**.

As principais funcionalidades incluem:

- **Conectividade:** ligação a bases de dados, ficheiros, APIs e sistemas empresariais (ERP/CRM).
- **Transformação:** aplicação de regras de negócio, limpeza e padronização de dados.
- **Orquestração:** gestão do fluxo de trabalho, agendamento e monitorização de processos.

---

## Classificação das Ferramentas

As ferramentas de integração de dados dividem-se em duas grandes categorias:

### Ferramentas Open Source

Exemplos: **Apache NiFi**, **Apache Airflow**, **Pentaho Kettle**, **Logstash**, **Meltano**, **dbt**.  
Características principais:

- Gratuitas (mas requerem manutenção interna).
- Altamente personalizáveis, exigindo conhecimentos técnicos.
- Suporte baseado na comunidade.
- Escalabilidade dependente da arquitetura e da experiência da equipa.
- Curva de aprendizagem mais acentuada.

### Ferramentas Comerciais

Exemplos: **Talend Enterprise**, **Microsoft SSIS**, **Informatica**, **Azure Data Factory**, **AWS Glue**, **Google Dataflow**.  
Características principais:

- Requerem licenciamento pago, mas incluem suporte profissional.
- Mais fáceis de usar (GUI intuitiva).
- Altamente escaláveis e otimizadas para ambientes empresariais.
- Documentação e suporte garantidos.

---

## Critérios de Seleção de uma Ferramenta ETL

A escolha de uma ferramenta depende de fatores técnicos e estratégicos:

- **Conectividade:** compatibilidade com todas as fontes e destinos de dados.
- **Escalabilidade e performance:** capacidade de lidar com grandes volumes de dados.
- **Facilidade de uso:** qualidade da interface e curva de aprendizagem.
- **Funcionalidades de transformação:** limpeza, padronização e agregação.
- **Orquestração e agendamento:** automação e monitorização dos fluxos de trabalho.
- **Custo total (TCO):** inclui licenças, infraestrutura e recursos humanos.
- **Suporte e comunidade:** disponibilidade de ajuda e documentação.

---

## Ferramentas Open Source em Destaque

### Apache NiFi

Plataforma para **automação de fluxos de dados** entre sistemas.  
Baseia-se em programação de fluxo de dados (_dataflow programming_) e é ideal para processamento em **tempo real**.

**Conceitos chave:**

- **FlowFile:** unidade de dados e metadados.
- **Processors:** componentes que executam tarefas específicas.
- **Connections:** filas de comunicação entre Processors.
- **Flow Controller:** gere a execução e o fluxo global.
- **Data Provenance:** histórico completo do ciclo de vida dos dados.

**Casos de uso:** ingestão de dados em tempo real, movimentação de grandes volumes, e roteamento dinâmico de dados.

---

### Apache Airflow

Plataforma para **criação, agendamento e monitorização de workflows**.  
Embora não seja uma ferramenta ETL pura, é amplamente usada para **orquestrar pipelines de dados**.

**Conceitos chave:**

- **DAG (Directed Acyclic Graph):** representa a sequência de tarefas.
- **Operators:** definem o tipo de tarefa (Bash, Python, SQL, etc.).
- **Tasks:** instâncias de operadores.
- **Scheduler:** agenda e gere a execução dos DAGs.

**Casos de uso:** orquestração de pipelines ETL, Machine Learning e gestão de dependências entre tarefas.

---

### Pentaho Data Integration (Kettle)

Ferramenta gráfica **open source** para o desenvolvimento de processos ETL.

**Componentes:**

- **Spoon:** ambiente gráfico onde se criam jobs e transformações.
- **Transformations:** executam operações de ETL (extração, transformação e carregamento).
- **Jobs:** coordenam as transformações e controlam o fluxo de execução.

**Vantagens:** interface intuitiva, elevada conectividade e ideal para processamento por lotes (_batch_).

---

## Outras Ferramentas Open Source

- **Logstash:** focado na ingestão e transformação de logs e eventos.
- **Meltano:** foca-se em extração e carregamento (ELT).
- **dbt (Data Build Tool):** concentra-se exclusivamente na transformação, usando SQL como código versionável.

---

## Ferramentas Comerciais e Cloud

### Talend Data Integration

Disponível em versão **open source** (Talend Open Studio) e **empresarial**.  
Oferece uma interface gráfica _drag-and-drop_, milhares de conectores e integração com Big Data e Cloud.

### Microsoft SSIS (SQL Server Integration Services)

Ferramenta ETL integrada no ecossistema Microsoft.  
Permite transformações complexas, integração com .NET e elevado desempenho em ambientes corporativos.

### Ferramentas Cloud

- **AWS Glue (Amazon):** ETL serverless para Big Data e Data Lakes.
- **Azure Data Factory:** serviço de integração e orquestração de dados baseado em Cloud.
- **Google Cloud Dataflow:** processamento de dados em _stream_ e _batch_, baseado em Apache Beam.

---

## Ferramentas ELT Modernas

O paradigma **ELT** carrega primeiro os dados para o **Data Warehouse** (ex.: Snowflake, BigQuery, Redshift) e realiza a transformação no próprio ambiente.  
Exemplos:

- **Fivetran** e **Stitch** — automatizam as fases de Extração e Carregamento.
- **dbt** — executa as transformações diretamente via SQL.

---

## Integração com Linguagens de Programação

### Python

O **Python** é amplamente utilizado na integração de dados devido às suas bibliotecas:

- **requests** — extração de dados de APIs REST e SOAP.
- **pandas** — manipulação, limpeza e transformação de dados.
- **sqlalchemy** — ligação a bases de dados relacionais.
- **pyspark** — processamento distribuído para Big Data.

**Vantagens:**

- Extração flexível (APIs, ficheiros CSV, JSON, etc.).
- Transformações poderosas através de _DataFrames_.
- Funções nativas para limpeza e padronização de dados.
- Ecossistema vasto e comunidade ativa.

---

### SQL

O **SQL** é essencial na fase de **Transformação (T)**, especialmente no paradigma ELT.

- **Views:** tabelas virtuais que simplificam consultas complexas e aplicam regras de negócio.
- **Stored Procedures:** blocos de instruções SQL pré-compilados que automatizam transformações e carregamentos.

---

### Conexão a APIs

A extração de dados de **APIs RESTful** é comum em integrações modernas.  
Com a biblioteca **requests**, é possível:

1. Fazer pedidos HTTP (GET, POST).
2. Receber dados (JSON ou XML).
3. Converter para _DataFrames_ Pandas para limpeza e transformação.
