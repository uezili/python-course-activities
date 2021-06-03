
#>Aqui pegamos o tamanho da sequencia
sequencia = int(input("Qual o tamanho da sequencia que quer mostrar: "))
i = 1 #>variavel de controle
termo1 = 0
termo2 = 1
"""
*Nessa parte ele mostrará o primeiro termo1.
"""
print("{}".format(termo1),end=" -> ")

while i < sequencia: #>Aqui ele fará o loop de do tamanho solicitado.
    i += 1
    total = termo2 + termo1 #>Aqui serão somado os dois primeiro termos
    termo2 = termo1 #>Nessa parte ele vai pegar o termo2 e receber o termo1
    termo1 = total #>Aqui pegará o total e  colocará no termo1
    print(total, end=" -> ")#>Mostrará ate o tamanho solicitado e continuar o loop
print("Acabou!")