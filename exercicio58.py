from random import randint
from time import sleep

tentativas = 1
x = randint(0,10)
print(" " * 10)
print("-=-*" * 12)
print("Irei pensar em um numero de 0 a 10,tente adivinhar")
print("-=-*" * 12,"\n")
number = int(input("Qual numero estou pensando: "))

espaço = " "
while number != x:

    if number < x:
        print("Ta quente!")
    else:
        print("Ta frio")
    if number == espaço:
        print("Digite apenas numeros.")

    number = int(input("Voçê errou! tente novamente: "))

    tentativas += 1

if tentativas <= 5:
    sleep(2)
    print("=" * 40)
    print("Você acertou com {} tentativas. Parabéns!!".format(tentativas))
    print("=" * 40)
else:
    sleep(2)
    print("=" * 60)
    print("Você acertou, mas com {} tentativas. Tente conseguir menos.".format(tentativas))
    print("=" * 60)
