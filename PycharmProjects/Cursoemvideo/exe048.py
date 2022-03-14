soma = 0
cont = 0
for c in range (1 , 501, 2):
    if (c) % 3 == 0:
        cont = cont + 1
        soma = soma + c
print ('A SOMA DE TODOS OS {} IMPARES E MULTIPLOS DE 3 DE 1 A 500 É {}'.format (cont, soma))
print ('FIM')


