"""
Programação Orientada a Objetos - POO

 - POO é um paradigma de programação que utiliza um mapeamento de objetos
 do mundo real para modelos computacionais

 - Paradigma de programação é a forma/metodologia utilizada para
 pensar/desenvolver sistemas.

Principais elementos da Orientação a Obetos:
 - Classes -> Modelo do objeto do mundo real sendo representado computacionalmente;
 - Atributo -> Características do objeto;
 - Método -> Comportamento do objeto (funções);
 - Construtor -> Método especial utilizado para crias objetos;
 - Objeto -> Instância da classe.
"""

numero = 10
print(type(numero))

nome = 'Geek'
print(type(nome))


class Produto:
    pass

ps4 = Produto()
# Classe Produto; Não há atributos ou métodos definidos;
# Define-se o objeto ps4 através do construtor 'Produto()'

print(type(ps4))
print('O tipo do objeto ps4 é um novo tipo, definido pela classe criada')

