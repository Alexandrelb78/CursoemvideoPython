fras = str (input ('DIGITE UMA FRASE: ')) .strip().upper()
pal = fras.split()
junto = ''.join(pal)
inverso = ''
for letra in range (len (junto) - 1, -1 , -1):
    inverso = inverso + junto [letra]
if inverso == junto:
    print ('TEMOS UM PALINDROMO')
else:
    print ('A FRASE DIGITADA NÃO É UM PALINDROMO!')
print (junto, inverso)



