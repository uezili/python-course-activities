from datetime import date

atual = date.today().year #pegar data atual que estamos

ano = int(input("Em que ano você nasceu: "))

ct = atual - ano #calculo da idade

if ct < 4:
    print("Desculpe, mas não temos categoria para ele.")
elif ct <= 9:
    print("A sua categoria é mirim que vai de 4 á 9 anos.")
elif ct <= 14:
    print("A sua categria é infatil que vai de 10 á 14 anos.")
elif ct <= 19:
    print("A sua categoria é junior que vai de 15 á 19 anos.")
elif ct <= 25:
    print("A sua categoria é senior que vai de  20 á 25 anos.")
else:
    print("A sua categoria é master que vai de 25 anos a cima")