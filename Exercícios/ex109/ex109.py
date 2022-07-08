# MODIFIQUE AS FUNÇÕES QUE FORAM CRIADAS NO DESAFIO 107 PARA QUE ELAS ACEITEM UM PARÂMETRO A MAIS, INFORMANDO SE O
# VALOR RETORNADO POR ELAS VAI SER OU NÃO FORMATADO PELA  FUNÇÃO MOEDA(), DESENVOLVIDO NO DESAFIO 108.

import moeda

p = float(input('Digite um preço: R$ '))
print(f'Aumentando 10% de {moeda.moeda(p)} temos {moeda.aumentar(p,10)};')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p)};')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p)};')