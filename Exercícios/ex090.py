# FAÇA UM PROGRAMA QUE LEIA NOME E MÉDIA DE UM ALUNO, GUARDANDO TAMBÉM A SINTUAÇÃO, SE FOR MAIOR OU MENOR DO QUE 7, EM
# UM DICIONÁRIO. NO FINAL, MOSTRE O CONTEÚDO DA ESTRUTURA NA TELA

dic={'nome':input('Digite o nome: '),
     'média': float(input('Digite a média: '))}
if dic['média']>=7:
    dic['sintuação'] = 'APROVADO'
else:
    dic['sintuação'] = 'REPROVADO'

print(f'\nNome é {dic["nome"]}\nMédia é igual a {dic["média"]}\nA sintuação de {dic["nome"]} é {dic["sintuação"]}')