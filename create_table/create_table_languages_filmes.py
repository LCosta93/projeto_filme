#importar Bibliotecas
import csv
import sqlite3


# Conectar ao banco de dados SQLite (cria o banco se não existir)
conexao = sqlite3.connect('../dados/filmes.db')
cursor = conexao.cursor()

# Criar a tabela languages (se não existir)
cursor.execute('''
            CREATE TABLE IF NOT EXISTS filmes_languages(
	            idfilme VARCHAR(50),
	            idlanguage INTEGER,
                FOREIGN KEY (idfilme) REFERENCES filmes(idfilme),
                FOREIGN KEY (idlanguage) REFERENCES languages(idlanguage)
            )
''')

## Deletar os dados da tabela filmes_languages
query = 'DELETE FROM filmes_languages'
cursor.execute(query)

# Buscar os dados de languages da tabela languages
query = '''
            SELECT
                idlanguage, language
            FROM languages
            '''
cursor.execute(query)
rows_languages = cursor.fetchall()

# Criar um dicionário para armazenar os dados únicos de languages
languages = {}
for row_languages in rows_languages:
    idlanguage = row_languages[0]
    languages_name = row_languages[1].replace('"', "") # Remove aspas duplas do nome do language
    query = f'''
            SELECT
                id, {idlanguage} idlanguage
            FROM filmes_imdb
            WHERE languages LIKE "%'{languages_name}'%"
            '''
    cursor.execute(query)
    rows_filmes = cursor.fetchall()
    for row_filmes in rows_filmes:
        idfilme = row_filmes[0]
        idlanguage = row_filmes[1]
        query = f'''INSERT INTO filmes_languages (idfilme,idlanguage) \
                    VALUES
                    ('{idfilme}',{idlanguage});'''
        cursor.execute(query)

    conexao.commit()

# Fechar a conexão
conexao.close()