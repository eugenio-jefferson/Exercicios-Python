# CRIE UM MÓDULO CHAMADO MOEDA.PY QUE TENHA AS FUNÇÕES INCORPORADAS, AUMENTAR(),DIRMINUIR(),DOBRO() E METADE(). FAÇA
# TAMBÉM UM PROGRAMA QUE IMPORTE ESSE MÓDULO E USE ALGUMAS DESSAS FUNÇÕES.

import moeda

p = float(input('Digite um preço: R$'))
print(f'Aumentando 10% de R${p:.2f}, temos R${moeda.aumentar(p,10):.2f};')
print(f'O dobro de R${p:.2f} é R${moeda.dobro(p):.2f};')
print(f'A metade de R${p:.2f} é R${moeda.metade(p):.2f};')