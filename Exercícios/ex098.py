# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA CONTADOR(), QUE RECEBA TRÊS PARÂMETROS: INÍCIO, FIM E PASSO E REALIZE A
# CONTAGEM. SEU PROGRAMA TEM QUE REALIZAR TRÊS CONTAGENS ATRAVÉS DA FUNÇÃO CRIADA: A) DE 1 ATÉ 10, DE 1 EM 1;
# B) DE 10 ATÉ 0, DE 2 EM 2; C) UMA CONTAGEM PERSONALIZADA;

from time import sleep

def contador(i,f,p):
    print('-'*50)
    if p==0:
        p=1
    if p<0:
        p*=-1

    print(f'Contagem de {i} até {f} de {p} em {p}: ')

    if i <f:
        for c in range(i,f+1,p):
            print(c,end=' ')
            sleep(0.2)
    else:
        c= i
        while c>=f:
            print(c,end=' ')
            c-=p
            sleep(0.2)
    print('Fim!')
    print('-'*50)

contador(1,10,1)
contador(10, 0,2)
print('Escolha os números para contagem:')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))