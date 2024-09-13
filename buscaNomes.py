from pyhtml2pdf import converter
import pandas as pd
import PyPDF2
import os

# Lê o .txt e separa os nomes em uma lista 
data = pd.read_csv('names.txt',names=['nomes'])
names = data['nomes'].to_list()

# O url certinho que o google acessa
siteAddress = 'https://www.google.com/search?q='

# Pra cada nome na lista, pega um nome, separa nos espaços e adiciona na url
for name in names:
    for word in name.split(' '):
        siteAddress = siteAddress+word+'+'

    # Acessa o site, salva o html como pdf e reseta o endereço de pesquisa
    converter.convert(siteAddress, f'{name}.pdf')
    siteAddress = 'https://www.google.com/search?q='

# Instancia o merger de pdf. Busca na pasta onde o script está por todos os arquivos .pdf e junta todos
merger = PyPDF2.PdfMerger()
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)

# Salva o relatório final
merger.write("Relatório Final.pdf")