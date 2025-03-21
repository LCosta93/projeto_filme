import pandas as pd
import sqlite3

# Ler o arquivo CSV usando pandas
nome_arquivo = '../csv/final_dataset.csv'
df = pd.read_csv(nome_arquivo, delimiter=',', encoding='utf-8')

# Conectar ao banco de dados SQLite (ou criar se não existir)
conn = sqlite3.connect('../dados/filmes.db')

# Salvar o DataFrame no banco de dados SQLite
df.to_sql('filmes_imdb_pd', conn, if_exists='replace', index=False)

# Fechar a conexão
conn.close()

print("Dados importados com sucesso para o banco de dados SQLite.")