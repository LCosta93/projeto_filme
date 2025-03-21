#importar Bibliotecas
import csv
import sqlite3


# Conectar ao banco de dados SQLite (cria o banco se não existir)
conexao = sqlite3.connect('../dados/filmes.db')
cursor = conexao.cursor()

# Criar a tabela locations (se não existir)
cursor.execute('''
        CREATE TABLE IF NOT EXISTS locations(
            idlocation INTEGER  PRIMARY KEY,
            location VARCHAR(256)
        )
''')

#Buscar os dados de
# locations
#  da tabela filmes_imdb
query = '''
        SELECT
            DISTINCT filming_locations
        FROM filmes_imdb
        WHERE filming_locations IS NOT NULL
        AND filming_locations != ''
            '''
cursor.execute(query)
rows = cursor.fetchall()
# Criar um dicionário para armazenar os dados únicos de locations

locations = {}
for row in rows:
    linha = row[0].replace('[', '').replace(']', '').replace("'",'')
    if ',' in linha:
        # Dividindo a variável usando '||' como delimitador
        lista_row = linha.split(",")
        for item_lista in lista_row:
            locations[item_lista] = item_lista
    else:
        locations[linha] = linha

# Deletar os dados da tabela locations
query = 'DELETE FROM locations'
cursor.execute(query)

# Inserir os dados na tabela locations
i = 1
for locations_name in locations:
    query = f'''INSERT INTO locations (idlocation,location)
                VALUES
                ({i},'{locations_name.strip()}');'''
    cursor.execute(query)
    i += 1
conexao.commit()

# Fechar a conexão
conexao.close()
