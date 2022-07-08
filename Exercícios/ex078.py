# FAÇA UM PROGRAMA QUE LEIA 5 VALORES NUMÉRICOS E GUARDE-OS EM UMA LISTA. NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR
# VALOR DIGITADO E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA.

lista=[int(input('Digite o número para posição 0: ')),int(input('Digite o número para posição 1: ')),
       int(input('Digite o número para posição 2: ')),int(input('Digite o número para posição 3: ')),
       int(input('Digite o número para posição 4: '))]
print('-'*20)
print(f'O maior valor digitado foi {max(lista)}, que esta na posição: ', end='')
for p,v in enumerate(lista):
    if v == max(lista):
        print(f'{p}; ',end='')
print(f'\nO menor valor digitado foi {min(lista)}, qu esta na posição: ',end='')
for p,v in enumerate(lista):
    if v==min(lista):
        print(f'{p}; ',end='')
