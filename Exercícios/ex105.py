# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO NOTAS() QUE PODE RECEBER VÁRIAS NOTAS DE UM ALUNO E VAI RETORNAR UM DICIONÁRIO
# COM AS SEGUINTES INFORMAÇÕES: - QUANTIDADE DE NOTAS; - A MAIOR NOTA; - A MENOR NOTA; - A MÉDIA DA TURMA;
# - A SINTUAÇÃO (OPCIONAL); ADICIONE TAMBÉM AS DOCSTRINGS DA FUNÇÃO.

def notas(*n,sit:bool=False):
    """
     - Analisa várias notas e da um relatório
    :param n: informe várias notas
    :param sit: mostrar ou não a sintuação
    :return: retorna várias informações
    """
    dic={'total': len(n)}
    mai=men=n[0]
    media=0
    for notas in n:
        if notas > mai:
            mai=notas
        if notas <men:
            men= notas
        media+=notas

    dic['maior'] = mai
    dic['menor'] = men
    media/=len(n)
    dic['média'] = f'{media:.2f}'

    if sit:
        if 5 <= media < 7:
            dic['situação'] ='RAZOÁVEL'
        elif media >= 7:
            dic['situação'] = 'BOA'
        else:
            dic['situação'] = 'RUIM'

    return dic

print(notas(5,2,7,1, sit=True))

help(notas)