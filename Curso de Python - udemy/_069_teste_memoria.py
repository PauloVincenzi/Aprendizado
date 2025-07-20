"""
Teste de Memória com Generators

# Sequência de Fibonacci
# 1, 1, 2, 3, 5, 8, 13...

# Função usando listas

def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a+b
    return nums

# TESTE 1 - 122 MB de memória
for n in fib_list(50000):
    print(n)

# Função usando geradores

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a+b
        yield a
        contador += 1

# TESTE 2 - 5 MB de memória
for n in fib_gen(50000):
    print(n)
"""
# Para retirar o limite de digitos de conversão em uma string
import sys

sys.set_int_max_str_digits(0)  # 0 = sem limite

