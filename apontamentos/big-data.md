# Big Data &nbsp; [![Ir para README](https://img.shields.io/badge/Indice-Verde?style=for-the-badge)](../README.md#indice)

O conceito de Big Data é frequentemente definido pelos seus **3 Vs** originais, que descrevem as características que tornam os dados difíceis de processar com métodos tradicionais:

-   **Volume**: A quantidade massiva de dados gerados (terabytes, petabytes, exabytes). A integração deve ser capaz de escalar horizontalmente para lidar com este volume.
-   **Velocidade (Velocity)**: A rapidez com que os dados são gerados, recolhidos e processados (abordado anteriormente como Real-Time).
-   **Variedade (Variety)**: A diversidade de formatos e tipos de dados, que vão desde o estruturado (tabelas relacionais) ao semi-estruturado (JSON, XML) e ao não-estruturado (texto livre, imagens, logs). A variedade é o principal desafio, pois a integração tradicional baseada em esquemas fixos (Schema-on-Write) não é adequada para dados que não se encaixam facilmente em linhas e colunas.

## Tecnologias e Plataformas para Big Data

Para lidar com a variedade e o volume do Big Data, surgiram novas tecnologias e arquiteturas de armazenamento:

### Bases de Dados NoSQL

As bases de dados NoSQL (Not Only SQL) são concebidas para lidar com grandes volumes de dados e esquemas flexíveis, sendo essenciais na integração de dados variados.

### Data Lakes e Data Warehouses Modernos

A integração de Big Data requer uma infraestrutura de armazenamento que possa receber dados em qualquer formato.

-   **Data Warehouse (DW)**: Armazena dados estruturados que foram limpos, transformados e modelados (Schema-on-Write) para fins de Business Intelligence (BI) e relatórios predefinidos. É otimizado para consultas analíticas rápidas.
-   **Data Lake (DL)**: Armazena dados brutos em qualquer formato (estruturado, semi-estruturado, não-estruturado) e permite que o esquema seja aplicado no momento da leitura (Schema-on-Read). É ideal para ciência de dados, machine learning e análises exploratórias. O Data Lake atua frequentemente como o ponto de entrada (*staging area*) para todos os dados, incluindo os não-estruturados, antes de serem integrados e transformados para o Data Warehouse ou para outras aplicações.
-   **Data Lakehouse**: Uma arquitetura híbrida que combina a flexibilidade e o baixo custo do Data Lake com as estruturas de gestão de dados e desempenho do Data Warehouse, utilizando formatos abertos como Parquet ou Delta Lake.

## Processamento de Dados Não-Estruturados

A integração de dados semi-estruturados (ex: JSON, XML) e não-estruturados (ex: logs, texto livre) exige etapas adicionais de **Parsing** e **Normalização** para que possam ser utilizados em análises ou carregados em bases de dados relacionais.

### Parsing (Análise Sintática)

É o processo de analisar o formato dos dados para extrair informações significativas.
-   Num ficheiro JSON, o *parsing* identifica as chaves e os valores correspondentes.
-   Em logs de servidor, o *parsing* separa os campos (*timestamp*, IP, método HTTP, URL) com base em delimitadores ou padrões (*regex*).

### Normalização

Após a extração, os dados precisam de ser normalizados, ou seja, transformados num formato consistente e padronizado. Isto pode incluir:
-   Aplanar (*Flattening*)
-   Tipagem
-   Padronização
