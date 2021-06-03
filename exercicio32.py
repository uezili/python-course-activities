#pegar o ano

print("Qual ano quer saber ?")
ano = int(input())

#fazer analize pegando o ano e dividindo por 4 e 100 ou 400;
#isso ira verificar se ele é multiplo de 100 que não é divisivel por 400;
#isso se dara que o resto da divisão não é 0  o ano não será bissexto

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('É um ano Bissexto!')
else:
    print("Não é Bissexto")