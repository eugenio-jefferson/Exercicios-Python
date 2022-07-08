# CRIE  UM PROGRAMA QUE LEIA O DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO NOME.

print('='*10, 'ANALISADOR DE NOMES', '='*10)
nome = str(input('Digite seu nome: ')).title().strip()
print('Analisando o nome {}:\nÉ verdade que tem Silva no seu nome? {}.'.format(nome, 'Silva' in nome))