opç = ''
numEstenço = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
    'Sete','Oito', 'Nove','Dez', 'Onze', 'Doze', ' Tresse', 'Catorze',
    'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    numero = int(input("Digite um numero(0 a 20): "))
    if numero >= 0 and numero <= 20:
        break
    print(f"Você digitou {numEstenço[numero]}")

    while opç not in "SN":
        opç = str(input("Quer continuar[S/N]: ")).split().upper()[0]
    if opç == "N":
        break