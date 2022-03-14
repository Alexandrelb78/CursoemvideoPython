exp = []
exp.append(str (input('DIGITE UMA EXPRESSÃO: ')))
for i, abre in enumerate(exp):
    if '(' in abre:
        abre.count('(')
for i, fecha in enumerate(exp):
    if ')' in fecha:
        fecha.count(')')
    if abre.count('(') == fecha.count(')'):
        print ('SUA EXPRESSÃO É VALIDA!!!!')
    else:
        print ('SUA EXPRESSÃO É INVALIDA!!!')


