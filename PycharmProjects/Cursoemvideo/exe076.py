produtos = ('BOLO 15 FATIAS', 15, 'BOLO 10 FATIAS', 10, 'SACOLE', 2, 'SACOLE GOURMET', 5, 'BOLO NO POTE', 8)
print ('-'*50)
print (f'{"ATELIE DA PATY":^50}')
print ('-'*50)
for pos in range (0 , len (produtos)):
    if pos % 2 == 0:
        print (f'{produtos[pos]:.<40}', end = '')
    else:
        print (f'R${produtos[pos]:>7.2f}')
print ('-'*50)