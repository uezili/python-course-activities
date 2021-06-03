
#>Exercício Python 083:
"""
/Crie um programa onde o usuário digite uma expressão
/qualquer que use parênteses. Seu aplicativo deverá analisar
/se a expressão passada está com os parênteses abertos e
/fechados na ordem correta.
"""
expr = str(input('Digite a expressão:'))
lista = list() #* lista onde será colocado os parenteses da expressão

#* Para cada elemente(i) da expressão ele falará...
for i in expr:
    #* Se o elemento(i) for igual a um "(" ele adcionara na lista.
    if i == '(':
        lista.append(i)
    #* Se for um ")" ele apagará o ultimo elemento da lista, pois o parentese vai ter encontrado seu par
    elif i == ')':
        lista.pop()

#* Se o numero de itens na lista for igual a zero,ele fará...
if len(lista) == 0:
    print("Sua expressão está correta!")
#* Se não for igual a zero, ele falará...
else:
    print("Sua expressão está errada!")