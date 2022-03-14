sidade = 0
midade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range (1, 5):
    print ('-'*5,'{} PESSOA'.format(c), '-'*5)
    nome = str (input ('QUAL O SEU NOME: ')).strip()
    idade = int (input ('SUA IDADE: '))
    sexo = str (input ('SEXO [M / F]: ')).strip()
    sidade = sidade + idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1

midade = sidade / 4
print ('A MEDIA DE IDADE DO GRUPO É DE {} ANOS.'.format (midade))
print ('O HOMEM MAIS VELHO TEM {} ANOS E SE CHAMA {}. '.format (maioridadehomem, nomevelho))
print ('AO TODO SÃO {} MULHERES COM MENOS DE 20 ANOS'.format (totmulher20))
