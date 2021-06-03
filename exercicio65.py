n = 0
soma = 0
i = 0
maior = 0
menor = 0
opç = ""

while opç != "N":
    i += 1
    n = int(input("Digite um numero: "))
    soma += n
    menor = maior
    if maior < n:
        maior = n
    if menor > n:
        menor = n
    opç = str(input('Quer continuar [S/N]: ').upper())
media  = soma / i

print("A media dos numero são {}, o maior é {} e o menor {}.".format(media,maior,menor))