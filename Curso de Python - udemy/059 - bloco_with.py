"""
O bloco with

Aprendemos que os passos para se trabalhar com arquivos:
 1 - Abrir o arquivo;
 2 - Trabalhar o arquivo;
 3 - Fechar o arquivo;

 O block with é utilizado para criar um contexto de trabalho onde a abertura e fechamentoos dos recursos
 utilizados são fechados automaeticamente após o bloco with.
"""

# O block with - Forma Pythônica de manipular arquivos

with open('texto.txt') as arquivo:
    print(arquivo.closed) # False -> Está aberto
    print(arquivo.readlines())

print(arquivo.closed) # True -> Está fechado
