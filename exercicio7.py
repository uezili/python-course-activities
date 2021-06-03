from random import uniform

n1 = uniform(0,10)
n2 = uniform(0,10)
n3 = uniform(0,10)
n4 = uniform(0,10)
print("tirando a média de {:.2f}, {:.2f}, {:.2} e {:.2}...".capitalize().format(n1,n2,n3,n4))
media = (n1 + n2 + n3 + n4)/ 2
print('a media das notas {:.2}, {:.2}, {:.2} e {:2} é {:.2}'.capitalize().format(n1,n2,n3,n4,media))