# DESAFIO: FAZER UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SEU SUCESSOR E ANTECESSOR.

print('=' * 10, 'QUAL É O SUCESSOR E ANTECESSOR', '=' * 10)
n = int(input('Digite um número: '))
s = n +1
a = n - 1
print('O sucessor de {} é {}. \nE o antecessor de {} é {}.'.format(n, s, n, a))

