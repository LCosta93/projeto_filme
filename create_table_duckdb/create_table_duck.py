#importar Bibliotecas
import csv
import duckdb
import pandas as pd

# Conecta abrindo / criando um arquivo
conexao = duckdb.connect('../dados/filme_duckdb.db')

def create_table(conexao, table_name, cabecalho, dados):
    # Converte para um DataFrame e depois para uma lista de dicionários
    df = pd.DataFrame(dados, columns=cabecalho)

    query = f'''
            CREATE TABLE IF NOT EXISTS {table_name}
            AS
            SELECT * FROM df;
            '''
    conexao.execute(query)
    conexao.commit()

# Criar um dicionário para armazenar os dados únicos de writers
def create_dict_unique(data):
    dados = {}
    i = 1
    for row in data:
        linha = row[0].replace('[', '').replace(']', '').replace("'",'')
        if ',' in linha:
            # Dividindo a variável usando '||' como delimitador
            lista_row = linha.split(",")
            for item_lista in lista_row:
                dados[i] = item_lista
            i += 1
        else:
            dados[i] = linha
            i += 1
    return dados

def get_dados_filme(conexao,coluna):
    query = f'''
            SELECT
                DISTINCT {coluna}
            FROM filmes_imdb
            WHERE {coluna} IS NOT NULL
            AND {coluna} != ''
                '''
    conexao.execute(query)
    return conexao.fetchall()

def gerar_dados(conexao,coluna,table_name,cabecalho):
    rows = get_dados_filme(conexao,coluna)
    dados = create_dict_unique(rows)
    create_table(conexao, table_name, cabecalho, dados)

coluna_filme = "writers"
table_name = "writers"
cabecalho = ["idwriter","writer"]
gerar_dados(conexao,coluna_filme,table_name,cabecalho)

coluna_filme = "countries_origin"
table_name = "countries"
cabecalho = ["idcountrie","countrie"]
gerar_dados(conexao,coluna_filme,table_name,cabecalho)

coluna_filme = "directors"
table_name = "directors"
cabecalho = ["iddirector","director"]
gerar_dados(conexao,coluna_filme,table_name,cabecalho)

coluna_filme = "genres"
table_name = "genres"
cabecalho = ["idgenre","genre"]
gerar_dados(conexao,coluna_filme,table_name,cabecalho)

coluna_filme = "languages"
table_name = "languages"
cabecalho = ["idlanguage","language"]
gerar_dados(conexao,coluna_filme,table_name,cabecalho)

coluna_filme = "filming_locations"
table_name = "locations"
cabecalho = ["idlocation","location"]
gerar_dados(conexao,coluna_filme,table_name,cabecalho)

coluna_filme = "stars"
table_name = "stars"
cabecalho = ["idstar","star"]
gerar_dados(conexao,coluna_filme,table_name,cabecalho)

coluna_filme = "writers"
table_name = "writers"
cabecalho = ["idwriter","writer"]
gerar_dados(conexao,coluna_filme,table_name,cabecalho)

conexao.commit()

# Fechar a conexão
conexao.close()
