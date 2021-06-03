from datetime import date

atual = date.today().year
ano = int(input("Qual ano você nasceu? "))
idade = atual - ano 

print("Você tem ou vai fazer {} anos".format(idade))

if idade < 18:
    print("Você devera se alistar aqui á {} anos.".format(18 - idade))

elif idade > 18:
    print("Você ja deveria ter se alistado")

else:
    print("Você precisa ir IMEDIATAMENTE se alisar")