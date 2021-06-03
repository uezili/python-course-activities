from random import randint
from time import sleep

print('Irei pensar em um número.Tente advinhar...')
x = randint(1,5) #Aqui é gerado o número aleatorio...
number = int(input("Qual numero eu penei?" ))
sleep(2)
if number == x:
    print("Parabens você acerto!!! Eu pensei no número {}".format(x))
else:
    print("Que peninha,mas vc perdeu!")
    
