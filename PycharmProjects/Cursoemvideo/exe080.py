valores = list()
for c in range (0 , 5):
    n = int (input ('DIGITE UM NUMERO: '))
    if c == 0 or n > valores [-1]:
        valores.append(n)
        print ('ADICIONADO AO FINAL DA LISTA...')
    else:
        pos = 0
        while pos < len (valores):
            if n <= valores [pos]:
                valores.insert(pos, n)
                print (f'ADICIONADO NA POSIÇÃO {pos} DA LISTA...')
                break
            pos = pos + 1
print ('=-'*30)
print (f'OS VALORES DIGITADOS FORAM {valores}')


