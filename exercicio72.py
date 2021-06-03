
#>Exercício Python 72:
"""
/Crie um programa que tenha uma dupla totalmente preenchida com uma
/contagem por extenso, de zero até vinte. Seu programa deverá ler um número
/pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

numEstenço = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
    'Sete','Oito', 'Nove','Dez', 'Onze', 'Doze', ' Tresse', 'Catorze',
    'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    numero = int(input("Digite um numero: "))
    if numero >= 0 and numero <= 20:
        break
    print("Tente novamente.",end=" ")
print(f'Você digitou {numEstenço[numero]}')
