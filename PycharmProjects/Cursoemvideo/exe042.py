print ('-=-'*20)
print ('ANALISADOR DE TRIANGULO')
print ('-=-'*20)
priseg = float (input ('DIGITE O PRIMEIRO SEGMENTO DE RETA: '))
segseg = float (input ('DIGITE O SEGUNDO SEGMENTO DE RETA: '))
terseg = float (input ('DIGITE O TERCEIRO SEGMENTO DE RETA: '))
if ( priseg + segseg ) > terseg and (priseg + terseg) > segseg and (segseg + terseg) > priseg:
    print ('OS SEGMENTOS PODEM FORMAR UM TRIANGULO')
    if priseg == segseg == terseg:
        print ('OS SEGMENTOS FORMAM UM TRIANGULO EQUILATERO')
    elif priseg == segseg or priseg == terseg or segseg == terseg:
        print ('OS SEGMENTOS FORMAM UM TRIANGULO ISOSCELES')
    elif priseg != segseg != terseg != priseg:
        print ('OS SEGMENTOS FORMAM UM TRIANGULO ESCALENO')
else:
    print('OS SEGMENTOS NÃO PODEM FORMAR UM TRIANGULO')
