number = int(input('digite um numero: '.capitalize()))
uni = number // 1 % 10
dez = number // 10 % 10
cen = number // 100 % 10
mil = number // 1000 % 10
print('o numero {} tem\n{} unidade;\n{} dezenas;\n{} centenas;\n milhares {}'.capitalize().format(number,uni,dez,cen,mil,))