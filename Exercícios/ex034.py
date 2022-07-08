# ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO. PARA SALÁRIOS SUPERIORES
# A R$ 1.250,00, CALCULE UM AUMENTO DE 10%. PARA OS INFERIORES OU IGUAIS O AUMENTO É DE 15%

print('\033[36m='*10, '\033[33mAUMENTO SALÁRIAL', '\033[36m=\033[m'*10)
sal = float(input('Qual o valor do seu salário: R$ '))
aum = sal * 1.1 if sal > 1250 else sal * 1.15
print('Com o salário de \033[31mR${:.2f}\033[m, você terá um aumento para \033[1;32mR${:.2f}\033[m.'.format(sal, aum))