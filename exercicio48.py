#Aqui temos um acumulador que vai
#ter a vai servir para acumular os
#valores e somalos
soma = 0

#Aqui o for ira fazer os loops retrindingo
#entre 1 e 501, ele ira pular de dois em
#dois assim pegando os nemeros impares em
#seguencia.

for i in range(1,501,2):
    #aqui o if ira verificar se o numero é multiplo de 3
    #e ira pegar o acumulador e somar com a variavel de
    #controle
    if i % 3 == 0:
        soma += i
#aqui o print ira imprimir o resultado da soma,
#fora do escopo do if e do for,se ele estiver
#dentro desses escopos ira mostrar todos os
#numeros em seguencia somando todos.
print("O valor da soma será {}.".format(soma))