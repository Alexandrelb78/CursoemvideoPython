cont = total = prod = quant = valor = caro = barato = 0
nomeprod= ''
print ('=*'*25)
print ('CASAS PONTO FRIO')
print ('=*'*25)
while True:
    prod = str (input ('NOME DO PRODUTO: ')).upper().strip()
    valor = float (input ('VALOR DO PRODUTO: R$  '))
    cont = cont + 1
    total = total + valor
    if cont == 1 or valor < barato:
        valor = barato
        nomeprod = prod
    if valor > 1000:
        quant = quant + 1
    op = str(input('DESEJA CONTINUAR [S/N]: ')).upper().strip()
    if op == 'N':
        break
print ('=-'*25)
print ('FINAL DAS COMPRAS')
print ('=-'*25)
print (f'O TOTAL DE COMPRAS FOI R$ {total}')
print (f'TEMOS {quant} PRODUTOS QUE CUSTAM MAIS DE R$ 1000,00')
print (f'O PRODUTO MAIS BARATO FOI {nomeprod} QUE CUSTA R$ {barato}.')
