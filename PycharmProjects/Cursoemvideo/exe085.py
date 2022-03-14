numeros = [[], []]
valor = 0
for n in range (1 , 8):
    valor = int(input(f'DIGITE UM NUMERO {n} : '))
    if valor %2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print ('=-'*30)
numeros[0].sort()
numeros[1].sort()
print (f'OS NUMEROS PARES SÃO {numeros[0]} ', end='')
print (f'OS NUMEROS IMPARES SÃO {numeros[1]}!')
