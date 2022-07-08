#DESENVOLVA UM PROGRAMA QUE LEIA QUATROS VALORES PELO TECLADO E GUARDE-OS EM UMA TUPLA. NO FINAL MOSTRE:
# A) QUANTAS VEZES APARECEU O VALOR 9. B) EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3. C) QUAIS FORAM OS NÚMEROS PARES.

tupla=(int(input('Digite o 1° número: ')),int(input('Digite o 2° número: ')),int(input('Digite o 3° número: ')),
       int(input('Digite o 4° número: ')))

print(f'O número 9 foi digitado {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O primeiro número 3 apareceu na {tupla.index(3)+1}ª posição.')
print("Os números pares são: ",end='')
for n in tupla:
    if n % 2==0:
        print(n,end=', ')