"""
Escrevendo um iterador customizado

for i in range(1, 61):
    print(i)
"""

# Criando um 'for (range)' simplificado

class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration
    

con = Contador(1, 61)

print(next(con))
print(next(con))
print(next(con))
print(next(con))

print('-'*50)

for n in con:
    print(n)
