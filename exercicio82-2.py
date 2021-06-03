lista = [] #* lista de valores.
pares = [] #* lista de valores pares.
impares = [] #* lista de valores impares.

while True:
    resp = " "
    lista.append(int(input("Adicione um numero na lista: ")))

    while resp not in "SN":
        resp = str(input('[S/N]: ')).strip().upper()[0]
    if resp == "N":
        break

#* Aqui teremos um for que fará... Para cada ele mento da lista ele fará...

for i in lista:
    if i % 2 == 0: #* Se o elemento(i), sua divisão inteira(%) for igual a zero...
        pares.append(i)
    #* se não..
    else:
        impares.append(i)

print("=" * 50)
print(f"A lista principal {lista}")
print(f"Lista com numero pares {pares}")
print(f'Lista com numero impares {impares}')
