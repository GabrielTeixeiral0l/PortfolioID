# Técnicas de Validação de Dados &nbsp; [![Ir para README](https://img.shields.io/badge/Indice-Verde?style=for-the-badge)](../README.md#indice)

A validação de dados é um processo crucial para garantir que os dados que entram ou são processados num sistema cumprem regras predefinidas, assegurando a sua **qualidade e integridade**.  
Previne erros e inconsistências que podem comprometer a fiabilidade da informação.  
As técnicas podem ser aplicadas em várias fases do ciclo de vida dos dados — desde a entrada até à integração.

---

## Definição de Regras de Validação

As **regras de validação** são critérios que os dados devem satisfazer para serem considerados válidos.  
Derivam dos requisitos de negócio e especificações do sistema.

**Exemplos:**

- Simples: `idade` deve ser um número inteiro.
- Complexa: `data_fim` deve ser posterior a `data_início`.

A definição clara destas regras é o ponto de partida de qualquer processo de validação eficaz.

---

## Restrições de Integridade (Integrity Constraints)

As bases de dados relacionais incluem mecanismos que asseguram a qualidade e consistência dos dados através de **restrições de integridade**, definidas ao nível do esquema da base de dados.

### Tipos de Restrições

- **Primary Key:** garante unicidade e não nulidade.
- **Foreign Key:** assegura integridade referencial entre tabelas.
- **UNIQUE:** valores distintos numa coluna.
- **NOT NULL:** impede valores nulos.
- **CHECK:** define condições a satisfazer (ex: `idade > 0`).

---

## Validação de Formato (Expressões Regulares)

Verifica se os dados seguem um **padrão específico** — útil para e-mails, telefones, códigos postais, NIF, etc.  
As **expressões regulares (regex)** permitem definir e aplicar estas regras.

**Exemplo de regex para e-mail:**
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$

---

## Validação de Tipo e Intervalo

### Tipo de Dados:

Confirma se o tipo de dado é o esperado (ex: números, datas válidas, etc.).  
Embora os SGBD já imponham restrições, é importante validar também nas interfaces e ingestão de dados.

### Intervalo:

Verifica se o valor está dentro de um intervalo aceitável.  
Exemplo: idade ∈ [0,120]; data de encomenda ≤ data atual.

---

## Validação Cruzada (Cross-field Validation)

Garante **consistência entre múltiplos campos**.

**Exemplos:**

- Se “Estado Civil” = “Casado”, então “Nome do Cônjuge” ≠ vazio.
- “Data de Fim” > “Data de Início”.
- Soma de colunas = total especificado.

---

## Data Profiling

Processo de **análise e descoberta de padrões e anomalias** nos dados.  
Permite recolher estatísticas e compreender estrutura, conteúdo e qualidade antes de aplicar regras formais.

### Revela:

- Distribuição de valores
- Valores únicos/distintos
- Mínimos, máximos, médias
- Percentagem de nulos
- Formatos inconsistentes
- Dependências entre colunas

---

## Limpeza e Transformação de Dados (Data Cleansing/Scrubbing)

Processo de deteção e correção (ou remoção) de registos **incorretos, corrompidos, duplicados ou incompletos**.  
Melhora a qualidade e adequação dos dados antes da análise.

Parte integrante da fase de **Transformação** no processo ETL.

---

## Identificação e Tratamento de Duplicados

Os duplicados distorcem análises e relatórios.

### Etapas:

- **Identificação:** algoritmos exatos ou difusos.
- **Remoção:** manter apenas o registo mais completo.
- **Fusão:** combinar registos.
- **Marcação:** identificar duplicados sem remoção imediata.

---

## Correção de Erros e Inconsistências

### Métodos:

- **Manual:** para pequenos volumes ou casos complexos.
- **Automático:** aplicação de regras (ex: correção ortográfica, padronização de códigos).
- **Comparação com Fontes Externas:** validação com bases de dados de referência (endereços, países, etc.).

---

## Normalização e Padronização de Dados

Visa garantir **formato uniforme** e **consistência**.

### Exemplos:

- Datas → AAAA-MM-DD
- Valores → “Masc.” e “M” → “Masculino”
- Texto → minúsculas/maiúsculas uniformes, sem caracteres especiais

---

## Tratamento de Valores em Falta (Imputation Techniques)

Valores em falta comprometem análises e modelos.

### Estratégias:

- **Remoção:** eliminar registos com muitos nulos.
- **Imputação por Constante:** preencher com média, mediana ou “Desconhecido”.
- **Imputação por Modelos:** usar regressão ou _k-NN_.
- **Imputação Temporal:** usar valor anterior ou posterior.

---

## Monitorização e Relatórios de Qualidade

A qualidade dos dados requer **monitorização contínua** e relatórios regulares (Data Quality Management – DQM).  
Visa garantir manutenção e deteção proativa de novos problemas.

---

## Métricas de Qualidade de Dados

Avaliam dimensões como **precisão, completude, atualidade, consistência, unicidade e validade**.

### Exemplos:

- **Completude:** % de campos preenchidos.
- **Unicidade:** % de registos únicos.
- **Validade:** % que cumpre regras de validação.
- **Consistência:** correspondência entre sistemas.
- **Atualidade:** frequência de atualização.
- **Erros por Categoria:** nº de códigos postais inválidos, etc.

---

## Dashboards e Relatórios de Qualidade

Ferramentas visuais para comunicar o estado da qualidade dos dados.

### Boas Práticas:

- Gráficos e KPIs claros.
- Atualizações regulares (diárias, semanais, mensais).
- Drill-down para análise detalhada.
- Alertas automáticos.
- Contextualização com impacto nos processos de negócio.

---

## Processos de Auditoria de Dados

Auditorias de dados avaliam de forma **sistemática e independente** a qualidade e conformidade dos dados com as políticas internas.

### Objetivos:

- Verificar conformidade com políticas e regulamentos.
- Identificar riscos (financeiros, operacionais, reputacionais).
- Avaliar eficácia da DQM.
- Propor melhorias e ações preventivas.
