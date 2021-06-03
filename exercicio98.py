
# >Exercício Python 098:
'''
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo. Seu programa
tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
from time import sleep

def contador(i, f, p):
    # *se o numero de passos p for menor que 0...
    if p < 0:
        p *= 1
    # *se o numero de passos p for igual á 0...
    if p == 0:
        p = 1
    # *se o numero de inicio i for maior que o numero final f...
    if i < f:
        cont = i
        # *enquanto o contador cont menor ou igual ao numero final f...
        while cont <= f:
            print(f'{cont}', end=" ", flush=True)
            sleep(0.5)
            cont += p
        print()
    # *se não...
    else:
        cont = i
        # *enquanto o contador cont for maior ou igual á f...
        while cont >= f:
            print(f'{cont}', end=" ", flush=True)
            sleep(0.5)
            cont -= p
        print()


contador(1, 10, 1)
contador(0, 10, 2)
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)