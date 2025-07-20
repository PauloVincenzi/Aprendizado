"""
1. Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e
setters para os atributos e um método para imprimir os dados de uma pessoa.
"""

from datetime import date

class Pessoa:

    def __init__(self, nome: str, data_nasc: date, email: str) -> None:
        self.__nome: str = nome
        self.__data_nasc: date = data_nasc
        self.__email: str = email
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def data_nasc(self) -> date:
        return self.__data_nasc
    
    @data_nasc.setter
    def data_nasc(self, data_nasc: date) -> None:
        self.__data_nasc = data_nasc

    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, email: str) -> None:
        self.__email = email

    def imprimir(self) -> None:
        print(f'Nome: {self.nome}')
        print(f'Data de nascimento: {self.data_nasc.strftime('%d/%m/%Y')}')
        print(f'Email: {self.email}')


if __name__ == '__main__':
    p: Pessoa = Pessoa('Paulo Eduardo', date(2004, 6, 28), 'paulovincenzi@usp.br')

    p.imprimir()

