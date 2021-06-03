from random import randint
c = 0

while True:
    joga = int(input("Escolha um numero: "))
    pc = randint(1,10)
    total = pc + joga
    tipo = " "
    while tipo not in 'PI':
        tipo = str(input("Impar ou Par[I/P]: ")).strip().upper()[0]
    print(f"Você jogou {joga} e o PC {pc}, o total é {total}.",end="")
    if total % 2 == 0 :
        print(" DEU PAR!")
    else:
        print(" DEU IMPAR!")
    if tipo == "P":
        if total % 2 == 0:
            print("Parabéns você ganhou!")
            c += 1
        else:
            print("Você perdeu!")
            break
    elif tipo == "i":
        if total % 2 != 0:
            print("Você venceu!")
            c += 1
        else:
            print("Você perdeu!")
            break
print(f"Você venceu {c} vezes. Ate a proxima!")
