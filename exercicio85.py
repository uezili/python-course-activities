
#>Exercício Python 085:
"""
/Crie um programa onde o usuário possa digitar sete
/valores numéricos e cadastre-os em uma lista única
/que mantenha separados os valores pares e ímpares.
/No final, mostre os valores pares e ímpares em ordem
/crescente.
"""
listas = [[], []]

for i in range(1, 8):
    number = int(input(f"Numero {i}º: "))
    #*Se o resto da divisão inteira do numero divido por 2 for igual a zero... fazer isso...
    if number % 2 == 0:
        listas[0].append(number)
    #*Se o resto da divisão inteira do numero divido por 2 for diferente de zero... fazer isso...
    elif number % 2 != 0:
        listas[1].append(number)

print(f"Lista de numeros pares digitados: {sorted(listas[0])}")
print(f"Lista de numeros impares digitados: {sorted(listas[1])}")