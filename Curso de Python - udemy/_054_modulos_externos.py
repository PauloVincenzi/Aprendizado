"""
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em: https:pypi.org

Para instalar: "pip install nome-do-modulo" no terminal

colorama -> É utilizado para permitir impressão de textos coloridos no terminal.

pdfkit -> Criação e manipulação de pdf
"""

from colorama import init
init()

from colorama import Fore, Back, Style
print(Fore.RED + 'O texto fica vermelho')
print(Back.GREEN + 'Agora o fundo fica verde')
print(Style.DIM + 'Com estilo DIM')
print(Style.RESET_ALL + 'Resetar as configurações de texto')

import pdfkit

# Caminho para o executável do wkhtmltopdf
caminho_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=caminho_wkhtmltopdf)

# HTML que será convertido
html = '<h1>Geek University</h1><br/><br/><strong>Progama&ccedil;&atilde;o em Python: Essencial</strong>'

# Gerar o PDF diretamente para um arquivo
pdfkit.from_string(html, 'gerar_arquivo_pdf.pdf', configuration=config)
