# Qualidade e Consistência de Dados &nbsp; [![Ir para README](https://img.shields.io/badge/Indice-Verde?style=for-the-badge)](../README.md#indice)

## Qualidade

Qualidade de dados e consistência de dados são fundamentais para o sucesso de qualquer processo de integração, análise ou tomada de decisão nas organizações. Dados de má qualidade podem gerar erros, distorções em análises e impactos nos negócios.

A qualidade de dados mede o grau em que os dados são:

- **Precisos** – refletem corretamente a realidade.
- **Completos** – sem valores em falta.
- **Consistentes** – coerentes entre diferentes fontes.
- **Atualizados** – representam o estado mais recente.
- **Únicos** – sem duplicações.

## Consistência

A Consistência de Dados é uma dimensão crítica da qualidade de dados que garante que os dados permaneçam uniformes e sem contradições em diferentes sistemas, bases de dados ou ao longo do tempo.

Em ambientes de integração de dados, a consistência assegura que a mesma informação, quando replicada ou distribuída, mantém o mesmo valor e formato em todas as suas ocorrências.

A inconsistência pode surgir de múltiplas fontes de dados, diferentes formatos de armazenamento ou regras de negócio divergentes.

## Importância da Qualidade e Consistência de Dados em Processos de Integração (ETL)

Se os dados extraídos forem de má qualidade ou inconsistentes, os resultados da transformação e do carregamento serão comprometidos, levando a análises erróneas e decisões inadequadas.

A importância pode ser resumida em:

- **Fiabilidade das Decisões**: Dados de alta qualidade fornecem uma base sólida para decisões estratégicas e operacionais.

- **Eficiência Operacional**: Reduz a necessidade de retrabalho e
  correção manual de dados, otimizando os processos.

- **Conformidade Regulatória**: Ajuda as organizações a cumprir
  regulamentos de privacidade e integridade de dados.

- **Confiança do Cliente**: Melhora a experiência do cliente através de informações precisas e personalizadas.

- **Redução de Custos**: Evita custos associados a erros, multas
  regulatórias e perda de oportunidades de negócio.

## Impacto de Dados de Má Qualidade nas Organizações

Dados de má qualidade podem ter um impacto devastador nas organizações, afetando diversas áreas.
Os problemas podem variar desde erros operacionais e ineficiências até perdas financeiras significativas e danos à reputação.

Principais impactos incluem:

- **Decisões Erradas**: Análises baseadas em dados incorretos levam a estratégias falhas.

- **Perda de Receita**: Oportunidades de vendas perdidas devido a informações incompletas ou imprecisas sobre clientes.

- **Aumento de Custos**: Gastos adicionais com a correção manual de dados, armazenamento de dados redundantes e ineficiências operacionais.

- **Insatisfação do Cliente**: Erros em faturas, comunicações ou serviços devido a dados de cliente incorretos.

- **Danos à Reputação**: Perda de confiança de clientes e parceiros devido a falhas na gestão de dados. Incapacidade de cumprir requisitos regulatórios, resultando em multas e sanções.

- **Não Conformidade**: Incapacidade de cumprir requisitos regulatórios, resultando em multas e sanções.

### Dimensões e Problemas Comuns de Qualidade

<table>
  <thead>
    <tr>
      <th>Tipo de Problema</th>
      <th>Descrição</th>
      <th>Exemplo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Dados em falta</td>
      <td>Campos nulos ou vazios</td>
      <td>email = ""</td>
    </tr>
    <tr>
      <td>Duplicidade</td>
      <td>Registos repetidos</td>
      <td>Duas linhas com o mesmo cliente</td>
    </tr>
    <tr>
      <td>Inconsistência</td>
      <td>Formatos diferentes</td>
      <td>Lisboa vs lisboa</td>
    </tr>
    <tr>
      <td>Erro de tipo</td>
      <td>Dados com tipo incorreto</td>
      <td>idade = "vinte"</td>
    </tr>
    <tr>
      <td>Valor inv lido</td>
      <td>Fora dos limites esperados</td>
      <td>idade = -5</td>
    </tr>
    <tr>
      <td>Viola o de integridade</td>
      <td>Chaves que n o existem na tabela relacionada</td>
      <td>id_cliente sem correspondência</td>
    </tr>
  </tbody>
</table>

## Dimensões da Qualidade de Dados

A qualidade dos dados não é um conceito singular, mas sim um conjunto de características ou dimensões que, em conjunto, determinam a sua adequação para um determinado propósito.

Compreender estas dimensões é crucial para avaliar, gerir e melhorar a qualidade dos dados em qualquer organização.

- Precisão (Accuracy)
- Completude (Completeness)
- Atualidade (Timeliness)
- Consistência (Consistency)
- Unicidade (Uniqueness)
- Validade (Validity)
- Relevância (Relevance)

## Problemas Comuns de Qualidade de Dados

- Dados Duplicados
- Dados Incorretos/Imprecisos
- Dados em Falta (Missing Data)
- Dados Desatualizados
- Inconsistências de Formato e Representação
- Dados Ambíguos ou Mal Interpretados
