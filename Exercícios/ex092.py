# CRIE UM PROGRAMA QUE LEIA NOME, ANO DE NASCIMENTO E CARTEIRA DE TRABALHO, E CADASTRE-OS (C0M IDADE) EM UM DICIONÁRIO
# SE POR ACASO O CTPS FOR DIFERENTE DE ZERO, O DICIONÁRIO TAMBÉM RECEBERAR O ANO DE CONTRATAÇÃO E O SALÁRIO. CALCULE E
# ACRESCENTE, ALÉM DA IDADE, COM QUANTOS ANOS A PESSOA VAI SE APOSENTAR, COM 35 DE CONTRIBUIÇÃO;

import datetime

dic={
    'Nome': str(input('Digite o nome: ')),
}

nasc=int(input('Digite ano de nascimento: '))
dic['Idade'] = int(datetime.date.today().year-nasc)
dic['CTPS'] = int(input('Digite o número da carteira de trabalho: [0 para não tem] '))

if dic['CTPS'] != 0:
    dic['Ano de contratação']=int(input('Digite o ano de contratação: '))
    dic['Salário']=int(input('Digite o valor do salário: R$ '))
    dic['Aposentadoria']=int((dic['Ano de contratação']+35)-nasc)
    for k,v in dic.items():
        print(f' - {k} é {v};')


else:
    print('-'*40)
    for k,v in dic.items():
        print(f' - {k} é {v};')