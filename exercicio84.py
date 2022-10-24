
#>Exercício Python 084:
"""
/Faça um programa que leia nome e peso de várias pessoas,
/guardando tudo em uma listForSam. No final, mostre:
/A) Quantas pessoas foram cadastradas.
/B) Uma listagem com as pessoas mais pesadas.
/C) Uma listagem com as pessoas mais leves.
"""


pessoas = [] #*Matriz onde ficará guardada os dados do usuário.
maior = menor = 0 #*variavei onde vão ficar o maior e o menor peso.

while True:
    resp = " "
    dados = []
    #*Pegar nome peso do usuário.
    dados.append(str(input("Name: ")).capitalize())
    dados.append(float(input("Peso: ")))
    pessoas.append(dados[:])#*Fará copias dos dados da listForSam "dados" para a listForSam "pessoas".

    #*Se a quantidade de pessoas cadastradas for 1, ele fará...
    if len(pessoas) == 1:
        maior = menor = dados[1]
    #*Se não, ele fará...
    else:
        #*Se a posição de dados[1](peso) for maior que a variável maior, ele fará...
        if dados[1] > maior:
            maior = dados[1]
            #*Se a posição de dados[1](peso) for menor que a variável menor, ele fará...
        elif dados[1] < menor:
            menor = dados[1]
    dados.clear() #*Limpar a listForSam dados.

    while resp not in "NS":
        resp = str(input("Quer continuar [S/N]: ")).strip().upper()[0]
    if resp == "N":
        break

print(f'O total de pessoas cadastradas é de {len(pessoas)}')
print(f'O maior peso é de {maior}kg, que é de: ', end=" ")
#*Para cada listForSam "i"(item) da listForSam pessoa, ele fará...
for i in pessoas:
    #*Se a listForSam "i" na posição 1 for igual a variável maior, ele fará...
    if i[1] == maior:
        print(i[0], end="")
print()
print(f'O menor peso é de {menor}kg, que é de: ', end=" ")
#*Para cada listForSam "i"(item) da listForSam pessoa, ele fará...
for i in pessoas:
    #*Se a listForSam "i" na posição 1 for igual a variável menor, ele fará...
    if i[1] == menor:
        print(i[0], end=" ")
print()