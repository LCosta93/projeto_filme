import pandas as pd
import duckdb

# Ler o arquivo CSV usando pandas
nome_arquivo = '../csv/final_dataset.csv'

conexao = duckdb.connect('../dados/filme_duckdb.db')

# Importando o arquivo CSV e salvando na tabela
conexao.execute(f"""
    CREATE TABLE IF NOT EXISTS filmes_imdb AS
    SELECT * FROM read_csv_auto('{nome_arquivo}');
""")

conexao.commit()

# Fechar a conexão
conexao.close()

print("Dados importados com sucesso para o banco de dados SQLite.")