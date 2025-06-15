"""
Seek e cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo.

OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco
do computador e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhos
com o arquivo devemos fechar essa conexão. Para isso utilizamos a função close()

Passos para se trabalhar com um arquivo:
 1 - Abrir o arquivo;
 2 - Trabalhar o arquivo;
 3 - Fechar o arquivo;
"""

arquivo = open('texto.txt', encoding='utf-8')

print(arquivo.read())

print('-'*100)

# O parâmetro que colocamos na função seek() indica onde queremos colocar o cursos.

# Movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(0)

print(arquivo.read())

print('-'*100)

arquivo.seek(113)

print(arquivo.read())

print('-'*100)

# readline() -> função lê o arquivo linha a linha
arquivo.seek(0)

print(arquivo.readline())
print('-'*100)
print(arquivo.readline())
print('-'*100)
print(arquivo.readline())
print('-'*100)
print(arquivo.readline())
print('-'*100)

arquivo.seek(0)

ret = arquivo.readline()

print(ret.split(' '))

print('-'*100)

# readlines()
arquivo.seek(0)

linhas = arquivo.readlines()
print(linhas)
print(f'Número de linhas no arquivo: {len(linhas)}')

# closed -> verifica se o arquivo está aberto ou fechado
print(arquivo.closed) # False

# Fechar o arquivo
arquivo.close()

print(arquivo.closed) # True
