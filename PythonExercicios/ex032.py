from datetime import date
ano = int(input('Digite o ano desejado! Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} É UM ANO BISSEXTO!'.format(ano))
else:
    print('{} NÃO É UM ANO BISSEXTO!'.format(ano))
