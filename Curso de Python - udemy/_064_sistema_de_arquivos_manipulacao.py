"""
Sistemas de Arquivos - Manipulação

https://docs.python.org/3/library/os.html?highlight=os#module-os
"""
import os

# Descobrindo se um arquivo ou diretório existe

# Arquivo
print(os.path.exists('arquivo.txt')) # False
print(os.path.exists('frutas.txt')) # True

# Diretório
print(os.path.exists('geek')) # True
print(os.path.exists('geek/university')) # True
print(os.path.exists('C:\\Users\\ABREU\\umjogodavelhagrandao')) # True

print()

# Criando diretórios

# OBS: A função mkdir() cria um diretório se este não existir. Caso exista, teremos FileExistsError
os.mkdir('templates')

# Utilizando makedirs podemos criar múltiplos diretórios (árvore de diretórios)
os.makedirs('templates/diretorio1/diretorio2/continua')
os.makedirs('templates/abobra')

# Renomear arquivos e diretórios

os.rename('templates/abobra', 'templates/abobrinha')
# OBS: Se o diretório não existir teremos um FileNotFoundError
# OBS: Se o diretório que queremos renomear não estiver vazio, teremos um OSError

# Vamos criar arquivos para depois excluir multiplos arquivos (no inicio do codigo).
# Criar

for i in range(10):
    open(f'templates/diretorio1/diretorio2/arquivo{i}.txt', 'w')

# ATENÇÃO! Ao remover um arquivo ou diretório este se perde, não vai para a lixeira!

# Remover arquivos e diretorios:

# os.remove()
# os.rmdir()
# os.removedirs()

# Biblioteca send2trash permite excluir arquivos, permitindo que sejam restaurados.
