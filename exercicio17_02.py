co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Agora, o valor do cateto adejacente:'))
hi = (ca ** 2) + (co ** 2)
print("Os catetos {} e {}, tem uma hipotenusa de {:.2f}".format(ca,co,hi ** (1/2)))