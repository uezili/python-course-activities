
# >Exercício Python 096:
'''
Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno
'''
def area(a, b):
    s = a * b
    print(f"A área de um terreno de {a}x{b} é {s}")


largura = float(input("Largura(m): "))
comprimento = float(input("Comprimento(m): "))

area(comprimento, largura)