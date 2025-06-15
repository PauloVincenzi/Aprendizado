"""
Leitura de Arquivos

Para ler o conteúdo de um arquivo em Python, utilizamos a função integrada open(),
que literalmente significa 'abrir'.

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro de entrada, 
que neste caso é o nome do arquivo a ser lido. 
Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir,
ou então teremos o erro FileNotFoundError

mode r -> Modo de leitura. 
r -> read() -> ler

OBS: Por padrão o Python no windowns usa o encoding cp1252 ou latin1, que não lida bem com caracteres especiais
(acentos, 'til', cecidilha, etc). Assim, definimos o parâmetro encoding='utf-8' que funciona corretamente
com a maioria dos caracteres 
"""

# Exemplo

arquivo = open('texto.txt', encoding='utf-8')

print(arquivo) # <_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

print(type(arquivo)) # <class '_io.TextIOWrapper'>

print()

# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()

print(arquivo.read())
# Se tentarmos denovo usar print(arquivo.read()) -> Será retornado uma linha vazia.
# # Isso ocorre, pois o Python utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor
# é semelhante ao cursor quando estamos escrevendo (barra que fica piscando). 
# Dessa forma, após ler todo o arquivo (com o read()),
# o cursor fica no fim do arquivo, de modo que o próximo read() lê conteúdo vazio (cursor para frente).

arquivo.seek(0)

# Se colocarmos um parâmetro númerico no read(), estamos limitando a leitura até aquele caractere
print(arquivo.read(50))
