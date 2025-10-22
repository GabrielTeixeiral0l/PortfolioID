# Tarefa 4 - Integração de dados &nbsp; [![Ir para README](https://img.shields.io/badge/Indice-Verde?style=for-the-badge)](../README.md#indice)

1.

-5; None; 122

2.

Devemos investigar se é o mesmo utilizador, se for unir os dados em apenas um registo.

3.

Email e Idade com dados em falta (Dados em falta)

cliente id 101 duplicado em 105 (Duplicação)

A cidade no id 107 está em maiusculo, enquanto nos restantes registos está apenas a primeira letra (Inconsistência)

Data de nascimento no futuro no registo 104 (Valor inválido)

Idade impossível no registo 103 (Valor inválido)

4.

```SQL
CREATE TABLE Produtos (
ProdutoID INT PRIMARY KEY NOT NULL,
NomeProduto VARCHAR(255) NOT NULL,
Preco DECIMAL(10,2) NOT NULL CHECK (Preco > 0),
Stock INT NOT NULL CHECK (Stock >= 0),
DataValidade DATE CHECK (DataValidade > CURRENT_DATE)
);
```

5.

```Python
import pandas as pd


vendas = pd.read_csv("vendas.csv")


vendas = vendas.drop_duplicates(subset=["Produto", "Quantidade", "Preco_Unitario", "Data_Venda", "Cliente_Email"])


vendas["Cliente_Email"] = vendas["Cliente_Email"].fillna("desconhecido@dominio.com")


vendas.loc[vendas["Quantidade"] <= 0, "Quantidade"] = 1


vendas["Produto"] = vendas["Produto"].str.title()


vendas.to_csv("vendas_corrigido.csv", index=False)
```
