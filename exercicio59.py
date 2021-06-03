opç = 0
print(" ")
print("*=-" * 15 + '*')
print('Vamos brincar com numeros,escolha dois numero:')
print("*=-" * 15 + '*')
n1 = int(input("Primeiro numero: "))
n2 = int(input("Segundo numero: "))

while opç != 5:
    print('''
[1] Somar;
[2] Multiplicar;
[3] Maior;
[4] Digitar outros numeros;
[5] Sair.''')
    opç = int(input("--> "))
    if opç == 1:
        print("A soma de {} + {} é {}.".format(n1,n2,n1+n2))

    elif opç == 2:
        print("A multiplicação de  {} x {} é {}.".format(n1,n2,n1*n2))

    elif opç == 3:
        if n1 > n2:
            print("O maior é {}.".format(n1))
        if n1 < n2:
            print("O maior é {}.".format(n2))

    elif opç == 4:
        print("Difite os numeros novamente: ")
        n1 = int(input("Primeiro numero: "))
        n2 = int(input('Segundo numero: '))

    else:
        print("Opção invalida,tente novamente!")