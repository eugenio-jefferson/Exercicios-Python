# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM SUA IDADE: -SE ELE AINDA VAI SE
# ALISTAR AO SERVIÇO MILITAR, -SE É A HORA DE SE ALISTAR, -SE JÁ PASSOU DO TEMPO DO ALISTAMENTO. SEU PROGRAMA TAMBÉM
# DEVE MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO.

print('\033[35m-='*10, '\033[33mALISTAMENTO MILITAR', '\033[35m-=\033[m'*10)
from datetime import date
nasc = int(input('Em que ano você nasceu? '))
sex = str(input('Você é homem ou mulher? ')).lower().strip()
alis = str(input('Você já se alistou no serviço militar? ')).lower().strip()
ano = date.today().year
idade = ano - nasc
print('\033[35m=-=\033[m'*20)
if alis == 'não':
    print('Quem nasceu em {} tem {} em {}.'.format(nasc, idade, ano))
if alis == 'sim':
    print('Que bom que você está com seus deveres militares em dia!')
elif sex == 'mulher':
    print('''\033[31mVocê não é obrigada a se alistar no serviço militar\033[m!
Mas caso queira é só ter 18 anos ou mais.''')
elif idade < 18:
    print('''Ainda \033[31mfaltam {} anos\033[m para você se alistar no serviço militar.
O ano do seu alistamento será em {}!'''.format(18 - idade, nasc + 18))
elif idade == 18:
    print('Já \033[31mestá na hora\033[m de você se alistar!')
else:
    print('''Já \033[31mpassou do tempo\033[m de você se alistar, deveria ter se alistado a {} anos!
O ano do seu alistamento foi em {}!'''.format(idade - 18, nasc + 18))
