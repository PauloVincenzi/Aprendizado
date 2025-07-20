"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico
utilizando classes.

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e
métodos privados de usuário.

# Se os atributos forem públicos, é possível alterar:
conta1.numero = 42
conta1.titular = 'Xuxa'
conta1.saldo = 912412
conta1.limite = 1

# Mesmo que os atributos forem privados, é possível alterar o valor com o Name Mangling:
conta1._Conta__titular = 'Wesley'
"""

class Conta:
    contador = 400
    def __init__(self, titulador, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titulador
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        self.__saldo -= valor
    
    def transferir(self, valor, conta_destino):
        self.__saldo -= valor
        conta_destino.__saldo += valor
    

# Testando

conta1 = Conta('Geek', 150.00, 1500)

print(conta1.__dict__)

conta1.extrato()
 
conta2 = Conta('Maicon', 500.00, 6000)

conta2.extrato()

conta2.transferir(100, conta1)

conta2.extrato()

conta1.extrato()
