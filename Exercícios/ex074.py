#CRIE UM PROGRAMA QUE VAI GERAR CINCO NÚMEROS ALEATÓRIOS E COLOCAR EM UMA TUPLA. DEPOIS DISSO MOSTRE A LISTAGEM DE NÚMEROS
# GERADOS E TAMBÉM INDIQUE O MENOR E O MAIOR VALOR QUE ESTÃO NA TUPLA.

from random import randint

tupla=(int(randint(0,10)),int(randint(0,10)),int(randint(0,10)),int(randint(0,10)),int(randint(0,10)))

menor = maior = cont=int(0)
for item in tupla:
    if item> maior:
        maior=item
        if cont == 0:
            menor=maior
    if item<menor:
        menor=item
    cont+=1
print(f'Os números sorteados foram: {tupla};')
print(f'O maior número é: {maior};')
print(f'O menor número é: {menor};')