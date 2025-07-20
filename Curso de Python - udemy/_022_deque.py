"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance.
"""

# Fazendo o import
from collections import deque

# Criando deques

deq = deque('Geek')

print(deq)

# Adicionado elementos no deque
print('Adicionado elementos')

deq.append('y') # Adiciona no final

print(deq)

deq.appendleft('k') # Adiciona no começo

print(deq)

# Remover elementos
print('Remover elementos')

print(deq.pop()) # Remove e retorna o último elemento

print(deq)

print(deq.popleft()) # Remove e retorna o primeiro elemento

print(deq)
