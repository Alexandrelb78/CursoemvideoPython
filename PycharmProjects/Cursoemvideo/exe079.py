Lista = []
resposta=0
while resposta != 'N':
    num = int (input('DIGITE UM NUMERO: '))
    if num not in Lista:
        Lista.append(num)
        print ('NUMERO INSERIDO COM SUCESSO!!!')
    else:
        print ('NUMERO JÁ DIGITADO, INSIRA OUTRO POR FAVOR!!!')

    resposta = str(input('QUER CONTINUAR [S/N]: ')).upper()
Lista.sort()
print('=-'*35)
print(f'VOCE DIGITOU OS SEGUINTES NUMEROS {Lista}')


