
# >Exercício Python 099:
'''
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer
qual deles é o maior.
'''

def maior(* num):
    maiorValor= cont = 0

    for i in num:
        print(i, end=" ")
        if cont == 0:
            maiorValor = i
        else:
            if i > maiorValor:
                maiorValor = i
        cont += 1
    print(f"Foram analizados {len(num)} numeros, e o maior deles é {maiorValor}")
    if num == 0:
        print("Não á nenhum valor para ser analizado")

maior(3, 4, 9, 10, 4, 6)
maior()