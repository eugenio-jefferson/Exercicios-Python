# FAÇA UM ALGORITIMO QUE LEIA O SALÁRIO DE UM FUNCIONARIO E MOSTRE SEU NOVO SALÁRIO COM 15% DE AUMENTO.

print('='*10, 'CALCULADOR DE AUMENTO DE 15%', '='*10)
s = float(input('Digite o valor do salário: R$ '))
a = s * (1 + 0.15)
print('O salário de R$ {}, com 15% de aumento fica por R$ {}.'.format(s, a))