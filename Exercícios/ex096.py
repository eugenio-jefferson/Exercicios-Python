# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ÁREA(), QUE RECEBA AS DIMENSÕES DE UM TERRENO RETANGULAR (LARGURA E
# COMPRIMENTO) E MOSTRE A ÁREA DO TERRENO.

def área(l,c):
    print(f'A área do terro com {l}x{c} é de {l*c:.2f}m².')

área(float(input('Largura: ')), float(input('Comprimento: ')))