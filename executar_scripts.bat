@echo off
REM Caminho do diretório com os arquivos Python
set "diretorio=./create_table/"

REM Navega até o diretório
cd /d "%diretorio%"

REM Lista todos os arquivos que começam com "create" e terminam com ".py"
for %%f in (create*.py) do (
    echo --------------------------------------------
    echo Executando arquivo: %%f
    echo Inicio: %date% %time%
    python "%%f"
    echo --------------------------------------------
)
pause
