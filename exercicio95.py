
#> Exercício Python 095:
"""
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento
de cada jogador.
"""
listJodores = list() #* Lista onde ficará os dados completos dos jogadores

while True:
    total = 0 #* Total de gols
    golsPartidas = list() #* Lista de gols em partida
    dadosJogador = dict()
    resp = " "
    dadosJogador['Nome'] = str(input("Nome do jogador:")).capitalize()
    partidas = int(input(f"Quantas partidas o {dadosJogador['Nome']} jogou: "))

    #* Para toda partida(i) em um range de 0 ao numero de partidas...
    for i in range(0, partidas):
        golsPartidas.append(int(input(f"Gols partida {i+1}: ")))

    #* Para todo numero de gols(s)...
    for s in golsPartidas:
        total += s

    dadosJogador['Total'] = total
    dadosJogador['Gols'] = golsPartidas.copy()
    listJodores.append(dadosJogador.copy())
    dadosJogador.clear()

    #* Enquanto a resp não for em S ou n...
    while resp not in 'SN':
        resp = str(input("Quer continuar[S/N]: ")).strip().capitalize()[0]
    if resp == 'N':
        break


print('-' * 50)
print('Cod ', end='')
#* Para toda chave(i) em dadosJogador...
for i in dadosJogador.keys():
    print(f'{i:>15}', end='')
print()
print('-' * 50)

#* Para toda chave(k) com valor(v)...
for k, v in enumerate(listJodores):
    print(f"{k+1:>4}" , end='')
    #* Para todo valor(d) em v(jogadores)
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print('-' * 50)


while True:
    jogador = 0
    print("Dados de partidas")
    print("=" * 50)
    jogador = int(input("Qual jogador quer quer ver(999 para): "))

    print()
    #* Para todo indice(i) com o valor (v)...
    for i, v in enumerate(listJodores[jogador]['Gols']):
        print(f"Partida {i+1}, gols: {v}.")

    if jogador == 999:
        break
