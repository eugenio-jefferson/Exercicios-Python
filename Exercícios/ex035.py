# DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA AO USÚARIO SE PODEM OU NÃO FORMAR UM TRIÂNGULO

print('\033[36m='*10, '\033[33mCRIAÇÃO DE TRIÂNGULOS', '\033[36m=\033[m'*10)
print('Diga o valor de três retas para eu verificar se podem formar um triângulo:')
r1 = float(input('Qual a medida da primeira reta? '))
r2 = float(input('Qual a medida da segunda reta? '))
r3 = float(input('Qual a medida da terceira reta? '))
a = 'v' if r2 + r3 > r1 > r2 - r3 else 'f'
b = 'v' if r1 + r3 > r2 > r1 - r3 else 'f'
c = 'v' if r1 + r2 > r3 > r1 - r2 else 'f'
if a and b and c == 'v':
    t = '\033[32mPODEM FORMAR\033[m'
else:
    t = '\033[31mNÃO PODEM FORMAR\033[m'
print('As retas acima {} um triângulo!'.format(t))