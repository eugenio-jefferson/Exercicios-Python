# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS DIGITOS SEPARADOS.
# EX: DIGITE UM NÚMERO: 1834 UNIDADE 4, DEZENA 3, CENTENA 8, MILHAR 1

print('='*10, 'SEPARANDO UM NÚMERO', '='*10)
'''n = input('Digite um número de 0 a 9999: ')
dez = ' '.join(n[-2:]).split()
print('O número {} tem:\n{} Unidade.\n{} Dezena.'.format(n, n[-1],dez[:-1]))
cent = ' '.join(n[:-2]).split()
print('{} Centena.\n{} Milhar.'.format(cent[-1:], n[:-3]))'''

n = int(input('Digite um número de 0 a 9999: '))
print('O número {} tem:\n{} Unidade.\n{} Dezena.'.format(n, n // 1 % 10, n // 10 % 10))
print('{} Centena.\n{} Milhar.'.format(n // 100 % 10, n // 1000 % 10))