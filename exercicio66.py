n = c = s = 0

while True:

    n = int(input("Digite um numero:[999 para parar] "))
    if n == 999:
        break
    c +=1
    s += n
print(f"A quantidade de numero digitados foi {c} e a soma deles foi {s}")