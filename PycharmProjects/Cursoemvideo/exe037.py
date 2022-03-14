numero = int (input ('INFORME UM NÚMERO INTEIRO: '))
print ('''ESCOLHA A BASE DE CONVERSÃO:
[1] BASE BINÁRIO
[2] BASE OCTAL
[3] BASE HEXADECIMAL''')
base = int (input ('SUA OPÇÃO: '))
if base == 1:
    print ('O VALOR INTEIRO {} CONVERTIDO EM BINÁRIO SERÁ {}'.format (numero , bin(numero)[2:]))
elif base == 2:
    print('O VALOR INTEIRO {} CONVERTIDO EM OCTAL SERÁ {}'.format(numero, oct(numero)[2:]))
elif base == 3:
    print('O VALOR INTEIRO {} CONVERTIDO EM HEXADECIMAL SERÁ {}'.format(numero, hex(numero)[2:]))
print ('BOM DIA')
