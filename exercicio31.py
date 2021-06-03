#pegar informação da viagem

km = float(input("De quantos Km é sua viagem? "))

#Analize da viagem 

if km < 200:
    print("Sua viagem ira custar R${:.2f}".format(km * 0.50))
else:
    print("sua viagem ira custar R${:.2f}".format(km * 0.45))