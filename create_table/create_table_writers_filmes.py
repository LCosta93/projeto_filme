#importar Bibliotecas
import csv
import sqlite3


# Conectar ao banco de dados SQLite (cria o banco se não existir)
conexao = sqlite3.connect('../dados/filmes.db')
cursor = conexao.cursor()

# Criar a tabela writers (se não existir)
cursor.execute('''
            CREATE TABLE IF NOT EXISTS filmes_writers(
	            idfilme VARCHAR(50),
	            idwriter INTEGER,
                FOREIGN KEY (idfilme) REFERENCES filmes(idfilme),
                FOREIGN KEY (idwriter) REFERENCES writers(idwriter)
            )
''')

## Deletar os dados da tabela filmes_writers
query = 'DELETE FROM filmes_writers'
cursor.execute(query)

# Buscar os dados de writers da tabela writers
query = '''
            SELECT
                idwriter, writer
            FROM writers
            '''
cursor.execute(query)
rows_writers = cursor.fetchall()

# Criar um dicionário para armazenar os dados únicos de writers
writers = {}
for row_writers in rows_writers:
    idwriter = row_writers[0]
    writers_name = row_writers[1].replace('"', "") # Remove aspas duplas do nome do writer
    query = f'''
            SELECT
                id, {idwriter} idwriter
            FROM filmes_imdb
            WHERE writers LIKE "%'{writers_name}'%"
            '''
    cursor.execute(query)
    rows_filmes = cursor.fetchall()
    for row_filmes in rows_filmes:
        idfilme = row_filmes[0]
        idwriter = row_filmes[1]
        query = f'''INSERT INTO filmes_writers (idfilme,idwriter) \
                    VALUES
                    ('{idfilme}',{idwriter});'''
        cursor.execute(query)

    conexao.commit()

# Fechar a conexão
conexao.close()