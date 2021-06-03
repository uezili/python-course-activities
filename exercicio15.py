km = float(input('Quantos Km foram pecorrido com o carro? '))
dias = int(input('Quantos dias ficou com o carro?'))
aluguel = 60 * dias + km * 0.15
print('O dias e quilometors foram de {} dias e {:.2f}km,\no aluguem do carro será de R${:.2f}!'.format(dias,km,aluguel))