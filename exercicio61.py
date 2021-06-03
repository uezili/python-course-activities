print("\nVamos fazer algumas Proegeções Aritimeticas.\n")
termo = int(input("Primeiro termo: "))
rasão = int(input("Rasão a ser seguida: "))
i = 0

if rasão != 0:

    print("A PA do numero {} com a rasão {} é a segunte:".format(termo, rasão))

    while i < 10:
        i += 1
        s = termo + (i - 1) * rasão
        print(s,end=" -> ")

        if i == 10:
            print('Acabou!')
else:

    print("Não podemos fazer essa PA, pois não existe rasão igual a zero.")
    print('Tente novamente:\n')

    termo = int(input("Primeiro termo: "))
    rasão = int(input("Rasão a ser seguida: "))

    while i < 10:
        i += 1
        s = termo + (i - 1) * rasão
        print(s, end=" -> ")
        if i == 10:
            print("Acabou!")