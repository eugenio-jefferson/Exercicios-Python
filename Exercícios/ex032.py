# FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO

from datetime import date
print('='*10, 'O ANO É BISSEXTO?', '='*10)
ano = int(input('Digite um ano. Coloque "0" para ver o ano atual: '))
print('O ano {} é bissexto? '.format(ano))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Sim! {} é bissexto.'.format(ano))
else:
    print('Não! {} não é bissexto.'.format(ano))