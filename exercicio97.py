
# >Exercício Python 097:
'''
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.
'''
def escreva(m):

    print(len(m)* '-')
    print(f"{m}".capitalize())
    print(len(m)* '-')

mensagem = str(input("Escreva algo: "))

escreva(mensagem)