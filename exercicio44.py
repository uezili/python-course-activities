pro = float(input("Qual o valor do prooduto? R$"))
print("""Formas de pragamento:
1.A vista com 10% de desconto.
2.A vista no cartão com 5% de desconto.
3.Parcelado em ate 2x.
4.Pacerlado em ate 3x.
""")
print("Qual opção deseja pagar:")
opc = int(input())

vst = pro - ((pro * 10) / 100) #desconto a vista de 10%
vstc = pro - ((pro * 5) / 100) #desconto com o cartão de 5%

if opc == 1:
    print("Sua compra de R${:.2f}, vai custar {:.2f}.".format(pro, vst))

elif opc == 2:
    print("Sua compra de R${:.2f}, vai custar R${:.2f}.".format(pro,vstc))

elif opc == 3:
    print("Sua compra de R${:.2f}, vai ficar com parcelas de R${:.2f}, sem juros.".format(pro,pro / 2))

elif opc == 4:
    parcelas = int(input("Quantas parcelas?\n"))
    juros = pro + ((pro * 20) / 100)
    total = juros / parcelas
    print("Sua compra de R${:.2f},\nem {}x parcelas ira custar R${:.2f}, com juros ficará {:.2f}.".format(pro,parcelas,pro / parcelas,total))

else:
    print("Opção não existente! Tente novamente.")