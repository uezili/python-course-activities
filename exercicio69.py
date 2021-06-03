idade = mais18 = quatidadeHomens = mulheresMesnos20 = 0

while True:
    idade = int(input("Qual sua idade: "))
    sexo = opç = ' '
    while sexo not in "MF":
        sexo = str(input("Qual seu sexo [M/F]: ")).strip().upper()[0]
    if idade > 18:
        mais18 += 1
    if sexo == "M":
        quatidadeHomens += 1
    if sexo == "F":
        if idade < 18:
            mulheresMesnos20 += 1

    while opç not in "SN":
        opç = str(input("Que cintinuar[S/N]: ")).strip().upper()[0]
    if opç == "S":
        continue
    if opç == "N":
        break
print(f"""A quantidade de pessoas cadastradas com mais de 18
anos é {mais18} pessoas,fora cadastrados {quatidadeHomens} homens
e foram cadastradas {mulheresMesnos20} mulheres com menos de 18 anos""")