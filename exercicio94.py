
#>Exercício Python 094:
"""
Crie um programa que leia nome, Sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma listForSam. No final, mostre:
A) Quantas pessoas foram cadastradas;
B) A média de idade
C) Uma listForSam com as mulheres
D) Uma listForSam de pessoas com idade acima da média
"""

dados = dict() #* informações de entrada do usuário
galera = list() #* onde serão guardadas
totSoma = 0

while True:
    resp = " "
    dados['Nome'] = str(input("Nome: ")).capitalize()
    dados['Idade'] = int(input("Idade: "))
    while True:
        dados['Sexo'] = str(input("Sexo[F/M]: ")).strip().capitalize()[0]
        if dados['Sexo'] in 'FM':
            break
        print("Você cometeu um erro, so aceitamos F ou M.")
    galera.append(dados.copy())
    totSoma += dados['Idade']

    while True:
        resp = str(input("Quer continuar[S/N]: ")).capitalize().strip()[0]
        if resp in 'SN':
            break
        print("Por favor, digite só S ou N.")
    if resp == 'N':
        break

mediaIdade = totSoma / len(galera)
print()
print(f"Total de pessoas cadastradas: {len(galera)}")
print(f"A média de idade do grupo é: {mediaIdade:.2f}")
print(f"As mulheres cadastradas foram: ", end=" ")
for p in galera:
    if p['Sexo'] in 'Ff':
        print(p['Nome'], end="...")
print()
print("As pessoa com idade acima da médida são: ", end=" ")

#* Para toda pessoa(p) em galera...
for p in galera:
    #* Se a idade da pessoa for maior ou igual a media de idade...
    if p['Idade'] >= mediaIdade:
        print(p['Nome'], end="...")
print()