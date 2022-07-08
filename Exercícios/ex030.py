# CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU ÍMPAR

print('='*10, 'ÍMPAR OU PAR', '='*10)
num = int(input('Digite um número inteiro: '))
print('Analisando o número...')
if num % 2 == 0:
    print('Concluir que o número {} é \033[33;40mPAR\033[m.'.format(num))
else:
    print('Concluir que o número {} é \033[36;40mÍMPAR\033[m.'.format(num))