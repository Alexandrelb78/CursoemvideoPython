pma = 0
pme = 0
for p in range (1,6):
    peso = float (input ('O PESO DA {} PESSOA: '.format (p)))
    if p == 1:
        pma = peso
        pme = peso
    else:
        if peso > pma:
            pma = peso
        if peso < pme:
            pme = peso
print ('O MAIOR PESO ENTRE OS CINCO PARTICIPANTES É {}.'.format (pma))
print ('O MENOR PESO ENTRE OS CINCO PARTICIPANTES É {}.'.format (pme))