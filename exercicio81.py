
#>Exercício Python 081:
"""
/Crie um programa que vai ler vários números e colocar em uma listForSam. Depois disso, mostre:
/A) Quantos números foram digitados.
/B) A listForSam de valores, ordenada de forma decrescente.
/C) Se o valor 5 foi digitado e está ou não na listForSam.
"""

listNumero = list() #> Lista onde ficaram os numero.

while True:
    resp = ' '
    listNumero.append(int(input("Adicione um numero a listForSam: "))) #>Aqui iremos colocalos intens na listForSam.

    while resp not in "SN":
        resp = str(input("Quer contunuar [S/N]: ")).strip().upper()[0]
    if resp == 'N':
        break

print('=' * 50)
print(f'Os numero digitados na listForSam foram {listNumero}')

print(f'A quantidade de numeros digitados foi {len(listNumero)};')
listNumero.sort(reverse=True) #> Aqui revertemos a ordem da listForSam.

print(f'A listForSam em forma decrescente {listNumero}')
if 5 not in listNumero: #> Se o numero 5 estiver, mostrar essa mensagem.
    print('O numero 5 não se encontra na listForSam.')
else: #> Se ele estiver, mostrar essa mensagem.
    print(f"O numero 5 aparece.")
