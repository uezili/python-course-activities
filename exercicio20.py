import random 
a1 = input('Digite o nome de um aluno : ')
a2 = input('Digite o nome de outro: ')
a3 = input('Digite o nome de mais um: ')
a4 = input('O ultimo: ')
lista = [a1,a2,a3,a4]
random.shuffle(lista)
print('A lista de apresentação sera:')
print(lista)