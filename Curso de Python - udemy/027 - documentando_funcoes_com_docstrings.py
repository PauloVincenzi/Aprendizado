"""
Documentando funções com Docstrings
"""

print(help(print))

# Exemplos

def diz_oi():
    """Uma função simples que retorna a string 'Oi!'"""
    return 'Oi!'

print(help(diz_oi))


def exponencial(base, expoente=2):
    """
    Função que retorna por padrão o quadrado de um número informado
    :param base: Número que desejamos exponenciar
    :param expoente: Potência/Expoente da base
    :return: Retorna o exponencial de 'base' por 'expoente' 
    """
    return base ** expoente

print(help(exponencial))
