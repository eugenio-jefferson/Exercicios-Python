# CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VÁRIOS PRODUTOS. O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO VAI CONTINUAR
# NO FINAL MOSTRE: A) QUAL É O TOTAL GASTO NA COMPRA; B) QUANTOS PRODUTOS CUSTAM MAIS DE R$ 1000; C) QUAL É O NOME DO
# PRODUTO MAIS BARATO.

print('=-='*15 + f'\n{"LISTA DE COMPRAS":^45}\n' + '=-='*15)
mais_de_1000 = total_gasto = preço_barato = 0

while True:
    nome = str(input('Nome do produto: ')).strip().lower()
    preço = float(input('Preço do produto: R$ '))

    total_gasto += float(preço)

    if preço > 1000:
        mais_de_1000 += 1

    if preço_barato == 0 or preço < preço_barato:
        preço_barato = preço
        nome_barato = nome

    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S / N] ')).strip().lower()[0]
    print('---'*15)
    if continuar == 'n':
        break

print(f'''\nO valor total gasto na compra foi de R${total_gasto:.2f}.
{mais_de_1000} {"produtos" if mais_de_1000 > 1 else "produto"} custa mais de R$ 1000,00.
{nome_barato} é o produto mais barato, custando R$ {preço_barato:.2f}.''')