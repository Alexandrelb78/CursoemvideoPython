aluno = {}
aluno['NOME'] = str (input('DIGITE O NOME DO ALUNO: ')).upper()
aluno['MEDIA'] = float (input(f'DIGITE A MÉDIA DO {aluno["NOME"]}: '))
if aluno['MEDIA'] >= 7:
    aluno['SITUAÇÃO'] = 'APROVADO'
elif 5 <= aluno ['SITUAÇÃO'] < 7:
    aluno['SITUAÇÃO'] = 'RECUPERAÇÃO'
else:
    aluno['SITUAÇÃO'] = 'REPROVADO'
print (f'O NOME DO ALUNO É {aluno["NOME"]}')
print (f'A MÉDIA É IGUAL A {aluno["MEDIA"]}')
print (f'A SITUAÇÃO DE {aluno["NOME"]} É {aluno["SITUAÇÃO"]}.')
