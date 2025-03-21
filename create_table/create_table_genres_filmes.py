#importar Bibliotecas
import csv
import sqlite3


# Conectar ao banco de dados SQLite (cria o banco se não existir)
conexao = sqlite3.connect('../dados/filmes.db')
cursor = conexao.cursor()

# Criar a tabela genres (se não existir)
cursor.execute('''
            CREATE TABLE IF NOT EXISTS filmes_genres(
	            idfilme VARCHAR(50),
	            idgenre INTEGER,
                FOREIGN KEY (idfilme) REFERENCES filmes(idfilme),
                FOREIGN KEY (idgenre) REFERENCES genres(idgenre)
            )
''')

## Deletar os dados da tabela filmes_genres
query = 'DELETE FROM filmes_genres'
cursor.execute(query)

# Buscar os dados de genres da tabela genres
query = '''
            SELECT
                idgenre, genre
            FROM genres
            '''
cursor.execute(query)
rows_genres = cursor.fetchall()

# Criar um dicionário para armazenar os dados únicos de genres
genres = {}
for row_genres in rows_genres:
    idgenre = row_genres[0]
    genres_name = row_genres[1]
    query = f'''
            SELECT
                id
            FROM filmes_imdb
            WHERE genres LIKE "%'{genres_name}'%"
            '''
    cursor.execute(query)
    rows_filmes = cursor.fetchall()
    for row_filmes in rows_filmes:
        idfilme = row_filmes[0]
        query = f'''INSERT INTO filmes_genres (idfilme,idgenre) VALUES ('{idfilme}',{idgenre});'''
        cursor.execute(query)

    conexao.commit()










# Fechar a conexão
conexao.close()
