# FAÇA UM PROGRAMA QUE LEIA UM FRASE PELO TECLADO E MOSTRE: QUANTAS VEZES APARECE A LETRA "A". EM QUE POSIÇÃO ELA
# APARECE A PIMEIRA VEZ. EM QUE POSIÇÃO ELA APRECE A ULTIMA VEZ.

print('='*10, 'ANALISADOR DE FRASES', '='*10)
frase = str(input('Digite uma frase: ')).strip().lower()
print('A frase que você digitou tem:\n{} Letras "A".'.format(frase.count('a')))
print('O primeiro "A" aparece na posição {}.'.format(frase.find('a')+1))
print('O último "A" apareceu na posição {}.'.format(frase.rfind('a')+1))