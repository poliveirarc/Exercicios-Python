peso = float(input('Qual seu peso? (kg): '))
altura = float(input('Qual sua altura? (m): '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('Você está NO SEU PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA!')
