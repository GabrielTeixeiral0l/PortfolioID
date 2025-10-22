import pandas as pd

# leitura dos ficheiros
clientes = pd.read_csv("clientes.csv")
vendas = pd.read_csv("vendas.csv")

# eliminação de duplicados
clientes = clientes.drop_duplicates(subset=["nome", "email"])

# eliminação de linhas com valores nulos
clientes["email"] = clientes["email"].fillna("email_desconhecido")

# eliminação de espaços em branco
clientes["nome"] = clientes["nome"].fillna("nome_desconhecido")
clientes["email"] = clientes["email"].fillna("email_desconhecido")

# eliminar clientes sem id
clientes = clientes.dropna(subset=["id_cliente"])

# verificação do email
clientes.loc[~clientes["email"].str.contains("@", na=False), "email"] = "email_desconhecido"

# verificação da idade
def verificar_idade(idade):
    if pd.notnull(idade) and (18 <= idade <= 120):
        return idade
    else:
        return None

clientes["idade"] = clientes["idade"].apply(verificar_idade)

# integridade referencial
clientes = clientes[clientes["id_cliente"].isin(vendas["id_cliente"])]

clientes.to_csv("clientes_final.csv", index=False)

clientes_final = pd.read_csv("clientes_final.csv")

# integridade referencial
vendas_validas = vendas[vendas["id_cliente"].isin(clientes_final["id_cliente"])]

# eliminar vendas sem id
vendas_validas = vendas_validas.dropna(subset=["id_venda"])

# total de vendas válidas (contar linhas)
total_vendas_validas = vendas_validas["valor"].count()

print(f"Total de vendas válidas: {total_vendas_validas}")

vendas_validas.to_csv("vendas_validas.csv", index=False)
