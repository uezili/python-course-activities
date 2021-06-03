#Receber informação do usuario 
print("Qual numero deseja analizar?")
number = int(input())
#calculo do número
x = number % 2
#Fazer comparação do numero...
if x == 0:
    print("Ele é par!")
else:
   print('não é par!')
