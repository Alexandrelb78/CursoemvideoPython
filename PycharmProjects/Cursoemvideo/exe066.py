s = n = c = 0
print('-=' * 25)
print('VAMOS INSERIR NUMEROS, SE QUISER PARA DIGITE 999')
print('-=' * 25)
while True:
    n = int (input ('DIGITE UM NÚMERO: '))
    if n == 999:
        break
    c = c + 1
    s = s + n
print (f'A SOMA DOS {c} VALORES FOI {s}!')
print ('FIM')
