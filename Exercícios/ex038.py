# ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS, MOSTRANDO NA TELA UMA MENSAGEM: -O PRIMEIRO VALOR É
# MAIOR, -O SEGUNDO VALOR É MAIOR, -NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS.

print('\033[35m=-'*10, '\033[33mCOMPARADOR DE DOIS NÚMEROS', '\033[35m=-\033[m'*10)
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print('O \033[31mprimeiro\033[m valor é maior!')
elif n2 > n1:
    print('O \033[31msegundo\033[m valor é maior!')
else:
    print('\033[31mNão existe\033[m valor maior, os dois são iguais!')