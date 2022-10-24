#>Exercício Python 077:

"""
/Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
/Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

p = ('Exercicio', 'Python', 'Crie', 'programa', 'tenha', 'tupla', 'com', 'disso','deve', 'mostrar', 'cada', 'quais', 'suas', 'vogais')
print('Vamos ver quais palavras e suas vogais existentes!')
for palavras in p: #>aqui, para cada posição(Palavras) da tupla "p" ele irá mostrar a palavra
                    #>da posição do jeito que está formatado a baixo
    print(f"\nAs vogais da palavra {palavras} ", end=" ")
    for vogais in palavras: #>Esse loop irá verificar as palavras com a variavel de contro(vogais)
        if vogais.lower() in "aeiou": #>Aqui irá verificar se tem "AEIOU"
            print(vogais, end=" ") #*Aqui ele mostra as letra que estiverem na condição

print("\n")
