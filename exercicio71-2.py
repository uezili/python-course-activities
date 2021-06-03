"""
/Exercício Python 071: Crie um programa que simule o
/funcionamento de um caixa eletrônico. No início, pergunte ao
/usuário qual será o valor a ser sacado (número inteiro) e o programa
/vai informar quantas cédulas de cada valor serão entregues. OBS:
/considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

valor = int(input("Quanto deseja tirar: R$ ")) #>Valor a ser pego do sagui
total = valor #>devemos transformar esse valor em um total
ceds = 50 #>Aqui é a variavel que ira receber as celulas
totCeds = 0 #>Aqui temos um contador de cédulas a serem tiradas de cada tipo
while True: #>loop infinito
    if total >= ceds: #>se o total for maior ou igual a cédulas
        total -= ceds #>Ele ira tirar do total o valor que aquela cédula tem
        totCeds += 1 #>Aqui ele ira pegar a quantidade que cada cédula vai ser necessário
    else:
        if totCeds > 0: #>para toda vez que mudar o valor da cédula ele vai imprimir a quantidade e qual valor da quela cédula
            print(f"Você receberá {totCeds} de R$ {ceds}")

        """
        *nesse caso toda vez que não der mais pra tirar aquela
        *quantidade que a cédula possui ele ira atribuir outro valores
        *para elas ate o total virar nulo.
        """
        if ceds == 50:
            ceds = 20
        elif ceds == 20:
            ceds = 10
        elif ceds == 10:
            ceds = 1
        totCeds = 0
        if total == 0:
            break
print("Ate mais!")