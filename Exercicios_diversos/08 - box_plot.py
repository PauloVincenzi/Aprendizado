"""
Análise descritiva sobre o tempo de prova de diferentes categorias em ambos os sexos.
O que se pode concluir ao analisar gráficos / boxplots?
"""

import matplotlib.pyplot as plt

categorias = ['100 m', '400 m', '3000 m']

tempos_fem = {
    '100 m': [0.1935, 0.1885, 0.2000, 0.1933, 0.1835, 0.1815, 0.1858, 0.1833, 0.1798, 0.1955],
    '400 m': [0.9083, 0.8800, 0.9150, 0.8876, 0.8026, 0.8621, 0.9050, 0.8343, 0.8436, 0.8783],
    '3000 m': [9.79, 9.77, 9.37, 9.46, 8.75, 8.98, 8.84, 8.81, 8.50, 9.20],
}

tempos_masc = {
    '100 m': [0.1732, 0.1703, 0.1723, 0.1738, 0.1693, 0.1685, 0.1755, 0.1695, 0.1655, 0.1743],
    '400 m': [0.7807, 0.7535, 0.7700, 0.7683, 0.7417, 0.7547, 0.7783, 0.7613, 0.7310, 0.7487],
    '3000 m': [8.20, 8.42, 8.50, 8.24, 8.26, 8.29, 8.40, 8.23, 8.22, 8.36],
}

# GRÁFICO DE BARRAS

media_fem = [sum(tempos_fem[cat]) / len(tempos_fem[cat]) for cat in categorias]
media_masc = [sum(tempos_masc[cat]) / len(tempos_masc[cat]) for cat in categorias]
x = range(len(categorias))
largura = 0.35

plt.bar([i - largura/2 for i in x], media_masc, width=largura, label='Homens')
plt.bar([i + largura/2 for i in x], media_fem, width=largura, label='Mulheres')
plt.xticks(ticks=x, labels=categorias)
plt.ylabel('Tempo médio (min)')
plt.title('Comparação de tempos por prova')
plt.legend()
plt.show()

# BOXPLOT's

# 100 m

plt.boxplot([tempos_fem['100 m'], tempos_masc['100 m']], labels=['Mulheres', 'Homens'])
plt.title('100m - Comparação de tempos')
plt.ylabel('Tempo (min)')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

# 400 m

plt.boxplot([tempos_fem['400 m'], tempos_masc['400 m']], labels=['Mulheres', 'Homens'])
plt.title('400m - Comparação de tempos')
plt.ylabel('Tempo (min)')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

# 3000 m

plt.boxplot([tempos_fem['3000 m'], tempos_masc['3000 m']], labels=['Mulheres', 'Homens'])
plt.title('3000m - Comparação de tempos')
plt.ylabel('Tempo (min)')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

print("""\nJá suspeitavamos que os tempos de todas categorias masculinas seriam menores que os tempos femininos.
Porém uma observação interessante foi obtida ao analisar os boxplots:
Os tempos de prova masculinos são muito mais concentrados que os tempos de prova feminino. Isto é, há menos variação
de tempo de prova no sexo masculino que no feminino. Isso ficou óbvio ao comparar o 'tamanho' de cada boxplot.
""")
