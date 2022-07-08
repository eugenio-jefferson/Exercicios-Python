# CRIE UM PROGRAMA QUE LEIA NOME E DUAS NOTAS DE VÁRIOS ALUNOS E GUARDE TUDO EM UMA LISTA COMPOSTA. NO FINAL, MOSTRE
# UM BOLETIM CONTENDO A MÉDIA DE CADA UM E PERMITA QUE O USUÁRIO POSSA MOSTRAR AS NOTAS DE CADA ALUNO INDIVIDUALMENTE.

boletim=[]
dados=[]
r='c'
id=0
while not r in 'Nn':
    nome=str(input('Digite o nome: '))
    n1=float(input('Digite a nota 1: '))
    n2=float(input('Digite a nota 2: '))
    média=(n1+n2)/2
    dados.append(str(id))
    dados.append(nome)
    dados.append(n1)
    dados.append(n2)
    dados.append(média)
    boletim.append(dados[:])
    dados.clear()
    r=str(input('Quer continuar? [S|N]: '))
    id+=1

print(f'{"ID":<4}{"NOME":<28}{"MÉDIA":>7}')
print('-'*40)
for c in range(0,len(boletim)):
    print(f'{boletim[c][0]:<4}{boletim[c][1]:<30}{boletim[c][4]:>5.2f}')
print('-'*40)
id=0
while id!=999:
    id=int(input('Indique um ID para mostrar as notas de um aluno (999 finaliza): '))
    for d in boletim:
        if str(id) in d:
            print(f'{d[1].title()},tirou {d[2]} na primeira nota e {d[3]} na segunda nota, ficou com média de {d[4]:.2f}.')
            print()
print('Finalizado')