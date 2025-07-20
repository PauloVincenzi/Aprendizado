"""
Dunder Name e Dunder Main

Dunder -> Double Under

Dunder Name -> __name__

Dunder Main -> __main__

Em Python, são utilizados dunder para criar funções, atributos, propriedades e etc utilizando
Double Under para não gerar conflito com os nomes desses elementos na programação.

# Na linguagem C, temos um programa da seguinte forma:

init main(){

    return 0;
}

# Na linguagem Java, temos um programa da seguinte forma:

public static void main(String[] args){

}

# Em Python, se executarmos um módulo Python diretamente na linha de comando, internamente
o Python atribuirá à variável __name__ o valor __main__ indicando que este módulo é o
módulo de execução principal.
"""

from arquivo_teste import soma_impares

print()

print(soma_impares([1, 2, 3, 4, 5])) # 9

# Olhe o 'arquivo_teste'. Sem o condicional, ao importar o arquivo, as execuções iriam rodar (prints), 
# sendo que queremos apenas a função soma_impares()

print()

import primeiro, segundo
