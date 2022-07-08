# CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCALOS EM UMA LISTA. DEPOIS DISSO, MOSTRE: A) QUANTOS NÚMEROS
# FORAM DIGITADOS. B) A LISTA DE VALORES ORDENADA DE FORMA DECRESCENTE. C) SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LISTA

lista= list()
conti='s'
while not conti in 'Nn':
    lista.append(int(input('Digite um número: ')))
    conti = input('Quer digitar outro número? [S|N}: ')

print(f'Você digitou {len(lista)} números;')
print(f'A lista na ordem decrescente é {sorted(lista, reverse=True)};')
if 5 in lista:
    print('O número 5 está na lista;')
else:
    print('O número 5 não foi digitado;')