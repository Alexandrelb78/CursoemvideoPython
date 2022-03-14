txt = str
def imprima (txt):
    tamanho = (len(txt) + 4)
    print ('#' * tamanho)
    print (f'  {txt}')
    print ('#' * tamanho)


imprima('VASCO DA GAMA')
imprima('FLAMENGO')
imprima('BOTA')
