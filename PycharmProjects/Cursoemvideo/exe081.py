numeros = list()
resposta = 0
while resposta != 'N':
    numeros.append(int(input ('DIGITE UM NUMERO: ')))
    resposta = str (input ('DESEJA CONTINUAR [S/N]: ')).upper()
print ('=-'*35)
print (f'VOCE DIGITOU {len(numeros)} NUMEROS')
print ('=-'*35)
numeros.sort(reverse=True)
print (f'OS VALORES EM ORDEM DECRESCENTE FORAM {numeros}')
print ('=-'*35)
if 5 in numeros:
    print ('O NUMERO 5 FOI DIGITADO E ESTA NA LISTA')
else:
    print ('O NUMERO 5 NÃO FOI DIGITADO')