def aumentar(n,a):
    mais = n + (n*a/100)
    return mais


def diminuir(n,d):
    menos = n - (n*d/100)
    return menos


def dobro(n):
    dob = n * 2
    return dob


def metade(n):
    met = n / 2
    return met


def moeda():
    print (f'R$ {aumentar(n,a)}')
    print (f'R$ {diminuir(n,d)}')
    print (f'R$ {dobro(n)}')
    print (f'R$ {metade(n)}')

