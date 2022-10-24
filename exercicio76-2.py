"""
/tupla onde irá os produtos da listForSam de compras
"""
produtosPreços = ('Detergente', 2.00, 'Sabão', 3.00, 'Limpa fácil', 2.50, 'Salgadinho', 1.00)
"""
/loop onde ira receber uma liitura da tupla com a função len
"""
for i in range(0, len(produtosPreços)):
    if i % 2 == 0: #*se os numero das posições forem par ele mostrara a esquerda
        print(f'{produtosPreços[i]:.<30}',end=" ")#//Aqui temmos um testo com 30 caraquiteres
                                                  #//com pontos (.)
    else: #>se não, ele mostrara os itens com posições impares a diretia
        print(f'R${produtosPreços[i]:.2f}')