i = 0
cont = 0
soma = 0
num = 0

while num != 999:
    num = int(input("Digite um numero: "))
    soma += num
    cont += 1
    if num == 999:
        cont -= 1
        soma -= 999
print("A quantidade de numero digitados foi {} e sua soma foi {}.".format(cont, soma))