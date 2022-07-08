# ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO:
# -1 PARA BINÁRIO, -2 PARA OCTAL, -3 PARA HEXADECIMAL.

print('\033[35m=-'*10, '\033[33mCONVERSOR DE BASES NÚMERICAS', '\033[35m=-\033[m'*10)
num = int(input('Digite um número para ser convertido: '))
print('\033[34mEscolha a base a ser convertida:\n[1] Para binário;\n[2] para octal;\n[3] para hexadecimal;\033[m')
base = input('Escolha uma opção: ')
if base == '1':
    print('{} em binário é {}.'.format(num, format(num, "b")))
elif base == '2':
    print('{} em octal é {}.'.format(num, oct(num)[2:]))
elif base == '3':
    print('{} em hexadecimal é {}.'.format(num, hex(num)[2:]))
else:
    print('\033[31mOpção inválida, tente novamente.')