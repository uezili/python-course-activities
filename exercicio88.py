
#>Exercício Python 088:
"""
/Faça um programa que ajude um jogador da
/MEGA SENA a criar palpites.O programa vai
/perguntar quantos jogos serão gerados e vai
/sortear 6 números entre 1 e 60 para cada jogo,
/cadastrando tudo em uma lista composta.
"""
from random import randint
lista = list() #*lista para pegar os dados
jogos = list() #*lista onde ficará os jogos
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
        #*Se o numero não estiver na lista...
        if number not in lista:
            #*Adicionar numero na lista
            lista.append(number)
            cont += 1
        #*se o cont for igual ou maior que 6... parar loop
        if cont >= 6:
            break
    lista.sort()#*ordenar lista
    jogos.append(lista[:])#*fazer uma copia de "lista" para a variavel composta jogos
    lista.clear()#*limpar lista
    total += 1
for pos,j in enumerate(jogos):
    print(f"Jogo {pos+1}: {j}")