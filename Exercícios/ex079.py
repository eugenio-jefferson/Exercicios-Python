# CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR VÁRIOS VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA. CASO O NÚMERO
# JÁ EXISTA NA LISTA ELE NÃO SERÁ ADICIONADO. NO FINAL, SERÃO EXIBIDOS TODOS OS VALORES ÚNICOS DIGITADOS, EM ORDEM
# CRESCENTE

lista=[]
while True:
    v=int(input('Digite um número: '))
    if v in lista:
        print(f'O número {v} já está na lista, não será adicionado novamente.')
    else:
        lista.append(v)
    cont=input('Quer continuar? [S|N]: ')
    if cont.lower()=='n':
        break
print(f'A lista final é: {sorted(lista)}')