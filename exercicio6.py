from math import pow
from random import randint

n = randint(0,100)
print("o dobro de {} é {}, seu triplo é {} e sia raiz quadrada {:.2}".capitalize().format(n, n*2,n*3,pow(n, 1/2)))
