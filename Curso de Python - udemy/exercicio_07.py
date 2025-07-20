"""
Crie a classe Veiculo, contendo marca e modelo. Crie as propriedades getters e setters para os atributos e
um método para imprimir os dados de um veículo. Crie também o construtor da classe.

Crie a classe Carro que herda a classe Veiculo e possui o atributo portas. Crie as propriedades getters e
setters para o atributo. Crie também o construtor da classe. Sobrescreva o método de imprimir os dados do
veículo de forma a apresentar também a quantidade de portas do carro.

"""

class Veiculo:

    def __init__(self, marca, modelo):
        self.__marca = marca
        self.modelo = modelo
    
    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self._modelo
    
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo
    
    def imprimir(self):
        print(f'Marca: {self.__marca}')
        print(f'Modelo: {self.__modelo}')


class Carro(Veiculo):

    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.__portas = portas
    
    @property
    def portas(self):
        return self.__portas

    @portas.setter
    def portas(self, portas):
        self.__portas = portas
    
    def imprimir(self):
        super().imprimir()
        print(f'Nº de Portas: {self.__portas}')

# Crie um programa, instancie um objeto da classe Carro e teste o seu médodo.

# from exercicio_07 import Carro

c1: Carro = Carro(marca='honda', modelo='Fit', portas=4)
c1.imprimir()