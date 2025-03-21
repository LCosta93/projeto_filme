#importar Bibliotecas
import csv
import sqlite3

# Conectar ao banco de dados SQLite (cria o banco se não existir)
conexao = sqlite3.connect('./dados/filmes.db')
cursor = conexao.cursor()

#Buscar os dados de
query = '''
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        ORDER BY name
            '''
cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    table = row[0]
    query_count = f'''
        SELECT count(*) as count
        FROM {table}
            '''
    cursor.execute(query_count)
    row_count = cursor.fetchone()
    # formatar o número de registros
    table_count = "{:,}".format(row_count[0])
    table_count = table_count.replace(',', '.')
    print(f'{table}: { table_count} registros')

# Fechar a conexão
conexao.close()
