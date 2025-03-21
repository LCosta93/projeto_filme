import os

# Caminho do diretório (altere para o diretório que deseja usar)
diretorio = "./create_table/"

# Nome do arquivo .bat onde os comandos serão salvos
arquivo_bat = "executar_create.bat"

# Abre o arquivo .bat para escrita
with open(arquivo_bat, "w") as bat:
    # Percorre os arquivos no diretório
    for arquivo in os.listdir(diretorio):
        # Verifica se o arquivo começa com 'create' e termina com '.py'
        if arquivo.startswith("create") and arquivo.endswith(".py"):
            # Escreve o comando para executar o arquivo Python no arquivo .bat
            bat.write(f'python "{os.path.join(diretorio, arquivo)}"\n')

print(f"Arquivo {arquivo_bat} criado com sucesso!")
