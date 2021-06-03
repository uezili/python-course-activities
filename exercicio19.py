from random import choice

a1 = input('nome do primeiro aluno: ')
a2 = input('Nme do segundo aluno: ')
a3 = input('nome do terceiro aluno: ')
a4 = input('nome do quarto aluno: ')

# Usamos lists que não foi ensinado na aula de modolo 
#Sacanagem isso!

lista = [a1,a2,a3,a4]
print('O aluno sorteado foi {}'.format(choice(lista)))