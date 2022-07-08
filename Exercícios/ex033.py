# FAÇA UM PROGRAMA QUE LEIA 3 NÚMEROS E MOSTRE NA TELA QUAL É O MAIOR E QUAL É O MENOR

print('\033[33m='*10, '\033[35mQUAL É O MAIOR E MENOR?', '\033[33m=\033[m'*10)
a = int(input('Pimeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O maior valor é \033[4;36m{}\033[m.'.format(maior))
print('O menor valor é \033[4;34m{}\033[m.'.format(menor))