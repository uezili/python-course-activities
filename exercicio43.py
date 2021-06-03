peso = float(input("Qual seu peso??"))
altu = float(input("e sua altura??"))

imc = peso / altu**2

if imc < 18.5:
    print("Seu imc é {:.2f}, você está ABAIXO DO PESO.".format(imc))
elif imc <= 25 and imc > 18.5:
    print("Seu imc é {:.2f}, você está no PESO IDEAL.".format(imc))
elif imc <= 30 and imc > 25:
    print("Seu imc é {:.2f}, você está com SOBREPESO.".format(imc)) 
elif imc <= 40 and imc > 30:
    print("Seu imc é {:.2f}, você está com OBESIDADE.".format(imc))
else:
    print("Seu imc é {:.2f}, você está com OBESIDADE MORBIDA.".format(imc))