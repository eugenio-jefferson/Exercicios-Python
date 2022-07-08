def aumentar(v,p):
    p /=100
    a = (v*p)+v
    return a

def dirminuir():
    pass

def dobro(v):
    return v*2

def metade(v):
    return v/2

def moeda(v=0,moeda='R$'):
    p=str(f'{moeda} {v:.2f}')
    return p.replace('.',',')
