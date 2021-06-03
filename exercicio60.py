#pegr os dados
n = int(input("Digite o numero a ser fatorado: "))
i = n #contador que vai reber o numero digatado.
f = 1 #aqui receberá um, pois o fatorial termina com o fator 1.

print("{}! = ".format(n),end=" ") #aqui mostrara o numero para aparecer na tela sem quebra de linha.

while i > 1: #aqui temos um loop que em ENQUANTO o i for maior que 1 vai ser feito que esta dentro.

    f *= i #aqui temos que o f recebe ele mesmo multiplicado por 1, assim fazendo a fatoração.
    i -= 1 #nessa parte ele ira subtrair 1 no i que serve como ingrementador
    print("{} ->".format(i),end=" ")

print(f)