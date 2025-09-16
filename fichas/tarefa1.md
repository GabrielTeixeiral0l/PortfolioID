# Tarefa 1 - Integração de dados &nbsp; [![Ir para README](https://img.shields.io/badge/Indice-Verde?style=for-the-badge)](../README.md#indice)

**1. Imagina que uma empresa tem três sistemas que guardam os dados dos
clientes**:

• **Empresa: Cliente_ID, Nome, NIF**

**• Cliente: ID_Cliente, NomeCompleto, NumeroContribuinte**

**• Loja Online: UserID, Nome, TaxID**

1.  **Identifica os problemas de interoperabilidade existentes.**

Os nomes dos campos são diferentes, apesar de guardarem os mesmos dados,
este problema resulta na redundância e na inconsistência dos dados.

2.  **Propõe uma tabela final integrada com campos coerentes.**

Tabela: id_cliente, nome, nif

**2. Uma empresa de marketing digital analisa o desempenho das campanhas
dos seus clientes. Para isso, recolhe dados de várias fontes:**

**• Relatórios de vendas em formato CSV.**

Estruturado, pois os dados encontram-se em forma de tabela.

**• Comentários e menções da marca em redes sociais (Twitter,
Instagram).**

Não estruturado, pois cada comentário tem a sua estrutura.

**• Vídeos promocionais da campanha.**

Não estruturado, pois não possuí um modelo fixo

**• Dados demográficos dos clientes a partir de um formulário online.**

Semi-estruturado, porque vai provavelmente ser armazenado sob a forma de
JSON.

**• Emails trocados com os clientes.**

Não estruturado, pois não possuí um modelo fixo.

**Classifique cada uma das fontes de dados como estruturada, não
estruturada ou semiestruturada e justifique a sua resposta.**

**3. Classifica cada um dos seguintes exemplos como estruturados,
semi-estruturados ou não estruturados:**

**3.1 Uma tabela Excel com notas dos alunos.**

Estruturado

**3.2 Um ficheiro JSON com informações de clientes.**

Semi-estruturado

**3.3 Um vídeo de vigilância.**

Não estruturado

**3.4 Um log de acesso ao servidor (ficheiro .log).**

Semi-estruturado

**3.5 Um contrato em PDF digitalizado.**

Não estruturado

**4. Para cada um dos cenários abaixo, escolha a arquitetura de
integração mais adequada (Batch, Streaming ou Serviços Web/APIs) e
justifique a sua escolha com base nas vantagens e desvantagens de cada
abordagem.**

**4.1 Um banco precisa de analisar as transações de cartão de crédito à
medida que acontecem para bloquear atividades suspeitas de fraude
instantaneamente.**

Streaming, pois tem baixa latência

**4.2 Uma universidade precisa de consolidar os dados de matrículas,
notas e propinas de todos os departamentos no final de cada semestre
para gerar relatórios académicos e financeiros para a administração.**

Batch, pois é fiável e ideal para grandes quantidades de dados

**4.3 Uma startup desenvolveu uma plataforma de meteorologia e quer
permitir que outras aplicações (ex: apps de agricultura, sites de
notícias) acedam às suas previsões meteorológicas em tempo real mediante
um pagamento.**

API, é flexível, escalável e reutilizável.

**5. Associa cada cenário ao tipo de arquitetura de integração mais
adequado (Batch, Streaming ou API):**

**5.1 Um hospital que precisa de consultar em tempo real o historial
clínico de um paciente noutra clínica.**

API

**5.2 Uma empresa que atualiza o seu Data Warehouse todas as noites com
vendas do dia anterior.**

Batch

**5.3 Uma aplicação que deteta e alerta instantaneamente quando um
cartão de crédito é usado de forma suspeita.**

Streaming

**5.4 Um site que, no checkout, comunica com a API da DHL para calcular
o custo de envio.**

API
