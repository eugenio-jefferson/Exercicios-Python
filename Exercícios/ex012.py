# FAÇA UM ALGORITIMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO

print('='*10, 'CALCULADOR DE 5% DE DESCONTO', '='*10)
v = float(input('Digite o preço de um produto em reais: R$ '))
d = v * (1 - 0.05)
print('O produto de R$ {:.2f}, com 5% de desconto fica por R$ {:.2f}.'.format(v, d))