"""
Por que testar nosso código?

Testes Automatizados!

Ex: Suponha uma aplicação web (um web site com frontend e backend)
Programamos testes automatizados para entrar no site, clicar nas opções, testar tudo que for escolhido.

Por que testar nosso código?
    - Reduzir bugs (problemas) no código;
    - Testes garantem que novos recursos da sua aplicação não quebrem (alterem) recursos antigos;
    - Testes garantem que bugs que foram corrigitos anteriormente continuem corrigidos;
    - Testes garantem que a refatoração que costumamos fazer não tragam novos bugs;

TDD - Test Driven Development (Desenvolvimento Guiado por Testes)

Com TDD é utilizado estágios de desenvolvimento:
    - Você escreve seu teste primeiro;
    - Então você escreve o código mínimo suficiente para o teste passar (ou seja, executar com sucesso);
    - Refatora o código para realizar a funcionalidade e testa novamente;
    - Uma vez que o teste passe, o recurso é considerado completo;

Estes estágios de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como:
    - Red (Teste falhou -> Vermelho);
    - Green (Codificar até funcionar -> Verde);
    - Refactor (Refatorar);

"""

class Gato:

    def __init__(self, nome):
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome
    
    def miar(self):
        print(f'{self.__nome} está miando...')
    

# Teste manual

felix = Gato('Felix')

felix.miar()

print(felix.nome)
