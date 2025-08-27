salario = float(input('Qual o salário atual do funcionário?: R$'))
print('O novo salário com aumento de 15% será de R${:.2f}.'.format(salario + (salario*15/100)))