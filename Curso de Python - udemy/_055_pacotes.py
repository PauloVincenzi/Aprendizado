"""
Pacotes

Módulo -> É apenas um arquivo Python que pode ter diversas funções para utilizarmos;

Pacote -> É um diretório contendo uma coleção de módulos;

OBS: Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um arquivo chamado __init__.py
Nas versões do Python 3.x, não é mais obrigatório a utilização deste arquivo, mas normalmente
ainda é utilizado para manter compatibilidade.

# Observe os packages criados 'geek' e 'university' (onde o pacote 'university' está contido no pacote 'geek')
"""

from geek import geek1, geek2

from geek.university import geek3, geek4

print(geek1.pi) #3.1415
print(geek1.funcao1(4, 6)) # 10

print(geek2.curso) # Programação em Python: Essencial
print(geek2.funcao2()) # Programação em Python: Essencial

print(geek3.funcao3()) # Geek

print(geek4.funcao4()) # University

from geek.geek1 import funcao1

print(funcao1(2, 3)) # 5

from geek.university.geek4 import funcao4

print(funcao4()) # University
