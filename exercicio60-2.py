from math import factorial

n = int(input("Digite o numero a ser fatorado: "))

print("{}! = ".format(n),end="")

for i in range(n,0,-1):
    print("{}".format(i),end=" -> ")

print(factorial(n))