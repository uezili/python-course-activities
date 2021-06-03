num = int(input("Digirte o numero que querira saber a taboada: "))

for i in range(1,11):
    total = num * i
    print("{:2} x {:2} = {}".format(num,i,total, end=" "))