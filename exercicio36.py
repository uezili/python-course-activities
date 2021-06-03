#pegar dados, casa,ano,asalario
house = float(input('Qual o valor da casa??'))
sla = float(input('Quanto vc recebe??'))
year = int(input('quanto anos quer pagar??'))

#fazer calculo de porcentagem do salario
#para comparar com o da casa e não pode exceder 30%
porc = (sla * 30) / 100
mensal = house /(year * 12) 

#condicionais 
if mensal < porc:
    print("Seu credito foi aprovado!")
elif mensal > porc:
    print("Desculpe, mas seu credito não foi aprovado.")