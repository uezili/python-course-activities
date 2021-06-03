
# >Exercício Python 076:
"""
/Crie um programa que tenha uma tupla única com nomes
/de produtos e seus respectivos preços, na sequência.
/No final, mostre uma listagem de preços, organizando
/os dados em forma tabular.
"""

produtosPreços = ('Detergente', 2.00, 'Sabão', 3.00, 'Limpa fácil', 2.50, 'Salgadinho', 1.00)

print(f'''
{produtosPreços[0]}................................R${produtosPreços[1]:.2f}
{produtosPreços[2]}.....................................R${produtosPreços[3]:.2f}
{produtosPreços[4]}...............................R${produtosPreços[5]:.2f}
{produtosPreços[6]}................................R${produtosPreços[7]:.2f}
''')