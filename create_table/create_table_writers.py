#importar Bibliotecas
import csv
import sqlite3


# Conectar ao banco de dados SQLite (cria o banco se não existir)
conexao = sqlite3.connect('../dados/filmes.db')
cursor = conexao.cursor()

# Criar a tabela writers (se não existir)
cursor.execute('''
        CREATE TABLE IF NOT EXISTS writers(
            idwriter INTEGER  PRIMARY KEY,
            writer VARCHAR(256)
        )
''')

#Buscar os dados de
# writers
#  da tabela filmes_imdb
query = '''
        SELECT
            DISTINCT writers
        FROM filmes_imdb
        WHERE writers IS NOT NULL
        AND writers != ''
            '''
cursor.execute(query)
rows = cursor.fetchall()
# Criar um dicionário para armazenar os dados únicos de writers

writers = {}
for row in rows:
    linha = row[0].replace('[', '').replace(']', '').replace("'",'')
    if ',' in linha:
        # Dividindo a variável usando '||' como delimitador
        lista_row = linha.split(",")
        for item_lista in lista_row:
            writers[item_lista] = item_lista
    else:
        writers[linha] = linha

# Deletar os dados da tabela writers
query = 'DELETE FROM writers'
cursor.execute(query)

# Inserir os dados na tabela writers
i = 1
for writers_name in writers:
    query = f'''INSERT INTO writers (idwriter,writer)
                VALUES
                ({i},'{writers_name.strip()}');'''
    cursor.execute(query)
    i += 1
conexao.commit()

# Fechar a conexão
conexao.close()
