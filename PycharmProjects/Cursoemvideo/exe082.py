numeros = []
par = []
impar = []
while True:
    numeros.append(int (input ('DIGITE UM NUMERO: ')))
    resp = str (input ('DESEJA CONTINUAR [S/N]: ')).upper()
    if resp == 'N':
        break
print (f'A LISTA COMPLETA É {numeros}')
for i, v in enumerate(numeros):
    if v %2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print ('=-'*30)
print (f'OS NUMEROS PARES DIGITADOS FORAM {par}')
print ('=-'*30)
print (f'OS NUMEROS IMPARES DIGITADOS FORAM {impar}')