
# >Exercício Python 092:
"""
/Crie um programa que leia nome, ano de nascimento
/e carteira de trabalho e cadastre-o (com idade) em
/um dicionário. Se por acaso a CTPS for diferente de
/ZERO, o dicionário receberá também o ano de contratação
/e o salário. Calcule e acrescente, além da idade, com
/quantos anos a pessoa vai se aposentar.
"""
from datetime import datetime #* Lib respoonsavel por pegar o ano atual.

anoAtual = datetime.now().year #* Ano atual
dados = dict()
dados['Nome'] = str(input("Nome: ")).capitalize()
idade = int(input("Ano de Nascimento: "))
dados['idade'] = anoAtual - idade
dados['Carteira de trabalho'] = int(input("Carteira de trabalho(0 se não tiver): "))
#* Se a Carteira de trabalho for diferente de 0...
if dados['Carteira de trabalho'] != 0:
    dados['Ano de contratação'] = int(input("Ano de contratação: "))
    dados['Aposentadoria'] = dados['idade'] + (35 + dados['Ano de contratação']) - anoAtual
    dados['Salario'] = int(input("Salario: "))

#* Para toda key(chave) e valor em dados...
for k,v in dados.items():
    print(f"-{k} tem valor {v}.")
