
#>Exercício Python 074:
"""
/Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
/Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
/valor que estão na tupla.
"""
from random import randint

numerosAle = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
tupleMaiorMenor = sorted(numerosAle)
print(f'Nossa listagem de numeros é {(numerosAle)}')
print(f'O maior numero é {tupleMaiorMenor[4]}')
print(f'O menor Numero é {tupleMaiorMenor[0]}')

