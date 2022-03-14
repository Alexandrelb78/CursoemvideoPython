numeros = list()
for cont in range (0 , 5):
    numeros.append(int (input (f'DIGITE UM PARA A POSIÇAO {cont} : ')))
print ('=-'*20)
print (f'VOCE DIGITOU OS VALORES {numeros}')
print (f'O MAIOR VALOR DIGITADO FOI {max(numeros)} NA POSIÇAO  ', end='')
for i, v in enumerate (numeros):
    if v == max(numeros):
        print (f'{i}...', end='')
print ()
print (f'O MENOR VALOR DIGITADO FOI {min(numeros)} NA POSIÇÃO  ', end='')
for i, v in enumerate (numeros):
    if v == min(numeros):
        print (f'{i}...', end='')


