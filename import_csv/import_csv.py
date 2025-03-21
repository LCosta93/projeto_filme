#importar Bibliotecas
import csv
import sqlite3


# Conectar ao banco de dados SQLite (cria o banco se não existir)
conexao = sqlite3.connect('../dados/filmes.db')
cursor = conexao.cursor()

# Criar a tabela (se não existir)
cursor.execute('''
CREATE TABLE IF NOT EXISTS filmes_imdb (
	id VARCHAR(50),
	Title VARCHAR(64),
	"Movie Link" VARCHAR(50),
	"Year" INTEGER,
	Duration VARCHAR(50),
	MPA VARCHAR(50),
	Rating REAL,
	Votes VARCHAR(50),
	budget REAL,
	grossWorldWide REAL,
	gross_US_Canada REAL,
	opening_weekend_Gross REAL,
	directors VARCHAR(64),
	writers VARCHAR(64),
	stars VARCHAR(128),
	genres VARCHAR(256),
	countries_origin VARCHAR(50),
	filming_locations VARCHAR(128),
	production_companies VARCHAR(128),
	Languages VARCHAR(64),
	wins INTEGER,
	nominations INTEGER,
	oscars INTEGER
)
''')


#importar arquivo csv
nome_arquivo = '../csv/final_dataset.csv'


# Abrir o arquivo CSV e ler os dados
with open(nome_arquivo, mode='r', encoding='utf-8',newline='') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=',')
    next(leitor_csv)  # Pular o cabeçalho
    for linha in leitor_csv:
        cursor.execute('INSERT INTO filmes_imdb (id,Title,"Movie Link","Year",Duration,MPA,Rating,Votes,budget,grossWorldWide,gross_US_Canada,opening_weekend_Gross,directors,writers,stars,genres,countries_origin,filming_locations,production_companies,Languages,wins,nominations,oscars)\
                       VALUES \
                       (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', linha)

# Salvar (commit) as mudanças e fechar a conexão
conexao.commit()
conexao.close()
