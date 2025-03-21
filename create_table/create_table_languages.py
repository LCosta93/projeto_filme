#importar Bibliotecas
import csv
import sqlite3


# Conectar ao banco de dados SQLite (cria o banco se não existir)
conexao = sqlite3.connect('../dados/filmes.db')
cursor = conexao.cursor()

# Criar a tabela languages (se não existir)
cursor.execute('''
        CREATE TABLE IF NOT EXISTS languages(
            idlanguage INTEGER  PRIMARY KEY,
            language VARCHAR(256)
        )
''')

#Buscar os dados de
# languages
#  da tabela filmes_imdb
query = '''
        SELECT
            DISTINCT languages
        FROM filmes_imdb
        WHERE languages IS NOT NULL
        AND languages != ''
            '''
cursor.execute(query)
rows = cursor.fetchall()
# Criar um dicionário para armazenar os dados únicos de languages

languages = {}
for row in rows:
    linha = row[0].replace('[', '').replace(']', '').replace("'",'')
    if ',' in linha:
        # Dividindo a variável usando '||' como delimitador
        lista_row = linha.split(",")
        for item_lista in lista_row:
            languages[item_lista] = item_lista
    else:
        languages[linha] = linha

# Deletar os dados da tabela languages
query = 'DELETE FROM languages'
cursor.execute(query)

# Inserir os dados na tabela languages
i = 1
for languages_name in languages:
    query = f'''INSERT INTO languages (idlanguage,language)
                VALUES
                ({i},'{languages_name.strip()}');'''
    cursor.execute(query)
    i += 1
conexao.commit()

# Fechar a conexão
conexao.close()
