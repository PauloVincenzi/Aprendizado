"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/yyyy 12:24:32.121324
data_final = dd/mm/yyyy 16:31:02.721552

delta = data_final - data_inicial


import datetime

data_hoje = datetime.datetime.now()

aniversario = datetime.datetime(2025, 9, 14, 3, 15, 30)

# Calculando o delta
tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))
print(repr(tempo_para_evento))
print(tempo_para_evento)
"""

import datetime

data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto

print(vencimento_boleto)
