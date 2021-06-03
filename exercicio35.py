#pegar medidas 

a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

#fazer calculo para ver qual é os menores e somalos

if a + b > c and b + c > a and a + c > b:
    print("Pode ser formado um triangolo com esse segmento!!")
else: 
    print("Não pode ser formado um triangulo com esses segmentos!!")