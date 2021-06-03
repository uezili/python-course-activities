
#>Exercício Python 075:
"""
/Desenvolva um programa que leia quatro valores pelo teclado e
/guarde-os em uma tupla. No final, mostre:
/A) Quantas vezes apareceu o valor 9.
/B) Em que posição foi digitado o primeiro valor 3.
/C) Quais foram os números pares.
"""

numeros = (int(input("Digite um numero ")),
    int(input("Digite mais um numero ")),
    int(input("Digite mais um numero ")),
    int(input("Digite so mais um numero ")))

print(f"Os numero digitados foram {numeros}.")
print(f'O numero 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O numero 3 apareceu na posição {numeros.index(3) + 1}.')
else:
    print("O numero 3 não foi encontrado")
print(f"Os numeros pares foram ",end=' ')
for i in numeros:
    if i % 2 == 0:
        print(i, end=" ")
print('\n')