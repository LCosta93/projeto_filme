#importar Bibliotecas
import csv
import sqlite3


# Conectar ao banco de dados SQLite (cria o banco se não existir)
conexao = sqlite3.connect('../dados/filmes.db')
cursor = conexao.cursor()

# Criar a tabela countries (se não existir)
cursor.execute('''
            CREATE TABLE IF NOT EXISTS filmes_countries(
	            idfilme VARCHAR(50),
	            idcountrie INTEGER,
                FOREIGN KEY (idfilme) REFERENCES filmes(idfilme),
                FOREIGN KEY (idcountrie) REFERENCES countries(idcountrie)
            )
''')

## Deletar os dados da tabela filmes_countries
query = 'DELETE FROM filmes_countries'
cursor.execute(query)

# Buscar os dados de countries da tabela countries
query = '''
            SELECT
                idcountrie, countrie
            FROM countries
            '''
cursor.execute(query)
rows_countries = cursor.fetchall()

# Criar um dicionário para armazenar os dados únicos de countries
countries = {}
for row_countries in rows_countries:
    idcountrie = row_countries[0]
    countries_name = row_countries[1].replace('"', "") # Remove aspas duplas do nome do countrie
    query = f'''
            SELECT
                id, {idcountrie} idcountrie
            FROM filmes_imdb
            WHERE countries_origin LIKE "%'{countries_name}'%"
            '''
    cursor.execute(query)
    rows_filmes = cursor.fetchall()
    for row_filmes in rows_filmes:
        idfilme = row_filmes[0]
        idcountrie = row_filmes[1]
        query = f'''INSERT INTO filmes_countries (idfilme,idcountrie) \
                    VALUES
                    ('{idfilme}',{idcountrie});'''
        cursor.execute(query)

    conexao.commit()

# Fechar a conexão
conexao.close()