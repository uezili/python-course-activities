from time import sleep

print("*-=" * 12)
print("Vamos brincar com alguns numeros:")
num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))
opç = 0

while opç != 5:
    print("=-" * 12)
    print('''
[1] Somar;
[2] Multiplicar;
[3] Maior;
[4] Digitar novos numeros;
[5] Sair''')
    print("=-" * 12)

    opç = int(input('-->'))

    if opç == 1:
        print("Um momento...")
        sleep(2)
        print("=" * 12)
        print("A soma de {} + {} é {}.".format(num1, num2, num1 + num2))
        print("=" * 12)

    elif opç == 2:
        print("Um momento...")
        sleep(2)
        print("=" * 12)
        print("A multiplicação de {} x {} é {}.".format(num1, num2, num1 * num2))
        print("=" * 12)

    elif opç == 3:
        maior = num1
        print("Um momento...")
        sleep(2)
        if num2 < num1:
            print("=" * 12)
            print("O maior é {}.".format(num1))
            print("=" * 12)
        else:
            print("=" * 12)
            print("O maior é {}.".format(num2))
            print("=" * 12)

    elif opç == 4:
        num1 = int(input("Primeiro valor: "))
        num2 = int(input("Segundo valor: "))

    elif opç == 5:
        print("Ate mais ^^")

    else:
        print("Escolha uma opção valida.")
    sleep(1)
