
#>Exercício Python 078:
"""
/Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
/No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas
/posições na lista.
"""
valores = list()#*lista fazia para os valores

for i in range(0, 5):#*aqui temos onde iremos pegar os valores com append
    valores.append(int(input(f"Digite um numero {i}: ")))

mai = max(valores)#*Aqui pegaremos o maior valor da lista
men = min(valores)#*Aqui pegaremos o menor valor da lista

print(f"Os valores da lista são {valores}")
print(f"O maior valor é {mai} na posição", end=" ")
"""
/Nessa parte temos um loop com um enumerate para pegar as posições dos valores
/com a variavel "posições" .
"""
for posição, c in enumerate(valores):
    """
    /Aqui ele ira verificar se o conteudo da lista que vai ser colocado na variavel
    /"c" é igual ao maior numero, se for ele irá mostrar suas posições.
    """
    if c == mai:
        print(f"{posição}...")
print(f"O menor valor é {men} na posição", end=" ")
"""
/Aqui ele irá fazera mesma coisa do loop acima.
"""
for posição, c in enumerate(valores):
    """
    /Aqui no caso ele irá verificar se contouda da variável de controle "c" é igual
    /ao menor, se for igual ele ira mostrar suas posições
    """
    if c == men:
        print(f"{posição}...", end=" ")
print()