#importar Bibliotecas
import csv
import sqlite3


# Conectar ao banco de dados SQLite (cria o banco se não existir)
conexao = sqlite3.connect('../dados/filmes.db')
cursor = conexao.cursor()

# Criar a tabela stars (se não existir)
cursor.execute('''
            CREATE TABLE IF NOT EXISTS filmes_stars(
	            idfilme VARCHAR(50),
	            idstar INTEGER,
                FOREIGN KEY (idfilme) REFERENCES filmes(idfilme),
                FOREIGN KEY (idstar) REFERENCES stars(idstar)
            )
''')

## Deletar os dados da tabela filmes_stars
query = 'DELETE FROM filmes_stars'
cursor.execute(query)

# Buscar os dados de stars da tabela stars
query = '''
            SELECT
                idstar, star
            FROM stars
            '''
cursor.execute(query)
rows_stars = cursor.fetchall()

# Criar um dicionário para armazenar os dados únicos de stars
stars = {}
for row_stars in rows_stars:
    idstar = row_stars[0]
    stars_name = row_stars[1].replace('"', "") # Remove aspas duplas do nome do star
    query = f'''
            SELECT
                id, {idstar} idstar
            FROM filmes_imdb
            WHERE stars LIKE "%'{stars_name}'%"
            '''
    cursor.execute(query)
    rows_filmes = cursor.fetchall()
    for row_filmes in rows_filmes:
        idfilme = row_filmes[0]
        idstar = row_filmes[1]
        query = f'''INSERT INTO filmes_stars (idfilme,idstar) \
                    VALUES
                    ('{idfilme}',{idstar});'''
        cursor.execute(query)

    conexao.commit()

# Fechar a conexão
conexao.close()