"""
Módulos Customizados

Como módulos Python nada mais são do que arquivos Python, então TODOS os arquivos que criamos neste curso
são módulos Python Python prontos para serem utilizados.

Um arquivo que serve como Módulo Python não deve ter execução, apenas funções definidas.
"""

from arquivo_teste import soma_impares

print(soma_impares([1, 3, 6, 8, 2, 7, 5, 1, 0, 5, 12, 11]))

# Ao importar um módulo (arquivo), podemos acessar qualquer elemento deste. Seja função ou variável.

import arquivo_teste as at

print(at.cidades)
