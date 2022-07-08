# FAÇA UM PROGRAMA QUE LEIA NOME E PESO DE VÁRIAS PESSOAS, GUARDANDO TUDO EM UMA LISTA, NO FINAL MOSTRE:
# A) QUANTAS PESSOAS FORAM CADASTRADAS; B) UMA LISTA COM AS PESSOAS MAIS PESADAS; C) UMA LISTA COM AS PESSOAS MAIS LEVES;

pessoas=[]
cont='s'
while not cont.upper() in 'N':
    dados=[str(input('Nome: ')), float(input('Peso: '))]
    pessoas.append(dados[:])
    cont=input('Quer continuar? [S|N]: ')

print(f'Você cadastrou {len(pessoas)} pessoas.')
maispeso= menospeso= n=c=0
for p in pessoas:
    for i,v in enumerate(p):
        if i==1 and v>=maispeso:
            maispeso=v
            if n==0:
                menospeso=v
        if i==1 and v<=menospeso:
            menospeso=v if i==1 else 0
        if c==0:
            pass
        else:
            n+=1
    c+=1
print(f'O maior peso é {maispeso}kg, de ',end='')
n=0
for d in pessoas:
    for i,v in enumerate(d):
        if v==maispeso:
            print(f'{pessoas[n][i-1]}',end='; ')
    n+=1
print(f'\nO menor peso é {menospeso}kg, de ',end='')
n=0
for d in pessoas:
    for i, v in enumerate(d):
        if v==menospeso:
            print(pessoas[n][i-1],end='; ')
    n+=1