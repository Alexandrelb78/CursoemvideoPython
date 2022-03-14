def fatorial(n, show=False):
    """
    Calcula o Fatorial de um número.
    :param n: O numero a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    c = n
    f = 1
    while c > 0:
        f = f * c
        c = c - 1
        if show:
            print (f'{c} x', end=' ')
    return f'O FATORIAL DE {n} É IGUAL A {f}'


n = int(input('DIGITE UM NUMERO PARA SEU FATORIAL: '))
print (fatorial(n, show=True))
help(fatorial)