n = int(input("Figite um numero para saber sua tabuada: "))

while True:
    print("-=" * 10)
    for i in range(1,11):
        reslt = n * i
        print(f"{n} x {i} = {reslt}")
    print("-=" * 10)
    n = int(input("digite novamente ou coloque um numero netivo para parar: "))
    if n < 0:
        break
print("Ate mais!")