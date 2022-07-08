# ADAPTE O CÓDIGO DO DESAFIO 107, CRIANDO UMA FUNÇÃO ADICIONAL CHAMADA MOEDA() QUE CONSIGA MOSTRAR OS VALORES
# COMO UM VALOR MONETÁRIO FORMATADO.

import moeda

p = float(input('Digite um preço: R$ '))
print(f'Aumentando 10% de {moeda.moeda(p)} temos {moeda.moeda(moeda.aumentar(p,10))};')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))};')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))};')