salario = float(input('Qual o salário atual do funcionário: R$'))
if salario <= 1250:
    novosalario = salario + (salario * 15/100)
else:
    novosalario = salario + (salario * 10 / 100)
print('O funcionário que ganhava R${:.2f} passa agora a receber R${:.2f}.'.format(salario , novosalario))