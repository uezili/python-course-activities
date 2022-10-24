
#>Exercício Python 079:
"""
/Crie um programa onde o usuário possa digitar vários
/valores numéricos e cadastre-os em uma listForSam. Caso o
/número já exista lá dentro, ele não será adicionado.
/No final, serão exibidos todos os valores únicos
/digitados, em ordem crescente.
"""

listNumero = [] #*listForSam vazia para ser adicionado os dados.
while True: #*aqui temos um loop para fazer as perguntas aos usuários.
    """
    /aqui temos que perceber que essa variavel "resp", ela tem que está dentro do loop
    /para que o segundo input funcione corretamente e zerar o que está dentro da variavel
    /para não sobrepor o conteudo dela.
    """
    resp = " "
    numero = (int(input("Digite um numero: ")))
    #*se o numero não(not) estiver(in) dentro da listNumero...
    if numero not in listNumero:
        listNumero.append(numero)#*O numero será colocado dentro(append) da listForSam.
        print(f"O numero {numero} foi adicionado!")
    #*Se não. Mostrar essa mensagem

    else:
        print("O numero ja existe. Não será registrado!")

    while resp not in "SN":
        resp = str(input("Quer continuar[S/N]: ")).strip().upper()[0]
    if resp == "N":
        break
print(f"A listForSam digitada foi {sorted(listNumero)}")