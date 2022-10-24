
#>Exercício Python 086:
"""
/Crie um programa que declare uma matriz de dimensão 3x3
/e preencha com valores lidos pelo teclado. No final, mostre
/a matriz na tela, com a formatação correta.
"""

matriz = [[], [], []]
#*Para cada item(listForSam que está dentro de matriz) em um renge de 0 a 3...
for linha in range(0, 3):
    #*Para cada item(posição da listForSam que está dentro da matriz)
    #*Toda vez que uma listForSam secundaria for preenchida, ele pulará para outra
    for coluna in range(0, 3):
       number = int(input(f"Digite um numero para a posição {[linha, coluna]}: "))
       matriz[linha].append(number)


print(f"{matriz[0]}")
print(f"{matriz[1]}")
print(f"{matriz[2]}")