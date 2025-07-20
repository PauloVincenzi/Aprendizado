"""
Sistema de arquivos e navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazer uso do módulo os.

os -> Operating System - Sistema Operacional

# Alguns recursos são limitados no Windows
"""

# Fazer o import
import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd())

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')
print(os.getcwd())

os.chdir('..')
print(os.getcwd())

os.chdir('..')
print(os.getcwd())

print('-'*80)

# Podemos checar se um diretório é absoluto ou relativo
# No Windows temos que usar um duplo '\'
print(os.path.isabs('C:\\Users\\paulo'))

# Podemos identificar o sistema operacional com o módulo os
print(os.name) # posix (Linux e Mac), nt (Windows)

# Podemos listar os arquivos e diretórios com o listdir()
print(os.listdir())

print('-'*80)

# Podemos fazer o mesmo com mais detalhes com scandir()

scanner = os.scandir()

arquivos = list(scanner)
print(arquivos)

print()

print(dir(arquivos))

print()

print(arquivos[0].inode()) # numeração deste objeto na árvore de diretórios
print(arquivos[0].is_dir()) # É um diretório? False
print(arquivos[0].is_file()) # É um arquivo? True
print(arquivos[0].is_symlink()) # É um link simbólico? False
print(arquivos[0].name) # Nome do arquivo
print(arquivos[0].path) # Caminho até o arquivo
print(arquivos[0].stat()) # Estatísticas sobre o arquivo (ex: nº de bits)

# OBS: Quando utilizamos a função scandir() nós precisamos fechá-la, assim quando abrimos um arquivo.

scanner.close()
