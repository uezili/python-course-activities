
#>Exercício Python 091:
"""
/Crie um programa onde 4 jogadores joguem um dado e tenham
/resultados aleatórios. Guarde esses resultados em um dicionário
/em Python. No final, coloque esse dicionário em ordem, sabendo
/que o vencedor tirou o maior número no dado.
"""
from random import randint #*Numeros aleatorios
from time import sleep #*Atrasos de tempo do programa
from operator import itemgetter

ordemVencedores = list()
# *Dicionario onde vai ser sortiados os numero para cada jogador
jogadores = {
    'jogador1':randint(1, 6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1, 6)
    }
# *Para cada chave(k) e valor(v) em jogadores...
for k, v in jogadores.items():
    print(f"{k} tirou {v}.")
    sleep(1)
# *Aqui iremos usar o sorted parar organizar os vencedores na ordem
# *Colocando em uma lista... temos uma função itemgetter que vai verificar
# *Conteudo da chave e organizar em ordem crescente. O "reverse=True" servirá
# *Para mudar a ordem para descrente.
ordemVencedores = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print("A ordem de vencedores é:")
for i, v in enumerate(ordemVencedores):
    print(f"{i+1}º luga: {v[0]}, com {v[1]}.")
    sleep(1)