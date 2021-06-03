brasil = list()
estado = dict()
for i in range(0, 1):
    estado['uf'] = str(input("Unidade federativa: "))
    estado['sigla'] = str(input("Sigla: "))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(f"O {v}")