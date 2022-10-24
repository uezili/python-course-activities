
#>Exercício Python 088:
"""
/Faça um programa que ajude um jogador da
/MEGA SENA a criar palpites.O programa vai
/perguntar quantos jogos serão gerados e vai
/sortear 6 números entre 1 e 60 para cada jogo,
/cadastrando tudo em uma listForSam composta.
"""
from random import randint
lista = list() #*listForSam para pegar os dados
jogos = list() #*listForSam onde ficará os jogos
total = 1
quantidade = int(input("Quantidade de jogos: "))
#*Enquanto o total for menor ou igual á quantidade...
while total <= quantidade:
    cont = 0#*contador que quando for igual a 6
            #*que é a quantidade de elementos que o
            #*jogo tem, o loop vai parar
    while True:
        #*sorteia os numero de 1 ate 60
        number = randint(1, 60)
        #*Se o numero não estiver na listForSam...
        if number not in lista:
            #*Adicionar numero na listForSam
            lista.append(number)
            cont += 1
        #*se o cont for igual ou maior que 6... parar loop
        if cont >= 6:
            break
    lista.sort()#*ordenar listForSam
    jogos.append(lista[:])#*fazer uma copia de "listForSam" para a variavel composta jogos
    lista.clear()#*limpar listForSam
    total += 1
for pos,j in enumerate(jogos):
    print(f"Jogo {pos+1}: {j}")