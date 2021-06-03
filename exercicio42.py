a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

if a + b > c and b + c > a and a + c > b:
    print("Pode ser formado um triangolo com esse segmento!!")
    if a == b == c:
        print("O triangulo é EQUILATERO.")
    elif a == b or a == c or b == c:
        print("O triangulo é ISOSCELES.")
    elif a != b and a != c and b != c:
        print("O triangulo é ESCALENO.")
else:
    print("Não é um triangulo.")