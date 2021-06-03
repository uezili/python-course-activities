from math import sin,cos,tan,radians

ang = float(input('Digite o valor do angulo: '))

print('O angulo {} no eixo dos Cossenos {:.2f}'.format(ang,cos(radians(ang))))
print('O mesmo valor no eixo dos Senos é {:.2f}'.format(sin(radians(ang))))
print('E esse mesmo valor como tangente é {:.2f}'.format(tan(radians(ang))))