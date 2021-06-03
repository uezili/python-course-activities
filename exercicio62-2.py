print("=-" * 16)
print("Vamos brincar um pouco com PAs:")
print("=-" * 16,"\n")

termo = int(input("Qual o primeiro termo: "))
razão = int(input("Qual a razão:"))
i = 0
limite = 10
total = 0

if razão == 0:
    print("Não podemos fazer essa PA pois não existe razão igual a zero.")

while limite != 0:
    total += limite
    while i < total:
        i += 1
        s = termo + (i - 1) * razão
        print(s, end=" -> ")
    print("Pausa")
    limite = int(input("Deseja ver mais? quantos agora?"))

if limite == 0:
    print("O total de temos foi {}.".format(total))
    print("Ate mais!")