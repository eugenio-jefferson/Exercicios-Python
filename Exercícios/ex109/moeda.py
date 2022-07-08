def aumentar(v,p,format=True):
    p /=100
    a = (v*p)+v
    if format:
        return moeda(a)
    else:
        return a

def dirminuir(v,p,format=True):
    a = v-(v*(p/100))
    return a if not format else moeda(a)

def dobro(v,format=True):
    if format:
        return moeda(v*2)
    else:
        return v*2

def metade(v,format=True):
    if format:
        return moeda(v/2)
    else:
        return v/2

def moeda(v=0,moeda='R$'):
    p=str(f'{moeda} {v:.2f}')
    return p.replace('.',',')
