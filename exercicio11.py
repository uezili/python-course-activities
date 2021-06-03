alt = float(input('Qual á altura da parede? '))
lar = float(input('Qual á largura da parede? '))
area = alt * lar
print('A área da parede que tem altura {}m e de largura {}m é de {}'.format(alt,lar,area))
print('A quantidade de tinda ultilizada para pintar essa parede é de {} litros '.format(area / 2)) 