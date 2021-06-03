print("=-" * 16)
print("Vamos princar um pouco com PAs:")
print("=-" * 16,"\n")

termo = int(input("Digite o primeiro termo:"))
rasão = int(input("e a rasão:"))
i = 0
if rasão == 0:
    print("Não podemos fazer essa PA pois não existe Rasão igual a zero")

while i < 10:
    i += 1
    s = termo + (i - 1) * rasão
    print(s, end=" -> ")

    if i == 10:
        print("Acabou!")

print("""\n
Deseja ver mais termos? Então escolha uma das opções:
1.Deseja ver mais termos;
2.Quero ver outra PA;
0.Sair.\n""")

opç = int(input("--> "))

if opç == 1:

    limite = int(input("Qual o tamnho dos termos que quer ver: "))
    limite += i

    while i < limite:
        i =+ 1
        s = termo + (i - 1) * rasão
        print(s, end=" -> ")

if opç == 2:
    termo = int(input("Digite o primeiro termo:"))
    rasão = int(input("e a rasão:"))

    if rasão == 0:
        print("Não podemos fazer essa PA pois não existe Rasão igual a zero")

    while i < 10:
        s = termo + (i - 1) * 10
        i += 1
        print(s, end=" -> ")

if opç == 0:
    print("Ate depois então")