"""
POO - MRO - Method Resolution Order

Method Resolution Order (Resolução de Ordem de Métodos), é a ordem
de execução dos métodos (quem será executado primeiro).

Em Python, a gende pode conferir a ordem de execução dos métodos (MRO) de 3 formas:
    - Via propriedade de calsse __mro__
    - Via método mro()
    - Via help
"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome
    
    def cumprimentar(self):
        return f'Eu sou {self.__nome}'
    
class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def nadar(self):
        return f'{self._Animal__nome} está nadando.'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def andar(self):
        return f'{self._Animal__nome} está andando.'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'

class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)

# Testando

pingu = Pinguim('Tux')
print(pingu.cumprimentar())

print('\nVerificando MRO')
print(Pinguim.__mro__)
print()
print(Pinguim.mro())

# Como mudar a ordem de execução da herança?
# Trocar:
# class Pinguim(Terrestre, Aquatico):
# Para:
# class Pinguim(Aquatico, Terrestre):
