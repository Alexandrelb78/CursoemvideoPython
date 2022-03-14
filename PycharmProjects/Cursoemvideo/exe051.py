n = int (input ('DIGITE UM NUMERO: '))
r = int (input ('DIGITE A RAZAO DA PROGRESSAO: '))
dec = n + (10 - 1) * r
for c in range (n, dec + r , r):
    print (c)
print ('FIM')
