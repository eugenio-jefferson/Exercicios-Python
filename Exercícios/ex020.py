# O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHO DOS ALUNOS.
# FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATROOS ALUNOS E MOSTRE A ORDEM SORTEADA

from random import shuffle
print('='*10, 'SORTEANDO UMA ORDEM NA LISTA', '='*10)
print('Escreva os nomes dos quatros alunos:')
a1 = input('Aluno(a) 1: ')
a2 = input('Aluno(a) 2: ')
a3 = input('Aluno(a) 3: ')
a4 = input('Aluno(a) 4: ')
l = [a1, a2, a3, a4]
shuffle(l)
print('A ordem dos escolhidos foi:', l)