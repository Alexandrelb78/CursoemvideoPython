n1 = int (input ('DIGITE O PRIMEIRO NUMERO: '))
n2 = int (input ('DIGITE O SEGUNDO NUMERO: '))
n3 = int (input ('DIGITE O TERCEIRO NUMERO: '))
n4 = int (input ('DIGITE O QUARTO NUMERO: '))
lista = (n1, n2, n3, n4)
print (f'VOCE DIGITOU OS SEGUINTES NÚMEROS {lista}')
print (f'O NUMERO 9 APARECE {lista.count(9)} VEZES')
if 3 in lista:
    print (f'O NUMERO 3 ESTÁ NA {lista.index(3)+1}ª POSIÇÃO')
else:
    print ('O NUMERO 3 NÃO FOI DIGITADO EM NENHUMA POSIÇÃO')
print ('OS VALORES PARES DIGITADOS FORAM ', end = ' ')
for n in lista:
    if n % 2 == 0:
        print (n , end=' ')