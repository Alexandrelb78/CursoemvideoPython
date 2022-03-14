def aumentar(n=0,a=0, show = False):
    mais = n + (n*a/100)
    return mais if show is False else moeda (mais)


def diminuir(n=0,d=0, show = False):
    menos = n - (n*d/100)
    return menos if show is False else moeda (menos)


def dobro(n=0, show = False):
    dob = n * 2
    return dob if show is False else moeda (dob)


def metade(n=0, show = False):
    met = n / 2
    return met if show is False else moeda (met)


def moeda( n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


