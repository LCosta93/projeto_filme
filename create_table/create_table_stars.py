#importar Bibliotecas
import csv
import sqlite3


# Conectar ao banco de dados SQLite (cria o banco se não existir)
conexao = sqlite3.connect('../dados/filmes.db')
cursor = conexao.cursor()

# Criar a tabela stars (se não existir)
cursor.execute('''
        CREATE TABLE IF NOT EXISTS stars(
            idstar INTEGER  PRIMARY KEY,
            star VARCHAR(256)
        )
''')

#Buscar os dados de
# stars
#  da tabela filmes_imdb
query = '''
        SELECT
            DISTINCT stars
        FROM filmes_imdb
        WHERE stars IS NOT NULL
        AND stars != ''
            '''
cursor.execute(query)
rows = cursor.fetchall()
# Criar um dicionário para armazenar os dados únicos de stars

stars = {}
for row in rows:
    linha = row[0].replace('[', '').replace(']', '').replace("'",'')
    if ',' in linha:
        # Dividindo a variável usando '||' como delimitador
        lista_row = linha.split(",")
        for item_lista in lista_row:
            stars[item_lista] = item_lista
    else:
        stars[linha] = linha

# Deletar os dados da tabela stars
query = 'DELETE FROM stars'
cursor.execute(query)

# Inserir os dados na tabela stars
i = 1
for stars_name in stars:
    query = f'''INSERT INTO stars (idstar,star)
                VALUES
                ({i},'{stars_name.strip()}');'''
    cursor.execute(query)
    i += 1
conexao.commit()

# Fechar a conexão
conexao.close()
