
#>Exercício Python 090:
"""
/Faça um programa que leia nome e média de um aluno,
/guardando também a situação em um dicionário. No final,
/mostre o conteúdo da estrutura na tela.
"""

aluno = dict()
aluno['nome'] = str(input("Nome de aluno: ")).capitalize()
aluno['media'] = float(input(f"Qual a media do {aluno['nome']}: "))

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado!'
else:
    aluno['situação'] = 'Recuperação!'
if aluno['media'] < 5:
    aluno['situação'] = 'Reprovado!'
print("=" * 30)
for k, v in aluno.items():
    print(f"-{k} é igual a {v}.")