# Gestão da Qualidade de Dados (DQM) &nbsp; [![Ir para README](https://img.shields.io/badge/Indice-Verde?style=for-the-badge)](../README.md#indice)

A Gestão da Qualidade de Dados (DQM - Data Quality Management) é um conjunto abrangente de processos, políticas, padrões e tecnologias implementadas por uma organização para garantir que os dados sejam adequados para o seu uso pretendido.

O objetivo da DQM é melhorar e manter a qualidade dos
dados ao longo de todo o seu ciclo de vida, desde a criação até
ao arquivo, garantindo que sejam precisos, completos, atuais,
consistentes, únicos e válidos.

## Princípios e Ciclo de Vida da DQM

A DQM não é um evento único, mas um processo contínuo e iterativo que segue um ciclo de vida bem definido.

Os princípios fundamentais da DQM incluem a
responsabilidade pelos dados, a medição contínua da
qualidade, a melhoria proativa e a integração da qualidade de
dados nos processos de negócio.

### Fases

O ciclo de vida da DQM segue as seguintes fases:

1. **Definição**: Identificar os requisitos de qualidade de dados com base nas
   necessidades de negócio e definir métricas de qualidade.

2. **Avaliação**: Medir a qualidade dos dados existentes em relação às
   métricas definidas, identificando problemas e suas causas-raiz (Data
   Profiling).

3. **Melhoria**: Implementar ações corretivas para resolver os problemas de
   qualidade de dados, como limpeza, padronização e enriquecimento.

4. **Monitorização**: Acompanhar continuamente a qualidade dos dados
   para garantir que os padrões são mantidos e para detetar novos
   problemas.

5. **Governança**: Estabelecer políticas, papéis e responsabilidades para a
   gestão da qualidade de dados em toda a organização.

## Estratégias para Melhorar a Qualidade de Dados

- **Definição de Padrões de Dados**: Estabelecer formatos, domínios de valores e regras de negócio claros para todos os dados.
- **Validação na Fonte**: Implementar validações no ponto de entrada dos dados para prevenir a introdução de erros.
- **Limpeza de Dados (Data Cleansing)**: Processos para identificar e corrigir dados incorretos, incompletos, duplicados ou inconsistentes.

- **Padronização e Normalização**: Transformar dados para um formato uniforme e consistente.
- **Enriquecimento de Dados**: Adicionar informações de fontes externas para tornar os dados mais completos e úteis.
- **Governança de Dados**: Criar uma estrutura organizacional com papéis e responsabilidades claras para a gestão de dados, incluindo a qualidade.
- **Formação e Consciencialização**: Educar os utilizadores sobre a importância da qualidade de dados e as melhores práticas.

## Ferramentas e Tecnologias para DQM

Existem diversas ferramentas e tecnologias que suportam os processos de DQM, desde soluções empresariais abrangentes até bibliotecas de código aberto:

- **Ferramentas de Data Profiling**: Analisam os dados para
  descobrir padrões, anomalias e identificar problemas de qualidade (ex:
  Talend Open Studio, Atlan).
- **Ferramentas de Data Cleansing e Padronização**:
  Automatizam a correção e transformação de dados (ex: Informatica
  Data Quality, OpenRefine).

- **Ferramentas de Gestão de Metadados**: Armazenam
  informações sobre os dados, incluindo definições, regras de negócio e
  linhagem (ex: Collibra, Alation).
- **Ferramentas de Governança de Dados**: Suportam a
  implementação de políticas e a gestão de acesso e conformidade.
- **Linguagens de Programação**: Python (com bibliotecas como
  Pandas, Great Expectations) e SQL são amplamente utilizadas para
  desenvolver rotinas personalizadas de validação e limpeza de dados.
