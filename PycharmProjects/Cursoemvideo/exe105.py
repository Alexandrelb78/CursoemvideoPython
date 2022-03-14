def notas (*n, sit=False):
    r = dict()
    r ['TOTAL'] = len(n)
    r ['MAIOR'] = max(n)
    r ['MENOR'] = min(n)
    r ['MEDIA'] = sun(n)/len(n)
    if sit:
        if r['MEDIA'] >=7:
            r['SITUACAO'] = 'BOA'
        elif r['MEDIA'] >=5:
            r['SITUACAO'] = 'RAZOAVEL'
        else:
            r['SITUACAO'] = 'RUIM'
    return r


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
