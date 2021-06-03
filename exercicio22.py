name = str(input("Digite seu nome: ").strip().lower())

lista = name.split()

print("seu nome completo em maiusculo é {}".capitalize().format(name.upper()))
print("-" * 12)
print("seu nome completo em menusculo é {}".capitalize().format(name.lower().title()))
print("-" * 12)
print("seu nome tem {} letras".capitalize().format(len(name) - name.count(" ")))
print("-" * 12)
print("seu primerio nome é {} e tem {} letras".capitalize().format(lista[0].title(), len(lista[0])))
print("-" * 12)
print("seu nome tem {} vogais".capitalize().format(name.count("a") + name.count("e") + name.count("i") + name.count("o") + name.count("u")))