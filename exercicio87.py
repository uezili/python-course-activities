
#>Exercício Python 087:
"""
/Aprimore o desafio anterior, mostrando no final:
/A) A soma de todos os valores pares digitados.
/B) A soma dos valores da terceira coluna.
/C) O maior valor da segunda linha
"""
matriz = [[], [], []]
somaPares = 0
somaTerceira = 0
for l in range(0,3):
    for c in range(0,3):
        number = int(input(f"Digite um valor para {[l], [c]}: "))
        matriz[l].append(number)
        if number % 2 == 0:
            somaPares += number
        if c == 2:
            somaTerceira += number
print("=-" * 40)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print()
print(f'A soma de todos os numero pares é {somaPares}')
print(f"A soma de toda a teceira coluna é {somaTerceira}")
print(f"O maior valor da segunda linha é {max(matriz[1])}")