"""
Criando sua própria versão de loop
"""

def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

numeros = [1, 2, 3, 4, 5]
palavra = 'Cebola'

print('-'*50)
meu_for(numeros)
print('-'*50)
meu_for(palavra)
print('-'*50)
