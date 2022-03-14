soma = 0
cont = 0
for c in range (1,7):
    n = int (input ('DIGITE UM NÚMERO: '))
    if n % 2 == 0:
       soma = soma + n
       cont = cont + 1
print ('A SOMA DOS {} NUMEROS PARES DIGITADOS É {}'.format (cont, soma))
