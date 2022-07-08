# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO COM A PALAVRA "SANTO".

print('='*10, 'VERIFICANDO NOMES DE CIDADES', '='*10)
nome = str(input('Digite o nome de uma cidade: ')).title().strip()
print('O nome da cidade {}, começa com Santo? {}.'.format(nome, 'Santo' in nome[:5]))