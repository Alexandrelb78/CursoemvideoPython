print ('{:=^40}'.format ('LOJAS FITNESS CG'))
valor = float (input ('QUAL O VALOR DO PRODUTO: R$  '))
print ('FORMA DE PAGAMENTO')
print ('-=-'*20)
print ('ESCOLHA 1 PARA DINHEIRO OU CHEQUE A VISTA. (OBS: 10% DE DESCONTO): ')
print ('-=-'*20)
print ('ESCOLHA 2 PARA CARTÃO A VISTA. (OBS: 5% DE DESCONTO): ')
print ('-=-'*20)
print ('ESCOLHA 3 PARA CARTÃO EM 2 VEZES: ')
print ('-=-'*20)
print ('ESCOLHA 4 PARA CARTÃO EM 3 OU MAIS VEZES. (OBS: 20% DE JUROS): ')
print ('-=-'*20)
forma = int (input ('ESCOLHA A FORMA DE PAGAMENTO: '))
if forma == 1:
    vista = valor - (valor * 10/100)
    print ('O VALOR A SER PAGO É DE {}.'.format (vista))
elif forma == 2:
    vista = valor - (valor * 5/100)
    print ('O VALOR A SER PAGO É DE {}.'.format (vista))
elif forma == 3:
    cartao = valor / 2
    print ('O VALOR A SER PAGO EM 2 VEZES NO CARTÃO É DE {}.'.format (cartao))
elif forma == 4:
    cartao = valor + (valor * 20/100)
    parc = int (input ('QUANTAS PARCELAS: '))
    totalparc = cartao / parc
    print ('SUA COMPRA SERÁ PARCELADA EM {} VEZES DE {:.2f}.'.format (parc,totalparc))
    print ('O VALOR A SER PAGO É DE {} NO CARTÃO.'.format (cartao))
else:
    forma = 0
    print ('OPÇÃO INVALIDA DE PAGAMENTO. TENTE NOVAMENTE')


