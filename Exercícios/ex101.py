# CRIE UM PROGRAMA COM UMA FUNÇÃO CHAMADA VOTO() QUE VAI RECEBER COMO PARÂMETRO O ANO DE NASCIMENTO DE UMA PESSOA,
# RETORNANDO UM VALOR LITERAL INDICANDO SE A PESSOA TEM VOTO NEGADO, OPCIONAL OU OBRIGATÓRIO NAS ELEIÇÕES.

def voto(an):
    from datetime import datetime
    id =datetime.now().year-an

    if 16 <= id <18 or id >70:
        return f'Com {id} anos o voto é OPCIONAL.'
    elif 18 <= id <= 70:
        return f'Com {id} anos o voto é OBRIGATÓRIO.'
    elif id < 16:
        return f'Com {id} anos o voto é NEGADO.'

print(voto(int(input('Em que ano você nasceu? '))))

