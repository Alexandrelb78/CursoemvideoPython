palavras = ('vasco','flamengo','botafogo','fluminense','arsenal','juventos')
for p in palavras:
    print (f'\n  NA PALAVRA {p.upper()} TEMOS ', end = ' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print (letra, end = ' ')
