# CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA. DEPOIS DISSO CRIE DUAS LISTA EXTRAS QUE VÃO
# CONTER APENAS OS VALORES PARES E OS VALORES ÍMPARES DIGITADOS, RESPECTIVAMENTE. NO FINAL MOSTRE AS TRÊS LISTAS.

list= []
resp='s'
while not resp.lower() in 'n':
    list.append(int(input('Digite um número: ')))
    resp=input('Quer continuar? [S|N]: ')

print(f'Lista com os números que você digitou: {list};')
listpar=[]
listimp=[]
for num in list:
    if num%2==0:
        listpar.append(num)
    else:
        listimp.append(num)
print(f'Lista com os números pares: {listpar};')
print(f'Lista com os números ímpares {listimp};')