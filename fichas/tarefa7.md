# Tarefa 7 - ETL com Python &nbsp; [![Ir para README](https://img.shields.io/badge/Indice-Verde?style=for-the-badge)](../README.md#indice)

## Exercício 1

```python
import requests
import pandas as pd

API_URL = "https://jsonplaceholder.typicode.com/users"


def extract_users_data(api_url):
    try:

        response = requests.get(API_URL)
        response.raise_for_status()
        users_data = response.json()

        # Convert to DataFrame

        data = []
        for user in users_data:
            data.append({
                'name': user['name'],
                'email': user['email'],
                'address.city': user['address']['city']
            })
        df = pd.DataFrame(data)
        return df


    except requests.exceptions.RequestException as e:
        print(f"Erro na Extração da API: {e}")

    except Exception as e:
        print(f"Ocurreu um erro: {e}")


df = extract_users_data(API_URL)

if not df.empty:
    print("\nCSV gerado com sucesso!")
    df.to_csv('users_data.csv', index=False)

else:
    print("\nNão foi possivel gerar o CSV.")
```

## Exercício 2

```python
import re
import requests
import pandas as pd

API_URL = "https://jsonplaceholder.typicode.com/comments"

def extract_and_clean_comments(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        comments_data = response.json()



        # Extract all data into a list of dictionaries
        all_comments_data = []
        for comment in comments_data:
            all_comments_data.append({
                'name': comment['name'],
                'email': comment['email'],
                'body': comment['body']
            })

        # Create DataFrame from all data
        df = pd.DataFrame(all_comments_data)

        # Regex for email validation
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        # Filter DataFrame based on email regex
        df_cleaned = df[df['email'].str.match(email_regex)]

        return df_cleaned

    except requests.exceptions.RequestException as e:
        print(f"Erro na Extração da API: {e}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None

df_cleaned_comments = extract_and_clean_comments(API_URL)

if not df_cleaned_comments.empty:
    print("\nCSV gerado com sucesso!")
    df_cleaned_comments.to_csv('comentarios_limpos.csv', index=False)
else:
    print("\nNão foi possivel gerar o CSV.")
```

## Exercício 3

```python
import requests
import pandas as pd

USERS_API_URL = "https://jsonplaceholder.typicode.com/users"
TODOS_API_URL = "https://jsonplaceholder.typicode.com/todos"

def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro na Extração da API: {e}")
        return None

users_data = fetch_data(USERS_API_URL)
todos_data = fetch_data(TODOS_API_URL)

if users_data and todos_data:
    users_df = pd.DataFrame(users_data)
    todos_df = pd.DataFrame(todos_data)

    merged_df = pd.merge(users_df, todos_df, left_on='id', right_on='userId')

    completed_todos_df = merged_df[merged_df['completed'] == True]

    completed_todos_per_user = completed_todos_df.groupby('name')['completed'].count().reset_index()
    completed_todos_per_user.rename(columns={'completed': 'completed_todos_count'}, inplace=True)

    completed_todos_per_user.to_csv('tarefas_por_utilizador.csv', index=False)

    print("\nCSV gerado com sucesso!")
else:
    print("\nNão foi possivel gerar o CSV.")
```

## Exercício 4

```python
import requests
import pandas as pd
import sqlite3

API_URL = "https://fakestoreapi.com/products"

def etl_process(api_url):
    try:
        # Extract
        response = requests.get(api_url)
        response.raise_for_status()
        products_data = response.json()
        df = pd.DataFrame(products_data)

        df['rating_rate'] = df['rating'].apply(lambda x: x['rate'])
        df['rating_count'] = df['rating'].apply(lambda x: x['count'])
        df = df.drop(columns=['rating'])

        # Salvar CSV original
        df.to_csv('produtos_novos.csv', index=False)
        print("\nCSV original gerado com sucesso!")

        # Transform
        df_cleaned = df[df['price'] > 0].copy()
        df_cleaned['preco_com_iva'] = df_cleaned['price'] * 1.23

        # Load
        conn = sqlite3.connect('produtos.db')
        df_cleaned.to_sql('produtos', conn, if_exists='replace', index=False)
        conn.close()
        print("\nDados inseridos na base de dados com sucesso!")

    except requests.exceptions.RequestException as e:
        print(f"Erro na Extração da API: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

etl_process(API_URL)
```

## Exercício 5

```python

import requests
import pandas as pd
import matplotlib.pyplot as plt
import json

API_URL = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&count=10"

def process_apod_data(api_url):
    try:
        # # Extract from API (commented out)
        # response = requests.get(api_url)
        # response.raise_for_status()
        # apod_data = response.json()
        # df = pd.DataFrame(apod_data)

        # Extract from JSON file
        with open('nasa.json', 'r', encoding='utf-8') as f:
            apod_data = json.load(f)
        df = pd.DataFrame(apod_data)

        # Filter for media_type == 'image'
        df = df[df['media_type'] == 'image'].copy()

        # Transform
        df['date'] = pd.to_datetime(df['date'])
        df['month'] = df['date'].dt.month

        photos_per_month = df.groupby('month').size().reset_index(name='count')

        # Create chart
        plt.figure(figsize=(10, 6))
        plt.bar(photos_per_month['month'], photos_per_month['count'])
        plt.xlabel("Mês")
        plt.ylabel("Number of Photos")
        plt.title("Número de Fotos por Mês")
        plt.xticks(photos_per_month['month'])
        plt.grid(axis='y', linestyle='--')
        plt.savefig('fotos_por_mes.png')
        print("\nGráfico gerado com sucesso! Salvo como photos_per_month.png")

        # Save data to table
        df_to_save = df[['date', 'title', 'url']]
        print("\nAPOD Data:")
        print(df_to_save)

    except requests.exceptions.RequestException as e:
        print(f"Erro na Extração da API: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

process_apod_data(API_URL)
```
