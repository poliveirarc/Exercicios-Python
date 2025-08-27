vel = float(input('Qual a velocidade do carro? (km/h): '))
if vel > 80:
    multa = (vel-80)*7
    print('MULTADO!! Você excedeu o limite de velocidade da via que é 80 km/h. ')
    print('Você deve pagar uma multa de R${:.2f}.'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')