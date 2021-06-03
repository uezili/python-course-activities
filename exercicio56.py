mediaIdade = 0 
soma = 0
maisVelho = ""
idadeMaiorMas = 0 
mulheresMenor = 0

for p in range(1,5):
    print("****** {}º Pesoa ******".format(p))
    nome = str(input("Nome: ".capitalize()).strip)
    idade = int(input("idade: "))
    sexo = str(input("Sexo [M/F]: "))
    soma += idade

    if sexo in "Mm" and idade > idadeMaiorMas:
        idadeMaiorMas = idade
        maisVelho = nome
    if sexo in "Ff" and idade < 20:
        mulheresMenor += 1

mediaIdade = soma / 4 

print("A media da idade das 4 pessoas é {}.".format(mediaIdade))
print("O home mais velho se chama {} e sua idade é de {} anos.".format(maisVelho,idadeMaiorMas))
print('Nesse grupo existem {} mulheres menores de idade.'.format(mulheresMenor))