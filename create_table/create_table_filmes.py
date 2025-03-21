#importar Bibliotecas
import csv
import sqlite3


# Conectar ao banco de dados SQLite (cria o banco se não existir)
conexao = sqlite3.connect('../dados/filmes.db')
cursor = conexao.cursor()

# Criar a tabela filmes (se não existir)
cursor.execute('''
            CREATE TABLE IF NOT EXISTS filmes (
                idfilme VARCHAR(50)  PRIMARY KEY,
                Title VARCHAR(64),
                "Movie Link" VARCHAR(50),
                "Year" INTEGER,
                Duration VARCHAR(50),
                MPA VARCHAR(50),
                Rating REAL,
                Votes VARCHAR(50)
            )
''')

# Buscar os dados de filmes da tabela filmes_imdb
query = '''
            SELECT
                DISTINCT
                	ID,
                    UPPER(Title),
                    "Movie Link",
                    Year,
                    Duration,
                    MPA,
                    Rating,
                    Votes
            FROM filmes_imdb
            WHERE Title IS NOT NULL
            AND Title != ''
            '''
cursor.execute(query)
rows = cursor.fetchall()


# Deletar os dados da tabela filmes
query = 'DELETE FROM filmes'
cursor.execute(query)


# Inserir os dados na tabela filmes
for row in rows:
    row = list(row)
    # Tratamento de Dados para a coluna Duration convertendo de h m para h:mm:ss (duração do filme)
    if 'h' in row[4] and 'm' in row[4]:
        row[4] = row[4].replace('h ',':').replace('m',':00')
    elif 'h' in row[4]:
        row[4] = row[4].replace('h',':00:00')
    elif 'm' in row[4]:
        row[4] = '0:'+row[4].replace('m',':00')

    cursor.execute('INSERT INTO filmes (idfilme,Title,"Movie Link","Year",Duration,MPA,Rating,Votes) \
            VALUES \
            (?,?,?,?,?,?,?,?)', row)

conexao.commit()

# Fechar a conexão
conexao.close()
