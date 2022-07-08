# DESENVOLVA UMA LÓGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA, CALCULE SEU IMC MOSTRE SEU STATUS, DE ACORDO COM A
# TABELA ABAIXO: -ABAIXO DE 18,5: ABAIXO DO PESO, -ENTRE 18,5 E 25: PESO IDEAL, -25 ATÉ 30: SOBREPESO, -30 ATÉ 40:
# OBESIDADE, -ACIMA DE 40: OBESIDADE MÓRBIDA

print('\033[35m-='*10, '\033[33mANALISADOR DE PESO', '\033[35m=-\033[m'*10)
pes = float(input('Qual seu peso? (kg) '))
alt = float(input('Qual sua altura? (m) '))
imc = pes / alt ** 2
print('Com {:.2f}kg, e com {:.2f}m o IMC é de {:.1f}kg/m².'.format(pes, alt, imc))
if imc < 18.5:
    print('Está \033[31mabaixo do peso\033[m!')
elif 18.5 <= imc < 25:
    print('Está com o \033[32mpeso ideal\033[m, parabéns!')
elif 25 <= imc < 30:
    print('Está com \033[31msobrepeso\033[m!')
elif 30 <= imc <= 40:
    print('Está com \033[31mOBESIDADE\033[m!')
else:
    print('Está com \033[1:31mOBESIDADE MÓRBIDA\033[m, cuidado!')
