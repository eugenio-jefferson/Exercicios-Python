# CRIE UM PROGRAMA QUE LEIA NOME, SEXO E IDADE DE VÁRIAS PESSOAS, GUARDANDO OS DADOS DE CADA PESSOA EM UM DICIONÁRIO
# E TODOS OS DICIONÁRIOS EM UMA LISTA. NO FINAL, MOSTRE: A) QUANTAS PESSOAS FORAM CADASTRADAS; B) A MÉDIA DE IDADE DO
# GRUPO; C) UMA LISTA COM TODAS AS MULHERES; D) UMA LISTA COM TODAS AS PESSOAS COM IDADE ACIMA DA MÉDIA;

list= list()
dic={}
resp = 's'
while not resp in 'n':
    dic.clear()
    dic['nome']= str(input('Nome: '))
    while True:
        dic['sexo']=str(input('Sexo [M | F]: ')).lower()
        if dic['sexo'] in 'mf':
            break
        else:
            print('Use apenas "M" ou "F"!')
    dic['idade']= int(input('Idade: '))
    list.append(dic.copy())
    while True:
        resp=str(input('Quer continuar? [S | N]: ')).lower()
        if resp in 'sn':
            break
        else:
            print('Use apenas "S" ou "N"!')
print(f'A) {len(list)} pessoas foram cadastradas;')
média=0
for d in list:
    for k,v in d.items():
        if k =='idade':
            média+=v
média /= len(list)
print(f'B) A média de idade do grupo é de {média:.2f};')
print(f'C) As mulheres cadastradas foram: ',end='')
for d in list:
    for k,v in d.items():
        if k=='sexo' and v=='f':
            print(d['nome'],end=', ')
print(';\nD) Lista das pessoas com idade acima da média: ')
for d in list:
    if d['idade']>média:
        print(f"      Nome = {d['nome']}; Sexo = {d['sexo']}; Idade = {d['idade']};")