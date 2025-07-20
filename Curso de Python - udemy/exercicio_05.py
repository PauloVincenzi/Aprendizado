"""
2. Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:

a) armazenar_contato(contato: Contato);
b) remover_contato(contato: Contato);
c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda.
e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice.
"""

from datetime import date

from exercicio_04 import Pessoa 

class Agenda:

    def __init__(self):
        self.__contatos: list[Pessoa] = []
    

    @property
    def contatos(self) -> list[Pessoa]:
        return self.__contatos
    
    def armazenar_contato(self, contato: Pessoa) -> None:
        self.contatos.append(contato)
    
    def remover_contato(self, contato: Pessoa) -> None:
        self.contatos.remove(contato)
    
    def buscar_contato(self, nome: str) -> None:
        for indice, contato in enumerate(self.contatos):
            if contato.nome == nome:
                print(f'O contato {nome} está na posição: {indice}')
    
    def imprimir_agenda(self) -> None:
        for contato in self.contatos:
            contato.imprimir()
    
    def imprimir_contato(self, indice: int) -> None:
        self.contatos[indice].imprimir()


if __name__ == '__main__':
    contato1: Pessoa = Pessoa('Julia Abackerli', date(2004, 4, 20), 'juliaabackerli@gmail.com')
    contato2: Pessoa = Pessoa('Paulo Eduardo', date(2004, 6, 28), 'paulovincenzi@usp.br')
    contato3: Pessoa = Pessoa('Carlos Eduardo', date(1967, 3, 13), 'carloseduardo@gmail.com')
    contato4: Pessoa = Pessoa('Kelen Cristina', date(1978, 2, 25), 'kelencristina@gmail.com')

    agenda: Agenda = Agenda()

    agenda.armazenar_contato(contato1)
    agenda.armazenar_contato(contato2)
    agenda.armazenar_contato(contato3)
    agenda.armazenar_contato(contato4)

    print('-'*50)

    agenda.imprimir_agenda()

    print('-'*50)

    agenda.buscar_contato('Paulo Eduardo')

    print('-'*50)

    agenda.imprimir_contato(3)

    print('-'*50)

    agenda.remover_contato(contato2)

    agenda.imprimir_agenda()

    print('-'*50)
