"""
Geradores

 - Geradores (Generators) são Iterators (Iteradores):

OBS: O contrário não é verdadeiro. Ou seja, nem todo iterator é um generator.

Outras informações:
 - Generators podem ser criados com funções geradores;
 - Funções geradores utilizam a palavra reservada yield;
 - Generators podem ser criados com Expressões Geradoras;

 Difrenças entre Funções e Generator Functions (Funções Geradoras)
 
 ======================================================================================
 | Funções                              | Generator Functions                         |
 |======================================|=============================================|
 |--------------------------------------|---------------------------------------------|
 | utilizam return                      | utilizam yield                              |
 |--------------------------------------|---------------------------------------------|
 | retornam uma vez                     | podem utilizar yield múltiplas vezes        |
 |--------------------------------------|---------------------------------------------|
 | quando executadas, retorna um valor  | quando executada, retorna um generator      |
 --------------------------------------------------------------------------------------
 """

# Exemplo Generator Function

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

gen = conta_ate(5)
print(type(gen))

print(list(gen))

gen = conta_ate(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) # StopIteration

# OBS: Uma Generator Function não é um Generator. Ela gera um generator!
