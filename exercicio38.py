n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))

if n1 > n2:
    print("O maior é o {}.".format(n1))
elif n2 > n1:
    print("O maior é o {}.".format(n2))
else:
    print("Os dois são iguais.")