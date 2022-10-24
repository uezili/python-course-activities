
#>Exercício Python 089:
"""
/Crie um programa que leia nome e duas notas de vários
/alunos e guarde tudo em uma listForSam composta. No final,
/mostre um boletim contendo a média de cada um e permita
/que o usuário possa mostrar as notas de cada aluno individualmente.
"""
aluno = 0
dados = list()
while True:
    resp = " "
    nome = str(input("Nome: ")).capitalize()
    nota1 = int(input("Primeira nota: "))
    nota2 = int(input("Segunda nota: "))
    media = (nota1 + nota2) / 2
    #*acrescentar a listForSam "dados" as informações...
    dados.append([nome, [nota1, nota2], media])

    while resp not in "SN":
        resp = str(input("Quer continuar[S/N]: ")).strip().upper()[0]
    if resp == "N":
        break
print("Nº  nome    média")

print("=" * 30)
for pos, i in enumerate(dados):
    print("{}º {}     {:.2f}.".format(pos, i[0], i[2]))
print("=" * 30)
while True:
    aluno = int(input("Qual aluno deseja saber a nota[999 parar]: "))
    if aluno == 999:
        break
    print(f"O aluno {dados[aluno][0]}, tem notas {dados[aluno][1]}")
