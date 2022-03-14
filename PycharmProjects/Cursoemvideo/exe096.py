def resp():
    print (f'A AREA DE UM TERRENO {larg} X {comp} É DE {area}mª.')

print ('=-'*30)
print ('CONTROLE DE TERRRENOS')
print ('=-'*30)
larg = float (input ('LARGURA[m]: '))
comp = float (input ('COMPRIMENTO[m]: '))
area = larg * comp
resp()