# APRIMORE O DESAFIO ANTERIOR, MOSTRANDO NO FINAL: A) A SOMA DE TODOS OS VALORES PARES DIGITADOS; B) A SOMA DOS VALORES
# DA TERCEIRA COLUNA; C) O MAIOR VALOR DA SEGUNDA LINHA;

matriz=[[0,0,0],[0,0,0],[0,0,0]]
soma=ter=maior=0
for linha in range(0,3):
    for coluna in range(0,3):
        num=int(input(f'Digite um número para posição ({linha},{coluna}): '))
        matriz[linha][coluna] = num
        if num%2==0:
            soma+=num
        if coluna==2:
            ter+=matriz[linha][coluna]
        if linha==1 and coluna==0:
            maior=matriz[linha][coluna]
        else:
            if linha==1:
                if matriz[linha][coluna]>maior:
                    maior=matriz[linha][coluna]
print('-'*30)
for linha in range(0,3):
    print('|',end='')
    for coluna in range(0,3):
        print(f'{matriz[linha][coluna]:^9}',end='')
    print('|')
print('-'*30)
print(f'A soma de todos os números pares da matriz é {soma};')
print(f'A soma dos números da terceira coluna é {ter};')
print(f'O maior número da segunda linha é {maior}:')