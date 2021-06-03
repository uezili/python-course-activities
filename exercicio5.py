from random import randint

nu = randint(0,100)
print("processando a resposta...".capitalize())
print("o sucessor de {} é {} e o sei antecessor é {}".capitalize().format(nu,nu+1,nu-1))