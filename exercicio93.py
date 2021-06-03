

#>Exercício Python 093:
"""
/Crie um programa que gerencie o aproveitamento de um jogador
/de futebol. O programa vai ler o nome do jogador e quantas
/partidas ele jogou. Depois vai ler a quantidade de gols feitos
/em cada partida. No final, tudo isso será guardado em um
/dicionário, incluindo o total de gols feitos durante o campeonato.
"""
total = 0
dadosJogador = dict()
golsPartidas = list()
dadosJogador['Nome'] = str(input("Nome do jogador:")).capitalize()
partidas = int(input(f"Quantas partidas o {dadosJogador['Nome']} jogou: "))

for i in range(0, partidas):
    golsPartidas.append(int(input(f"Gols partida {i}: ")))

# *Para todo gol(s) em golsPartidas...
for s in golsPartidas:
    total += s

dadosJogador['total'] = total
dadosJogador['Gols'] = golsPartidas.copy()

for k,v in dadosJogador.items():
    print(f"- O {k} tem valor {v}.")

