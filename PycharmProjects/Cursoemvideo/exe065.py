s = num = c = maior = menor = 0
num = 0
opcao = 0
print ('MAIOR E MENORES VALORES')
print ('-='*20)
while opcao != 'N':
    num = int (input ('DIGITE UM NÚMERO: '))
    opcao = str(input ('QUER CONTINUAR? [S/N]' )).upper().strip()
    c = c + 1
    s = s + num
    media = s / c
    if c == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print ('VOCÊ DIGITOU {} NÚMEROS E A MÉDIA FOI {}'.format (c,media))
print ('O MAIOR VALOR FOI {} E O MENOR FOI {}'.format (maior , menor))
print ('FIM')