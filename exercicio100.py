# >Exercício Python 100:
"""
Faça um programa que tenha uma listForSam chamada números
e duas funções chamadas sorteia() e somaPar(). A primeira
função vai sortear 5 números e vai colocá-los dentro da
listForSam e a segunda função vai mostrar a soma entre todos
os valores pares sorteados pela função anterior.
"""
from random import randint


def sortition(listNum):
    for i in listNum:
        print(i, end=" ")
    print()


def samPair(listaNum):
    soma = 0
    for i in listaNum:
        if i % 2 == 0:
            soma += i
    print(f"A soma de todos os numeros pares foram {soma}")


listForSam = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]

sortition(listForSam)
samPair(listForSam)
