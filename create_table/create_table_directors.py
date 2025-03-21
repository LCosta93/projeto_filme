#importar Bibliotecas
import csv
import sqlite3


# Conectar ao banco de dados SQLite (cria o banco se não existir)
conexao = sqlite3.connect('../dados/filmes.db')
cursor = conexao.cursor()

# Criar a tabela directors (se não existir)
cursor.execute('''
        CREATE TABLE IF NOT EXISTS directors(
            iddirector INTEGER  PRIMARY KEY,
            director VARCHAR(256)
        )
''')

#Buscar os dados de
# directors
#  da tabela filmes_imdb
query = '''
        SELECT
            DISTINCT directors
        FROM filmes_imdb
        WHERE directors IS NOT NULL
        AND directors != ''
            '''
cursor.execute(query)
rows = cursor.fetchall()
# Criar um dicionário para armazenar os dados únicos de directors

directors = {}
for row in rows:
    linha = row[0].replace('[', '').replace(']', '').replace("'",'')
    if ',' in linha:
        # Dividindo a variável usando '||' como delimitador
        lista_row = linha.split(",")
        for item_lista in lista_row:
            directors[item_lista] = item_lista
    else:
        directors[linha] = linha

# Deletar os dados da tabela directors
query = 'DELETE FROM directors'
cursor.execute(query)

# Inserir os dados na tabela directors
i = 1
for directors_name in directors:
    query = f'''INSERT INTO directors (iddirector,director)
                VALUES
                ({i},'{directors_name.strip()}');'''
    cursor.execute(query)
    i += 1
conexao.commit()

# Fechar a conexão
conexao.close()
