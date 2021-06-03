soma = 0
cont = 0
for i in range(1,7):
    num = int(input("Digite {}º numero: ".format(i)))

    if num % 2 == 0:
        soma += num
        cont += 1
print("A quantidade de numero pares é {}, soma de todos os numeros pares é {}.".format(cont,soma))