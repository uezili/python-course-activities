name = str(input('Qual seu nome: ').strip())
list = name.split(" ")
print('Muito prazer em conhecelo {}'.format(list[0]))
print('Seu primerio nome é {}\n e seu ultimo nome é {}'.format(list[0],list[-1]))