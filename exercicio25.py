name = str(input("Digite seu nome: "))
nome = name.title().split(" ")
print("Seu nome tem Silva? {}".format("Silva" in nome))