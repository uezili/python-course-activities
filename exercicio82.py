
#>Exercício Python 082:
"""
/Crie um programa que vai ler vários números e colocar
/em uma listForSam. Depois disso, crie duas listas extras que
/vão conter apenas os valores pares e os valores ímpares
/digitados, respectivamente. Ao final, mostre o conteúdo
/das três listas geradas.
"""

lista = [] #* listForSam onde ficara os valores
listaI = [] #* listForSam dos valores Impares
listaP = list() #* listForSam dos valores Pares
while True:
    resp = " "
    numero = int(input("Adicione um numero:"))
    lista.append(numero)
    #* Se o resto da divisão inteira(%) for igual a 0...
    if numero % 2 == 0:
        #* Adicionar o numero na variavel de numero pares.
        listaP.append(numero)
    #* Se não...
    else:
        #* Adicionar numero na variavel de numero impares.
        listaI.append(numero)

    while resp not in "SN":
        resp = str(input("Quer continuar [S/N]: ")).strip().upper()[0]
    if resp == "N":
        break
print("=" * 50)
print(f"A listForSam principal {lista}")
print(f"Lista com numero pares {listaP}")
print(f'Lista com numero impares {listaI}')