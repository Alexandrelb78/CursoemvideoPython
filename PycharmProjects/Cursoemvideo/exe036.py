nome = str (input ('NOME DO COMPRADOR: '))
casa = float (input ('QUAL O VALOR DA CASA: R$ '))
sal = float (input ('QUAL O SALARIO DO COMPRADOR: R$ '))
parc = float (input ('EM QUANTOS ANOS SERÁ PAGO O EMPRESTIMO: '))
prest = casa / parc
if prest <= (sal * 30/100):
    print ('SEU EMPRESTIMO FOI AUTORIZADO {}'.format (nome))
elif prest >= (sal * 30/100):
    print ('O SEU EMPRÉSTIMO NÃO FOI AUTORIZADO, {}'.format (nome))
print ('OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS, BOM DIA {}'.format (nome))



