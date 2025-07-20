"""
Doctests

Doctestes são testes que colocamos na docstring das funções/métodos Python.

Para rodar um test do doctest:
python -m doctest -v nome_do_modulo.py

neste caso: 
python -m doctest -v Aulas\_098_doctests.py   
"""

def soma(a, b):
    """soma os números a e b

    >>> soma(1, 2)
    3

    >>> soma(0, -2)
    2
    """
    return a + b


# Outro exemplo

def duplicar(valores):
    """duplica os valores em uma lista
    
    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]
    
    >>> duplicar([])
    []
    
    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    Traceback (most recent call last):
       ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]

# No teste duplicar([True, False])
# Dizemos que o retorno é um erro especificado. Se tudo bater (escrita do erro identica)
# Este teste não é tido como falha.


# Erro inesperado...

def fala_oi():
    """Fala oi
    
    >>> fala_oi()
    "oi"              # Aqui
    """
    return "oi"

# Se trocarmos as aspas duplas do "oi" por aspas simples 'oi', o teste não falha.


# Um último caso estranho...

def verdade():
    """Retorna veradde
    
    >>> verdade()
    True  
    """
    return True

# Note que o retorno do teste tem dois espaços após o True: 'True  '
# Alguma IDE's corrijem isto. (VSCode parece que não)
