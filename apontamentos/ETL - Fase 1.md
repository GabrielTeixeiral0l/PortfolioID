# ETL - Fase 1 (Extract) &nbsp; [![Ir para README](https://img.shields.io/badge/Indice-Verde?style=for-the-badge)](../README.md#indice)

A primeira fase do ETL consiste em recolher ou extrair os dados das
suas fontes de origem. As fontes de dados podem ser extremamente
variadas e heterogéneas, incluindo:

<ul>
  <li>Bancos de dados relacionais (SQL Server, Oracle, MySQL).</li>
  <li>Bancos de dados NoSQL (MongoDB, Cassandra).</li>
  <li>Sistemas empresariais como ERPs e CRMs.</li>
  <li>Ficheiros planos (CSV, JSON, XML).</li>
  <li>APIs de servi os web.</li>
  <li>Sensores de dispositivos IoT.</li>
</ul>

Os dados extraídos são geralmente movidos para uma área de preparação (staging area), que é um repositório intermédio onde os dados são armazenados temporariamente antes de serem transformados.

## Métodos de Extração

### Carga Completa (Full Load)

A carga completa (Full Load) consiste em recolher todos os dados da
fonte de uma só vez. Este método é mais simples, mas pode ser
impraticável para grandes volumes de dados.

### Carga Incremental (Incremental Load)

A carga incremental (Incremental Load) consiste em recolher
apenas os dados novos ou modificados desde a última extração.
Este método é mais eficiente, pois reduz o volume de dados
transferidos e o tempo de processamento.

```Python
import sqlite3
import pandas as pd

conn = sqlite3.connect("base_dados.db")

clientes = pd.read_sql("SELECT * FROM cliente", conn)

print(clientes.head())

conn.close()
```
