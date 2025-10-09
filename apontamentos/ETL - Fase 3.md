# ETL - Fase 3 (Load) &nbsp; [![Ir para README](https://img.shields.io/badge/Indice-Verde?style=for-the-badge)](../README.md#indice)

<p>
A fase final consiste em carregar os dados transformados para o sistema de destino final.
</p>

<ul>
  <li><strong>Sistemas de Destino Comuns:</strong>
    <ul>
      <li>Data Warehouse (DW): Um repositório central de dados estruturados, otimizado para consulta e análise.</li>
      <li>Data Lake: Um repositório que armazena grandes volumes de dados brutos, tanto estruturados como não estruturados.</li>
    </ul>
  </li>
</ul>

<h3>Métodos de Carga</h3>

<ul>
  <li><strong>Carga Completa (Full Load):</strong> também conhecida como "destrutiva", apaga todos os dados existentes na tabela de destino e insere o novo conjunto de dados. É usada para tabelas pequenas ou quando os dados históricos não precisam de ser mantidos.</li>
  <li><strong>Carga Incremental (Incremental Load):</strong> adicionar novos registros (append) ou atualizar registros existentes (update/insert) no destino. Este método é mais comum em Data Warehouses para preservar o histórico e otimizar o desempenho.</li>
</ul>
