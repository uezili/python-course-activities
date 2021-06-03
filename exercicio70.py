mais1000 = total = c = 0
nomeMBarato = " "

while True:
    produto = str(input("Qual o nome do produto: ")).strip()
    valor = float(input("Qual o valor do produto: "))
    total += valor
    resp = " "
    proMBarato = 0
    c += 1

    if valor > 1000:
        mais1000 += 1
    else:
        if valor < proMBarato:
            proMBarato = valor
            nomeMBarato = produto

    if proMBarato < valor:
        nomeMBarato = produto
        proMBarato = valor

    if c == 1:
        nomeMBarato = produto


    while resp not in "SN":
        resp = str(input("Quer continuar[S/N]? ")).strip().upper()[0]

    if resp == "N":
        break
print("=" * 30)
print(f"""Valor total da compra é R$ {total:.2f}
Os produtos comprados acima de 1000 reais são {mais1000}
O produto mais barato é {nomeMBarato} e custa {proMBarato:.2f} reais.""")
print("=" * 30)
