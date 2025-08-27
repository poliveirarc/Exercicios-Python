l = float(input('Qual a largura da parede em metros: '))
h = float(input('Qual a altura da parede em metros: '))
print ('Sua parede tem {} x {}, o que equivale a {}m² \n Para pintá-la, você precisará de {} litros de tinta.'.format(l, h, l*h, (l*h)/2) )