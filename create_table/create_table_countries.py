#importar Bibliotecas
import csv
import sqlite3


# Conectar ao banco de dados SQLite (cria o banco se não existir)
conexao = sqlite3.connect('../dados/filmes.db')
cursor = conexao.cursor()

# Criar a tabela countries (se não existir)
cursor.execute('''
        CREATE TABLE IF NOT EXISTS countries(
            idcountrie INTEGER  PRIMARY KEY,
            countrie VARCHAR(256)
        )
''')

#Buscar os dados de
# countries
#  da tabela filmes_imdb
query = '''
        SELECT
            DISTINCT countries_origin
        FROM filmes_imdb
        WHERE countries_origin IS NOT NULL
        AND countries_origin != ''
            '''
cursor.execute(query)
rows = cursor.fetchall()
# Criar um dicionário para armazenar os dados únicos de countries

countries = {}
for row in rows:
    linha = row[0].replace('[', '').replace(']', '').replace("'",'')
    if ',' in linha:
        # Dividindo a variável usando '||' como delimitador
        lista_row = linha.split(",")
        for item_lista in lista_row:
            countries[item_lista] = item_lista
    else:
        countries[linha] = linha

# Deletar os dados da tabela countries
query = 'DELETE FROM countries'
cursor.execute(query)

# Inserir os dados na tabela countries
i = 1
for countries_name in countries:
    query = f'''INSERT INTO countries (idcountrie,countrie)
                VALUES
                ({i},'{countries_name.strip()}');'''
    cursor.execute(query)
    i += 1
conexao.commit()

# Fechar a conexão
conexao.close()
