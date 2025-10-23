# Tarefa 5 - Integração de dados &nbsp; [![Ir para README](https://img.shields.io/badge/Indice-Verde?style=for-the-badge)](../README.md#indice)

```Python
import pandas as pd

padrao_email = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
padra_nome = r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$'

# lê ficheiros
clientes = pd.read_csv("clientes_T5.csv")
vendas = pd.read_csv("vendas_T5.csv")

# email para minúsculas e remove espaços em branco
clientes['email'] = clientes['email'].astype(str).str.lower().str.strip()

# valida email, substitui inválidos por None (para poder unir e ignorar este)
clientes.loc[~clientes['email'].str.match(padrao_email), 'email'] = None

# Juntar duplicados por id_cliente
clientes = clientes.groupby('id_cliente', as_index=False).agg({
    'nome': 'first',
    'idade': 'max',
    'email': 'first'
})

# substitui nomes ausentes por "Nome Desconhecido" e emails ausentes por "email_desconhecido"
clientes.loc[clientes['email'].isna(), 'email'] = "email_desconhecido"
clientes.loc[clientes['nome'].isna(), 'nome'] = "nome_desconhecido"

# substitui nomes inválidos por "nome_desconhecido"
clientes.loc[~clientes['nome'].str.match(padra_nome), 'nome'] = "nome_desconhecido"

# substitui idades inválidas ou ausentes com a média
media = int(round(clientes['idade'].mean(skipna=True)))
clientes['idade'] = clientes['idade'].fillna(media)

clientes.loc[(clientes['idade'] < 18) | (clientes['idade'] > 100), 'idade'] = media


# remove clientes com nome e email ausentes
clientes = clientes.loc[~((clientes['email'] == "email_desconhecido") & (clientes['nome'] == "nome_desconhecido"))]


# formata nomes e emails
clientes['nome'] = clientes['nome'].astype(str).str.strip().str.title()
clientes['email'] = clientes['email'].astype(str).str.strip().str.lower()


# Elimina vendas sem cliente associado
vendas = vendas[vendas['id_cliente'].isin(clientes['id_cliente'])]

# remove vendas com valores ausentes ou nulos
vendas = vendas.dropna(subset=['valor', 'id_cliente', 'id_venda'])

# ordena por id
clientes = clientes.sort_values(by='id_cliente')
vendas = vendas.sort_values(by='id_venda')

# guarda ficheiros
clientes.to_csv("clientes_final.csv", index=False)
vendas.to_csv("vendas_validas.csv", index=False)
```
