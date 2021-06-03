#1.Pegar as informações de velocidade 

x = float(input("Qual á sua velocidade?"))

#2.Se ele não passar responder isso...
if x <= 80:
    print("Tenha um bom dia!!")
#3.Se ele passar mostrar isso...
else:
    print("Você exedeu a velocidade exigida!\nTera que pagar R${:.2f} de multa!".format(7 * (x - 80)))
