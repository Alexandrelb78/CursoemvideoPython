from datetime import date
ano = int (input ('DIGITE SEU ANO DE NASCIMENTO: '))
alist = ((date.today().year) - ano)
if alist < 18:
    print ('VOCÊ AINDA NÃO ESTÁ COM IDADE PARA O ALISTAMENTO MILITAR, FALTAM {} ANOS.'.format (18-alist))
elif alist == 18:
    print ('VOCÊ ESTÁ NO ANO DE PRESTAR O SERVIÇO MILITAR, ALISTE-SE')
elif alist > 18:
    print ('VOCÊ PASSOU {} ANOS DO PRAZO PARA O ALISTAMENTO MILITAR. BUSQUE INFORMAÇÕES.'.format (18-alist))