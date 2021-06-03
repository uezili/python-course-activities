
#>Exercício Python 73:
"""
/Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
/Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
/a) Os 5 primeiros times.
/b) Os últimos 4 colocados.
/c) Times em ordem alfabética.
/d) Em que posição está o time da Flamengo.
"""

times = ('Palmeiras', 'Grêmio', 'Sport', 'Internascional', 'Atlético-PR', 'Ceará', 'Bahia', 'Fortaleza',
    'Santos', 'Atlético-GO', 'Vasco da Gama', 'Curitiba', 'Flamengo','Fluminense', 'Aletico-MG', 'Corinthians',
    'Botafogo', 'São Paulo', 'Goiás')

print("=" * 20)
print(f'''
Os 5 primeiros colocados da tabela:
{times[0:5]}''')
print("=" * 20)
print(f'''
Os 4 últimos colocados da tabela:
{times[-4:]}''')
print("=" * 20)
print(f'''
Os times por ordem alfabética:
{sorted(times)}''')
print("=" * 20)
print(f'''
A colocação do flamengo é:
{times.index('Flamengo') + 1}''')