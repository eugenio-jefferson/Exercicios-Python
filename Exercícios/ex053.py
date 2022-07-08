# CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM PALÍNDROMO, DESCONSIDERANDO OS ESPAÇOS. EX: APOS A SOPA,
# A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

print('\033[35m-='*20, '\033[33mDETECTOR DE PALÍNDROMO', '\033[35m=-\033[m'*20)
fra = str(input('Digite uma palavra ou uma frase (sem pontuação): ')).strip()
fo = fra.lower().replace(' ', '')
p = ''
for c in range(len(fo) -1, -1,-1):
    p += fo[c]
print(end='''Analisando... 
Concluir que o inverso de {}, é {} e, '''.format(fra, p))
if p == fo:
    print('\033[32mé um polindromo\033[m!')
else:
    print('\033[31mnão é um polindromo\033[m!')
print(p)
