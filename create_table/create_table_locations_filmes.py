#importar Bibliotecas
import csv
import sqlite3


# Conectar ao banco de dados SQLite (cria o banco se não existir)
conexao = sqlite3.connect('../dados/filmes.db')
cursor = conexao.cursor()

# Criar a tabela locations (se não existir)
cursor.execute('''
            CREATE TABLE IF NOT EXISTS filmes_locations(
	            idfilme VARCHAR(50),
	            idlocation INTEGER,
                FOREIGN KEY (idfilme) REFERENCES filmes(idfilme),
                FOREIGN KEY (idlocation) REFERENCES locations(idlocation)
            )
''')

## Deletar os dados da tabela filmes_locations
query = 'DELETE FROM filmes_locations'
cursor.execute(query)

# Buscar os dados de locations da tabela locations
query = '''
            SELECT
                idlocation, location
            FROM locations
            '''
cursor.execute(query)
rows_locations = cursor.fetchall()

# Criar um dicionário para armazenar os dados únicos de locations
locations = {}
for row_locations in rows_locations:
    idlocation = row_locations[0]
    locations_name = row_locations[1].replace('"', "") # Remove aspas duplas do nome do location
    query = f'''
            SELECT
                id, {idlocation} idlocation
            FROM filmes_imdb
            WHERE filming_locations LIKE "%'{locations_name}'%"
            '''
    cursor.execute(query)
    rows_filmes = cursor.fetchall()
    for row_filmes in rows_filmes:
        idfilme = row_filmes[0]
        idlocation = row_filmes[1]
        query = f'''INSERT INTO filmes_locations (idfilme,idlocation) \
                    VALUES
                    ('{idfilme}',{idlocation});'''
        cursor.execute(query)

    conexao.commit()

# Fechar a conexão
conexao.close()