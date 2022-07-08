# CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRÔNICO. NO INÍCIO PERGUNTE AO USUÁRIO QUAL SERÁ O VALOR A
# SER SACADO (NÚMERO INTEIRO) E O PROGRAMA VAI INFORMAR QUANTAS CÉDULAS DE CADA VALOR SERÃO ENTREGUES. OBS: CONSIDERE QUE
# O  CAIXA POSSUI CÉDULAS DE R$ 50, R$ 20, R$ 10 E R$ 1.

import math

print('=-='*15 + f'\n{"BANCO":^45}\n' + '=-='*15)
valor = int(input('Qual o valor a ser sacado? R$ '))
print('=-='*15)
print('Você vai receber:')
cédula = 50
total_cédulas = 0
while True:
    if valor >= cédula:
        valor -= cédula
        total_cédulas += 1
    else:
        if cédula == 50:
            cédula = 20
            if total_cédulas >= 1:
                print(f'{total_cédulas} {"cédulas" if total_cédulas > 1 else "cédula"} de R$ 50,00;')
            total_cédulas = 0
        elif cédula == 20:
            cédula = 10
            if total_cédulas >= 1:
                print(f'{total_cédulas} {"cédulas" if total_cédulas > 1 else "cédula"} de R$ 20,00;')
            total_cédulas = 0
        elif cédula == 10:
            cédula = 1
            if total_cédulas >= 1:
                print(f'{total_cédulas} {"cédulas" if total_cédulas > 1 else "cédula"} de R$ 10,00;')
            total_cédulas = 0
        elif cédula == 1:
            if total_cédulas >= 1:
                print(f'{total_cédulas} {"cédulas" if total_cédulas > 1 else "cédula"} de R$ 1,00;')

        if valor == 0:
            break
print('=-='*15 + f'\n{"Atendimento finalizado, volte sempre!":^45}\n' + '=-='*15)