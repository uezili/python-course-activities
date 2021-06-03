from math import hypot
co = float(input('Qual o cateto oposto do triângulo: '))
ca = float(input('Agora, qual o cateto adjacente do triângulo: '))
print('O CO e CA são {} e {}, sua Hipotenusa é {:.2f}'.format(co,ca,(hypot(co,ca))))