nome = str (input ('QUAL O SEU NOME: '))
alt = float (input ('QUAL A SUA ALTURA: '))
pes = float (input ('QUAL O SEU PESO: '))
imc = pes / (alt**2)
if imc < 18.5:
    print ('SEU IMC É DE {:.2f} E VOCÊ ESTÁ ABAIXO DO PESO.'.format (imc))
elif imc >= 18.5 and imc < 25:
    print ('O SEU IMC É DE {:.2f} E VOCÊ ESTÁ COM PESO IDEAL.'.format (imc))
elif imc >= 25 and imc < 30:
    print ('O SEU IMC É DE {:.2f} E VOCÊ ESTÁ COM SOBREPESO.'.format (imc))
elif imc >= 30 and imc <= 40:
    print ('O SEU IMC É DE {:.2f} E VOCÊ ESTÁ COM OBESIDADE.'.format (imc))
elif imc > 40:
    print ('O SEU IMC É DE {:.2f} E VOCÊ ESTÁ COM OBESIDADE MÓRBIDA.'.format (imc))
