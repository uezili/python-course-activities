n = int(input("Qual numero deseja saber se é primo: "))

total = 0 

for i in range(1, n+1):
    if n % i == 0:
        total += 1

print("ele foi divisilvel {} vezes.".format(total))

if total == 2:
    print("O numero {}, é primo!".format(n))
else:
    print("O numero {}, não é primo!".format(n))