number = int(input("Qual valor quer converter? "))
print('''Qual base:
1.Binario
2.octal
3.hexadecimal''')
opc = int(input("Qual sua opção? "))
if opc == 1:
    print("O numero {} em binario é {}.".format(number, bin(number)[2:]))
elif opc == 2:
    print("O mumero {} em octal é {}.".format(number,oct(number)[2:]))
elif opc == 3:
    print("O numero {} em hexadecimal é {}.".format(number,hex(number)[2:]))
else:
    print("Tente novamente.")