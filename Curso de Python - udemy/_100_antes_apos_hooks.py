"""
Unittest - Antes e após hooks

----
Hooks -> são os testes em si. Ou seja, a execusão dos testes.
----

setup() -> é executado antes de cada método de teste. É útil para criamrmos intâncias de objetos e outros dados;

tearDown() -> é execitadp ap fomaç de cada método de teste. É útil para excluir dados ou fechar conexões com
banco de dados.

"""

import unittest

class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Configurações do setUp()
        pass

    def test_primeito(self):
        # setUp vai rodar antes do teste.
        # tearDown() vai rodar após o teste.
        pass

    def test_segundo(self):
        # setUp vai rodar antes do teste.
        # tearDown() vai rodar após o teste.
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass