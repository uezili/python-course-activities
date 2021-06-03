not1 = float(input("Primeira nota: "))
not2 = float(input("Segunda nota: "))

media = (not1 + not2) / 2

if media < 5:
    print("Você foi REPROVADO. nota: {}.".format(media))

elif media >= 7:
    print("Você foi APROVADO. Nota: {}.".format(media))

elif media > 5 or media <= 6.9:
    print("Você está de RECUPERAÇÂO. nota: {}.".format(media))
