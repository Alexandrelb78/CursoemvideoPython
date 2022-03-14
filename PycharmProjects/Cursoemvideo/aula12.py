nome = str (input ('QUAL O SEU NOME: '))
nome.upper()
if nome == 'GUSTAVO':
    print ('QUE NOME BONITO!')
elif nome == 'ALEXANDRE' or nome == 'MARIA' or nome == 'PEDRO':
    print ('SEU NOME É BEM POPULAR, {}!'.format (nome))
else:
    print ('SEU MOME É BEM NORMAL.')

print ('TENHA UM BOM DIA {}'.format(nome))
