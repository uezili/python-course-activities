from random import choice
from time import sleep

print("-=-" * 11,"JOGAR JOGAR","-=-" * 11)
print("""Escola faça sua escolas e vamos ver se ganha de mim:
.Pedra
.Papel
.Tesoura""")

esc = str(input("--> ").capitalize())
lista = ["Pedra","Papel","Tesoura"]
pc = choice(lista)

sleep(1)
print("JO")
sleep(1)
print("GEM")
sleep(1)
print("POH")

print("-=-" * 11 )
print("VOCE ESCOLHEU {} E O PC {}.".format(esc,pc))
if esc == lista [0]:
    if pc == "Pedra":
        print("IMPATE!!!") 
    elif pc != "Tesoura":
        print("EU GANHEI!!!")
    elif pc != "Papel":
        print("PARABENS,VOCÊ GANHOU!!!")
if esc == lista [1]:
    if pc == "Papel":
        print("IMPATE")
    elif pc != "Tesoura":
        print("EU GANHEI!!!")
    elif pc != "Papel":
        print("PARABESN,VOCÊ GANHOU")
if esc == lista [2]:
    if pc == "Tesoura":
        print("IMPATE!!!")
    elif pc != "Papel":
        print("EU GANHEI!!!")
    elif pc != "Pedra":
        print("PARABENS, VOCÊ GANHOU!!!")
if esc != "Pedra" and esc != "Tesoura" and esc != "Papel":
    print("OPÇÃO INVALIDA. TENTE NOVAMENTE!")

print("-=-" * 11 )