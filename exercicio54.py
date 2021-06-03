import datetime

menor = 0
atual = datetime.date.today().year
maior = 0

for i in range(1,8):
    ano = int(input("Qual o ano de nacimento das 7 pessoas? "))
    idade = atual - ano
    if idade > 18:
       maior += 1
    else:
        menor += 1


print("Nesse grupo só temos {} maior de idade e menore temos {} !".format(maior,menor))