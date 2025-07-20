"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

C ou Java:

for(int i = 0; i < 10; i++){
    //execução do loop
}

Python:

for item in iteravel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplo de iteráveis:
- String
    nome = 'Paulo Eduardo'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)

nome = 'Paulo Eduardo'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

# Exemplo de for 1 (Iterando sobre uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)
for numero in range(1, 10):
    print(numero)

range(valor_inicial, valor_final)
OBS: valor final não é incluso.

# Imprimir sem pular linha
for letra in nome:
    print(letra, end='')

Enumerate:

([0, 'P'], [1, 'a'], [2, 'u'], [3, 'l'], ... [11, 'd'], [12, 'o'])

for indice, letra in enumerate(nome):
    print(nome[indice])

for i, l in enumerate(nome):
   print(l)

for _, l in enumerate(nome):
   print(l)

OBS: Quando não precisamos de uma valor, podemos descartá-lo utilizando um underline

for listas in enumerate(nome):
    print(listas)

qnt = int(input('Quantas vezes o loop vai rodar? '))
soma = 0
for c in range(1, qnt+1):
    n = int(input(f'Informe o {c}º valor: '))
    soma = soma + n
print(f'A soma deu {soma}')

Tabela de emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""

# Original: U+1F60D e U+1F613
# Modificado: U0001F60D e U0001F613

for num in range(1, 11):
    print('\U0001F60D' * num)
    print('\U0001F613' * (11-num))


