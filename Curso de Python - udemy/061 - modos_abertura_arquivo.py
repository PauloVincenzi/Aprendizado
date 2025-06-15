"""
Modos de Abertura de Arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - cria o arquivo ou sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FileExistsError
a -> Abre para escrita, adicionando o conteúdo ao final do arquivo.
+ -> Abre para o modo de atualização: Leitura e escrita.

OBS: Abrindo no modo 'a' -> se o arquivo não existir, será criado. Caso exista, o novo conteúdo será adicionado ao final (sempre).
"""

with open('frutas.txt', 'a', encoding='utf-8') as arquivo:
    fruta = str()
    while fruta != 'sair':
        fruta = input("Digite uma fruta ou 'sair': ")
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
