# FAÇA UM MINI-SISTEMA QUE ULTILIZE O INTERACTIVE HELP DO PYTHON. O USUÁRIO VAI DIGITAR O COMANDO E O MANUAL VAI
# APARECER. QUANDO O USUÁRIO DIGITAR A PALAVRA FIM, O PROGRAMA SE ENCERRARÁ.

r=''
while not r.strip().lower()=='fim':
    r=input('Digite um comando [FIM para sair]: ').strip().lower()
    if r!='fim':
        help(r)
    else:
        print('Saindo..')
