#aqui pegamos o primrito termo que será base da PA
#e também sau razão para que seja feita o calculo
t = int(input("Priemiro termo: "))
r = int(input("Ração: "))
#aqui teremos um laço que começará do 1 e irá ate o 11
#e fará, o uso da formula da PA e mostrará o sua progração 
if r != 0:
    print("A progressão aritimetica do termo {} e da razão {} é: ".format(t,r))
    for i in range(1,11):
        s = t + (i - 1) * r
        print(s, end = "-> ")
else:
        print("Não podemos fazer essa PA, pois não existe razão igual a 0!")