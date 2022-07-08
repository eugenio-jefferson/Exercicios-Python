# CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR SETE VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA ÚNICA QUE MANTEM
# SEPARADOS OS VALORES PARES E ÍMPARES. NO FINAL MOSTRE OS VALORES PARES E ÍMPARES EM ORDEM CRESCENTES.

lista= [[],[]]
for c in range(1,8):
    num=int(input(f'Digite o {c}º número: '))
    if num %2==0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print(f'Os números pares digitados foram: {sorted(lista[0])}')
print(f'Os números ímpares digitados foram: {sorted(lista[1])}')