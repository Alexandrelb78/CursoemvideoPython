from datetime import date
aluno = str (input ('NOME DO ALUNO: '))
anonas = int (input ('ANO DE NASCIMENTO: '))
cat = ((date.today().year) - anonas)
if cat <= 9:
    print ('O ATLETA {} ESTÁ NA CATEGORIA MIRIM.'.format (aluno))
elif cat <= 14:
    print ('O ATLETA {} ESTÁ NA CATEGORIA INFANTIL.'.format(aluno))
elif cat <= 19:
    print('O ATLETA {} ESTÁ NA CATEGORIA JUNIOR.'.format(aluno))
elif cat <= 25:
    print('O ATLETA {} ESTÁ NA CATEGORIA SENIOR.'.format(aluno))
else:
    print('O ATLETA {} ESTÁ NA CATEGORIA MASTER.'.format(aluno))
    
