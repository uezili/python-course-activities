#pegar o salario 
sala = float(input("Qual seu salario? "))

#fazer o calculo de porcentagem de 15% caso seja menor que 1250
if sala <= 1250:
    print("Seu acrecimo de 15%, ficando com salario de R${:.2f}".format((sala * 15) / 100 + sala))

#fazer calculo de 10% caso seja acima do teto do salario 
else:
    print("Seu acrescimo de 10%, ficara com salario de R${:.2f}".format((sala * 10) / 100 + sala))