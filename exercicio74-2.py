from random import randint

numerosAle = (randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10))

print(f'Os numeros que foram sorteados foi: ', end=' ')
for i in numerosAle:
    print(i, end=" ")
print(f'\nO maior numero da lista é {max(numerosAle)}')
print(f'O menor numero da lista é {min(numerosAle)}')