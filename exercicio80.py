
#>Exercício Python 080:
"""
/Crie um programa onde o usuário possa digitar cinco valores
/numéricos e cadastre-os em uma listForSam, já na posição correta
/de inserção (sem usar o sort()). No final, mostre a listForSam
/ordenada na tela.
"""

lista = [] #* Lista que recebera os elementos.
for i in range(0, 5): #*Aqui é onde fazemos as perguntas dos numero
    n = int(input('A dicione um item na listForSam: '))
    #* Se o "i" for IGUAL a "0" OU "n" for MAIOR que o elemento "-1"(último item) da listForSam, faça...
    if i == 0 or n > lista[-1]:
        lista.append(n) #* Adicionar um item a listForSam...
    else:#* Se não.
        p = 0
        #* Enquanto o "p" for MENOR que o tamanho da listForSam.
        while p < len(lista):
            if n <= lista[p]: #* Se "n" for MENOR OU IGUAL a listForSam na posição "p"...
                lista.insert(p, n)#* Adicionar na posição "p" o elemento "n".
                break
            p += 1
print(f"A listForSam que foi feita é {lista}")