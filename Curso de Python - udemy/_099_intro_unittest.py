"""
Introdução ao módulo Unittest

Unittest -> Testes Unitários

O que são testes unitários?

Teste unitário é a forma de se testar unidades individuais de código fonte.

Unidades individuais podem ser: funções, métodos, classes, módulos, etc.

# OBS: Teste unitário não é específico da linguagem Python.

Para criar nossos testes, criamos classes que herdam de unittest.TestCase
e a partir de então ganhamos todos os 'assertions' presentes no módulo.

Para rodar os testes, utilizamos unittest.main()

TestCase -> Casos de teste para sua unidade

# Conhecendo as assertions

Método                      Checa se
assertEqual(a,b)            a == b
assertNotEqual(a, b)        a != b
assertTrue(x)               x é verdadeiro
assertFalse(x)              x é falso
assertIs(a, b)              a é b
assertIsNot(a, b)           a not é b
assertIsNone(x)             x é None
assertIsNotNone(x)          x não é None
assertIn(a, b)              a está em b
assertNotIn(a, b)           a não está em b
assertIsInstance(a, b)      a é instância de b
assertNosIsInstance(a, b)   a não é instância de b

Por convenção, todos os testes em um teste case, devem ter seu nome
iniciado com test_

Para executar os testes com unittes

python nome_do_modulo.py

# Para executar os testes com unittest no modo verbose

python nome_do_modulo.py -v

# Docstrings nos testes

Podemos acrescentar (e é recomendado) docstrings nos nossos testes
"""

# Prática - arquivos 'atividades.py' e 'testes.py'
# O ideal é que o arquivo de testes seja diferente do código principal
