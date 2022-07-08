# CRIE UM PROGRAMA QUE CRIE UMA MATRIZ DE DIMENSÃO 3X3 E PREENCHA COM VALORES LIDOS PELO TECLADO. NO FINAL MOSTRE A
# MATRIZ NA TELA COM A FORMATAÇÃO CORRETA.

matriz=[[0,0,0],[0,0,0],[0,0,0]]

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna]=int(input(f'Digite um número para posição ({linha},{coluna}): '))

print('A matriz digita é: ')
for linha in range(0,3):
    print('|',end='')
    for coluna in range(0,3):
        print(f'{matriz[linha][coluna]:^7}',end='')
    print('|')
