# Tarefa 6 - Integração de dados &nbsp; [![Ir para README](https://img.shields.io/badge/Indice-Verde?style=for-the-badge)](../README.md#indice)

## Exercicio 1

```Python
import pandas as pd

# Criar DataFrame com colunas consistentes
dados = pd.DataFrame([
    {"Data": "2024-05-01", "Produto": "Teclado", "Quantidade": 10, "Preco_Unitario": 25.00},
    {"Data": "2024-05-01", "Produto": "Rato", "Quantidade": 5, "Preco_Unitario": 15.50},
    {"Data": "2024-05-02", "Produto": "Monitor", "Quantidade": 2, "Preco_Unitario": 150.00},
    {"Data": "2024-05-02", "Produto": "Webcam", "Quantidade": 8, "Preco_Unitario": 30.00},
    {"Data": "2024-05-03", "Produto": "Teclado", "Quantidade": 12, "Preco_Unitario": 25.00}
])

dados.to_csv("vendas_diarias.csv", index=False)

df = pd.read_csv("vendas_diarias.csv")

print(df.head(3))
print("\n=== Tipos de dados ===")
print(df.dtypes)

```

## Exercicio 2

```Python
import pandas as pd
import json

dados_json = [
    {"id": "P001", "nome": "Teclado", "stock": 150, "localizacao": "A1"},
    {"id": "P002", "nome": "Rato", "stock": 200, "localizacao": "A2"},
    {"id": "P003", "nome": "Monitor", "stock": 50, "localizacao": "B1"},
    {"id": "P004", "nome": "Webcam", "stock": 80, "localizacao": "B2"}
]

with open("stock_produtos.json", "w") as f:
    json.dump(dados_json, f, indent=4)

df_stock = pd.read_json("stock_produtos.json")

df_stock.to_csv("stock_limpo.csv", index=False)

print(df_stock)
```

## Exercicio 3

```Python
import pandas as pd


df = pd.read_csv("vendas_brutas.csv")

media = df["Quantidade"].mean()

media = round(media, 0)
df["Quantidade"] = df["Quantidade"].fillna(media)

df["Quantidade"] = df["Quantidade"].astype(int)

df["Valor_Total"] = df["Valor_Unitario"] * df["Quantidade"]


df_total = df.groupby("Cliente_ID", as_index=False)["Valor_Total"].sum()
df_total.rename(columns={"Valor_Total": "Total_Gasto"}, inplace=True)


df_total.to_csv("total_gasto_clientes.csv", index=False)

df.to_csv("vendas_limpo.csv", index=False)
```
