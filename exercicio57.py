sexo = str(input("qual seu sexo [M/F]: ").strip()).upper()[0]
while sexo not in 'FM':
      sexo = str(input("valor não aceito. Qual seu sexo [M/F]:")).strip().upper()[0]

print("Seu sexo foi lido({}).".format((sexo)))

