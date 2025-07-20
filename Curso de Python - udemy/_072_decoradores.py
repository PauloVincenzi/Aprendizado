"""
Decoradores (Decorators)

O que são decorators?

 - Decorators são funções;
 - Decorators envolvem outras funções e aprimoram seus comportamentos;
 - Decorators também são exemplos de High Order Functions;
 - Decorators tem uma sintaxe própria, usando '@' (Syntact Sugas / Açúcar Sintático)

"""

# Decorators como funções (Sintaxe não recomendada / Sem Açúcar Sintático)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Seja bem-vindo(a) à Geek University')

# Testando 1
teste = seja_educado(saudacao)
teste()

print('-'*50)

# Testando 2

def raiva():
    print('EU TE ODEIO!')


raiva_educada = seja_educado(raiva)
raiva_educada()

# estamos decorando a funcao saudacao

print('-'*50)

# -----------------------------------------------

# Decorators com Syntax Sugar (Açúcar Sintático)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

# Testando 1 

apresentando()

print('-'*50)

# Testando 2

@seja_educado_mesmo
def dormir():
    print('Quero dormir...')


dormir()

# OBS: Não confunda Decorator com Decorator Function
