# CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS, A CADA PESSOA CADASTRADA O PROGRAMA DEVE PERGUNTAR SE
# O USUÁRIO QUER OU NÃO CONTINUA. NO FINAL, MOSTRE: A) QUANTAS PESSOAS TEM 18 ANOS OU MAIS; B) QUANTOS HOMENS FORAM CADASTRADOS;
# C) QUANTAS MULHERES TEM MENOS DE 20 ANOS;

print('=-='*15, f'\n{"CADASTRAMENTO DE PESSOAS":^45}\n'+ '=-='*15)

mais_de_18 = homens_cadastrados = mulheres_menos_de_20 = 0

# ler idade e sexo
while True:
    idade = int(input('Informe a idade da pessoa: '))
    sexo = continuar = ' '

    # confirmar que o usuário digitou o sexo corretamente
    while sexo not in 'mf':
        sexo = str(input('Informe o sexo da pessoa: [M / F] ')).strip().lower()[0]

    # pergunta se é pra continua ou não
    while continuar not in 'sn':
        continuar = str(input('\nQuer cadastrar outra pessoa? [S / N] ')).strip().lower()[0]
        print('---'*15)

    # conferir quantas pessoas tem mais de 18
    if idade >= 18:
        mais_de_18 += 1

    # conferir quantos homens foram cadastrados
    if sexo == 'm':
        homens_cadastrados += 1

    #conferir quantas mulheres tem mais de 20
    if sexo == 'f' and idade < 20:
        mulheres_menos_de_20 += 1

    # se for parar o programa
    if continuar == 'n':
        break

print(f'''\nForam cadastradas:
{mais_de_18} {"pessoas" if mais_de_18 > 1 else "pessoa"} com 18 anos ou mais.
{homens_cadastrados} {"homens" if homens_cadastrados > 1 else "homen"}.
E {mulheres_menos_de_20} {"mulheres" if mulheres_menos_de_20 > 1 else "mulher"} com menos de 20 anos.
''')