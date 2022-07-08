#CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VÁRIAS PALAVRAS (NÃO USAR ACENTOS). DEPOIS DISSO VOCÊ DEVE MOSTRAR PARA CADA
# PALAVRA QUAIS SÃO SUAS VOGAIS

tupla=('AROZ','CARNE','FEIJAO','BRIOCU')
for i in tupla:
    print(f'Na palavra {i} temos: ',end='')
    for l in i:
        if l.upper() in'AEIOU':
            print(l,end=' ')
    print('')