#importar Bibliotecas
import csv
import sqlite3


# Conectar ao banco de dados SQLite (cria o banco se não existir)
conexao = sqlite3.connect('../dados/filmes.db')
cursor = conexao.cursor()

# Criar a tabela directors (se não existir)
cursor.execute('''
            CREATE TABLE IF NOT EXISTS filmes_directors(
	            idfilme VARCHAR(50),
	            iddirector INTEGER,
                FOREIGN KEY (idfilme) REFERENCES filmes(idfilme),
                FOREIGN KEY (iddirector) REFERENCES directors(iddirector)
            )
''')

## Deletar os dados da tabela filmes_directors
query = 'DELETE FROM filmes_directors'
cursor.execute(query)

# Buscar os dados de directors da tabela directors
query = '''
            SELECT
                iddirector, director
            FROM directors
            '''
cursor.execute(query)
rows_directors = cursor.fetchall()

# Criar um dicionário para armazenar os dados únicos de directors
directors = {}
for row_directors in rows_directors:
    iddirector = row_directors[0]
    directors_name = row_directors[1].replace('"', "") # Remove aspas duplas do nome do director
    query = f'''
            SELECT
                id, {iddirector} iddirector
            FROM filmes_imdb
            WHERE directors LIKE "%'{directors_name}'%"
            '''
    cursor.execute(query)
    rows_filmes = cursor.fetchall()
    for row_filmes in rows_filmes:
        idfilme = row_filmes[0]
        iddirector = row_filmes[1]
        query = f'''INSERT INTO filmes_directors (idfilme,iddirector) \
                    VALUES
                    ('{idfilme}',{iddirector});'''
        cursor.execute(query)
    conexao.commit()

# Fechar a conexão
conexao.close()