# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIÂNGULO RETÂNGULO,
# CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA

from math import hypot
print('='*10, 'CALCULANDO A HIPOTENUSA', '='*10)
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa de {} e {}, é igual a {:.2f}.'.format(co, ca, hi))