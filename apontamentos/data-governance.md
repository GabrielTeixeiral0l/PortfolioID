# Data Governance e Qualidade de Dados &nbsp; [![Ir para README](https://img.shields.io/badge/Indice-Verde?style=for-the-badge)](../README.md#indice)

À medida que a integração de dados se torna mais complexa (tempo real, Big Data, variedade de fontes), a necessidade de gerir e garantir a fiabilidade dos dados integrados torna-se crítica. A **Data Governance (Governança de Dados)** e a **Qualidade de Dados** são os pilares que sustentam a confiança e o valor dos sistemas de integração.

## Data Governance (Governança de Dados)

A Data Governance é o conjunto de políticas, normas, padrões e práticas que orientam, monitoram e avaliam a gestão e o uso dos dados, para assegurar que sejam utilizados de forma consistente, segura e em conformidade com as regulamentações (ex: RGPD).

### O Papel da Data Governance na Integração de Dados

A Data Governance é vital para a integração, pois define:
-   **Propriedade dos Dados**: Quem é responsável pela qualidade e integridade dos dados em cada sistema de origem (*Data Owners*).
-   **Padrões de Integração**: Normas para nomenclatura, formatos de dados e modelos de dados canónicos a serem usados nos pipelines de integração.
-   **Segurança e Acesso**: Políticas que garantem que apenas utilizadores e sistemas autorizados possam aceder e modificar os dados integrados, especialmente em ambientes de Big Data e *cloud*.
-   **Conformidade**: Assegurar que os dados integrados cumprem os requisitos legais e regulamentares.

## Qualidade de Dados (Data Quality)

A Qualidade de Dados refere-se à adequação dos dados para o uso pretendido. Dados de baixa qualidade podem levar a decisões de negócio erradas, ineficiências operacionais e perda de confiança.

### Dimensões da Qualidade de Dados

| Dimensão         | Descrição                                                              | Exemplo de Falha                                                              |
| :--------------- | :--------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| **Precisão**     | O grau em que os dados refletem a realidade.                           | Um endereço de cliente está incorreto.                                        |
| **Completude**   | A percentagem de valores não nulos em campos críticos.                 | O campo "Email" está vazio para 30% dos clientes.                             |
| **Consistência** | Os dados são coerentes entre diferentes sistemas.                      | O nome do cliente é "João Silva" num sistema e "J. Silva" noutro.             |
| **Atualidade**   | Os dados estão disponíveis e atualizados no momento necessário.        | O inventário de produtos está desatualizado em 24 horas.                      |
| **Validade**     | Os dados estão em conformidade com o formato, tipo e intervalo de valores definidos. | Um campo de idade contém o valor "abc" ou um número negativo.                 |

## Processos de Data Profiling e Data Cleansing

### Data Profiling (Criação de Perfil de Dados)

É a análise sistemática dos dados de origem para descobrir a sua estrutura, qualidade e conteúdo. O *profiling* identifica padrões, anomalias, valores únicos e a distribuição de valores, fornecendo uma base para definir as regras de qualidade e transformação.

### Data Cleansing (Limpeza de Dados)

É o processo de detetar e corrigir ou remover registos incorretos, incompletos, imprecisos ou irrelevantes. Inclui a padronização de formatos, a correção de erros de digitação e a resolução de inconsistências.
