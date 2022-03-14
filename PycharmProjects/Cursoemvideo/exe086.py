matriz = []
for a in range (0 , 3):
    matriz.append(int(input (f'DIGITE UM VALOR PARA [0 , {a}]: ')))
for b in range (0 , 3):
    matriz.append(int(input (f'DIGITE UM VALOR PARA [1 , {b}]: ')))
for c in range (0 , 3):
    matriz.append(int(input (f'DIGITE UM VALOR PARA [2 , {c}]: ')))
print ('-='*30)
print(f'[ {matriz[0]:^5} ]  [ {matriz[1]:^5} ]  [ {matriz[2]:^5} ]')
print(f'[ {matriz[3]:^5} ]  [ {matriz[4]:^5} ]  [ {matriz[5]:^5} ]')
print(f'[ {matriz[6]:^5} ]  [ {matriz[7]:^5} ]  [ {matriz[8]:^5} ]')
print ('=-'*30)

