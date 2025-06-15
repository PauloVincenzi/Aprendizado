"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemo lê-lo, somente escrever.

# OBS: Ao abrir um arquivo para escrita, se o arquivo não existir, ele é criado no sistema operacional.
Casp o arquivo exista, seu conteúdo será modificado, perdendo todo o conteúdo antes da abertura com 'w'.

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parâmetro, caso contrário teremos um TypeError.
"""

# Exemplo de escrita - modo 'w' - write (escrita)

with open('escrita.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Esta é a última linha.')

with open('frutas.txt', 'w', encoding='utf-8') as arquivo:
    fruta = str()
    while fruta != 'sair':
        fruta = input("Digite uma fruta ou 'sair': ")
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
