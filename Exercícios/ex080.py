# CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR CINCO VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA, JÁ NA POSIÇÃO
# CORRETA DE INSERÇÃO (SEM USAR O SORT!). NO FINAL MOSTRE A LISTA ORDENANDA NA TELA.

lista=[]
for c in range(0,5):
    n = int(input(f'Digite o {c+1}º número: '))
    if c==0 or n> lista[-1]:
        lista.append(n)
    else:
        p=0
        while p<len(lista):
            if n<=lista[p]:
                lista.insert(p,n)
                break
            p+=1
print(f'A lista final ordenada é: {lista}')