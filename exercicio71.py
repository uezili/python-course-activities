'''Exercício Python 071: Crie um programa que simule o
funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa
vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

dinheiro = int(input("Quanto de dinheiro quer sacar: "))
total = dinheiro
ced = 100
totalCed = 0
while True:
    if total >= ced:
        total -= ced
        totalCed += 1
    else:
        if totalCed > 0:
            print(f"Você receberá {totalCed} de R$ {ced}")

        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totalCed = 0
        if total == 0:
            break
print("Ate mais!")