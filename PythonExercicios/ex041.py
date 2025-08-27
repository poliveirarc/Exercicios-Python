from datetime import datetime
nasc = int(input('Ano de nascimento: '))
idade = datetime.now().year - nasc
if idade <= 9:
    categoria ='MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print('Quem nasceu em {} tem hoje {} anos'.format(nasc, idade))
print('Sua categoria é {}.'.format(categoria))
