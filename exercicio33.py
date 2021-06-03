#preencher as 3 variaveis
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))

#comparar cada uma e ver qual é a de menor valor
menor = x
if y < x and y < z:
    menor = y
if z < x and z < y:
    menor = z
#maior valor
maior = x
if y > x and y > z:
    maior = y
if z > x and z > y:
    maior = z

#mostrar resultado
print("O menor valor é {}".format(menor))
print("O maior valor é {}".format(maior))