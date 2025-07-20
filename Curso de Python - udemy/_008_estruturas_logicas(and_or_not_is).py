"""
Estruturas Lógicas and, or, not, is

Operadores unários:
    - not;
Operadores binários:
    - and, or, is;

Para o 'and', ambos os valores precisam ser True.
Para o 'or', um ou outro valor precisa ser True.
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se for False vira True.
Para o 'is', o valor é comparado com um segundo.
"""
logado = True
ativo = True

if logado and ativo:
    print('Bem vindo ao sistema')
elif not logado:
    print('Logue no sistema')
else:
    print('Ative sua conta')

print('"Logado é verdadeiro?"')
print(logado is True)

print('"Logado é falso?"')
print(logado is False)
print()

nome = 'PAULO'
print(nome.isupper())
print()

print(1 is 1)
print(1 == 1)
