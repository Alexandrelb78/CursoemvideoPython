from random import randint
from time import sleep
numeros = []
pares = []


def sorteia():
    for c in range (0, 5):
        n = randint(1, 10)
        sleep(0.5)
        print (n, end= ' ')
        numeros.append(n)


def somapar():
    for p, par in enumerate (numeros):
        if par %2 == 0:
            pares.append(par)
    somapares = sum(pares)
    print (somapares)


print ('SORTEANDO 5 VALORES DA LISTA: ', end= ' ')
sorteia()
print ('PRONTO!!!')
print (f'A SOMA DOS VALORES PARES DA LISTA {numeros} É', end=' ')
somapar()
print ('FIM')
