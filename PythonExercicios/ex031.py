distancia = float(input('Qual a distância da sua viagem?: '))
print('Você está prestes a começar uma viagem de {} km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.5
else:
    preço = distancia * 0.45
print('O preço da passagem será de R${:.2f}.'.format(preço))