# FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE VALORES 'M' OU 'F'. CASO ESTEJA ERRADO PEÇA A DIGITAÇÃO
# NOVAMENTE ATÉ TER UM VALOR CORRETO.

print('\033[35m='*10, '\033[33mVALIDAÇÃO DE DADOS', '\033[35m=\033[m'*10)
sexo = str(input('Informe seu sexo [M/F]: ')).strip().lower()[0]
while not sexo in 'mf':
    sexo = str(input('Dado invalido. Informe seu sexo: ')).strip().lower()[0]
print('Sexo {} validado!'.format(sexo))