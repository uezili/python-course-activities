
# >Exercício Python 100:
'''
Faça um programa que tenha uma lista chamada números
e duas funções chamadas sorteia() e somaPar(). A primeira
função vai sortear 5 números e vai colocá-los dentro da
lista e a segunda função vai mostrar a soma entre todos
os valores pares sorteados pela função anterior.
'''
from random import randint

def sorteio(listaNum):
    for i in listaNum:
        print(i, end=" ")
    print()
def somaPar(listaNum):
    soma = 0
    for i in listaNum:
        if i % 2 == 0:
            soma += i
    print(f"A soma de todos os numeros pares foram {soma}")

lista = [randint(1, 10), randint(1,10), randint(1, 10), randint(1, 10)]

sorteio(lista)
somaPar(lista)


