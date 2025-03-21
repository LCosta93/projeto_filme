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

# Buscar os dados de filmes da tabela filmes_imdb
query = '''
            SELECT
                id, REPLACE(stars, '"', '') as stars
            FROM filmes_imdb
            '''
cursor.execute(query)
rows_filmes = cursor.fetchall()

# Criar um dicionário para mapear stars aos seus respectivos filmes
filmes_por_star = {}
for row_filmes in rows_filmes:
    idfilme = row_filmes[0]
    stars_list = row_filmes[1].split(',')
    for star in stars_list:
        star = star.strip()
        if star not in filmes_por_star:
            filmes_por_star[star] = []
        filmes_por_star[star].append(idfilme)

# Inserir os dados na tabela filmes_stars
inserts = []
for row_stars in rows_stars:
    idstar = row_stars[0]
    stars_name = row_stars[1].replace('"', "").strip()
    if stars_name in filmes_por_star:
        for idfilme in filmes_por_star[stars_name]:
            inserts.append((idfilme, idstar))

cursor.executemany('INSERT INTO filmes_stars (idfilme, idstar) VALUES (?, ?)', inserts)

# Salvar (commit) as mudanças e fechar a conexão
conexao.commit()
conexao.close()