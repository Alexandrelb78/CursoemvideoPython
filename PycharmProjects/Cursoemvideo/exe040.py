nome = str (input ('DIGITE O NOME DO ALUNO: '))
nota1 = float (input ('DIGITE A PRIMEIRA NOTA: '))
nota2 = float (input ('DIGITE A SEGUNDA NOTA: '))
media =(( nota1 + nota2 ) / 2)
if media < 5.0:
    print ('O ALUNO {} FOI REPROVADO COM A MÉDIA {:.2F}.'.format (nome , media))
elif media == 5.0 or media <= 6.9:
    print ('O ALUNO {} ESTÁ EM RECUPERAÇÃO COM A MÉDIA {:.2F}.'.format (nome , media))
elif media >= 7.0:
    print('O ALUNO {} ESTÁ APROVADO COM A MÉDIA {:.2F}, PARABENS.'.format(nome, media))