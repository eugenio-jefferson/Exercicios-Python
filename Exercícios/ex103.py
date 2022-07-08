# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA FICHA(), QUE RECEBA DOIS PARÂMETROS OPCIONAIS: O NOME DE UM JOGADOR E
# QUANTOS GOLS ELE MARCOU. O PROGRAMA DEVERÁ SER CAPAZ DE MOSTRAR A FICHA DO JOGADOR, MESMO QUE ALGUM DADO NÃO TENHA
# CIDO INFORMADO CORRETAMENTE.

def ficha(nome:str="",gols:int=0):
    if nome.strip() == '':
        nome='<desconhecidoo>'
    if not gols.isnumeric():
        gols=0
    print(f'O jogador {nome} fez {gols} no campeonato.')

ficha(str(input('Nome do jogador: ')),input('Quantos gols ele fez: '))