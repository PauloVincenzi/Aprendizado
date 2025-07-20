"""
Len, Abs, Sum, Round

len() -> Retorna o tamanho (ou seja, o número de itens) de um iterável.

abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o módulo do número.

sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma de todos os elementos, incluindo o valor inicial.

round() -> Retorna um número arredondado para n digitos de precisão após a casa decimal. Se a precisão não for
informada, retorna o inteiro mais próximo da entrada.
"""

print('LEN:')
print(len([1, 2, 3, 4]))
print(len('Abobrinha'))
print(len({'a': 2, 'b': 1, 'c': 3, 'd': 4, 'e': 2}))
print(len(range(0, 10)))

# Por debaixo dos panos, quanto utilizamos a função len() o Python faz o seguinte:

# Dunter len
# print('Abobrinha'.__len__())

print('\nABS') # não funciona com strings
print(abs(3))
print(abs(-3))
print(abs(-3.14))

print('\nSUM') # não funciona com strings
print(sum([1, 2, 3, 4, 5]))
print(sum([0.4, 3, 0.1, 0.7, 2], 100)) # 100 como valor inicial

print('\nROUND')
print(round(2))
print(round(2.3))
print(round(2.7))
print(10.9572, 3)
print(10.9577, 3)
print(10.312, 2)
