"""
Este arquivo serve como módulo.
Ao tentar puxar um dos outros arquivos python começados por número, da erro.

Ex:
from 025_funcoes_com_parametro import soma_impares()

-> ERRO
"""

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28), ('Londres', 22)]


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))
else:
    print('O módulo arquivo_teste.py foi importado') 
