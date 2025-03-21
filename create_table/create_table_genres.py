#importar Bibliotecas
import sqlite3
# Conectar ao banco de dados SQLite (cria o banco se não existir)
conexao = sqlite3.connect('../dados/filmes.db')
cursor = conexao.cursor()

# Criar a tabela genres (se não existir)
cursor.execute('''CREATE TABLE IF NOT EXISTS genres ( idgenre INTEGER  PRIMARY KEY, genre VARCHAR(256)) ''')

# Buscar os dados de genres da tabela filmes_imdb
query = "SELECT DISTINCT genres FROM filmes_imdb WHERE genres IS NOT NULL AND genres != '' "
cursor.execute(query)
rows = cursor.fetchall()

# Criar um dicionário para armazenar os dados únicos de genres
genres = {}
for row in rows:
    linha = row[0].replace('[', '').replace(']', '').replace("'",'')
    if ',' in linha:
        # Dividindo a variável usando '||' como delimitador
        lista_row = linha.split(",")
        for item_lista in lista_row:
            genres[item_lista] = item_lista
    else:
        genres[linha] = linha

# Deletar os dados da tabela genres
query = 'DELETE FROM genres'
cursor.execute(query)

# Inserir os dados na tabela genres
i = 1
for genres_name in genres:
    query = f'INSERT INTO genres (idgenre,genre) VALUES ({i},"{genres_name.strip()}");'
    cursor.execute(query)
    i += 1
conexao.commit()
# Fechar a conexão
conexao.close()
