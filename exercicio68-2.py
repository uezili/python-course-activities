import random
c = 0

jogador = str(input("Escolha IMPA ou PAR [I/P]: ").upper().strip())
n = int(input("Escolha um numero: "))

while True:
    pc = random.randint(0, 10)
    resultado = pc + n
    if resultado % 2 == 0:
        resultado = "Par"
    else:
        resultado = "impar"

    if jogador == "I":
        if resultado == "impar":
            c = c + 1
            print(f"Você escolheu {n} e eu {pc}.{resultado}, Você ganhou!")
            jogador = str(input("Mais uma vez [I/P]: ").upper().strip())
            n = int(input("Escolha um numero: "))
        else:
            print(f"Você esoclheu {n} e eu {pc}.{resultado}, você perdeu!")
            break

    elif jogador == "P":
        if resultado == "Par":
            c = c + 1
            print(f"Você escolheu {n} e eu {pc}.{resultado}, Você ganhou!")
            jogador = str(input("Mais uma vez [I/P]: ").upper().strip())
            n = int(input("Escolha um numero: "))
        else:
            print(f"Você esoclheu {n} e eu {pc}.Impar, você perdeu!")
            break

    else:
        jogador = str(input("Escolha uma opçao valida[I/P]:").upper().strip())
        n = int(input("Escolha um numero: "))
print(f'Você ganhou {c} vezes.')