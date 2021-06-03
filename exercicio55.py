maior = 0
menor = 0

for pess in range(1,6):
    peso = float(input("Pesso da {}º pessoa : ".format(pess)))

    if pess == 1:
        maior = peso
        menor = peso 
    else: 
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O menor peso é {}kg e o maior é {}kg.".format(menor, maior))