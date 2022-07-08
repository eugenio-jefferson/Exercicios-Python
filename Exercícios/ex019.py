# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATROS ALUNOS PARA APAGAR O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE,
# LENDO O NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO.

from random import choice
print('='*10, 'SORTEIO ENTRE ALUNOS', '='*10)
print('Escreva os nomes dos alunos(a):')
a1 = input('Aluno(a) 1: ')
a2 = input('Aluno(a) 2: ')
a3 = input('Aluno(a) 3: ')
a4 = input('Aluno(a) 4: ')
lista = [a1, a2, a3, a4]
sorteado = choice(lista)
print('O aluno escolhido foi', sorteado+ '.')