def aumentar(n=0,a=0):
    mais = n + (n*a/100)
    return mais


def diminuir(n=0,d=0):
    menos = n - (n*d/100)
    return menos


def dobro(n=0):
    dob = n * 2
    return dob


def metade(n=0):
    met = n / 2
    return met


def moeda( n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


